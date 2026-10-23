# Axiom Vision v0.18.17 — Run Profile Presets

บันทึกชื่อและเวลาของ Run Profile สำหรับแต่ละการฟาร์มได้
รายการ PRESET อยู่ใต้ RUN PROFILE และก่อน RANDOM BOOST

- SAVE AS สร้าง Preset โดยตั้งชื่อและเวลา 30–1,800 วินาที
- เลือก Preset เพื่อใช้เวลาที่บันทึกไว้เป็น Custom
- EDIT แก้ชื่อหรือเวลา และ DELETE ลบรายการที่เลือก
- รองรับชื่อภาษาไทยและเก็บไว้หลังปิดโปรแกรมหรือ Reset Batch
- บันทึกทันที ไม่ต้องเริ่มแบตช์ก่อน และไม่เปลี่ยน Random Boost, Relay หรือจำนวนรอบ
- ระหว่างที่แบตช์ยังแก้การตั้งค่าไม่ได้ ปุ่ม Preset จะถูกล็อกด้วย
  Resume ใช้แผนและเวลาที่ตรึงไว้ตอนเริ่ม ไม่อ่านค่าจาก Preset ที่อาจแก้ภายหลัง

AUTO / SHORT / NORMAL / CUSTOM ยังใช้ได้ตามเดิม
AUTO ใช้ Cookie Relay ไม่ได้ เมื่อเปิด Relay เวลาของ Preset คือเวลาประมาณของ
Cookie ตัวแรก ระบบใช้เวลานี้ช่วยเริ่มเฝ้าภาพ ไม่ใช้เวลาเป็นหลักฐานว่าปุ่มปรากฏ
หรือว่าวิ่งจบแล้ว ต้องยืนยันปุ่ม Relay จากภาพสดก่อนส่งคลิก

แก้การตรวจสิทธิ์ Relay รอบสุดท้าย: ถ้า watchdog หมดเวลาระหว่างตรวจหน้าต่าง
จะไม่ส่งคลิก และยังเก็บ intent ไว้ตามกฎไม่กดซ้ำ

แก้ข้อความยืนยัน RUN ทาง Telegram หลังแบตช์เดิมจบ ให้แสดง Run Profile
และผูกกับค่าที่เลือกสำหรับงานใหม่ การเปลี่ยนเวลาทำให้คำยืนยันเก่าใช้ไม่ได้
ส่วน Resume ยังผูกกับแผนเดิมที่ตรึงไว้
ช่อง Custom ปฏิเสธค่าที่ไม่ใช่จำนวนเต็มหรืออยู่นอกช่วง แทนการแปลงเป็น AUTO เงียบ ๆ

Stop / Pause / Human Verification และกฎภาพสด หน้าต่าง Geometry และ replay
ยังทำงานตามเดิม ไม่เปลี่ยนสิทธิ์ Heart Sender และระบบอ่านสมบัติยังปิดอยู่
Universal Mission ใช้ revision 9 เมื่อ Relay OFF และ revision 10 เมื่อ Relay ON

อัปเดตที่ Settings → CHECK UPDATE รอช่วงที่ updater ติดตั้งได้
ไฟล์ state / checkpoint / stats / session เดิมคงอยู่ ไม่ต้อง Reset Batch เพื่ออัปเดต

ตรวจ UI และเส้นทางจำลองบน Linux การกด Relay ทันหน้าต่าง 2 วินาที
และผลในเกมยังไม่ได้ยืนยันบน Windows / LDPlayer จริง

Validation: 1,198 passed / 17 skipped (1,215 total). Signed upgrades from v0.18.13–v0.18.16 preserve nine runtime files per installation byte-for-byte; saved timing presets load after upgrading. All 146 signed package hashes match the frozen source.

Package: AxiomVision-v0.18.17-Run-Profile-Presets-Windows10.zip
Size: 9,535,334 bytes
SHA-256: 61aaa7b253669a10ed021a18bdae8dd2c5ef136a7b58f4e90d69b26509e83e5a
