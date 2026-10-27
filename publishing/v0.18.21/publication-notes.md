# Axiom Vision v0.18.21 — Relay Logs on Windows

แก้บั๊กตัวเก็บประวัติ Relay ใน v0.18.20 ที่พบไฟล์แต่รายงาน read_error ทุกไฟล์บน Windows
สาเหตุคือใช้ข้อมูล identity จาก DirEntry.stat ที่เป็นศูนย์บน Windows ไปเทียบกับ fstat ของไฟล์จริง

- อ่าน metadata ใหม่ของไฟล์ที่เลือกก่อนเปิด แล้วเทียบกับ handle ในรูปแบบเดียวกัน
- ยังคงตรวจไฟล์ปกติและบล็อกไฟล์ที่ถูกแทนที่หรือเปลี่ยนเป็น symlink
- จำกัดจำนวนไฟล์ จำนวนบรรทัด bytes และขนาดรายงานตามเดิม
- เก็บเฉพาะเหตุการณ์และฟิลด์ที่กำหนด พร้อม read_error_reason ที่ไม่เปิดเผย path หรือข้อความลับ
- นับขนาดและตำแหน่ง tail จากไฟล์ที่เปิดสำเร็จ เพื่อรายงานไฟล์ที่โตขึ้นหรือถูกตัดได้ตรง

การเผยแพร่รุ่นนี้ต้องผ่านการทดสอบตัวอ่านบน Windows จริงกับ Python 3.12.10
โดยทดสอบให้ v0.18.20 เกิด read_error และ v0.18.21 อ่านเหตุการณ์เดิมได้
รวมทั้งเส้นสร้าง diagnostic bundle และ Telegram excerpt
การทดสอบนี้ครอบคลุมไฟล์ Log ไม่ใช่การรับคลิกหรือจับหน้าจอของ LDPlayer

Log วันที่ 28 ตุลาคมแสดงแพ็กเกจ v0.18.20 แต่ Session ที่แนบมายังเป็น v0.18.19 เดิม
และตัวอ่านประวัติ Relay อ่านไม่ผ่านทั้ง 64 ไฟล์ จึงยังสรุปผลการตรวจหรือกด Relay ไม่ได้
ข้อผิดพลาด Recovery ในไฟล์นี้เป็นเหตุการณ์เดิม ไม่ใช่หลักฐานว่า v0.18.20 แก้ไม่สำเร็จ

อัปเดตผ่าน Settings → CHECK UPDATE เมื่อ worker หยุดและไม่มี checkpoint ที่กำลังทำงาน
เปิด Controller ใหม่ แล้วกด SEND LOG เพื่อดึงประวัติจากไฟล์เดิมที่ยังเก็บอยู่
การเก็บ Log ไม่ต้องเริ่มแบตช์ใหม่ และไม่เปลี่ยนสถานะการฟาร์ม

โหมด Relay, Preset เวลา, Recovery และ Plan ใช้ค่าจาก v0.18.20 ตามเดิม
OFF revision 9, ON revision 11; AUTO ยังปิด Relay
ไม่มีการปรับเกณฑ์ภาพหรือสิทธิ์คลิกจากข้อมูล Log

Validation before CI: 1,275 passed / 17 skipped (1,292 total), including19 reader tests. Native Windows Python3.12.10 must reproduce the v20 reader failure, read the same event in v21, and pass the complete reader suite before the publisher can run. The test includes real bundle creation and exact Telegram excerpt retention. Signed upgrades from v0.18.13–v0.18.20 verify all161 package files and preserve nine runtime files per installation, including saved timing presets. Native LDPlayer capture/input is not covered.

Package: AxiomVision-v0.18.21-Relay-Logs-Windows10.zip
Size: 9,707,588 bytes
SHA-256: e3eb419d924a7ad5398788ca1404e379e5bf241586e5278e7253c156fb34539d
