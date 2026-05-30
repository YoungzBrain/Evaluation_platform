-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2026 at 09:30 PM
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
-- Database: `evaluate`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE `answers` (
  `id` int(11) UNSIGNED NOT NULL,
  `evaluation_id` int(11) UNSIGNED NOT NULL,
  `question_id` int(11) UNSIGNED NOT NULL,
  `score` int(1) DEFAULT NULL,
  `text_answer` text DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`id`, `evaluation_id`, `question_id`, `score`, `text_answer`, `created_at`, `updated_at`) VALUES
(5, 3, 1, 3, NULL, '2026-04-27 18:23:45', '2026-04-27 18:23:45'),
(6, 3, 2, 5, NULL, '2026-04-27 18:23:45', '2026-04-27 18:23:45'),
(7, 3, 3, 4, NULL, '2026-04-27 18:23:45', '2026-04-27 18:23:45'),
(8, 4, 1, 5, NULL, '2026-04-27 18:46:55', '2026-04-27 18:46:55'),
(9, 4, 2, 4, NULL, '2026-04-27 18:46:55', '2026-04-27 18:46:55'),
(10, 4, 3, 5, NULL, '2026-04-27 18:46:55', '2026-04-27 18:46:55'),
(11, 5, 1, 1, NULL, '2026-04-27 18:47:05', '2026-04-27 18:47:05'),
(12, 5, 2, 1, NULL, '2026-04-27 18:47:05', '2026-04-27 18:47:05'),
(13, 5, 3, 1, NULL, '2026-04-27 18:47:05', '2026-04-27 18:47:05'),
(14, 6, 1, 4, NULL, '2026-04-28 10:23:50', '2026-04-28 10:23:50'),
(15, 6, 2, 4, NULL, '2026-04-28 10:23:50', '2026-04-28 10:23:50'),
(16, 6, 3, 4, NULL, '2026-04-28 10:23:50', '2026-04-28 10:23:50'),
(17, 6, 4, NULL, 'He actually has a mastery of his course and he is quite punctual. and i find that very interesting', '2026-04-28 10:23:50', '2026-04-28 10:23:50'),
(18, 7, 1, 5, NULL, '2026-05-02 09:03:40', '2026-05-02 09:03:40'),
(19, 7, 2, 3, NULL, '2026-05-02 09:03:40', '2026-05-02 09:03:40'),
(20, 7, 3, 1, NULL, '2026-05-02 09:03:40', '2026-05-02 09:03:40'),
(21, 7, 4, NULL, 'very perfect', '2026-05-02 09:03:40', '2026-05-02 09:03:40'),
(22, 7, 5, 3, NULL, '2026-05-02 09:03:40', '2026-05-02 09:03:40'),
(23, 8, 1, 2, NULL, '2026-05-02 09:26:11', '2026-05-02 09:26:11'),
(24, 8, 2, 3, NULL, '2026-05-02 09:26:11', '2026-05-02 09:26:11'),
(25, 8, 3, 5, NULL, '2026-05-02 09:26:11', '2026-05-02 09:26:11'),
(26, 8, 4, NULL, 'he tries', '2026-05-02 09:26:11', '2026-05-02 09:26:11'),
(27, 8, 5, 4, NULL, '2026-05-02 09:26:11', '2026-05-02 09:26:11'),
(28, 9, 1, 3, NULL, '2026-05-02 09:31:26', '2026-05-02 09:31:26'),
(29, 9, 2, 3, NULL, '2026-05-02 09:31:26', '2026-05-02 09:31:26'),
(30, 9, 3, 3, NULL, '2026-05-02 09:31:26', '2026-05-02 09:31:26'),
(31, 9, 4, NULL, 'cool', '2026-05-02 09:31:26', '2026-05-02 09:31:26'),
(32, 9, 5, 3, NULL, '2026-05-02 09:31:26', '2026-05-02 09:31:26'),
(33, 10, 1, 4, NULL, '2026-05-02 11:41:32', '2026-05-02 11:41:32'),
(34, 10, 2, 4, NULL, '2026-05-02 11:41:32', '2026-05-02 11:41:32'),
(35, 10, 3, 4, NULL, '2026-05-02 11:41:32', '2026-05-02 11:41:32'),
(36, 10, 4, NULL, 'cool', '2026-05-02 11:41:32', '2026-05-02 11:41:32'),
(37, 10, 5, 3, NULL, '2026-05-02 11:41:32', '2026-05-02 11:41:32'),
(38, 11, 1, 1, NULL, '2026-05-02 11:51:28', '2026-05-02 11:51:28'),
(39, 11, 2, 1, NULL, '2026-05-02 11:51:28', '2026-05-02 11:51:28'),
(40, 11, 3, 1, NULL, '2026-05-02 11:51:28', '2026-05-02 11:51:28'),
(41, 11, 4, NULL, 'cool', '2026-05-02 11:51:28', '2026-05-02 11:51:28'),
(42, 11, 5, 1, NULL, '2026-05-02 11:51:28', '2026-05-02 11:51:28'),
(43, 12, 1, 4, NULL, '2026-05-11 08:54:10', '2026-05-11 08:54:10'),
(44, 12, 2, 4, NULL, '2026-05-11 08:54:10', '2026-05-11 08:54:10'),
(45, 12, 3, 3, NULL, '2026-05-11 08:54:10', '2026-05-11 08:54:10'),
(46, 12, 4, NULL, 'yesssssss', '2026-05-11 08:54:10', '2026-05-11 08:54:10'),
(47, 12, 5, 3, NULL, '2026-05-11 08:54:10', '2026-05-11 08:54:10');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) UNSIGNED NOT NULL,
  `name` varchar(150) NOT NULL,
  `description` text DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`, `description`, `created_at`, `updated_at`) VALUES
(1, 'ethique', 'punctualite', '2026-04-27 14:36:01', '2026-04-27 14:36:01');

-- --------------------------------------------------------

--
-- Table structure for table `courses`
--

CREATE TABLE `courses` (
  `id` int(11) UNSIGNED NOT NULL,
  `name` varchar(150) NOT NULL,
  `description` text DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`id`, `name`, `description`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'math', 'analyse', 1, '2026-04-27 14:35:26', '2026-04-27 14:35:26'),
(2, 'Web developement', 'design web page', 1, '2026-04-27 14:43:13', '2026-04-27 14:43:13'),
(3, 'Atelier de programmation', 'Python', 1, '2026-04-27 18:05:17', '2026-04-27 18:05:17'),
(4, 'Law', 'Droit de TIC', 1, '2026-04-28 10:21:58', '2026-04-28 10:21:58'),
(5, 'POO', 'Programmation oriente objet\r\n', 1, '2026-05-02 09:24:29', '2026-05-02 09:24:29');

-- --------------------------------------------------------

--
-- Table structure for table `evaluations`
--

CREATE TABLE `evaluations` (
  `id` int(11) UNSIGNED NOT NULL,
  `student_id` int(11) UNSIGNED NOT NULL,
  `teacher_id` int(11) UNSIGNED NOT NULL,
  `course_id` int(11) UNSIGNED NOT NULL,
  `status` enum('pending','submitted') NOT NULL DEFAULT 'pending',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `evaluations`
--

INSERT INTO `evaluations` (`id`, `student_id`, `teacher_id`, `course_id`, `status`, `created_at`, `updated_at`) VALUES
(3, 6, 7, 1, 'submitted', '2026-04-27 18:23:45', '2026-04-27 18:23:45'),
(4, 6, 4, 2, 'submitted', '2026-04-27 18:46:55', '2026-04-27 18:46:55'),
(5, 6, 4, 3, 'submitted', '2026-04-27 18:47:05', '2026-04-27 18:47:05'),
(6, 6, 7, 4, 'submitted', '2026-04-28 10:23:50', '2026-04-28 10:23:50'),
(7, 6, 8, 2, 'submitted', '2026-05-02 09:03:40', '2026-05-02 09:03:40'),
(8, 6, 4, 5, 'submitted', '2026-05-02 09:26:11', '2026-05-02 09:26:11'),
(9, 9, 4, 2, 'submitted', '2026-05-02 09:31:26', '2026-05-02 09:31:26'),
(10, 9, 8, 2, 'submitted', '2026-05-02 11:41:32', '2026-05-02 11:41:32'),
(11, 9, 7, 1, 'submitted', '2026-05-02 11:51:28', '2026-05-02 11:51:28'),
(12, 9, 4, 3, 'submitted', '2026-05-11 08:54:10', '2026-05-11 08:54:10');

-- --------------------------------------------------------

--
-- Table structure for table `evaluation_pdfs`
--

CREATE TABLE `evaluation_pdfs` (
  `id` int(11) UNSIGNED NOT NULL,
  `evaluation_id` int(11) UNSIGNED NOT NULL,
  `file_path` varchar(255) NOT NULL,
  `generated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `evaluation_pdfs`
