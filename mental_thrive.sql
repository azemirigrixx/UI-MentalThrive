-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 30, 2024 at 03:40 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mental_thrive`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_portal`
--

CREATE TABLE `admin_portal` (
  `id` int(255) NOT NULL,
  `Aemail` varchar(255) NOT NULL,
  `Apassword` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_portal`
--

INSERT INTO `admin_portal` (`id`, `Aemail`, `Apassword`) VALUES
(2, 'mima@phinmaed.com', 'mima123!');

-- --------------------------------------------------------

--
-- Table structure for table `counselor_portal`
--

CREATE TABLE `counselor_portal` (
  `counselor_id` int(11) NOT NULL,
  `Cemail` varchar(255) NOT NULL,
  `Cpassword` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `counselor_portal`
--

INSERT INTO `counselor_portal` (`counselor_id`, `Cemail`, `Cpassword`) VALUES
(16, 'jeje@phinmaed.com', '$2b$12$wba9P3BDjEoijJvp/JqmGuDP1Cea7053B2QcvHOqmZ4O2eyBfvaxu'),
(17, 'ben@phinmaed.com', '$2b$12$ZbVyn1WybZBnLTq6Dddl5uAT9VEGCep.HLCI3dn/Sau.48YrGU652'),
(18, 'grace@phinmaed.com', '$2b$12$8V8GmqIhGgwGQk2fHJy8QO7BfN5kdkZKmO9HIhlTUIdLnFEcIK1si'),
(21, 'karen@phinmaed.com', '$2b$12$9QL3mrllTjpNMK2lO2UQ.u91fQ6OFrbcu3WUfYSeCryYKe41B6V0K'),
(22, 'kaka@phinmaed.com', '$2b$12$.mmevST3mXpxpj1Zft1dEeB0i6QINfhcN6/qVONe.7opKXetBpwL2'),
(23, 'jema@phinmaed.com', '$2b$12$0fd6.qJUb7V82XDa5GRwGOS9LUlFfBOOr/uHSSRjCjiXu4KDRFdRm'),
(25, 'jema@phinmaed.com', '$2b$12$nQwLcUHKhmudgiifP4L2pupAQmskItN7Ydg91kREnSL0237tSIMxq'),
(26, 'jemima@phinmaed.com', '$2b$12$boMl1IcrlOjn4eh0i534I.S4WeyJ9ZFPn9yrwch3oSHzlTnvkhO0i'),
(27, 'mima@phinmaed.com', '$2b$12$TiZuKYr0GGFJKAOGCaz1EOYMLeGpIQbrum6oe54gEPrRDuHG9TOtu');

-- --------------------------------------------------------

--
-- Table structure for table `student_form`
--

CREATE TABLE `student_form` (
  `form_id` int(11) NOT NULL,
  `fattempt` int(11) NOT NULL,
  `fcomment` varchar(255) NOT NULL,
  `fresult` varchar(255) NOT NULL,
  `ftime` varchar(255) NOT NULL,
  `fday` int(11) NOT NULL,
  `fmonth` int(11) NOT NULL,
  `fyear` int(11) NOT NULL,
  `dep_result` varchar(255) NOT NULL,
  `anx_result` varchar(255) NOT NULL,
  `stress_result` varchar(255) NOT NULL,
  `dep_score` int(11) NOT NULL,
  `anx_score` int(11) NOT NULL,
  `stress_score` int(11) NOT NULL,
  `Fid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_form`
--

INSERT INTO `student_form` (`form_id`, `fattempt`, `fcomment`, `fresult`, `ftime`, `fday`, `fmonth`, `fyear`, `dep_result`, `anx_result`, `stress_result`, `dep_score`, `anx_score`, `stress_score`, `Fid`) VALUES
(1, 0, 'I\'m okey I\'m fine gwenchana', '', '10:44 AM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Severe', 32, 40, 32, NULL),
(2, 0, 'oke lang eh', '', '10:51 AM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 36, 40, 34, NULL),
(3, 0, 'herjefdf', '', '12:33 PM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 34, 32, 38, NULL),
(4, 0, 'heeeee', '', '12:34 PM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 28, 24, 34, NULL),
(5, 0, 'okay lang', '', '01:56 PM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 28, 36, 40, NULL),
(6, 0, 'okay lang po', '', '01:59 PM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 30, 36, 38, NULL),
(7, 0, 'okay langpowsss', '', '02:22 PM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 32, 28, 36, NULL),
(8, 0, 'okae langf.', '', '05:42 PM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Severe', 38, 28, 32, NULL),
(9, 0, 'okae langf.', '', '05:43 PM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Severe', 38, 28, 32, NULL),
(10, 0, 'Howayooo', '', '06:19 PM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Severe', 28, 26, 32, NULL),
(11, 0, 'bruhhhh', '', '06:22 PM', 30, 1, 2024, 'Moderate', 'Extremely Severe', 'Moderate', 20, 26, 22, NULL),
(12, 0, 'please I need to talk to someone', '', '06:24 PM', 30, 1, 2024, 'Extremely Severe', 'Extremely Severe', 'Extremely Severe', 34, 32, 36, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `student_portal`
--

CREATE TABLE `student_portal` (
  `student_id` int(255) NOT NULL,
  `Semail` varchar(255) NOT NULL,
  `Sfirst_name` varchar(255) NOT NULL,
  `Slast_name` varchar(255) NOT NULL,
  `Sid_number` varchar(255) NOT NULL,
  `Scourse` varchar(255) NOT NULL,
  `Spassword` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student_portal`
--

INSERT INTO `student_portal` (`student_id`, `Semail`, `Sfirst_name`, `Slast_name`, `Sid_number`, `Scourse`, `Spassword`) VALUES
(1, 'jeje@phinmaed.com', '', '', '', '', '$2b$12$t4zsiYIwZFqpzNYMS/GmWOJSbpo3XVdy/KTY5qU2fSC7fcKCrKDZC'),
(2, 'mekini@phinmaed.com', '', '', '', '', '$2b$12$WtU4i/x6PLXOkigbS/krsu2Vhe1KsWlpAXUK/oP3tdeOSgJznggU6'),
(3, 'jemima@phinamed.com', '', '', '', '', '$2b$12$rve7h/tCGh2huGx1zOCH..7GEDY.pSaFP0n9j0AX.CM95NuyL6Sni'),
(7, 'mima@phinmaed.com', 'mima', 'mariano', '04-2122-032201', 'BSIT', '$2b$12$J5s6ZLVxZqbzaPW5bSTPZOQINKElYX5rBqBxE3PJ3dCOPW9MlDrY2'),
(8, 'karen@phinmaed.com', 'Karen', 'Gaytano', '04-2122-032201', 'BSIT', '$2b$12$4sUUzb5sq8zHssTO9KXeguY7IOv6B4Bv0MVjiHMvPA/G3ncIrwk0C'),
(9, 'grace@phinmaed.comm', 'grace', 'Gaytano', '04-2122-345454', 'BSIT', '$2b$12$Eb1J9y9QIJS7RA/PZVXFru8j9cyNUY2zU4KOUbXqFjCjotgu.fgzq'),
(10, 'mg@gmail.com', 'Grace', 'Tabarnero', '04-1920-00805', 'BSIT', '$2b$12$it.FrsU9L2OEh9Nu2U6Fq.Lf5N4IVcOQEbXcwgCVfXnCikfgkIDXi'),
(11, 'kar@phinmaed.com', 'Karen', 'Gaytano', '04-2122-032201', 'bbsit', '$2b$12$tAWDTnhoWchsgHFRH/1pf.PrHl91ZpoIbZGqHPy.GOk9wtjLy.GHe');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_portal`
--
ALTER TABLE `admin_portal`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `counselor_portal`
--
ALTER TABLE `counselor_portal`
  ADD PRIMARY KEY (`counselor_id`);

--
-- Indexes for table `student_form`
--
ALTER TABLE `student_form`
  ADD PRIMARY KEY (`form_id`),
  ADD KEY `Fid` (`Fid`);

--
-- Indexes for table `student_portal`
--
ALTER TABLE `student_portal`
  ADD PRIMARY KEY (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_portal`
--
ALTER TABLE `admin_portal`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `counselor_portal`
--
ALTER TABLE `counselor_portal`
  MODIFY `counselor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `student_form`
--
ALTER TABLE `student_form`
  MODIFY `form_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `student_portal`
--
ALTER TABLE `student_portal`
  MODIFY `student_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `student_form`
--
ALTER TABLE `student_form`
  ADD CONSTRAINT `student_form_ibfk_1` FOREIGN KEY (`Fid`) REFERENCES `student_portal` (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
