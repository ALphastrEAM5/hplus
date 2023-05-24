-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2023 at 04:17 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `covid`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookingpatient`
--

CREATE TABLE `bookingpatient` (
  `id` int(11) NOT NULL,
  `srfid` varchar(50) NOT NULL,
  `bedtype` varchar(50) NOT NULL,
  `hcode` varchar(50) NOT NULL,
  `spo2` int(11) NOT NULL,
  `pname` varchar(50) NOT NULL,
  `pphone` varchar(12) NOT NULL,
  `paddress` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookingpatient`
--

INSERT INTO `bookingpatient` (`id`, `srfid`, `bedtype`, `hcode`, `spo2`, `pname`, `pphone`, `paddress`) VALUES
(3, 'K2002120', 'HICUBed', 'MTHK80', 89, 'Pranab Guha', '0234842748', 'Sbei_SWJF Road'),
(4, '0940824', 'HICUBed', 'PTS051', 92, 'Arun', '09655035', 'dkfksjdfk'),
(5, 'Sabin', 'VENTILATORBed', 'MTHK80', 87, 'Parbina Khatun', '030485344', 'Raipur'),
(6, 'ABCD705', 'VENTILATORBed', 'JKH5K', 78, 'Arabind Ghosh', '40590353', 'City Street Salt lake'),
(7, 'ABCDEF', 'Choose Bed Type', 'MTHK80', 82, 'Rahul Dravid', '32937428', 'City Street Salt lake'),
(8, 'EFGHIJ', 'HICUBed', 'MTHK80', 92, 'Pranab', '932427842', 'Salt Lake'),
(9, 'gfg123', 'Choose Bed Type', 'PTS051', 88, 'Asis', '398938493', 'Haldia');

-- --------------------------------------------------------

--
-- Table structure for table `doctors`
--

CREATE TABLE `doctors` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `specialization` varchar(100) DEFAULT NULL,
  `degree` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctors`
--

INSERT INTO `doctors` (`id`, `name`, `email`, `specialization`, `degree`, `city`, `address`) VALUES
(1, 'Dr. Rajesh Gupta', 'drrajeshgupta@example.com', 'Cardiology', 'MD', 'Delhi', '123 Main St'),
(2, 'Dr. Sneha Patel', 'drsnehapatel@example.com', 'Dermatology', 'MBBS', 'Mumbai', '456 Park Ave'),
(3, 'Dr. Anu Verma', 'dranuverma@example.com', 'Pediatrics', 'MD', 'Chennai', '789 Elm St'),
(4, 'Dr. Rahul Singh', 'drrahulsingh@example.com', 'Orthopedics', 'MS', 'Kolkata', '567 Oak St'),
(5, 'Dr. Nisha Sharma', 'drnishasharma@example.com', 'Gynecology', 'MD', 'Bangalore', '890 Maple Ave'),
(6, 'Dr. Sanjay Kumar', 'drsanjaykumar@example.com', 'Neurology', 'MD', 'Delhi', '234 Elm St'),
(7, 'Dr. Pooja Mishra', 'drpoojamishra@example.com', 'Ophthalmology', 'MS', 'Mumbai', '345 Oak St'),
(8, 'Dr. Mohan Sharma', 'drmohansharma@example.com', 'Endocrinology', 'MD', 'Delhi', '456 Main St'),
(9, 'Dr. Reena Gupta', 'drreenagupta@example.com', 'Psychiatry', 'MD', 'Mumbai', '567 Park Ave'),
(10, 'Dr. Siddharth Reddy', 'dr.siddharthreddy@example.com', 'Oncology', 'DM', 'Chennai', '678 Elm St'),
(11, 'Dr. Priya Khanna', 'drpriyakhanna@example.com', 'Dentistry', 'BDS', 'Kolkata', '789 Oak St'),
(12, 'Dr. Vivek Kumar', 'drvivekkumar@example.com', 'ENT', 'MS', 'Bangalore', '890 Maple Ave'),
(13, 'Dr. Nisha Verma', 'drnishaverma@example.com', 'Cardiology', 'DM', 'Delhi', '901 Elm St'),
(14, 'Dr. Rakesh Patel', 'drrakeshpatel@example.com', 'Dermatology', 'MD', 'Mumbai', '123 Park Ave'),
(15, 'Dr. Shalini Rao', 'drshalinirao@example.com', 'Pediatrics', 'MD', 'Chennai', '234 Elm St'),
(16, 'Dr. Sameer Desai', 'drsameerdesai@example.com', 'Orthopedics', 'MS', 'Kolkata', '345 Oak St'),
(17, 'Dr. Meera Singh', 'drmeerasingh@example.com', 'Gynecology', 'MD', 'Bangalore', '456 Maple Ave'),
(18, 'Dr. Sunil Sharma', 'drsunilsharma@example.com', 'Neurology', 'DM', 'Delhi', '567 Elm St'),
(19, 'Dr. Poonam Gupta', 'drpoonamgupta@example.com', 'Ophthalmology', 'MS', 'Mumbai', '678 Oak St'),
(20, 'Dr. Rohit Kumar', 'drrohitkumar@example.com', 'Endocrinology', 'MD', 'Chennai', '789 Elm St'),
(21, 'Dr. Anjali Sinha', 'dranjalisinha@example.com', 'Psychiatry', 'MD', 'Kolkata', '890 Oak St'),
(22, 'Dr. Arjun Sharma', 'drarjunsharma@example.com', 'Oncology', 'DM', 'Bangalore', '901 Maple Ave'),
(23, 'Dr. Neetu Kapoor', 'drneetukapoor@example.com', 'Dentistry', 'BDS', 'Delhi', '123 Elm St'),
(24, 'Dr. Rahul Desai', 'drrahuldesai@example.com', 'ENT', 'MS', 'Mumbai', '234 Oak St'),
(25, 'Dr. Shikha Reddy', 'dr.shikhareddy@example.com', 'Cardiology', 'DM', 'Chennai', '345 Elm St'),
(26, 'Dr. Vikram Patel', 'drvikrampatel@example.com', 'Dermatology', 'MD', 'Kolkata', '456 Oak St'),
(27, 'Dr. Preeti Rao', 'drpreetirao@example.com', 'Pediatrics', 'MD', 'Bangalore', '567 Maple Ave');

-- --------------------------------------------------------

--
-- Table structure for table `hospitaldata`
--

CREATE TABLE `hospitaldata` (
  `id` int(11) NOT NULL,
  `hcode` varchar(200) NOT NULL,
  `hname` varchar(200) NOT NULL,
  `normalbed` int(11) NOT NULL,
  `hicubed` int(11) NOT NULL,
  `icubed` int(11) NOT NULL,
  `vbed` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hospitaldata`