--

INSERT INTO `evaluation_pdfs` (`id`, `evaluation_id`, `file_path`, `generated_at`) VALUES
(1, 3, 'evaluation_3_20260427182345.pdf', '2026-04-27 18:23:46'),
(2, 4, 'evaluation_4_20260427184655.pdf', '2026-04-27 18:46:55'),
(3, 5, 'evaluation_5_20260427184705.pdf', '2026-04-27 18:47:06'),
(4, 6, 'evaluation_6_20260428102350.pdf', '2026-04-28 10:23:55'),
(5, 7, 'evaluation_7_20260502090340.pdf', '2026-05-02 09:03:44'),
(6, 8, 'evaluation_8_20260502092611.pdf', '2026-05-02 09:26:11'),
(7, 9, 'evaluation_9_20260502093126.pdf', '2026-05-02 09:31:26'),
(8, 10, 'evaluation_10_20260502114132.pdf', '2026-05-02 11:41:34'),
(9, 11, 'evaluation_11_20260502115128.pdf', '2026-05-02 11:51:28'),
(10, 12, 'evaluation_12_20260511085410.pdf', '2026-05-11 08:54:11');

-- --------------------------------------------------------

--
-- Table structure for table `migrations`
--

CREATE TABLE `migrations` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `version` varchar(255) NOT NULL,
  `class` varchar(255) NOT NULL,
  `group` varchar(255) NOT NULL,
  `namespace` varchar(255) NOT NULL,
  `time` int(11) NOT NULL,
  `batch` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `migrations`
