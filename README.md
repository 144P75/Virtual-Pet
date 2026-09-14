# 🐾 Virtual Pet Companion (CLI)

ระบบจำลองการดูแลสัตว์เลี้ยงเสมือนจริง พัฒนาในรูปแบบ Command Line Interface (CLI) ด้วยภาษา Python โดยประยุกต์ใช้หลักการเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming - OOP), การบันทึกข้อมูลยั่งยืนลงไฟล์ JSON, การดึงข้อมูลจาก External API (Dog API / Cat Facts API) และการจัดโครงสร้างโค้ดแบบแยกชั้น (Modular Architecture)

---

## สถาปัตยกรรมระบบ (Architectural Scope)
โปรเจกต์นี้ถูกออกแบบโดยแบ่งหน้าที่การทำงานอย่างชัดเจน (Separation of Concerns) ออกเป็น 3 ชั้นหลัก:
1. **Presentation Layer:** ส่วนจัดการ CLI, การแสดงผลหน้าจอ/เมนูหลัก และรับอินพุตพร้อมตรวจสอบความถูกต้อง (Input Validation)
2. **Business Logic Layer:** ส่วนประมวลผลคำนวณสถานะสัตว์เลี้ยง (Hunger, Energy), การคำนวณ Decay Over Time และการประเมินอารมณ์ (MoodTracker)
3. **Data Access Layer:** ส่วนการอ่านและบันทึกข้อมูลสถานะลงในไฟล์ `pet_state.json` (Data Persistence)

---

## สมาชิกในทีมและหน้าที่ความรับผิดชอบ (Team Roles)

| ชื่อ-นามสกุล / รหัสนักศึกษา | บทบาทหลัก (Role) | หน้าที่และความรับผิดชอบ |
| :--- | :--- | :--- |
| **นางสาวพิชยา สิทธิพันธ์** | **Planner** | • วางแผนและนิยามสเปกต์ระบบในเอกสาร `PLAN.md`<br>• กำหนด Definition of Done (DoD)<br>• ควบคุมภาพรวมสถาปัตยกรรมและการส่งมอบงาน |
| **นางสาวมุกดา บุญประจันทร์** | **Coder** | • เขียนโค้ดระบบ CLI, ควบคุม Control Flow และ Menu Loop<br>• พัฒนาโครงสร้าง Class ตามแนวคิด OOP (`Pet`, `MoodTracker`, `Interaction`) |
| **นางสาวพรีมภัทร ภาวัฒนวคุณ** | **Debugger** | • ออกแบบและทำการทดสอบเคสขอบเขต (Edge Case Testing)<br>• ตรวจสอบ Exception Handling และ Input Sanitization<br>• สรุปรายงาน QA และจัดการ Pull Request (PR) บน GitHub |

*(หมายเหตุ: บทบาทหน้าที่อาจมีการหมุนเวียนกันตามข้อกำหนดในแต่ละ Sprint)*

---

## โครงสร้างเอกสารโครงการ (Documentation Structure)
* **`README.md`** - เอกสารอธิบายภาพรวมโครงการ สถาปัตยกรรม และบทบาทของสมาชิกในทีม
* **`ALL_SPRINTS.md`** - เอกสารสรุปรายละเอียด ความก้าวหน้า และผลการทดสอบของทุก Sprint
* **`PLAN.md`** - เอกสารวางแผนงาน นิยามขอบเขต และ Definition of Done (DoD) ประจำสัปดาห์