--

INSERT INTO `hospitaldata` (`id`, `hcode`, `hname`, `normalbed`, `hicubed`, `icubed`, `vbed`) VALUES
(11, 'BBH01', 'Bangalore Baptist Hospital', 76, 43, 56, 2),
(12, 'MTHK80', 'Vizianagaram Matha Hospital', 45, 85, 23, 3),
(13, 'PTS051', 'Pune', 455, 655, 345, 45),
(18, 'RIEISH-002', 'Raipurjila Hospital', 35, 56, 24, 567);

-- --------------------------------------------------------

--
-- Table structure for table `hospitaluser`
--

CREATE TABLE `hospitaluser` (
  `id` int(11) NOT NULL,
  `hcode` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hospitaluser`
--

INSERT INTO `hospitaluser` (`id`, `hcode`, `email`, `password`) VALUES
(18, 'BBH01', 'sarbanibiswas04538@gmail.com', 'pbkdf2:sha256:260000$H1sXz0B6TqwhBtA9$bb4a86ed329a75da784726d410805fedc3f5483328efcff15532f45447cc84d5'),
(24, 'MTHK80', 'abirbiswas20023010@gmail.com', 'pbkdf2:sha256:260000$yicKHykk5Lr85ch2$a30d45ad6290c5c45ad57e7dd3ebf8deb940ed2dde51ec583e8dffd1613ea217'),
(29, 'PTS051', 'rahul20587@iiitkalyani.ac.in', 'pbkdf2:sha256:260000$bEATLGC63cP7uruA$e21ed7b9b7684ecf9ad456ff7fbb0db3e96c6d9f6c2b3b91da2efb5354ec9800'),
(39, 'RIEISH-002', 'spihbdcpj@gmail.com', 'pbkdf2:sha256:260000$xXwd3x2niKxJqsPI$2289153f11459a56b153923cb5ad8b9f464bbb6052c977faebe6bae662257c4e');

-- --------------------------------------------------------

--
-- Table structure for table `medical_data`
--

CREATE TABLE `medical_data` (
  `id` int(11) NOT NULL,
  `hcode` varchar(30) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `tests` varchar(100) DEFAULT NULL,
  `schedules` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `medical_data`
--

INSERT INTO `medical_data` (`id`, `hcode`, `postal_code`, `tests`, `schedules`) VALUES
(1, 'MTHK80', '123456', 'Blood Test', '2023-05-16 09:00:00'),
(2, 'BBH01', '234567', 'X-ray', '2023-05-17 14:30:00'),
(3, 'BBH01', '234567', 'MRI', '2023-05-18 11:15:00'),
(4, 'BBH01', '234567', 'Ultrasound', '2023-05-19 08:45:00'),
(5, 'MTHK80', '123456', 'EKG', '2023-05-20 13:00:00'),
(6, 'PTS051', '345678', 'Blood Test', '2023-05-23 10:30:00'),
(7, 'PTS051', '345678', 'X-ray', '2023-05-24 15:45:00'),
(8, 'BBH01', '234567', 'MRI', '2023-05-25 12:30:00'),
(9, 'RIEISH-002', '567890', 'Ultrasound', '2023-05-26 07:15:00'),
(10, 'RIEISH-002', '567890', 'EKG', '2023-05-27 11:45:00');

-- --------------------------------------------------------

--
-- Table structure for table `pkgs`
--

CREATE TABLE `pkgs` (
  `id` int(11) NOT NULL,
  `hcode` varchar(30) DEFAULT NULL,
  `hname` varchar(100) DEFAULT NULL,
  `packages` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pkgs`
--

INSERT INTO `pkgs` (`id`, `hcode`, `hname`, `packages`) VALUES
(1, 'BBH01', 'Bangalore Baptist Hospital', 'SURAKSHA SMART CHECK'),
(2, 'PTS051', 'Pune', '60 PLUS MALES'),
(3, 'MTHK80', 'Vizianagaram Matha Hospital', '60 PLUS FEMALES'),
(4, 'PTS051', 'Pune', '40 PLUS MALES'),
(5, 'RIEISH-002', 'Raipurjila Hospital', '40 PLUS FEMALES'),
(6, 'PTS051', 'Pune', 'SURAKSHA WOMEN GOLD+'),
(7, 'MTHK80', 'Vizianagaram Matha Hospital', 'SURAKSHA SENIOR MALE'),
(8, 'RIEISH-002', 'Raipurjila Hospital', 'SURAKSHA SENIOR FEMALE'),
(9, 'BBH01', 'Bangalore Baptist Hospital', 'SURAKSHA WOMEN GOLD'),
(10, 'RIEISH-002', 'Raipurjila Hospital', 'SURAKSHA MEN GOLD'),
(11, 'RIEISH-002', 'Raipurjila Hospital', 'SURAKSHA MEN GOLD+'),
(12, 'RIEISH-002', 'Raipurjila Hospital', 'HEALTH PACKAGE BASIC'),
(13, 'PTS051', 'Pune', 'HEALTH PACKAGE ADVANCED'),
(14, 'MTHK80', 'Vizianagaram Matha Hospital', 'HEALTH CHECK FOR TEENS(FEMALE)'),
(15, 'BBH01', 'Bangalore Baptist Hospital', 'HEALTH CHECK FOR TEENS(MALE)'),
(16, 'MTHK80', 'Vizianagaram Matha Hospital', 'SURAKSHA PRE-MARRIAGE PROFILE-FEMALE'),
(17, 'RIEISH-002', 'Raipurjila Hospital', 'SURAKSHA PRE-MARRIAGE PROFILE-MALE'),
(18, 'PTS051', 'Pune', 'SURAKSHA IMMUNITY CHECK BASIC PANEL');

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`) VALUES
(1, 'abir'),
(2, 'binay');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `srfid` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `srfid`, `email`, `dob`) VALUES
(5, 'K2002120', 'abirbiswas@gmail.com', 'pbkdf2:sha256:260000$28nDFQtoWeUDOswY$11c0130888292827e50f4509073a15138db0e1ab8cda58583ba045a76930dd08'),
(6, '0940824', 'jdkjaefjhjf@gmail.com', 'pbkdf2:sha256:260000$ehfsHCrdFoGel3XX$19ddf2646635c31c7711e6d49cb96c0446788e07b50fd0a068bf99f86f8f0675'),
(7, 'Sabin', 'sabin5084@gmail.com', 'pbkdf2:sha256:260000$976P1UCT3P0bzlaF$575f24c5250dd42f1ebcbc0583a9a6c574583fb240b6826f5ea857e6a72a8f1f'),
(8, 'ABCD705', 'sbih@gmai.com', 'pbkdf2:sha256:260000$HT8z2cE4MUYFPw4d$ee27dc0ca68d412f9ef4deed7bd350b995ff43c7ae79882114b73c78664a7d0a'),
(9, 'ABCDEF', 'rahul77@gmail.com', 'pbkdf2:sha256:260000$YSGnXr3WPCGVOp4h$35f3b60f8f77133cd6f293867020bf0759a369165bb85cfe28efd32814aa5e1b'),
(10, 'EFGHIJ', 'abir2002@gmail.com', 'pbkdf2:sha256:260000$y2le1cmoNnqayNcO$f5bc620f3c3bde313f82bccedfa52df0d44763e99d06acb02e0f91b8c4ec2a95'),
(11, 'gfg123', 'gfg123@gmail.com', 'pbkdf2:sha256:260000$QY1u1T0ysMKnCPnE$2d9a3963452e2b04384dd792551ccfa1a401a6c0ae5409b5ab926a55f6b25952');

-- --------------------------------------------------------

--
-- Table structure for table `visiting`
--

CREATE TABLE `visiting` (
  `id` int(11) NOT NULL,
  `hcode` varchar(30) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `appointment` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `visiting`
--

INSERT INTO `visiting` (`id`, `hcode`, `name`, `location`, `appointment`) VALUES
(1, 'RIEISH-002', 'Dr. Rajesh Gupta', 'Delhi', '2023-05-16 09:00:00'),
(2, 'BBH01', 'Dr. Nisha Verma', 'Delhi', '2023-05-18 10:30:00'),
(3, 'MTHK80', 'Dr. Sneha Patel', 'Mumbai', '2023-05-17 14:30:00'),
(4, 'RIEISH-002', 'Dr. Rakesh Patel', 'Mumbai', '2023-05-19 11:00:00'),
(5, 'MTHK80', 'Dr. Anu Verma', 'Chennai', '2023-05-18 11:15:00'),
(6, 'PTS051', 'Dr. Shalini Rao', 'Chennai', '2023-05-20 09:30:00'),
(7, 'PTS051', 'Dr. Siddharth Reddy', 'Kolkata', '2023-05-19 08:45:00'),
(8, 'RIEISH-002', 'Dr. Sameer Desai', 'Kolkata', '2023-05-21 10:00:00'),
(9, 'MTHK80', 'Dr. Vivek Kumar', 'Bangalore', '2023-05-20 13:00:00'),
(10, 'RIEISH-002', 'Dr. Meera Singh', 'Bangalore', '2023-05-22 15:30:00'),
(11, 'BBH01', 'Dr. Mohan Sharma', 'Delhi', '2023-05-23 10:30:00'),
(12, 'MTHK80', 'Dr. Poonam Gupta', 'Delhi', '2023-05-25 11:45:00'),
(13, 'PTS051', 'Dr. Reena Gupta', 'Mumbai', '2023-05-24 15:45:00'),
(14, 'BBH01', 'Dr. Vikram Patel', 'Mumbai', '2023-05-26 12:00:00'),
(15, 'MTHK80', 'Dr. Priya Khanna', 'Chennai', '2023-05-25 12:30:00'),
(16, 'PTS051', 'Dr. Preeti Rao', 'Chennai', '2023-05-27 09:15:00'),
(17, 'MTHK80', 'Dr. Rahul Singh', 'Kolkata', '2023-05-26 07:15:00'),
(18, 'PTS051', 'Dr. Shikha Reddy', 'Kolkata', '2023-05-28 10:45:00'),
(19, 'MTHK80', 'Dr. Nisha Sharma', 'Bangalore', '2023-05-27 11:45:00'),
(20, 'BBH01', 'Dr. Rahul Desai', 'Bangalore', '2023-05-29 13:30:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookingpatient`
--
ALTER TABLE `bookingpatient`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `srfid` (`srfid`);

--
-- Indexes for table `doctors`
--
ALTER TABLE `doctors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hospitaldata`
--
ALTER TABLE `hospitaldata`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `hcode` (`hcode`),
  ADD UNIQUE KEY `hcode_2` (`hcode`);

--
-- Indexes for table `hospitaluser`
--
ALTER TABLE `hospitaluser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `hcode` (`hcode`);

--
-- Indexes for table `medical_data`
--
ALTER TABLE `medical_data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pkgs`
--
ALTER TABLE `pkgs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `srfid` (`srfid`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `visiting`
--
ALTER TABLE `visiting`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookingpatient`
--
ALTER TABLE `bookingpatient`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `doctors`
--
ALTER TABLE `doctors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `hospitaldata`
--
ALTER TABLE `hospitaldata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `hospitaluser`
--
ALTER TABLE `hospitaluser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT for table `medical_data`
--
ALTER TABLE `medical_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `pkgs`
--
ALTER TABLE `pkgs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `visiting`
--
ALTER TABLE `visiting`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bookingpatient`
--
ALTER TABLE `bookingpatient`
  ADD CONSTRAINT `bookingpatient_ibfk_1` FOREIGN KEY (`srfid`) REFERENCES `user` (`srfid`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `hospitaldata`
--
ALTER TABLE `hospitaldata`
  ADD CONSTRAINT `hospitaldata_ibfk_1` FOREIGN KEY (`hcode`) REFERENCES `hospitaluser` (`hcode`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