--

INSERT INTO `migrations` (`id`, `version`, `class`, `group`, `namespace`, `time`, `batch`) VALUES
(1, '2026-04-25-000001', 'App\\Database\\Migrations\\CreateUsersTable', 'default', 'App', 1777116094, 1),
(2, '2026-04-27-000002', 'App\\Database\\Migrations\\CreateCoursesTable', 'default', 'App', 1777300453, 2),
(3, '2026-04-27-000003', 'App\\Database\\Migrations\\CreateTeacherCoursesTable', 'default', 'App', 1777300453, 2),
(4, '2026-04-27-000004', 'App\\Database\\Migrations\\CreateCategoriesTable', 'default', 'App', 1777300453, 2),
(5, '2026-04-27-000005', 'App\\Database\\Migrations\\CreateQuestionsTable', 'default', 'App', 1777300453, 2),
(6, '2026-04-27-000006', 'App\\Database\\Migrations\\CreateEvaluationsTable', 'default', 'App', 1777301786, 3),
(7, '2026-04-27-000007', 'App\\Database\\Migrations\\CreateAnswersTable', 'default', 'App', 1777301786, 3),
(8, '2026-04-27-000006', 'App\\Database\\Migrations\\CreateEvaluationPdfsTable', 'default', 'App', 1777313805, 4);

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(11) UNSIGNED NOT NULL,
  `text` text NOT NULL,
  `type` enum('scored','open') NOT NULL DEFAULT 'scored',
  `category_id` int(11) UNSIGNED DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `text`, `type`, `category_id`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'is this teacher punctual?', 'scored', 1, 1, '2026-04-27 14:36:38', '2026-04-27 14:36:38'),
(2, 'Does this teacher have a mastery of their course', 'scored', 1, 1, '2026-04-27 18:03:27', '2026-04-27 18:03:27'),
(3, 'Does this teacher leave on time?', 'scored', 1, 1, '2026-04-27 18:03:52', '2026-04-27 18:03:52'),
(4, 'Describe your teacher in some few words', 'open', 1, 1, '2026-04-28 10:21:12', '2026-04-28 10:21:12'),
(5, 'faites vous les corrections apres evaluations', 'scored', 1, 1, '2026-05-02 08:58:08', '2026-05-02 08:58:08');

-- --------------------------------------------------------

--
-- Table structure for table `teacher_courses`
--

