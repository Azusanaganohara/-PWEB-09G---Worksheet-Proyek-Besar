-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 25, 2024 at 03:28 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `box_inc`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('bb8990856173');

-- --------------------------------------------------------

--
-- Table structure for table `penyewa`
--

CREATE TABLE `penyewa` (
  `id` int(11) NOT NULL,
  `nama_penyewa` varchar(80) NOT NULL,
  `no_hp` varchar(80) NOT NULL,
  `alamat` varchar(80) NOT NULL,
  `banyak_box` int(11) NOT NULL,
  `tipe_box` varchar(80) NOT NULL,
  `tanggal_penyewaan` varchar(80) NOT NULL,
  `lama_penitipan` int(11) NOT NULL,
  `penanggung_jawab` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `penyewa`
--

INSERT INTO `penyewa` (`id`, `nama_penyewa`, `no_hp`, `alamat`, `banyak_box`, `tipe_box`, `tanggal_penyewaan`, `lama_penitipan`, `penanggung_jawab`) VALUES
(9, 'abc', '123', 'disini', 1, 'kecil', '2024-12-17', 1, 'hanafi'),
(10, 'def', '456', 'disana', 2, 'sedang', '2024-12-18', 2, 'hanafi'),
(11, 'ghi', '7890', 'dimana', 1, 'besar', '2024-12-19', 1, 'hanafi');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'isnain', 'isnain'),
(2, 'rahmat', 'rahmat'),
(3, 'ersa', 'ersa'),
(4, 'hajar', 'hajar'),
(5, 'hanafi', 'hanafi'),
(6, 'fahmi', 'fahmi');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `penyewa`
--
ALTER TABLE `penyewa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_penanggung_jawab` (`penanggung_jawab`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `penyewa`
--
ALTER TABLE `penyewa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `penyewa`
--
ALTER TABLE `penyewa`
  ADD CONSTRAINT `fk_penanggung_jawab` FOREIGN KEY (`penanggung_jawab`) REFERENCES `users` (`username`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
