from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
from api_service.app.container.container import container
from api_service.app.config.config import FILE_PATH_UPLOAD_TMP, FILE_PATH_DOWNLOAD_TMP

router_file = APIRouter()


@router_file.post("/save_file")
async def create_file(file: UploadFile = File(...),
                      service=Depends(container.get_service)):
    try:
        resp = await service.insert_file(file=file)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"error: {ex}")
    return JSONResponse({"response": resp})


@router_file.get("/get_file")
async def get_file(filename: str,
                   service=Depends(container.get_service)):
    try:
        file = await service.get_file(object_name=filename)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"error: {ex}")
    return FileResponse(FILE_PATH_DOWNLOAD_TMP + filename, media_type=file.content_type, filename=filename)


# @router_file.get("/get_list_files")
# async def get_list_files():
#     pass


@router_file.delete("/delete_dile")
async def delete_file():
    pass


@router_file.put("/update_file")
async def update_file():
    pass
