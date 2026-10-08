# Axiom Vision v0.18.13 — Recovery Resume

เมื่อ Stop ระหว่าง Auto Recovery ที่ checkpoint เป็น blocked รุ่นก่อนหน้า
ตัวตรวจของ Controller รับเฉพาะ active ทำให้ Resume หายและ Start ใหม่
อาจข้ามขั้น archive ของ checkpoint เดิม

รุ่นนี้ให้ Controller ยอมรับ blocked เฉพาะ Universal ที่มี Plan hash,
Stage และ phase ตรงกับสัญญาปัจจุบัน ทำให้ Resume กลับมา และ Heart Sender
กับ Start ใหม่ยังเคารพรอบเดิม ต้อง archive ก่อนแทนที่รอบที่กู้ต่อได้
การยอมรับนี้อ่าน state เท่านั้น ไม่คลิก ไม่ล้าง intent และไม่อนุญาต replay

คง Auto Recovery ของ v0.18.12, backoff 2/5/10/30/60/120/300 วินาที,
Universal Revision 9, Heart Revision 13, Stop/Pause/Human Verification
Reward Archive และ Send Log คงโค้ดเดิมทุกไบต์

Regression เพิ่ม 5 กรณี: blocked resume, Stop/Heart exclusion,
archive-before-new-Start, terminal/unknown status, legacy/foreign Plan/Stage
ทดสอบบน Linux; native Windows/LDPlayer จริงยังต้องยืนยัน

ติดตั้งผ่าน Settings → CHECK UPDATE รอ worker จบและปิด Controller
updater จะรอให้ runtime ว่างก่อนสลับไฟล์และเปิด Controller ใหม่
ไม่ต้อง Reset Batch; checkpoint active จะยังเลื่อนการติดตั้งตามกฎเดิม
หาก pending Confirm เก่ายังไม่ทราบผล ระบบยังไม่กดซ้ำอัตโนมัติ

