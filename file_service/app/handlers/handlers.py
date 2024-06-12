from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse, FileResponse
import aiofiles
from app.container.container import container
from app.config.config import FILE_PATH_UPLOAD_TMP


router_file = APIRouter()

async def get_body(request: Request):
    return await request.form()

@router_file.post("/save_file")
async def create_file(request: Request,
                      container=Depends(container.get_repository)):
    
    f = await request.form()
    filename = f.get("file").filename
    file_path = FILE_PATH_UPLOAD_TMP + filename
    print(type(f.get("file")))
    print(f.get("file"))

    async with aiofiles.open(file_path, 'wb') as afp:
        data = await f.get("file").read()
        await afp.write(data)
    
    res = await container.create(file_name=filename, file_path=file_path)

    return JSONResponse({"resp": res})


@router_file.get("/get_file")
async def get_file(filename: str):
    pass


@router_file.put("/update_file")
async def update_file():
    pass


@router_file.delete("/delete_dile")
async def delete_file():
    pass
