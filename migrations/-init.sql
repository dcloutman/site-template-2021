-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2021 at 06:24 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
-- SET time_zone = "+00:00";


-- /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
-- /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
-- /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
-- /*!40101 SET NAMES utf8mb4 */;

--
-- Database: `site_template_2021`
--
CREATE DATABASE IF NOT EXISTS `site_template_2021` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `site_template_2021`;

-- --------------------------------------------------------

--
-- Table structure for table `email_addresses`
--

CREATE TABLE `email_addresses` (
  `email_address_id` bigint(20) UNSIGNED NOT NULL,
  `email_address` varchar(320) NOT NULL,
  `time_added` datetime DEFAULT CURRENT_TIMESTAMP,
  `time_updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `email_lists`
--

CREATE TABLE `email_lists` (
  `email_list_id` mediumint(5) UNSIGNED NOT NULL,
  `list_name` varchar(1023) NOT NULL,
  `list_description` mediumtext NOT NULL,
  `time_added` datetime DEFAULT CURRENT_TIMESTAMP,
  `time_updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='A table of mailing lists.';

--
-- Dumping data for table `email_lists`
--

INSERT INTO `email_lists` (`email_list_id`, `list_name`, `list_description`, `time_added`, `time_updated`) VALUES
(1, 'Newsletter [test]', 'Test data. Delete this record before using database in production.', '2021-02-18 23:48:32', '2021-02-18 23:49:36'),
(2, 'Special Offers [test]', 'Test data. Delete before using database in production.', '2021-02-18 23:52:21', '2021-02-18 23:52:21'),
(3, 'No Subscribers [test]', 'Delete this data before using database in production.\r\n\r\nThis list is unused by built-in sources (forms).', '2021-02-18 23:54:31', '2021-02-18 23:54:31');

-- --------------------------------------------------------

--
-- Table structure for table `email_list_subscriptions`
--

CREATE TABLE `email_list_subscriptions` (
  `email_list_id` mediumint(8) UNSIGNED NOT NULL,
  `email_address_id` bigint(20) UNSIGNED NOT NULL,
  `subscription_source_id` int(8) UNSIGNED NOT NULL,
  `time_added` datetime DEFAULT CURRENT_TIMESTAMP,
  `time_updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `email_list_subscription_sources`
--

CREATE TABLE `email_list_subscription_sources` (
  `subscription_source_id` int(10) UNSIGNED NOT NULL,
  `string_identifier` varchar(255) DEFAULT NULL COMMENT 'A short string for easy programmatic access. Must be unique.',
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `time_added` datetime DEFAULT CURRENT_TIMESTAMP,
  `time_updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `email_list_subscription_sources`
--

INSERT INTO `email_list_subscription_sources` (`subscription_source_id`, `string_identifier`, `name`, `description`, `time_added`, `time_updated`) VALUES
(1, 'site_email_lightbox', 'Web Site Email Lightbox', 'The lightbox that pops up and prompts users to sign up on the first page.', '2021-02-18 23:57:26', '2021-02-18 23:57:26'),
(2, 'user_onboarding', 'User On-boarding', 'A form for users that onboard for user logins.', '2021-02-19 00:00:40', '2021-02-19 00:00:40'),
(3, 'contact_us_form', 'Contact Us Form', 'Email lists to sign up for via the contact-us form.', '2021-02-19 00:02:14', '2021-02-19 00:02:14');

-- --------------------------------------------------------

--
-- Table structure for table `email_subscription_source_default_lists`
--

CREATE TABLE `email_subscription_source_default_lists` (
  `subscription_source_id` int(10) UNSIGNED NOT NULL,
  `email_list_id` mediumint(8) UNSIGNED NOT NULL,
  `time_added` datetime DEFAULT CURRENT_TIMESTAMP,
  `time_updated` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
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
-- Indexes for table `email_addresses`
--
ALTER TABLE `email_addresses`
  ADD PRIMARY KEY (`email_address_id`),
  ADD UNIQUE KEY `unique_email_address` (`email_address`);

--
-- Indexes for table `email_lists`
--
ALTER TABLE `email_lists`
  ADD PRIMARY KEY (`email_list_id`);

--
-- Indexes for table `email_list_subscriptions`
--
ALTER TABLE `email_list_subscriptions`
  ADD KEY `email_list_subscription_email_address_id` (`email_address_id`),
  ADD KEY `email_list_subscriptions_source_id` (`subscription_source_id`),
  ADD KEY `email_list_subscriptions_email_lists` (`email_list_id`);

--
-- Indexes for table `email_list_subscription_sources`
--
ALTER TABLE `email_list_subscription_sources`
  ADD PRIMARY KEY (`subscription_source_id`),
  ADD UNIQUE KEY `email_list_subscription_source_string_identifier_unique` (`string_identifier`);

--
-- Indexes for table `email_subscription_source_default_lists`
--
ALTER TABLE `email_subscription_source_default_lists`
  ADD UNIQUE KEY `email_subscription_source_default_lists_unique` (`subscription_source_id`,`email_list_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `email_addresses`
--
ALTER TABLE `email_addresses`
  MODIFY `email_address_id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `email_lists`
--
ALTER TABLE `email_lists`
  MODIFY `email_list_id` mediumint(5) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `email_list_subscription_sources`
--
ALTER TABLE `email_list_subscription_sources`
  MODIFY `subscription_source_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `email_list_subscriptions`
--
ALTER TABLE `email_list_subscriptions`
  ADD CONSTRAINT `email_list_subscription_email_address_id` FOREIGN KEY (`email_address_id`) REFERENCES `email_addresses` (`email_address_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `email_list_subscriptions_email_lists` FOREIGN KEY (`email_list_id`) REFERENCES `email_lists` (`email_list_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `email_list_subscriptions_source_id` FOREIGN KEY (`subscription_source_id`) REFERENCES `email_list_subscription_sources` (`subscription_source_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
