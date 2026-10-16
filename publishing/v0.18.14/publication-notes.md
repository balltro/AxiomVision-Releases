# Axiom Vision v0.18.14 — Recovery Core

ตัดระบบอ่านรายการวัตถุดิบ/สมบัติ
- ไม่บันทึกภาพ Confirm เพื่ออ่านรายชื่อของ ไม่เปิด OCR archive เบื้องหลัง
- หน้า Run Summary เหลือรอบ กล่อง Coins และ EXP; Telegram ไม่อ่านรายการของเก่า
- เก็บประวัติรางวัลเดิม และยังเปิดกล่อง/Confirm ด้วย scene OCR และ input guards

แก้ Auto Recovery จาก diagnostic v0.18.13 วันที่ 16 ตุลาคม
- เหตุการณ์ก่อนส่ง diagnostic: กลับหน้า Confirm ได้ แต่ scene OCR ปฏิเสธก่อน
  คลิก และอีกครั้ง reason แทน note ทำให้ KeyError; snapshot ตอนส่งเป็นรอบใหม่
  ที่กำลัง passive-running จึงไม่อ้างว่ารอบใหม่ค้าง
- อ่านเฉพาะปุ่ม Confirm จากภาพเดียวกันเมื่อ OCR ทั้งภาพพลาด ต้องมีหัวข้อ
  Mystery Box/Reward Box, โครงสร้างปุ่ม cyan, ตำแหน่งและความมั่นใจที่กำหนด
  full-frame Human/overlay exclusions คงเดิม ไม่ใช้ชื่อของเป็นสิทธิ์คลิก
- สังเกตใหม่ได้หนึ่งครั้งก่อน first Confirm เฉพาะ ledger ที่สะอาด ภาพใหม่
  กับ OCR ต้องคู่กัน ไม่เพิ่มจำนวนคลิก/attempt และไม่อนุญาต pending/committed replay
- checkpoint รางวัลที่ยังไม่ทำ action และผูก Plan/Result/route/anchor ครบ
  ลอง Local หนึ่งครั้งก่อน Codex เก็บโหมด คิว และ backoff ข้าม Controller reopen
  ความผิดพลาด Local เดิมกลับไป Codex ไม่วน Local ไม่สิ้นสุด
- รับ note/reason เป็น alias ที่ตรวจชนิด/ความยาว/ความขัดแย้งก่อนอ่าน Session
- Recovered เพิ่มเมื่อมี Stage progress จริง ไม่เพิ่มจาก observe unlock ซ้ำ
- แก้ age-only abort ก่อน native dispatch ที่ล็อก safe replay ผิด ต้องมี private
  same-process witness เดิม ไม่สร้างสิทธิ์จาก checkpoint/log และไม่คืน attempt budget
- terminal disposition ที่ห้าม Supervisor ไม่วนเปิด Codex ซ้ำ

Stop/Pause/Human Verification, window/geometry/freshness, watchdog/runtime limits,
Universal Revision 9, Heart Revision 13 และ never-replay guards คงเดิม
Send Log transport และ dependency pins คงเดิม

ติดตั้งด้วย Settings → CHECK UPDATE รอ worker หยุด แล้วปิด Controller
state/checkpoint/stats/session/reward เดิมคงอยู่ ไม่ต้อง Reset Batch
active checkpoint จะเลื่อนการติดตั้งตามกฎ updater เดิม

การยืนยันรอบนี้ใช้ diagnostic จาก Windows และรันทดสอบจำลองบน Linux
ยังไม่ได้รัน native Windows/LDPlayer ด้วยรุ่นนี้ และยังไม่รับรอง loop ≤200 วินาที

ผลตรวจ: 1,088 ผ่าน / 17 ข้าม จาก 1,105 tests
ติดตั้ง signed package ผ่าน updater เดิมจาก v0.18.11 / v0.18.12 / v0.18.13
ตรวจไฟล์แพ็กเกจ 127 รายการและเก็บ runtime state เดิม 9 ไฟล์ต่อการติดตั้งตรงทุกไบต์

Package: AxiomVision-v0.18.14-Recovery-Core-Windows10.zip
Size: 9,269,256 bytes
SHA-256: 86f7f539c5702455c4cf13cf75ac816f4c3f0e708f5aba161d300a2a646ec9de
