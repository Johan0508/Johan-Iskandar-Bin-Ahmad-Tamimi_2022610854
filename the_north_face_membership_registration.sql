-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 04:01 PM
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
-- Database: `the_north_face_membership_registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `membership_registration`
--

CREATE TABLE `membership_registration` (
  `FirstName` text NOT NULL,
  `LastName` text NOT NULL,
  `ContactNumber` varchar(12) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Address` varchar(125) NOT NULL,
  `country_name` text NOT NULL,
  `currency_name` varchar(50) NOT NULL,
  `paymentmethod_name` varchar(50) NOT NULL,
  `membershipstatus_select` text NOT NULL,
  `result_label` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `membership_registration`
--

INSERT INTO `membership_registration` (`FirstName`, `LastName`, `ContactNumber`, `Email`, `Address`, `country_name`, `currency_name`, `paymentmethod_name`, `membershipstatus_select`, `result_label`) VALUES
('', '', '', '', '', 'United Kingdom', 'Sterling', 'Google Pay', '', 'Membership Fee: £34.0'),
('MUHAMMAD HANIF AIMAN ', 'BIN KAMARUZAMAN ', '01121955708', 'hanifaiman2004@gmail.com', 'Kuala Berang, hulu Terengganu, Terengganu', 'Singapore', 'Singapore dollar', 'Financial Process Exchange (FPX)', 'Current Member', 'Membership Fee: $40.124'),
('MUHAMMAD AMMAR ', 'KHAMISAN', '0149307134', 'AMMAR@gmail.com', 'Kolej Malinja UITM KEDAH', 'United Kingdom', 'Sterling', 'Google Pay', 'Current Member', 'Membership Fee: £23.8'),
('JOHAN ', 'ISKANDAR ', '0184063913', 'ISKNDR05082gmail.com', 'Selangor, Petaling Jaya, Sungai Way', 'Malaysia', 'Malaysian Ringgit', 'Financial Process Exchange (FPX)', 'Current Member', 'Membership Fee: RM140.0'),
('MOHD ZARIF ZAFRAN', 'KUZAIRI', '01278837462', 'ZARIF2KUZAIRI@GMAIL.COM', 'TELUK INTAN, PERAK, MALAYSIA', 'United Kingdom', 'Sterling', 'PayPal', 'New Member', 'Membership Fee: £32.3'),
('LEE  ', 'CHIE SIE ', '0126627361', 'LEE5566@gmail.com', 'port dickson, negeri sembilan, Malaysia', 'Singapore', 'Singapore dollar', 'Google Pay', 'Current Member', 'Membership Fee: $40.124'),
('MUHAMMAD ', 'AFHAM', '01128567340', 'afhammahathir11@gmail.com', '149 persiaran chandan 9 Taman Chandan putri kuala kangsar Perak 33000', 'Malaysia', 'Malaysian Ringgit', 'VisaCard', 'New Member', 'Membership Fee: RM190.0'),
('MUHAMMAD', 'ZARIF HILMAN', '0175468718', 'ZARIFHILMAN15@gmail.com', 'Taman kurau sejati', 'Malaysia', 'Malaysian Ringgit', 'VisaCard', 'New Member', 'Membership Fee: RM190.0');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
