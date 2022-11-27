
DROP SCHEMA IF EXISTS cook_county_home_sales2;

CREATE SCHEMA cook_county2;


CREATE TABLE cook_county2.cook_county_home_sales2
(
  `Property_Class` int,
  `Property_Address` text,
  `Property_City` text,
  `Sale_Date` datetime,
  `Sale_Price`  decimal(10,2),
  `Land_Square_Feet` decimal(10,2),
  `Age` int,
  `Bedrooms` int,
  `Rooms` int,
  `Basement` text,
  `Central_Heating` text,
  `Central_Air_Conditioning` text,
  `Fireplaces` int,
  `Full_Baths` int,
  `Half_Baths` decimal(7,2),
  `Sale_Year` int,
  `Sale_Month` text
);

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\cook_county_sales_data.csv' 
INTO TABLE cook_county2.cook_county_home_sales2
FIELDS TERMINATED BY ',' 
       OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;