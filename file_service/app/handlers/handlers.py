from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse, FileResponse


router_file = APIRouter()


@router_file.post("/save_file")
async def create_file():
    print("file saved")


@router_file.get("/get_file")
async def get_file(filename: str):
    pass


@router_file.put("/update_file")
async def update_file():
    pass


@router_file.delete("/delete_dile")
async def delete_file():
    pass
