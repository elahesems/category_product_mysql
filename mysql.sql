Use srs;
INSERT INTO Contacts(FirstName,LastName,MobilePhone,Address) VALUES ("name","lastName","+49 *** 99 99","142 street");
INSERT INTO Contacts(FirstName,LastName,MobilePhone,Address) VALUES ("name","lastName","+49 *** 55 22","152 street");
INSERT INTO Contacts(FirstName,LastName,MobilePhone,Address) VALUES ("name","lastName","+49 *** 99 99","1462 street");
INSERT INTO Contacts(FirstName,LastName,MobilePhone,Address) VALUES ("name","lastName","+49 *** 99 99","1427 street");
INSERT INTO Contacts(FirstName,LastName,MobilePhone,Address) VALUES ("name","lastName","+49 *** 99 99","152 street");

UPDATE Contacts SET MobilePhone="+90 545 *** 44 44" WHERE Id=26;
UPDATE Contacts SET LastName="Aslan", Address="2156 street" WHERE Id=26;

DELETE FROM Contacts;
DELETE FROM Contacts WHERE Id=26;


/* Selection */
SELECT * FROM Contacts;
SELECT Id FROM Contacts;
SELECT FirstName,LastName FROM Contacts;

SELECT * FROM Contacts WHERE Id=26;
SELECT * FROM Contacts WHERE LastName="Yılmaz";
SELECT * FROM Contacts WHERE LastName="Yılmaz" AND Address="152 street";
SELECT * FROM Contacts WHERE MobilePhone ="+49 999 99 99" OR FirstName="Berkan";
SELECT * FROM Contacts WHERE LastName="Yılmaz" AND NOT FirstName="Gizem";
SELECT * FROM Contacts ORDER BY FirstName;
SELECT * FROM Contacts ORDER BY FirstName ASC;
SELECT * FROM Contacts ORDER BY FirstName DESC;
SELECT * FROM Contacts WHERE Id BETWEEN 22 AND 24;
SELECT MIN(Id) FROM Contacts;
SELECT MAX(Id) FROM Contacts;
SELECT COUNT(Id) FROM Contacts;
SELECT AVG(Id) FROM Contacts;
SELECT SUM(Id) FROM Contacts;
SELECT * FROM Contacts WHERE FirstName LIKE "G%";
SELECT * FROM Contacts WHERE FirstName LIKE "%m";
SELECT * FROM Contacts WHERE FirstName LIKE "%a%";
SELECT * FROM Contacts WHERE FirstName LIKE "_h%";


