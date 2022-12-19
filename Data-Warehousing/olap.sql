-- Creating tables
CREATE TABLE Location(
LID varchar(45),
region varchar(45) not null,
city varchar(45) not null,
primary key(LID)
);

CREATE TABLE dates(
D_ID varchar(64),
d_date int not null,
d_month int not null,
d_year int not null,
primary key(D_ID)
);

CREATE TABLE Transactions (
TID varchar(64),
Name varchar(64) not null,
Address varchar(64) not null,
Phone_no varchar(64) not null,
Tdate varcher(64) not null,
primary key(TID)
foreign  key(Address) REFERENCES Location(LID)
foreign  key(Tdate) REFERENCES Dates (D_ID)
);

-- Populating tables
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D1",24,2,2020);
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D2",10,1,2022);
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D3",14,3,2015);
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D4",16,2,2021);
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D5",28,5,2021);
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D6",22,10,2017);
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D7",21,3,2018);
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D8",18,8,2016);
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D9",8,9,2020);
INSERT INTO Dates (D_ID, d_date, d_month, d_year)
VALUES ("D10",3,1,2022);

INSERT INTO Location (LID, region, city)
VALUES ("L1","Bhandup","Mumbai");
INSERT INTO Location (LID, region, city)
VALUES ("L2","Diva","Thane");
INSERT INTO Location (LID, region, city)
VALUES ("L3","Kurla","Mumbai");
INSERT INTO Location (LID, region, city)
VALUES ("L4","Khed","Pune");
INSERT INTO Location (LID, region, city)
VALUES ("L5","Bhandup","Mumbai");
INSERT INTO Location (LID, region, city)
VALUES ("L6","Andheri","Mumbai");
INSERT INTO Location (LID, region, city)
VALUES ("L7","Kalva","Thane");
INSERT INTO Location (LID, region, city)
VALUES ("L8","Andheri","Mumbai");
INSERT INTO Location (LID, region, city)
VALUES ("L9","Khed","Pune");
INSERT INTO Location (LID, region, city)
VALUES ("L10","Bhandup","Mumbai");


INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T1","Nilesh Parab","L1","9082286717","D1");
INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T2","Prajwal Shinde","L2","8067189056","D2");
INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T3","Vivek Tiwari","L3","8098768453","D3");
INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T4","Vishal Gupta","L4","8967564320","D4");
INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T5","Ayush Jaiswal","L5","8906754567","D5");
INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T6","Mohit Kulkarni","L6","7865479087","D6");
INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T7","Gaurang Lavlekar","L7","8765678987","D7");
INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T8","Muskaan Ladji","L8","789766719","D8");
INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T9","Ananya Yadav","L9","8224286817","D9");
INSERT INTO Transactions (TID, Name, Address, Phone_no, Tdate)
VALUES ("T10","Riya Singh","L10","9082111727","D10");

-- Roll Up
Select t.TID, t.Name, d.d_year 
From Transactions t, Dates d
Where d.D_ID=t.Tdate

-- Drill Down
Select t.TID, t.Name, l.region 
From Transactions t, Location l
Where l.LID=t.Address

-- Slicing
Select t.TID, t.Name, l.city 
From Transactions t, Location l
Where l.LID=t.Address and l.city="Mumbai"

-- Dicing
Select t.TID, t.Name, l.city, d.d_year
From Transactions t, Location l, Dates d 
Where l.LID=t.Address and d.D_ID=t.Tdate and l.city="Mumbai" and d.d_year>=2020;

-- Pivot
Select l.city, t.Name
From Transactions t, Location l
Where l.LID=t.Address 
