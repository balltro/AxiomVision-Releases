# Axiom Vision v0.18.18 — Relay Response

แก้ Cookie Relay ที่ตรวจพบปุ่มแล้วแต่ไม่ถึงขั้นเตรียมคลิก

นำภาพ Relay ที่ผู้ใช้ให้มาจำลองในกรอบ LDPlayer ตามขนาดใน diagnostic
1642×941 พิกเซล โดยมีแถบบน 41 พิกเซลและแถบเครื่องมือขวา 42 พิกเซล
ตัวตรวจภาพพบปุ่มที่ขอบซ้าย x714 แต่กรอบอนุญาตเดิมเริ่มที่ x722 จึงปฏิเสธ
ก่อนเตรียม intent ปัญหานี้สอดคล้องกับ Log ห้ารอบที่เริ่มเฝ้าแล้วแต่ attempts ยังเป็น 0
ภาพสดในจังหวะที่พลาดไม่ได้อยู่ใน diagnostic จึงยังไม่ใช่การยืนยันพิกเซลของเหตุการณ์จริง

- แก้ขอบซ้ายของกรอบ Relay สำหรับหน้าต่างที่มีแถบเครื่องมือด้านเดียว
  ต้องผ่านข้อความ Relay กรอบสี และ Jump/Slide จากภาพสดตามเดิม
- แก้การอ่านขอบสีที่เหลือหนึ่งพิกเซลหลังย่อภาพ โดยยังตรวจครบทั้งสี่ด้าน
- ตรวจ Human Verification หนึ่งครั้งต่อภาพเดิม รวมภาพที่ช้าจนหมดอายุ
  ภาพใหม่ก่อนส่งคลิกยังต้องตรวจ Human และเงื่อนไข input ทุกครั้ง
- วัดความเปลี่ยนแปลงเฉพาะปุ่มในเส้น Relay ด้วยวิธีและเกณฑ์เดิม
  ลดงานคำนวณภาพพื้นหลังที่กำลังเคลื่อนไหว อายุภาพสูงสุดยัง 0.5 วินาที
- เพิ่มสรุปจำนวนภาพที่ตรวจและเหตุที่ไม่คลิกตอนจบช่วงเฝ้า
  ไม่เขียน Log ทุกภาพลบ และไม่ใช้ข้อมูลสรุปเป็นสิทธิ์ส่ง input

Relay ON ใช้ Mission revision 11 และตัวตรวจภาพ visual-2
Relay OFF ใช้ revision 9 และ Plan เดิม Preset ที่ตั้งชื่อไว้ยังอยู่

ถ้าแบตช์เก่ายังเป็น Relay revision 10 ให้ Stop แล้ว Reset Batch ก่อนเริ่มแบตช์ใหม่
Reset เก็บประวัติเดิมตามระบบ Archive โปรแกรมไม่ล้าง checkpoint หรือ intent ให้อัตโนมัติ
Resume แผนเก่าจะถูกบล็อกพร้อมข้อความให้เริ่มแผนใหม่ เพื่อไม่เปลี่ยนสิทธิ์กลางแบตช์

อัปเดตที่ Settings → CHECK UPDATE รอ worker หยุดและปิด Controller เพื่อติดตั้ง
ถ้า updater ยังรอ active checkpoint ให้ Stop และ Reset Batch ก่อน
ไม่เปลี่ยน Heart Sender, การอ่านสมบัติ, Random Boost หรือกฎ Stop/Pause/Human

การทดสอบใช้ภาพต้นฉบับ การจำลองกรอบหน้าต่าง เวลา และ input พร้อมเส้นตรวจจริง
ยังไม่ได้ยืนยันการกดทันสองวินาทีและการรับคลิกใน Windows/LDPlayer จริง

Validation: 1,224 passed / 17 skipped (1,241 total). The actual-image geometry replay reproduces the old guard rejection. All 42 chrome phases and 15 visual negatives pass; 14 modeled two-second timing windows pass with real detectors, Controller checks, ROI freshness and durable I/O. Native capture/input and phase clocks are simulated. Signed upgrades from v0.18.13–v0.18.17 preserve nine runtime files per installation byte-for-byte and retain readable timing presets.

Package: AxiomVision-v0.18.18-Relay-Response-Windows10.zip
Size: 9,590,883 bytes
SHA-256: 1aef624093ed45ed3fea0ccb21deeb7c919a5869147432c78e26ca88b2c93934
