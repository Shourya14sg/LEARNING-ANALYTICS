import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from fastapi import HTTPException

async def handleFile(xls):
    try:
        df_student=pd.read_excel(xls,sheet_name="Sheet1")
        df_metric=pd.read_excel(xls,sheet_name="Sheet2")
        
        # Check if 'Matrics' column exists
        if "Metrics" not in df_metric.columns:
            raise HTTPException(status_code=400, detail="Column 'Metrics' not found in Sheet2")

        params=df_metric["Metrics"].tolist()
        df_metric.set_index('Metrics', inplace=True)

        df=df_student[["Enrollment No."] + params].copy()
        for col in params:
            df[col]=(df[col]/df_metric.loc[col]['Total'])*df_metric.loc[col]['Weight'] 

        features = df.drop(columns=["Enrollment No."])
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
        df_student["Cluster"] =kmeans.fit_predict(scaled_features)

    # Return JSON response
        return df_student.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching IAM details: {str(e)}")
        