CREATE TABLE "Doctor" (
  "ID" int,
  "First Name" String,
  "Last Name" String,
  "Address" String,
  "Email" String,
  "Phone" String,
  PRIMARY KEY ("ID")
);


CREATE TABLE "Patient" (
  "ID" int,
  "First Name" String,
  "Last Name" String,
  "Address" String,
  "Email" String,
  "Phone" String,
  PRIMARY KEY ("ID")
);



CREATE TABLE "Measurement" (
  "ID" IDENTITY,
  "PatientID" String,
  "Weight" Type,
  "Weight_UOM" Type,
  "BMI" Type,
  "FatPct" Type,
  "MusclePct" Type,
  "vFat" Type,
  "Waist" Type,
  "Hip" Type,
  "Lenght_UOM" Type,
  PRIMARY KEY ("ID"),
  CONSTRAINT fk_patient FOREIGN KEY("PatientID") REFERENCES Patient("ID")
);



CREATE TABLE "Appointments" (
  "ID" int,
  "PatientID" String,
  "DoctorID" String,
  "DateTime" DateTime,
  "Comment" String,
  PRIMARY KEY ("ID"),
  CONSTRAINT fk_patient FOREIGN KEY("PatientID") REFERENCES Patient("ID"),
  CONSTRAINT fk_doctor FOREIGN KEY("DoctorID") REFERENCES Doctor("ID")
);



CREATE TABLE "Plan" (
  "ID" IDENTITY,
  "MeasurementID" Type,
  "AppointmentID" String,
  "PlanDetail" Type,
  PRIMARY KEY ("ID"),
  CONSTRAINT fk_measurement FOREIGN KEY("MeasurementID") REFERENCES Measurement("ID"),
  CONSTRAINT fk_appointment FOREIGN KEY("AppointmentID") REFERENCES Appointment("ID")
);

