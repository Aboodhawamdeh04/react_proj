from fastapi import APIRouter, HTTPException
from models import Crop
from database import crops

# Use APIRouter instead of FastAPI()
router = APIRouter()

@router.get("/crops")
def get_crops(limit: int = 10, status: str = None):
    result = crops
    if status:
        result = [crop for crop in result if crop["status"].lower() == status.lower()]
    return {"crops": result[:limit]}

@router.get("/crops/{crop_id}")
def get_crop(crop_id: int):
    for crop in crops:
        if crop["id"] == crop_id:
            return crop
    raise HTTPException(status_code=404, detail="Crop not found")

@router.post("/crops")
def create_crop(crop: Crop):
    crops.append(crop.model_dump())
    return {"message": "Crop created successfully", "crop": crop}

@router.put("/crops/{crop_id}")
def update_crop(crop_id: int, updated_crop: Crop):
    for index, crop in enumerate(crops):
        if crop["id"] == crop_id:
            crops[index] = updated_crop.model_dump()
            return {"message": "Crop updated successfully", "crop": crops[index]}
    raise HTTPException(status_code=404, detail="Crop not found")

@router.delete("/crops/{crop_id}")
def delete_crop(crop_id: int):
    for index, crop in enumerate(crops):
        if crop["id"] == crop_id:
            deleted_crop = crops.pop(index)
            return {"message": "Crop deleted successfully", "crop": deleted_crop}
    raise HTTPException(status_code=404, detail="Crop not found")