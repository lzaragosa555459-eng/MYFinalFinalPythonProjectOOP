create database carrentalsandservices;

use carrentalsandservices

create table Customer(
CustomerID INT AUTO_INCREMENT PRIMARY KEY,
Name varchar(20) not null,
Email varchar(30) not null,
Phone varchar(15) not null
);

create table Vehicle(
VehicleID INT AUTO_INCREMENT PRIMARY KEY,
type varchar(20) not null,
Make DATE not null,
Model varchar(20) not null,
totalCost INT not null
);

create table Rental(
RentalID INT AUTO_INCREMENT PRIMARY KEY,
RentalDate DATE not null,
ReturnDate DATE not null,
CustomerID INT,
FOREIGN KEY(CustomerID) REFERENCES Customer (CustomerID),
VehicleID INT,
FOREIGN KEY(VehicleID) REFERENCES Vehicle (VehicleID)
);

create table Payment(
PaymentID INT  AUTO_INCREMENT PRIMARY KEY,
PaymentMethod varchar(20) not null,
PaymentDate DATE not null,
Amount varchar(20) not null,
RentalID INT,
FOREIGN KEY (RentalID) REFERENCES Rental (RentalID)
);

INSERT INTO vehicle (VehicleID, Type, Make, Model,totalCost) VALUES
(1, 'Sedan', '2018-05-20', 'Toyota Corolla',8000),
(2, 'Sedan', '2019-07-14', 'Honda Civic',6000),
(3, 'Truck', '2020-03-11', 'Ford Ranger',5600),
(4, 'Truck', '2017-09-08', 'Nissan Navara',7000),
(5, 'SUV', '2021-02-25', 'Mitsubishi Montero S',6000),
(6, 'SUV', '2018-11-30', 'Chevrolet Trailblaze',7500),
(7, 'SUV', '2019-04-18', 'Hyundai Tucson',8500),
(8, 'SUV', '2020-12-05', 'Kia Sorento',5400),
(9, 'SUV', '2021-06-22', 'Mazda CX-5',6500),
(10, 'SUV', '2017-08-17', 'Subaru Forester',8600);
