CREATE TABLE IF NOT EXISTS "users" ( "id" INTEGER PRIMARY KEY AUTOINCREMENT, "name" VARCHAR(45), "password_hash" CHAR(64));

CREATE TABLE IF NOT EXISTS "staff" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "name" VARCHAR(45),
  "password_hash" VARCHAR(64));
  
CREATE TABLE IF NOT EXISTS "med_visit" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "notes" VARCHAR(160),
  "patient_id" INTEGER,
  "doctor_id" INTEGER,
 
  CONSTRAINT "patient_fk"
    FOREIGN KEY ("patient_id")
    REFERENCES "users" ("id")
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT "doctor_fk"
    FOREIGN KEY ("doctor_id")
    REFERENCES "staff" ("id")
    ON DELETE SET NULL
    ON UPDATE CASCADE);

CREATE INDEX "doctor_fk_idx" ON "med_visit"("doctor_id" ASC);
CREATE INDEX "patient_fk_idx"  ON "med_visit"("patient_id" ASC);

CREATE TABLE IF NOT EXISTS "med_report" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "report_data" VARCHAR(400),
  "visit_id" INTEGER,

  CONSTRAINT "visit_fk"
    FOREIGN KEY ("visit_id")
    REFERENCES "med_visit" ("id")
    ON DELETE SET NULL
    ON UPDATE CASCADE);

 CREATE INDEX "visit_fk_idx" ON "med_report"("visit_id" ASC);

