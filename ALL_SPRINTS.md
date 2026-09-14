# 🚀 Project Sprint Lifecycle & Reports (ALL_SPRINTS.md)

เอกสารรวบรวมแผนการดำเนินงาน ผลการพัฒนา และรายงานการทดสอบระบบ (QA & Debugging Reports) สำหรับโปรเจกต์ **Virtual Pet Companion (CLI)** ครอบคลุมตั้งแต่ Sprint 1 ถึง Final Sprint 

---

## Sprint 1: Front-End App Dev & Foundation
* **ช่วงเวลา:** สัปดาห์ที่ 12 (นำเสนอ: 15 ก.ย. 2569 | ส่งงาน: 18 ก.ย. 2569)
* **เน้นจุด:** การออกแบบ UI/CLI, ระบบจัดการเมนู และการทำ Input Validation

### เป้าหมายและขอบเขต (Scope & DoD)
- [x] แสดงแบนเนอร์ต้อนรับและเมนูนำทางหลักในระบบ CLI
- [x] รองรับการรับคำสั่งแบบไม่ไวต่อตัวพิมพ์เล็ก-ใหญ่ด้วย `.strip().lower()`
- [x] จัดการ Exception (Invalid Input, ValueError) เพื่อป้องกันไม่ให้โปรแกรม Crash
- [x] รองรับคำสั่งออกจากโปรแกรม (`5`, `quit`, `exit`) อย่างปลอดภัย

## สมาชิกในทีมและหน้าที่ความรับผิดชอบ (Team Roles)

| ชื่อ-นามสกุล | รหัสนักศึกษา | บทบาทหลัก (Role) | หน้าที่และความรับผิดชอบ |
| :--- | :--- | :--- |:--- |
| **นางสาวพรีมภัทร ภาวัฒนวคุณ** | **673380594-9** | **Planner** | • วางแผนและนิยามสเปกต์ระบบในเอกสาร `PLAN.md`<br>• กำหนด Definition of Done (DoD)<br>• ควบคุมภาพรวมสถาปัตยกรรมและการส่งมอบงาน |
| **นางสาวมุกดา บุญประจันทร์** | **673380598-1** | **Coder** | • เขียนโค้ดระบบ CLI, ควบคุม Control Flow และ Menu Loop<br>• พัฒนาโครงสร้าง Class ตามแนวคิด OOP (`Pet`, `MoodTracker`, `Interaction`) |
| **นางสาวพิชยา สิทธิพันธ์** | **673380596-5** | **Debugger** | • ออกแบบและทำการทดสอบเคสขอบเขต (Edge Case Testing)<br>• ตรวจสอบ Exception Handling และ Input Sanitization<br>• สรุปรายงาน QA และจัดการ Pull Request (PR) บน GitHub |

*(หมายเหตุ: บทบาทหน้าที่อาจมีการหมุนเวียนกันตามข้อกำหนดในแต่ละ Sprint)*

### ผลการทดสอบประจำ Sprint 1 (Quality Assurance)
| รายการทดสอบ | อินพุตที่ใช้ | ผลลัพธ์ที่คาดหวัง | ผลการทดสอบจริง | สถานะ |
| :--- | :--- | :--- | :--- | :---: |
| การออกจากโปรแกรม | `5`, `QUIT`, ` exit ` | แสดงข้อความอำลาและหยุดทำงาน | แสดงข้อความอำลาและหลุดจาก Loop | **PASSED** |
| การจัดการคำสั่งเมนู | ` 1 `, `check` | ตัดช่องว่าง และเลือกเมนูข้อ 1 | ทำงานถูกต้องตามคำสั่ง | **PASSED** |
| การกรอกข้อมูลผิดพลาด | `abc`, `99` | แสดงคำเตือน และวนลูปรับค่าใหม่ | แสดงแจ้งเตือน ไม่ทำให้โปรแกรม Crash | **PASSED** |

### Retrospective (Wow! & Whoops!)
* **Wow! (ส่วนที่ทำได้ดี):** มีระบบจัดการ Input Sanitization ที่รัดกุม ผู้ใช้พิมพ์ช่องว่างติดมาหรือพิมพ์ตัวใหญ่ โปรแกรมยังสามารถประมวลผลได้ถูกต้อง
* **Whoops! (ปัญหาและแก้ไข):** ช่วงแรกการกด `Ctrl+C` ทำให้เกิด `KeyboardInterrupt` โค้ดหลุดกระจาย แก้ไขโดยการครอบ `try-except (KeyboardInterrupt, EOFError)` ให้ปิดโปรแกรมได้อย่างนุ่มนวล (Graceful Exit)

---

## Sprint 2: Back-End App Dev
* **ช่วงเวลา:** สัปดาห์ที่ 13 (นำเสนอ: 22-23 ก.ย. 2569 | ส่งงาน: 25 ก.ย. 2569)
* **จุดเน้น:** Business Logic Layer, โครงสร้าง OOP และระบบ File I/O (Data Persistence)

