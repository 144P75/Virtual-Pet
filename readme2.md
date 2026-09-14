# 🐾 Virtual Pet Companion (CLI Application)

ระบบจำลองสัตว์เลี้ยงเสมือนจริงบน Terminal/CLI พัฒนาด้วยภาษา Python ตามหลัก **Object-Oriented Programming (OOP)** และ **Modular Architecture** เพื่อรองรับการประมวลผลสถานะตามเวลาจริง (Time-based Decay), การเชื่อมต่อ External API และการทำงานร่วมกับ CI/CD Pipeline

---

## 🌟 คุณสมบัติเด่นของระบบ (Key Features)

* **Modular Architecture:** แยก Presentation Layer (`src/cli.py`) และ Business Logic (`src/pet.py`) ชัดเจน
* **OOP Design:** พัฒนาด้วย 3 คลาสหลัก ได้แก่ `Pet`, `MoodTracker` และ `Interaction`
* **Data Persistence:** บันทึกและดึงสถานะผ่านไฟล์ `pet_state.json`
* **Time-based Decay:** คำนวณความหิว พลังงาน และอารมณ์ลดลงตามเวลาจริง
* **API Integration:** ดึงข้อมูลสุ่มเกร็ดความรู้แมวจาก Cat Facts API
* **DevOps Ready:** มี CI/CD Pipeline ด้วย GitHub Actions (`pytest` & `flake8`)

---

## 🏗️ สถาปัตยกรรมระบบ (Architectural Scope)

โปรเจกต์นี้ถูกออกแบบโดยแบ่งหน้าที่การทำงานอย่างชัดเจน (Separation of Concerns) ออกเป็น 3 ชั้นหลัก:

1. **Presentation Layer (`src/cli.py`):** ส่วนจัดการ CLI, การแสดงผลหน้าจอ/เมนูหลัก และรับอินพุตพร้อมตรวจสอบความถูกต้อง (Input Validation & Sanitization)
2. **Business Logic Layer (`src/pet.py`):** ส่วนประมวลผลคำนวณสถานะสัตว์เลี้ยง (Hunger, Energy, Happiness), การคำนวณ Decay Over Time และการประเมินอารมณ์ (`MoodTracker`)
3. **Data Access Layer (`src/main.py` / `pet_state.json`):** ส่วนการอ่านและบันทึกข้อมูลสถานะลงในไฟล์ `pet_state.json` (Data Persistence)

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```text
virtual-pet-cli/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD Pipeline
├── src/
│   ├── __init__.py
│   ├── cli.py             # Presentation Layer (CLI & UI)
│   ├── pet.py             # Business Logic Layer (OOP Classes & API)
│   └── main.py            # Entry Point & Data Access Layer
├── tests/
│   ├── __init__.py
│   └── test_cli.py        # Automated Unit Tests
├── .gitignore             # Git Ignore File
├── ALL_SPRINTS.md         # สรุปผลการดำเนินงานและ QA Reports แต่ละ Sprint
├── pet_state.json         # ไฟล์บันทึกสถานะสัตว์เลี้ยง (Auto-generated)
├── README.md              # เอกสารอธิบายโปรเจกต์
└── requirements.txt       # Dependencies (requests, pytest, flake8)
```
---

## 🚀 การรันโปรแกรม (Execution)

1. **เปิด Terminal / Command Prompt** และเข้าสู่โฟลเดอร์ Root ของโปรเจกต์
2. **รันไฟล์ Main Script:**
   ```bash
   python -m src.main

---
## 👥 สมาชิกในทีม (Team Members)

| รหัสนักศึกษา | ชื่อ-นามสกุล |
| :---: | :--- |
| **673380594-9** | นางสาวพรีมภัทร ภาวัฒนวคุณ | 
| **673380596-5** | นางสาวพิชยา สิทธิพันธ์ | 
| **673380598-1** | นางสาวมุกดา บุญประจันทร์ | 


