-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 30, 2019 at 10:34 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.1.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectx`
--

-- --------------------------------------------------------

--
-- Table structure for table `advisor_advisor`
--

CREATE TABLE `advisor_advisor` (
  `advisor_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `country_code_primary` varchar(255) NOT NULL,
  `phone_number_primary` varchar(10) NOT NULL,
  `email_adress` varchar(254) NOT NULL,
  `about_seller` longtext NOT NULL,
  `website` varchar(500) DEFAULT NULL,
  `professional_link` varchar(500) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `album_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `advisor_advisor`
--

INSERT INTO `advisor_advisor` (`advisor_id`, `first_name`, `middle_name`, `last_name`, `country_code_primary`, `phone_number_primary`, `email_adress`, `about_seller`, `website`, `professional_link`, `created_at`, `album_id`, `type`, `title`) VALUES
(1, 'djc', 'adkb', 'akdhbv', 'Afghanistan (+93)', '6451', 'afn@adf.com', 'Institutions', NULL, NULL, '2019-05-27 11:22:20.631862', 77, 'Business', 'something'),
(2, 'jsdhv', 'skjdbv', 'sjkbdv', 'Afghanistan (+93)', '6451', 'ahdv@ad.com', 'Incubators', NULL, NULL, '2019-05-27 12:04:44.486504', 78, 'Startup', 'something'),
(3, 'Minusjvh', 'hbfv', 'jhfvb', 'Afghanistan (+93)', '97846', 'sdjkv@addv.com', 'Incubators', NULL, NULL, '2019-05-30 14:14:55.339729', 85, 'Business', 'something'),
(4, 'Minusdjadjba', 'aadhkbcad', 'shdbv', 'Afghanistan (+93)', '978415', 'agcv@adv.com', 'Incubators', NULL, NULL, '2019-05-30 14:19:08.292333', 86, 'Business', 'something'),
(5, 'sdch', 'smn', 'smhb', 'Afghanistan (+93)', '5', '41@scb.com', 'Incubators', NULL, NULL, '2019-05-31 14:27:51.131654', 88, 'Business', 'something'),
(6, 'Prajwal', 'tegetg', 'rgergreg', 'Afghanistan (+93)', '3423423', 'wfwef@rrwrtrwt.com', 'Mentors', NULL, 'http://rwwwrrwf.google.con', '2019-05-31 14:58:25.940310', 89, 'Business', 'something'),
(7, 'Prajwal_1', 'rfrf', 'ererreferf', 'Belarus(+375)', '32332233', 'prithvi@gmail.com', 'Incubators', NULL, 'http://www.google.com', '2019-05-31 15:04:04.491053', 90, 'Business', 'something'),
(8, 'Prajwal', 'Subhash', 'Baratatre', 'Afghanistan (+93)', '548798123', 'asdf@vfv.com', 'Incubators', NULL, 'http://af@sdvjjk.com', '2019-06-13 06:08:05.577516', 93, 'Business', 'something'),
(9, 'Prajwal', 'Subhash', 'Baratatre', 'Afghanistan (+93)', '548798123', 'asdf@vfv.com', 'Incubators', NULL, 'http://af@sdvjjk.com', '2019-06-13 06:23:32.088148', 93, 'Business', 'something'),
(10, 'sdv', 'svd', 'fb', 'Afghanistan (+93)', '548745', 'adv@qsdv.com', 'Incubators', NULL, 'http://adv@adv.com', '2019-06-17 09:55:19.635764', 106, 'Business', 'something'),
(11, 'jkfvn', 'kjsv', 'kjdv', 'Afghanistan (+93)', '7845', 'dsv@sdv.com', 'Incubators', NULL, 'http://sdv@wdsv.com', '2019-06-17 15:32:52.770029', 107, 'Business', 'something'),
(12, 'jhsbv', ',jv', ',jsvb', 'Afghanistan (+93)', '42', 'sdv@asc.com', 'Incubators', NULL, 'http://sdv@asdcv.com', '2019-06-17 16:42:03.856978', 108, 'Business', 'something'),
(13, 'sdhvb', 'jhcb', 'sbhcvjhdcb', 'Afghanistan (+93)', '541', 'ghdc@sdkjvb.com', 'Incubators', NULL, 'http://sdjvb@asfc.com', '2019-06-17 16:59:07.761017', 109, 'Business', 'something'),
(14, 'sdhvb', 'jhcb', 'sbhcvjhdcb', 'Afghanistan (+93)', '541', 'ghdc@sdkjvb.com', 'Incubators', NULL, 'http://sdjvb@asfc.com', '2019-06-17 17:31:11.858376', 109, 'Business', 'something'),
(15, 'sdhvb', 'jhcb', 'sbhcvjhdcb', 'Afghanistan (+93)', '541', 'ghdc@sdkjvb.com', 'Incubators', NULL, 'http://sdjvb@asfc.com', '2019-06-17 17:32:44.349634', 109, 'Business', 'something'),
(16, 'sdhvb', 'jhcb', 'sbhcvjhdcb', 'Afghanistan (+93)', '541', 'ghdc@sdkjvb.com', 'Incubators', NULL, 'http://sdjvb@asfc.com', '2019-06-17 17:33:37.074257', 109, 'Business', 'something'),
(17, 'shbv', 'sdbh', 'dvhj', 'Afghanistan (+93)', '78453', 'asdc@ACS.COM', 'Incubators', NULL, 'http://asdc@ACS.COM', '2019-06-17 17:37:00.947981', 113, 'Business', 'something'),
(18, 'sjfvb', 'jcsv', 'kjf v', 'Afghanistan (+93)', '8754', 'dv@ASCV.COM', 'Incubators', NULL, 'http://dv@ASCV.COM', '2019-06-18 07:56:22.937928', 114, 'Business', 'something'),
(19, 'hbf dfvbd fvnd fv', 'djfvn sdfv', 'ddjfkv', 'Afghanistan (+93)', '7854', 'fhbv@b.com', 'Incubators', NULL, 'http://jbv@adb.com', '2019-06-20 15:05:07.487260', 115, 'Business', 'something'),
(20, 'kdb vkjsbkjdc', 'ksdhvb', 'sdjkbv', 'Afghanistan (+93)', '7845', 'sdvhb@asv.com', 'Incubators', NULL, 'http://sdv@ads.com', '2019-06-21 05:24:37.858921', 116, 'Startup', 'something'),
(21, 'kjsdbv', 'dn,vb', 'aksjcb', 'Afghanistan (+93)', '45613', 'hgdvc@asdc.com', 'Incubators', NULL, 'http://ac@adv.com', '2019-06-23 13:59:21.958580', 132, 'Business', 'hgc g hg hg kshbv sdjsd v'),
(22, 'sjdv', 'sbnv', 'jbv', 'Afghanistan (+93)', '5165', 'sv@sddv.com', 'Incubators', NULL, NULL, '2019-06-24 19:42:14.501484', 136, 'Business', 'jd sdvsb dvsj dv sdv s');

-- --------------------------------------------------------

--
-- Table structure for table `advisor_businessadvisor`
--

CREATE TABLE `advisor_businessadvisor` (
  `business_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `category1` varchar(255) NOT NULL,
  `sub_category1` varchar(255) NOT NULL,
  `category2` varchar(255) NOT NULL,
  `sub_category2` varchar(255) NOT NULL,
  `category3` varchar(255) NOT NULL,
  `sub_category3` varchar(255) NOT NULL,
  `skill1` varchar(255) NOT NULL,
  `skill2` varchar(255) NOT NULL,
  `skill3` varchar(255) NOT NULL,
  `city1` varchar(255) NOT NULL,
  `state1` varchar(255) NOT NULL,
  `country1` varchar(255) NOT NULL,
  `city2` varchar(255) NOT NULL,
  `state2` varchar(255) NOT NULL,
  `country2` varchar(255) NOT NULL,
  `city3` varchar(255) NOT NULL,
  `state3` varchar(255) NOT NULL,
  `country3` varchar(255) NOT NULL,
  `address_line1` varchar(256) NOT NULL,
  `address_line2` varchar(256) NOT NULL,
  `address_line3` varchar(256) NOT NULL,
  `about` longtext NOT NULL,
  `years_exp` int(11) NOT NULL,
  `hour_fee` int(11) NOT NULL,
  `advisor_id` int(11) DEFAULT NULL,
  `about_seller` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `advisor_businessadvisor`
--

