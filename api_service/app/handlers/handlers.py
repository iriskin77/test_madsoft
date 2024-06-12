from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse
from app.container.container import container


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
async def get_file(filename: str):
    pass


@router_file.get("/get_list_files")
async def get_list_files():
    pass


@router_file.delete("/delete_dile")
async def delete_file():
    pass


@router_file.put("/update_file")
async def update_file():
    pass
