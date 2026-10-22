# Axiom Vision v0.18.16 — Cookie Relay

เพิ่ม COOKIE RELAY ต่อจาก Random Boost ในหน้า Universal Loop
- OFF เป็นค่าเริ่มต้น เปิด ON ได้เมื่อเลือก Short / Normal / Custom
- AUTO ใช้ Relay ไม่ได้ เมื่อเปลี่ยนเป็น AUTO ระบบปิด Relay ให้อัตโนมัติ
- ขณะเปิด Relay เวลาของ Run Profile หมายถึงเวลาประมาณของ Cookie ตัวแรก
  เลือก Custom หากต้องการระบุเวลาให้ตรงกับตัวที่ใช้อยู่

วิธีทำงาน
- ใช้เวลา Profile ช่วยเริ่มเฝ้าภาพก่อนถึงเวลาคาดหมาย โดยเผื่ออย่างน้อย60วินาที
  หรือ30% ของเวลาตัวแรก เช่น Short180เริ่มเฝ้าประมาณ120วินาที
- เว้นพัก0.15วินาทีระหว่างการตรวจในช่วงเฝ้า มีเวลาจับภาพ/ประมวลผลเพิ่ม
  ใช้ตัวตรวจภาพLocal
  ไม่รอ Codex หรือ OCR ทั้งภาพในเส้นทางกดปุ่มช่วงสั้น
- ต้องเห็นข้อความ Relay กรอบปุ่ม และองค์ประกอบหน้าRunningในภาพสดจริง
  ตรวจซ้ำก่อนส่งinput ไม่กดจากเวลา/ตำแหน่งเก่าเพียงอย่างเดียว
- ใช้คำสั่งกดได้หนึ่งครั้งต่อloop บันทึกintent/commitแยกจากstage Running
  เมื่อมีคำสั่งที่ผลไม่แน่ชัดจะไม่กดซ้ำหลังrestart
- หากปุ่มไม่ปรากฏหรือพลาดช่วงเวลา ยังสังเกตResultตามเส้นทางเดิม
- โหมดOFFใช้MissionและPlanhashเดิมrevision9; ONใช้revision10
  เก็บตัวเลือกไว้ในfrozenPlanและแสดงในสถานะ/แผนผ่านTelegram

Stop/Pause/Human Verification, foreground/geometry, freshness, durable input,
watchdog และ never-replay guards ยังทำงาน ไม่มีสิทธิ์คลิกทั่วไปขณะRunning
Relay ไม่เพิ่มหรือรีเซ็ต budget ของStage; ขีดจำกัดRunningเดิมยังอยู่
Customที่ใกล้ขีดจำกัด1800วินาทีอาจไม่มีเวลาพอสำหรับCookieตัวที่สอง
ระบบอ่านสมบัติ/วัตถุดิบยังปิดตามเดิม Heart Sender ไม่เปลี่ยน

การตรวจรุ่นนี้ใช้ภาพที่ผู้ใช้ให้และการจำลองinput/เวลา/การรีสตาร์ตบนLinux
ยังไม่ได้ยืนยันการกดทันหน้าต่าง2วินาทีด้วยWindows/LDPlayerจริง

อัปเดตที่Settings → CHECK UPDATE แล้วรอช่วงที่updaterติดตั้งได้
state/checkpoint/stats/sessionเดิมคงอยู่ activecheckpointเลื่อนการติดตั้ง
ไม่ต้องReset Batchเพื่อรับอัปเดต
