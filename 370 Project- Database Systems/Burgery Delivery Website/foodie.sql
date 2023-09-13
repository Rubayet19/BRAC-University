-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 28, 2021 at 07:46 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `foodie`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Admin_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Admin_id`, `name`, `email`, `password`) VALUES
(18101002, 'Noshin Nanjiba Islam', 'noshin.nanjiba.islam.preoshi@g', 'burger'),
(19241009, 'Rubayet Bin Mujahid', 'Sk.rubayet.bin.mujahid@g.bracu', 'burger'),
(20101134, 'Moin Uddin', 'moin.uddin@g.bracu.ac.bd', 'burger'),
(20101141, 'Sumaiya Sinha', 'Sumaiya.sinha@g.bracu.ac.bd', 'burger'),
(20101338, 'Mahir Aseef', 'mahir.aseef@g.bracu.ac.bd', 'burger');

-- --------------------------------------------------------

--
-- Table structure for table `admin updateview_order`
--

CREATE TABLE `admin updateview_order` (
  `order_id` int(11) NOT NULL,
  `admin_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `bun`
--

CREATE TABLE `bun` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bun`
--

INSERT INTO `bun` (`id`, `name`, `price`) VALUES
(1, 'Brioche bun', 50),
(2, 'Potato bun', 30),
(3, 'Sesame Seed bun', 60);

-- --------------------------------------------------------

--
-- Table structure for table `burger`
--

CREATE TABLE `burger` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `burger_price` float NOT NULL,
  `salad_name` varchar(20) NOT NULL,
  `sauce_name` varchar(20) NOT NULL,
  `patty_name` varchar(20) NOT NULL,
  `bun_name` varchar(20) NOT NULL,
  `spicy_level` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `burger`
--

INSERT INTO `burger` (`id`, `name`, `burger_price`, `salad_name`, `sauce_name`, `patty_name`, `bun_name`, `spicy_level`) VALUES
(17, 'Chicken Burger', 200, 'Cashew nut salad', 'Chilli Sauce', 'Vegetable', 'Potato bun', 'Mild spicy'),
(18, 'Beef Burger', 250, 'Mix veggie salad', 'Barbeque sauce', 'Chicken', 'Brioche bun', 'Mild spicy'),
(19, 'Zinger Burger', 300, 'Cashew nut salad', 'Chilli Sauce', 'Vegetable', 'Potato bun', 'Mild spicy');

-- --------------------------------------------------------

--
-- Table structure for table `manages`
--

CREATE TABLE `manages` (
  `Admin_id` int(11) NOT NULL,
  `burger_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `user_id` int(11) NOT NULL,
  `burger_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `order_status`
--

CREATE TABLE `order_status` (
  `order_id` int(11) NOT NULL,
  `address` varchar(200) NOT NULL,
  `price` int(11) NOT NULL,
  `delivery_status` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `patty`
--

CREATE TABLE `patty` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patty`
--

INSERT INTO `patty` (`id`, `name`, `price`) VALUES
(1, 'Beef', 55),
(2, 'Chicken', 50),
(3, 'Vegetable', 40);

-- --------------------------------------------------------

--
-- Table structure for table `salad`
--

CREATE TABLE `salad` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `salad`
--

INSERT INTO `salad` (`id`, `name`, `price`) VALUES
(1, 'Cashew nut salad', 80),
(2, 'Lettuce', 50),
(3, 'Mix veggie salad', 60);

-- --------------------------------------------------------

--
-- Table structure for table `sauce`
--

CREATE TABLE `sauce` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sauce`
--

INSERT INTO `sauce` (`id`, `name`, `price`) VALUES
(1, 'Barbeque sauce', 50),
(2, 'Chilli Sauce', 20),
(3, 'Tomato sauce', 30);

-- --------------------------------------------------------

--
-- Table structure for table `spice_level`
--

CREATE TABLE `spice_level` (
  `id` int(11) NOT NULL,
  `level` varchar(20) NOT NULL,
  `price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `spice_level`
--

