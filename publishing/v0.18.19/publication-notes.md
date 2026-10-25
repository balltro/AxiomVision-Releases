# Axiom Vision v0.18.19 — Relay Direct

เปลี่ยนเส้นกด Cookie Relay เป็นตัวตอบสนองในเครื่องที่อ่านพิกเซลจากหน้าจอโดยตรง
ไม่สร้าง PNG แล้วถอดภาพซ้ำในช่วงตัดสินใจกด ไม่รอ Codex หรือ OCR ทั้งภาพ

- ใช้ MSS capture context เดิมตลอดช่วงเฝ้า และคืนทรัพยากรบน thread เจ้าของเมื่อจบ
- เก็บ RGB เป็นข้อมูลที่เปลี่ยนไม่ได้ พร้อมเวลาเริ่มจับภาพ HWND และ Geometry
- ใช้ตัวตรวจ Relay visual-2 และ Human Verification เดิมกับพิกเซลโดยตรง
- ตรวจความสดเฉพาะปุ่มจาก RGB โดยใช้วิธีและเกณฑ์เดิม
- ยังคงภาพเสถียรก่อน intent และภาพสดอีกชุดก่อนส่งคลิก
  อายุภาพเริ่มนับก่อนจับภาพและต้องไม่เกิน 0.5 วินาที
- เก็บชนิดข้อมูลและ hash ให้ชัดว่าเป็น raw RGB หรือ PNG และไม่กดซ้ำหลังผลไม่แน่ชัด

เกณฑ์ภาพ ขอบเขตปุ่ม สิทธิ์ input และ Plan ไม่เปลี่ยนจาก v0.18.18
Relay OFF ใช้ revision 9; Relay ON ใช้ revision 11 ตามเดิม
แบตช์ Relay revision 10 ที่เก่ากว่ายังต้อง Stop และ Reset ตามกฎเดิม
การอัปเดตไม่เปลี่ยนแบตช์ OFF ให้เป็น ON และไม่แก้แผนที่กำลังรัน

วิธีเปิดใช้งาน

1. ถ้าแบตช์ปัจจุบันเป็น Relay OFF ให้ Stop รอ worker หยุด แล้ว Reset Batch
2. อัปเดตที่ Settings → CHECK UPDATE และเปิด Controller ใหม่หลังติดตั้ง
3. เลือก Short / Normal / Custom หรือ Preset เวลา แล้วเลือก COOKIE RELAY → ON
4. ตรวจข้อความ Relay: On ในแผนก่อนกด START BATCH

AUTO ยังใช้ Relay ไม่ได้ Preset บันทึกเฉพาะเวลา ไม่เปิด Relay ให้อัตโนมัติ
Preset และประวัติเดิมยังอยู่ ข้อความหน้า UI แยก OFF และ ON ให้ชัดขึ้น

Log วันที่ 25 ตุลาคมที่ผู้ใช้ส่งเป็น Relay OFF จึงไม่มีข้อมูล latency ของ Relay ที่เปิดใช้งาน
การทดสอบรุ่นนี้เทียบกับโค้ด v0.18.18 และภาพต้นฉบับ พร้อมเส้นตรวจจริงในเครื่องทดสอบ
ยังไม่ได้ยืนยัน native screen grab, การรับคลิก หรือเวลาจริงบน Windows/LDPlayer ของผู้ใช้

Validation: 1,247 passed / 17 skipped (1,264 total). Real-clock whole-transaction replay: v18 median 584.725ms/max592.187ms versus v19 median183.405ms/max190.609ms; all9cases/version pass. Three extra public-sample overlap cases per version also pass. Native grab, OS window calls and mouse sink are adapters; classifiers, MSS conversion/PNG encoding, Controller, freshness and durable writes run. All63 compiled config/Plan identities remain exact. Signed upgrades from v0.18.13–v0.18.18 preserve nine runtime files per installation byte-for-byte, including readable timing presets.

Package: AxiomVision-v0.18.19-Relay-Direct-Windows10.zip
Size: 9,640,549 bytes
SHA-256: 2dab8cec0991ad30bbdd0abfc0d8013d1419f54522e2ff6da0ea949dadc6279f
