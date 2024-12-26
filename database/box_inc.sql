-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 26, 2024 at 10:06 AM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tugas`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_general_ci NOT NULL
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
  `id` int NOT NULL,
  `nama_penyewa` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `no_hp` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `alamat` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `banyak_box` int NOT NULL,
  `tipe_box` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `tanggal_penyewaan` varchar(80) COLLATE utf8mb4_general_ci NOT NULL,
  `lama_penitipan` int NOT NULL,
  `penanggung_jawab` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `penyewa`
--

INSERT INTO `penyewa` (`id`, `nama_penyewa`, `no_hp`, `alamat`, `banyak_box`, `tipe_box`, `tanggal_penyewaan`, `lama_penitipan`, `penanggung_jawab`) VALUES
(7, 'Bamabank', '12141313', 'asd', 12, 'kecil', '2024-12-27', 12, 'Hanafi'),
(8, 'Hajar', '134123', '21313', 12, 'besar', '2024-12-27', 21, 'Hanafi'),
(9, 'Bambank', '12141313', 'dsad', 1, 'kecil', '2024-12-30', 12, 'Hanafi');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(8, 'hajar', 'pbkdf2:sha256:1000000$donqGYJHJqyVO6GQ$cdea3ba9769f3c6616024bba31b69eb22945b8fc1c8e021e625331a9fd6ca20e'),
(9, 'Arbai', 'pbkdf2:sha256:1000000$RW7i3sxgyTcD8j48$4566cb2be40d1dd126399b302fa6fcbabadee122229f59aefed0c7add599a73d'),
(10, 'Hanafi', 'pbkdf2:sha256:1000000$wJbw7P5hXBc1us5y$5294cce4f9968f5c356df405eaff7f06187681d80f488b926da59584759a5c09'),
(11, 'Fahmi', 'pbkdf2:sha256:1000000$9O6N8qQZMoMDQLGb$cf016401d900dd27eef9b456443724cd5df7b4d57887fcabf75e612c2e0a3813'),
(12, 'Isnain', 'pbkdf2:sha256:1000000$a4BKG3XYzO1O92n2$454fd5f0136ffb6d1ffb53ef87904fc340144344e451b334cf348bb89cfc9965'),
(13, 'Ersa', 'pbkdf2:sha256:1000000$98Jy4LOz97Wz85Wy$1c80376dafdd199fec17e8485907ced2b8cc464b080641448c817231a1b43182');

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

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
