-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 28, 2021 at 08:00 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `playlist`
--

-- --------------------------------------------------------

--
-- Table structure for table `playlist`
--

CREATE TABLE `playlist` (
  `Name` text NOT NULL,
  `Genre` text NOT NULL,
  `Link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `playlist`
--

INSERT INTO `playlist` (`Name`, `Genre`, `Link`) VALUES
('O Humdum Suniyo Re\r\n\r\n', 'Happy', 'https://www.youtube.com/watch?v=_9geEbZIAJM'),
('Patakha Guddi', 'Happy', 'https://www.youtube.com/watch?v=8HDTS80dlr4'),
('Rubaroo', 'Happy', 'https://www.youtube.com/watch?v=N9nRKJ0mHHg'),
('Bum bum bole', 'Happy', 'https://www.youtube.com/watch?v=NJ1NIIdHhXs'),
('Selfie le le re', 'Happy', 'https://www.youtube.com/watch?v=TITGBTGJZS8'),
('Ik Junoon', 'Happy', 'https://www.youtube.com/watch?v=ivUXoV0qLpE'),
('Khwabon Ke Parindey', 'Happy', 'https://www.youtube.com/watch?v=cscdqZUdgCk'),
('Maston Ka Jhund', 'Happy', 'https://www.youtube.com/watch?v=yWeVII7qF3A'),
('Meethi Boliyan', 'Happy', 'https://www.youtube.com/watch?v=BO9cos32DYc'),
('Meethi Boliyan', 'Happy', 'https://www.youtube.com/watch?v=BO9cos32DYc'),
('Salaam India', 'Happy', 'https://www.youtube.com/watch?v=iii1NM-Zv1g'),
('Kabira', 'Sad', 'https://www.youtube.com/watch?v=jHNNMj5bNQw'),
('Agar Tum Saath Ho', 'Sad', 'https://www.youtube.com/watch?v=sK7riqg2mr4'),
('Mana Ke Hum Yaar Nahi', 'Sad', 'https://www.youtube.com/watch?v=k4R39ofX-CQ'),
('Channa Mereya', 'Sad', 'https://www.youtube.com/watch?v=bzSTpdcs-EI'),
('Phir Le Aaya Dil', 'Sad', 'https://www.youtube.com/watch?v=-RAsJ6dAF68'),
('Main Rahoon Ya Na Rahoon', 'Sad', 'https://www.youtube.com/watch?v=Dp6lbdoprZ0'),
('Humdard', 'Sad', 'https://www.youtube.com/watch?v=FJ55SHCzt88'),
('Bulleya', 'Sad', 'https://www.youtube.com/watch?v=wTgrZE9RWNY'),
('Tujhe Bhula Diya', 'Sad', 'https://www.youtube.com/watch?v=-Hb2DeHvvEg'),
('Yeh Dooriyan', 'Sad', 'https://www.youtube.com/watch?v=yJqcJE2RL8E'),
('Saadda hakk', 'Angry', 'https://www.youtube.com/watch?v=p9DQINKZxWE'),
('Jatt da mukabla', 'Angry', 'https://www.youtube.com/watch?v=HYhdyu-_mgk'),
('Get ready to fight', 'Angry', 'https://www.youtube.com/watch?v=h6aGikIL-I4'),
('Brothers anthem', 'Angry', 'https://www.youtube.com/watch?v=IjBAgWKW12Y'),
('Jee karda', 'Angry', 'https://www.youtube.com/watch?v=xI6jLdsK15I'),
('Hona hai kya', 'Angry', 'https://www.youtube.com/watch?v=ZCVsAyZATNA'),
('Chhil Gaye Naina', 'Angry', 'https://www.youtube.com/watch?v=Lhn0e7cDKS0'),
('Dastan-e-om shanti om ', 'Angry', 'https://www.youtube.com/watch?v=ymuNkKuToao'),
('Khalbali', 'Angry', 'https://www.youtube.com/watch?v=hnswwRWLi3E'),
('Bheegi Bheegi', 'Angry', 'https://www.youtube.com/watch?v=T_NtMcaCEYE');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
