# Axiom Vision v0.18.13 — Recovery Resume

แก้ Resume ที่หายหลัง Stop ระหว่างกู้ checkpoint แบบ blocked และป้องกัน
Start ใหม่หรือ Heart Sender ข้าม checkpoint เดิมที่ยังกลับมาทำต่อได้
รายละเอียดและข้อจำกัด: RELEASE_v0.18.13_TH.md
อัปเดตผ่าน Settings → CHECK UPDATE แล้วรอ worker จบและปิด Controller
เก็บ state/checkpoint/stats/session/reward เดิม ไม่ต้อง Reset Batch