### เป้าหมายและขอบเขต (Scope & DoD)
- [ ] ออกแบบ Class ตามแนวคิด OOP (`Pet`, `MoodTracker`, `Interaction`)
- [ ] พัฒนาระบบ Data Access Layer สำหรับอ่าน/เขียนสถานะสัตว์เลี้ยงลงไฟล์ `pet_state.json`
- [ ] พัฒนาฟังก์ชันการค้นหา กรองข้อมูล และเรียงลำดับสถานะ
- [ ] เชื่อมต่อ API ภายนอก (Dog API / Cat Facts API) เพื่อใช้สุ่มข้อความ/รูปภาพ

### ผลการทดสอบประจำ Sprint 2 (QA Plan)
| รายการทดสอบ | อินพุต/สถานการณ์ | ผลลัพธ์ที่คาดหวัง | ผลการทดสอบจริง | สถานะ |
| :--- | :--- | :--- | :--- | :---: |
| การบันทึกข้อมูล (Save) | สั่ง Feed / Play | บันทึกค่า Hunger, Energy ลงใน `pet_state.json` | *Pending* | **PENDING** |
| การโหลดข้อมูล (Load) | เปิดโปรแกรมใหม่ | อ่านค่าสถานะล่าสุดจากไฟล์ JSON มาใช้งานต่อ | *Pending* | **PENDING** |
| การจัดการไฟล์หาย | ลบไฟล์ `pet_state.json` | ระบบสร้างไฟล์ใหม่พร้อมค่า Default โดยไม่พัง | *Pending* | **PENDING** |

### Retrospective
* *(รอสรุปหลังเสร็จสิ้น Sprint 2)*

---

## Sprint 3: Full-Stack App Dev
* **ช่วงเวลา:** สัปดาห์ที่ 14 (นำเสนอ: 29-30 ก.ย. 2569 | ส่งงาน: 2 ต.ค. 2569)
* **จุดเน้น:** การเชื่อมต่อ Front-End & Back-End, ระบบ Decay Over Time และการรับมือ Edge Cases

### เป้าหมายและขอบเขต (Scope & DoD)
- [ ] เชื่อมต่อ UI/CLI เข้ากับคลาส Business Logic และ Data Access Layer อย่างสมบูรณ์
- [ ] พัฒนากลไกคำนวณส่วนต่างของเวลา (`timestamp`) เพื่อหักลบค่า Stats (Decay Over Time) อัตโนมัติเมื่อเปิดโปรแกรม
- [ ] ประเมินและจัดการกรณีขอบเขต (Edge Cases) เช่น ค่า Hunger/Energy ติดลบ หรือเกิน 100

### ผลการทดสอบประจำ Sprint 3 (QA Plan)
| รายการทดสอบ | อินพุต/สถานการณ์ | ผลลัพธ์ที่คาดหวัง | ผลการทดสอบจริง | สถานะ |
| :--- | :--- | :--- | :--- | :---: |
| คำนวณ Decay ตามเวลา | ปิดโปรแกรมไว้ 2 ชม. | เมื่อเปิดใหม่ ค่า Hunger และ Energy ลดลงอย่างถูกต้อง | *Pending* | **PENDING** |
| Edge Case (Stats Boundary) | เล่นกับสัตว์เลี้ยงรัวๆ | ค่า Energy ไม่ลดลงต่ำกว่า 0 และ Hunger ไม่เกิน 100 | *Pending* | **PENDING** |

### Retrospective
* *(รอสรุปหลังเสร็จสิ้น Sprint 3)*

---

## Final Sprint: DevOps, CI/CD & AI Integration
* **ช่วงเวลา:** สัปดาห์ที่ 15 (นำเสนอ: 6-7 ต.ค. 2569 | ส่งงานส่งท้าย: 16 ต.ค. 2569)
* **จุดเน้น:** Automated Testing, GitHub Actions CI/CD Pipeline และ AI/Automation Agent Integration

### เป้าหมายและขอบเขต (Scope & DoD)
- [ ] พัฒนาชุดทดสอบอัตโนมัติ (Automated Unit Tests) ด้วย `pytest` หรือ `unittest`
- [ ] ตั้งค่า CI/CD Pipeline บน GitHub Actions สำหรับตรวจ Linting และรัน Unit Test อัตโนมัติทุกครั้งที่ Push/PR
- [ ] เชื่อมต่อฟีเจอร์ AI หรือ Smart Automation Agent (เช่น AI ประเมินอารมณ์สัตว์เลี้ยง หรือสร้างบทสนทนาโต้ตอบ)
- [ ] รวบรวม Artifacts และจัดทำสไลด์นำเสนอฉบับสมบูรณ์ (5-Part Presentation)

### ผลการทดสอบประจำ Final Sprint (QA Plan)
| รายการทดสอบ | อินพุต/สถานการณ์ | ผลลัพธ์ที่คาดหวัง | ผลการทดสอบจริง | สถานะ |
| :--- | :--- | :--- | :--- | :---: |
| GitHub Actions CI | Push Code ขึ้น Main | Workflow รันผ่าน (Passed) และไม่พบ Linting Error | *Pending* | **PENDING** |
| AI Integration Test | เรียกฟีเจอร์ Smart Pet | AI ตอบกลับวิเคราะห์สถานะสัตว์เลี้ยงได้เป็นธรรมชาติ | *Pending* | **PENDING** |

### Retrospective
* *(รอสรุปหลังเสร็จสิ้น Final Sprint)*
