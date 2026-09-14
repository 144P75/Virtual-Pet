# 🐾 Virtual Pet Companion (CLI)

ระบบจำลองการดูแลสัตว์เลี้ยงเสมือนจริง พัฒนาในรูปแบบ Command Line Interface (CLI) ด้วยภาษา Python โดยประยุกต์ใช้หลักการเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming - OOP), การบันทึกข้อมูลยั่งยืนลงไฟล์ JSON, การดึงข้อมูลจาก External API (Dog API / Cat Facts API) และการจัดโครงสร้างโค้ดแบบแยกชั้น (Modular Architecture)

---
## 🎯 วัตถุประสงค์ของโครงการ (Project Objectives)

1. **การบูรณาการหลักการ OOP & Modular Architecture:** ประยุกต์ใช้การเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming) ร่วมกับการจัดโครงสร้างโปรแกรมแบบโมดูลที่มีการแบ่งแยกหน้าที่อย่างชัดเจน (Separation of Concerns) แบ่งออกเป็น Presentation, Business Logic และ Data Access Layer
2. **การจัดการข้อมูลยั่งยืน (Data Persistence):** พัฒนากลไกการอ่านและบันทึกสถานะของสัตว์เลี้ยงลงในไฟล์ JSON เพื่อให้ข้อมูลคงอยู่ระหว่างการเปิด-ปิดใช้งานโปรแกรม
3. **การประมวลผลข้อมูลและการคำนวณตามเวลา (Data Processing & Decay System):** พัฒนาอัลกอริทึมคำนวณส่วนต่างของเวลา (Timestamp) เพื่อหักลบค่าสถานะ (Decay Over Time) อัตโนมัติ รวมถึงการกรอง ค้นหา และเรียงลำดับข้อมูลสถานะ
4. **การเชื่อมต่อ API ภายนอก (External API Integration):** ดึงข้อมูลแบบเรียลไทม์จาก Dog API หรือ Cat Facts API มาสร้างปฏิสัมพันธ์ (Interactions) สุ่มรูปภาพและเกร็ดความรู้ให้กับผู้ใช้
5. **ความทนทานต่อข้อผิดพลาดและการจัดการ Edge Cases (Error Resilience):** ออกแบบระบบตรวจสอบความถูกต้องของข้อมูลนำเข้า (Input Validation) และการดักจับ Exception (Exception Handling) เพื่อป้องกันไม่ให้โปรแกรมพังเมื่อผู้ใช้กรอกข้อมูลผิดพลาด
6. **การพัฒนาแบบ Iterative & DevOps Standards:** ดำเนินงานตามกระบวนการ Agile/Sprint จัดทำชุดทดสอบอัตโนมัติ (Automated Testing) และตั้งค่า CI/CD Pipeline ผ่าน GitHub Actions รวมกับแนวคิด AI Integration

---

## สถาปัตยกรรมระบบ (Architectural Scope)
โปรเจกต์นี้ถูกออกแบบโดยแบ่งหน้าที่การทำงานอย่างชัดเจน (Separation of Concerns) ออกเป็น 3 ชั้นหลัก:
1. **Presentation Layer:** ส่วนจัดการ CLI, การแสดงผลหน้าจอ/เมนูหลัก และรับอินพุตพร้อมตรวจสอบความถูกต้อง (Input Validation)
2. **Business Logic Layer:** ส่วนประมวลผลคำนวณสถานะสัตว์เลี้ยง (Hunger, Energy), การคำนวณ Decay Over Time และการประเมินอารมณ์ (MoodTracker)
3. **Data Access Layer:** ส่วนการอ่านและบันทึกข้อมูลสถานะลงในไฟล์ `pet_state.json` (Data Persistence)

---

## สมาชิกในทีมและหน้าที่ความรับผิดชอบ (Team Roles)

| ชื่อ-นามสกุล | รหัสนักศึกษา | บทบาทหลัก (Role) | หน้าที่และความรับผิดชอบ |
| :--- | :--- | :--- |:--- |
| **นางสาวพิชยา สิทธิพันธ์** | **673380596-5** | **Planner** | • วางแผนและนิยามสเปกต์ระบบในเอกสาร `PLAN.md`<br>• กำหนด Definition of Done (DoD)<br>• ควบคุมภาพรวมสถาปัตยกรรมและการส่งมอบงาน |
| **นางสาวมุกดา บุญประจันทร์** | **673380598-1** | **Coder** | • เขียนโค้ดระบบ CLI, ควบคุม Control Flow และ Menu Loop<br>• พัฒนาโครงสร้าง Class ตามแนวคิด OOP (`Pet`, `MoodTracker`, `Interaction`) |
| **นางสาวพรีมภัทร ภาวัฒนวคุณ** | **673380594-9** | **Debugger** | • ออกแบบและทำการทดสอบเคสขอบเขต (Edge Case Testing)<br>• ตรวจสอบ Exception Handling และ Input Sanitization<br>• สรุปรายงาน QA และจัดการ Pull Request (PR) บน GitHub |

*(หมายเหตุ: บทบาทหน้าที่อาจมีการหมุนเวียนกันตามข้อกำหนดในแต่ละ Sprint)*

---

## โครงสร้างเอกสารโครงการ (Documentation Structure)
* **`README.md`** - เอกสารอธิบายภาพรวมโครงการ สถาปัตยกรรม และบทบาทของสมาชิกในทีม
* **`ALL_SPRINTS.md`** - เอกสารสรุปรายละเอียด ความก้าวหน้า และผลการทดสอบของทุก Sprint
* **`PLAN.md`** - เอกสารวางแผนงาน นิยามขอบเขต และ Definition of Done (DoD) ประจำสัปดาห์