INSERT INTO `spice_level` (`id`, `level`, `price`) VALUES
(1, 'Less spicy', 25),
(2, 'Mild spicy', 30),
(3, 'Very spicy', 60);

-- --------------------------------------------------------

--
-- Table structure for table `user_reg`
--

CREATE TABLE `user_reg` (
  `user_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `address` varchar(200) NOT NULL,
  `password` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_reg`
--

INSERT INTO `user_reg` (`user_id`, `name`, `email`, `address`, `password`) VALUES
(10, 'test', 'test@gmail.com', '', '$2y$10$muPPE7dnSWU89i/MPR4UcOn3JpUQGhvw4IH.TU5tIOMvP5sXycgpe'),
(11, 'test1', 'test1@gail.com', '', '$2y$10$ZW3Vv60l38y75HjfWSAJM.3mJdhwIFQ0UgXLboPUkpKaz1rJb3Xai');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Admin_id`);

--
-- Indexes for table `admin updateview_order`
--
ALTER TABLE `admin updateview_order`
  ADD PRIMARY KEY (`order_id`,`admin_id`),
  ADD KEY `admin_id` (`admin_id`);

--
-- Indexes for table `bun`
--
ALTER TABLE `bun`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `burger`
--
ALTER TABLE `burger`
  ADD PRIMARY KEY (`id`),
  ADD KEY `salad_name` (`salad_name`),
  ADD KEY `sauce_name` (`sauce_name`),
  ADD KEY `patty_name` (`patty_name`),
  ADD KEY `bun_name` (`bun_name`),
  ADD KEY `spicy_level` (`spicy_level`);

--
-- Indexes for table `manages`
--
ALTER TABLE `manages`
  ADD PRIMARY KEY (`Admin_id`,`burger_id`),
  ADD KEY `burger_id` (`burger_id`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`user_id`,`burger_id`),
  ADD KEY `burger_id` (`burger_id`);

--
-- Indexes for table `order_status`
--
ALTER TABLE `order_status`
  ADD PRIMARY KEY (`order_id`),
  ADD KEY `address` (`address`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `patty`
--
ALTER TABLE `patty`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `salad`
--
ALTER TABLE `salad`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sauce`
--
ALTER TABLE `sauce`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `spice_level`
--
ALTER TABLE `spice_level`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_reg`
--
ALTER TABLE `user_reg`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `Admin_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20101339;

--
-- AUTO_INCREMENT for table `bun`
--
ALTER TABLE `bun`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `burger`
--
ALTER TABLE `burger`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `order_status`
--
ALTER TABLE `order_status`
  MODIFY `order_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patty`
--
ALTER TABLE `patty`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `salad`
--
ALTER TABLE `salad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `sauce`
--
ALTER TABLE `sauce`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `spice_level`
--
ALTER TABLE `spice_level`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_reg`
--
ALTER TABLE `user_reg`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin updateview_order`
--
ALTER TABLE `admin updateview_order`
  ADD CONSTRAINT `admin updateview_order_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`Admin_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `admin updateview_order_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `order_status` (`order_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `burger`
--
ALTER TABLE `burger`
  ADD CONSTRAINT `burger_ibfk_1` FOREIGN KEY (`sauce_name`) REFERENCES `sauce` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `burger_ibfk_2` FOREIGN KEY (`spicy_level`) REFERENCES `spice_level` (`level`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `burger_ibfk_3` FOREIGN KEY (`patty_name`) REFERENCES `patty` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `burger_ibfk_4` FOREIGN KEY (`salad_name`) REFERENCES `salad` (`name`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `burger_ibfk_5` FOREIGN KEY (`bun_name`) REFERENCES `bun` (`name`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `manages`
--
ALTER TABLE `manages`
  ADD CONSTRAINT `manages_ibfk_1` FOREIGN KEY (`Admin_id`) REFERENCES `admin` (`Admin_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `manages_ibfk_2` FOREIGN KEY (`burger_id`) REFERENCES `burger` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_reg` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_ibfk_2` FOREIGN KEY (`burger_id`) REFERENCES `burger` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `order_status`
--
ALTER TABLE `order_status`
  ADD CONSTRAINT `order_status_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_reg` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
