# Axiom Vision v0.18.20 — Recovery Observation

แก้เส้นกู้คืนที่ติดหลัง Multi-Buy: เมื่อเวลาล็อกอินพุตหมดแล้ว ระบบต้องดูภาพใหม่
แต่เส้น Recovery เดิมกลับถูกเงื่อนไขเดียวกันขวางก่อนจับภาพ ทำให้กู้คืนซ้ำโดยไม่คืบหน้า

- อนุญาตเฉพาะการดูภาพใน Recovery หลังหมดเวลาล็อก และตรวจสถานะอีกครั้งหลังจับภาพ
- ปลดเฉพาะเงื่อนไขรอภาพใหม่ของ lockout เดิมเมื่อภาพสำเร็จและผ่าน Human Guard
- ยังต้องยืนยัน Scene ก่อน Resume และไม่กด Multi-Buy หรือ Confirm ซ้ำ
- Stop, Pause, Human Verification, intent และงบกู้คืนเดิมยังมีผล
- SEND LOG เก็บประวัติ Relay แยกจาก Session ล่าสุด 5 รายการ พร้อมระบุขอบเขตและข้อมูลที่ขาด
  เพื่อไม่ให้ Session กู้คืนหลายครั้งดันประวัติตอนวิ่งออกจาก Log ที่ส่ง

Log วันที่ 27 ตุลาคมยืนยัน Relay ON, Custom 60 วินาที และ Plan revision 11
แต่ Session ที่แนบมาทั้งห้าครอบคลุมเฉพาะการเตรียมเกมและกู้คืน ไม่มีช่วง Running
จึงยังสรุปไม่ได้ว่า Relay ตรวจไม่พบปุ่ม ส่งคลิกช้า หรือเกมไม่รับคลิก
รุ่นนี้แก้ปัญหากู้คืนที่พิสูจน์ได้และการเก็บ Log ไม่ได้เปลี่ยนเกณฑ์ตรวจหรือเส้นคลิก Relay

อัปเดตที่ Settings → CHECK UPDATE ขณะหยุด worker และไม่มี checkpoint ที่กำลังทำงาน
จากนั้นเปิด Controller ใหม่ ตั้ง Run Profile และตรวจ COOKIE RELAY → ON ก่อนเริ่ม
Preset เวลาและข้อมูลเดิมยังอยู่ AUTO ยังคงปิด Relay
ไม่มีการเปลี่ยน Plan จาก v0.18.19: OFF revision 9, ON revision 11
แบตช์ Relay revision 10 เก่ายังใช้กฎ Stop/Reset เดิม

การตรวจยืนยันบนเครื่องทดสอบครอบคลุมโค้ดกู้คืนและการเก็บ Log
ยังไม่ได้ทดสอบการจับหน้าจอและรับคลิกจริงบน Windows/LDPlayer ของผู้ใช้

Validation: 1,268 passed / 17 skipped (1,285 total). The expired-lockout recovery reproduction fails on v19 and passes on v20. New tests cover real restored and uncertain purchase state, active lockout, capture failure/black frames, Human, Stop/Pause, window/Stage/intent changes, and attached Controller replacement with the same Plan. Relay diagnostics survive five newer setup sessions and Telegram packing byte-exact. All91 profile/boost/Relay config and Plan comparisons match v19. Signed upgrades from v0.18.13–v0.18.19 verify all160 package files and preserve nine runtime files per installation, including saved timing presets.

Package: AxiomVision-v0.18.20-Recovery-Observation-Windows10.zip
Size: 9,692,554 bytes
SHA-256: 6b09fb34d5cbae7a616197cd454e908e0899a809a9c74cfca27f3f9f8fcf106a
