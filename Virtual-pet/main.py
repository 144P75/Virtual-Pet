"""
Virtual Pet CLI Application
Presentation Layer & Main Controller
"""

import sys
from storage import PetStore
from interaction import Interaction

def display_welcome_banner() -> None:
    print("=" * 55)
    print(" 🐾 WELCOME TO VIRTUAL PET COMPANION (CLI) 🐾 ")
    print("=" * 55)

def display_menu(pet_name: str) -> None:
    print(f"\n--- เมนูหลัก [กำลังดูแล: {pet_name}] ---")
    print("[1] ดูสถานะสัตว์เลี้ยง (Check Stats)")
    print("[2] ให้อาหาร (Feed Pet)")
    print("[3] เล่นกับสัตว์เลี้ยง (Play with Pet)")
    print("[4] สุ่มรูปสุนัขน่ารัก (Random Dog Image API)")
    print("[5] สุ่มข้อความน่ารู้เกี่ยวกับแมว (Random Cat Fact API)")
    print("[6] บันทึกและออกจากโปรแกรม (Save & Exit)")
    print("-" * 35)

def get_command_input(prompt: str) -> str:
    try:
        user_input = input(prompt)
        return user_input.strip().lower()
    except (KeyboardInterrupt, EOFError):
        print("\n\nได้รับการขัดจังหวะ ปิดโปรแกรมอัตโนมัติ...")
        sys.exit(0)

def main():
    display_welcome_banner()
    
    # โหลดข้อมูลสัตว์เลี้ยงผ่าน Data Access Layer
    store = PetStore()
    pet = store.load(default_name="Mochi")
    interactor = Interaction()

    print(f"\n[System]: โหลดข้อมูลของ '{pet.name}' เรียบร้อยแล้ว!")

    is_running = True
    while is_running:
        display_menu(pet.name)
        choice = get_command_input("กรุณาเลือกคำสั่ง (1-6): ")

        if choice in ["1", "check"]:
            pet.apply_decay()
            print(f"\n📊 --- สถานะของ {pet.name} ---")
            print(f"• ความอิ่ม (Hunger)  : {pet.hunger:.1f} / 100")
            print(f"• พลังงาน (Energy)   : {pet.energy:.1f} / 100")
            print(f"• อารมณ์ (Mood)      : {pet.mood}")

        elif choice in ["2", "feed"]:
            pet.feed()
            print(f"\n🍖 ให้อาหาร {pet.name} เรียบร้อยแล้ว! (Hunger: {pet.hunger:.1f})")

        elif choice in ["3", "play"]:
            if pet.energy < 15:
                print(f"\n⚠️ {pet.name} เหนื่อยเกินไป ไร้พลังงานสำหรับเล่น (Energy: {pet.energy:.1f})")
            else:
                pet.play()
                print(f"\n🎾 เล่นกับ {pet.name} สนุกมาก! (Energy เหลือ: {pet.energy:.1f})")

        elif choice in ["4", "dog"]:
            print("\n🐶 กำลังดึงข้อมูลรูปภาพจาก Dog API...")
            res = interactor.fetch_dog_image()
            if res["ok"]:
                print(f"[Dog Image URL]: {res['detail']}")
                pet._log("dog_api", res["detail"])
            else:
                print(f"⚠️ {res['detail']}")

        elif choice in ["5", "cat"]:
            print("\n🐱 กำลังดึงเกร็ดความรู้จาก Cat Fact API...")
            res = interactor.fetch_cat_fact()
            if res["ok"]:
                print(f"[Cat Fact]: {res['detail']}")
                pet._log("cat_api", res["detail"])
            else:
                print(f"⚠️ {res['detail']}")

        elif choice in ["6", "quit", "exit"]:
            if store.save(pet):
                print(f"\n💾 บันทึกสถานะของ {pet.name} ลงไฟล์สำเร็จ!")
            print("ขอบคุณที่ใช้งาน Virtual Pet CLI! สวัสดีครับ 🐾")
            is_running = False

        else:
            print("\n⚠️ [Error]: คำสั่งไม่ถูกต้อง กรุณาเลือกตัวเลข 1-6 หรือพิมพ์คำสั่งที่กำหนด")

if __name__ == "__main__":
    main()