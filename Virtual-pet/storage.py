import json
import os
from models import Pet

DEFAULT_STATE_PATH = "pet_state.json"

class PetStore:
    def __init__(self, path: str = DEFAULT_STATE_PATH):
        self.path = path

    def save(self, pet: Pet) -> bool:
        try:
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(pet.to_dict(), f, ensure_ascii=False, indent=2)
            return True
        except OSError as e:
            print(f"[Error] บันทึกข้อมูลไม่สำเร็จ: {e}")
            return False

    def load(self, default_name: str = "Mochi") -> Pet:
        if not os.path.exists(self.path):
            print(f"[Info] ไม่พบไฟล์ข้อมูลเดิม กำลังสร้างสัตว์เลี้ยงใหม่ชื่อ '{default_name}'")
            return Pet(name=default_name)

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
            pet = Pet.from_dict(data)
            pet.apply_decay()  # คำนวณค่า decay ทันทีที่โหลดไฟล์
            return pet
        except (OSError, json.JSONDecodeError) as e:
            print(f"[Error] ไฟล์ข้อมูลเสียหาย ({e}) กำลังสร้างสัตว์เลี้ยงใหม่")
            return Pet(name=default_name)