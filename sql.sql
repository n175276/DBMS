

CREATE TABLE Gallery(
  ID varchar(5) ,
  name varchar(30) ,
  location varchar(20),
  PRIMARY KEY (ID)
);

insert into Gallery values('78546','Kalakriti Art Gallery','New Delhi');
insert into Gallery values('97851','Dhoomimal Art Gallery','New Delhi');
insert into Gallery values('98745','e Art Art Gallery','Mumbai');
insert into Gallery values('99874','Jehangir Art Gallery','New Delhi');
insert into Gallery values('12854','Darpan Art Gallery','Lahore');
insert into Gallery values('14785','Abstract Art Gallery','Banglore');
insert into Gallery values('14987','Gitanjali Art Gallery','Goa');
insert into Gallery values('18745','Studio3 Art Gallery','Mumbai');
insert into Gallery values('12658','Tilting Art Gallery','Mumbai');
insert into Gallery values('12546','Creative Space Art Gallery','Jalgaon');

CREATE TABLE Artist (
  ArtistId varchar(5) ,
  name varchar(20) ,
  address varchar(20) ,
  mobile varchar(10) ,
  G_id varchar(5) ,
  PRIMARY KEY (ArtistId),
  FOREIGN KEY (G_id) REFERENCES Gallery(ID)  ON DELETE CASCADE
) ;

insert into Artist values('54875','Prabhakar', 'Jalgaon', '7775256210', '12546');
insert into Artist values('95864', 'Tyeb Mehta', 'Mumbai', '8574956812','12658');
insert into Artist values('85742', 'Satish Gujral','Lahore','8574632145', '12854');
insert into Artist values('85126', 'Sheela Gowda', 'Banglore', '9587154523', '14785');
insert into Artist values('45785', 'Nikhil Chopra', 'Goa', '5478523654', '14987');
insert into Artist values('78547','Shilpa Gupta', 'Mumbai', '9587549874', '18745');
insert into Artist values('65478', 'Thukral & Tagra', 'New Delhi', '1254796356', '78546');
insert into Artist values('36584', 'Sahej Rahal', 'Mumbai', '7854124578', '98745');
insert into Artist values('36812', 'Asim Waqif', 'New Delhi', '7852783245', '99874');
insert into Artist values('37812', 'Himali Singh Soin', 'New Delhi', '7852543245', '99874');

CREATE TABLE `Customer` (
  `cust_id` varchar(5) ,
  `cust_name` varchar(20) ,
  `cust_addr` varchar(20) ,
  `painting_id` varchar(5),
  `mobile` varchar(10),
  `cost` varchar(10) ,
  PRIMARY KEY (`cust_id`)
) ;

insert into Customer values('12129','Rahul Sharma','Mumbai','52','9587456895','10000');
insert into Customer values('78545','Radhika Sartaj','Dehradun','85','9581285895','20000');
insert into Customer values('12475','Sairaj Roy','Goa','21','8574265124','25000');
insert into Customer values('12545', 'Anjali Mehta', 'Mumbai', '22','9558745854','50200');
insert into Customer values('78544', 'Ranvijay Kapoor', 'Nashik','30','9587452364','30000'); 
insert into Customer values('85745','Bennie Young', 'Ahmednagar', '25','9558746178','35000');
insert into Customer values('85985','Sonia Bajaj','Goa','35','9551000785','31000');
insert into Customer values('12547','Ana Jordan', 'Mumbai','48','985475320','40800');
insert into Customer values('54785','Cheryl Neal', 'Mumbai','51','8745100215','78000');
insert into Customer values('57895','Maya Pingle','Navi Mumbai','63','7845951000','71000');
insert into Customer values('51236','Sai Pathak','Raipur','69','7845005410','98000');
insert into Customer values('48596','Vasuda Bhatt','Mumbai','76','9874568745','100000');
insert into Customer values('47895','Samrat Pathak','Mumbai','82','7002589422','120000');
insert into Customer values('12897','Kalinda Trivedi','Mumbai','89','9552143871','200500');
DELETE from customer where cust_id = "49953";

CREATE TABLE `Exhibition` (
  `ID` varchar(5) ,
  `Start_Date` date DEFAULT NULL,
  `End_Date` date DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ;
insert into Exhibition values('101','2021/11/26','2021/11/28');
insert into Exhibition values('102','2021/11/27','2021/11/30');
insert into Exhibition values('103','2021/12/12','2021/12/15');
insert into Exhibition values('104','2021/12/18','2021/12/20');

CREATE TABLE `exhibition_artists` (
  `ID` varchar(5),
  `ExhibitionId` varchar(5),
  `ArtistId` varchar(5),
   PRIMARY KEY (`ID`)
) ;
insert into exhibition_artists values('1','201','98745');
insert into exhibition_artists values('2','202','18745');
insert into exhibition_artists values('3','203','78546');
insert into exhibition_artists values('4','101','14785');
insert into exhibition_artists values('5','101','98745');
insert into exhibition_artists values('6','101','14785');
insert into exhibition_artists values('7','201','18745');

CREATE TABLE `contains` (
  `a_id` varchar(5) ,
  `e_id` varchar(5),
  PRIMARY KEY (`a_id`,`e_id`),
  FOREIGN KEY (`a_id`) REFERENCES `exhibition_artists` (`ID`),
  FOREIGN KEY (`e_id`) REFERENCES `Exhibition` (`ID`)
) ;

insert into contains values('1','101');
insert into contains values('2','102');
insert into contains values('3','101');
insert into contains values('4','101');


CREATE TABLE `Organize` (
  `e_id` varchar(5) ,
  `g_id` varchar(5),
  PRIMARY KEY (`e_id`),
  FOREIGN KEY (`g_id`) REFERENCES `Gallery` (`ID`) ON DELETE CASCADE,
  FOREIGN KEY (`e_id`) REFERENCES `Exhibition` (`ID`) ON DELETE CASCADE
) ;


insert into Organize values('101','97851');
insert into Organize values('102','12854');
insert into Organize values('103','18745');


CREATE TABLE `Painting` (
  `ID` varchar(5),
  `title` varchar(20) ,
  `year` varchar(4),
  `a_id` varchar(5),
  PRIMARY KEY (`ID`),
  FOREIGN KEY (`a_id`) REFERENCES `Artist` (`ArtistId`)
) ;

insert into Painting values('13','Dream','2020','54875');
insert into Painting values('21','Eye','2018','95864');
insert into Painting values('22','Modern Art','2021','85742');
insert into Painting values('52','Heartless','2017','85126');
insert into Painting values('53','Husn','2019','45785');

CREATE TABLE `Brought_By` (
  `p_id` varchar(5) ,
  `c_id` varchar(5) ,
  PRIMARY KEY (`p_id`),
  FOREIGN KEY (`p_id`) REFERENCES `Painting` (`ID`) 
         ON DELETE CASCADE,
  FOREIGN KEY (`c_id`) REFERENCES `Customer` (`cust_id`) 
         ON DELETE CASCADE
) ;
insert into Brought_By values('13','78545');
insert into Brought_By values('21', '85745');
insert into Brought_By values('22','12545');
insert into Brought_By values('52', '85985');
insert into Brought_By values('53', '12475');

