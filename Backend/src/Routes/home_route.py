from fastapi import APIRouter,File,UploadFile,HTTPException
import pandas as pd
import io
from src.Utils.ProcessXcel import processFile
 
router=APIRouter()


"""UploadFile is a special file type in FastAPI that does not provide a direct file path.
Instead, it streams the file asynchronously."""
@router.post('/upload/')
async def upload_file(file: UploadFile=File(...)):
    content=await file.read()   #contents is now in bytes 
    #xls=pd.read_excel(file) #single sheet and file is of UploadFile which returns async file obj
    xls=pd.ExcelFile(io.BytesIO(content)) #loads the entire workbook into memory once. # io.BytesIO(contents) readss byte in RAM/ memory buffer
    df=await processFile.handleFile(xls)
    return df