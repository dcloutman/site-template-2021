-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 19, 2021 at 09:12 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `site_template_2021`
--

-- --------------------------------------------------------

--
-- Table structure for table `email_subscription_source_default_lists`
--

CREATE TABLE `email_subscription_source_default_lists` (
  `subscription_source_id` int(10) UNSIGNED NOT NULL,
  `email_list_id` mediumint(8) UNSIGNED NOT NULL,
  `time_added` datetime DEFAULT current_timestamp(),
  `time_updated` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='List source associations set defaults for different forms.';

--
-- Dumping data for table `email_subscription_source_default_lists`
--

INSERT INTO `email_subscription_source_default_lists` (`subscription_source_id`, `email_list_id`, `time_added`, `time_updated`) VALUES
(1, 1, '2021-02-19 00:09:37', '2021-02-19 00:09:37'),
(1, 2, '2021-02-19 00:09:37', '2021-02-19 00:09:37');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `email_subscription_source_default_lists`
--
ALTER TABLE `email_subscription_source_default_lists`
  ADD UNIQUE KEY `email_subscription_source_default_lists_unique` (`subscription_source_id`,`email_list_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