INSERT INTO `advisor_businessadvisor` (`business_id`, `type`, `category1`, `sub_category1`, `category2`, `sub_category2`, `category3`, `sub_category3`, `skill1`, `skill2`, `skill3`, `city1`, `state1`, `country1`, `city2`, `state2`, `country2`, `city3`, `state3`, `country3`, `address_line1`, `address_line2`, `address_line3`, `about`, `years_exp`, `hour_fee`, `advisor_id`, `about_seller`) VALUES
(1, 'Business', 'Aerospace', 'Aerospace', 'Education', 'E-Learning', 'Agriculture', 'Agriculture', '', '', '', 'Mumbai Central', 'Mumbai Central', '', 'Bangalore Urban', 'Bangalore Urban', '', 'Ivankivs\'kyi district', 'Ivankivs\'kyi district', '', 'Mumbai Central Railway Station Building, Mumbai Central, Mumbai, Maharashtra, India', 'Bangalore, Karnataka, India', 'Chernobyl, Kyiv Oblast, Ukraine', 'smdvn smnd vs dv', 841, 651, 1, 'Incubators'),
(2, 'Business', 'Utility', 'Utility (Water)', 'Electronics', 'Consumer Electronics', 'Manufacturing', 'Chemical (Basic)', '', '', '', 'Mumbai', 'Mumbai', '', '', '', '', '', '', '', 'Mumbai Central, Mumbai, Maharashtra, India', 'Goa, India', 'Gujarat, India', 'sjdbvs vs vs v', 651, 651, 3, 'Incubators'),
(3, 'Business', 'Automotive', 'Automotive', 'Electronics', 'Consumer Electronics', 'Retail', 'Retail (Building Supply)', '', '', '', 'Mumbai', 'Mumbai', '', '', '', '', '', '', '', 'Mumbai, Maharashtra, India', 'Goa, India', 'Berlin, Germany', 'ascn vskdvsndv sv skv kv', 61, 655, 4, 'Incubators'),
(4, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Utility', 'Utility (Water)', 'Electronics', 'Electronics (Consumer & Office)', '', '', '', 'Mumbai', 'Mumbai', '', 'Upper Bavaria', 'Upper Bavaria', '', '', '', '', 'Mumbai Central, Mumbai, Maharashtra, India', 'Munich, Germany', 'Playa del Carmen, Quintana Roo, Mexico', 'hg hjv jh jhv', 5412, 8751654, 5, 'Incubators'),
(5, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Agriculture', 'Agriculture', 'Social Media', 'Blogging Platforms', '', '', '', 'Erode', 'Erode', '', 'Chennai', 'Chennai', '', 'Bangalore Urban', 'Bangalore Urban', '', 'Chennimalai, Tamil Nadu, India', 'Chennai, Tamil Nadu, India', 'Bangalore, Karnataka, India', 'fjnergu eguhe ge eugeug egheg heugh egh g htguthghu g etuhg etug e', 12, 122133233, 6, 'Incubators'),
(6, 'Business', 'Business Services', 'Brand Marketing', 'IT', 'Software (Entertainment)', 'Manufacturing', 'Chemical (Diversified)', '', '', '', 'Indore', 'Indore', '', 'Ekta Vihar', 'Ekta Vihar', '', 'Mumbai', 'Mumbai', '', 'Indore, Madhya Pradesh, India', 'Tamil Sangam Marg, Ekta Vihar, West Block, Rama Krishna Puram, New Delhi, Delhi, India', 'Mumbai, Maharashtra, India', 'rferer ererg eg teg etg etg etegt et', 1212, 1221, 7, 'Incubators'),
(7, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Utility', 'Water', 'Manufacturing', 'Machinery', '', '', '', 'Mumbai', 'Mumbai', '', 'Pune', 'Pune', '', 'Greenville County', 'Greenville County', '', 'Mumbai, Maharashtra, India', 'Pune, Maharashtra, India', 'Greenville, SC, USA', 'hbdc sdhjd sdshdvsjdvsjdv svsvjhs vsh vsvh sidhv sidhvwdihfbwdi wdvhw dvshd v jzc c dc dc vdd vsdv sd v dvsd vsdvs dvshdv', 46553, 6451, 8, 'Incubators'),
(8, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Utility', 'Water', 'Manufacturing', 'Machinery', '', '', '', 'Mumbai', 'Mumbai', '', 'Pune', 'Pune', '', 'Greenville County', 'Greenville County', '', 'Mumbai, Maharashtra, India', 'Pune, Maharashtra, India', 'Greenville, SC, USA', 'hbdc sdhjd sdshdvsjdvsjdv svsvjhs vsh vsvh sidhv sidhvwdihfbwdi wdvhw dvshd v jzc c dc dc vdd vsdv sd v dvsd vsdvs dvshdv', 46553, 6451, 9, 'Incubators'),
(9, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Retail', 'Retail (Building Supply)', 'Automotive', 'Automotive', '', '', '', 'Mumbai', 'Mumbai', '', 'Stanislaus County', 'Stanislaus County', '', '', '', '', 'Mumbai, Maharashtra, India', 'Modesto, CA, USA', 'Virginia Beach, VA, USA', 'sjkdvs svd sk dvskjv skd v', 87, 78455, 10, 'Incubators'),
(10, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Manufacturing', 'Machinery', 'Automotive', 'Automotive', '', '', '', 'Mumbai', 'Mumbai', '', 'Riverside County', 'Riverside County', '', 'Chennai', 'Chennai', '', 'Mumbai, Maharashtra, India', 'Moreno Valley, CA, USA', 'Chennai, Tamil Nadu, India', 'ksjdvns s jsd vsdjv sjd v', 451, 78, 11, 'Incubators'),
(11, 'Business', 'Automotive', 'Automotive', 'Manufacturing', 'Chemical (Basic)', 'Manufacturing', 'Machinery', '', '', '', 'Mumbai', 'Mumbai', '', 'Monterey County', 'Monterey County', '', 'Jaipur', 'Jaipur', '', 'Mumbai, Maharashtra, India', 'Monterey, CA, USA', 'New Delhi, Delhi, India', 'dffc nhgfv gb b', 55, 536, 12, 'Incubators'),
(12, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Electronics', 'Electronics', 'Manufacturing', 'Machinery', '', '', '', 'Mumbai', 'Maharashtra', '', 'Montreal', 'Quebec', '', 'Chennai', 'Tamil Nadu', '', 'Mumbai, Maharashtra, India', 'Montreal, QC, Canada', 'Chennai, Tamil Nadu, India', 'sdvh sd sd shd', 561, 5421, 13, 'Incubators'),
(13, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Electronics', 'Electronics', 'Manufacturing', 'Machinery', '', '', '', 'Mumbai', 'Maharashtra', '', 'Montreal', 'Quebec', '', 'Chennai', 'Tamil Nadu', '', 'Mumbai, Maharashtra, India', 'Montreal, QC, Canada', 'Chennai, Tamil Nadu, India', 'sdvh sd sd shd', 561, 5421, 14, 'Incubators'),
(14, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Electronics', 'Electronics', 'Manufacturing', 'Machinery', '', '', '', 'Mumbai', 'Maharashtra', '', 'Montreal', 'Quebec', '', 'Chennai', 'Tamil Nadu', '', 'Mumbai, Maharashtra, India', 'Montreal, QC, Canada', 'Chennai, Tamil Nadu, India', 'sdvh sd sd shd', 561, 5421, 15, 'Incubators'),
(15, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Electronics', 'Electronics', 'Manufacturing', 'Machinery', '', '', '', 'Mumbai', 'Maharashtra', '', 'Montreal', 'Quebec', '', 'Chennai', 'Tamil Nadu', '', 'Mumbai, Maharashtra, India', 'Montreal, QC, Canada', 'Chennai, Tamil Nadu, India', 'sdvh sd sd shd', 561, 5421, 16, 'Incubators'),
(16, 'Business', 'Education', 'Knowledge Mangement', 'Manufacturing', 'Chemical (Basic)', 'Utility', 'Utility (Water)', '', '', '', 'Mumbai', 'Maharashtra', 'India', 'Kota', 'Rajasthan', 'India', 'Chennai', 'Tamil Nadu', 'India', 'Mumbai, Maharashtra, India', 'Kota, Rajasthan, India', 'Chennai, Tamil Nadu, India', 'cdg cc jc acjasc', 7845, 845, 17, 'Incubators'),
(17, 'Business', 'Automotive', 'Automotive', 'Manufacturing', 'Machinery', 'Manufacturing', 'Chemical (Basic)', '', '', '', 'Chennai', 'Tamil Nadu', 'India', 'Mumbai', 'Maharashtra', 'India', 'Jaipur', 'Rajasthan', 'India', 'Chennai, Tamil Nadu, India', 'Mumbai, Maharashtra, India', 'Jaipur, Rajasthan, India', 'hsdv sdcs dcs c', 7846, 781, 18, 'Incubators'),
(18, 'Business', 'Utility', 'Utility (Water)', 'Manufacturing', 'Building Materials', 'Manufacturing', 'Machinery', '', '', '', 'Jaipur', 'Rajasthan', 'India', 'Mumbai', 'Maharashtra', 'India', 'Ivankivs\'kyi district', 'Kyiv Oblast', 'Ukraine', 'Jaipur, Rajasthan, India', 'Mumbai, Maharashtra, India', 'Chernobyl, Kyiv Oblast, Ukraine', 'sdvhb h ch dv sdv', 7895, 785, 19, 'Incubators'),
(19, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Utility', 'Utility (Water)', 'Electronics', 'Electronics', '', '', '', 'Ivankivs\'kyi district', 'Kyiv Oblast', 'Ukraine', 'Mumbai', 'Maharashtra', 'India', 'Chennai', 'Tamil Nadu', 'India', 'Chernobyl, Kyiv Oblast, Ukraine', 'Mumbai, Maharashtra, India', 'Chennai, Tamil Nadu, India', 'sdjh dcscb scb sdb sdb sdb sdsd ns d', 654, 35, 21, 'Incubators'),
(20, 'Business', 'Manufacturing', 'Chemical (Basic)', 'Utility', 'Utility (Water)', 'Retail', 'Retail (Building Supply)', '', '', '', 'Mumbai', 'Maharashtra', 'India', 'Ivankivs\'kyi district', 'Kyiv Oblast', 'Ukraine', 'Chennai', 'Tamil Nadu', 'India', 'Mumbai, Maharashtra, India', 'Chernobyl, Kyiv Oblast, Ukraine', 'Chennai, Tamil Nadu, India', 'sdv mnv fsv  sv', 548, 658, 22, 'Incubators');

-- --------------------------------------------------------

--
-- Table structure for table `advisor_startupadvisor`
--

CREATE TABLE `advisor_startupadvisor` (
  `startup_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `category1` varchar(255) NOT NULL,
  `sub_category1` varchar(255) NOT NULL,
  `category2` varchar(255) NOT NULL,
  `sub_category2` varchar(255) NOT NULL,
  `category3` varchar(255) NOT NULL,
  `sub_category3` varchar(255) NOT NULL,
  `skill1` varchar(255) NOT NULL,
  `skill2` varchar(255) NOT NULL,
  `skill3` varchar(255) NOT NULL,
  `city1` varchar(255) NOT NULL,
  `state1` varchar(255) NOT NULL,
  `country1` varchar(255) NOT NULL,
  `city2` varchar(255) NOT NULL,
  `state2` varchar(255) NOT NULL,
  `country2` varchar(255) NOT NULL,
  `city3` varchar(255) NOT NULL,
  `state3` varchar(255) NOT NULL,
  `country3` varchar(255) NOT NULL,
  `address_line1` varchar(256) NOT NULL,
  `address_line2` varchar(256) NOT NULL,
  `address_line3` varchar(256) NOT NULL,
  `about` longtext NOT NULL,
  `years_exp` int(11) NOT NULL,
  `hour_fee` int(11) NOT NULL,
  `advisor_id` int(11) DEFAULT NULL,
  `about_seller` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `advisor_startupadvisor`
--

INSERT INTO `advisor_startupadvisor` (`startup_id`, `type`, `category1`, `sub_category1`, `category2`, `sub_category2`, `category3`, `sub_category3`, `skill1`, `skill2`, `skill3`, `city1`, `state1`, `country1`, `city2`, `state2`, `country2`, `city3`, `state3`, `country3`, `address_line1`, `address_line2`, `address_line3`, `about`, `years_exp`, `hour_fee`, `advisor_id`, `about_seller`) VALUES
(1, 'Startup', 'Agriculture', 'Farming/Agriculture', 'Social Media', 'Social Media', 'Retail', 'Retail (Distributors)', '', '', '', '', '', '', 'Orono Town', 'Orono Town', '', 'Dallas County', 'Dallas County', '', 'Bangkok, Thailand', 'Bangor NSW, Australia', 'Dallas, TX, USA', 'ahdb vbv da', 6451, 561, 2, 'Incubators'),
(2, 'Startup', 'Automotive', 'Automotive', 'Manufacturing', 'Chemical (Basic)', 'Utility', 'Utility (Water)', '', '', '', 'Chennai', 'Tamil Nadu', 'India', 'Mumbai', 'Maharashtra', 'India', 'Ivankivs\'kyi district', 'Kyiv Oblast', 'Ukraine', 'Chennai, Tamil Nadu, India', 'Mumbai, Maharashtra, India', 'Chernobyl, Kyiv Oblast, Ukraine', 'ssd sdv sdvk skv', 7845, 7852, 20, 'Incubators');

-- --------------------------------------------------------

--
-- Table structure for table `album_file`
--

CREATE TABLE `album_file` (
  `file_id` int(11) NOT NULL,
  `file` varchar(100) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `album_file`
--

INSERT INTO `album_file` (`file_id`, `file`, `name`) VALUES
(9, 'files/20170524_132828.jpg', 'files/20170524_132828.jpg'),
(10, 'files/20170524_083642.jpg', '20170524_083642.jpg'),
(11, 'files/20170524_132828_IL523yO.jpg', '20170524_132828.jpg'),
(12, 'files/20170525_072331.jpg', '20170525_072331.jpg'),
(13, 'files/20170524_083314.jpg', '20170524_083314.jpg'),
(14, 'files/20170524_132402.jpg', '20170524_132402.jpg'),
(17, 'files/20170525_072551.jpg', 'files/20170525_072551.jpg'),
(18, 'files/20170525_092321.jpg', 'files/20170525_092321.jpg'),
(19, 'files/20170525_072517.jpg', 'files/20170525_072517.jpg'),
(22, 'files/IMG_0334_vTFZBLb.jpg', 'files/IMG_0334_vTFZBLb.jpg'),
(23, 'files/IMG_0326.jpg', 'files/IMG_0326.jpg'),
(24, 'files/IMG_0334_4hygtzX.jpg', 'files/IMG_0334_4hygtzX.jpg'),
(26, 'files/IMG_0334_kxByPbB.jpg', 'files/IMG_0334_kxByPbB.jpg'),
(29, 'files/IMG_0335_z5rNCHP.jpg', 'files/IMG_0335_z5rNCHP.jpg'),
(30, 'files/IMG_0344.jpg', 'files/IMG_0344.jpg'),
(32, 'files/IMG_0329_iJWdCa1.jpg', 'files/IMG_0329_iJWdCa1.jpg'),
(33, 'files/IMG_0264.jpg', 'files/IMG_0264.jpg'),
(36, 'files/IMG_0340.jpg', 'files/IMG_0340.jpg'),
(39, 'files/IMG_0152.jpg', 'files/IMG_0152.jpg'),
(41, 'files/IMG_0151.jpg', 'files/IMG_0151.jpg'),
(43, 'files/20170525_130519.jpg', 'files/20170525_130519.jpg'),
(44, 'files/20170525_130553.jpg', 'files/20170525_130553.jpg'),
(45, 'files/IMG_0264_weSKbxH.jpg', 'files/IMG_0264_weSKbxH.jpg'),
(46, 'files/IMG_0150_UBMB2L4.jpg', 'files/IMG_0150_UBMB2L4.jpg'),
(47, 'files/20170525_132844.jpg', 'files/20170525_132844.jpg'),
(81, 'files/HEAD_4YU4dzS', 'files/HEAD_4YU4dzS'),
(94, 'files/routing_tvk8Ade.py', 'files/routing_tvk8Ade.py'),
(96, 'files/urls_19jY3ii.py', 'files/urls_19jY3ii.py'),
(109, 'files/urls_ApPBR1V.py', 'files/urls_ApPBR1V.py'),
(110, 'files/views_4kJl1FS.py', 'files/views_4kJl1FS.py'),
(123, 'files/routing.cpython-36_N1M8241.pyc', 'files/routing.cpython-36_N1M8241.pyc'),
(125, 'files/urls.cpython-36_xyTz47G.pyc', 'files/urls.cpython-36_xyTz47G.pyc'),
(126, 'files/master_lPTczWQ', 'files/master_lPTczWQ'),
(130, 'files/auth_wUgGe7W.js', 'files/auth_wUgGe7W.js'),
(132, 'files/urls.cpython-36_Xz9VBdc.pyc', 'files/urls.cpython-36_Xz9VBdc.pyc'),
(133, 'files/views.cpython-36_1GLrV1e.pyc', 'files/views.cpython-36_1GLrV1e.pyc'),
(135, 'files/IMG_0264_Duf4l6t.jpg', 'files/IMG_0264_Duf4l6t.jpg'),
(138, 'files/IMG_0283.jpg', 'files/IMG_0283.jpg'),
(139, 'files/IMG_0303.jpg', 'files/IMG_0303.jpg'),
(141, 'files/IMG_0309_UGvkdUY.jpg', 'files/IMG_0309_UGvkdUY.jpg'),
(142, 'files/IMG_0309.jpg', 'files/IMG_0309.jpg'),
(143, 'files/IMG_0202.jpg', 'files/IMG_0202.jpg'),
(144, 'files/IMG_0202_yly4eaa.jpg', 'files/IMG_0202_yly4eaa.jpg'),
(146, 'files/IMG_0095_AaPR0ZG.jpg', 'files/IMG_0095_AaPR0ZG.jpg'),
(149, 'files/IMG_0091_IvzyHgd.jpg', 'files/IMG_0091_IvzyHgd.jpg'),
(151, 'files/IMG_0123_vsB0tQg.jpg', 'files/IMG_0123_vsB0tQg.jpg'),
(154, 'files/IMG_0079_JLtRzQQ.jpg', 'files/IMG_0079_JLtRzQQ.jpg'),
(157, 'files/IMG_0071_URzsuYD.jpg', 'files/IMG_0071_URzsuYD.jpg'),
(158, 'files/IMG_0069.jpg', 'files/IMG_0069.jpg'),
(160, 'files/IMG_0163_ICOXCGq.jpg', 'files/IMG_0163_ICOXCGq.jpg'),
(162, 'files/IMG_0167.jpg', 'files/IMG_0167.jpg'),
(163, 'files/IMG_0167_6lSdnNw.jpg', 'files/IMG_0167_6lSdnNw.jpg'),
(164, 'files/IMG_0155_jT7sVK4.jpg', 'files/IMG_0155_jT7sVK4.jpg'),
(165, 'files/IMG_0155_uhbgLhh.jpg', 'files/IMG_0155_uhbgLhh.jpg'),
(167, 'files/IMG_0094_brV2ZCk.jpg', 'files/IMG_0094_brV2ZCk.jpg'),
(169, 'files/IMG_0077_c15S3OC.jpg', 'files/IMG_0077_c15S3OC.jpg'),
(170, 'files/IMG_0178.jpg', 'files/IMG_0178.jpg'),
(171, 'files/IMG_0178_bDqMr6r.jpg', 'files/IMG_0178_bDqMr6r.jpg'),
(174, 'files/IMG_0299.jpg', 'files/IMG_0299.jpg'),
(175, 'files/IMG_0286_5GDv48s.jpg', 'files/IMG_0286_5GDv48s.jpg'),
(178, 'files/IMG_0246_lI3yAhK.jpg', 'files/IMG_0246_lI3yAhK.jpg'),
(179, 'files/IMG_0166.jpg', 'files/IMG_0166.jpg'),
(180, 'files/IMG_0155_paSKb82.jpg', 'files/IMG_0155_paSKb82.jpg'),
(181, 'files/IMG_0111.jpg', 'files/IMG_0111.jpg'),
(183, 'files/IMG_0151_npMec2b.jpg', 'files/IMG_0151_npMec2b.jpg'),
(184, 'files/IMG_0198.jpg', 'files/IMG_0198.jpg'),
(185, 'files/IMG_0198_IYsIsZ4.jpg', 'files/IMG_0198_IYsIsZ4.jpg'),
(186, 'files/IMG_0270.jpg', 'files/IMG_0270.jpg'),
(188, 'files/IMG_0272_br7dKcu.jpg', 'files/IMG_0272_br7dKcu.jpg'),
(189, 'files/IMG_0272.jpg', 'files/IMG_0272.jpg'),
(190, 'files/IMG_0164.jpg', 'files/IMG_0164.jpg'),
(191, 'files/IMG_0155_tBW7eyp.jpg', 'files/IMG_0155_tBW7eyp.jpg'),
(192, 'files/IMG_0155_GvCxwUG.jpg', 'files/IMG_0155_GvCxwUG.jpg'),
(193, 'files/IMG_0150.jpg', 'files/IMG_0150.jpg'),
(194, 'files/IMG_0318.jpg', 'files/IMG_0318.jpg'),
(198, 'files/IMG_0303_T4VTZ6u.jpg', 'files/IMG_0303_T4VTZ6u.jpg'),
(202, 'files/IMG_0063.jpg', 'files/IMG_0063.jpg'),
(204, 'files/IMG_0058.jpg', 'files/IMG_0058.jpg'),
(205, 'files/IMG_0081.jpg', 'files/IMG_0081.jpg'),
(206, 'files/IMG_0081_APJx0Fs.jpg', 'files/IMG_0081_APJx0Fs.jpg'),
(207, 'files/IMG_0025.jpg', 'files/IMG_0025.jpg'),
(208, 'files/IMG_0091_7y0BMRN.jpg', 'files/IMG_0091_7y0BMRN.jpg'),
(210, 'files/IMG_0079.jpg', 'files/IMG_0079.jpg'),
(213, 'files/IMG_0091_5UVVQ3t.jpg', 'files/IMG_0091_5UVVQ3t.jpg'),
(214, 'files/Screenshot_1.png', 'files/Screenshot_1.png'),
(215, 'files/Screenshot_1_QVB0cgd.png', 'files/Screenshot_1_QVB0cgd.png'),
(216, 'files/Screenshot_1_wcT4dQF.png', 'files/Screenshot_1_wcT4dQF.png'),
(217, 'files/IMG_0355_iGRUDce.jpg', 'files/IMG_0355_iGRUDce.jpg'),
(230, 'files/IMG_0356.jpg', 'files/IMG_0356.jpg'),
(231, 'files/IMG_0356_7pmuVrd.jpg', 'files/IMG_0356_7pmuVrd.jpg'),
(232, 'files/IMG_0356_brTzfWp.jpg', 'files/IMG_0356_brTzfWp.jpg'),
(233, 'files/IMG_0334_eI1cMXI.jpg', 'files/IMG_0334_eI1cMXI.jpg'),
(234, 'files/IMG_0334_HVJf9wD.jpg', 'files/IMG_0334_HVJf9wD.jpg'),
(235, 'files/IMG_0331.jpg', 'files/IMG_0331.jpg'),
(236, 'files/IMG_0355.jpg', 'files/IMG_0355.jpg'),
(237, 'files/IMG_0340_YSlCLKh.jpg', 'files/IMG_0340_YSlCLKh.jpg'),
(238, 'files/IMG_0331_82iMm3w.jpg', 'files/IMG_0331_82iMm3w.jpg'),
(239, 'files/IMG_0356_WSbWKld.jpg', 'files/IMG_0356_WSbWKld.jpg'),
(240, 'files/IMG_0329_L9mCiQR.jpg', 'files/IMG_0329_L9mCiQR.jpg'),
(241, 'files/IMG_0331_7a9zO6B.jpg', 'files/IMG_0331_7a9zO6B.jpg'),
(242, 'files/IMG_0340_ChjMCbV.jpg', 'files/IMG_0340_ChjMCbV.jpg'),
(243, 'files/IMG_0329_BU6rPFN.jpg', 'files/IMG_0329_BU6rPFN.jpg'),
(244, 'files/IMG_0355_64ga9as.jpg', 'files/IMG_0355_64ga9as.jpg'),
(245, 'files/IMG_0329_91He1Ni.jpg', 'files/IMG_0329_91He1Ni.jpg'),
(246, 'files/IMG_0356_SuY2yGx.jpg', 'files/IMG_0356_SuY2yGx.jpg'),
(249, 'files/IMG_0283_ia8ZsFP.jpg', 'files/IMG_0283_ia8ZsFP.jpg'),
(251, 'files/IMG_0272_IweucNq.jpg', 'files/IMG_0272_IweucNq.jpg'),
(252, 'files/IMG_0356_kwB4zib.jpg', 'files/IMG_0356_kwB4zib.jpg'),
(253, 'files/IMG_0355_bMQAEbJ.jpg', 'files/IMG_0355_bMQAEbJ.jpg'),
(255, 'files/IMG_0331_WXADeQN.jpg', 'files/IMG_0331_WXADeQN.jpg'),
(256, 'files/IMG_0334_K4jUsYN.jpg', 'files/IMG_0334_K4jUsYN.jpg'),
(257, 'files/IMG_0334_lwlb1Gw.jpg', 'files/IMG_0334_lwlb1Gw.jpg'),
(258, 'files/IMG_0331_F3Qhwor.jpg', 'files/IMG_0331_F3Qhwor.jpg'),
(260, 'files/IMG_0303_7Fwoxdk.jpg', 'files/IMG_0303_7Fwoxdk.jpg'),
(261, 'files/IMG_0332.jpg', 'files/IMG_0332.jpg'),
(262, 'files/IMG_0340_G1IoNXJ.jpg', 'files/IMG_0340_G1IoNXJ.jpg'),
(265, 'files/IMG_0355_pLg5Q8k.jpg', 'files/IMG_0355_pLg5Q8k.jpg'),
(266, 'files/IMG_0202_lygz4KQ.jpg', 'files/IMG_0202_lygz4KQ.jpg'),
(267, 'files/IMG_0272_mhwWGph.jpg', 'files/IMG_0272_mhwWGph.jpg'),
(268, 'files/IMG_0331_AtgIY1S.jpg', 'files/IMG_0331_AtgIY1S.jpg'),
(269, 'files/IMG_0332_YjUqCN0.jpg', 'files/IMG_0332_YjUqCN0.jpg'),
(270, 'files/IMG_0326_JMxBBJB.jpg', 'files/IMG_0326_JMxBBJB.jpg'),
(271, 'files/IMG_0334.jpg', 'files/IMG_0334.jpg'),
(272, 'files/IMG_0111_rk9aSe9.jpg', 'files/IMG_0111_rk9aSe9.jpg'),
(273, 'files/IMG_0334_ije184k.jpg', 'files/IMG_0334_ije184k.jpg'),
(274, 'files/IMG_0332_Igketmd.jpg', 'files/IMG_0332_Igketmd.jpg'),
(275, 'files/IMG_0340_kAwj66h.jpg', 'files/IMG_0340_kAwj66h.jpg'),
(276, 'files/IMG_0332_2mqzNRG.jpg', 'files/IMG_0332_2mqzNRG.jpg'),
(277, 'files/IMG_0331_EjHyUwj.jpg', 'files/IMG_0331_EjHyUwj.jpg'),
(278, 'files/images_15.jpg', 'files/images_15.jpg'),
(279, 'files/images_16.jpg', 'files/images_16.jpg'),
(280, 'files/images_16_x7WMZER.jpg', 'files/images_16_x7WMZER.jpg'),
(281, 'files/download_2.jpg', 'files/download_2.jpg'),
(282, 'files/images_8.jpg', 'files/images_8.jpg'),
(283, 'files/download.jpg', 'files/download.jpg'),
(284, 'files/images_3.jpg', 'files/images_3.jpg'),
(285, 'files/download_6_1hBTJrY.jpg', 'files/download_6_1hBTJrY.jpg'),
(286, 'files/download_7_NY9Usz9.jpg', 'files/download_7_NY9Usz9.jpg'),
(287, 'files/download_8_S0cEgZX.jpg', 'files/download_8_S0cEgZX.jpg'),
(288, 'files/images_7.jpg', 'files/images_7.jpg'),
(289, 'files/images_6.jpg', 'files/images_6.jpg'),
(290, 'files/images_8_tHk7H4R.jpg', 'files/images_8_tHk7H4R.jpg'),
(291, 'files/download_8_80N1etI.jpg', 'files/download_8_80N1etI.jpg'),
(292, 'files/download_Rx9EtTC.jpg', 'files/download_Rx9EtTC.jpg'),
(293, 'files/images_1_52CiZ5I.jpg', 'files/images_1_52CiZ5I.jpg'),
(294, 'files/download_4_XCcqIN8.jpg', 'files/download_4_XCcqIN8.jpg'),
(295, 'files/download_3.jpg', 'files/download_3.jpg'),
(296, 'files/download_7WGSDrE.jpg', 'files/download_7WGSDrE.jpg'),
(297, 'files/images_5.jpg', 'files/images_5.jpg'),
(298, 'files/images_4.jpg', 'files/images_4.jpg'),
(299, 'files/images_8_kA2ahkA.jpg', 'files/images_8_kA2ahkA.jpg'),
(300, 'files/download_1.jpg', 'files/download_1.jpg'),
(301, 'files/download_4_XbDJ8gK.jpg', 'files/download_4_XbDJ8gK.jpg'),
(302, 'files/download_4_lr24v9f.jpg', 'files/download_4_lr24v9f.jpg'),
(303, 'files/download_1_RjWQux4.jpg', 'files/download_1_RjWQux4.jpg'),
(304, 'files/download_4_2XwJ21Z.jpg', 'files/download_4_2XwJ21Z.jpg'),
(305, 'files/download_9_V36ZUSN.jpg', 'files/download_9_V36ZUSN.jpg'),
(306, 'files/download_u0qcupY.jpg', 'files/download_u0qcupY.jpg'),
(307, 'files/images_1_24niO11.jpg', 'files/images_1_24niO11.jpg'),
(308, 'files/images_4_IPAtbJH.jpg', 'files/images_4_IPAtbJH.jpg'),
(309, 'files/images_3_1nAmcFV.jpg', 'files/images_3_1nAmcFV.jpg'),
(310, 'files/download_5_9vxauJq.jpg', 'files/download_5_9vxauJq.jpg'),
(311, 'files/download_6_Bdb8n5i.jpg', 'files/download_6_Bdb8n5i.jpg'),
(312, 'files/download_2_bRxL1Vg.jpg', 'files/download_2_bRxL1Vg.jpg'),
(313, 'files/download_4_G5VQB2y.jpg', 'files/download_4_G5VQB2y.jpg'),
(314, 'files/download_4_DDCUwFr.jpg', 'files/download_4_DDCUwFr.jpg'),
(315, 'files/download_8_2zSauTr.jpg', 'files/download_8_2zSauTr.jpg'),
(316, 'files/download_9_FqLwvlz.jpg', 'files/download_9_FqLwvlz.jpg'),
(317, 'files/images_3_u5GJxLT.jpg', 'files/images_3_u5GJxLT.jpg'),
(318, 'files/download_8_VsZtj6d.jpg', 'files/download_8_VsZtj6d.jpg'),
(319, 'files/download_4_AfPEOkI.jpg', 'files/download_4_AfPEOkI.jpg'),
(320, 'files/download_4_u94HoKN.jpg', 'files/download_4_u94HoKN.jpg'),
(321, 'files/download_2_14jV72d.jpg', 'files/download_2_14jV72d.jpg'),
(322, 'files/download_6_CRAH8Qu.jpg', 'files/download_6_CRAH8Qu.jpg'),
(323, 'files/download_4_DP8vAqC.jpg', 'files/download_4_DP8vAqC.jpg'),
(324, 'files/download_5_WTKm2hJ.jpg', 'files/download_5_WTKm2hJ.jpg'),
(325, 'files/images_1_CL3Erfg.jpg', 'files/images_1_CL3Erfg.jpg'),
(326, 'files/images_5_hbIcTuY.jpg', 'files/images_5_hbIcTuY.jpg'),
(327, 'files/download_7_ZhkhxCQ.jpg', 'files/download_7_ZhkhxCQ.jpg'),
(328, 'files/download_6_Pji51Mw.jpg', 'files/download_6_Pji51Mw.jpg'),
(329, 'files/download_7_B3aRtVY.jpg', 'files/download_7_B3aRtVY.jpg'),
(330, 'files/download_9_usgfTiP.jpg', 'files/download_9_usgfTiP.jpg'),
(331, 'files/download_9_jq4yMdD.jpg', 'files/download_9_jq4yMdD.jpg'),
(332, 'files/download_5_HOIwoM5.jpg', 'files/download_5_HOIwoM5.jpg'),
(333, 'files/images_16_mevAGIM.jpg', 'files/images_16_mevAGIM.jpg'),
(334, 'files/images_12_YOwdWxZ.jpg', 'files/images_12_YOwdWxZ.jpg'),
(335, 'files/images_11.jpg', 'files/images_11.jpg'),
(336, 'files/images_13.jpg', 'files/images_13.jpg'),
(337, 'files/download_3_tV1Qogj.jpg', 'files/download_3_tV1Qogj.jpg'),
(338, 'files/download_2_ucg8Q7B.jpg', 'files/download_2_ucg8Q7B.jpg'),
(339, 'files/download_6_DwllkMN.jpg', 'files/download_6_DwllkMN.jpg'),
(340, 'files/download_5_KgVU93h.jpg', 'files/download_5_KgVU93h.jpg'),
(341, 'files/download_1_LlZcnlH.jpg', 'files/download_1_LlZcnlH.jpg'),
(342, 'files/download_6_68eLbV4.jpg', 'files/download_6_68eLbV4.jpg'),
(343, 'files/download_5_po4adMv.jpg', 'files/download_5_po4adMv.jpg'),
(344, 'files/download_1_PWFq3hu.jpg', 'files/download_1_PWFq3hu.jpg'),
(345, 'files/download_6_GGyBWvv.jpg', 'files/download_6_GGyBWvv.jpg'),
(346, 'files/images_12_wnIkkYb.jpg', 'files/images_12_wnIkkYb.jpg'),
(347, 'files/images_16_c275qJh.jpg', 'files/images_16_c275qJh.jpg'),
(348, 'files/images.jpg', 'files/images.jpg'),
(349, 'files/download_6_9Y2gmX7.jpg', 'files/download_6_9Y2gmX7.jpg'),
(350, 'files/download_7_NGZW2hf.jpg', 'files/download_7_NGZW2hf.jpg'),
(351, 'files/download_5_c4PtqwL.jpg', 'files/download_5_c4PtqwL.jpg'),
(352, 'files/download_6_c0rossD.jpg', 'files/download_6_c0rossD.jpg'),
(353, 'files/images_16_p0alUj4.jpg', 'files/images_16_p0alUj4.jpg'),
(354, 'files/images_27HqBIP.jpg', 'files/images_27HqBIP.jpg'),
(355, 'files/images_13_45aOkdl.jpg', 'files/images_13_45aOkdl.jpg'),
(356, 'files/images_qQkUs2g.jpg', 'files/images_qQkUs2g.jpg'),
(357, 'files/download_5_0crpYdJ.jpg', 'files/download_5_0crpYdJ.jpg'),
(358, 'files/download_6_7vHPiIM.jpg', 'files/download_6_7vHPiIM.jpg'),
(359, 'files/download_7_cwYKCBn.jpg', 'files/download_7_cwYKCBn.jpg'),
(360, 'files/download_7_hG61uPt.jpg', 'files/download_7_hG61uPt.jpg'),
(361, 'files/download_6_9focKFT.jpg', 'files/download_6_9focKFT.jpg'),
(362, 'files/download_8_dziEOvd.jpg', 'files/download_8_dziEOvd.jpg'),
(363, 'files/images_16_fpBt5HY.jpg', 'files/images_16_fpBt5HY.jpg'),
(364, 'files/images_ktiORsa.jpg', 'files/images_ktiORsa.jpg'),
(365, 'files/download_6_qFdUWrv.jpg', 'files/download_6_qFdUWrv.jpg'),
(366, 'files/download_7_m2k2yBF.jpg', 'files/download_7_m2k2yBF.jpg'),
(367, 'files/images_3_fsZerZV.jpg', 'files/images_3_fsZerZV.jpg'),
(368, 'files/images_4cTlqPi.jpg', 'files/images_4cTlqPi.jpg'),
(369, 'files/images_11_piGhtcL.jpg', 'files/images_11_piGhtcL.jpg'),
(370, 'files/download_6_WAXJU7c.jpg', 'files/download_6_WAXJU7c.jpg'),
(371, 'files/download_7_gHXOF8B.jpg', 'files/download_7_gHXOF8B.jpg'),
(372, 'files/images_16_e8oMOqk.jpg', 'files/images_16_e8oMOqk.jpg'),
(373, 'files/images_11_gCITeqA.jpg', 'files/images_11_gCITeqA.jpg'),
(374, 'files/images_rdBCShh.jpg', 'files/images_rdBCShh.jpg'),
(375, 'files/images_10.jpg', 'files/images_10.jpg'),
(376, 'files/images_9.jpg', 'files/images_9.jpg'),
(377, 'files/images_8_pT7Sdmf.jpg', 'files/images_8_pT7Sdmf.jpg'),
(378, 'files/images_9_mzESRfG.jpg', 'files/images_9_mzESRfG.jpg'),
(379, 'files/images_5_DNSoFax.jpg', 'files/images_5_DNSoFax.jpg'),
(380, 'files/images_6_QvrMI5C.jpg', 'files/images_6_QvrMI5C.jpg'),
(381, 'files/images_10_xRhbO31.jpg', 'files/images_10_xRhbO31.jpg'),
(382, 'files/images_5_sJHLZdE.jpg', 'files/images_5_sJHLZdE.jpg'),
(383, 'files/images_1_fTB36Th.jpg', 'files/images_1_fTB36Th.jpg'),
(384, 'files/images_6_sduRFdh.jpg', 'files/images_6_sduRFdh.jpg'),
(385, 'files/images_4_MSqQyjj.jpg', 'files/images_4_MSqQyjj.jpg'),
(386, 'files/images_9_f0yetsG.jpg', 'files/images_9_f0yetsG.jpg'),
(387, 'files/images_10_8mYPJRM.jpg', 'files/images_10_8mYPJRM.jpg'),
(388, 'files/download_2kseozj.jpg', 'files/download_2kseozj.jpg'),
(389, 'files/images_1_0dmrSjh.jpg', 'files/images_1_0dmrSjh.jpg'),
(390, 'files/download_5_cE1h0It.jpg', 'files/download_5_cE1h0It.jpg'),
(391, 'files/download_5_L23ub4I.jpg', 'files/download_5_L23ub4I.jpg'),
(392, 'files/download_4_TtpAFRy.jpg', 'files/download_4_TtpAFRy.jpg'),
(393, 'files/download_EzeFuKj.jpg', 'files/download_EzeFuKj.jpg'),
(394, 'files/download_7_ev2f77k.jpg', 'files/download_7_ev2f77k.jpg'),
(395, 'files/download_6_g35aBfm.jpg', 'files/download_6_g35aBfm.jpg'),
(397, 'files/download_1_zAYfSW0.jpg', 'files/download_1_zAYfSW0.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `album_kalbumforfile`
--

CREATE TABLE `album_kalbumforfile` (
  `album_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `album_kalbumforfile`
--

INSERT INTO `album_kalbumforfile` (`album_id`) VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10),
(11),
(12),
(13),
(14),
(15),
(16),
(17),
(18),
(19),
(20),
(21),
(22),
(23),
(24),
(25),
(26),
(27),
(28),
(29),
(30),
(31),
(32),
(33),
(34),
(35),
(36),
(37),
(38),
(39),
(40),
(41),
(42),
(43),
(44),
(45),
(46),
(47),
(48),
(49),
(50),
(51),
(52),
(53),
(54),
(55),
(56),
(57),
(58),
(59),
(60),
(61),
(62),
(63),
(64),
(65),
(66),
(67),
(68),
(69),
(70),
(71),
(72),
(73),
(74),
(75),
(76),
(77),
(78),
(79),
(80),
(81),
(82),
(84),
(85),
(86),
(87),
(88),
(89),
(90),
(91),
(92),
(93),
(94),
(95),
(96),
(97),
(98),
(99),
(100),
(101),
(102),
(103),
(104),
(105),
(106),
(107),
(108),
(109),
(110),
(111),
(112),
(113),
(114),
(115),
(116),
(117),
(118),
(119),
(120),
(121),
(122),
(123),
(124),
(125),
(126),
(127),
(128),
(129),
(130),
(131),
(132),
(133),
(134),
(135),
(136),
(137),
(138),
(139);

-- --------------------------------------------------------

--
-- Table structure for table `album_kalbumforfile_files`
--

CREATE TABLE `album_kalbumforfile_files` (
  `id` int(11) NOT NULL,
  `kalbumforfile_id` int(11) NOT NULL,
  `file_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `album_kalbumforfile_files`
--

INSERT INTO `album_kalbumforfile_files` (`id`, `kalbumforfile_id`, `file_id`) VALUES
(4, 4, 30),
(7, 7, 33),
(9, 8, 36),
(12, 9, 39),
(14, 10, 41),
(16, 11, 43),
(17, 11, 44),
(19, 12, 33),
(20, 12, 47),
(97, 14, 33),
(100, 16, 138),
(101, 16, 139),
(103, 17, 142),
(104, 18, 143),
(113, 24, 158),
(116, 26, 162),
(120, 29, 170),
(123, 31, 174),
(127, 33, 183),
(128, 33, 184),
(129, 33, 185),
(130, 34, 186),
(132, 34, 188),
(133, 34, 189),
(134, 35, 190),
(135, 35, 191),
(136, 35, 192),
(137, 35, 193),
(138, 36, 194),
(142, 36, 198),
(145, 37, 202),
(148, 37, 204),
(149, 38, 205),
(150, 39, 206),
(151, 40, 207),
(152, 41, 208),
(154, 43, 210),
(157, 46, 213),
(158, 47, 214),
(159, 48, 215),
(160, 49, 216),
(161, 49, 217),
(174, 57, 230),
(175, 58, 231),
(176, 59, 232),
(177, 60, 233),
(178, 61, 234),
(179, 62, 235),
(180, 63, 236),
(181, 64, 237),
(182, 65, 238),
(183, 66, 239),
(184, 67, 240),
(185, 68, 241),
(186, 69, 242),
(187, 70, 243),
(188, 71, 244),
(189, 72, 245),
(190, 72, 246),
(193, 73, 249),
(195, 74, 251),
(196, 75, 252),
(197, 76, 253),
(199, 77, 255),
(200, 78, 256),
(201, 79, 257),
(202, 80, 258),
(204, 81, 260),
(205, 82, 261),
(206, 82, 262),
(209, 84, 265),
(210, 85, 266),
(211, 86, 267),
(212, 87, 268),
(213, 87, 269),
(214, 88, 270),
(215, 88, 271),
(216, 89, 272),
(217, 89, 273),
(218, 90, 274),
(219, 90, 275),
(220, 91, 276),
(221, 91, 277),
(222, 92, 278),
(223, 92, 279),
(224, 93, 280),
(225, 94, 281),
(226, 95, 282),
(227, 96, 283),
(228, 97, 284),
(229, 98, 285),
(230, 98, 286),
(231, 98, 287),
(232, 99, 288),
(233, 99, 289),
(234, 99, 290),
(235, 100, 291),
(236, 100, 292),
(237, 100, 293),
(238, 101, 294),
(239, 101, 295),
(240, 101, 296),
(241, 102, 297),
(242, 102, 298),
(243, 102, 299),
(244, 103, 300),
(245, 103, 301),
(247, 104, 302),
(246, 104, 303),
(249, 105, 304),
(248, 105, 305),
(250, 105, 306),
(251, 105, 307),
(252, 106, 308),
(253, 106, 309),
(254, 107, 310),
(255, 107, 311),
(256, 107, 312),
(257, 108, 313),
(259, 109, 314),
(258, 109, 315),
(260, 110, 316),
(261, 110, 317),
(262, 111, 318),
(263, 111, 319),
(264, 112, 320),
(265, 112, 321),
(266, 112, 322),
(267, 113, 323),
(268, 113, 324),
(269, 114, 325),
(270, 114, 326),
(271, 114, 327),
(272, 115, 328),
(273, 115, 329),
(274, 115, 330),
(275, 116, 331),
(276, 116, 332),
(277, 116, 333),
(278, 117, 334),
(279, 117, 335),
(280, 117, 336),
(281, 118, 337),
(282, 118, 338),
(283, 118, 339),
(285, 119, 340),
(284, 119, 341),
(286, 119, 342),
(287, 120, 343),
(288, 120, 344),
(289, 120, 345),
(290, 120, 346),
(291, 120, 347),
(292, 120, 348),
(293, 121, 349),
(294, 121, 350),
(295, 122, 351),
(296, 122, 352),
(297, 123, 353),
(298, 123, 354),
(299, 124, 355),
(300, 124, 356),
(301, 125, 357),
(302, 125, 358),
(303, 125, 359),
(304, 126, 360),
(305, 126, 361),
(306, 126, 362),
(307, 127, 363),
(308, 127, 364),
(309, 128, 365),
(310, 128, 366),
(311, 128, 367),
(312, 129, 368),
(313, 129, 369),
(314, 130, 370),
(315, 130, 371),
(316, 131, 372),
(317, 131, 373),
(318, 131, 374),
(319, 132, 375),
(320, 132, 376),
(321, 133, 377),
(322, 133, 378),
(323, 134, 379),
(324, 134, 380),
(325, 134, 381),
(326, 135, 382),
(327, 135, 383),
(328, 135, 384),
(329, 136, 385),
(330, 136, 386),
(331, 136, 387),
(333, 137, 388),
(332, 137, 389),
(334, 137, 390),
(335, 138, 391),
(336, 138, 392),
(337, 138, 393),
(338, 139, 394),
(339, 139, 395),
(341, 139, 397);

-- --------------------------------------------------------

--
-- Table structure for table `album_kalbumforfile_seller`
--

CREATE TABLE `album_kalbumforfile_seller` (
  `id` int(11) NOT NULL,
  `kalbumforfile_id` int(11) NOT NULL,
  `sellbusiness_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add advisor', 7, 'add_advisor'),
(26, 'Can change advisor', 7, 'change_advisor'),
(27, 'Can delete advisor', 7, 'delete_advisor'),
(28, 'Can view advisor', 7, 'view_advisor'),
(29, 'Can add business sectors', 8, 'add_businesssectors'),
(30, 'Can change business sectors', 8, 'change_businesssectors'),
(31, 'Can delete business sectors', 8, 'delete_businesssectors'),
(32, 'Can view business sectors', 8, 'view_businesssectors'),
(33, 'Can add codes', 9, 'add_codes'),
(34, 'Can change codes', 9, 'change_codes'),
(35, 'Can delete codes', 9, 'delete_codes'),
(36, 'Can view codes', 9, 'view_codes'),
(37, 'Can add company', 10, 'add_company'),
(38, 'Can change company', 10, 'change_company'),
(39, 'Can delete company', 10, 'delete_company'),
(40, 'Can view company', 10, 'view_company'),
(41, 'Can add countries', 11, 'add_countries'),
(42, 'Can change countries', 11, 'change_countries'),
(43, 'Can delete countries', 11, 'delete_countries'),
(44, 'Can view countries', 11, 'view_countries'),
(45, 'Can add association', 12, 'add_association'),
(46, 'Can change association', 12, 'change_association'),
(47, 'Can delete association', 12, 'delete_association'),
(48, 'Can view association', 12, 'view_association'),
(49, 'Can add code', 13, 'add_code'),
(50, 'Can change code', 13, 'change_code'),
(51, 'Can delete code', 13, 'delete_code'),
(52, 'Can view code', 13, 'view_code'),
(53, 'Can add nonce', 14, 'add_nonce'),
(54, 'Can change nonce', 14, 'change_nonce'),
(55, 'Can delete nonce', 14, 'delete_nonce'),
(56, 'Can view nonce', 14, 'view_nonce'),
(57, 'Can add user social auth', 15, 'add_usersocialauth'),
(58, 'Can change user social auth', 15, 'change_usersocialauth'),
(59, 'Can delete user social auth', 15, 'delete_usersocialauth'),
(60, 'Can view user social auth', 15, 'view_usersocialauth'),
(61, 'Can add partial', 16, 'add_partial'),
(62, 'Can change partial', 16, 'change_partial'),
(63, 'Can delete partial', 16, 'delete_partial'),
(64, 'Can view partial', 16, 'view_partial'),
(65, 'Can add seller1', 17, 'add_seller1'),
(66, 'Can change seller1', 17, 'change_seller1'),
(67, 'Can delete seller1', 17, 'delete_seller1'),
(68, 'Can view seller1', 17, 'view_seller1'),
(69, 'Can add years', 18, 'add_years'),
(70, 'Can change years', 18, 'change_years'),
(71, 'Can delete years', 18, 'delete_years'),
(72, 'Can view years', 18, 'view_years'),
(73, 'Can add file', 19, 'add_file'),
(74, 'Can change file', 19, 'change_file'),
(75, 'Can delete file', 19, 'delete_file'),
(76, 'Can view file', 19, 'view_file'),
(77, 'Can add album', 20, 'add_album'),
(78, 'Can change album', 20, 'change_album'),
(79, 'Can delete album', 20, 'delete_album'),
(80, 'Can view album', 20, 'view_album'),
(81, 'Can add ablumfiles', 21, 'add_ablumfiles'),
(82, 'Can change ablumfiles', 21, 'change_ablumfiles'),
(83, 'Can delete ablumfiles', 21, 'delete_ablumfiles'),
(84, 'Can view ablumfiles', 21, 'view_ablumfiles'),
(85, 'Can add sell business', 22, 'add_sellbusiness'),
(86, 'Can change sell business', 22, 'change_sellbusiness'),
(87, 'Can delete sell business', 22, 'delete_sellbusiness'),
(88, 'Can add sell asset', 23, 'add_sellasset'),
(89, 'Can change sell asset', 23, 'change_sellasset'),
(90, 'Can delete sell asset', 23, 'delete_sellasset'),
(91, 'Can add sell equity', 24, 'add_sellequity'),
(92, 'Can change sell equity', 24, 'change_sellequity'),
(93, 'Can delete sell equity', 24, 'delete_sellequity'),
(94, 'Can add raise loan', 25, 'add_raiseloan'),
(95, 'Can change raise loan', 25, 'change_raiseloan'),
(96, 'Can delete raise loan', 25, 'delete_raiseloan'),
(97, 'Can add k album for file', 26, 'add_kalbumforfile'),
(98, 'Can change k album for file', 26, 'change_kalbumforfile'),
(99, 'Can delete k album for file', 26, 'delete_kalbumforfile'),
(100, 'Can add profile', 27, 'add_profile'),
(101, 'Can change profile', 27, 'change_profile'),
(102, 'Can delete profile', 27, 'delete_profile'),
(103, 'Can add message', 28, 'add_message'),
(104, 'Can change message', 28, 'change_message'),
(105, 'Can delete message', 28, 'delete_message'),
(106, 'Can add contact', 29, 'add_contact'),
(107, 'Can change contact', 29, 'change_contact'),
(108, 'Can delete contact', 29, 'delete_contact'),
(109, 'Can add chat', 30, 'add_chat'),
(110, 'Can change chat', 30, 'change_chat'),
(111, 'Can delete chat', 30, 'delete_chat'),
(112, 'Can add revenue model', 31, 'add_revenuemodel'),
(113, 'Can change revenue model', 31, 'change_revenuemodel'),
(114, 'Can delete revenue model', 31, 'delete_revenuemodel'),
(115, 'Can add sell startup', 32, 'add_sellstartup'),
(116, 'Can change sell startup', 32, 'change_sellstartup'),
(117, 'Can delete sell startup', 32, 'delete_sellstartup'),
(118, 'Can add sell app', 33, 'add_sellapp'),
(119, 'Can change sell app', 33, 'change_sellapp'),
(120, 'Can delete sell app', 33, 'delete_sellapp'),
(121, 'Can add sell ipcode', 34, 'add_sellipcode'),
(122, 'Can change sell ipcode', 34, 'change_sellipcode'),
(123, 'Can delete sell ipcode', 34, 'delete_sellipcode'),
(124, 'Can add individual investor', 35, 'add_individualinvestor'),
(125, 'Can change individual investor', 35, 'change_individualinvestor'),
(126, 'Can delete individual investor', 35, 'delete_individualinvestor'),
(127, 'Can add company investor', 36, 'add_companyinvestor'),
(128, 'Can change company investor', 36, 'change_companyinvestor'),
(129, 'Can delete company investor', 36, 'delete_companyinvestor'),
(130, 'Can add investor', 37, 'add_investor'),
(131, 'Can change investor', 37, 'change_investor'),
(132, 'Can delete investor', 37, 'delete_investor'),
(133, 'Can add business advisor', 38, 'add_businessadvisor'),
(134, 'Can change business advisor', 38, 'change_businessadvisor'),
(135, 'Can delete business advisor', 38, 'delete_businessadvisor'),
(136, 'Can add advisor', 39, 'add_advisor'),
(137, 'Can change advisor', 39, 'change_advisor'),
(138, 'Can delete advisor', 39, 'delete_advisor'),
(139, 'Can add startup advisor', 40, 'add_startupadvisor'),
(140, 'Can change startup advisor', 40, 'change_startupadvisor'),
(141, 'Can delete startup advisor', 40, 'delete_startupadvisor'),
(142, 'Can add sell', 41, 'add_sell'),
(143, 'Can change sell', 41, 'change_sell'),
(144, 'Can delete sell', 41, 'delete_sell'),
(145, 'Can add advise', 42, 'add_advise'),
(146, 'Can change advise', 42, 'change_advise'),
(147, 'Can delete advise', 42, 'delete_advise'),
(148, 'Can add invest', 43, 'add_invest'),
(149, 'Can change invest', 43, 'change_invest'),
(150, 'Can delete invest', 43, 'delete_invest'),
(151, 'Can add malbum', 44, 'add_malbum'),
(152, 'Can change malbum', 44, 'change_malbum'),
(153, 'Can delete malbum', 44, 'delete_malbum');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$488y8eb5hQFK$b7JwBPKvgo9xQ7rgfNzsYvtRnNgPkQC003ggctWQkw4=', NULL, 0, 'prajwalbarapatre', '', '', 'prajwalbarapatre13@gmail.com', 0, 1, '2019-05-08 19:23:50.839926'),
(2, 'pbkdf2_sha256$100000$jVl6t9hbeLrH$CgaL8Srpuy8e3jVXOBuzkylT1yEcqAfOODcIEJBytpg=', NULL, 0, 'prajwalbarapatre1', '', '', 'prajwal@gmail.com', 0, 1, '2019-05-08 19:29:28.342127'),
(3, 'pbkdf2_sha256$100000$6rVLKmR7Ed8i$mZtpskQ4G3fqCZWxnHQwOXJPqsUrmN7B9wmbi9vSU3g=', NULL, 0, 'prajwalbarapatre13', '', '', 'prajwal13@gmail.com', 0, 1, '2019-05-08 19:41:04.673937'),
(4, 'pbkdf2_sha256$100000$wHeQSexwXLGk$ZvVPTnM+bqcUnuBqw0t7tMkOGq35dB9em0qOH+J01KA=', NULL, 0, 'prajwalbarapatre_13', '', '', 'prajwal_13@gmail.com', 0, 1, '2019-05-08 19:43:20.258754'),
(5, 'pbkdf2_sha256$100000$TRPGWEaRKM5Z$cuiD3fzutwiQ0CHsB21ntwr3v2mZtFuDEXIR5cQU5ww=', '2019-06-29 20:27:40.747465', 0, 'prajwalbarapatre_15', '', '', '17D070005@iitb.ac.in', 0, 1, '2019-05-08 19:47:14.771867'),
(6, 'pbkdf2_sha256$100000$0IaXNPat4KJz$WdwP7PPpgKblaiJDo6A1B8+NA9OucwAYdMoIfxrreqM=', '2019-05-08 20:24:56.222274', 0, 'admin', '', '', '17D070004@iitb.ac.in', 0, 1, '2019-05-08 20:24:50.223892'),
(7, 'pbkdf2_sha256$100000$lLdf4CDGEbct$WLhJ/T5lfZXnENeWZEgy3S6pBWj0RFVQarCIRUccl7U=', '2019-05-08 20:30:34.278216', 0, 'jsnv', '', '', 'aadiupadh@yahoo.co.in', 0, 1, '2019-05-08 20:30:28.468584'),
(8, 'pbkdf2_sha256$100000$EttQgh20NTz8$WUIPkWujrw5Ub1UMYZV/cMEGFiMEf8yvbwhbV/92Xm4=', '2019-05-09 14:10:01.031868', 0, 'prajwalb', '', '', '17D070015@iitb.ac.in', 0, 1, '2019-05-09 14:07:26.297375'),
(9, 'pbkdf2_sha256$100000$Y9FsOqttdhaE$e/ZKzOo+4sq8VYKEtmEAK+cxV6g3+24YaI0h6N+xAbk=', NULL, 0, 'prajwalbara', '', '', '17D0700155@iitb.ac.in', 0, 1, '2019-05-09 14:16:03.296849'),
(10, 'pbkdf2_sha256$100000$rtrSh4FVC6pJ$EDPPKGcl4wVJ4lkAvit69l6MY63DIzITv/VGtKUWLGc=', '2019-05-09 18:29:08.612073', 0, 'minu', '', '', '17D070025@iitb.ac.in', 0, 1, '2019-05-09 18:29:07.263037'),
(11, 'pbkdf2_sha256$100000$FECgxdItcNdQ$to81pnbXTeeJXEoD/6ZXivTAiRkobIgGKyGTKszpkMs=', NULL, 0, 'mrunali_bara', '', '', 'minuistupid@gmail.com', 0, 1, '2019-05-09 19:27:59.260506'),
(12, 'pbkdf2_sha256$100000$Ej2PKI4bjd2Y$X1YzVJhwBCe9I2xgCecMdnWG6XXQvdNdM9V2il31wFE=', '2019-05-09 19:32:02.994377', 0, 'mrunali_barapatre', '', '', 'minuisstupid@gmail.com', 0, 1, '2019-05-09 19:32:02.059513'),
(13, 'pbkdf2_sha256$100000$4UNk4MPq4JhQ$CxGARQoKcyFqi1DXYrRQSmUSAeGJ6PsI7iGsMgfdyKU=', '2019-05-09 19:50:07.065139', 0, 'kjfv', '', '', 'good@gmail.com', 0, 1, '2019-05-09 19:35:45.288852'),
(14, 'pbkdf2_sha256$100000$H828umkmBU5l$H96iP7GmBKx3g4gkBCPsDAA9mRC1ilaAkKBLM7Bwaag=', NULL, 0, 'trying', '', '', 'trying@gmail.com', 0, 1, '2019-05-09 20:55:52.816703'),
(15, 'pbkdf2_sha256$100000$scubzLGFjQd9$XSc4k56Cz1DNdHvDmpvV8JjqZYbkYXpOC/ku+bI8wZw=', '2019-05-09 21:08:08.573904', 0, 'trying2', '', '', 'trying2@gmail.com', 0, 1, '2019-05-09 21:06:03.363990'),
(16, 'pbkdf2_sha256$100000$y12EnSopMLRZ$EerWnjFqNNR1/V65M4uPy5aVch/pyfAz15puHyupy4k=', '2019-05-09 21:10:45.002322', 0, 'trying3', '', '', 'trying3@gmail.com', 0, 1, '2019-05-09 21:10:43.890144'),
(17, 'pbkdf2_sha256$100000$HUALIpH62LLI$eMa3PXh3hr41Kb4IR9gltVOTuUWIu5NGUMwYQRFjmrQ=', NULL, 0, 'trying5', '', '', 'trying5@gmail.com', 0, 1, '2019-05-09 21:14:54.772178'),
(18, 'pbkdf2_sha256$100000$ZV3qiFsX7Tug$CuPdgAP+o+V7mRhxS5f2Lttx9riy9J2WQq8RETFFGlo=', '2019-05-09 22:14:57.892490', 0, 'trying8', '', '', 'trying8@gmail.com', 0, 1, '2019-05-09 22:14:56.858793'),
(19, 'pbkdf2_sha256$100000$dVaYyy7wXZnG$Moe9ZhH2ZbA6P4oKJpf1Z7oBkQYlhign8u5rb7Z6ttI=', '2019-05-09 22:19:59.428237', 0, 'trying9', '', '', 'trying9@gmail.com', 0, 1, '2019-05-09 22:19:58.212731'),
(20, 'pbkdf2_sha256$100000$Zxx5tF75d0KR$lXSucjtwZT1KNFUkd9s+NAaxJd8lPFOIAnWwJMmtoBc=', '2019-06-29 11:15:40.857342', 0, 'minu1', '', '', 'minu1@gmail.com', 0, 1, '2019-05-10 09:26:38.458580'),
(21, 'pbkdf2_sha256$100000$A8hoHtUAgfKU$cfpnOwqcqRJotNb/KjO5gqPIZCfvcXgQoATQEo/rD78=', '2019-05-11 11:14:26.673303', 0, 'prithvi_raj', '', '', 'prithvi_raj12@gmail.com', 0, 1, '2019-05-11 11:14:25.600411'),
(22, 'pbkdf2_sha256$100000$Fn17QICmm0vD$CmRIxAUu9TQZ99Rx3s5VeIabnIrQRPlNz+1R4pJqIJk=', '2019-05-31 15:01:27.775085', 0, 'adminda', '', '', 'prithvi1@gmail.com', 0, 1, '2019-05-31 15:01:26.385801'),
(23, 'pbkdf2_sha256$100000$MPKRZ6XVuppp$6Ki9cPpMQAScorR26W2DjnvYhnPbJiBnemG6HwZPUpg=', '2019-06-02 09:47:30.102305', 0, 'minuprajwal', '', '', 'minuprajwal15@gmail.com', 0, 1, '2019-06-02 06:50:56.181769'),
(24, 'pbkdf2_sha256$100000$91JWzBAoDEzE$PS+HYrDG+XJpj/dkoPDTqXXpvK1AboYYoKaV82JiVlc=', '2019-06-02 06:57:15.636675', 0, 'vimalbarapatre', '', '', 'vimalb@gmail.com', 0, 1, '2019-06-02 06:57:14.439929'),
(25, 'pbkdf2_sha256$100000$0qm8LKJc1Ksh$fAlnGpheiVwAhkL55IBOBZ0sSX6I/jOaQjMnM2Ab6Po=', '2019-06-02 07:00:15.762676', 0, 'subhashbarapatre', '', '', 'subhashb@gmail.com', 0, 1, '2019-06-02 07:00:14.696700'),
(26, 'pbkdf2_sha256$100000$OkBs0MOp9vji$Ctrjfz3fOGu8nxSG1v5Rzt4EK4nGI5tH4bDnn1MlQKM=', '2019-06-02 07:01:56.601734', 0, 'sweetypriya', '', '', 'sweetyp@gmail.com', 0, 1, '2019-06-02 07:01:55.547261'),
(27, 'pbkdf2_sha256$100000$bp5Zg9PJUXwX$MciAVRnH6Egcv7g7tfEBUQ3/BUuk3sYFUYLwqOgd1QA=', '2019-06-21 10:38:14.521472', 0, 'renukadhakate', '', '', 'renukad@gmail.com', 0, 1, '2019-06-02 07:21:38.098231'),
(28, 'pbkdf2_sha256$100000$4S3jILdVE6Ph$Vbr+rImkXfGwOtKKEMJBgWI+Gd2jB583AKcg8z5oVes=', '2019-06-02 07:30:07.713013', 0, 'thrishadhakate', '', '', 'thrishad@gmail.com', 0, 1, '2019-06-02 07:23:07.425798'),
(29, 'pbkdf2_sha256$100000$VuWI24v8CevN$xEB/JUuh1tdE6SmlZsoQnWLDdzVzfoCfWa59AvyErk8=', '2019-06-02 07:25:32.556497', 0, 'ushabarapatre', '', '', 'ushab@gmail.com', 0, 1, '2019-06-02 07:25:31.731290'),
(30, 'pbkdf2_sha256$100000$a2hNdqOuuVA7$duH8ypbHoDMgjwwZmNuyKWZTMHVKpF3mFy1E/TlW4s8=', '2019-06-02 07:31:02.098660', 0, 'vidhyadhakate', '', '', 'vidhyad@gmail.com', 0, 1, '2019-06-02 07:27:45.412709'),
(31, 'pbkdf2_sha256$100000$rDFOdwaKVZUq$FqmP78ey0jK7DJWXmNRqn6hvJCsaFzbTPmFjP7lPQOM=', '2019-06-27 19:46:47.719392', 0, 'vimal', '', '', 'vimal@gmail.com', 0, 1, '2019-06-21 06:06:38.567168'),
(32, 'pbkdf2_sha256$100000$YtXtguvqKLeP$E9Ystmu0lkuAjRfGkv3tfoaY1D+25ufphg+0NJUm6Jc=', '2019-06-26 14:51:50.202933', 0, 'user1', '', '', 'user1@gmail.com', 0, 1, '2019-06-26 14:51:45.888293'),
(33, 'pbkdf2_sha256$100000$LcOnvMzLTdlP$tTEAt4q8If2hSUjSGaX2ftHIdBiRAMSotumMFXE6r78=', '2019-06-26 15:41:39.614272', 0, 'user2', '', '', 'user2@gmail.com', 0, 1, '2019-06-26 15:41:38.521240'),
(34, '!7gxR3QxobUBnu55mLMwoZcybN0mk0WKJ2Cm0Y5de', '2019-06-29 20:31:18.660488', 0, 'PrajwalBarapatreeacdf260bad54bf6', '', '', '', 0, 1, '2019-06-29 08:41:48.870208'),
(35, '!NtLe8lrYzFxYcuDjCgZm3cTY5WKbQKJLrVBkc7xb', '2019-06-29 20:34:05.380894', 0, 'prajwalbarapatre134746e95f0a8a4328', 'Prajwal', 'Barapatre', 'prajwalbarapatre13@gmail.com', 0, 1, '2019-06-29 08:46:11.284449'),
(36, '!OnleAvqqhZEe2eRw9DWyqPXZo2keULJKOF9xWLld', '2019-06-29 11:37:50.038267', 0, 'bmerge2100', '', '', '', 0, 1, '2019-06-29 11:37:49.440551'),
(37, '!W0HACmM4keRd7P8ENv6DsVGAvqKyHWS1HxlfZasG', '2019-06-29 12:18:07.686982', 0, 'arjunpandiant', '', '', '', 0, 1, '2019-06-29 11:41:43.005127'),
(38, '!SqGh9Zi4s801Qe6mSKa2jxi0uc6YMGU03skTISdJ', NULL, 0, 'admin7d7cc45bb6694054', '', '', 'admin@bverge.com', 0, 1, '2019-06-29 13:33:38.214873'),
(39, '!vq1Qbraa4F4doxnk3RZfHzrBQks5kZE4WuueN86x', '2019-06-29 13:38:11.168656', 0, 'adminb456b1ca2af24a2d', 'BVerge', 'Ventures', 'admin@bverge.com', 0, 1, '2019-06-29 13:36:34.295616'),
(40, '!QaCTxNbszuJJqfWFunvJDkurLoj300I4jpDLtUTK', '2019-06-29 14:11:51.326024', 0, 'prithviphysics', '', '', '', 0, 1, '2019-06-29 13:37:34.298896'),
(41, '!FsqsPjlkSBSFr2G5CwhYOVhTABfP3dznwcQFZ7lv', '2019-06-29 14:22:32.236149', 0, 'PrithvirajRadhakrishnan', 'Prithviraj', 'Radhakrishnan', '', 0, 1, '2019-06-29 14:06:18.948321'),
(42, '!uns9VVSP4cFj7SZW3DzwzeAxAlHJHZ4AhnzHGOsk', '2019-06-29 14:19:01.024865', 0, 'ArjunPandianT430793404af5411e', 'Arjun', 'Pandian T', '', 0, 1, '2019-06-29 14:18:48.351478');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `chat_chat`
--

CREATE TABLE `chat_chat` (
  `chat_id` int(11) NOT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat_chat`
--

INSERT INTO `chat_chat` (`chat_id`, `seller_id`) VALUES
(1, 22),
(3, 47);

-- --------------------------------------------------------

--
-- Table structure for table `chat_chat_messages`
--

CREATE TABLE `chat_chat_messages` (
  `id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `message_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat_chat_messages`
--

INSERT INTO `chat_chat_messages` (`id`, `chat_id`, `message_id`) VALUES
(1, 1, 13),
(2, 1, 14),
(4, 1, 18),
(6, 1, 20),
(7, 1, 21),
(8, 1, 22),
(10, 1, 24),
(11, 1, 25),
(14, 1, 28),
(16, 1, 30),
(17, 1, 31),
(19, 1, 33),
(20, 1, 34),
(22, 1, 36),
(23, 1, 37),
(24, 1, 38),
(25, 1, 39),
(26, 1, 40),
(27, 1, 41),
(29, 1, 43),
(31, 1, 45),
(32, 1, 46),
(33, 1, 47),
(34, 1, 48),
(35, 1, 49),
(36, 1, 50),
(37, 1, 51),
(40, 1, 54),
(41, 1, 55),
(42, 1, 56),
(43, 1, 57),
(44, 1, 58),
(45, 1, 59),
(46, 1, 60),
(47, 1, 61),
(48, 1, 62),
(49, 1, 63),
(50, 1, 64),
(51, 1, 65),
(52, 1, 66),
(53, 1, 67),
(54, 1, 68),
(55, 1, 69),
(56, 1, 70),
(57, 1, 71),
(58, 1, 72),
(59, 1, 73),
(60, 1, 74),
(61, 1, 75),
(62, 1, 76),
(63, 1, 77),
(70, 1, 84),
(71, 1, 85),
(72, 1, 86),
(73, 1, 87),
(74, 1, 88),
(75, 1, 89),
(76, 1, 90),
(77, 1, 91),
(79, 1, 93),
(80, 1, 94),
(81, 1, 95),
(82, 1, 96),
(83, 1, 97),
(84, 1, 98),
(85, 1, 99),
(87, 1, 101),
(88, 1, 102),
(89, 1, 103),
(90, 1, 104),
(91, 1, 105),
(92, 1, 106),
(94, 1, 108),
(95, 1, 109),
(97, 1, 111),
(98, 1, 112),
(102, 1, 116),
(104, 1, 118),
(105, 1, 119),
(107, 1, 121),
(108, 1, 122),
(111, 1, 125),
(113, 1, 127),
(114, 1, 128),
(115, 1, 129),
(117, 1, 131),
(118, 1, 132),
(119, 1, 133),
(120, 1, 134),
(122, 1, 136),
(123, 1, 137),
(124, 1, 138),
(125, 1, 139),
(126, 1, 140),
(127, 1, 141),
(130, 1, 144),
(131, 1, 145),
(133, 1, 148),
(134, 1, 149),
(137, 1, 152),
(140, 1, 155),
(142, 1, 157),
(143, 1, 158),
(144, 1, 159),
(145, 1, 160),
(154, 1, 169),
(157, 1, 172),
(158, 1, 173),
(132, 3, 147),
(135, 3, 150),
(136, 3, 151),
(138, 3, 153),
(139, 3, 154),
(141, 3, 156),
(146, 3, 161),
(150, 3, 165),
(151, 3, 166),
(152, 3, 167),
(153, 3, 168),
(155, 3, 170),
(156, 3, 171),
(159, 3, 174),
(160, 3, 175),
(161, 3, 176),
(162, 3, 177),
(163, 3, 178),
(164, 3, 179);

-- --------------------------------------------------------

--
-- Table structure for table `chat_chat_participants`
--

CREATE TABLE `chat_chat_participants` (
  `id` int(11) NOT NULL,
  `chat_id` int(11) NOT NULL,
  `contact_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat_chat_participants`
--

INSERT INTO `chat_chat_participants` (`id`, `chat_id`, `contact_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(4, 3, 1),
(5, 3, 2);

-- --------------------------------------------------------

--
-- Table structure for table `chat_contact`
--

CREATE TABLE `chat_contact` (
  `contact_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat_contact`
--

INSERT INTO `chat_contact` (`contact_id`, `user_id`) VALUES
(1, 5),
(2, 20);

-- --------------------------------------------------------

--
-- Table structure for table `chat_contact_friends`
--

CREATE TABLE `chat_contact_friends` (
  `id` int(11) NOT NULL,
  `from_contact_id` int(11) NOT NULL,
  `to_contact_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `chat_malbum`
--

CREATE TABLE `chat_malbum` (
  `malbum_id` int(11) NOT NULL,
  `file` varchar(100) DEFAULT NULL,
  `file_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat_malbum`
--

INSERT INTO `chat_malbum` (`malbum_id`, `file`, `file_name`) VALUES
(1, 'message/maxresdefault_Jv1QIPN.jpg', 'maxresdefault.jpg'),
(2, 'message/maxresdefault_ZJg5cUS.jpg', 'maxresdefault.jpg'),
(3, 'message/maxresdefault_pesQa9C.jpg', 'maxresdefault.jpg'),
(4, 'message/download.jpg', 'download.jpg'),
(5, 'message/maxresdefault_ROWYlj0.jpg', 'maxresdefault.jpg'),
(6, 'message/download_8.jpg', 'download (8).jpg'),
(7, 'message/download_5.jpg', 'download (5).jpg'),
(8, 'message/download_9.jpg', 'download (9).jpg'),
(9, 'message/download_5_Bgcrse4.jpg', 'download (5).jpg'),
(10, 'message/download_6.jpg', 'download (6).jpg'),
(11, 'message/images_13_ktPXTjc.jpg', 'message/images_13_ktPXTjc.jpg'),
(12, 'message/download_1.jpg', 'message/download_1.jpg'),
(13, 'message/images_4.jpg', 'message/images_4.jpg'),
(14, 'message/django-selectable.pdf', 'message/django-selectable.pdf'),
(15, 'message/ME604_4.pdf', 'message/ME604_4.pdf'),
(16, 'uploads/ME604_4.pdf', 'uploads/ME604_4.pdf'),
(17, 'message/ME604_4_RWHGXlt.pdf', 'message/ME604_4_RWHGXlt.pdf'),
(18, 'message/ME604_5.pdf', 'message/ME604_5.pdf'),
(19, 'message/spong.pdf', 'message/spong.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `chat_message`
--

CREATE TABLE `chat_message` (
  `message_id` int(11) NOT NULL,
  `content` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `file_exist` tinyint(1) NOT NULL,
  `malbum_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `chat_message`
--

INSERT INTO `chat_message` (`message_id`, `content`, `timestamp`, `contact_id`, `file_exist`, `malbum_id`) VALUES
(13, 'Hii', '2019-05-18 09:16:44.114779', 1, 0, NULL),
(14, 'Hii !\r\nHow are you ?', '2019-05-18 09:19:07.959621', 2, 0, NULL),
(15, 'Hii', '2019-05-18 09:19:54.493579', NULL, 0, NULL),
(16, 'I am fine.', '2019-05-20 11:24:07.804747', NULL, 0, NULL),
(17, 'I am fine.', '2019-05-20 11:26:40.629763', NULL, 0, NULL),
(18, 'Hii', '2019-05-20 16:32:09.561689', 1, 0, NULL),
(19, 'Hello there !!!', '2019-05-20 16:33:54.761261', 1, 0, NULL),
(20, 'I am fine.', '2019-05-20 17:11:28.444044', 1, 0, NULL),
(21, 'Hello minu', '2019-05-20 18:07:26.008401', 1, 0, NULL),
(22, 'Hii prajwal', '2019-05-20 18:27:57.733995', 2, 0, NULL),
(23, 'Minu is not here', '2019-05-20 18:28:15.123205', 1, 0, NULL),
(24, 'Hii there prajwal', '2019-05-20 18:37:09.645790', 2, 0, NULL),
(25, 'hello', '2019-05-20 18:38:18.259136', 2, 0, NULL),
(26, 'Well you shouldn\'t recieve message', '2019-05-20 19:32:58.638734', 1, 0, NULL),
(27, 'Hii', '2019-05-20 19:45:45.587875', 1, 0, NULL),
(28, 'Hii', '2019-05-20 19:47:04.995932', 2, 0, NULL),
(29, 'Hii', '2019-05-21 07:29:26.101199', 1, 0, NULL),
(30, 'Hello prajwal', '2019-05-21 07:29:49.298199', 2, 0, NULL),
(31, 'Hii there', '2019-05-21 07:31:19.377240', 1, 0, NULL),
(32, 'you should not recieve it', '2019-05-21 08:22:10.615675', 1, 0, NULL),
(33, 'well', '2019-05-21 08:26:17.104116', 1, 0, NULL),
(34, 'shbv', '2019-05-21 08:53:40.824507', 2, 0, NULL),
(35, 'Haa haa', '2019-05-21 08:53:49.619001', 1, 0, NULL),
(36, 'Hmm', '2019-05-21 08:54:02.919451', 1, 0, NULL),
(37, 'Hi ha ha ', '2019-05-21 08:59:58.498583', 2, 0, NULL),
(38, 'kk', '2019-05-21 09:00:05.186868', 1, 0, NULL),
(39, 'bfvkfb', '2019-05-21 09:00:10.526595', 2, 0, NULL),
(40, 'mns dsj kj ', '2019-05-21 09:00:15.471379', 1, 0, NULL),
(41, 'mnv s k j', '2019-05-21 09:00:19.610317', 2, 0, NULL),
(42, 'Hmm', '2019-05-21 09:00:26.794115', 1, 0, NULL),
(43, 'Hello minu once again', '2019-05-21 18:12:47.097212', 1, 0, NULL),
(44, 'Hello', '2019-05-21 18:13:34.545487', 1, 0, NULL),
(45, 'Hii there minu', '2019-05-23 08:36:56.914178', 1, 0, NULL),
(46, 'Hello', '2019-05-23 08:37:18.588657', 2, 0, NULL),
(47, 'apple', '2019-05-23 08:48:23.935430', 2, 0, NULL),
(48, 'green apple', '2019-05-23 08:48:59.841408', 1, 0, NULL),
(49, 'blue apple', '2019-05-23 08:49:10.056612', 2, 0, NULL),
(50, 'white apple', '2019-05-23 08:49:17.939527', 1, 0, NULL),
(51, 'yellow apple', '2019-05-23 08:49:25.962070', 2, 0, NULL),
(52, 'no apple', '2019-05-23 08:49:58.846412', 1, 0, NULL),
(53, 'white apple', '2019-05-23 08:50:05.451438', 1, 0, NULL),
(54, 'Hii good morning ', '2019-05-23 08:50:30.760549', 1, 0, NULL),
(55, 'hiisdjb sdkjbs dkvjsdvk nskdvbs v', '2019-05-23 08:50:42.722555', 1, 0, NULL),
(56, 'mangoes', '2019-05-23 08:54:18.643909', 1, 0, NULL),
(57, 'Hiiiiiiiiiiii', '2019-05-23 08:56:02.410861', 1, 0, NULL),
(58, 'Hmmm', '2019-05-23 09:34:17.899663', 2, 0, NULL),
(59, 'okk lets check now', '2019-05-23 09:34:57.818890', 1, 0, NULL),
(60, 'How about lil fast', '2019-05-23 09:35:11.955081', 2, 0, NULL),
(61, 'Well its working alright', '2019-05-23 09:35:31.133782', 1, 0, NULL),
(62, 'Both sending and recieving', '2019-05-23 09:35:41.911953', 2, 0, NULL),
(63, 'Well yess', '2019-05-23 09:35:53.186795', 1, 0, NULL),
(64, 'Lets type something arandom', '2019-05-23 09:36:05.490885', 1, 0, NULL),
(65, 'random*', '2019-05-23 09:36:11.051013', 1, 0, NULL),
(66, 'Okk', '2019-05-23 09:36:17.964521', 2, 0, NULL),
(67, 'daj hbf ajb ', '2019-05-23 09:36:23.628372', 1, 0, NULL),
(68, 'hjfab adbh ha f', '2019-05-23 09:36:30.070650', 2, 0, NULL),
(69, 'svh sdjf fdsdfsndf', '2019-05-23 09:36:40.154679', 1, 0, NULL),
(70, 'Working great even in random typing', '2019-05-23 09:37:00.274862', 2, 0, NULL),
(71, 'd', '2019-05-23 09:37:05.173759', 2, 0, NULL),
(72, 'df', '2019-05-23 09:37:08.424065', 2, 0, NULL),
(73, 'd', '2019-05-23 09:37:09.642805', 2, 0, NULL),
(74, 'Worked even when we submitted that fast', '2019-05-23 09:37:46.942039', 1, 0, NULL),
(75, 'I guess it is working now', '2019-05-23 09:37:57.210573', 1, 0, NULL),
(76, 'Ya seems so', '2019-05-23 09:38:05.711856', 2, 0, NULL),
(77, 'Let me type in different chat', '2019-05-23 09:38:20.204092', 1, 0, NULL),
(78, 'Hii, lets check here', '2019-05-23 09:38:39.114512', 1, 0, NULL),
(79, 'Hmm working great', '2019-05-23 09:38:49.370082', 1, 0, NULL),
(80, 'f', '2019-05-23 09:38:51.836485', 1, 0, NULL),
(81, 'f', '2019-05-23 09:38:53.299571', 1, 0, NULL),
(82, 'dfk', '2019-05-23 09:38:56.617696', 1, 0, NULL),
(83, 'knn', '2019-05-23 09:38:58.533573', 1, 0, NULL),
(84, 'Hey, its working great', '2019-05-23 09:39:17.717264', 1, 0, NULL),
(85, 'I don\'t why its not working now', '2019-05-23 09:40:01.274781', 1, 0, NULL),
(86, 'I am getting two times message being rendered', '2019-05-23 09:41:22.951823', 1, 0, NULL),
(87, 'Okk lets check now', '2019-05-23 09:55:47.952782', 1, 0, NULL),
(88, 'Thats one time', '2019-05-23 09:55:55.359970', 1, 0, NULL),
(89, 'Once again, we are restarting', '2019-05-23 09:56:41.449692', 1, 0, NULL),
(90, 'Now changing', '2019-05-23 09:56:49.703635', 1, 0, NULL),
(91, 'Okk', '2019-05-23 09:56:54.521747', 2, 0, NULL),
(92, 'Hii there', '2019-05-23 09:57:11.026110', 1, 0, NULL),
(93, 'This should be two times', '2019-05-23 09:57:30.669570', 1, 0, NULL),
(94, 'This is one time', '2019-05-23 10:16:05.521972', 1, 0, NULL),
(95, 'Yess this works fine', '2019-05-23 10:16:16.847679', 2, 0, NULL),
(96, 'Now lets check the other one', '2019-05-23 10:16:28.448649', 1, 0, NULL),
(97, 'okk go ahead', '2019-05-23 10:16:34.111503', 2, 0, NULL),
(98, 'you wont see this', '2019-05-23 10:17:06.573753', 2, 0, NULL),
(99, 'Ohh you wre suppose to message, sorry', '2019-05-23 10:17:45.922526', 2, 0, NULL),
(100, 'Okk', '2019-05-23 10:18:01.541749', 1, 0, NULL),
(101, 'Here it comes', '2019-05-23 10:18:17.362432', 1, 0, NULL),
(102, 'Helloooo', '2019-05-23 10:35:25.459881', 1, 0, NULL),
(103, 'Hmm', '2019-05-23 10:35:36.053545', 1, 0, NULL),
(104, 'Hii', '2019-05-23 10:50:19.770384', 1, 0, NULL),
(105, 'Hmm', '2019-05-23 10:50:42.543013', 2, 0, NULL),
(106, 'Made some changes i see', '2019-05-23 10:50:51.407303', 2, 0, NULL),
(107, 'Okkk', '2019-05-23 10:51:03.126468', 1, 0, NULL),
(108, 'Lets check now', '2019-05-23 10:51:16.084808', 1, 0, NULL),
(109, 'okk', '2019-05-23 10:54:59.078375', 2, 0, NULL),
(110, 'Kk', '2019-05-23 10:55:14.224861', 1, 0, NULL),
(111, 'dhfsh', '2019-05-23 10:55:25.767500', 2, 0, NULL),
(112, 'kk', '2019-05-23 10:55:39.419980', 1, 0, NULL),
(113, 'dfbsdf', '2019-05-23 10:58:25.296302', 1, 0, NULL),
(114, 'f', '2019-05-23 10:58:28.995411', 1, 0, NULL),
(115, 'f', '2019-05-23 10:58:39.066471', 1, 0, NULL),
(116, 'Hmm', '2019-05-23 11:02:05.805517', 1, 0, NULL),
(117, 'll', '2019-05-23 11:02:22.613560', 1, 0, NULL),
(118, 'Haa', '2019-05-23 11:02:36.817568', 1, 0, NULL),
(119, 'kk', '2019-05-23 11:06:20.514237', 1, 0, NULL),
(120, 'jk', '2019-05-23 11:06:34.192650', 1, 0, NULL),
(121, 'okk', '2019-05-23 11:06:40.302308', 1, 0, NULL),
(122, 'Hii hello', '2019-05-23 11:41:38.178901', 1, 0, NULL),
(123, 'sdfh', '2019-05-23 11:41:53.550857', 1, 0, NULL),
(124, 'sd', '2019-05-23 11:42:02.659066', 1, 0, NULL),
(125, 'Hell', '2019-05-23 11:42:19.854637', 1, 0, NULL),
(126, 'kk', '2019-05-23 11:44:04.465048', 1, 0, NULL),
(127, 'Hello', '2019-05-23 12:07:46.835310', 1, 0, NULL),
(128, 'kk', '2019-05-23 12:07:54.640433', 2, 0, NULL),
(129, 'Hmm', '2019-05-23 12:08:07.393833', 1, 0, NULL),
(130, 'kk', '2019-05-23 12:08:21.615793', 1, 0, NULL),
(131, 'Okk its just one time', '2019-05-23 12:08:46.483279', 1, 0, NULL),
(132, 'Yeah thats great', '2019-05-23 12:09:02.032688', 2, 0, NULL),
(133, 'khdsfh', '2019-05-23 12:09:09.691203', 2, 0, NULL),
(134, 'Hwel', '2019-05-23 12:31:49.909562', 1, 0, NULL),
(135, 'sdbfg sjbf skg k ', '2019-05-23 12:32:02.948687', 1, 0, NULL),
(136, 'lsdn', '2019-05-23 12:32:11.530732', 1, 0, NULL),
(137, 'db df wdf skd v', '2019-05-23 12:32:42.850959', 2, 0, NULL),
(138, 'Hw', '2019-05-24 10:54:13.067211', 1, 0, NULL),
(139, 'skdvs sjv sjn v', '2019-05-24 10:54:27.877072', 1, 0, NULL),
(140, 'Hello', '2019-05-24 11:05:25.414050', 2, 0, NULL),
(141, 'hi', '2019-05-24 14:48:43.363048', 2, 0, NULL),
(142, 'sdfj', '2019-05-24 14:52:06.347129', 1, 0, NULL),
(143, 'Hii there', '2019-05-29 14:48:12.287726', 1, 0, NULL),
(144, 'Hmm', '2019-05-29 14:48:35.778739', 1, 0, NULL),
(145, 'okk', '2019-05-29 14:48:53.231042', 1, 0, NULL),
(146, 'kk', '2019-05-29 14:49:00.392784', 2, 0, NULL),
(147, 'hi', '2019-05-31 15:38:04.301438', 1, 0, NULL),
(148, 'hello minu', '2019-06-25 10:26:10.322379', 1, 0, NULL),
(149, 'hmm', '2019-06-25 10:26:46.757812', 2, 0, NULL),
(150, 'sdvjbs d', '2019-06-25 10:27:11.060911', 1, 0, NULL),
(151, 'dmvb s', '2019-06-25 10:27:22.591775', 2, 0, NULL),
(152, 'kk', '2019-06-25 10:28:35.953640', 2, 0, NULL),
(153, 'jhv', '2019-06-25 10:29:11.112063', 1, 0, NULL),
(154, 'sdv', '2019-06-25 10:29:29.329189', 1, 0, NULL),
(155, 'akjdbv', '2019-06-25 13:47:33.714825', 1, 0, NULL),
(156, 'oho', '2019-06-25 18:51:49.018707', 1, 0, NULL),
(157, 'Hello there', '2019-06-25 20:44:32.120016', 2, 0, NULL),
(158, 'I got it', '2019-06-25 20:44:46.176565', 1, 0, NULL),
(159, 'Thats good', '2019-06-25 20:44:58.799577', 2, 0, NULL),
(160, 'sjdvb', '2019-06-25 20:59:42.817730', 2, 0, NULL),
(161, 'sd', '2019-06-26 07:51:21.562302', 1, 0, NULL),
(165, 'kk', '2019-06-26 10:48:51.585975', 2, 0, NULL),
(166, 'hmm', '2019-06-26 10:49:15.702297', 1, 0, NULL),
(167, 'download (6).jpg', '2019-06-26 11:10:07.626985', 1, 1, 10),
(168, 'message/images_13_ktPXTjc.jpg', '2019-06-26 11:22:10.056534', 2, 1, 11),
(169, 'message/download_1.jpg', '2019-06-26 11:27:39.159926', 2, 1, 12),
(170, 'sdkjbsd sn vsn dvsmndv snd v', '2019-06-26 16:21:11.120962', 2, 0, NULL),
(171, 'sjdvbs dvs dvsn dv', '2019-06-26 16:22:06.418737', 2, 0, NULL),
(172, 'dkhvbd d ', '2019-06-26 16:23:05.819457', 1, 0, NULL),
(173, 'message/images_4.jpg', '2019-06-26 16:26:41.188178', 2, 1, 13),
(174, 'message/django-selectable.pdf', '2019-06-27 04:20:15.105704', 2, 1, 14),
(175, 'message/ME604_4.pdf', '2019-06-27 06:45:51.570638', 2, 1, 15),
(176, 'uploads/ME604_4.pdf', '2019-06-27 07:12:31.992015', 1, 1, 16),
(177, 'message/ME604_4_RWHGXlt.pdf', '2019-06-27 07:15:07.565810', 1, 1, 17),
(178, 'message/ME604_5.pdf', '2019-06-27 07:15:08.166991', 1, 1, 18),
(179, 'message/spong.pdf', '2019-06-27 07:57:24.028847', 1, 1, 19);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(39, 'advisor', 'advisor'),
(38, 'advisor', 'businessadvisor'),
(40, 'advisor', 'startupadvisor'),
(20, 'album', 'album'),
(19, 'album', 'file'),
(26, 'album', 'kalbumforfile'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(30, 'chat', 'chat'),
(29, 'chat', 'contact'),
(44, 'chat', 'malbum'),
(28, 'chat', 'message'),
(5, 'contenttypes', 'contenttype'),
(36, 'investor', 'companyinvestor'),
(35, 'investor', 'individualinvestor'),
(37, 'investor', 'investor'),
(7, 'metadata', 'advisor'),
(8, 'metadata', 'businesssectors'),
(9, 'metadata', 'codes'),
(10, 'metadata', 'company'),
(11, 'metadata', 'countries'),
(18, 'metadata', 'years'),
(27, 'profiles', 'profile'),
(21, 'seller1', 'ablumfiles'),
(25, 'seller1', 'raiseloan'),
(31, 'seller1', 'revenuemodel'),
(33, 'seller1', 'sellapp'),
(23, 'seller1', 'sellasset'),
(22, 'seller1', 'sellbusiness'),
(24, 'seller1', 'sellequity'),
(17, 'seller1', 'seller1'),
(34, 'seller1', 'sellipcode'),
(32, 'seller1', 'sellstartup'),
(6, 'sessions', 'session'),
(12, 'social_django', 'association'),
(13, 'social_django', 'code'),
(14, 'social_django', 'nonce'),
(16, 'social_django', 'partial'),
(15, 'social_django', 'usersocialauth'),
(42, 'user_seller', 'advise'),
(43, 'user_seller', 'invest'),
(41, 'user_seller', 'sell');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-04-25 19:40:51.429920'),
(2, 'auth', '0001_initial', '2019-04-25 19:40:53.583218'),
(3, 'admin', '0001_initial', '2019-04-25 19:41:04.197972'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-04-25 19:41:07.671257'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-04-25 19:41:07.836289'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-04-25 19:41:09.284129'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-04-25 19:41:10.592376'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-04-25 19:41:11.702527'),
(9, 'auth', '0004_alter_user_username_opts', '2019-04-25 19:41:11.745090'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-04-25 19:41:13.024061'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-04-25 19:41:13.078028'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-04-25 19:41:13.141241'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-04-25 19:41:14.032398'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-04-25 19:41:15.016634'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-04-25 19:41:16.084622'),
(16, 'auth', '0011_update_proxy_permissions', '2019-04-25 19:41:16.160301'),
(17, 'metadata', '0001_initial', '2019-04-25 19:41:18.107889'),
(18, 'sessions', '0001_initial', '2019-04-25 19:41:18.536622'),
(19, 'default', '0001_initial', '2019-04-25 19:41:22.011676'),
(20, 'social_auth', '0001_initial', '2019-04-25 19:41:22.288538'),
(21, 'default', '0002_add_related_name', '2019-04-25 19:41:26.033642'),
(22, 'social_auth', '0002_add_related_name', '2019-04-25 19:41:26.115595'),
(23, 'default', '0003_alter_email_max_length', '2019-04-25 19:41:27.335895'),
(24, 'social_auth', '0003_alter_email_max_length', '2019-04-25 19:41:27.382870'),
(25, 'default', '0004_auto_20160423_0400', '2019-04-25 19:41:27.448830'),
(26, 'social_auth', '0004_auto_20160423_0400', '2019-04-25 19:41:27.511794'),
(27, 'social_auth', '0005_auto_20160727_2333', '2019-04-25 19:41:27.879586'),
(28, 'social_django', '0006_partial', '2019-04-25 19:41:28.493233'),
(29, 'social_django', '0007_code_timestamp', '2019-04-25 19:41:29.609592'),
(30, 'social_django', '0008_partial_timestamp', '2019-04-25 19:41:30.783922'),
(31, 'social_django', '0003_alter_email_max_length', '2019-04-25 19:41:31.325335'),
(32, 'social_django', '0001_initial', '2019-04-25 19:41:31.374348'),
(33, 'social_django', '0004_auto_20160423_0400', '2019-04-25 19:41:31.467461'),
(34, 'social_django', '0002_add_related_name', '2019-04-25 19:41:31.542136'),
(35, 'social_django', '0005_auto_20160727_2333', '2019-04-25 19:41:31.598390'),
(36, 'metadata', '0002_auto_20190426_0120', '2019-04-25 19:50:20.800568'),
(37, 'metadata', '0003_auto_20190426_0127', '2019-04-25 19:57:37.782302'),
(38, 'metadata', '0004_auto_20190426_0231', '2019-04-25 21:01:26.013903'),
(39, 'metadata', '0005_advisor_businesssectors_codes_company', '2019-04-25 21:14:40.092589'),
(40, 'metadata', '0006_years', '2019-04-28 13:39:32.232301'),
(42, 'album', '0001_initial', '2019-04-28 18:00:17.158933'),
(43, 'album', '0002_auto_20190429_0001', '2019-04-28 18:31:26.122655'),
(44, 'album', '0003_album_file', '2019-04-28 20:39:59.597752'),
(45, 'album', '0004_auto_20190429_0322', '2019-04-28 21:52:06.779541'),
(46, 'seller1', '0001_initial', '2019-04-29 16:14:09.835829'),
(47, 'seller1', '0002_auto_20190429_2146', '2019-04-29 16:16:05.995436'),
(48, 'seller1', '0003_auto_20190429_2156', '2019-04-29 16:26:05.895671'),
(49, 'seller1', '0004_auto_20190429_2159', '2019-04-29 16:29:39.809563'),
(50, 'album', '0002_auto_20190429_2218', '2019-04-29 16:48:26.435726'),
(51, 'album', '0003_auto_20190429_2220', '2019-04-29 16:51:09.958007'),
(52, 'seller1', '0005_auto_20190502_2024', '2019-05-02 14:54:20.821913'),
(53, 'seller1', '0006_auto_20190502_2202', '2019-05-02 16:32:34.327305'),
(54, 'seller1', '0007_auto_20190506_0209', '2019-05-05 21:35:07.625237'),
(55, 'seller1', '0008_auto_20190506_0307', '2019-05-05 21:39:36.149737'),
(56, 'seller1', '0009_auto_20190506_0310', '2019-05-05 21:44:55.371269'),
(57, 'seller1', '0010_sellbusiness', '2019-05-05 21:46:34.192984'),
(58, 'seller1', '0011_auto_20190506_0318', '2019-05-05 21:48:12.198667'),
(59, 'seller1', '0012_auto_20190506_0320', '2019-05-05 21:51:19.658231'),
(60, 'seller1', '0013_auto_20190506_0322', '2019-05-05 21:52:41.069974'),
(61, 'seller1', '0014_auto_20190506_0323', '2019-05-05 21:54:07.254387'),
(62, 'seller1', '0015_auto_20190506_0324', '2019-05-05 21:54:40.450749'),
(63, 'seller1', '0016_auto_20190506_0401', '2019-05-05 22:31:24.398510'),
(64, 'seller1', '0017_auto_20190506_0411', '2019-05-05 22:41:14.572835'),
(65, 'seller1', '0018_auto_20190506_1107', '2019-05-06 05:37:48.341888'),
(66, 'seller1', '0019_auto_20190506_1113', '2019-05-06 05:43:38.810422'),
(67, 'seller1', '0020_auto_20190507_0050', '2019-05-06 19:20:50.318124'),
(68, 'seller1', '0021_auto_20190507_0100', '2019-05-06 19:31:00.782138'),
(69, 'seller1', '0022_auto_20190507_0122', '2019-05-06 19:52:31.795569'),
(70, 'seller1', '0023_auto_20190507_0136', '2019-05-06 20:07:08.082324'),
(71, 'seller1', '0024_auto_20190507_1411', '2019-05-07 08:41:18.497832'),
(72, 'seller1', '0025_auto_20190508_1042', '2019-05-08 05:12:44.587629'),
(73, 'album', '0004_file_seller', '2019-05-08 05:12:50.142637'),
(74, 'seller1', '0026_auto_20190508_1112', '2019-05-08 05:42:45.369675'),
(75, 'seller1', '0027_auto_20190508_1115', '2019-05-08 05:46:04.058277'),
(76, 'seller1', '0028_auto_20190508_1119', '2019-05-08 05:52:11.453641'),
(77, 'seller1', '0029_auto_20190508_1121', '2019-05-08 05:52:19.320943'),
(78, 'seller1', '0030_auto_20190508_1147', '2019-05-08 06:18:30.460072'),
(79, 'seller1', '0031_auto_20190508_1148', '2019-05-08 06:18:38.755927'),
(80, 'seller1', '0032_auto_20190508_1148', '2019-05-08 06:25:55.893003'),
(81, 'seller1', '0033_auto_20190508_1149', '2019-05-08 06:26:04.098333'),
(82, 'seller1', '0034_auto_20190508_1155', '2019-05-08 06:26:10.670664'),
(83, 'album', '0002_kalbumforfile', '2019-05-08 06:26:20.882043'),
(84, 'profiles', '0001_initial', '2019-05-08 19:08:42.137960'),
(85, 'seller1', '0035_auto_20190509_0037', '2019-05-08 19:08:49.112343'),
(86, 'seller1', '0036_auto_20190509_0038', '2019-05-08 19:08:53.951387'),
(87, 'profiles', '0002_auto_20190510_0111', '2019-05-09 19:41:55.350590'),
(88, 'seller1', '0037_auto_20190510_0111', '2019-05-09 19:42:00.456000'),
(89, 'seller1', '0038_auto_20190513_0135', '2019-05-12 20:05:34.931112'),
(90, 'seller1', '0039_auto_20190513_0206', '2019-05-12 20:36:39.027028'),
(91, 'chat', '0001_initial', '2019-05-15 13:17:35.382888'),
(92, 'seller1', '0040_auto_20190515_1847', '2019-05-15 13:17:38.431849'),
(93, 'seller1', '0041_auto_20190516_1802', '2019-05-16 12:34:21.502361'),
(94, 'seller1', '0042_auto_20190516_1803', '2019-05-16 12:34:27.676130'),
(95, 'seller1', '0043_auto_20190516_1804', '2019-05-16 12:34:36.239793'),
(96, 'seller1', '0038_auto_20190516_1817', '2019-05-16 12:48:52.901434'),
(97, 'seller1', '0039_auto_20190516_1818', '2019-05-16 12:48:59.257035'),
(98, 'seller1', '0040_auto_20190516_1818', '2019-05-16 12:49:04.290028'),
(99, 'seller1', '0041_auto_20190516_1826', '2019-05-16 12:56:50.030379'),
(100, 'chat', '0002_manual_table', '2019-05-16 13:13:10.313173'),
(101, 'seller1', '0042_auto_20190516_1827', '2019-05-16 13:13:15.770727'),
(102, 'seller1', '0043_auto_20190516_1831', '2019-05-16 13:13:23.675545'),
(103, 'seller1', '0044_auto_20190516_1843', '2019-05-16 13:13:31.111212'),
(104, 'chat', '0003_auto_20190518_1224', '2019-05-18 06:55:04.060790'),
(105, 'seller1', '0045_auto_20190518_1224', '2019-05-18 06:55:11.864687'),
(106, 'chat', '0004_auto_20190521_0120', '2019-05-20 19:51:12.469085'),
(107, 'seller1', '0046_auto_20190521_0120', '2019-05-20 19:51:17.851697'),
(108, 'chat', '0005_auto_20190521_0148', '2019-05-20 20:18:27.211724'),
(109, 'seller1', '0047_auto_20190521_0148', '2019-05-20 20:18:34.208202'),
(110, 'seller1', '0048_auto_20190524_0314', '2019-05-23 21:45:09.595675'),
(111, 'chat', '0006_chat_seller', '2019-05-23 21:45:11.245470'),
(112, 'chat', '0007_auto_20190524_1538', '2019-05-24 10:09:19.377412'),
(113, 'profiles', '0003_profile_status', '2019-05-24 10:09:19.816486'),
(114, 'seller1', '0049_auto_20190524_1538', '2019-05-24 10:09:22.874582'),
(115, 'chat', '0008_auto_20190525_0230', '2019-05-24 21:00:44.374798'),
(116, 'seller1', '0050_auto_20190525_0230', '2019-05-24 21:00:54.273705'),
(117, 'album', '0003_auto_20190525_1717', '2019-05-25 11:47:43.319164'),
(118, 'chat', '0009_auto_20190525_1717', '2019-05-25 11:47:44.868885'),
(119, 'seller1', '0051_auto_20190525_1717', '2019-05-25 11:47:52.030169'),
(120, 'chat', '0010_auto_20190526_1700', '2019-05-26 11:30:24.649089'),
(121, 'seller1', '0052_auto_20190526_1700', '2019-05-26 11:30:36.115681'),
(122, 'chat', '0011_auto_20190526_1738', '2019-05-26 12:08:42.249059'),
(123, 'seller1', '0053_auto_20190526_1738', '2019-05-26 12:08:53.176486'),
(124, 'chat', '0012_auto_20190526_1747', '2019-05-26 12:17:32.466177'),
(125, 'seller1', '0054_auto_20190526_1747', '2019-05-26 12:17:42.575980'),
(126, 'chat', '0013_auto_20190526_2048', '2019-05-26 15:18:17.686731'),
(127, 'seller1', '0055_auto_20190526_2048', '2019-05-26 15:18:26.904952'),
(128, 'chat', '0014_auto_20190526_2054', '2019-05-26 15:24:38.825747'),
(129, 'seller1', '0056_auto_20190526_2054', '2019-05-26 15:24:50.219766'),
(130, 'chat', '0015_auto_20190526_2102', '2019-05-26 15:32:28.899900'),
(131, 'seller1', '0057_auto_20190526_2102', '2019-05-26 15:32:38.996236'),
(132, 'chat', '0016_auto_20190527_0001', '2019-05-26 18:31:22.827200'),
(133, 'seller1', '0058_auto_20190527_0001', '2019-05-26 18:31:33.918118'),
(134, 'chat', '0017_auto_20190527_0236', '2019-05-26 21:06:45.759421'),
(135, 'investor', '0001_initial', '2019-05-26 21:06:49.984635'),
(136, 'seller1', '0059_auto_20190527_0236', '2019-05-26 21:07:00.879096'),
(137, 'chat', '0018_auto_20190527_0244', '2019-05-26 21:14:28.306152'),
(138, 'investor', '0002_auto_20190527_0244', '2019-05-26 21:14:28.685789'),
(139, 'seller1', '0060_auto_20190527_0244', '2019-05-26 21:14:40.628668'),
(140, 'chat', '0019_auto_20190527_1229', '2019-05-27 06:59:36.442939'),
(141, 'investor', '0003_auto_20190527_1229', '2019-05-27 06:59:36.600209'),
(142, 'seller1', '0061_auto_20190527_1229', '2019-05-27 06:59:48.148709'),
(143, 'advisor', '0001_initial', '2019-05-27 11:05:44.272374'),
(144, 'chat', '0020_auto_20190527_1635', '2019-05-27 11:05:45.674384'),
(145, 'seller1', '0062_auto_20190527_1635', '2019-05-27 11:05:58.032100'),
(146, 'advisor', '0002_startupadvisor', '2019-05-27 12:01:07.736423'),
(147, 'chat', '0021_auto_20190527_1730', '2019-05-27 12:01:09.360373'),
(148, 'seller1', '0063_auto_20190527_1730', '2019-05-27 12:01:20.702022'),
(149, 'chat', '0022_auto_20190527_1757', '2019-05-27 12:27:26.600878'),
(150, 'seller1', '0064_auto_20190527_1757', '2019-05-27 12:27:39.147952'),
(151, 'chat', '0023_auto_20190529_0318', '2019-05-28 21:49:17.547486'),
(152, 'seller1', '0065_auto_20190529_0318', '2019-05-28 21:49:25.190963'),
(153, 'user_seller', '0001_initial', '2019-05-28 21:49:44.092438'),
(154, 'profiles', '0004_auto_20190529_0318', '2019-05-28 21:49:55.416999'),
(155, 'profiles', '0005_profile_user_sell', '2019-05-28 21:50:01.193337'),
(156, 'chat', '0024_auto_20190529_1800', '2019-05-29 12:31:14.240275'),
(157, 'profiles', '0006_auto_20190529_1800', '2019-05-29 12:31:19.523788'),
(158, 'seller1', '0066_auto_20190529_1800', '2019-05-29 12:31:31.905890'),
(159, 'user_seller', '0002_auto_20190529_1800', '2019-05-29 12:31:34.271131'),
(160, 'chat', '0025_auto_20190602_1818', '2019-06-02 12:49:08.331249'),
(161, 'seller1', '0067_auto_20190602_1818', '2019-06-02 12:49:18.446720'),
(162, 'user_seller', '0003_auto_20190602_1818', '2019-06-02 12:49:57.869542'),
(163, 'profiles', '0007_auto_20190602_1818', '2019-06-02 12:50:11.046418'),
(164, 'profiles', '0008_auto_20190602_1818', '2019-06-02 12:50:24.612396'),
(165, 'advisor', '0003_businessadvisor_about_seller', '2019-06-17 15:49:44.153340'),
(166, 'chat', '0026_auto_20190617_2119', '2019-06-17 15:49:45.681767'),
(167, 'profiles', '0009_auto_20190617_2119', '2019-06-17 15:49:53.562070'),
(168, 'seller1', '0068_auto_20190617_2119', '2019-06-17 15:50:14.494924'),
(169, 'user_seller', '0004_auto_20190617_2119', '2019-06-17 15:50:39.397797'),
(170, 'advisor', '0004_startupadvisor_about_seller', '2019-06-18 19:44:01.635196'),
(171, 'chat', '0027_auto_20190619_0113', '2019-06-18 19:44:02.639994'),
(172, 'investor', '0004_auto_20190619_0113', '2019-06-18 19:44:19.669355'),
(173, 'profiles', '0010_auto_20190619_0113', '2019-06-18 19:44:28.764334'),
(174, 'seller1', '0069_auto_20190619_0113', '2019-06-18 19:44:49.525395'),
(175, 'user_seller', '0005_auto_20190619_0113', '2019-06-18 19:45:07.681919'),
(176, 'advisor', '0005_advisor_title', '2019-06-23 13:56:01.947896'),
(177, 'chat', '0028_auto_20190623_1925', '2019-06-23 13:56:03.993663'),
(178, 'investor', '0005_auto_20190623_1925', '2019-06-23 13:56:05.843391'),
(179, 'profiles', '0011_auto_20190623_1925', '2019-06-23 13:56:12.234939'),
(180, 'seller1', '0070_auto_20190623_1925', '2019-06-23 13:56:25.500098'),
(181, 'user_seller', '0006_auto_20190623_1925', '2019-06-23 13:56:39.273655'),
(182, 'advisor', '0006_auto_20190623_1949', '2019-06-23 14:19:07.629922'),
(183, 'chat', '0029_auto_20190623_1949', '2019-06-23 14:19:09.149555'),
(184, 'investor', '0006_auto_20190623_1949', '2019-06-23 14:19:09.222901'),
(185, 'profiles', '0012_auto_20190623_1949', '2019-06-23 14:19:14.906095'),
(186, 'seller1', '0071_auto_20190623_1949', '2019-06-23 14:19:27.996461'),
(187, 'user_seller', '0007_auto_20190623_1949', '2019-06-23 14:19:41.190326'),
(188, 'chat', '0030_auto_20190623_2005', '2019-06-23 14:36:02.113714'),
(189, 'investor', '0007_auto_20190623_2005', '2019-06-23 14:36:02.623799'),
(190, 'profiles', '0013_auto_20190623_2005', '2019-06-23 14:36:07.645943'),
(191, 'seller1', '0072_auto_20190623_2005', '2019-06-23 14:36:19.326320'),
(192, 'user_seller', '0008_auto_20190623_2005', '2019-06-23 14:36:31.744295'),
(193, 'chat', '0031_auto_20190626_0130', '2019-06-25 20:01:04.304067'),
(194, 'profiles', '0014_auto_20190626_0130', '2019-06-25 20:01:11.667241'),
(195, 'seller1', '0073_auto_20190626_0130', '2019-06-25 20:01:22.864989'),
(196, 'user_seller', '0009_auto_20190626_0130', '2019-06-25 20:01:34.536572'),
(197, 'chat', '0032_auto_20190626_0924', '2019-06-26 03:54:50.830959'),
(198, 'profiles', '0015_auto_20190626_0924', '2019-06-26 03:54:55.881986'),
(199, 'seller1', '0074_auto_20190626_0924', '2019-06-26 03:55:08.812658'),
(200, 'user_seller', '0010_auto_20190626_0924', '2019-06-26 03:55:22.892917'),
(201, 'chat', '0033_auto_20190626_1614', '2019-06-26 10:44:53.282109'),
(202, 'profiles', '0016_auto_20190626_1614', '2019-06-26 10:44:59.564996'),
(203, 'seller1', '0075_auto_20190626_1614', '2019-06-26 10:45:11.855014'),
(204, 'user_seller', '0011_auto_20190626_1614', '2019-06-26 10:45:24.675222'),
(205, 'chat', '0034_auto_20190627_1231', '2019-06-27 07:01:34.359528'),
(206, 'profiles', '0017_auto_20190627_1231', '2019-06-27 07:01:42.241023'),
(207, 'seller1', '0076_auto_20190627_1231', '2019-06-27 07:01:56.123595'),
(208, 'user_seller', '0012_auto_20190627_1231', '2019-06-27 07:02:11.710830'),
(209, 'chat', '0035_auto_20190627_1235', '2019-06-27 07:05:21.466140'),
(210, 'profiles', '0018_auto_20190627_1235', '2019-06-27 07:05:28.280689'),
(211, 'seller1', '0077_auto_20190627_1235', '2019-06-27 07:05:42.157330'),
(212, 'user_seller', '0013_auto_20190627_1235', '2019-06-27 07:05:57.975675'),
(213, 'chat', '0036_auto_20190627_1243', '2019-06-27 07:13:46.275832'),
(214, 'profiles', '0019_auto_20190627_1243', '2019-06-27 07:13:53.269695'),
(215, 'seller1', '0078_auto_20190627_1243', '2019-06-27 07:14:04.268779'),
(216, 'user_seller', '0014_auto_20190627_1243', '2019-06-27 07:14:21.617574'),
(217, 'chat', '0037_auto_20190627_1257', '2019-06-27 07:28:02.686668'),
(218, 'profiles', '0020_auto_20190627_1257', '2019-06-27 07:28:08.004376'),
(219, 'seller1', '0079_auto_20190627_1257', '2019-06-27 07:28:19.384970'),
(220, 'user_seller', '0015_auto_20190627_1257', '2019-06-27 07:28:31.762308'),
(221, 'chat', '0038_auto_20190627_1317', '2019-06-27 07:47:40.352252'),
(222, 'profiles', '0021_auto_20190627_1317', '2019-06-27 07:47:45.955962'),
(223, 'seller1', '0080_auto_20190627_1317', '2019-06-27 07:47:58.058847'),
(224, 'user_seller', '0016_auto_20190627_1317', '2019-06-27 07:48:10.600097'),
(225, 'chat', '0039_auto_20190629_1643', '2019-06-29 11:14:16.545492'),
(226, 'profiles', '0022_auto_20190629_1643', '2019-06-29 11:14:22.007250'),
(227, 'seller1', '0081_auto_20190629_1643', '2019-06-29 11:14:34.908888'),
(228, 'user_seller', '0017_auto_20190629_1643', '2019-06-29 11:14:51.458915'),
(229, 'chat', '0040_auto_20190629_1720', '2019-06-29 11:50:17.266241'),
(230, 'profiles', '0023_auto_20190629_1720', '2019-06-29 11:50:26.977710'),
(231, 'seller1', '0082_auto_20190629_1720', '2019-06-29 11:50:39.648734'),
(232, 'user_seller', '0018_auto_20190629_1720', '2019-06-29 11:50:52.388393'),
(233, 'chat', '0041_auto_20190629_1742', '2019-06-29 12:12:25.963334'),
(234, 'profiles', '0024_auto_20190629_1742', '2019-06-29 12:12:33.911685'),
(235, 'seller1', '0083_auto_20190629_1742', '2019-06-29 12:12:47.975680'),
(236, 'user_seller', '0019_auto_20190629_1742', '2019-06-29 12:13:01.822830'),
(237, 'chat', '0042_auto_20190629_1934', '2019-06-29 14:04:45.630769'),
(238, 'profiles', '0025_auto_20190629_1934', '2019-06-29 14:04:51.114015'),
(239, 'seller1', '0084_auto_20190629_1934', '2019-06-29 14:05:04.612454'),
(240, 'user_seller', '0020_auto_20190629_1934', '2019-06-29 14:05:20.063726');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0cd3ti5qzibpu8el75alwatveccjk43l', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-04 17:29:16.096399'),
('24ck81q4g7kzahcwochxj7ys99v92gpr', 'NDE1ZWEzNjk0ZWRlODk1YzUwYTZlNWU0YzA3NjkwZGUzMjk4Yjk3Nzp7ImdpdGh1Yl9zdGF0ZSI6InJiVk92Ym1rbGtXdm9aY3dsdG1PRHJpZDFBV2VtdWlvIiwiX2F1dGhfdXNlcl9pZCI6IjM3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsX2NvcmUuYmFja2VuZHMuZ2l0aHViLkdpdGh1Yk9BdXRoMiIsIl9hdXRoX3VzZXJfaGFzaCI6IjhlZWQxYWIyNjMzYzBiOTk3NDAyNGI3NjhiZWEwMTQ0ZDc2N2Y1NjAiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJnaXRodWIifQ==', '2019-07-13 12:18:06.243227'),
('2n5xfw7n3sxurfynstxpvyxos423o4lw', 'NzU2NzcxYzQxMGNkYTk3MmY3MTEzZWUyNjc5ZjVkNjkwYWQ0ZjBiYjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkN2FlMjc4OWI4NTQ4NjMxMjA1MTJlNjQ3YjAzNTEzZGQzY2RiNjExIn0=', '2019-05-31 20:56:08.527795'),
('3lp31yxhdua3hwmjp57rxy7rnzr1lmf3', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-14 15:37:13.975011'),
('4w3vgm3m9b4csblb6rm4pkny5u5l09k2', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-07-04 15:03:15.983364'),
('6vpn3o51xj1wclotp0qprkf846pqz4fe', 'NDE1ZWEzNjk0ZWRlODk1YzUwYTZlNWU0YzA3NjkwZGUzMjk4Yjk3Nzp7ImdpdGh1Yl9zdGF0ZSI6InJiVk92Ym1rbGtXdm9aY3dsdG1PRHJpZDFBV2VtdWlvIiwiX2F1dGhfdXNlcl9pZCI6IjM3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsX2NvcmUuYmFja2VuZHMuZ2l0aHViLkdpdGh1Yk9BdXRoMiIsIl9hdXRoX3VzZXJfaGFzaCI6IjhlZWQxYWIyNjMzYzBiOTk3NDAyNGI3NjhiZWEwMTQ0ZDc2N2Y1NjAiLCJzb2NpYWxfYXV0aF9sYXN0X2xvZ2luX2JhY2tlbmQiOiJnaXRodWIifQ==', '2019-07-13 12:18:07.018290'),
('7lsip254zqowuu3i1ksjcu7grct3ovtt', 'Y2IxNWNhZmQ4MDk2ODBjNjAwMDRkN2I2NTUwY2ViODRkZGViZGVkOTp7ImdpdGh1Yl9zdGF0ZSI6Ijgzdk9YbG5hTUtTNXg4QllzMnJLZm14U2ZFSUpGRFF1IiwiZ29vZ2xlLW9hdXRoMl9zdGF0ZSI6IkZMWkJYYVg4OUp5VWNlbW9YYW1WSDNoYmFNU2FsVVo3In0=', '2019-07-13 10:47:30.145928'),
('7qixv757l6jvfqhahudiyg5991skj8wb', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-29 06:09:47.378720'),
('7wz0h9tj8991rc1bkz56ha1ribyyh78v', 'NzU2NzcxYzQxMGNkYTk3MmY3MTEzZWUyNjc5ZjVkNjkwYWQ0ZjBiYjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkN2FlMjc4OWI4NTQ4NjMxMjA1MTJlNjQ3YjAzNTEzZGQzY2RiNjExIn0=', '2019-07-11 06:46:47.640082'),
('a7vhkrmwrsfje4g9ka28olpst7sysioe', 'MjI2YTIxNzZkNGMwZDhiMzc5N2FmOWQwMmJlYWJjNGU3ZDQzYWZhODp7ImxpbmtlZGluLW9hdXRoMl9zdGF0ZSI6ImlzVzBiYmhvSFJjc0NwTXl2MmM5SDhVcXNSbHBiODJHIiwiX2F1dGhfdXNlcl9pZCI6IjQyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsX2NvcmUuYmFja2VuZHMubGlua2VkaW4uTGlua2VkaW5PQXV0aDIiLCJfYXV0aF91c2VyX2hhc2giOiI3ZGQyMGZiNGQxOGE2NDUwOGUzZmVjN2E5OWJkYmZiOWE4MWMwYzM1Iiwic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoibGlua2VkaW4tb2F1dGgyIn0=', '2019-07-13 14:18:51.387892'),
('abpjiz67dt6yabg2harzwkewa23lw86o', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-07 14:47:50.523824'),
('ac04xqgks92kw3ndo6vl4gp801wff3cx', 'Njc2YTgyYjhiZTMyODY0NzJmZGIyZGE3NDc5ZjlhMWM5ZjE4ZjMzZjp7Il9hdXRoX3VzZXJfaWQiOiIzMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmNlODYyNzQ3MjJjYzYyYTEwMGY3MDI2NmFhOWRhYWJjN2YyYTliMiJ9', '2019-07-05 13:18:49.610486'),
('acf3ko2yb8peumkpi3h3fu4sh3rj25lx', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-07-01 15:30:29.385249'),
('c1vnmznjxkrs5fzk0x3dvn6a2s2zvxnh', 'NzU2NzcxYzQxMGNkYTk3MmY3MTEzZWUyNjc5ZjVkNjkwYWQ0ZjBiYjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkN2FlMjc4OWI4NTQ4NjMxMjA1MTJlNjQ3YjAzNTEzZGQzY2RiNjExIn0=', '2019-07-09 13:38:09.583614'),
('crjytei0yqgkgsvrc6zroi1mbmqoaq8i', 'ODYxM2FkZGJmZWRhMzhiMGE1MGIyZWFjYWE1YTA0OWQyZDMzZGJhNDp7Imdvb2dsZS1vYXV0aDJfc3RhdGUiOiJwdnQxQWlrbUZ3bkpZNEJFeE95bjFCRmNKNnQ4MFRIQSIsIl9hdXRoX3VzZXJfaWQiOiIzNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InNvY2lhbF9jb3JlLmJhY2tlbmRzLmdvb2dsZS5Hb29nbGVPQXV0aDIiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDRjZjExMGYwZGEzMzg3MjRkN2FhMTRjYTZmNjVhNWRlZDgyNzljIiwic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoiZ29vZ2xlLW9hdXRoMiJ9', '2019-07-13 20:34:05.480627'),
('fudrr307gu5k4nc1amjnxnh333ijt2wt', 'Njc2YTgyYjhiZTMyODY0NzJmZGIyZGE3NDc5ZjlhMWM5ZjE4ZjMzZjp7Il9hdXRoX3VzZXJfaWQiOiIzMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiMmNlODYyNzQ3MjJjYzYyYTEwMGY3MDI2NmFhOWRhYWJjN2YyYTliMiJ9', '2019-07-06 08:02:04.649864'),
('h7uogfccnrc434mj3ygfkma9rh2z4t0i', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-07 10:45:37.871428'),
('htp1d93kr1ppkt0yhfbk9gm2jqqno97x', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-06 11:36:38.450243'),
('jy94squ2w0cgl5gat103zs03yrrlzx1d', 'ZjQwOGM3YTFlN2I3ZTg1YjUzM2VkZDU3ZWU3Y2VmMzcxODhlOWE4ODp7Imdvb2dsZS1vYXV0aDJfc3RhdGUiOiJrNDVNd3RYNnFSRERwaFIxM0hNeFlnWVZHTE1TY0RvcCIsIl9hdXRoX3VzZXJfaWQiOiIzNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6InNvY2lhbF9jb3JlLmJhY2tlbmRzLmdvb2dsZS5Hb29nbGVPQXV0aDIiLCJfYXV0aF91c2VyX2hhc2giOiI5ZDRjZjExMGYwZGEzMzg3MjRkN2FhMTRjYTZmNjVhNWRlZDgyNzljIiwic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoiZ29vZ2xlLW9hdXRoMiJ9', '2019-07-13 08:46:12.909769'),
('ktvim1r1njyl2ixepkdxchvhq3wo0w2p', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-06 19:43:52.123431'),
('ofzlu47syqnjyyskfogjnn1nhov4yb9p', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-07 19:57:26.940593'),
('q639ac99r0oqlknjmfo4ptwal55ougt4', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-06 11:40:54.124555'),
('r2ljmdse81oyzwf1r8tq4gre3flbshij', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-05-26 09:26:01.727243'),
('rlp3riugbkyeuqsk280v4dey95mrau9k', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-12 14:19:06.557247'),
('t22fshehlsi9qsd9z1me1rzubb0w5hb5', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-05-31 21:31:09.161603'),
('u5ice7b4vwr7l6cmyej6xz2levsngvh1', 'NzU2NzcxYzQxMGNkYTk3MmY3MTEzZWUyNjc5ZjVkNjkwYWQ0ZjBiYjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkN2FlMjc4OWI4NTQ4NjMxMjA1MTJlNjQ3YjAzNTEzZGQzY2RiNjExIn0=', '2019-05-29 13:33:59.198865'),
('v2011j6xmnn7clso8ve3hrc9ocvsdq99', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-06 08:27:16.141554'),
('v6z2ogaxr69bccldgwfmbpnybqt4ftgl', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-12 15:31:25.289973'),
('w9e0npakjduo0apo4eazim3gacvd6i8v', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-10 09:46:41.813490'),
('y20lw31zqn86bx42a1ixv6717bwithql', 'OWUzNzQ2YWIzYmVjNjE2MDhiNjdlOWEzZjExYzBiOTU1Yjc3MzAxMjp7ImxpbmtlZGluLW9hdXRoMl9zdGF0ZSI6Im1DZEQ2cW9UZ1k0OW4zTTZrcmFHWjBNaFZ1V3A2NE9DIiwiX2F1dGhfdXNlcl9pZCI6IjQyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoic29jaWFsX2NvcmUuYmFja2VuZHMubGlua2VkaW4uTGlua2VkaW5PQXV0aDIiLCJfYXV0aF91c2VyX2hhc2giOiI3ZGQyMGZiNGQxOGE2NDUwOGUzZmVjN2E5OWJkYmZiOWE4MWMwYzM1Iiwic29jaWFsX2F1dGhfbGFzdF9sb2dpbl9iYWNrZW5kIjoibGlua2VkaW4tb2F1dGgyIn0=', '2019-07-13 14:19:01.168480'),
('yv8f1tk33ahfyhcrd9n3ca33js18um2g', 'NjQ3NGI3MGZmNjNmMWUxMzUzMjdjOWVjYTFiOGUyZjkzOTE5ZTBiNzp7Il9hdXRoX3VzZXJfaWQiOiIyMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNGZjNGFjNGUzNDVmNWE1YzU1ZDUzM2NiMmU2ZmZmYTMxMDFmN2Y2ZiJ9', '2019-06-03 18:04:57.415448');

-- --------------------------------------------------------

--
-- Table structure for table `investor_companyinvestor`
--

CREATE TABLE `investor_companyinvestor` (
  `company_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `investment_bracket` varchar(255) NOT NULL,
  `category1` varchar(255) NOT NULL,
  `category2` varchar(255) NOT NULL,
  `category3` varchar(255) NOT NULL,
  `sub_category1` varchar(255) NOT NULL,
  `sub_category2` varchar(255) NOT NULL,
  `sub_category3` varchar(255) NOT NULL,
  `capital_type` varchar(255) NOT NULL,
  `about` longtext NOT NULL,
  `looking_for` longtext NOT NULL,
  `website` varchar(500) DEFAULT NULL,
  `investor_id` int(11) DEFAULT NULL,
  `about_seller` longtext NOT NULL,
  `address_line1` varchar(256) NOT NULL,
  `address_line2` varchar(256) NOT NULL,
  `address_line3` varchar(256) NOT NULL,
  `city1` varchar(255) NOT NULL,
  `city2` varchar(255) NOT NULL,
  `city3` varchar(255) NOT NULL,
  `country1` varchar(255) NOT NULL,
  `country2` varchar(255) NOT NULL,
  `country3` varchar(255) NOT NULL,
  `state1` varchar(255) NOT NULL,
  `state2` varchar(255) NOT NULL,
  `state3` varchar(255) NOT NULL,
  `institution_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `investor_companyinvestor`
--

INSERT INTO `investor_companyinvestor` (`company_id`, `type`, `investment_bracket`, `category1`, `category2`, `category3`, `sub_category1`, `sub_category2`, `sub_category3`, `capital_type`, `about`, `looking_for`, `website`, `investor_id`, `about_seller`, `address_line1`, `address_line2`, `address_line3`, `city1`, `city2`, `city3`, `country1`, `country2`, `country3`, `state1`, `state2`, `state3`, `institution_name`) VALUES
(1, 'Company', '2 to 4 Crores', 'Education', 'Aerospace', 'Emerging Technology', '', '', '', 'Select type 2', 'rrsc v j j j', 'hagdv aca dcha dc', NULL, 3, 'Investment_Bank', '', '', '', '', '', '', '', '', '', '', '', '', 'soething'),
(2, 'Company', '1 to 2 Crores', 'Manufacturing', 'Retail', 'Utility', '', '', '', 'Select type 2', 'scbs dcnsb csnbd s dn dc', 'sm s dm sdm sdn sdn sdc sd', NULL, 9, 'Individual_Investor', 'Mumbai, Maharashtra, India', 'Chernobyl, Kyiv Oblast, Ukraine', 'Knoxville, TN, USA', 'Mumbai', 'Ivankivs\'kyi district', 'Knox County', 'India', 'Ukraine', 'United States', 'Maharashtra', 'Kyiv Oblast', 'Tennessee', 'hdvcs dcsdc snb dc');

-- --------------------------------------------------------

--
-- Table structure for table `investor_individualinvestor`
--

CREATE TABLE `investor_individualinvestor` (
  `individual_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `investment_bracket` varchar(255) NOT NULL,
  `category1` varchar(255) NOT NULL,
  `category2` varchar(255) NOT NULL,
  `category3` varchar(255) NOT NULL,
  `sub_category1` varchar(255) NOT NULL,
  `sub_category2` varchar(255) NOT NULL,
  `sub_category3` varchar(255) NOT NULL,
  `capital_type` varchar(255) NOT NULL,
  `about` longtext NOT NULL,
  `looking_for` longtext NOT NULL,
  `website` varchar(500) DEFAULT NULL,
  `investor_id` int(11) DEFAULT NULL,
  `about_seller` longtext NOT NULL,
  `address_line1` varchar(256) NOT NULL,
  `address_line2` varchar(256) NOT NULL,
  `address_line3` varchar(256) NOT NULL,
  `city1` varchar(255) NOT NULL,
  `city2` varchar(255) NOT NULL,
  `city3` varchar(255) NOT NULL,
  `country1` varchar(255) NOT NULL,
  `country2` varchar(255) NOT NULL,
  `country3` varchar(255) NOT NULL,
  `state1` varchar(255) NOT NULL,
  `state2` varchar(255) NOT NULL,
  `state3` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `investor_individualinvestor`
--

INSERT INTO `investor_individualinvestor` (`individual_id`, `type`, `investment_bracket`, `category1`, `category2`, `category3`, `sub_category1`, `sub_category2`, `sub_category3`, `capital_type`, `about`, `looking_for`, `website`, `investor_id`, `about_seller`, `address_line1`, `address_line2`, `address_line3`, `city1`, `city2`, `city3`, `country1`, `country2`, `country3`, `state1`, `state2`, `state3`) VALUES
(1, 'Individual', '1 to 2 Crores', 'Consumer', 'Energy', 'Automotive', 'Gift', 'Oil/Gas (Production and Exploration)', 'Auto & Truck', 'Select type 2', 'bs sdv sd vdv', 'sdbhvdnv kdvskv  dw', NULL, 2, 'Financier', '', '', '', '', '', '', '', '', '', '', '', ''),
(2, 'Individual', '2 to 4 Crores', 'Social Media', 'Energy', 'Agriculture', 'Blogging Platforms', 'Energy', 'Farming/Agriculture', 'Select type 2', 'jhdc sjs dvs vs v', 'sjvs vks vks v', NULL, 4, 'Financier', '', '', '', '', '', '', '', '', '', '', '', ''),
(3, 'Individual', '2 to 4 Crores', 'Consumer', 'Manufacturing', 'Agriculture', 'Beauty', 'Chemical (Basic)', 'Agriculture', 'Select type 2', 'uuitu3t u3t uu 3uututu uj juj5tjtj tj 3535io 35 ji3ji  3tjo3', 't34tj34tjo 3tj3tj 3ioti3 jij43tj i3jt j4ji 3it i3jt j3iji3 4ij34i3j4t3j4tij34', 'http://www.google.com', 5, 'Financier', '', '', '', '', '', '', '', '', '', '', '', ''),
(4, 'Individual', '2 to 4 Crores', 'Manufacturing', 'Education', 'Education', 'Chemical (Basic)', 'Knowledge Mangement', 'EdTech', 'Select type 2', 'hbd dhbdc dh bdc', 'hjdb d dw sjdb wd', NULL, 6, 'Financier', '', '', '', '', '', '', '', '', '', '', '', ''),
(5, 'Individual', '2 to 4 Crores', 'Manufacturing', 'Manufacturing', 'Aerospace', 'Chemical (Basic)', 'Machinery', 'Aerospace/Defense', 'Select type 2', 'sd,jvbsd sdmn sdmn sdc', 'msdb sdbs dms dmsd ms', NULL, 7, 'Financier', '', '', '', '', '', '', '', '', '', '', '', ''),
(6, 'Individual', '1 to 2 Crores', 'Manufacturing', 'Manufacturing', 'Electronics', 'Chemical (Basic)', 'Building Materials', 'Electronics', 'Select type 2', 'whjb wfhw fwk fjnw', 'wjknfw wn f', NULL, 8, 'Financier', 'Chernobyl, Kyiv Oblast, Ukraine', 'Mumbai, Maharashtra, India', 'Chennai, Tamil Nadu, India', 'Ivankivs\'kyi district', 'Mumbai', 'Chennai', 'Ukraine', 'India', 'India', 'Kyiv Oblast', 'Maharashtra', 'Tamil Nadu');

-- --------------------------------------------------------

--
-- Table structure for table `investor_investor`
--

CREATE TABLE `investor_investor` (
  `investor_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `country_code_primary` varchar(255) NOT NULL,
  `phone_number_primary` varchar(10) NOT NULL,
  `email_adress` varchar(254) NOT NULL,
  `about_seller` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `album_id` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `investor_investor`
--

INSERT INTO `investor_investor` (`investor_id`, `first_name`, `middle_name`, `last_name`, `country_code_primary`, `phone_number_primary`, `email_adress`, `about_seller`, `created_at`, `album_id`, `type`, `title`) VALUES
(1, 'sdjv', 'lkv', 'jkdv', 'Aruba(+297)', '54', 'kajbd@dv.com', 'Broker', '2019-05-26 21:17:06.450591', 73, 'Individual', 'something'),
(2, 'sdjv', 'lkv', 'jkdv', 'Aruba(+297)', '54', 'kajbd@dv.com', 'Broker', '2019-05-26 21:19:49.903947', 73, 'Individual', 'something'),
(3, 'skdbv sddv d', 'hbv', 'kdjvb', 'Bahrain(+973)', '641', 'dc@sd.com', 'Owner', '2019-05-27 06:53:19.918449', 74, 'Company', 'something'),
(4, 'Minu', 'hsdbdv', 'wkjdb wwdkh', 'Afghanistan (+93)', '9846', 'asgvc@adv.com', 'Owner', '2019-05-29 14:27:37.579569', 84, 'Individual', 'something'),
(5, 'Prajwal_1', 'ergerg', 'ergerge', 'Afghanistan (+93)', '23323232', 'rfrwfrwf@gmail.com', 'Owner', '2019-05-31 15:06:07.848197', 91, 'Individual', 'something'),
(6, 'hvdc', 'sb', 'shkdvb', 'Afghanistan (+93)', '6851', 'hdbcsd@sdvc.com', 'Owner', '2019-06-13 06:19:02.826967', 95, 'Individual', 'something'),
(7, 'Pjdvsjd', 'sjhv', 'skjdbv', 'Afghanistan (+93)', '6541', 'sdcv@sfv.com', 'Owner', '2019-06-15 09:09:53.938264', 102, 'Individual', 'something'),
(8, 'dkfjnkjfv', 'sdkjbvkjb', 'sjvn', 'India (+91)', '78522', 'asfv@adv.com', 'Financier', '2019-06-21 06:24:43.715458', 117, 'Individual', 'something'),
(9, 'dvhb', 'ahvc', 'kjdbv', 'Afghanistan (+93)', '355', 'dv@adv.com', 'Individual_Investor', '2019-06-23 14:29:16.907304', 133, 'Company', 'ghdcv dcs csdcbscs cns c scnsbdcnbsdc');

-- --------------------------------------------------------

--
-- Table structure for table `metadata_advisor`
--

CREATE TABLE `metadata_advisor` (
  `id` int(11) NOT NULL,
  `types` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `metadata_advisor`
--

INSERT INTO `metadata_advisor` (`id`, `types`) VALUES
(1, 'Account Management'),
(2, 'Accounting'),
(3, 'Ad Planning & Buying'),
(4, '?Advertising'),
(5, '?Affiliate Marketing'),
(6, '?Algorithm'),
(7, '?Analytics Sales'),
(8, '?ATS Sales'),
(9, '?Attorney'),
(10, '?Audit'),
(11, '?Augmented Reality'),
(12, '?Autotask'),
(13, '?BPO'),
(14, '?Brand Management'),
(15, '?Brand Marketing'),
(16, '?Branding'),
(17, '?Bulk Marketing'),
(18, '?Business Analysis'),
(19, '?Business Plans'),
(20, '?Buyer Sourcing'),
(21, '?Call Center'),
(22, '?Channel Account Management'),
(23, '?Channel Sales'),
(24, '?Classifieds Posting'),
(25, '?Clean Technology'),
(26, '?Compliance'),
(27, '?Content Marketing'),
(28, '?Contracts'),
(29, '?Conversion Rate Optimisation'),
(30, '?CRM'),
(31, '?Customer Retention'),
(32, '?Customer Service'),
(33, '?Customer Support'),
(34, '?Data Analytics'),
(35, '?Data Mining'),
(36, '?Data Science'),
(37, '?Datacenter Sales'),
(38, '?Digital Agency Sales'),
(39, '?Drones'),
(40, '?Econometrics'),
(41, '?Economics'),
(42, '?Electrical Engineering'),
(43, '?Email Marketing'),
(44, '?Emerging Accounts'),
(45, '?Employment Law'),
(46, '?Engineering'),
(47, '?Enterprise Sales'),
(48, '?Enterprise Sales Management'),
(49, '?Entrepreneurship'),
(50, '?ERP'),
(51, '?Event Planning'),
(52, '?Facebook Marketing'),
(53, '?Field Sales'),
(54, '?Field Sales Management'),
(55, '?Finance'),
(56, '?Financial Analysis'),
(57, '?Financial Sales'),
(58, '?Fundraising'),
(59, '?Google Adsense'),
(60, '?Google Adwords'),
(61, '?Healthcare Sales'),
(62, '?HR Sales'),
(63, '?Human Resources'),
(64, '?Industrial Engineering'),
(65, '?Instrumentation'),
(66, '?Internet Marketing'),
(67, '?Internet of Things'),
(68, '?Internet Research'),
(69, '?Inventory Management'),
(70, '?Investment Research'),
(71, '?ISO9001'),
(72, '?Legal'),
(73, '?Legal Research'),
(74, '?Legal Writing'),
(75, '?Linear Programming'),
(76, '?Logistics & Shipping'),
(77, '?Machine Learning'),
(78, '?Management'),
(79, '?Manufacturing'),
(80, '?Manufacturing Design'),
(81, '?Market Research'),
(82, '?Marketing'),
(83, '?Marketing Strategy'),
(84, '?Materials Engineering'),
(85, '?Media Sales'),
(86, '?Medical Devices Sales'),
(87, '?Network Sales'),
(88, '?OEM Account Management'),
(89, '?OEM Sales'),
(90, '?Order Processing'),
(91, '?Organizational Change Management'),
(92, '?Patents'),
(93, '?Personal Development'),
(94, '?Procurement'),
(95, '?Product Design'),
(96, '?Product Management'),
(97, '?Product Sourcing'),
(98, '?Project Management'),
(99, '?Project Scheduling'),
(100, '?Property Development'),
(101, '?Property Law'),
(102, '?Property Management'),
(103, '?Public Relations'),
(104, '?Qualitative Research'),
(105, '?Rapid Prototyping'),
(106, '?Recruiting Sales'),
(107, '?Recruitment'),
(108, '?Resellers'),
(109, '?Retail Sales'),
(110, '?Risk Management'),
(111, '?Robotics'),
(112, '?Sales'),
(113, '?Sales Account Management'),
(114, '?Sales Management'),
(115, '?Sales Promotion'),
(116, '?Scientific Research'),
(117, '?Search Engine Marketing'),
(118, '?Security Sales'),
(119, '?Social Media Marketing'),
(120, '?Social Sales'),
(121, '?Software Sales'),
(122, '?Statistical Analysis'),
(123, '?Statistics'),
(124, '?Supplier Sourcing'),
(125, '?Tax'),
(126, '?Tax Law'),
(127, '?Technology Sales'),
(128, '?Time Management'),
(129, '?Twitter Marketing'),
(130, '?Viral Marketing'),
(131, '?Visual Merchandising'),
(132, 'Artificial Intelligence'),
(133, 'Cognitive Technologies'),
(134, 'Compliances & Outsourcing'),
(135, 'Cyber security consultant'),
(136, 'Eccomerce Marketing'),
(137, 'Financial consultant'),
(138, 'Financial Modelling'),
(139, 'HR consultant '),
(140, 'Import & Export Regulations'),
(141, 'IT consultant'),
(142, 'Marketing consultant'),
(143, 'MCA documentation'),
(144, 'Mobile App Development'),
(145, 'New venture registration'),
(146, 'Operations consultant'),
(147, 'Qualitative research'),
(148, 'Quantitative research'),
(149, 'SEO Consultant'),
(150, 'Technology consultant'),
(151, 'Transaction advisory'),
(152, 'Website Development');

-- --------------------------------------------------------

--
-- Table structure for table `metadata_businesssectors`
--

CREATE TABLE `metadata_businesssectors` (
  `id` int(11) NOT NULL,
  `sectors` varchar(255) NOT NULL,
  `sub_sectors` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `metadata_businesssectors`
--

INSERT INTO `metadata_businesssectors` (`id`, `sectors`, `sub_sectors`) VALUES
(1, 'Automotive ', 'Auto & Truck'),
(2, 'Manufacturing', 'Chemical (Basic)'),
(3, 'Utility', 'Utility (Water)'),
(4, 'Financial Services ', 'Brokerage & Investment Banking'),
(5, 'Financial Services ', 'Bank (Money Center)'),
(6, 'Electronics ', 'Electronics (Consumer & Office)'),
(7, 'Retail', 'Retail (Building Supply)'),
(8, 'Manufacturing', 'Shipbuilding & Marine'),
(9, 'Manufacturing', 'Metals & Mining'),
(10, 'Retail', 'Retail (Online)'),
(11, 'Aerospace', 'Aerospace/Defense'),
(12, 'Manufacturing', 'Machinery'),
(13, 'IT', 'Software (Entertainment)'),
(14, 'Education', 'Knowledge Mangement'),
(15, 'Retail', 'Apparel'),
(16, 'Manufacturing', 'Building Materials'),
(17, 'Realestate&Construction', 'Homebuilding'),
(18, 'Media & Broadcasting', 'Cable TV'),
(19, 'Aerospace', 'Aerospace'),
(20, 'Agriculture', 'Agriculture'),
(21, 'Emerging Technology', 'Analytics'),
(22, 'Website & Applications', 'Android'),
(23, 'Website & Applications', 'Apps'),
(24, 'Non-classifiable Establishments', 'Art'),
(25, 'Emerging Technology', 'Artificial Intelligence'),
(26, 'Non-classifiable Establishments', 'Association'),
(27, 'Automotive ', 'Automotive'),
(28, 'Non-classifiable Establishments', 'B2B'),
(29, 'Financial Services ', 'Banking'),
(30, 'Consumer', 'Beauty'),
(31, 'Emerging Technology', 'Big Data'),
(32, 'Pharma & Healthcare', 'Biotechnology'),
(33, 'Emerging Technology', 'Blockchain'),
(34, 'Social Media', 'Blogging Platforms'),
(35, 'Business Services ', 'Brand Marketing'),
(36, 'Business Services ', 'Business Development'),
(37, 'Business Services ', 'Business Intelligence'),
(38, 'Website & Applications', 'Cloud Computing'),
(39, 'Non-classifiable Establishments', 'Communities'),
(40, 'IT', 'Computer'),
(41, 'Realestate&Construction', 'Construction'),
(42, 'Business Services ', 'Consulting'),
(43, 'Electronics ', 'Consumer Electronics'),
(44, 'Retail', 'Consumer'),
(45, 'Social Media', 'Content'),
(46, 'Business Services ', 'Customer Service'),
(47, 'Emerging Technology', 'Cyber Security'),
(48, 'Business Services ', 'Data Visualization'),
(49, 'Business Services ', 'Database'),
(50, 'Transaporation & Logistics', 'Delivery'),
(51, 'Website & Applications', 'Developer APIs'),
(52, 'Website & Applications', 'Developer Platform'),
(53, 'Website & Applications', 'Developer Tools'),
(54, 'Media & Broadcasting', 'Digital Entertainment'),
(55, 'Business Services ', 'Digital Marketing'),
(56, 'Media & Broadcasting', 'Digital Media'),
(57, 'Emerging Technology', 'Drones'),
(58, 'Transaporation & Logistics', 'E-Commerce'),
(59, 'Education', 'EdTech'),
(60, 'Education', 'Education'),
(61, 'Education', 'E-Learning'),
(62, 'Electronics ', 'Electronics'),
(63, 'Business Services ', 'Employment'),
(64, 'Energy', 'Energy'),
(65, 'IT', 'Enterprise Software'),
(66, 'Non-classifiable Establishments', 'Event Management'),
(67, 'Non-classifiable Establishments', 'Events'),
(68, 'Consumer', 'Fashion'),
(69, 'Media & Broadcasting', 'Film'),
(70, 'Financial Services ', 'Finance'),
(71, 'Financial Services ', 'Financial Services'),
(72, 'Financial Services ', 'FinTech'),
(73, 'Pharma & Healthcare', 'Fitness'),
(74, 'Food & Beverage', 'Food and Beverage'),
(75, 'Food & Beverage', 'Food Delivery'),
(76, 'Food & Beverage', 'Food Processing'),
(77, 'Non-classifiable Establishments', 'Furniture'),
(78, 'Non-classifiable Establishments', 'Gambling'),
(79, 'Non-classifiable Establishments', 'Gamification'),
(80, 'Non-classifiable Establishments', 'Generation Y'),
(81, 'Pharma & Healthcare', 'Genetics'),
(82, 'Non-classifiable Establishments', 'Geospatial'),
(83, 'Business Services ', 'Gift Card'),
(84, 'Consumer', 'Gift'),
(85, 'Government', 'Government'),
(86, 'Website & Applications', 'Graphic Design'),
(87, 'Energy', 'GreenTech'),
(88, 'IT', 'Hardware'),
(89, 'Pharma & Healthcare', 'Health Care'),
(90, 'Pharma & Healthcare', 'Health Diagnostics'),
(91, 'Education', 'Higher Education'),
(92, 'Non-classifiable Establishments', 'Home Decor'),
(93, 'Non-classifiable Establishments', 'Home Services'),
(94, 'Pharma & Healthcare', 'Hospital'),
(95, 'Travel,Hotel&Hospitality', 'Hospitality'),
(96, 'Travel,Hotel&Hospitality', 'Hotel'),
(97, 'Manufacturing', 'Industrial Engineering'),
(98, 'Manufacturing', 'Industrial'),
(99, 'IT', 'Information Services'),
(100, 'IT', 'Information Technology'),
(101, 'IT', 'Infrastructure'),
(102, 'Non-classifiable Establishments', 'Innovation Management'),
(103, 'Financial Services ', 'Insurance'),
(104, 'Emerging Technology', 'Internet of Things'),
(105, 'Emerging Technology', 'Internet'),
(106, 'Website & Applications', 'iOS'),
(107, 'Non-classifiable Establishments', 'Janitorial Service'),
(108, 'Consumer', 'Jewelry'),
(109, 'Media & Broadcasting', 'Journalism'),
(110, 'Education', 'Language Learning'),
(111, 'Business Services ', 'Lead Generation'),
(112, 'Business Services ', 'Legal'),
(113, 'Travel,Hotel&Hospitality', 'Leisure'),
(114, 'Financial Services ', 'Lending'),
(115, 'Pharma & Healthcare', 'Life Science'),
(116, 'Consumer', 'Lifestyle'),
(117, 'Non-classifiable Establishments', 'Local'),
(118, 'Non-classifiable Establishments', 'Location Based Services'),
(119, 'Transaporation & Logistics', 'Logistics'),
(120, 'Emerging Technology', 'Machine Learning'),
(121, 'Manufacturing', 'Manufacturing'),
(122, 'Business Services ', 'Marketing'),
(123, 'Website & Applications', 'Marketplace'),
(124, 'Media & Broadcasting', 'Media and Entertainment'),
(125, 'Pharma & Healthcare', 'Medical Device'),
(126, 'Pharma & Healthcare', 'Medical'),
(127, 'Website & Applications', 'Mobile Apps'),
(128, 'Consumer', 'Mobile'),
(129, 'Entertainment', 'Music'),
(130, 'Emerging Technology', 'Nanotechnology'),
(131, 'Government', 'National Security'),
(132, 'Emerging Technology', 'Natural Language Processing'),
(133, 'Non-classifiable Establishments', 'Natural Resources'),
(134, 'Non-classifiable Establishments', 'Navigation'),
(135, 'IT', 'Network Hardware'),
(136, 'Website & Applications', 'Network Security'),
(137, 'Media & Broadcasting', 'News'),
(138, 'Non-classifiable Establishments', 'Non Profit'),
(139, 'Food & Beverage', 'Nutrition'),
(140, 'Energy', 'Oil and Gas'),
(141, 'Website & Applications', 'Online Auctions'),
(142, 'Non-classifiable Establishments', 'Online Games'),
(143, 'Non-classifiable Establishments', 'Online Portals'),
(144, 'Non-classifiable Establishments', 'Open Source'),
(145, 'Non-classifiable Establishments', 'Optical Communication'),
(146, 'Food & Beverage', 'Organic Food'),
(147, 'Food & Beverage', 'Organic'),
(148, 'Non-classifiable Establishments', 'Outdoors'),
(149, 'Non-classifiable Establishments', 'Outsourcing'),
(150, 'Financial Services ', 'Payments'),
(151, 'Pharma & Healthcare', 'Pharmaceutical'),
(152, 'Media & Broadcasting', 'Photography'),
(153, 'Non-classifiable Establishments', 'Printing'),
(154, 'Manufacturing', 'Product Design'),
(155, 'Business Services ', 'Professional Services'),
(156, 'Business Services ', 'Project Management'),
(157, 'Realestate&Construction', 'Property Management'),
(158, 'Media & Broadcasting', 'Public Relations'),
(159, 'Media & Broadcasting', 'Publishing'),
(160, 'Non-classifiable Establishments', 'Q&A'),
(161, 'Non-classifiable Establishments', 'QR Codes'),
(162, 'Business Services ', 'Quality Assurance'),
(163, 'Non-classifiable Establishments', 'Quantified Self'),
(164, 'Emerging Technology', 'Quantum Computing'),
(165, 'Realestate&Construction', 'Real Estate Investment'),
(166, 'Realestate&Construction', 'Real Estate'),
(167, 'Non-classifiable Establishments', 'Real Time'),
(168, 'Non-classifiable Establishments', 'Recruiting'),
(169, 'Energy', 'Renewable Energy'),
(170, 'Travel,Hotel&Hospitality', 'Restaurants'),
(171, 'Retail', 'Retail Technology'),
(172, 'Retail', 'Retail'),
(173, 'Financial Services ', 'Risk Management'),
(174, 'Emerging Technology', 'Robotics'),
(175, 'IT', 'SaaS'),
(176, 'Website & Applications', 'Search Engine'),
(177, 'Website & Applications', 'Security'),
(178, 'Website & Applications', 'SEO'),
(179, 'Travel,Hotel&Hospitality', 'Service Industry'),
(180, 'Consumer', 'Shopping'),
(181, 'Social Media', 'Social Media'),
(182, 'Social Media', 'Social Network'),
(183, 'IT', 'Software'),
(184, 'Non-classifiable Establishments', 'Sports'),
(185, 'Telecommunications', 'Telecommunications'),
(186, 'Non-classifiable Establishments', 'Test and Measurement'),
(187, 'Consumer', 'Textiles'),
(188, 'Pharma & Healthcare', 'Therapeutics'),
(189, 'Non-classifiable Establishments', 'Ticketing'),
(190, 'Travel,Hotel&Hospitality', 'Tourism'),
(191, 'Financial Services ', 'Trading Platform'),
(192, 'Education', 'Training'),
(193, 'Travel,Hotel&Hospitality', 'Transportation'),
(194, 'Travel,Hotel&Hospitality', 'Travel'),
(195, 'Non-classifiable Establishments', 'Ultimate Frisbee'),
(196, 'Non-classifiable Establishments', 'Underserved Children'),
(197, 'Non-classifiable Establishments', 'Unified Communications'),
(198, 'Education', 'Universities'),
(199, 'IT', 'Usability Testing'),
(200, 'Website & Applications', 'UX Design'),
(201, 'Non-classifiable Establishments', 'Venture Capital'),
(202, 'Pharma & Healthcare', 'Veterinary'),
(203, 'Media & Broadcasting', 'Video Advertising'),
(204, 'Non-classifiable Establishments', 'Video Games'),
(205, 'Media & Broadcasting', 'Video on Demand'),
(206, 'Media & Broadcasting', 'Video Streaming'),
(207, 'Media & Broadcasting', 'Video'),
(208, 'Emerging Technology', 'Virtual Reality'),
(209, 'Emerging Technology', 'Virtualization'),
(210, 'Telecommunications', 'VoIP'),
(211, 'Utility', 'Water'),
(212, 'Emerging Technology', 'Wearables'),
(213, 'Website & Applications', 'Web Apps'),
(214, 'Website & Applications', 'Web Design'),
(215, 'Website & Applications', 'Web Development'),
(216, 'Website & Applications', 'Web Hosting'),
(217, 'Pharma & Healthcare', 'Wellness'),
(218, 'Consumer', 'Wholesale'),
(219, 'Food & Beverage', 'Wine And Spirits'),
(220, 'Telecommunications', 'Wireless'),
(221, 'Consumer', 'Young Adults'),
(222, 'Non-classifiable Establishments', 'Gaming'),
(223, 'Pharma & Healthcare', 'Heathcare Information and Technology'),
(224, 'Pharma & Healthcare', 'Hospitals/Healthcare Facilities'),
(225, 'Food & Beverage', 'Beverage (Alcoholic)'),
(226, 'Entertainment', 'Recreation'),
(227, 'Energy', 'Coal & Related Energy'),
(228, 'Media & Broadcasting', 'Broadcasting'),
(229, 'Education', 'Education'),
(230, 'Financial Services ', 'Insurance (Life)'),
(231, 'Food & Beverage', 'Beverage (Soft)'),
(232, 'Energy', 'Green & Renewable Energy'),
(233, 'Manufacturing', 'Chemical (Specialty)'),
(234, 'Financial Services ', 'Banks (Regional)'),
(235, 'Energy', 'Oil/Gas (Integrated)'),
(236, 'Non-classifiable Establishments', 'Diversified'),
(237, 'Media & Broadcasting', 'Advertising'),
(238, 'Realestate&Construction', 'Real Estate (Operations & Services)'),
(239, 'Pharma & Healthcare', 'Drugs (Pharmaceutical)'),
(240, 'Electronics ', 'Electronics (General)'),
(241, 'Financial Services ', 'Insurance (General)'),
(242, 'Retail', 'Retail (General)'),
(243, 'Utility', 'Utility (General)'),
(244, 'Pharma & Healthcare', 'Drugs (Biotechnology)'),
(245, 'Retail', 'Retail (Distributors)'),
(246, 'IT', 'Software (System & Application)'),
(247, 'Agriculture', 'Farming/Agriculture'),
(248, 'Transaporation & Logistics', 'Transportation (Railroads)'),
(249, 'IT', 'Computers/Peripherals'),
(250, 'Telecommunications', 'Telecom (Wireless)'),
(251, 'Retail', 'Retail (Special Lines)'),
(252, 'Non-classifiable Establishments', 'Hotel/Gaming'),
(253, 'Food & Beverage', 'Food Wholesalers'),
(254, 'Realestate&Construction', 'Real Estate (Development)'),
(255, 'Financial Services ', 'Investments & Asset Management'),
(256, 'Retail', 'Retail (Grocery and Food)'),
(257, 'Consumer', 'Furn/Home Furnishings'),
(258, 'Financial Services ', 'Reinsurance'),
(259, 'IT', 'Software (Internet)'),
(260, 'Food & Beverage', 'Food Processing'),
(261, 'Retail', 'Retail (Automotive)'),
(262, 'Electronics ', 'Semiconductor'),
(263, 'Manufacturing', 'Packaging & Container'),
(264, 'Financial Services ', 'Insurance (Prop/Cas.)'),
(265, 'Electronics ', 'Semiconductor Equip'),
(266, 'Energy', 'Oil/Gas (Production and Exploration)'),
(267, 'Transaporation & Logistics', 'Transportation'),
(268, 'Business Services ', 'Human ResourcesCategory '),
(269, 'Energy', 'Power'),
(270, 'Pharma & Healthcare', 'Healthcare Products'),
(271, 'Consumer', 'Household Products'),
(272, 'Non-classifiable Establishments', 'Paper/Forest Products'),
(273, 'Electronics ', 'Electrical Equipment'),
(274, 'Telecommunications', 'Telecom. Equipment'),
(275, 'Manufacturing', 'Rubber& Tires'),
(276, 'Realestate&Construction', 'R.E.I.T.'),
(277, 'Aerospace', 'Air Transport'),
(278, 'Emerging Technology', 'Generation Z'),
(279, 'Energy', 'Oil/Gas Distribution'),
(280, 'Manufacturing', 'Chemical (Diversified)'),
(281, 'Realestate&Construction', 'Real Estate (General/Diversified)'),
(282, 'Non-classifiable Establishments', 'Precious Metals'),
(283, 'Energy', 'Oilfield Svcs/Equip.'),
(284, 'Business Services ', 'Business & Consumer Services'),
(285, 'IT', 'Computer Services'),
(286, 'Non-classifiable Establishments', 'Environmental & Waste Services'),
(287, 'Pharma & Healthcare', 'Healthcare Support Services'),
(288, 'IT', 'Information Services'),
(289, 'Business Services ', 'Office Equipment & Services'),
(290, 'Telecommunications', 'Telecom. Services'),
(291, 'Consumer', 'Shoe'),
(292, 'Realestate&Construction', 'Steel'),
(293, 'Realestate&Construction', 'Construction Supplies'),
(294, 'Financial Services ', 'Financial Svcs. (Non-bank & Insurance)'),
(295, 'Travel,Hotel&Hospitality', 'Restaurant/Dining'),
(296, 'Entertainment', 'Entertainment'),
(297, 'Automotive ', 'Auto Parts'),
(298, 'Non-classifiable Establishments', 'Tobacco'),
(299, 'Transaporation & Logistics', 'Trucking'),
(300, 'Realestate&Construction', 'Engineering/Construction'),
(301, 'Media & Broadcasting', 'Publishing & Newspapers'),
(302, 'Non-classifiable Establishments', 'Xbox');

-- --------------------------------------------------------

--
-- Table structure for table `metadata_codes`
--

CREATE TABLE `metadata_codes` (
  `id` int(11) NOT NULL,
  `dialing` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `metadata_codes`
--

INSERT INTO `metadata_codes` (`id`, `dialing`, `code`) VALUES
(1, '93', 'Afghanistan (+93)'),
(2, '355', 'Albania (+355)'),
(3, '213', 'Algeria (+213)'),
(4, '-683', 'Samoa(+1-684)'),
(5, '376', 'Andorra(+376)'),
(6, '244', 'Angola(+244)'),
(7, '-263', 'Anguilla (+1-264)'),
(8, '672', 'Antarctica(+672)'),
(9, '-267', 'Antigua(+1-268)'),
(10, '54', 'Argentina (+54)'),
(11, '374', 'Armenia(+374)'),
(12, '297', 'Aruba(+297)'),
(13, '61', 'Australia(+61)'),
(14, '43', 'Austria(+43)'),
(15, '994', 'Azerbaijan(+994)'),
(16, '-241', 'Bahamas(+1-242)'),
(17, '973', 'Bahrain(+973)'),
(18, '880', 'Bangladesh(+880)'),
(19, '-245', 'Barbados (+1-246)'),
(20, '375', 'Belarus(+375)'),
(21, '32', 'Belgium (+32)'),
(22, '501', 'Belize(+501)'),
(23, '229', 'Benin(+229)'),
(24, '-440', 'Bermuda (+1-441)'),
(25, '975', 'Bhutan(+975)'),
(26, '591', 'Bolivia (+591)'),
(27, '387', 'Bosnia(+387)'),
(28, '267', 'Botswana(+267)'),
(29, '55', 'Brazil (+55)'),
(30, '673', 'Brunei(+673)'),
(31, '359', 'Bulgaria (+359)'),
(32, '226', 'Burkina Faso(+226)'),
(33, '257', 'Burundi(+257)'),
(34, '855', 'Cambodia(+855)'),
(35, '237', 'Cameroon(+237)'),
(36, '1', 'Canada (+1)'),
(37, '238', 'Cape Verde (+238)'),
(38, '-344', 'Cayman Islands (+1-345)'),
(39, '236', 'Central African(+236)'),
(40, '235', 'Chad (+235)'),
(41, '56', 'Chile (+56)'),
(42, '86', 'China (+86)'),
(43, '53', 'Christmas Island (+53)'),
(44, '61', 'Cocos(+61)'),
(45, '57', 'Colombia (+57)'),
(46, '269', 'Comoros(+269)'),
(47, '243', 'Congo(+243)'),
(48, '242', 'Congo(+242)'),
(49, '682', 'Cook Islands(+682)'),
(50, '506', 'Costa Rica (+506)'),
(51, '225', 'Cote D\'Ivoire(+225)'),
(52, '385', 'Croatia(+385)'),
(53, '53', 'Cuba (+53)'),
(54, '357', 'Cyprus (+357)'),
(55, '420', 'Czech Republic(+420)'),
(56, '45', 'Denmark (+45)'),
(57, '253', 'Djibouti(+253)'),
(58, '-766', 'Dominica (+1-767)'),
(59, '+1-809 and +1-829? ', 'Dominican Republic (+1-809 and +1-829? )'),
(60, '670', 'East Timor(+670)'),
(61, '593', 'Ecuador (+593 )'),
(62, '20', 'Egypt(+20)'),
(63, '503', 'El Salvador (+503)'),
(64, '240', 'Guinea(+240)'),
(65, '291', 'Eritrea(+291)'),
(66, '372', 'Estonia(+372)'),
(67, '251', 'Ethiopia(+251)'),
(68, '500', 'Falkland Islands(+500)'),
(69, '298', 'Faroe Islands (+298)'),
(70, '679', 'Fiji (+679)'),
(71, '358', 'Finland (+358)'),
(72, '33', 'France (+33)'),
(73, '594', 'French Guiana(+594)'),
(74, '689', 'French Polynesia(+689)'),
(75, '241', 'Gabon(+241)'),
(76, '220', 'Gambia, The (+220)'),
(77, '995', 'Georgia(+995)'),
(78, '49', 'Germany (+49)'),
(79, '233', 'Ghana(+233)'),
(80, '350', 'Gibraltar (+350)'),
(81, '30', 'Greece (+30)'),
(82, '299', 'Greenland (+299)'),
(83, '-472', 'Grenada (+1-473)'),
(84, '590', 'Guadeloupe(+590)'),
(85, '-670', 'Guam(+1-671)'),
(86, '502', 'Guatemala (+502)'),
(87, '224', 'Guinea(+224)'),
(88, '245', 'Guinea-Bissau(+245)'),
(89, '592', 'Guyana(+592)'),
(90, '509', 'Haiti (+509)'),
(91, '504', 'Honduras (+504)'),
(92, '852', 'Hong Kong (+852)'),
(93, '36', 'Hungary (+36)'),
(94, '354', 'Iceland (+354)'),
(95, '91', 'India (+91)'),
(96, '62', 'Indonesia(+62)'),
(97, '98', 'Iran, Islamic Republic of(+98)'),
(98, '964', 'Iraq (+964)'),
(99, '353', 'Ireland (+353)'),
(100, '972', 'Israel (+972)'),
(101, '39', 'Italy (+39)'),
(102, '-875', 'Jamaica (+1-876)'),
(103, '81', 'Japan (+81)'),
(104, '962', 'Jordan(+962)'),
(105, '7', 'Kazakstan(+7)'),
(106, '254', 'Kenya(+254)'),
(107, '686', 'Kiribati(+686)'),
(108, '850', 'North Korea(+850)'),
(109, '82', 'South Korea(+82)'),
(110, '965', 'Kuwait (+965)'),
(111, '996', 'Kyrgyzstan(+996)'),
(112, '856', 'Lao(+856)'),
(113, '371', 'Latvia(+371)'),
(114, '961', 'Lebanon (+961)'),
(115, '266', 'Lesotho(+266)'),
(116, '231', 'Liberia (+231)'),
(117, '218', 'Libya(+218)'),
(118, '423', 'Liechtenstein (+423)'),
(119, '370', 'Lithuania(+370)'),
(120, '352', 'Luxembourg (+352)'),
(121, '853', 'Macau (+853)'),
(122, '389', 'Macedonia, The Former Yugoslav Republic of(+389)'),
(123, '261', 'Madagascar(+261)'),
(124, '265', 'Malawi(+265)'),
(125, '60', 'Malaysia (+60)'),
(126, '960', 'Maldives (+960)'),
(127, '223', 'Mali(+223)'),
(128, '356', 'Malta (+356)'),
(129, '692', 'Marshall Islands(+692)'),
(130, '596', 'Martinique(+596)'),
(131, '222', 'Mauritania (+222)'),
(132, '230', 'Mauritius (+230)'),
(133, '269', 'Mayotte(+269)'),
(134, '52', 'Mexico (+52)'),
(135, '691', 'Micronesia(+691)'),
(136, '373', 'Moldova, Republic of(+373)'),
(137, '377', 'Monaco, Principality of(+377)'),
(138, '976', 'Mongolia(+976)'),
(139, '-663', 'Montserrat (+1-664)'),
(140, '212', 'Morocco (+212)'),
(141, '258', 'Mozambique(+258)'),
(142, '95', 'Myanmar(+95)'),
(143, '264', 'Namibia(+264)'),
(144, '674', 'Nauru(+674)'),
(145, '977', 'Nepal (+977)'),
(146, '31', 'Netherlands (+31)'),
(147, '599', 'Netherlands Antilles(+599)'),
(148, '687', 'New Caledonia (+687)'),
(149, '64', 'New Zealand(+64)'),
(150, '505', 'Nicaragua (+505)'),
(151, '227', 'Niger (+227)'),
(152, '234', 'Nigeria (+234)'),
(153, '683', 'Niue(+683)'),
(154, '672', 'Norfolk Island (+672)'),
(155, '-669', 'Mariana Islands(+1-670)'),
(156, '47', 'Norway (+47)'),
(157, '968', 'Oman(+968)'),
(158, '92', 'Pakistan(+92)'),
(159, '680', 'Palau(+680)'),
(160, '970', 'Palestinian State(+970)'),
(161, '507', 'Panama (+507)'),
(162, '675', 'Papua New Guinea(+675)'),
(163, '595', 'Paraguay (+595)'),
(164, '51', 'Peru (+51)'),
(165, '63', 'Philippines (+63)'),
(166, '48', 'Poland (+48)'),
(167, '351', 'Portugal (+351)'),
(168, '+1-787 or +1-939', 'Puerto Rico (+1-787 or +1-939)'),
(169, '974', 'Qatar, State of (+974 )'),
(170, '262', 'Reunion(+262)'),
(171, '40', 'Romania (+40)'),
(172, '7', 'Russian Federation (+7)'),
(173, '250', 'Rwanda(+250)'),
(174, '290', 'Saint Helena (+290)'),
(175, '-868', 'Saint Kitts(+1-869)'),
(176, '-757', 'Saint Lucia (+1-758)'),
(177, '508', 'Saint Pierre(+508)'),
(178, '-783', 'Saint Vincent(+1-784)'),
(179, '685', 'Samoa(+685)'),
(180, '378', 'San Marino (+378)'),
(181, '239', 'Sao Tome(+239)'),
(182, '966', 'Saudi Arabia (+966)'),
(183, '221', 'Senegal (+221)'),
(184, '248', 'Seychelles (+248)'),
(185, '232', 'Sierra Leone (+232)'),
(186, '65', 'Singapore (+65)'),
(187, '421', 'Slovakia(+421)'),
(188, '386', 'Slovenia (+386)'),
(189, '677', 'Solomon Islands(+677)'),
(190, '252', 'Somalia(+252)'),
(191, '27', 'South Africa(+27)'),
(192, '34', 'Spain (+34)'),
(193, '94', 'Sri Lanka(+94)'),
(194, '249', 'Sudan(+249)'),
(195, '597', 'Suriname(+597)'),
(196, '268', 'Swaziland(+268)'),
(197, '46', 'Sweden (+46)'),
(198, '41', 'Switzerland (+41)'),
(199, '963', 'Syria(+963)'),
(200, '886', 'Taiwan(+886)'),
(201, '992', 'Tajikistan(+992)'),
(202, '255', 'Tanzania(+255)'),
(203, '66', 'Thailand(+66)'),
(204, '690', 'Tokelau (+690)'),
(205, '676', 'Tonga, Kingdom of(+676)'),
(206, '-867', 'Trinidad(+1-868)'),
(207, '216', 'Tunisia (+216)'),
(208, '90', 'Turkey (+90)'),
(209, '993', 'Turkmenistan(+993)'),
(210, '-648', 'Turks & Caicos(+1-649)'),
(211, '688', 'Tuvalu(+688)'),
(212, '256', 'Uganda(+256)'),
(213, '380', 'Ukraine(+380)'),
(214, '971', 'UAE(+971)'),
(215, '44', 'United Kingdom(+44)'),
(216, '1', 'United States (+1)'),
(217, '598', 'Uruguay(+598)'),
(218, '998', 'Uzbekistan(+998)'),
(219, '678', 'Vanuatu(+678)'),
(220, '418', 'Vatican City State(+418)'),
(221, '58', 'Venezuela (+58)'),
(222, '84', 'Vietnam (+84)'),
(223, '-283', 'Virgin Islands(+1-284)'),
(224, '-339', 'Virgin Islands(+1-340)'),
(225, '681', 'Wallis & Futuna(+681)'),
(226, '967', 'Yemen (+967)'),
(227, '260', 'Zambia(+260)'),
(228, '263', 'Zimbabwe(+263)');

-- --------------------------------------------------------

--
-- Table structure for table `metadata_company`
--

CREATE TABLE `metadata_company` (
  `id` int(11) NOT NULL,
  `types` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `metadata_company`
--

INSERT INTO `metadata_company` (`id`, `types`) VALUES
(1, 'Sole Proprietorship/trader'),
(2, 'Association'),
(3, 'S Corporation'),
(4, 'C Corporation '),
(5, 'General Partnership'),
(6, 'Joint Venture'),
(7, 'Limited Liability Company (LLC)'),
(8, 'Limited Liability Limited Partnership (LLLP)'),
(9, 'Limited Liability Partnership (LLP)'),
(10, 'Limited Partnership'),
(11, 'Trust'),
(12, 'Municipality'),
(13, 'Nonprofit Corporation'),
(14, 'Co-orperative'),
(15, 'Private Limited'),
(16, 'Public Limited'),
(17, 'One Person Company');

-- --------------------------------------------------------

--
-- Table structure for table `metadata_years`
--

CREATE TABLE `metadata_years` (
  `id` int(11) NOT NULL,
  `code` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `metadata_years`
--

INSERT INTO `metadata_years` (`id`, `code`) VALUES
(1, 2019),
(2, 2018),
(3, 2017),
(4, 2016),
(5, 2015),
(6, 2014),
(7, 2013),
(8, 2012),
(9, 2011),
(10, 2010),
(11, 2009),
(12, 2008),
(13, 2007),
(14, 2006),
(15, 2005),
(16, 2004),
(17, 2003),
(18, 2002),
(19, 2001),
(20, 2000),
(21, 1999),
(22, 1998),
(23, 1997),
(24, 1996),
(25, 1995),
(26, 1994),
(27, 1993),
(28, 1992),
(29, 1991),
(30, 1990),
(31, 1989),
(32, 1988),
(33, 1987),
(34, 1986),
(35, 1985),
(36, 1984),
(37, 1983),
(38, 1982),
(39, 1981),
(40, 1980),
(41, 1979),
(42, 1978),
(43, 1977),
(44, 1976),
(45, 1975),
(46, 1974),
(47, 1973),
(48, 1972),
(49, 1971),
(50, 1970),
(51, 1969),
(52, 1968),
(53, 1967),
(54, 1966),
(55, 1965),
(56, 1964),
(57, 1963),
(58, 1962),
(59, 1961),
(60, 1960),
(61, 1959),
(62, 1958),
(63, 1957),
(64, 1956),
(65, 1955),
(66, 1954),
(67, 1953),
(68, 1952),
(69, 1951),
(70, 1950),
(71, 1949),
(72, 1948),
(73, 1947),
(74, 1946),
(75, 1945),
(76, 1944),
(77, 1943),
(78, 1942),
(79, 1941);

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile`
--

CREATE TABLE `profiles_profile` (
  `profile_id` int(11) NOT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `contact_number` varchar(10) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `invest_type_id` int(11) DEFAULT NULL,
  `curr_chat_id` int(11) DEFAULT NULL,
  `photo_url` varchar(255) DEFAULT NULL,
  `social` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles_profile`
--

INSERT INTO `profiles_profile` (`profile_id`, `first_name`, `last_name`, `photo`, `contact_number`, `created_at`, `user_id`, `status`, `invest_type_id`, `curr_chat_id`, `photo_url`, `social`) VALUES
(1, '', '', '', NULL, '2019-05-09 00:53:51.579924', 1, 0, NULL, NULL, NULL, 0),
(3, '', '', '', NULL, '2019-05-09 00:59:28.862162', 2, 0, NULL, NULL, NULL, 0),
(4, '', '', '', NULL, '2019-05-09 01:11:05.577892', 3, 0, NULL, NULL, NULL, 0),
(5, '', '', '', NULL, '2019-05-09 01:13:20.670756', 4, 0, NULL, NULL, NULL, 0),
(6, 'Prajwal', 'Barapatre', 'files/20170525_150857.jpg', NULL, '2019-05-09 01:17:15.323865', 5, 0, NULL, 3, NULL, 0),
(7, '', '', '', NULL, '2019-05-09 01:54:51.201281', 6, 0, NULL, NULL, NULL, 0),
(8, 'Prajwal', 'Barapatre', '[]', '9167330324', '2019-05-09 02:00:29.252487', 7, 0, NULL, NULL, NULL, 0),
(9, 'Prajwal_15', 'Barapatre', '[]', '9167330324', '2019-05-09 19:37:26.862700', 8, 0, NULL, NULL, NULL, 0),
(10, '', '', '', NULL, '2019-05-09 19:46:03.710415', 9, 0, NULL, NULL, NULL, 0),
(11, 'Prajwal_1', 'Barapatre', 'files/20170526_111201.jpg', '9167330324', '2019-05-09 23:59:07.709373', 10, 0, NULL, NULL, NULL, 0),
(12, '', '', '', NULL, '2019-05-10 00:58:00.054974', 11, 0, NULL, NULL, NULL, 0),
(13, 'Mrunali', 'Barapatre', '[]', '9167330324', '2019-05-10 01:02:02.402594', 12, 0, NULL, NULL, NULL, 0),
(14, 'good', 'good', 'files/20170525_133305.jpg', '9167330324', '2019-05-10 01:05:46.724109', 13, 0, NULL, NULL, NULL, 0),
(15, '', '', '', NULL, '2019-05-09 20:55:53.143345', 14, 0, NULL, NULL, NULL, 0),
(16, 'Trying', 'Trying', 'files/20170525_150857.jpg', '9167330324', '2019-05-09 21:06:03.673174', 15, 0, NULL, NULL, NULL, 0),
(17, 'Trying', 'Barapatre', 'files/20170525_103344.jpg', '9167330324', '2019-05-09 21:10:44.293393', 16, 0, NULL, NULL, NULL, 0),
(18, '', '', '', NULL, '2019-05-09 21:14:55.149399', 17, 0, NULL, NULL, NULL, 0),
(19, 'Mrunali', 'Barapatre', 'files/20170525_072328.jpg', '8795642130', '2019-05-09 22:14:57.146470', 18, 0, NULL, NULL, NULL, 0),
(20, 'Prajwal_15', 'Try', 'files/20170524_132531.jpg', '8795462130', '2019-05-09 22:19:58.633681', 19, 0, NULL, NULL, NULL, 0),
(21, 'Minu1', 'Barapatre', 'files/20170525_072328_tp7lf0K.jpg', '9167330324', '2019-05-10 09:26:38.766120', 20, 0, 4, 3, NULL, 0),
(22, 'Prithvi', 'Raj', 'files/20170525_161727.jpg', '9167330324', '2019-05-11 11:14:25.885760', 21, 0, NULL, NULL, NULL, 0),
(23, 'Mrunali', 'good', 'files/IMG_0335.jpg', '43434433', '2019-05-31 15:01:26.825625', 22, 0, 5, NULL, NULL, 0),
(24, 'Minu', 'Prajwal', 'files/download_4.jpg', '458133', '2019-06-02 06:50:56.554525', 23, 0, 6, NULL, NULL, 0),
(25, 'Vimal', 'Barapatre', 'files/download_6.jpg', '8765430984', '2019-06-02 06:57:14.749938', 24, 0, NULL, NULL, NULL, 0),
(26, 'Subhash', 'Barapatre', 'files/download_7.jpg', '7624098', '2019-06-02 07:00:15.076720', 25, 0, NULL, NULL, NULL, 0),
(27, 'Sweety', 'Priya', 'files/download_9.jpg', '7654092', '2019-06-02 07:01:55.869606', 26, 0, NULL, NULL, NULL, 0),
(28, 'Renuka', 'Dhakate', 'files/download_8.jpg', '76123095', '2019-06-02 07:21:38.415223', 27, 0, 9, NULL, NULL, 0),
(29, 'Thrisha', 'Dhakate', 'files/download_5.jpg', '6531097', '2019-06-02 07:23:07.663165', 28, 0, NULL, NULL, NULL, 0),
(30, 'Usha', 'Barapatre', 'files/download_9_38d6mJ8.jpg', '7651094', '2019-06-02 07:25:32.013304', 29, 0, NULL, NULL, NULL, 0),
(31, 'Vidhya', 'Dhakate', 'files/images_1.jpg', '8797435', '2019-06-02 07:27:45.737811', 30, 0, NULL, NULL, NULL, 0),
(32, 'vimal', 'barapatre', 'files/images_12.jpg', '788542', '2019-06-21 06:06:38.824479', 31, 0, 8, NULL, NULL, 0),
(33, 'user1', 'user', 'files/images_3_tbigiNo.jpg', '9167330324', '2019-06-26 14:51:46.429790', 32, 0, NULL, NULL, NULL, 0),
(34, 'akjdbc', 'kadbc', 'files/images_9_kxg9HYG.jpg', '454548', '2019-06-26 15:41:38.756596', 33, 0, NULL, NULL, NULL, 0),
(35, '', '', '', NULL, '2019-06-29 08:41:48.966946', 34, 0, NULL, NULL, 'https://avatars3.githubusercontent.com/u/42388402?v=4', 0),
(36, 'Prajwal', 'Barapatre', '', NULL, '2019-06-29 08:46:11.479463', 35, 0, NULL, NULL, 'https://lh6.googleusercontent.com/-r7xuWnjtvQM/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rc3yLReSTZRWDGYr6fDqLRbFjFpFw/photo.jpg', 1),
(37, '', '', '', NULL, '2019-06-29 11:37:49.449268', 36, 0, NULL, NULL, NULL, 0),
(38, '', '', '', NULL, '2019-06-29 11:41:43.016895', 37, 0, NULL, NULL, 'https://avatars3.githubusercontent.com/u/52349321?v=4', 0),
(39, NULL, NULL, '', NULL, '2019-06-29 13:33:38.224846', 38, 0, NULL, NULL, NULL, 0),
(40, 'BVerge', 'Ventures', '', NULL, '2019-06-29 13:36:34.305203', 39, 0, NULL, NULL, 'https://lh4.googleusercontent.com/--nu_2kpXoO4/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3re-ddcktjkhBIldF8FwhfL-YkH9Dw/photo.jpg', 0),
(41, '', '', '', NULL, '2019-06-29 13:37:34.304582', 40, 0, NULL, NULL, 'https://avatars3.githubusercontent.com/u/52351217?v=4', 0),
(42, NULL, NULL, '', NULL, '2019-06-29 14:06:18.966483', 41, 0, NULL, NULL, NULL, 0),
(43, NULL, NULL, '', NULL, '2019-06-29 14:18:48.433258', 42, 0, NULL, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile_advise_type`
--

CREATE TABLE `profiles_profile_advise_type` (
  `id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `advisor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles_profile_advise_type`
--

INSERT INTO `profiles_profile_advise_type` (`id`, `profile_id`, `advisor_id`) VALUES
(2, 6, 5),
(1, 21, 4),
(3, 21, 6),
(8, 21, 11),
(26, 21, 19),
(27, 21, 20),
(4, 23, 7),
(5, 24, 8),
(6, 24, 9),
(25, 28, 5),
(24, 28, 8),
(7, 28, 10),
(9, 28, 12),
(10, 28, 13),
(11, 28, 14),
(12, 28, 15),
(13, 28, 16),
(23, 28, 18),
(28, 28, 20),
(29, 28, 21),
(30, 32, 22);

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile_investors_type`
--

CREATE TABLE `profiles_profile_investors_type` (
  `id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `investor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile_just_advise`
--

CREATE TABLE `profiles_profile_just_advise` (
  `id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `advisor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles_profile_just_advise`
--

INSERT INTO `profiles_profile_just_advise` (`id`, `profile_id`, `advisor_id`) VALUES
(2, 28, 19);

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile_just_invest`
--

CREATE TABLE `profiles_profile_just_invest` (
  `id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `investor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile_just_sell`
--

CREATE TABLE `profiles_profile_just_sell` (
  `id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `seller1_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles_profile_just_sell`
--

INSERT INTO `profiles_profile_just_sell` (`id`, `profile_id`, `seller1_id`) VALUES
(1, 24, 48),
(3, 32, 69);

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile_sell_type`
--

CREATE TABLE `profiles_profile_sell_type` (
  `id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `seller1_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles_profile_sell_type`
--

INSERT INTO `profiles_profile_sell_type` (`id`, `profile_id`, `seller1_id`) VALUES
(1, 6, 47),
(7, 21, 53),
(8, 21, 54),
(9, 21, 55),
(10, 21, 56),
(2, 24, 48),
(3, 24, 49),
(4, 24, 50),
(5, 24, 51),
(6, 24, 52),
(28, 28, 48),
(16, 28, 51),
(11, 28, 57),
(17, 28, 58),
(18, 28, 60),
(23, 28, 64),
(27, 28, 65),
(32, 32, 49),
(30, 32, 60),
(19, 32, 61),
(20, 32, 62),
(22, 32, 63),
(24, 32, 65),
(25, 32, 66),
(26, 32, 67),
(37, 32, 69),
(33, 33, 69),
(34, 33, 70);

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile_user_advise`
--

CREATE TABLE `profiles_profile_user_advise` (
  `id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `advise_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles_profile_user_advise`
--

INSERT INTO `profiles_profile_user_advise` (`id`, `profile_id`, `advise_id`) VALUES
(3, 21, 3),
(11, 21, 11),
(12, 21, 12),
(1, 24, 1),
(2, 28, 2),
(4, 28, 4),
(5, 28, 5),
(6, 28, 6),
(7, 28, 7),
(8, 28, 8),
(9, 28, 9),
(10, 28, 10),
(13, 28, 13),
(14, 32, 14);

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile_user_invest`
--

CREATE TABLE `profiles_profile_user_invest` (
  `id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `invest_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles_profile_user_invest`
--

INSERT INTO `profiles_profile_user_invest` (`id`, `profile_id`, `invest_id`) VALUES
(1, 24, 1),
(2, 28, 2),
(4, 28, 4),
(3, 32, 3);

-- --------------------------------------------------------

--
-- Table structure for table `profiles_profile_user_sell`
--

CREATE TABLE `profiles_profile_user_sell` (
  `id` int(11) NOT NULL,
  `profile_id` int(11) NOT NULL,
  `sell_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `profiles_profile_user_sell`
--

INSERT INTO `profiles_profile_user_sell` (`id`, `profile_id`, `sell_id`) VALUES
(1, 6, 1),
(7, 21, 7),
(8, 21, 8),
(9, 21, 9),
(10, 21, 10),
(2, 24, 2),
(3, 24, 3),
(4, 24, 4),
(5, 24, 5),
(6, 24, 6),
(11, 28, 11),
(12, 28, 12),
(13, 28, 13),
(14, 28, 14),
(18, 28, 18),
(15, 32, 15),
(16, 32, 16),
(17, 32, 17),
(19, 32, 19),
(20, 32, 20),
(21, 32, 21),
(22, 33, 22),
(23, 33, 23);

-- --------------------------------------------------------

--
-- Table structure for table `seller1_ablumfiles`
--

CREATE TABLE `seller1_ablumfiles` (
  `id` int(11) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_ablumfiles`
--

INSERT INTO `seller1_ablumfiles` (`id`, `file_name`, `seller_id`) VALUES
(37, 'butterfly.jpg', 42),
(38, 'image1.jpg', 42),
(39, 'image1.jpg', 45),
(40, 'butterfly.jpg', 45),
(41, 'Screenshot_1.png', 6),
(42, 'Screenshot_1_0nnCv6p.png', 6),
(43, 'Screenshot_1_vIEnrcU.png', 6),
(44, 'Screenshot_1.png', 7),
(45, '20170524_083314.jpg', 18),
(46, '20170524_083642.jpg', 18),
(47, '20170524_132402.jpg', 18),
(48, '20170524_132816.jpg', 18),
(49, '20170524_132828.jpg', 18),
(50, '20170525_072331.jpg', 18),
(51, '20170524_083314.jpg', 19),
(52, '20170524_083642.jpg', 19);

-- --------------------------------------------------------

--
-- Table structure for table `seller1_raiseloan`
--

CREATE TABLE `seller1_raiseloan` (
  `loan_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `about_business` longtext NOT NULL,
  `loan_amount` int(11) NOT NULL,
  `sought_interest` decimal(30,20) NOT NULL,
  `year_established` int(11) NOT NULL,
  `reason_loan` longtext NOT NULL,
  `website` varchar(500) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_raiseloan`
--

INSERT INTO `seller1_raiseloan` (`loan_id`, `type`, `about_business`, `loan_amount`, `sought_interest`, `year_established`, `reason_loan`, `website`, `seller_id`) VALUES
(1, 'Loan', 'mnsdvs s vs vs v', 64, '465.00000000000000000000', 2009, 'jsv svsnv v', NULL, 41),
(2, 'Loan', 'sdjns vs dvsmdv', 75445, '45.00000000000000000000', 5, 'sjbds dv ks vs dv n', NULL, 62);

-- --------------------------------------------------------

--
-- Table structure for table `seller1_revenuemodel`
--

CREATE TABLE `seller1_revenuemodel` (
  `revenue_id` int(11) NOT NULL,
  `rev_year` int(11) NOT NULL,
  `year_16` int(11) NOT NULL,
  `year_15` int(11) NOT NULL,
  `year_14` int(11) NOT NULL,
  `year_13` int(11) NOT NULL,
  `year_17` int(11) NOT NULL,
  `no_emp` int(11) NOT NULL,
  `cp_emp` int(11) NOT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_revenuemodel`
--

INSERT INTO `seller1_revenuemodel` (`revenue_id`, `rev_year`, `year_16`, `year_15`, `year_14`, `year_13`, `year_17`, `no_emp`, `cp_emp`, `seller_id`) VALUES
(1, 8, 0, 0, 0, 0, 3, 3, 12344, 25),
(2, 4, 0, 0, 0, 0, 4, 6, 3, 26),
(3, 4, 0, 0, 0, 0, 4, 6, 3, 27),
(4, 4, 0, 0, 0, 0, 4, 6, 3, 28),
(5, 4, 0, 0, 0, 0, 4, 6, 3, 29),
(6, 4, 0, 0, 0, 0, 4, 6, 3, 30),
(7, 4, 0, 0, 0, 0, 4, 6, 3, 31),
(8, 4, 0, 0, 0, 0, 4, 6, 3, 32),
(9, 4, 0, 0, 0, 0, 4, 6, 3, 33),
(10, 4, 0, 0, 0, 0, 4, 6, 3, 34),
(11, 645, 0, 0, 0, 0, 64, 546, 654646, 35),
(12, 64, 0, 0, 0, 0, 5, 6, 5, 36),
(13, 465, 0, 0, 0, 0, 645, 45, 465, 37),
(14, 54, 0, 0, 0, 0, 5, 64545, 645, 38),
(15, 54, 0, 0, 0, 0, 5, 645, 645, 39),
(16, 64, 0, 0, 0, 0, 5, 645, 65, 40),
(17, 645, 0, 0, 0, 0, 65, 645, 5, 41),
(18, 54, 0, 0, 0, 0, 645, 54, 64, 42),
(19, 6451, 0, 0, 0, 0, 6541, 65, 56312, 47),
(20, 8645, 0, 0, 0, 0, 421, 413, 754, 48),
(21, 8465, 0, 0, 0, 0, 7542, 852, 748, 49),
(22, 641, 0, 0, 0, 0, 12132, 54112, 54132, 50),
(23, 6855645, 0, 0, 0, 0, 556656, 54456, 76854, 51),
(24, 3512325, 0, 0, 0, 0, 6456, 47845, 78456, 52),
(25, 68545654, 0, 0, 0, 0, 8754, 6865, 655363, 53),
(26, 68545654, 0, 0, 0, 0, 8754, 6865, 655363, 54),
(27, 546519, 0, 0, 0, 0, 6554, 5454, 4656535, 55),
(28, 64512665, 0, 0, 0, 0, 554, 541212, 5441, 56),
(29, 546, 0, 0, 0, 0, 5542, 5542, 542, 57),
(30, 454561, 0, 0, 0, 0, 75434, 12, 1212, 60),
(31, 458126, 0, 0, 0, 0, 7856, 78, 45, 61),
(32, 455621, 0, 0, 0, 0, 7856, 52, 7896, 62),
(33, 5416544, 0, 0, 0, 0, 5415, 6455, 1545, 69),
(34, 65, 0, 0, 0, 0, 54654, 4556, 455, 70);

-- --------------------------------------------------------

--
-- Table structure for table `seller1_sellapp`
--

CREATE TABLE `seller1_sellapp` (
  `app_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `about` longtext NOT NULL,
  `startup_type` varchar(255) NOT NULL,
  `email_app` varchar(255) NOT NULL,
  `asking_price` int(11) NOT NULL,
  `website` varchar(500) DEFAULT NULL,
  `monitization_method` varchar(255) NOT NULL,
  `average_monthly_revenue` int(11) NOT NULL,
  `average_monthly_expense` int(11) NOT NULL,
  `date_established` date NOT NULL,
  `average_monthly_downloads` int(11) NOT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_sellapp`
--

INSERT INTO `seller1_sellapp` (`app_id`, `type`, `about`, `startup_type`, `email_app`, `asking_price`, `website`, `monitization_method`, `average_monthly_revenue`, `average_monthly_expense`, `date_established`, `average_monthly_downloads`, `seller_id`) VALUES
(1, 'Application', 'ndca c acjka', '', '', 51, NULL, 'Category5', 81, 9841, '2019-05-15', 6841, 43),
(2, 'Application', 'ndca c acjka', '', '', 51, NULL, 'Category1', 81, 9841, '2019-05-15', 6841, 44),
(3, 'Application', 'sb fmn nm mns yjtyty', '', 'dv@dv.com', 65, 'http://www.google.com', 'Category5', 655, 5618, '2019-05-08', 6518, 46),
(4, 'Application', 'akhcbad cakdh ad adhk dc', '', '', 755452, NULL, 'Category1', 223, 75659, '2019-06-14', 5407, 59),
(5, 'Application', 'ajsc ascbsc na scanbcs  asc', 'Application', '', 54615, 'http://www.sony.com', 'Category2', 54135, 5351, '2019-06-21', 35155, 64),
(6, 'Application', 'jhv ssb v', 'Application', '', 215, 'http://www.sony.com', 'Category1', 4651, 6458, '2019-06-13', 6548, 65),
(7, 'Application', 'asjca sas casc asc asc', 'Application', '', 5215, NULL, 'Category1', 541, 45, '2019-06-13', 53145, 66),
(8, 'Application', 'asgdva cac an ca scb', 'Website', '', 513, 'http://www.sony.com', 'Category3', 68541, 64513, '2019-06-20', 215, 67);

-- --------------------------------------------------------

--
-- Table structure for table `seller1_sellasset`
--

CREATE TABLE `seller1_sellasset` (
  `asset_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `asset_type` varchar(255) NOT NULL,
  `about_asset` longtext NOT NULL,
  `asking_price` int(11) NOT NULL,
  `purchase_price` int(11) NOT NULL,
  `purchase_year` int(11) NOT NULL,
  `reason_selling` longtext NOT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_sellasset`
--

INSERT INTO `seller1_sellasset` (`asset_id`, `type`, `asset_type`, `about_asset`, `asking_price`, `purchase_price`, `purchase_year`, `reason_selling`, `seller_id`) VALUES
(1, 'Asset', 'Business Seller', 'sf sh svs v', 45645, 546, 2019, 'mdsb sbv sdjk', 38),
(2, 'Asset', 'Asset Type', 'sf sh svs v', 45645, 546, 2002, 'mdsb sbv sdjk', 39),
(3, 'Asset', 'Business Seller', 'kjdf adb adn a', 51, 651, 2003, 'asfadf adfa df adfa f adfa', 47),
(4, 'Asset', 'Business Seller', 'dsb sdhsdshv sjv shfv vsj', 68512, 8764, 2017, 'ghdv dcjhcad cad h', 48),
(5, 'Asset', 'Asset Type', 'sjkdvs vns v sn vsn vsn vns v', 985, 7845, 2019, 'skdvs vnk vs sn sn sn d', 49);

-- --------------------------------------------------------

--
-- Table structure for table `seller1_sellbusiness`
--

CREATE TABLE `seller1_sellbusiness` (
  `business_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `about` longtext NOT NULL,
  `asking_price` int(11) NOT NULL,
  `year_established` int(11) NOT NULL,
  `reason_selling` longtext NOT NULL,
  `website` varchar(500) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_sellbusiness`
--

INSERT INTO `seller1_sellbusiness` (`business_id`, `type`, `about`, `asking_price`, `year_established`, `reason_selling`, `website`, `seller_id`) VALUES
(1, 'Business', 'fhvb jbfv jfv', 783, 1997, 'afnhnv jfv vfn v', NULL, 11),
(2, 'Business', 'fhvb jbfv jfv', 783, 1997, 'afnhnv jfv vfn v', NULL, 12),
(3, 'Business', 'fhvb jbfv jfv', 783, 1997, 'afnhnv jfv vfn v', NULL, 13),
(4, 'Business', 'fhvb jbfv jfv', 783, 1997, 'afnhnv jfv vfn v', NULL, 14),
(5, 'Business', 'fhvb jbfv jfv', 783, 1997, 'afnhnv jfv vfn v', NULL, 15),
(9, 'Business', 'hdvc dbc amdc', 8458, 1997, 'aschb anc anc', 'http://www.sony.com', NULL),
(10, 'Business', 'aejgs sbdf smef', 54, 5, 'aef aefa fe', NULL, NULL),
(11, 'Business', 'fgsf  fbsfb dfb', 622, 897, 'adc sdv sv', NULL, NULL),
(12, 'Business', 'ajbdf jdf j j', 6, 458, 'avhd ajbhdf hjsdv', NULL, 23),
(13, 'Business', 'ajbdf jdf j j', 64, 45, 'avhd ajbhdf h jsdv', NULL, 24),
(14, 'Business', 'jhdf djfv dfv', 59, 6, 'jkfv fv mfv', 'http://www.sony.com', 25),
(15, 'Business', 'gv jh bhj', 546, 645, 'g bbhj bh', NULL, 26),
(16, 'Business', 'gv jh bhj', 546, 645, 'g bbhj bh', NULL, 27),
(17, 'Business', 'gv jh bhj', 546, 645, 'g bbhj bh', NULL, 28),
(18, 'Business', 'gv jh bhj', 546, 645, 'g bbhj bh', NULL, 29),
(19, 'Business', 'gv jh bhj', 546, 645, 'g bbhj bh', NULL, 30),
(20, 'Business', 'gv jh bhj', 546, 645, 'g bbhj bh', NULL, 31),
(21, 'Business', 'gv jh bhj', 546, 645, 'g bbhj bh', NULL, 32),
(22, 'Business', 'gv jh bhj', 546, 645, 'g bbhj bh', NULL, 33),
(23, 'Business', 'gv jh bhj', 546, 645, 'g bbhj bh', NULL, 34),
(24, 'Business', 'Okk jsdv jh h', 6446, 66, '565 kjdv kfjv ffve', 'http://www.sony.com', 35),
(25, 'Business', 'adcjka adma dcad', 466, 5446, 'adjbk dsbd sdjba', NULL, 36),
(26, 'Business', 'jbkfvm f v fv af vaef v', 546, 2009, 'hfvb fvh eve efv bv', NULL, 37),
(27, 'Business', 'shdvs vsvsjv s vskhdv sv skhdv sdv', 87516538, 2006, 'kudv svjhsv sdvjsdvsdv svn', NULL, 51),
(28, 'Business', 'hsdbvhskd sdjhd sdvkshdv sdkvsdv', 6851, 2010, 'jkbsd cshs vsvshkv s vskv', NULL, 52),
(29, 'Business', 'acva dcambc ambc ad cacd', 674, 2017, 'jhvc acja cab cab ca ckack ac', NULL, 53),
(30, 'Business', 'acva dcambc ambc ad cacd', 674, 2017, 'jhvc acja cab cab ca ckack ac', NULL, 54),
(31, 'Business', 'svsmvsvsv sv m sdvmsdv smdv', 6453, 2002, 'sdmcsd scm sdcmsdm s dms dc', NULL, 55),
(32, 'Business', 'sjbs dsk s vs vsnd vsnkv', 6515, 2016, 'hjcbs cs dskd sk skdv', NULL, 56),
(33, 'Business', 'jkc dcsdc s csd sd', 654, 2014, 'jksd ssd s s skd c', NULL, 57),
(34, 'Business', 'nsd vsdvs vs dvs dvks dvks vk sdv', 6515, 2010, 'js vsv sv sd vsv sd vs dv', NULL, 68),
(35, 'Business', 'nsd vsdvs vs dvs dvks dvks vk sdv', 648, 2008, 'js vsv sv sd vsv sdvs dv', NULL, 69),
(36, 'Business', 'sndv svmnsd vnsd v', 5339, 2016, 'hjdb j j d hkd', NULL, 70);

-- --------------------------------------------------------

--
-- Table structure for table `seller1_sellequity`
--

CREATE TABLE `seller1_sellequity` (
  `equity_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `about_business` longtext NOT NULL,
  `stake` decimal(30,20) NOT NULL,
  `asking_price` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `reason` longtext NOT NULL,
  `website` varchar(500) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_sellequity`
--

INSERT INTO `seller1_sellequity` (`equity_id`, `type`, `about_business`, `stake`, `asking_price`, `year`, `reason`, `website`, `seller_id`) VALUES
(1, 'Equity', 'jhb jkd w w', '546.00000000000000000000', 54, 1999, 'dn sn vns fv', NULL, 40),
(2, 'Equity', 'sdbj sdvs vmsnv  svdadjkbcd', '7845.00000000000000000000', 784, 2017, 'f f f f f f', NULL, 60),
(3, 'Equity', 'jhdbc d d dn sds dsndv msndv s vnd vsdv  dv', '25.00000000000000000000', 852, 2014, 'jhdc sdv svb sdvn s vsdmn dmvsmvsdmv  mdvmvmdv', NULL, 61);

-- --------------------------------------------------------

--
-- Table structure for table `seller1_seller1`
--

CREATE TABLE `seller1_seller1` (
  `first_name` varchar(255) NOT NULL,
  `middle_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `country_code_primary` varchar(255) NOT NULL,
  `phone_number_primary` varchar(10) NOT NULL,
  `email_adress` varchar(254) NOT NULL,
  `about_seller` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `completed` int(11) NOT NULL,
  `category1` varchar(255) NOT NULL,
  `category2` varchar(255) NOT NULL,
  `business_type` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `adress` longtext NOT NULL,
  `lat` decimal(22,16) DEFAULT NULL,
  `lngt` decimal(22,16) DEFAULT NULL,
  `address_line` varchar(255) NOT NULL,
  `album_id` int(11) DEFAULT NULL,
  `city` varchar(256) DEFAULT NULL,
  `country` varchar(256) DEFAULT NULL,
  `region` varchar(256) DEFAULT NULL,
  `business_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_seller1`
--

INSERT INTO `seller1_seller1` (`first_name`, `middle_name`, `last_name`, `country_code_primary`, `phone_number_primary`, `email_adress`, `about_seller`, `created_at`, `completed`, `category1`, `category2`, `business_type`, `name`, `title`, `adress`, `lat`, `lngt`, `address_line`, `album_id`, `city`, `country`, `region`, `business_id`, `type`) VALUES
('', '', '', 'Afghanistan (+93)', '0', '', '0', '2019-05-02 23:18:02.201902', 0, 'Automotive', 'volvo', 'Sole Proprietorship/trader', '', '', '', NULL, NULL, '', NULL, NULL, NULL, NULL, 1, NULL),
('', '', '', 'Afghanistan (+93)', '0', '', '0', '2019-05-02 23:18:22.913266', 0, 'Automotive', 'volvo', 'Sole Proprietorship/trader', '', '', '', NULL, NULL, '', NULL, NULL, NULL, NULL, 2, NULL),
('', '', '', 'Afghanistan (+93)', '0', '', '0', '2019-05-03 00:06:31.678950', 0, 'Automotive', 'volvo', 'Sole Proprietorship/trader', '', '', '', NULL, NULL, '', NULL, NULL, NULL, NULL, 3, NULL),
('', '', '', 'Afghanistan (+93)', '0', '', '0', '2019-05-03 00:14:37.547053', 0, 'Automotive', 'volvo', 'Sole Proprietorship/trader', '', '', '', NULL, NULL, '', NULL, NULL, NULL, NULL, 4, NULL),
('PRITHVIRAJ', 'm', 'RADHAKRISHNAN', 'Afghanistan (+93)', '3323', 'prithviphysics1992@gmail.com', '0', '2019-05-03 00:18:52.229727', 0, 'Automotive', 'volvo', 'Sole Proprietorship/trader', '', '', '', NULL, NULL, '', NULL, NULL, NULL, NULL, 5, NULL),
('dx', 'nv', 'v', 'India (+91)', '9167330324', 'sdfg@dfg.com', '0', '2019-05-07 01:39:07.943875', 0, 'Retail', 'Consumer', 'C Corporation', 'Prediction 1', 'Custom Popups', '', NULL, NULL, 'Unnamed Road, Bhim Nagar, Andheri East, Mumbai, Maharashtra 400053, India', NULL, NULL, NULL, NULL, 6, NULL),
('dasd', 'sdcf', 'dv', 'India (+91)', '9167330324', 'ad@gmail.com', '0', '2019-05-07 01:52:27.579007', 0, 'Realestate&Construction', 'Real Estate (General/Diversified)', 'Limited Liability Company (LLC)', 'nd fb', 'svbdfv f nv', '', '19.0976681000000000', '72.9080361000000000', 'D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 7, 'Business'),
('dasd', 'sdcf', 'dv', 'India (+91)', '9167330324', 'ad@gmail.com', '0', '2019-05-07 01:57:34.147695', 0, 'Realestate&Construction', 'Real Estate (General/Diversified)', 'Limited Liability Company (LLC)', 'nd fb', 'svbdfv f nv', '', '19.0976681000000000', '72.9080361000000000', 'D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 8, 'Business'),
('dasd', 'sdcf', 'dv', 'India (+91)', '9167330324', 'ad@gmail.com', '0', '2019-05-07 01:57:38.788406', 0, 'Realestate&Construction', 'Real Estate (General/Diversified)', 'Limited Liability Company (LLC)', 'nd fb', 'svbdfv f nv', '', '19.0976681000000000', '72.9080361000000000', 'D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 9, 'Business'),
('dasd', 'sdcf', 'dv', 'India (+91)', '9167330324', 'ad@gmail.com', '0', '2019-05-07 01:57:53.686717', 0, 'Realestate&Construction', 'Real Estate (General/Diversified)', 'Limited Liability Company (LLC)', 'nd fb', 'svbdfv f nv', '', '19.0976681000000000', '72.9080361000000000', 'D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 10, 'Business'),
('dasd', 'sdcf', 'dv', 'India (+91)', '9167330324', 'ad@gmail.com', '0', '2019-05-07 01:59:56.847152', 0, 'Realestate&Construction', 'Real Estate (General/Diversified)', 'Limited Liability Company (LLC)', 'nd fb', 'svbdfv f nv', '', '19.0976681000000000', '72.9080361000000000', 'D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 11, 'Business'),
('dasd', 'sdcf', 'dv', 'India (+91)', '9167330324', 'ad@gmail.com', '0', '2019-05-07 02:14:45.094324', 0, 'Realestate&Construction', 'Real Estate (General/Diversified)', 'Limited Liability Company (LLC)', 'nd fb', 'svbdfv f nv', '', '19.0976681000000000', '72.9080361000000000', 'D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 12, 'Business'),
('dasd', 'sdcf', 'dv', 'India (+91)', '9167330324', 'ad@gmail.com', '0', '2019-05-07 02:22:08.440549', 0, 'Realestate&Construction', 'Real Estate (General/Diversified)', 'Limited Liability Company (LLC)', 'nd fb', 'svbdfv f nv', '', '19.0976681000000000', '72.9080361000000000', 'D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 13, 'Business'),
('dasd', 'sdcf', 'dv', 'India (+91)', '9167330324', 'ad@gmail.com', '0', '2019-05-07 02:24:25.871074', 0, 'Realestate&Construction', 'Real Estate (General/Diversified)', 'Limited Liability Company (LLC)', 'nd fb', 'svbdfv f nv', '', '19.0976681000000000', '72.9080361000000000', 'D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 14, 'Business'),
('dasd', 'sdcf', 'dv', 'India (+91)', '9167330324', 'ad@gmail.com', '0', '2019-05-07 02:28:49.941054', 0, 'Realestate&Construction', 'Real Estate (General/Diversified)', 'Limited Liability Company (LLC)', 'nd fb', 'svbdfv f nv', '', '19.0976681000000000', '72.9080361000000000', 'D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 15, 'Business'),
('Prajwal', 'Subhash', 'Barapatre', 'Afghanistan (+93)', '9167330324', 'prajwalbarapatre13@gmail.com', '0', '2019-05-08 00:34:26.213667', 0, 'Automotive', 'volvo', 'Sole Proprietorship/trader', 'bsdvsdv', 'sdhsdv', '', '19.1127552000000000', '72.8694783999999300', 'Unnamed Road, Bhim Nagar, Andheri East, Mumbai, Maharashtra 400053, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 19, NULL),
('asdff', 'dsvbn', 'xzcvvb', 'Afghanistan (+93)', '9167330324', 'prajwal@gmail.com', '0', '2019-05-08 10:32:42.878628', 0, 'Automotive', 'volvo', 'Sole Proprietorship/trader', 'xcvbb', 'asddgf', '', '19.0956996000000030', '72.9086391999999300', '11, Jagdusha Nagar Rd, D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra 400086, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 20, NULL),
('asdff', 'dsvbn', 'xzcvvb', 'India (+91)', '9167330324', 'prajwal@gmail.com', '0', '2019-05-08 10:38:47.219830', 0, 'Financial Services', 'Lending', 'Municipality', 'xcvbb', 'asddgf', '', '19.0956996000000030', '72.9086391999999300', '11, Jagdusha Nagar Rd, D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra 400086, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 21, 'Business'),
('jh', 'jh', 'jhds', 'Afghanistan (+93)', '45', 's@s.com', '0', '2019-05-08 12:36:28.775097', 0, 'Automotive', 'volvo', 'Sole Proprietorship/trader', 'dgh', 'gb', '', '19.1119360000000000', '72.8571904000000400', 'Hindustan Unilever Ltd., Parshiwada, Chakala, Andheri East, Mumbai, Maharashtra 400053, India', 9, 'Mumbai Suburban', 'India', 'Maharashtra', 22, NULL),
('hjadf', 'nbaf', 'jhbd', 'Afghanistan (+93)', '645', 'jh@hd.com', '0', '2019-05-24 21:06:58.626901', 0, 'Realestate&Construction', 'Real Estate (Development)', 'Municipality', 'jhd', 'ah hab h hbn', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', 13, 'Mumbai Suburban', 'India', 'Maharashtra', 23, 'Business'),
('hjadf', 'nbaf', 'jhbd', 'Afghanistan (+93)', '64', 'jh@hd.com', '0', '2019-05-24 21:08:55.912553', 0, 'Realestate&Construction', '', 'Municipality', 'jhd', 'ah hab h hbn c', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', 13, 'Mumbai Suburban', 'India', 'Maharashtra', 24, 'Business'),
('Ha Ha Hi', 'Hu HU', 'akjsb', 'Afghanistan (+93)', '56', 'adh@adbh.com', 'Owner', '2019-05-24 21:53:18.127435', 0, '', '', 'Co-orperative', 'ajdsf jdb', 'ajdbf adfjds aadmn', '', '18.2610195813591430', '74.4857703062500600', 'Sonvadisupe, Maharashtra, India', 16, 'Pune', 'India', 'Maharashtra', 25, 'Business'),
('gf jhhb  ghb', 'jh', 'nv', 'Afghanistan (+93)', '65', 'f@f.com', 'Broker', '2019-05-24 23:13:48.205295', 0, 'Realestate&Construction', 'Real Estate (Development)', 'Municipality', 'gh', 'gh g hg', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 26, 'Business'),
('gf jhhb  ghb', 'jh', 'nv', 'Afghanistan (+93)', '65', 'f@f.com', 'Broker', '2019-05-24 23:24:34.177372', 0, 'Realestate&Construction', 'Real Estate (Development)', 'Municipality', 'gh', 'gh g hg', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 27, 'Business'),
('gf jhhb  ghb', 'jh', 'nv', 'Afghanistan (+93)', '65', 'f@f.com', 'Broker', '2019-05-24 23:28:45.960784', 0, 'Realestate&Construction', 'Real Estate (Development)', 'Municipality', 'gh', 'gh g hg', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 28, 'Business'),
('gf jhhb  ghb', 'jh', 'nv', 'Afghanistan (+93)', '65', 'f@f.com', 'Broker', '2019-05-24 23:31:33.119002', 0, 'Realestate&Construction', 'Real Estate (Development)', 'Municipality', 'gh', 'gh g hg', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 29, 'Business'),
('gf jhhb  ghb', 'jh', 'nv', 'Afghanistan (+93)', '65', 'f@f.com', 'Broker', '2019-05-24 23:33:33.927732', 0, 'Realestate&Construction', 'Real Estate (Development)', 'Municipality', 'gh', 'gh g hg', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 30, 'Business'),
('gf jhhb  ghb', 'jh', 'nv', 'Afghanistan (+93)', '65', 'f@f.com', 'Broker', '2019-05-24 23:36:45.522145', 0, 'Realestate&Construction', 'Real Estate (Development)', 'Municipality', 'gh', 'gh g hg', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 31, 'Business'),
('gf jhhb  ghb', 'jh', 'nv', 'Afghanistan (+93)', '65', 'f@f.com', 'Broker', '2019-05-24 23:43:06.334610', 0, 'Realestate&Construction', 'Real Estate (Development)', 'Municipality', 'gh', 'gh g hg', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 32, 'Business'),
('gf jhhb  ghb', 'jh', 'nv', 'Afghanistan (+93)', '65', 'f@f.com', 'Broker', '2019-05-24 23:44:47.579810', 0, 'Realestate&Construction', 'Real Estate (Development)', 'Municipality', 'gh', 'gh g hg', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 33, 'Business'),
('gf jhhb  ghb', 'jh', 'nv', 'Afghanistan (+93)', '65', 'f@f.com', 'Broker', '2019-05-24 23:47:46.160795', 0, 'Emerging Technology', 'Quantum Computing', 'Municipality', 'gh', 'gh g hg', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', NULL, 'Mumbai Suburban', 'India', 'Maharashtra', 34, 'Business'),
('rgwg', 'wfgwg', 'sffeb', 'Armenia(+374)', '5565', 'sfgdsgb@sdf.com', 'Broker', '2019-05-25 11:54:35.720017', 0, 'Social Media', 'Social Media', 'Limited Liability Limited Partnership (LLLP)', 'Hmm', 'Something bad ok', '', NULL, NULL, 'Mumbai ajdf sdjf', 36, NULL, NULL, NULL, 35, 'Business'),
('Something', 'sfsf', 'ff', 'Argentina (+54)', '4652', 'adf@df.com', 'Owner', '2019-05-25 13:23:41.252956', 0, 'Emerging Technology', 'Internet of Things', 'Sole Proprietorship/trader', 'bfgsdfg sfng', 'adf adbf dsjs', '', '19.0945328000000000', '72.9165150999999700', '274, LBS Rd, Nityanand Nagar, Ghatkopar West, Mumbai, Maharashtra 400086, India', 37, 'Mumbai Suburban', 'India', 'Maharashtra', 36, 'Business'),
('jvh', 'b', 'v', 'Angola(+244)', '54', 'cb@fgcc.vh', 'Owner', '2019-05-25 20:01:03.143642', 0, 'Automotive', 'Auto & Truck', 'Sole Proprietorship/trader', 'hbjfvhafvava', 'ebv efjv efv evf jkfv', '', NULL, NULL, 'jbkvafv mnf v', 58, NULL, NULL, NULL, 37, 'Business'),
('adhb', 'badv', 'hbjadva', 'Afghanistan (+93)', '546', 'vad@gs.com', 'Owner', '2019-05-26 07:37:08.670398', 0, 'IT', 'Network Hardware', 'Sole Proprietorship/trader', 'bhadc', 'gasv ahg acgh ahgc a', '', NULL, NULL, 'kj hd', 60, NULL, NULL, NULL, 38, 'Asset'),
('adhb', 'badv', 'hbjadva', 'Afghanistan (+93)', '546', 'vad@gs.com', 'Owner', '2019-05-26 07:41:48.528721', 0, 'IT', 'Network Hardware', 'Sole Proprietorship/trader', 'bhadc', 'gasv ahg acgh ahgc a', '', NULL, NULL, 'kj hd', 60, NULL, NULL, NULL, 39, 'Asset'),
('skjdbv', 'sfv', 'kjnsfv', 'Uganda(+256)', '546', 'sdv@adcv.com', 'Broker', '2019-05-26 10:27:15.236538', 0, 'Automotive', 'Auto & Truck', 'Trust', ',svnsv', 'kdvb djbv ssv sv sv', '', NULL, NULL, 'jsbv', 64, NULL, NULL, NULL, 40, 'Equity'),
('sjbdv', 'kjbdv', 'jsbv', 'Afghanistan (+93)', '645', 'ach@avgsc.sdd', 'Owner', '2019-05-26 11:09:24.183589', 0, 'Non-classifiable Establishments', 'Innovation Management', 'Private Limited', 'smnv', 'dbhc sd sdvns dv sddv', '', NULL, NULL, 'sdn v', 65, NULL, NULL, NULL, 41, 'Loan'),
('sfvb', 'hbdv', 'jbkdv', 'Afghanistan (+93)', '645', 'gdasv@acgh.cad', 'Owner', '2019-05-26 11:54:26.078166', 0, 'Agriculture', 'Farming/Agriculture', 'Sole Proprietorship/trader', 'ksdv', 'ajfd ad va vad d v', '', NULL, NULL, 'adjvb', 67, NULL, NULL, NULL, 42, 'Startup'),
('mad c', ',m dc', 'm dv', 'Afghanistan (+93)', '6451', 'ajcv@asc.com', 'Owner', '2019-05-26 15:44:38.773014', 0, 'Retail', 'Retail (Building Supply)', '', 'something', 'lkndca can an c mnc a', '', NULL, NULL, 'something', 71, NULL, NULL, NULL, 43, 'Application'),
('mad c', ',m dc', 'm dv', 'Afghanistan (+93)', '6451', 'ajcv@asc.com', 'Owner', '2019-05-26 15:55:43.761819', 0, 'Retail', 'Retail (Building Supply)', '', 'something', 'lkndca can an c mnc a', '', NULL, NULL, 'something', 71, NULL, NULL, NULL, 44, 'Application'),
('jd', 'kbdv', 'admv', 'Australia(+61)', '815', 'ahcv@dc.com', 'Owner', '2019-05-26 18:37:46.404680', 0, '', '', '', 'something', 'anbc ba scjac ac kadc', '', NULL, NULL, 'something', 72, NULL, NULL, NULL, 45, 'Ipcode'),
('jhdf', 'khadbv', 'idubv', 'India (+91)', '65132', 'ad@adv.com', 'Owner', '2019-05-27 15:38:06.406661', 0, 'Non-classifiable Establishments', 'Innovation Management', '', 'something', 'nbdfsjf vsjv sf sfv sfv d', '', NULL, NULL, 'something', 81, NULL, NULL, NULL, 46, 'Application'),
('Prithvi Raj', 'sdhvsfv', 'skjbv', 'India (+91)', '9167330324', 'dug@aadv.com', 'Owner', '2019-05-31 14:11:50.474360', 0, 'Social Media', 'Blogging Platforms', 'Public Limited', 'dhf djsds dsjdh', 'agf djdd vsdjvsd vsdh fa', '', '19.1143936000000000', '72.8817664000000600', 'Gaondevi Talao, Marol Maroshi Rd, Sankasth Pada Welfare Society, Marol, Andheri East, Mumbai, Maharashtra 400059, India', 87, 'Mumbai Suburban', 'India', 'Maharashtra', 47, 'Asset'),
('jhfvbsfv', 'gdvadfjb', 'habfha', 'India (+91)', '754313515', 'dgva@axv.com', 'Broker', '2019-06-02 09:59:04.478867', 0, 'Manufacturing', 'Chemical (Basic)', 'Limited Partnership', 'jhvdcsjbdhbv', 'hgac csdc sdc sdg svj vdb', '', '19.0957380000000000', '72.9082120000000500', 'C-5, Golibar Rd, D.G.Q.A. Colony, Ghatkopar West, Mumbai, Maharashtra 400086, India', 92, 'Mumbai Suburban', 'India', 'Maharashtra', 48, 'Asset'),
('hsbv', 'jsv', 'shbbv', 'Afghanistan (+93)', '87546', 'sdbh@qwan.xjsdv', 'Owner', '2019-06-13 06:12:28.349276', 0, 'Manufacturing', 'Chemical (Basic)', 'S Corporation', 'skjvs dvs', 'n vs fvsn vsk v', 'jsv sdvkjsd sdvkj', '19.0708251999999900', '72.8842604999999800', '36, PT Marg, LIG Colony, Vinobha Bhave Nagar, Kurla West, Kurla, Mumbai, Maharashtra 400070, India', 94, 'Mumbai Suburban', 'India', 'Maharashtra', 49, 'Asset'),
('ahdcb', 'hjdv', 'kdvb', 'Afghanistan (+93)', '8751', 'djkv@sdv.com', 'Owner', '2019-06-13 10:06:27.651511', 0, 'Manufacturing', 'Building Materials', 'Sole Proprietorship/trader', 'skdjvsvsdv', 'jbdc sdcns dcs vs dv', '', '19.0708251999999900', '72.8842604999999800', '36, PT Marg, LIG Colony, Vinobha Bhave Nagar, Kurla West, Kurla, Mumbai, Maharashtra 400070, India', 96, 'Mumbai Suburban', 'India', 'Maharashtra', 50, 'Startup'),
('Prajwal', 'skdjvb', 'kjbv', 'Afghanistan (+93)', '681213', 'kd@dsvv.com', 'Broker', '2019-06-13 15:18:10.115976', 0, 'Manufacturing', 'Chemical (Basic)', 'Association', 'sdjkbvshvbskvbsvsjbdvsv sdmbv sdv sdv', 'jskdbv fvvfmfv sm vsmnfv smn v', '', '19.1209472000000000', '72.8866815999999700', 'B-9, KBM Compound, Military Road, Marol,  Andheri East, Mumbai, Maharashtra 400072, India', 97, NULL, 'India', 'Maharashtra', 51, 'Business'),
('sbfbv', 'skjbdv', 'kjsbdv', 'Afghanistan (+93)', '653', 'jhcb@sdv.com', 'Owner', '2019-06-13 15:20:58.069460', 0, 'Manufacturing', 'Chemical (Basic)', 'Limited Liability Partnership (LLP)', 'jdbskbjdv', 'hjdbc dcjhd cj dcdj cdj c', '', '19.1209472000000000', '72.8866815999999700', 'B-9, KBM Compound, Military Road, Marol, Andheri East, Mumbai, Maharashtra 400072, India', 98, NULL, 'India', 'Maharashtra', 52, 'Business'),
('jadcv', 'advc', 'mhdc', 'Afghanistan (+93)', '5451', 'havc@adv.com', 'Owner', '2019-06-15 06:11:33.514429', 0, 'Manufacturing', 'Chemical (Basic)', 'Association', 'sdmhc', 'khdcs d djvdjs djs dsdkdk', '', '19.1747385000000000', '72.9578329999999400', 'F-9A, Sarojini Naidu Rd, Siddharth Nagar, Mulund West, Mumbai, Maharashtra 400080, India', 99, 'Mumbai Suburban', 'India', 'Maharashtra', 53, 'Business'),
('jadcv', 'advc', 'mhdc', 'Afghanistan (+93)', '5451', 'havc@adv.com', 'Owner', '2019-06-15 06:18:42.934865', 0, 'Manufacturing', 'Chemical (Basic)', 'Association', 'sdmhc', 'khdcs d djvdjs djs dsdkdk', '', '19.1747385000000000', '72.9578329999999400', 'F-9A, Sarojini Naidu Rd, Siddharth Nagar, Mulund West, Mumbai, Maharashtra 400080, India', 99, 'Mumbai Suburban', 'India', 'Maharashtra', 54, 'Business'),
('dcfb', 'sfvsfv', 'sdvsdv', 'Afghanistan (+93)', '8609', 'sdv@edg.com', 'Owner', '2019-06-15 06:20:31.751660', 0, 'Manufacturing', 'Chemical (Basic)', 'Sole Proprietorship/trader', 'ads ds ds ds dv', 'sd sd sd sdc sdc', '', '19.1747385000000000', '72.9578329999999400', 'F-9A, Sarojini Naidu Rd, Siddharth Nagar, Mulund West, Mumbai, Maharashtra 400080, India', 100, 'Mumbai Suburban', 'India', 'Maharashtra', 55, 'Business'),
('kjb', 'khbv', 'kjbfv', 'Afghanistan (+93)', '64512', 'jhdv@dsv.com', 'Owner', '2019-06-15 08:10:29.500309', 0, 'Manufacturing', 'Chemical (Basic)', 'Sole Proprietorship/trader', 'dfjvhb', 'sfhvd fvdhf jhv dkfvd fv', '', '19.1651720908073140', '72.9574896772460300', '1, Nav Indraprastha CHS,  Mulund East, Mumbai, Maharashtra 400081, India', 101, 'Mumbai Suburban', 'India', 'Maharashtra', 56, 'Business'),
('jfv', 'kjhfv', 'jkfv', 'Afghanistan (+93)', '6538', 'sd@asc.com', 'Owner', '2019-06-17 09:50:03.252040', 0, 'Manufacturing', 'Chemical (Basic)', 'Sole Proprietorship/trader', 'sdsdvsdv', 'sdvsfv sv sv sv sv s', '', '19.0941244874027600', '72.8932545443340100', 'B1, Himalaya Society, Govind Nagar, Asalpha, Mumbai, Maharashtra 400084, India', 105, 'Mumbai Suburban', 'India', 'Maharashtra', 57, 'Business'),
('kjbv afvknaf v', 'skjbfvanfv', 'esfkjnd fbseknfv', 'Afghanistan (+93)', '874568', 'fdhvb@Avc.com', 'Owner', '2019-06-21 11:55:21.671740', 0, '', '', '', 'something', 'dsjvsd sjvsdv jsvsvs dv d sjdv', '', '19.0302330361992200', '73.0665827230468500', 'Plot No 21, Pravesh Marg, Sector 2, Kharghar, Navi Mumbai, Maharashtra 410210, India', 119, 'Raigad', 'India', 'Maharashtra', 58, 'Ipcode'),
('sdvbhss dvsdv', 'skjdbv', 'sdvkjb', 'Afghanistan (+93)', '7200', 'adv@Adv.com', 'Owner', '2019-06-21 11:58:08.819266', 0, 'Manufacturing', 'Chemical (Basic)', '', 'something', 'djc sdvsnv smnv s vs dv', '', '18.4528247470500230', '74.1464797762362200', 'Vitthal Wadi, Dalimb, Maharashtra 412202, India', 120, 'Pune', 'India', 'Maharashtra', 59, 'Application'),
('skjdvbsv', 'sdmnv', 'ksjdbv', 'Afghanistan (+93)', '851', 'dv@adv.com', 'Owner', '2019-06-22 07:57:46.423783', 0, 'Manufacturing', 'Chemical (Basic)', 'Association', 'sdvb sdmv', 'sdkjbs vdsm dvs vsm dv', '', '19.1201279999999980', '72.8866815999999700', '48, Raje Shivaji Nagar, Marol, Andheri East, Mumbai, Maharashtra 400072, India', 121, 'Mumbai Suburban', 'India', 'Maharashtra', 60, 'Equity'),
('djvb', 's,ndv', 'ksjdvn', 'Afghanistan (+93)', '5421', 'sdv@adv.com', 'Owner', '2019-06-22 08:04:02.793835', 0, 'Manufacturing', 'Chemical (Basic)', 'General Partnership', 'dcb ad jdd', 'jsbd sdvsnv s sdvsdvnsdvs dvsdv', '', '19.1201279999999980', '72.8866815999999700', '48, Raje Shivaji Nagar, Marol, Andheri East, Mumbai, Maharashtra 400072, India', 122, 'Mumbai Suburban', 'India', 'Maharashtra', 61, 'Equity'),
('dksjvb sdv', 'adjv', 'advn', 'Afghanistan (+93)', '78542', 'adv@asvc.com', 'Owner', '2019-06-22 08:41:29.444105', 0, 'Manufacturing', 'Chemical (Basic)', 'Association', 'sdnv s dvns dv', 'sjdbks dvs vs s dvk sdv', '', '19.1201279999999980', '72.8866815999999700', '48, Raje Shivaji Nagar, Marol, Andheri East, Mumbai, Maharashtra 400072, India', 123, 'Mumbai Suburban', 'India', 'Maharashtra', 62, 'Loan'),
('ajva', 'khbacv', 'havc', 'Afghanistan (+93)', '851', 'av@asc.com', 'Owner', '2019-06-22 11:18:07.582660', 0, 'Manufacturing', 'Chemical (Basic)', '', 'something', 'jhvs dvsdjb s nbsd  ndsmv sdv', '', '17.5145916338362080', '76.8054787562500700', 'Chinchansur, Karnataka, India', 127, 'Gulbarga', 'India', 'Karnataka', 63, 'Ipcode'),
('jdv', 'ambdc', 'ajbc', 'Afghanistan (+93)', '5841', 'acv@adv.com', 'Owner', '2019-06-22 11:41:59.558196', 0, 'Manufacturing', 'Chemical (Basic)', '', 'something', 'ahgscva sa scjascscsjc asca c asc', '', '11.1092806583526830', '79.3778256185603400', 'SH 140, Kodangudi, Tamil Nadu 612904, India', 128, 'Ariyalur', 'India', 'Tamil Nadu', 64, 'Application'),
('jhdsbv', 'sdjkvb', 'wudfb', 'Afghanistan (+93)', '5334', 'sdjvh@sdv.com', 'Owner', '2019-06-22 11:44:35.200740', 0, 'Manufacturing', 'Chemical (Basic)', '', 'something', 'ahagcvdc hdc sgh sdcsd snd', '', '18.3293678385493560', '74.0072870687499700', 'Diwale-Narayanpur Rd, Supe Kh., Maharashtra 412301, India', 129, 'Pune', 'India', 'Maharashtra', 65, 'Application'),
('jhvdc', 'ahdgvc', 'kgabv', 'Afghanistan (+93)', '541', 'av@ac.com', 'Owner', '2019-06-22 11:51:36.027940', 0, 'Manufacturing', 'Chemical (Basic)', '', 'something', 'as a  as asc as c', '', '19.1201279999999980', '72.8866815999999700', '48, Raje Shivaji Nagar, Marol, Andheri East, Mumbai, Maharashtra 400072, India', 130, 'Mumbai Suburban', 'India', 'Maharashtra', 66, 'Application'),
('hsdb', 'ajdcv', 'adbc', 'Afghanistan (+93)', '546', 'afc@av.com', 'Owner', '2019-06-22 12:02:36.783265', 0, 'Manufacturing', 'Chemical (Basic)', '', 'something', 'ajshvc aca cab cabn b asc', '', '19.0999889000000030', '72.9163338999999300', 'D-109, LBS Rd, Amrut Nagar, Ghatkopar West, Mumbai, Maharashtra 400086, India', 131, 'Mumbai Suburban', 'India', 'Maharashtra', 67, 'Application'),
('asc', 'ascv', 'asv', 'Samoa(+1-684)', '541486521', 'sav@addv.com', 'Broker', '2019-06-26 14:56:54.237171', 0, 'Manufacturing', 'Chemical (Basic)', 'Association', 'nd v', 'jhds sdjs dsj dvsj dv sh', '', '18.3293678385493560', '73.8534784749999700', 'Bormal, Maharashtra 412205, India', 137, 'Pune', 'India', 'Maharashtra', 68, 'Business'),
('asc', 'ascv', 'asv', 'Samoa(+1-684)', '54148652', 'sav@addv.com', 'Broker', '2019-06-26 14:59:17.316854', 0, 'Manufacturing', 'Chemical (Basic)', 'Association', 'nd v', 'jhds sdjs dsj dvsj dv sh', '', '19.1000236999999980', '72.9163031000000500', 'D-109, LBS Rd, Amrut Nagar, Ghatkopar West, Mumbai, Maharashtra 400086, India', 138, 'Mumbai Suburban', 'India', 'Maharashtra', 69, 'Business'),
('ksjdvn', 'ajkdv', 'ljsdv', 'Afghanistan (+93)', '54546', 'adhv@easdfv.com', 'Owner', '2019-06-26 15:00:58.527940', 0, 'Manufacturing', 'Chemical (Basic)', 'Limited Liability Partnership (LLP)', 'ajbad', 'sd sf df fdf df', '', '23.0225050000000000', '72.5713620999999900', 'Ahmedabad, Gujarat, India', 139, 'Ahmedabad', 'India', 'Gujarat', 70, 'Business');

-- --------------------------------------------------------

--
-- Table structure for table `seller1_sellipcode`
--

CREATE TABLE `seller1_sellipcode` (
  `ipcode_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `startup_type` varchar(255) NOT NULL,
  `research_title` varchar(255) NOT NULL,
  `about` longtext NOT NULL,
  `asking_price` int(11) NOT NULL,
  `website` varchar(500) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_sellipcode`
--

INSERT INTO `seller1_sellipcode` (`ipcode_id`, `type`, `startup_type`, `research_title`, `about`, `asking_price`, `website`, `seller_id`) VALUES
(1, 'Ipcode', '', 'jac  aja csajb csa', 'acacna csa csabcsa csan', 874, 'http://www.google.com', 45),
(2, 'Ipcode', '', 'skjdbs vdsv sdv sdv skdvs dv', 'db sdvs vsv sn v', 8745544, NULL, 58),
(3, 'Ipcode', 'Intellectual Property', 'gahdva dnbd andb anbd', 'jdv dajaj dc', 5461, NULL, 63);

-- --------------------------------------------------------

--
-- Table structure for table `seller1_sellstartup`
--

CREATE TABLE `seller1_sellstartup` (
  `startup_id` int(11) NOT NULL,
  `type` varchar(100) DEFAULT NULL,
  `about` longtext NOT NULL,
  `sought_equity` decimal(30,20) DEFAULT NULL,
  `asking_price` int(11) NOT NULL,
  `revenue_growth` decimal(30,20) DEFAULT NULL,
  `year_established` int(11) NOT NULL,
  `reason_selling` longtext NOT NULL,
  `website` varchar(500) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `seller1_sellstartup`
--

INSERT INTO `seller1_sellstartup` (`startup_id`, `type`, `about`, `sought_equity`, `asking_price`, `revenue_growth`, `year_established`, `reason_selling`, `website`, `seller_id`) VALUES
(1, 'Startup', 'mndn a dmsn sm vsm vsv', '46.00000000000000000000', 45, '465.00000000000000000000', 2006, 'bdv sd sd vsbdv', NULL, 42),
(2, 'Startup', 'khbd sdvkdv sdvk sdvn sdvkn', '97865.00000000000000000000', 985615, '841.00000000000000000000', 2013, 'sjh ssjd sjd sn vsdn', NULL, 50);

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_association`
--

CREATE TABLE `social_auth_association` (
  `id` int(11) NOT NULL,
  `server_url` varchar(255) NOT NULL,
  `handle` varchar(255) NOT NULL,
  `secret` varchar(255) NOT NULL,
  `issued` int(11) NOT NULL,
  `lifetime` int(11) NOT NULL,
  `assoc_type` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_code`
--

CREATE TABLE `social_auth_code` (
  `id` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  `code` varchar(32) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_nonce`
--

CREATE TABLE `social_auth_nonce` (
  `id` int(11) NOT NULL,
  `server_url` varchar(255) NOT NULL,
  `timestamp` int(11) NOT NULL,
  `salt` varchar(65) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_partial`
--

CREATE TABLE `social_auth_partial` (
  `id` int(11) NOT NULL,
  `token` varchar(32) NOT NULL,
  `next_step` smallint(5) UNSIGNED NOT NULL,
  `backend` varchar(32) NOT NULL,
  `data` longtext NOT NULL,
  `timestamp` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `social_auth_usersocialauth`
--

CREATE TABLE `social_auth_usersocialauth` (
  `id` int(11) NOT NULL,
  `provider` varchar(32) NOT NULL,
  `uid` varchar(255) NOT NULL,
  `extra_data` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `social_auth_usersocialauth`
--

INSERT INTO `social_auth_usersocialauth` (`id`, `provider`, `uid`, `extra_data`, `user_id`) VALUES
(1, 'github', '42388402', '{\"auth_time\": 1561840277, \"id\": 42388402, \"expires\": null, \"login\": \"PrajwalBarapatre\", \"access_token\": \"5cea0abe3d2da4813c66e85efeaae836b930a060\", \"token_type\": \"bearer\"}', 34),
(2, 'google-oauth2', 'prajwalbarapatre13@gmail.com', '{\"auth_time\": 1561840445, \"expires\": 3600, \"token_type\": \"Bearer\", \"access_token\": \"ya29.Gls2B-uUyYiDK1_9hSc-duvfq5DGoRC4SxB45I3LSB5bQWCHOi_csCzfUyp8lx8MIgjULjwm-5PXtnjI1FHdtBEcK85ta76p8qPlSNjcO2bhuexNSVczgjgfFW7L\"}', 35),
(3, 'github', '49993230', '{\"auth_time\": 1561808269, \"id\": 49993230, \"expires\": null, \"login\": \"bmerge2100\", \"access_token\": \"9468170e7534b0d3b1961dcb2ecc293543979291\", \"token_type\": \"bearer\"}', 36),
(4, 'github', '52349321', '{\"auth_time\": 1561810687, \"id\": 52349321, \"expires\": null, \"login\": \"arjunpandiant\", \"access_token\": \"bd45801a0b436e22f82e9f2a91f6cc62e6151339\", \"token_type\": \"bearer\"}', 37),
(5, 'google-oauth2', 'admin@bverge.com', '{\"auth_time\": 1561815490, \"expires\": 3600, \"token_type\": \"Bearer\", \"access_token\": \"ya29.Gls2BznXzNXewTJm_K_iuqYVf-tot-XWfL2Vuxov9e6XCTimlIsOycNhMwr5Ot70bGDHulUoNIKXTCS8iGDE1ZwI-iOboAjVsvutJryv6TqUq-EwWP7eyRN0QxIt\"}', 39),
(6, 'github', '52351217', '{\"auth_time\": 1561817511, \"id\": 52351217, \"expires\": null, \"login\": \"prithviphysics\", \"access_token\": \"1b99cebeeb92c6c5a0bcf6d02f8e8c7fbe21e3e3\", \"token_type\": \"bearer\"}', 40),
(7, 'linkedin-oauth2', 'rOm4mGMsfx', '{\"auth_time\": 1561818152, \"id\": \"rOm4mGMsfx\", \"expires\": 5183999, \"first_name\": {\"localized\": {\"en_US\": \"Prithviraj\"}, \"preferredLocale\": {\"country\": \"US\", \"language\": \"en\"}}, \"last_name\": {\"localized\": {\"en_US\": \"Radhakrishnan\"}, \"preferredLocale\": {\"country\": \"US\", \"language\": \"en\"}}, \"access_token\": \"AQV9EBfsy9MprDdQpwKvP78KtUMyWJYVU0OZM8RK8nhxgdpQ77u5H1jL_uziXx6WXB06iZVPIfhvBKfYc1GC_6CWz6DdGdfNGSb-AkWdTAVMDt21lak4KDpHQGgizqykoV1tw-gd0Dh2Bg2IhduRlE3D7ddM8XGQrZe63-M5ePPrH8qgyW6-GkzZFeEpxKf54IoeTRGmyW4oNyB4Na_M0jBqIVFGpF912m_O8m8YWqhQ5oQTMJqjhUESUW_NQoIq8HpjRh6rRR345VkkVbIq3uktZTqWyn4mIYeQfAy6WB2bdtBtcghrTU1Thq7ecDhvCoj_-uvthDLfzZgEmMUjKJWARB9MQg\", \"token_type\": null, \"name\": null, \"email_address\": null, \"picture_url\": null, \"profile_url\": null}', 41),
(8, 'linkedin-oauth2', 'fkHwEzoFiH', '{\"auth_time\": 1561817940, \"id\": \"fkHwEzoFiH\", \"expires\": 5183999, \"first_name\": {\"localized\": {\"en_US\": \"Arjun\"}, \"preferredLocale\": {\"country\": \"US\", \"language\": \"en\"}}, \"last_name\": {\"localized\": {\"en_US\": \"Pandian T\"}, \"preferredLocale\": {\"country\": \"US\", \"language\": \"en\"}}, \"name\": null, \"email_address\": null, \"picture_url\": null, \"profile_url\": null, \"access_token\": \"AQXckzY2g4OobwUfw09eU_pPkxd9BGn-9VTG67zb3XPQFjgbuRQs8N2WUXMMEVWTyuaOxCpfjPkI8sWdhibYGPIHEHn0wmYFrA8MAe5Yt6UFNnjPAFoEuNPjUxXZZFeBRagl5YLuZLQK9ztPDYkzAR6G1JSR5Ju0YtTs4u3-svzf3na3jOSOm6lujrojWQpCVBq7pLAiPjxVJ-CeOUeXCAACF8D1iSx72NfXUyLPuZw5BlTdsB-5bFoodOs8teDzXDLjAiX-wSxAZe2lQdIEawq5uhx8vRgah0l1RGf2e7QQ-eqGc_ju1hr3iEwf7RSBl0lWW8qsLhGFB9JRMANqKjT4HK0SmA\", \"token_type\": null}', 42);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_advise`
--

CREATE TABLE `user_seller_advise` (
  `advise_id` int(11) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `advisor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_advise`
--

INSERT INTO `user_seller_advise` (`advise_id`, `type`, `advisor_id`) VALUES
(1, 'Business', 9),
(2, 'Business', 10),
(3, 'Business', 11),
(4, 'Business', 12),
(5, 'Business', 13),
(6, 'Business', 14),
(7, 'Business', 15),
(8, 'Business', 16),
(9, 'Business', 17),
(10, 'Business', 18),
(11, 'Business', 19),
(12, 'Startup', 20),
(13, 'Business', 21),
(14, 'Business', 22);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_advise_cart_invest`
--

CREATE TABLE `user_seller_advise_cart_invest` (
  `id` int(11) NOT NULL,
  `advise_id` int(11) NOT NULL,
  `investor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_advise_cart_seller`
--

CREATE TABLE `user_seller_advise_cart_seller` (
  `id` int(11) NOT NULL,
  `advise_id` int(11) NOT NULL,
  `seller1_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_advise_cart_seller`
--

INSERT INTO `user_seller_advise_cart_seller` (`id`, `advise_id`, `seller1_id`) VALUES
(1, 2, 48),
(5, 14, 49),
(3, 14, 60),
(6, 14, 69);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_advise_inst_invest`
--

CREATE TABLE `user_seller_advise_inst_invest` (
  `id` int(11) NOT NULL,
  `advise_id` int(11) NOT NULL,
  `investor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_advise_inst_invest`
--

INSERT INTO `user_seller_advise_inst_invest` (`id`, `advise_id`, `investor_id`) VALUES
(3, 12, 7);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_advise_inst_seller`
--

CREATE TABLE `user_seller_advise_inst_seller` (
  `id` int(11) NOT NULL,
  `advise_id` int(11) NOT NULL,
  `seller1_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_advise_inst_seller`
--

INSERT INTO `user_seller_advise_inst_seller` (`id`, `advise_id`, `seller1_id`) VALUES
(1, 12, 57);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_invest`
--

CREATE TABLE `user_seller_invest` (
  `invest_id` int(11) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `investor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_invest`
--

INSERT INTO `user_seller_invest` (`invest_id`, `type`, `investor_id`) VALUES
(1, 'Individual', 6),
(2, 'Individual', 7),
(3, 'Individual', 8),
(4, 'Company', 9);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_invest_cart_advisor`
--

CREATE TABLE `user_seller_invest_cart_advisor` (
  `id` int(11) NOT NULL,
  `invest_id` int(11) NOT NULL,
  `advisor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_invest_cart_advisor`
--

INSERT INTO `user_seller_invest_cart_advisor` (`id`, `invest_id`, `advisor_id`) VALUES
(3, 2, 20);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_invest_cart_seller`
--

CREATE TABLE `user_seller_invest_cart_seller` (
  `id` int(11) NOT NULL,
  `invest_id` int(11) NOT NULL,
  `seller1_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_invest_cart_seller`
--

INSERT INTO `user_seller_invest_cart_seller` (`id`, `invest_id`, `seller1_id`) VALUES
(5, 2, 51),
(10, 3, 69),
(7, 4, 65);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_invest_inst_advisor`
--

CREATE TABLE `user_seller_invest_inst_advisor` (
  `id` int(11) NOT NULL,
  `invest_id` int(11) NOT NULL,
  `advisor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_invest_inst_seller`
--

CREATE TABLE `user_seller_invest_inst_seller` (
  `id` int(11) NOT NULL,
  `invest_id` int(11) NOT NULL,
  `seller1_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_sell`
--

CREATE TABLE `user_seller_sell` (
  `sell_id` int(11) NOT NULL,
  `type` varchar(255) DEFAULT NULL,
  `seller_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_sell`
--

INSERT INTO `user_seller_sell` (`sell_id`, `type`, `seller_id`) VALUES
(1, 'Asset', 47),
(2, 'Asset', 48),
(3, 'Asset', 49),
(4, 'Startup', 50),
(5, 'Business', 51),
(6, 'Business', 52),
(7, 'Business', 53),
(8, 'Business', 54),
(9, 'Business', 55),
(10, 'Business', 56),
(11, 'Business', 57),
(12, 'Ipcode', 58),
(13, 'Application', 59),
(14, 'Equity', 60),
(15, 'Equity', 61),
(16, 'Loan', 62),
(17, 'Ipcode', 63),
(18, 'Application', 64),
(19, 'Application', 65),
(20, 'Application', 66),
(21, 'Application', 67),
(22, 'Business', 69),
(23, 'Business', 70);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_sell_cart_advisor`
--

CREATE TABLE `user_seller_sell_cart_advisor` (
  `id` int(11) NOT NULL,
  `sell_id` int(11) NOT NULL,
  `advisor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_sell_cart_advisor`
--

INSERT INTO `user_seller_sell_cart_advisor` (`id`, `sell_id`, `advisor_id`) VALUES
(1, 1, 7),
(2, 11, 20);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_sell_cart_investor`
--

CREATE TABLE `user_seller_sell_cart_investor` (
  `id` int(11) NOT NULL,
  `sell_id` int(11) NOT NULL,
  `investor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_sell_inst_advisor`
--

CREATE TABLE `user_seller_sell_inst_advisor` (
  `id` int(11) NOT NULL,
  `sell_id` int(11) NOT NULL,
  `advisor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_sell_inst_advisor`
--

INSERT INTO `user_seller_sell_inst_advisor` (`id`, `sell_id`, `advisor_id`) VALUES
(1, 1, 6),
(2, 2, 10),
(6, 3, 22),
(4, 14, 22),
(7, 22, 22);

-- --------------------------------------------------------

--
-- Table structure for table `user_seller_sell_inst_investors`
--

CREATE TABLE `user_seller_sell_inst_investors` (
  `id` int(11) NOT NULL,
  `sell_id` int(11) NOT NULL,
  `investor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_seller_sell_inst_investors`
--

INSERT INTO `user_seller_sell_inst_investors` (`id`, `sell_id`, `investor_id`) VALUES
(1, 1, 5),
(3, 1, 8),
(6, 5, 7),
(8, 19, 9),
(11, 22, 8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `advisor_advisor`
--
ALTER TABLE `advisor_advisor`
  ADD PRIMARY KEY (`advisor_id`);

--
-- Indexes for table `advisor_businessadvisor`
--
ALTER TABLE `advisor_businessadvisor`
  ADD PRIMARY KEY (`business_id`),
  ADD UNIQUE KEY `advisor_id` (`advisor_id`);

--
-- Indexes for table `advisor_startupadvisor`
--
ALTER TABLE `advisor_startupadvisor`
  ADD PRIMARY KEY (`startup_id`),
  ADD UNIQUE KEY `advisor_id` (`advisor_id`);

--
-- Indexes for table `album_file`
--
ALTER TABLE `album_file`
  ADD PRIMARY KEY (`file_id`);

--
-- Indexes for table `album_kalbumforfile`
--
ALTER TABLE `album_kalbumforfile`
  ADD PRIMARY KEY (`album_id`);

--
-- Indexes for table `album_kalbumforfile_files`
--
ALTER TABLE `album_kalbumforfile_files`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `album_kalbumforfile_files_kalbumforfile_id_file_id_63446e57_uniq` (`kalbumforfile_id`,`file_id`),
  ADD KEY `album_kalbumforfile_files_file_id_77a0b7c0_fk_album_file_file_id` (`file_id`);

--
-- Indexes for table `album_kalbumforfile_seller`
--
ALTER TABLE `album_kalbumforfile_seller`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `album_kalbumforfile_sell_kalbumforfile_id_sellbus_e192a748_uniq` (`kalbumforfile_id`,`sellbusiness_id`),
  ADD KEY `album_kalbumforfile__sellbusiness_id_abe684c1_fk_seller1_s` (`sellbusiness_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `chat_chat`
--
ALTER TABLE `chat_chat`
  ADD PRIMARY KEY (`chat_id`),
  ADD UNIQUE KEY `seller_id` (`seller_id`);

--
-- Indexes for table `chat_chat_messages`
--
ALTER TABLE `chat_chat_messages`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `chat_chat_messages_chat_id_message_id_0dc243e3_uniq` (`chat_id`,`message_id`),
  ADD KEY `chat_chat_messages_message_id_efa31cba_fk_chat_mess` (`message_id`);

--
-- Indexes for table `chat_chat_participants`
--
ALTER TABLE `chat_chat_participants`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `chat_chat_participants_chat_id_contact_id_827dbf76_uniq` (`chat_id`,`contact_id`),
  ADD KEY `chat_chat_participan_contact_id_703a4fb8_fk_chat_cont` (`contact_id`);

--
-- Indexes for table `chat_contact`
--
ALTER TABLE `chat_contact`
  ADD PRIMARY KEY (`contact_id`),
  ADD KEY `chat_contact_user_id_1df671c2_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `chat_contact_friends`
--
ALTER TABLE `chat_contact_friends`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `chat_contact_friends_from_contact_id_to_contact_id_7995e049_uniq` (`from_contact_id`,`to_contact_id`),
  ADD KEY `chat_contact_friends_to_contact_id_5cb5d725_fk_chat_cont` (`to_contact_id`);

--
-- Indexes for table `chat_malbum`
--
ALTER TABLE `chat_malbum`
  ADD PRIMARY KEY (`malbum_id`);

--
-- Indexes for table `chat_message`
--
ALTER TABLE `chat_message`
  ADD PRIMARY KEY (`message_id`),
  ADD KEY `chat_message_contact_id_3553335c_fk_chat_contact_contact_id` (`contact_id`),
  ADD KEY `chat_message_malbum_id_9d86ddc4_fk_chat_malbum_malbum_id` (`malbum_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `investor_companyinvestor`
--
ALTER TABLE `investor_companyinvestor`
  ADD PRIMARY KEY (`company_id`),
  ADD UNIQUE KEY `investor_id` (`investor_id`);

--
-- Indexes for table `investor_individualinvestor`
--
ALTER TABLE `investor_individualinvestor`
  ADD PRIMARY KEY (`individual_id`),
  ADD UNIQUE KEY `investor_id` (`investor_id`);

--
-- Indexes for table `investor_investor`
--
ALTER TABLE `investor_investor`
  ADD PRIMARY KEY (`investor_id`);

--
-- Indexes for table `metadata_advisor`
--
ALTER TABLE `metadata_advisor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `metadata_businesssectors`
--
ALTER TABLE `metadata_businesssectors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `metadata_codes`
--
ALTER TABLE `metadata_codes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `metadata_company`
--
ALTER TABLE `metadata_company`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `metadata_years`
--
ALTER TABLE `metadata_years`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `profiles_profile`
--
ALTER TABLE `profiles_profile`
  ADD PRIMARY KEY (`profile_id`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD UNIQUE KEY `invest_type_id` (`invest_type_id`),
  ADD KEY `profiles_profile_curr_chat_id_2fea31c2` (`curr_chat_id`);

--
-- Indexes for table `profiles_profile_advise_type`
--
ALTER TABLE `profiles_profile_advise_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profiles_profile_advise_type_profile_id_advisor_id_e0fa308b_uniq` (`profile_id`,`advisor_id`),
  ADD KEY `profiles_profile_adv_advisor_id_d4cc4ec2_fk_advisor_a` (`advisor_id`);

--
-- Indexes for table `profiles_profile_investors_type`
--
ALTER TABLE `profiles_profile_investors_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profiles_profile_investo_profile_id_investor_id_ac37f5fb_uniq` (`profile_id`,`investor_id`),
  ADD KEY `profiles_profile_inv_investor_id_22d560cb_fk_investor_` (`investor_id`);

--
-- Indexes for table `profiles_profile_just_advise`
--
ALTER TABLE `profiles_profile_just_advise`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profiles_profile_just_advise_profile_id_advisor_id_109c7241_uniq` (`profile_id`,`advisor_id`),
  ADD KEY `profiles_profile_jus_advisor_id_08c19062_fk_advisor_a` (`advisor_id`);

--
-- Indexes for table `profiles_profile_just_invest`
--
ALTER TABLE `profiles_profile_just_invest`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profiles_profile_just_in_profile_id_investor_id_108fbfed_uniq` (`profile_id`,`investor_id`),
  ADD KEY `profiles_profile_jus_investor_id_c9579499_fk_investor_` (`investor_id`);

--
-- Indexes for table `profiles_profile_just_sell`
--
ALTER TABLE `profiles_profile_just_sell`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profiles_profile_just_sell_profile_id_seller1_id_2110f478_uniq` (`profile_id`,`seller1_id`),
  ADD KEY `profiles_profile_jus_seller1_id_1a6c63a2_fk_seller1_s` (`seller1_id`);

--
-- Indexes for table `profiles_profile_sell_type`
--
ALTER TABLE `profiles_profile_sell_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profiles_profile_sell_type_profile_id_seller1_id_75b5fd2f_uniq` (`profile_id`,`seller1_id`),
  ADD KEY `profiles_profile_sel_seller1_id_d5441616_fk_seller1_s` (`seller1_id`);

--
-- Indexes for table `profiles_profile_user_advise`
--
ALTER TABLE `profiles_profile_user_advise`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profiles_profile_user_advise_profile_id_advise_id_fd664035_uniq` (`profile_id`,`advise_id`),
  ADD KEY `profiles_profile_use_advise_id_e12d2822_fk_user_sell` (`advise_id`);

--
-- Indexes for table `profiles_profile_user_invest`
--
ALTER TABLE `profiles_profile_user_invest`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profiles_profile_user_invest_profile_id_invest_id_7fcd3725_uniq` (`profile_id`,`invest_id`),
  ADD KEY `profiles_profile_use_invest_id_ca727dcb_fk_user_sell` (`invest_id`);

--
-- Indexes for table `profiles_profile_user_sell`
--
ALTER TABLE `profiles_profile_user_sell`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `profiles_profile_user_sell_profile_id_sell_id_bd60b265_uniq` (`profile_id`,`sell_id`),
  ADD KEY `profiles_profile_use_sell_id_3b49b4ca_fk_user_sell` (`sell_id`);

--
-- Indexes for table `seller1_ablumfiles`
--
ALTER TABLE `seller1_ablumfiles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `seller1_raiseloan`
--
ALTER TABLE `seller1_raiseloan`
  ADD PRIMARY KEY (`loan_id`),
  ADD UNIQUE KEY `seller_id` (`seller_id`);

--
-- Indexes for table `seller1_revenuemodel`
--
ALTER TABLE `seller1_revenuemodel`
  ADD PRIMARY KEY (`revenue_id`),
  ADD UNIQUE KEY `seller_id` (`seller_id`);

--
-- Indexes for table `seller1_sellapp`
--
ALTER TABLE `seller1_sellapp`
  ADD PRIMARY KEY (`app_id`),
  ADD UNIQUE KEY `seller_id` (`seller_id`);

--
-- Indexes for table `seller1_sellasset`
--
ALTER TABLE `seller1_sellasset`
  ADD PRIMARY KEY (`asset_id`),
  ADD UNIQUE KEY `seller_id` (`seller_id`);

--
-- Indexes for table `seller1_sellbusiness`
--
ALTER TABLE `seller1_sellbusiness`
  ADD PRIMARY KEY (`business_id`),
  ADD UNIQUE KEY `seller1_sellbusiness_seller_id_02ac42a7_uniq` (`seller_id`);

--
-- Indexes for table `seller1_sellequity`
--
ALTER TABLE `seller1_sellequity`
  ADD PRIMARY KEY (`equity_id`),
  ADD UNIQUE KEY `seller_id` (`seller_id`);

--
-- Indexes for table `seller1_seller1`
--
ALTER TABLE `seller1_seller1`
  ADD PRIMARY KEY (`business_id`);

--
-- Indexes for table `seller1_sellipcode`
--
ALTER TABLE `seller1_sellipcode`
  ADD PRIMARY KEY (`ipcode_id`),
  ADD UNIQUE KEY `seller_id` (`seller_id`);

--
-- Indexes for table `seller1_sellstartup`
--
ALTER TABLE `seller1_sellstartup`
  ADD PRIMARY KEY (`startup_id`),
  ADD UNIQUE KEY `seller_id` (`seller_id`);

--
-- Indexes for table `social_auth_association`
--
ALTER TABLE `social_auth_association`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_association_server_url_handle_078befa2_uniq` (`server_url`,`handle`);

--
-- Indexes for table `social_auth_code`
--
ALTER TABLE `social_auth_code`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_code_email_code_801b2d02_uniq` (`email`,`code`),
  ADD KEY `social_auth_code_code_a2393167` (`code`),
  ADD KEY `social_auth_code_timestamp_176b341f` (`timestamp`);

--
-- Indexes for table `social_auth_nonce`
--
ALTER TABLE `social_auth_nonce`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_nonce_server_url_timestamp_salt_f6284463_uniq` (`server_url`,`timestamp`,`salt`);

--
-- Indexes for table `social_auth_partial`
--
ALTER TABLE `social_auth_partial`
  ADD PRIMARY KEY (`id`),
  ADD KEY `social_auth_partial_token_3017fea3` (`token`),
  ADD KEY `social_auth_partial_timestamp_50f2119f` (`timestamp`);

--
-- Indexes for table `social_auth_usersocialauth`
--
ALTER TABLE `social_auth_usersocialauth`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `social_auth_usersocialauth_provider_uid_e6b5e668_uniq` (`provider`,`uid`),
  ADD KEY `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `user_seller_advise`
--
ALTER TABLE `user_seller_advise`
  ADD PRIMARY KEY (`advise_id`),
  ADD UNIQUE KEY `advisor_id` (`advisor_id`);

--
-- Indexes for table `user_seller_advise_cart_invest`
--
ALTER TABLE `user_seller_advise_cart_invest`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_advise_cart__advise_id_investor_id_8475abf7_uniq` (`advise_id`,`investor_id`),
  ADD KEY `user_seller_advise_c_investor_id_b4cb96bd_fk_investor_` (`investor_id`);

--
-- Indexes for table `user_seller_advise_cart_seller`
--
ALTER TABLE `user_seller_advise_cart_seller`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_advise_cart__advise_id_seller1_id_b0e64606_uniq` (`advise_id`,`seller1_id`),
  ADD KEY `user_seller_advise_c_seller1_id_9247a68e_fk_seller1_s` (`seller1_id`);

--
-- Indexes for table `user_seller_advise_inst_invest`
--
ALTER TABLE `user_seller_advise_inst_invest`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_advise_inst__advise_id_investor_id_468e086b_uniq` (`advise_id`,`investor_id`),
  ADD KEY `user_seller_advise_i_investor_id_a8750df7_fk_investor_` (`investor_id`);

--
-- Indexes for table `user_seller_advise_inst_seller`
--
ALTER TABLE `user_seller_advise_inst_seller`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_advise_inst__advise_id_seller1_id_bbc88e54_uniq` (`advise_id`,`seller1_id`),
  ADD KEY `user_seller_advise_i_seller1_id_5fdec6ba_fk_seller1_s` (`seller1_id`);

--
-- Indexes for table `user_seller_invest`
--
ALTER TABLE `user_seller_invest`
  ADD PRIMARY KEY (`invest_id`),
  ADD UNIQUE KEY `investor_id` (`investor_id`);

--
-- Indexes for table `user_seller_invest_cart_advisor`
--
ALTER TABLE `user_seller_invest_cart_advisor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_invest_cart__invest_id_advisor_id_529f720a_uniq` (`invest_id`,`advisor_id`),
  ADD KEY `user_seller_invest_c_advisor_id_3edca75a_fk_advisor_a` (`advisor_id`);

--
-- Indexes for table `user_seller_invest_cart_seller`
--
ALTER TABLE `user_seller_invest_cart_seller`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_invest_cart__invest_id_seller1_id_1a02374e_uniq` (`invest_id`,`seller1_id`),
  ADD KEY `user_seller_invest_c_seller1_id_735226e2_fk_seller1_s` (`seller1_id`);

--
-- Indexes for table `user_seller_invest_inst_advisor`
--
ALTER TABLE `user_seller_invest_inst_advisor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_invest_inst__invest_id_advisor_id_79089973_uniq` (`invest_id`,`advisor_id`),
  ADD KEY `user_seller_invest_i_advisor_id_6e50b379_fk_advisor_a` (`advisor_id`);

--
-- Indexes for table `user_seller_invest_inst_seller`
--
ALTER TABLE `user_seller_invest_inst_seller`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_invest_inst__invest_id_seller1_id_6a826987_uniq` (`invest_id`,`seller1_id`),
  ADD KEY `user_seller_invest_i_seller1_id_1e1d817c_fk_seller1_s` (`seller1_id`);

--
-- Indexes for table `user_seller_sell`
--
ALTER TABLE `user_seller_sell`
  ADD PRIMARY KEY (`sell_id`),
  ADD UNIQUE KEY `seller_id` (`seller_id`);

--
-- Indexes for table `user_seller_sell_cart_advisor`
--
ALTER TABLE `user_seller_sell_cart_advisor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_sell_cart_advisor_sell_id_advisor_id_70b8faa7_uniq` (`sell_id`,`advisor_id`),
  ADD KEY `user_seller_sell_car_advisor_id_ff26873b_fk_advisor_a` (`advisor_id`);

--
-- Indexes for table `user_seller_sell_cart_investor`
--
ALTER TABLE `user_seller_sell_cart_investor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_sell_cart_investor_sell_id_investor_id_9ccf62cb_uniq` (`sell_id`,`investor_id`),
  ADD KEY `user_seller_sell_car_investor_id_a8304aa0_fk_investor_` (`investor_id`);

--
-- Indexes for table `user_seller_sell_inst_advisor`
--
ALTER TABLE `user_seller_sell_inst_advisor`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_sell_inst_advisor_sell_id_advisor_id_640744d5_uniq` (`sell_id`,`advisor_id`),
  ADD KEY `user_seller_sell_ins_advisor_id_33f51fe1_fk_advisor_a` (`advisor_id`);

--
-- Indexes for table `user_seller_sell_inst_investors`
--
ALTER TABLE `user_seller_sell_inst_investors`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_seller_sell_inst_in_sell_id_investor_id_0ddee386_uniq` (`sell_id`,`investor_id`),
  ADD KEY `user_seller_sell_ins_investor_id_ebd308ed_fk_investor_` (`investor_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `advisor_advisor`
--
ALTER TABLE `advisor_advisor`
  MODIFY `advisor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `advisor_businessadvisor`
--
ALTER TABLE `advisor_businessadvisor`
  MODIFY `business_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `advisor_startupadvisor`
--
ALTER TABLE `advisor_startupadvisor`
  MODIFY `startup_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `album_file`
--
ALTER TABLE `album_file`
  MODIFY `file_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=398;

--
-- AUTO_INCREMENT for table `album_kalbumforfile`
--
ALTER TABLE `album_kalbumforfile`
  MODIFY `album_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=140;

--
-- AUTO_INCREMENT for table `album_kalbumforfile_files`
--
ALTER TABLE `album_kalbumforfile_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=342;

--
-- AUTO_INCREMENT for table `album_kalbumforfile_seller`
--
ALTER TABLE `album_kalbumforfile_seller`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=154;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chat_chat`
--
ALTER TABLE `chat_chat`
  MODIFY `chat_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `chat_chat_messages`
--
ALTER TABLE `chat_chat_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=165;

--
-- AUTO_INCREMENT for table `chat_chat_participants`
--
ALTER TABLE `chat_chat_participants`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `chat_contact`
--
ALTER TABLE `chat_contact`
  MODIFY `contact_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `chat_contact_friends`
--
ALTER TABLE `chat_contact_friends`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `chat_malbum`
--
ALTER TABLE `chat_malbum`
  MODIFY `malbum_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `chat_message`
--
ALTER TABLE `chat_message`
  MODIFY `message_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=180;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=241;

--
-- AUTO_INCREMENT for table `investor_companyinvestor`
--
ALTER TABLE `investor_companyinvestor`
  MODIFY `company_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `investor_individualinvestor`
--
ALTER TABLE `investor_individualinvestor`
  MODIFY `individual_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `investor_investor`
--
ALTER TABLE `investor_investor`
  MODIFY `investor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `metadata_advisor`
--
ALTER TABLE `metadata_advisor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=153;

--
-- AUTO_INCREMENT for table `metadata_businesssectors`
--
ALTER TABLE `metadata_businesssectors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=303;

--
-- AUTO_INCREMENT for table `metadata_codes`
--
ALTER TABLE `metadata_codes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=229;

--
-- AUTO_INCREMENT for table `metadata_company`
--
ALTER TABLE `metadata_company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `metadata_years`
--
ALTER TABLE `metadata_years`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=80;

--
-- AUTO_INCREMENT for table `profiles_profile`
--
ALTER TABLE `profiles_profile`
  MODIFY `profile_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `profiles_profile_advise_type`
--
ALTER TABLE `profiles_profile_advise_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `profiles_profile_investors_type`
--
ALTER TABLE `profiles_profile_investors_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profiles_profile_just_advise`
--
ALTER TABLE `profiles_profile_just_advise`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `profiles_profile_just_invest`
--
ALTER TABLE `profiles_profile_just_invest`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profiles_profile_just_sell`
--
ALTER TABLE `profiles_profile_just_sell`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `profiles_profile_sell_type`
--
ALTER TABLE `profiles_profile_sell_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `profiles_profile_user_advise`
--
ALTER TABLE `profiles_profile_user_advise`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `profiles_profile_user_invest`
--
ALTER TABLE `profiles_profile_user_invest`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `profiles_profile_user_sell`
--
ALTER TABLE `profiles_profile_user_sell`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `seller1_ablumfiles`
--
ALTER TABLE `seller1_ablumfiles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `seller1_raiseloan`
--
ALTER TABLE `seller1_raiseloan`
  MODIFY `loan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `seller1_revenuemodel`
--
ALTER TABLE `seller1_revenuemodel`
  MODIFY `revenue_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `seller1_sellapp`
--
ALTER TABLE `seller1_sellapp`
  MODIFY `app_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `seller1_sellasset`
--
ALTER TABLE `seller1_sellasset`
  MODIFY `asset_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `seller1_sellbusiness`
--
ALTER TABLE `seller1_sellbusiness`
  MODIFY `business_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `seller1_sellequity`
--
ALTER TABLE `seller1_sellequity`
  MODIFY `equity_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `seller1_seller1`
--
ALTER TABLE `seller1_seller1`
  MODIFY `business_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT for table `seller1_sellipcode`
--
ALTER TABLE `seller1_sellipcode`
  MODIFY `ipcode_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `seller1_sellstartup`
--
ALTER TABLE `seller1_sellstartup`
  MODIFY `startup_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `social_auth_association`
--
ALTER TABLE `social_auth_association`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `social_auth_code`
--
ALTER TABLE `social_auth_code`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `social_auth_nonce`
--
ALTER TABLE `social_auth_nonce`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `social_auth_partial`
--
ALTER TABLE `social_auth_partial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `social_auth_usersocialauth`
--
ALTER TABLE `social_auth_usersocialauth`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `user_seller_advise`
--
ALTER TABLE `user_seller_advise`
  MODIFY `advise_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `user_seller_advise_cart_invest`
--
ALTER TABLE `user_seller_advise_cart_invest`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_seller_advise_cart_seller`
--
ALTER TABLE `user_seller_advise_cart_seller`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user_seller_advise_inst_invest`
--
ALTER TABLE `user_seller_advise_inst_invest`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_seller_advise_inst_seller`
--
ALTER TABLE `user_seller_advise_inst_seller`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `user_seller_invest`
--
ALTER TABLE `user_seller_invest`
  MODIFY `invest_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `user_seller_invest_cart_advisor`
--
ALTER TABLE `user_seller_invest_cart_advisor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user_seller_invest_cart_seller`
--
ALTER TABLE `user_seller_invest_cart_seller`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `user_seller_invest_inst_advisor`
--
ALTER TABLE `user_seller_invest_inst_advisor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_seller_invest_inst_seller`
--
ALTER TABLE `user_seller_invest_inst_seller`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_seller_sell`
--
ALTER TABLE `user_seller_sell`
  MODIFY `sell_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `user_seller_sell_cart_advisor`
--
ALTER TABLE `user_seller_sell_cart_advisor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `user_seller_sell_cart_investor`
--
ALTER TABLE `user_seller_sell_cart_investor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_seller_sell_inst_advisor`
--
ALTER TABLE `user_seller_sell_inst_advisor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `user_seller_sell_inst_investors`
--
ALTER TABLE `user_seller_sell_inst_investors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `advisor_businessadvisor`
--
ALTER TABLE `advisor_businessadvisor`
  ADD CONSTRAINT `advisor_businessadvi_advisor_id_c44defa9_fk_advisor_a` FOREIGN KEY (`advisor_id`) REFERENCES `advisor_advisor` (`advisor_id`);

--
-- Constraints for table `advisor_startupadvisor`
--
ALTER TABLE `advisor_startupadvisor`
  ADD CONSTRAINT `advisor_startupadvis_advisor_id_8d0f4b94_fk_advisor_a` FOREIGN KEY (`advisor_id`) REFERENCES `advisor_advisor` (`advisor_id`);

--
-- Constraints for table `album_kalbumforfile_files`
--
ALTER TABLE `album_kalbumforfile_files`
  ADD CONSTRAINT `album_kalbumforfile__kalbumforfile_id_35e36c07_fk_album_kal` FOREIGN KEY (`kalbumforfile_id`) REFERENCES `album_kalbumforfile` (`album_id`),
  ADD CONSTRAINT `album_kalbumforfile_files_file_id_77a0b7c0_fk_album_file_file_id` FOREIGN KEY (`file_id`) REFERENCES `album_file` (`file_id`);

--
-- Constraints for table `album_kalbumforfile_seller`
--
ALTER TABLE `album_kalbumforfile_seller`
  ADD CONSTRAINT `album_kalbumforfile__kalbumforfile_id_894d0378_fk_album_kal` FOREIGN KEY (`kalbumforfile_id`) REFERENCES `album_kalbumforfile` (`album_id`),
  ADD CONSTRAINT `album_kalbumforfile__sellbusiness_id_abe684c1_fk_seller1_s` FOREIGN KEY (`sellbusiness_id`) REFERENCES `seller1_sellbusiness` (`business_id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `chat_chat`
--
ALTER TABLE `chat_chat`
  ADD CONSTRAINT `chat_chat_seller_id_b3e3f429_fk_seller1_seller1_business_id` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `chat_chat_messages`
--
ALTER TABLE `chat_chat_messages`
  ADD CONSTRAINT `chat_chat_messages_chat_id_6ef09da4_fk_chat_chat_chat_id` FOREIGN KEY (`chat_id`) REFERENCES `chat_chat` (`chat_id`),
  ADD CONSTRAINT `chat_chat_messages_message_id_efa31cba_fk_chat_mess` FOREIGN KEY (`message_id`) REFERENCES `chat_message` (`message_id`);

--
-- Constraints for table `chat_chat_participants`
--
ALTER TABLE `chat_chat_participants`
  ADD CONSTRAINT `chat_chat_participan_contact_id_703a4fb8_fk_chat_cont` FOREIGN KEY (`contact_id`) REFERENCES `chat_contact` (`contact_id`),
  ADD CONSTRAINT `chat_chat_participants_chat_id_c4383b55_fk_chat_chat_chat_id` FOREIGN KEY (`chat_id`) REFERENCES `chat_chat` (`chat_id`);

--
-- Constraints for table `chat_contact`
--
ALTER TABLE `chat_contact`
  ADD CONSTRAINT `chat_contact_user_id_1df671c2_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `chat_contact_friends`
--
ALTER TABLE `chat_contact_friends`
  ADD CONSTRAINT `chat_contact_friends_from_contact_id_767f7e54_fk_chat_cont` FOREIGN KEY (`from_contact_id`) REFERENCES `chat_contact` (`contact_id`),
  ADD CONSTRAINT `chat_contact_friends_to_contact_id_5cb5d725_fk_chat_cont` FOREIGN KEY (`to_contact_id`) REFERENCES `chat_contact` (`contact_id`);

--
-- Constraints for table `chat_message`
--
ALTER TABLE `chat_message`
  ADD CONSTRAINT `chat_message_contact_id_3553335c_fk_chat_contact_contact_id` FOREIGN KEY (`contact_id`) REFERENCES `chat_contact` (`contact_id`),
  ADD CONSTRAINT `chat_message_malbum_id_9d86ddc4_fk_chat_malbum_malbum_id` FOREIGN KEY (`malbum_id`) REFERENCES `chat_malbum` (`malbum_id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `investor_companyinvestor`
--
ALTER TABLE `investor_companyinvestor`
  ADD CONSTRAINT `investor_companyinve_investor_id_d653bedc_fk_investor_` FOREIGN KEY (`investor_id`) REFERENCES `investor_investor` (`investor_id`);

--
-- Constraints for table `investor_individualinvestor`
--
ALTER TABLE `investor_individualinvestor`
  ADD CONSTRAINT `investor_individuali_investor_id_10b1dd54_fk_investor_` FOREIGN KEY (`investor_id`) REFERENCES `investor_investor` (`investor_id`);

--
-- Constraints for table `profiles_profile`
--
ALTER TABLE `profiles_profile`
  ADD CONSTRAINT `profiles_profile_curr_chat_id_2fea31c2_fk_chat_chat_chat_id` FOREIGN KEY (`curr_chat_id`) REFERENCES `chat_chat` (`chat_id`),
  ADD CONSTRAINT `profiles_profile_invest_type_id_61c3c70c_fk_investor_` FOREIGN KEY (`invest_type_id`) REFERENCES `investor_investor` (`investor_id`),
  ADD CONSTRAINT `profiles_profile_user_id_a3e81f91_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `profiles_profile_advise_type`
--
ALTER TABLE `profiles_profile_advise_type`
  ADD CONSTRAINT `profiles_profile_adv_advisor_id_d4cc4ec2_fk_advisor_a` FOREIGN KEY (`advisor_id`) REFERENCES `advisor_advisor` (`advisor_id`),
  ADD CONSTRAINT `profiles_profile_adv_profile_id_0adf9438_fk_profiles_` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`profile_id`);

--
-- Constraints for table `profiles_profile_investors_type`
--
ALTER TABLE `profiles_profile_investors_type`
  ADD CONSTRAINT `profiles_profile_inv_investor_id_22d560cb_fk_investor_` FOREIGN KEY (`investor_id`) REFERENCES `investor_investor` (`investor_id`),
  ADD CONSTRAINT `profiles_profile_inv_profile_id_9596efe2_fk_profiles_` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`profile_id`);

--
-- Constraints for table `profiles_profile_just_advise`
--
ALTER TABLE `profiles_profile_just_advise`
  ADD CONSTRAINT `profiles_profile_jus_advisor_id_08c19062_fk_advisor_a` FOREIGN KEY (`advisor_id`) REFERENCES `advisor_advisor` (`advisor_id`),
  ADD CONSTRAINT `profiles_profile_jus_profile_id_f50716ea_fk_profiles_` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`profile_id`);

--
-- Constraints for table `profiles_profile_just_invest`
--
ALTER TABLE `profiles_profile_just_invest`
  ADD CONSTRAINT `profiles_profile_jus_investor_id_c9579499_fk_investor_` FOREIGN KEY (`investor_id`) REFERENCES `investor_investor` (`investor_id`),
  ADD CONSTRAINT `profiles_profile_jus_profile_id_b4a0cee3_fk_profiles_` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`profile_id`);

--
-- Constraints for table `profiles_profile_just_sell`
--
ALTER TABLE `profiles_profile_just_sell`
  ADD CONSTRAINT `profiles_profile_jus_profile_id_21cb438d_fk_profiles_` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`profile_id`),
  ADD CONSTRAINT `profiles_profile_jus_seller1_id_1a6c63a2_fk_seller1_s` FOREIGN KEY (`seller1_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `profiles_profile_sell_type`
--
ALTER TABLE `profiles_profile_sell_type`
  ADD CONSTRAINT `profiles_profile_sel_profile_id_d07923e2_fk_profiles_` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`profile_id`),
  ADD CONSTRAINT `profiles_profile_sel_seller1_id_d5441616_fk_seller1_s` FOREIGN KEY (`seller1_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `profiles_profile_user_advise`
--
ALTER TABLE `profiles_profile_user_advise`
  ADD CONSTRAINT `profiles_profile_use_advise_id_e12d2822_fk_user_sell` FOREIGN KEY (`advise_id`) REFERENCES `user_seller_advise` (`advise_id`),
  ADD CONSTRAINT `profiles_profile_use_profile_id_d3ad2d4b_fk_profiles_` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`profile_id`);

--
-- Constraints for table `profiles_profile_user_invest`
--
ALTER TABLE `profiles_profile_user_invest`
  ADD CONSTRAINT `profiles_profile_use_invest_id_ca727dcb_fk_user_sell` FOREIGN KEY (`invest_id`) REFERENCES `user_seller_invest` (`invest_id`),
  ADD CONSTRAINT `profiles_profile_use_profile_id_480a77d7_fk_profiles_` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`profile_id`);

--
-- Constraints for table `profiles_profile_user_sell`
--
ALTER TABLE `profiles_profile_user_sell`
  ADD CONSTRAINT `profiles_profile_use_profile_id_f1102934_fk_profiles_` FOREIGN KEY (`profile_id`) REFERENCES `profiles_profile` (`profile_id`),
  ADD CONSTRAINT `profiles_profile_use_sell_id_3b49b4ca_fk_user_sell` FOREIGN KEY (`sell_id`) REFERENCES `user_seller_sell` (`sell_id`);

--
-- Constraints for table `seller1_raiseloan`
--
ALTER TABLE `seller1_raiseloan`
  ADD CONSTRAINT `seller1_raiseloan_seller_id_f2731d75_fk_seller1_s` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `seller1_revenuemodel`
--
ALTER TABLE `seller1_revenuemodel`
  ADD CONSTRAINT `seller1_revenuemodel_seller_id_8573a38f_fk_seller1_s` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `seller1_sellapp`
--
ALTER TABLE `seller1_sellapp`
  ADD CONSTRAINT `seller1_sellapp_seller_id_14658b52_fk_seller1_s` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `seller1_sellasset`
--
ALTER TABLE `seller1_sellasset`
  ADD CONSTRAINT `seller1_sellasset_seller_id_8692f172_fk_seller1_s` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `seller1_sellbusiness`
--
ALTER TABLE `seller1_sellbusiness`
  ADD CONSTRAINT `seller1_sellbusiness_seller_id_02ac42a7_fk_seller1_s` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `seller1_sellequity`
--
ALTER TABLE `seller1_sellequity`
  ADD CONSTRAINT `seller1_sellequity_seller_id_ca23bd33_fk_seller1_s` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `seller1_sellipcode`
--
ALTER TABLE `seller1_sellipcode`
  ADD CONSTRAINT `seller1_sellipcode_seller_id_47c3fe69_fk_seller1_s` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `seller1_sellstartup`
--
ALTER TABLE `seller1_sellstartup`
  ADD CONSTRAINT `seller1_sellstartup_seller_id_5094be29_fk_seller1_s` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `social_auth_usersocialauth`
--
ALTER TABLE `social_auth_usersocialauth`
  ADD CONSTRAINT `social_auth_usersocialauth_user_id_17d28448_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `user_seller_advise`
--
ALTER TABLE `user_seller_advise`
  ADD CONSTRAINT `user_seller_advise_advisor_id_005f0c78_fk_advisor_a` FOREIGN KEY (`advisor_id`) REFERENCES `advisor_advisor` (`advisor_id`);

--
-- Constraints for table `user_seller_advise_cart_invest`
--
ALTER TABLE `user_seller_advise_cart_invest`
  ADD CONSTRAINT `user_seller_advise_c_advise_id_841112b5_fk_user_sell` FOREIGN KEY (`advise_id`) REFERENCES `user_seller_advise` (`advise_id`),
  ADD CONSTRAINT `user_seller_advise_c_investor_id_b4cb96bd_fk_investor_` FOREIGN KEY (`investor_id`) REFERENCES `investor_investor` (`investor_id`);

--
-- Constraints for table `user_seller_advise_cart_seller`
--
ALTER TABLE `user_seller_advise_cart_seller`
  ADD CONSTRAINT `user_seller_advise_c_advise_id_560924fe_fk_user_sell` FOREIGN KEY (`advise_id`) REFERENCES `user_seller_advise` (`advise_id`),
  ADD CONSTRAINT `user_seller_advise_c_seller1_id_9247a68e_fk_seller1_s` FOREIGN KEY (`seller1_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `user_seller_advise_inst_invest`
--
ALTER TABLE `user_seller_advise_inst_invest`
  ADD CONSTRAINT `user_seller_advise_i_advise_id_4ba0663f_fk_user_sell` FOREIGN KEY (`advise_id`) REFERENCES `user_seller_advise` (`advise_id`),
  ADD CONSTRAINT `user_seller_advise_i_investor_id_a8750df7_fk_investor_` FOREIGN KEY (`investor_id`) REFERENCES `investor_investor` (`investor_id`);

--
-- Constraints for table `user_seller_advise_inst_seller`
--
ALTER TABLE `user_seller_advise_inst_seller`
  ADD CONSTRAINT `user_seller_advise_i_advise_id_21b01bc8_fk_user_sell` FOREIGN KEY (`advise_id`) REFERENCES `user_seller_advise` (`advise_id`),
  ADD CONSTRAINT `user_seller_advise_i_seller1_id_5fdec6ba_fk_seller1_s` FOREIGN KEY (`seller1_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `user_seller_invest`
--
ALTER TABLE `user_seller_invest`
  ADD CONSTRAINT `user_seller_invest_investor_id_969e4279_fk_investor_` FOREIGN KEY (`investor_id`) REFERENCES `investor_investor` (`investor_id`);

--
-- Constraints for table `user_seller_invest_cart_advisor`
--
ALTER TABLE `user_seller_invest_cart_advisor`
  ADD CONSTRAINT `user_seller_invest_c_advisor_id_3edca75a_fk_advisor_a` FOREIGN KEY (`advisor_id`) REFERENCES `advisor_advisor` (`advisor_id`),
  ADD CONSTRAINT `user_seller_invest_c_invest_id_d8e1860f_fk_user_sell` FOREIGN KEY (`invest_id`) REFERENCES `user_seller_invest` (`invest_id`);

--
-- Constraints for table `user_seller_invest_cart_seller`
--
ALTER TABLE `user_seller_invest_cart_seller`
  ADD CONSTRAINT `user_seller_invest_c_invest_id_a21132e1_fk_user_sell` FOREIGN KEY (`invest_id`) REFERENCES `user_seller_invest` (`invest_id`),
  ADD CONSTRAINT `user_seller_invest_c_seller1_id_735226e2_fk_seller1_s` FOREIGN KEY (`seller1_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `user_seller_invest_inst_advisor`
--
ALTER TABLE `user_seller_invest_inst_advisor`
  ADD CONSTRAINT `user_seller_invest_i_advisor_id_6e50b379_fk_advisor_a` FOREIGN KEY (`advisor_id`) REFERENCES `advisor_advisor` (`advisor_id`),
  ADD CONSTRAINT `user_seller_invest_i_invest_id_e9d51c64_fk_user_sell` FOREIGN KEY (`invest_id`) REFERENCES `user_seller_invest` (`invest_id`);

--
-- Constraints for table `user_seller_invest_inst_seller`
--
ALTER TABLE `user_seller_invest_inst_seller`
  ADD CONSTRAINT `user_seller_invest_i_invest_id_000c08a5_fk_user_sell` FOREIGN KEY (`invest_id`) REFERENCES `user_seller_invest` (`invest_id`),
  ADD CONSTRAINT `user_seller_invest_i_seller1_id_1e1d817c_fk_seller1_s` FOREIGN KEY (`seller1_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `user_seller_sell`
--
ALTER TABLE `user_seller_sell`
  ADD CONSTRAINT `user_seller_sell_seller_id_fb1ff177_fk_seller1_s` FOREIGN KEY (`seller_id`) REFERENCES `seller1_seller1` (`business_id`);

--
-- Constraints for table `user_seller_sell_cart_advisor`
--
ALTER TABLE `user_seller_sell_cart_advisor`
  ADD CONSTRAINT `user_seller_sell_car_advisor_id_ff26873b_fk_advisor_a` FOREIGN KEY (`advisor_id`) REFERENCES `advisor_advisor` (`advisor_id`),
  ADD CONSTRAINT `user_seller_sell_car_sell_id_2074f85f_fk_user_sell` FOREIGN KEY (`sell_id`) REFERENCES `user_seller_sell` (`sell_id`);

--
-- Constraints for table `user_seller_sell_cart_investor`
--
ALTER TABLE `user_seller_sell_cart_investor`
  ADD CONSTRAINT `user_seller_sell_car_investor_id_a8304aa0_fk_investor_` FOREIGN KEY (`investor_id`) REFERENCES `investor_investor` (`investor_id`),
  ADD CONSTRAINT `user_seller_sell_car_sell_id_c49c8a52_fk_user_sell` FOREIGN KEY (`sell_id`) REFERENCES `user_seller_sell` (`sell_id`);

--
-- Constraints for table `user_seller_sell_inst_advisor`
--
ALTER TABLE `user_seller_sell_inst_advisor`
  ADD CONSTRAINT `user_seller_sell_ins_advisor_id_33f51fe1_fk_advisor_a` FOREIGN KEY (`advisor_id`) REFERENCES `advisor_advisor` (`advisor_id`),
  ADD CONSTRAINT `user_seller_sell_ins_sell_id_0fedf470_fk_user_sell` FOREIGN KEY (`sell_id`) REFERENCES `user_seller_sell` (`sell_id`);

--
-- Constraints for table `user_seller_sell_inst_investors`
--
ALTER TABLE `user_seller_sell_inst_investors`
  ADD CONSTRAINT `user_seller_sell_ins_investor_id_ebd308ed_fk_investor_` FOREIGN KEY (`investor_id`) REFERENCES `investor_investor` (`investor_id`),
  ADD CONSTRAINT `user_seller_sell_ins_sell_id_493dad6d_fk_user_sell` FOREIGN KEY (`sell_id`) REFERENCES `user_seller_sell` (`sell_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
