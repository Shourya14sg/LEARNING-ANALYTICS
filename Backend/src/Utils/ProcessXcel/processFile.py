import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from fastapi import HTTPException

async def handleFile(xls):
    try:
        df_student = pd.read_excel(xls, sheet_name="Sheet1")
        df_metric = pd.read_excel(xls, sheet_name="Sheet2")
        
        # Check if 'Metrics' column exists
        if "Metrics" not in df_metric.columns:
            raise HTTPException(status_code=400, detail="Column 'Metrics' not found in Sheet2")

        params = df_metric["Metrics"].tolist()
        df_metric.set_index('Metrics', inplace=True)

        df = df_student[["Enrollment No."] + params].copy()
        for col in params:
            df[col] = (df[col] / df_metric.loc[col]['Total']) * df_metric.loc[col]['Weight']

        # Drop ID column and scale features
        features = df.drop(columns=["Enrollment No."])
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)

        # Apply PCA (retain 95% variance or specify n_components=2 for visualization)
        pca = PCA(n_components=0.95)
        pca_features = pca.fit_transform(scaled_features)

        # KMeans clustering
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        cluster_labels = kmeans.fit_predict(pca_features)
        df_student["Cluster"] = cluster_labels

        # Silhouette score
        silhouette = silhouette_score(pca_features, cluster_labels)

        return {
            "clustering_score": float(silhouette),  # Ensure it's a native float
            "explained_variance_ratio": [float(val) for val in pca.explained_variance_ratio_],
            "n_pca_components": int(pca.n_components_),
            "clustered_data": df_student.to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")
