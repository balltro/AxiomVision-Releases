# Axiom Vision v0.18.15 — Recovery Watchdog

แก้เส้นทาง Auto Recovery ที่ทดสอบจำลองให้เกิดซ้ำได้
- worker ค้างใหม่ยังไม่ตั้ง resume_required จึงไม่ผ่านเงื่อนไขกู้คืนเดิม
- ยืนยัน Bridge/Plan/Stage/geometry และปิดสิทธิ์ input ก่อนยุติ worker
  รอ process เดิมจบ แล้วส่ง checkpoint เดิมเข้า recovery/backoff ที่มีอยู่
- เคารพการปิด autonomous recovery และไม่ให้ Stop/Pause/Human/terminal/completion
  ถูกการกู้คืนเขียนทับ ไม่ล้าง intent, purchase, Confirm หรือ attempt budget
- no-fresh-frame ไม่บังการจัดการ worker ที่ยืนยันว่าไม่ตอบสนองแล้ว
- แยกสถานะ RESET REQUIRED/NEEDS REVIEW จาก AUTO-RECOVERING ที่มีคิวจริง

ปรับ Send Log เพื่อเก็บหลักฐานที่ใช้ตรวจปัญหาได้
- เพิ่มประวัติ failure/recovery แบบย่อจาก worker log และไฟล์หมุนเวียนที่ยังอยู่
  แยกจาก tail ปกติ เพื่อไม่ให้รอบที่ทำงานสำเร็จดันเหตุขัดข้องหายง่าย
- บอกขอบเขตข้อมูลที่เก็บได้ ไม่อ้างว่าเป็นประวัติทั้งหมด
- ให้ภาพปัจจุบันของงานที่กำลังทำมาก่อนภาพ OCR เก่า/Heart ที่ reset แล้ว
  ส่งไฟล์ ZIP เดียวตามงบเดิม state หลักยังตรงทุกไบต์
- ภาพ preview ใช้ดูประกอบเท่านั้น ไม่ใช้อนุญาตคลิกหรือเป็นหลักฐาน OCR ต้นฉบับ

ข้อเท็จจริงจาก diagnostic v0.18.14 รอบ 17 ตุลาคม
- batch ล่าสุดจบ 12 รอบในช่วง 02:39–03:39 น. เวลาประเทศไทย
- tail ที่ได้รับมี 5 รอบสำเร็จติดต่อกัน ไม่มีเหตุ recovery/error ใหม่
- pending Multi-Buy ใน snapshot มีบันทึก dispatch/commit สำเร็จตามมา
- ข้อมูลชุดนี้จึงยังพิสูจน์ไม่ได้ว่าช่องโหว่ที่แก้เป็นสาเหตุของอาการที่ผู้ใช้เห็น

ระบบอ่านรายการสมบัติ/วัตถุดิบยังปิดอยู่ตาม v0.18.14
Universal Revision 9, Heart Revision 13, dependency pins, never-replay guards,
freshness, geometry, watchdog/runtime budgets และ Human Verification คงเดิม

อัปเดตจาก Settings → CHECK UPDATE และหยุด worker/ปิด Controller เมื่อติดตั้ง
updater จะเลื่อนการติดตั้งระหว่างมีงานหรือ active checkpoint ตามกฎเดิม
เก็บ runtime state เดิม ไม่ต้อง Reset Batch เพื่อรับอัปเดต

ทดสอบด้วย replay/จำลองและ updater บน Linux
ยังไม่ได้ทดสอบ native Windows/LDPlayer ด้วยรุ่นนี้
