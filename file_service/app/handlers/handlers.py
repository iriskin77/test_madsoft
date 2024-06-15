from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse, FileResponse
import aiofiles
from file_service.app.container.container import container
from file_service.app.config.config import FILE_PATH_UPLOAD_TMP


router_file = APIRouter()


@router_file.post("/save_file")
async def create_file(request: Request,
                      repository=Depends(container.get_repository)):
    
    f = await request.form()
    filename = f.get("file").filename
    file_path = FILE_PATH_UPLOAD_TMP + filename
    print(type(f.get("file")))
    print(f.get("file"))

    async with aiofiles.open(file_path, 'wb') as afp:
        data = await f.get("file").read()
        await afp.write(data)
    
    res = await repository.create(file_name=filename)

    return JSONResponse({"resp": res})


@router_file.get("/get_file")
async def get_file(request: Request,
                   repository=Depends(container.get_repository)):

    filename = request.query_params["filename"]
    #filename = "uszips.csv"
    try:
        file = await repository.get(object_name=filename)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"database error: {ex}")
    print("handler get_file")
    return FileResponse(repository._file_path_download + file.object_name, media_type=file.content_type, filename=file.object_name)


@router_file.put("/update_file")
async def update_file():
    pass


@router_file.delete("/delete_dile")
async def delete_file():
    pass