CREATE TABLE `teacher_courses` (
  `id` int(11) UNSIGNED NOT NULL,
  `teacher_id` int(11) UNSIGNED NOT NULL,
  `course_id` int(11) UNSIGNED NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teacher_courses`
--

INSERT INTO `teacher_courses` (`id`, `teacher_id`, `course_id`, `created_at`, `updated_at`) VALUES
(5, 7, 1, '2026-04-28 10:22:17', '2026-04-28 10:22:17'),
(6, 7, 4, '2026-04-28 10:22:17', '2026-04-28 10:22:17'),
(7, 8, 2, '2026-05-02 09:02:22', '2026-05-02 09:02:22'),
(8, 4, 2, '2026-05-02 09:25:15', '2026-05-02 09:25:15'),
(9, 4, 3, '2026-05-02 09:25:15', '2026-05-02 09:25:15'),
(10, 4, 5, '2026-05-02 09:25:15', '2026-05-02 09:25:15');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) UNSIGNED NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `matricule` varchar(50) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','teacher','student') NOT NULL DEFAULT 'student',
  `is_active` tinyint(1) NOT NULL DEFAULT 1,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `email`, `matricule`, `password`, `role`, `is_active`, `created_at`, `updated_at`) VALUES
(1, 'Administrateur', 'admin@school.cm', NULL, '$2y$10$YlBmBuuHyxrR28ZZ4s9VLet2MOG961epZ5Jh7A9wlRfy5SC23G6ym', 'admin', 1, '2026-04-25 11:27:24', '2026-04-25 11:27:24'),
(4, 'Dr. Abdoulaziz', 'teacher2@gmail.com', NULL, '$2y$10$K28SIqxaKV4fuoU5NlESPu08xKFUjCGhlVPgw5jeRYCpJI2EXrpTy', 'teacher', 1, '2026-04-27 09:37:13', '2026-04-27 18:46:19'),
(6, 'Diyen Yem Brian', 'youngzbrain1@gmail.com', '22E0466EP', '$2y$10$6TydkqRDbu1vzCH3upIxVuR5LqDkKANpZ/kf/7AobQCD5pg/s3MQi', 'student', 1, '2026-04-27 09:42:15', '2026-04-27 09:54:27'),
(7, 'Mr. Touza', 'teacher1@gmail.com', NULL, '$2y$10$5L05rFfdz7t20DbGryo9ZeVBrS.mbFoYSE.u4JV2QtS1zmqUW8Cri', 'teacher', 1, '2026-04-27 18:22:52', '2026-04-27 18:22:52'),
(8, 'Dr Onesime', 'onesime@gmail.com', NULL, '$2y$10$CO2wEu.Jrbngmfi2lIa9.e8kun3ZzT6aWZ.uPjXj/a6ofhx9t1mDy', 'teacher', 1, '2026-05-02 09:02:00', '2026-05-02 09:02:00'),
(9, 'student1', 'student1@gmail.com', 'ET001', '$2y$10$WX17kQbrCJBloLr8.FiubOCkRlaw7LFbdGzRw/kKPaI7DmIVbrDVm', 'student', 1, '2026-05-02 09:30:12', '2026-05-02 09:30:12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `answers_evaluation_id_foreign` (`evaluation_id`),
  ADD KEY `answers_question_id_foreign` (`question_id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `courses`
--
ALTER TABLE `courses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `evaluations`
--
ALTER TABLE `evaluations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `evaluations_student_id_foreign` (`student_id`),
  ADD KEY `evaluations_teacher_id_foreign` (`teacher_id`),
  ADD KEY `evaluations_course_id_foreign` (`course_id`);

--
-- Indexes for table `evaluation_pdfs`
--
ALTER TABLE `evaluation_pdfs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `evaluation_pdfs_evaluation_id_foreign` (`evaluation_id`);

--
-- Indexes for table `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `questions_category_id_foreign` (`category_id`);

--
-- Indexes for table `teacher_courses`
--
ALTER TABLE `teacher_courses`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `teacher_id_course_id` (`teacher_id`,`course_id`),
  ADD KEY `teacher_courses_course_id_foreign` (`course_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answers`
--
ALTER TABLE `answers`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `courses`
--
ALTER TABLE `courses`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `evaluations`
--
ALTER TABLE `evaluations`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `evaluation_pdfs`
--
ALTER TABLE `evaluation_pdfs`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `teacher_courses`
--
ALTER TABLE `teacher_courses`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `answers_evaluation_id_foreign` FOREIGN KEY (`evaluation_id`) REFERENCES `evaluations` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `answers_question_id_foreign` FOREIGN KEY (`question_id`) REFERENCES `questions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `evaluations`
--
ALTER TABLE `evaluations`
  ADD CONSTRAINT `evaluations_course_id_foreign` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `evaluations_student_id_foreign` FOREIGN KEY (`student_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `evaluations_teacher_id_foreign` FOREIGN KEY (`teacher_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `evaluation_pdfs`
--
ALTER TABLE `evaluation_pdfs`
  ADD CONSTRAINT `evaluation_pdfs_evaluation_id_foreign` FOREIGN KEY (`evaluation_id`) REFERENCES `evaluations` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_category_id_foreign` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE SET NULL ON UPDATE SET NULL;

--
-- Constraints for table `teacher_courses`
--
ALTER TABLE `teacher_courses`
  ADD CONSTRAINT `teacher_courses_course_id_foreign` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `teacher_courses_teacher_id_foreign` FOREIGN KEY (`teacher_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
