/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 8.0.23 : Database - djangovue
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`djangovue` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `djangovue`;

/*Table structure for table `api_sql` */

DROP TABLE IF EXISTS `api_sql`;

CREATE TABLE `api_sql` (
  `uid` varchar(64) NOT NULL,
  `statue` smallint NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(64) NOT NULL,
  `sql` varchar(640) NOT NULL,
  `is_all` tinyint(1) NOT NULL,
  `field_list` varchar(320) NOT NULL,
  `owner_id` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  KEY `api_sql_owner_id_4ab65b05_fk_user_user_id` (`owner_id`),
  CONSTRAINT `api_sql_owner_id_4ab65b05_fk_user_user_id` FOREIGN KEY (`owner_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `api_sql` */

/*Table structure for table `api_sql_case` */

DROP TABLE IF EXISTS `api_sql_case`;

CREATE TABLE `api_sql_case` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `sql_id` varchar(64) NOT NULL,
  `testcase_id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_sql_case_sql_id_testcase_id_29fdc418_uniq` (`sql_id`,`testcase_id`),
  KEY `api_sql_case_testcase_id_7e9e2002_fk_case_uid` (`testcase_id`),
  CONSTRAINT `api_sql_case_sql_id_afd50b64_fk_api_sql_uid` FOREIGN KEY (`sql_id`) REFERENCES `api_sql` (`uid`),
  CONSTRAINT `api_sql_case_testcase_id_7e9e2002_fk_case_uid` FOREIGN KEY (`testcase_id`) REFERENCES `case` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `api_sql_case` */

/*Table structure for table `api_white_list` */

DROP TABLE IF EXISTS `api_white_list`;

CREATE TABLE `api_white_list` (
  `coremodel_ptr_id` bigint NOT NULL,
  `url` varchar(200) NOT NULL,
  `method` int DEFAULT NULL,
  `enable_datasource` tinyint(1) NOT NULL,
  PRIMARY KEY (`coremodel_ptr_id`),
  CONSTRAINT `api_white_list_coremodel_ptr_id_17e30fb9_fk_public_coremodel_id` FOREIGN KEY (`coremodel_ptr_id`) REFERENCES `public_coremodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `api_white_list` */

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add content type',4,'add_contenttype'),
(14,'Can change content type',4,'change_contenttype'),
(15,'Can delete content type',4,'delete_contenttype'),
(16,'Can view content type',4,'view_contenttype'),
(17,'Can add session',5,'add_session'),
(18,'Can change session',5,'change_session'),
(19,'Can delete session',5,'delete_session'),
(20,'Can view session',5,'view_session'),
(21,'Can add django job',6,'add_djangojob'),
(22,'Can change django job',6,'change_djangojob'),
(23,'Can delete django job',6,'delete_djangojob'),
(24,'Can view django job',6,'view_djangojob'),
(25,'Can add django job execution',7,'add_djangojobexecution'),
(26,'Can change django job execution',7,'change_djangojobexecution'),
(27,'Can delete django job execution',7,'delete_djangojobexecution'),
(28,'Can view django job execution',7,'view_djangojobexecution'),
(29,'Can add task result',8,'add_taskresult'),
(30,'Can change task result',8,'change_taskresult'),
(31,'Can delete task result',8,'delete_taskresult'),
(32,'Can view task result',8,'view_taskresult'),
(33,'Can add chord counter',9,'add_chordcounter'),
(34,'Can change chord counter',9,'change_chordcounter'),
(35,'Can delete chord counter',9,'delete_chordcounter'),
(36,'Can view chord counter',9,'view_chordcounter'),
(37,'Can add group result',10,'add_groupresult'),
(38,'Can change group result',10,'change_groupresult'),
(39,'Can delete group result',10,'delete_groupresult'),
(40,'Can view group result',10,'view_groupresult'),
(41,'Can add crontab',11,'add_crontabschedule'),
(42,'Can change crontab',11,'change_crontabschedule'),
(43,'Can delete crontab',11,'delete_crontabschedule'),
(44,'Can view crontab',11,'view_crontabschedule'),
(45,'Can add interval',12,'add_intervalschedule'),
(46,'Can change interval',12,'change_intervalschedule'),
(47,'Can delete interval',12,'delete_intervalschedule'),
(48,'Can view interval',12,'view_intervalschedule'),
(49,'Can add periodic task',13,'add_periodictask'),
(50,'Can change periodic task',13,'change_periodictask'),
(51,'Can delete periodic task',13,'delete_periodictask'),
(52,'Can view periodic task',13,'view_periodictask'),
(53,'Can add periodic tasks',14,'add_periodictasks'),
(54,'Can change periodic tasks',14,'change_periodictasks'),
(55,'Can delete periodic tasks',14,'delete_periodictasks'),
(56,'Can view periodic tasks',14,'view_periodictasks'),
(57,'Can add solar event',15,'add_solarschedule'),
(58,'Can change solar event',15,'change_solarschedule'),
(59,'Can delete solar event',15,'delete_solarschedule'),
(60,'Can view solar event',15,'view_solarschedule'),
(61,'Can add clocked',16,'add_clockedschedule'),
(62,'Can change clocked',16,'change_clockedschedule'),
(63,'Can delete clocked',16,'delete_clockedschedule'),
(64,'Can view clocked',16,'view_clockedschedule'),
(65,'Can add crontab exec id',17,'add_crontabexecid'),
(66,'Can change crontab exec id',17,'change_crontabexecid'),
(67,'Can delete crontab exec id',17,'delete_crontabexecid'),
(68,'Can view crontab exec id',17,'view_crontabexecid'),
(69,'Can add execution record',18,'add_executionrecord'),
(70,'Can change execution record',18,'change_executionrecord'),
(71,'Can delete execution record',18,'delete_executionrecord'),
(72,'Can view execution record',18,'view_executionrecord'),
(73,'Can add execution request backup',19,'add_executionrequestbackup'),
(74,'Can change execution request backup',19,'change_executionrequestbackup'),
(75,'Can delete execution request backup',19,'delete_executionrequestbackup'),
(76,'Can view execution request backup',19,'view_executionrequestbackup'),
(77,'Can add project',20,'add_project'),
(78,'Can change project',20,'change_project'),
(79,'Can delete project',20,'delete_project'),
(80,'Can view project',20,'view_project'),
(81,'Can add scenario',21,'add_scenario'),
(82,'Can change scenario',21,'change_scenario'),
(83,'Can delete scenario',21,'delete_scenario'),
(84,'Can view scenario',21,'view_scenario'),
(85,'Can add sql',22,'add_sql'),
(86,'Can change sql',22,'change_sql'),
(87,'Can delete sql',22,'delete_sql'),
(88,'Can view sql',22,'view_sql'),
(89,'Can add templates',23,'add_templates'),
(90,'Can change templates',23,'change_templates'),
(91,'Can delete templates',23,'delete_templates'),
(92,'Can view templates',23,'view_templates'),
(93,'Can add test case',24,'add_testcase'),
(94,'Can change test case',24,'change_testcase'),
(95,'Can delete test case',24,'delete_testcase'),
(96,'Can view test case',24,'view_testcase'),
(97,'Can add test suit',25,'add_testsuit'),
(98,'Can change test suit',25,'change_testsuit'),
(99,'Can delete test suit',25,'delete_testsuit'),
(100,'Can view test suit',25,'view_testsuit'),
(101,'Can add menu',26,'add_menu'),
(102,'Can change menu',26,'change_menu'),
(103,'Can delete menu',26,'delete_menu'),
(104,'Can view menu',26,'view_menu'),
(105,'Can add role',27,'add_role'),
(106,'Can change role',27,'change_role'),
(107,'Can delete role',27,'delete_role'),
(108,'Can view role',27,'view_role'),
(109,'Can add user profile',28,'add_userprofile'),
(110,'Can change user profile',28,'change_userprofile'),
(111,'Can delete user profile',28,'delete_userprofile'),
(112,'Can view user profile',28,'view_userprofile'),
(113,'Can add core model',29,'add_coremodel'),
(114,'Can change core model',29,'change_coremodel'),
(115,'Can delete core model',29,'delete_coremodel'),
(116,'Can view core model',29,'view_coremodel'),
(117,'Can add 接口白名单',30,'add_apiwhitelist'),
(118,'Can change 接口白名单',30,'change_apiwhitelist'),
(119,'Can delete 接口白名单',30,'delete_apiwhitelist'),
(120,'Can view 接口白名单',30,'view_apiwhitelist'),
(121,'Can add 操作日志',31,'add_operationlog'),
(122,'Can change 操作日志',31,'change_operationlog'),
(123,'Can delete 操作日志',31,'delete_operationlog'),
(124,'Can view 操作日志',31,'view_operationlog');

/*Table structure for table `case` */

DROP TABLE IF EXISTS `case`;

CREATE TABLE `case` (
  `uid` varchar(64) NOT NULL,
  `statue` smallint NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `case` varchar(64) NOT NULL,
  `case_title` varchar(100) NOT NULL,
  `case_description` varchar(320) DEFAULT NULL,
  `priority` smallint NOT NULL,
  `owner_id` varchar(32) DEFAULT NULL,
  `template_id` varchar(64) NOT NULL,
  `testsuit_id` varchar(64) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `case` (`case`),
  KEY `case_owner_id_b7e73fc8_fk_user_user_id` (`owner_id`),
  KEY `case_template_id_9f7552fc_fk_templates_uid` (`template_id`),
  KEY `case_testsuit_id_fb6f0016_fk_suit_uid` (`testsuit_id`),
  KEY `case_case_1b6f0c_idx` (`case`),
  CONSTRAINT `case_owner_id_b7e73fc8_fk_user_user_id` FOREIGN KEY (`owner_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `case_template_id_9f7552fc_fk_templates_uid` FOREIGN KEY (`template_id`) REFERENCES `templates` (`uid`),
  CONSTRAINT `case_testsuit_id_fb6f0016_fk_suit_uid` FOREIGN KEY (`testsuit_id`) REFERENCES `suit` (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `case` */

insert  into `case`(`uid`,`statue`,`create_time`,`update_time`,`case`,`case_title`,`case_description`,`priority`,`owner_id`,`template_id`,`testsuit_id`) values 
('3a1407fea7264dbb8a077b18cc8de6cf',1,'2022-07-16 11:58:46.408015','2022-07-16 11:58:46.408015','auth_api','用例登录接口','用例登录接口',0,'root','219baffcb4cb4c33956526fe2deef0ff','9ecea461b8ef4b6fab80cc05451151a4');

/*Table structure for table `crontab_exec` */

DROP TABLE IF EXISTS `crontab_exec`;

CREATE TABLE `crontab_exec` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `code` varchar(64) DEFAULT NULL,
  `task` varchar(64) DEFAULT NULL,
  `task_type` smallint DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `crontab_exe_code_2cf70d_idx` (`code`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `crontab_exec` */

insert  into `crontab_exec`(`id`,`code`,`task`,`task_type`,`create_time`) values 
(1,'EXEC_E7B1259FF7E74D57B668E78BFFFF31EC','CRONbf4dc689324647a1bd18e68d864b2a50',1,'2022-07-16 12:00:19.716504'),
(2,'EXEC_20A7E053BE10425C958FB48454D045BE','PERIOD8115f26e4d2a46f282ebd3bbc1d939d7',2,'2022-07-16 12:00:28.682514');

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_apscheduler_djangojob` */

DROP TABLE IF EXISTS `django_apscheduler_djangojob`;

CREATE TABLE `django_apscheduler_djangojob` (
  `id` varchar(255) NOT NULL,
  `next_run_time` datetime(6) DEFAULT NULL,
  `job_state` longblob NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_apscheduler_djangojob_next_run_time_2f022619` (`next_run_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_apscheduler_djangojob` */

/*Table structure for table `django_apscheduler_djangojobexecution` */

DROP TABLE IF EXISTS `django_apscheduler_djangojobexecution`;

CREATE TABLE `django_apscheduler_djangojobexecution` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(50) NOT NULL,
  `run_time` datetime(6) NOT NULL,
  `duration` decimal(15,2) DEFAULT NULL,
  `finished` decimal(15,2) DEFAULT NULL,
  `exception` varchar(1000) DEFAULT NULL,
  `traceback` longtext,
  `job_id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_job_executions` (`job_id`,`run_time`),
  KEY `django_apscheduler_djangojobexecution_run_time_16edd96b` (`run_time`),
  CONSTRAINT `django_apscheduler_djangojobexecution_job_id_daf5090a_fk` FOREIGN KEY (`job_id`) REFERENCES `django_apscheduler_djangojob` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_apscheduler_djangojobexecution` */

/*Table structure for table `django_celery_beat_clockedschedule` */

DROP TABLE IF EXISTS `django_celery_beat_clockedschedule`;

CREATE TABLE `django_celery_beat_clockedschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `clocked_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_celery_beat_clockedschedule` */

/*Table structure for table `django_celery_beat_crontabschedule` */

DROP TABLE IF EXISTS `django_celery_beat_crontabschedule`;

CREATE TABLE `django_celery_beat_crontabschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `minute` varchar(240) NOT NULL,
  `hour` varchar(96) NOT NULL,
  `day_of_week` varchar(64) NOT NULL,
  `day_of_month` varchar(124) NOT NULL,
  `month_of_year` varchar(64) NOT NULL,
  `timezone` varchar(63) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_celery_beat_crontabschedule` */

insert  into `django_celery_beat_crontabschedule`(`id`,`minute`,`hour`,`day_of_week`,`day_of_month`,`month_of_year`,`timezone`) values 
(1,'0','4','*','*','*','Asia/Shanghai'),
(2,'30','5','*','*','*','Asia/Shanghai'),
(3,'0','6','*','*','*','Asia/Shanghai'),
(4,'59','23','*','*','*','Asia/Shanghai'),
(5,'17','12','*','16','7','Asia/Shanghai');

/*Table structure for table `django_celery_beat_intervalschedule` */

DROP TABLE IF EXISTS `django_celery_beat_intervalschedule`;

CREATE TABLE `django_celery_beat_intervalschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `every` int NOT NULL,
  `period` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_celery_beat_intervalschedule` */

insert  into `django_celery_beat_intervalschedule`(`id`,`every`,`period`) values 
(1,7200,'seconds'),
(2,10,'minutes');

/*Table structure for table `django_celery_beat_periodictask` */

DROP TABLE IF EXISTS `django_celery_beat_periodictask`;

CREATE TABLE `django_celery_beat_periodictask` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `task` varchar(200) NOT NULL,
  `args` longtext NOT NULL,
  `kwargs` longtext NOT NULL,
  `queue` varchar(200) DEFAULT NULL,
  `exchange` varchar(200) DEFAULT NULL,
  `routing_key` varchar(200) DEFAULT NULL,
  `expires` datetime(6) DEFAULT NULL,
  `enabled` tinyint(1) NOT NULL,
  `last_run_at` datetime(6) DEFAULT NULL,
  `total_run_count` int unsigned NOT NULL,
  `date_changed` datetime(6) NOT NULL,
  `description` longtext NOT NULL,
  `crontab_id` int DEFAULT NULL,
  `interval_id` int DEFAULT NULL,
  `solar_id` int DEFAULT NULL,
  `one_off` tinyint(1) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `priority` int unsigned DEFAULT NULL,
  `headers` longtext NOT NULL DEFAULT (_utf8mb3'{}'),
  `clocked_id` int DEFAULT NULL,
  `expire_seconds` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` (`crontab_id`),
  KEY `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` (`interval_id`),
  KEY `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` (`solar_id`),
  KEY `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` (`clocked_id`),
  CONSTRAINT `django_celery_beat_p_clocked_id_47a69f82_fk_django_ce` FOREIGN KEY (`clocked_id`) REFERENCES `django_celery_beat_clockedschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_crontab_id_d3cba168_fk_django_ce` FOREIGN KEY (`crontab_id`) REFERENCES `django_celery_beat_crontabschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_interval_id_a8ca27da_fk_django_ce` FOREIGN KEY (`interval_id`) REFERENCES `django_celery_beat_intervalschedule` (`id`),
  CONSTRAINT `django_celery_beat_p_solar_id_a87ce72c_fk_django_ce` FOREIGN KEY (`solar_id`) REFERENCES `django_celery_beat_solarschedule` (`id`),
  CONSTRAINT `django_celery_beat_periodictask_chk_1` CHECK ((`total_run_count` >= 0)),
  CONSTRAINT `django_celery_beat_periodictask_chk_2` CHECK ((`priority` >= 0)),
  CONSTRAINT `django_celery_beat_periodictask_chk_3` CHECK ((`expire_seconds` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_celery_beat_periodictask` */

insert  into `django_celery_beat_periodictask`(`id`,`name`,`task`,`args`,`kwargs`,`queue`,`exchange`,`routing_key`,`expires`,`enabled`,`last_run_at`,`total_run_count`,`date_changed`,`description`,`crontab_id`,`interval_id`,`solar_id`,`one_off`,`start_time`,`priority`,`headers`,`clocked_id`,`expire_seconds`) values 
(1,'celery.backend_cleanup','celery.backend_cleanup','[]','{}',NULL,NULL,NULL,NULL,1,'2022-07-17 01:26:07.313938',1,'2022-07-17 09:26:37.427159','',1,NULL,NULL,0,NULL,NULL,'{}',NULL,43200),
(2,'clean_logs_job','sse.celery_job.jobs.clean_logs_job','[7]','{}',NULL,NULL,NULL,NULL,1,'2022-07-17 01:26:07.330591',1,'2022-07-17 09:26:37.436168','',2,NULL,NULL,0,NULL,NULL,'{}',NULL,NULL),
(3,'clean_reports_job','sse.celery_job.jobs.clean_reports_job','[]','{}',NULL,NULL,NULL,NULL,1,'2022-07-17 01:26:07.295223',6,'2022-07-17 09:26:37.403154','',NULL,1,NULL,0,NULL,NULL,'{}',NULL,NULL),
(4,'update_expired_job','sse.celery_job.jobs.update_expired_job','[]','{}',NULL,NULL,NULL,NULL,1,'2022-07-17 01:26:07.341199',1,'2022-07-17 09:26:37.411358','',3,NULL,NULL,0,NULL,NULL,'{}',NULL,NULL),
(5,'clean_cron_task_job','sse.celery_job.jobs.clean_cron_task_job','[]','{}',NULL,NULL,NULL,NULL,1,'2022-07-17 01:26:05.829018',1,'2022-07-17 09:26:37.390138','',4,NULL,NULL,0,NULL,NULL,'{}',NULL,NULL),
(6,'clear_period_task_job','sse.celery_job.jobs.clear_period_task_job','[]','{}',NULL,NULL,NULL,NULL,1,'2022-07-17 01:26:07.209586',1,'2022-07-17 09:26:37.419615','',4,NULL,NULL,0,NULL,NULL,'{}',NULL,NULL),
(7,'CRONbf4dc689324647a1bd18e68d864b2a50','sse.celery_job.tasks.celery_exec_request','[{\"exec_id\": \"EXEC_E7B1259FF7E74D57B668E78BFFFF31EC\", \"body\": [{\"uid\": \"3a1407fea7264dbb8a077b18cc8de6cf\", \"case_scenario\": [{\"uid\": \"e9b7c3b97f8d48739935e2c1f1633b85\", \"statue_display\": \"有效\", \"testcase\": \"auth_api\", \"case_title\": \"用例登录接口\", \"statue\": 1, \"create_time\": \"2022-07-16 11:59:21\", \"update_time\": \"2022-07-16 11:59:21\", \"scenario\": \"用户名和密码正确\", \"parameter\": {\"password@0\": \"aaaa1111!\", \"username@0\": \"admin\"}, \"validator\": {\"$.jwt@2@0\": \"e\"}, \"owner\": \"root\", \"cases\": \"3a1407fea7264dbb8a077b18cc8de6cf\"}], \"casetemplate\": {\"uid\": \"219baffcb4cb4c33956526fe2deef0ff\", \"statue_display\": \"有效\", \"method_display\": \"POST\", \"statue\": 1, \"create_time\": \"2022-07-16 11:57:47\", \"update_time\": \"2022-07-16 11:57:47\", \"name\": \"请求认证接口\", \"url\": \"http://192.168.44.129:9000/api/auth\", \"method\": 1, \"header\": {\"Content-Type\": \"application/json\"}, \"data\": {\"password\": \"{{password}}\", \"username\": \"{{username}}\"}, \"default\": [{\"val\": \"admin\", \"type\": 0, \"field\": \"username\"}, {\"val\": \"aaaa1111!\", \"type\": 0, \"field\": \"password\"}], \"process_name\": \"\", \"linux_order_str\": \"\", \"table_name\": \"\", \"owner\": \"root\"}, \"statue_display\": \"有效\", \"priority_display\": \"高\", \"module\": \"PORTAINER\", \"class_title\": \"容器云基本功能\", \"statue\": 1, \"create_time\": \"2022-07-16 11:58:46\", \"update_time\": \"2022-07-16 11:58:46\", \"case\": \"auth_api\", \"case_title\": \"用例登录接口\", \"case_description\": \"用例登录接口\", \"priority\": 0, \"owner\": \"root\", \"template\": \"219baffcb4cb4c33956526fe2deef0ff\", \"testsuit\": \"9ecea461b8ef4b6fab80cc05451151a4\", \"scenarios\": [[{\"password\": \"aaaa1111!\", \"username\": \"admin\"}, \"用户名和密码正确\", {\"$.jwt@2\": \"e\"}]]}]}, false]','{}',NULL,NULL,NULL,'2022-07-16 12:01:19.709552',1,'2022-07-16 04:17:00.001812',1,'2022-07-16 12:18:30.112924','',5,NULL,NULL,0,NULL,NULL,'{}',NULL,NULL);

/*Table structure for table `django_celery_beat_periodictasks` */

DROP TABLE IF EXISTS `django_celery_beat_periodictasks`;

CREATE TABLE `django_celery_beat_periodictasks` (
  `ident` smallint NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`ident`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_celery_beat_periodictasks` */

insert  into `django_celery_beat_periodictasks`(`ident`,`last_update`) values 
(1,'2022-07-17 09:26:33.850609');

/*Table structure for table `django_celery_beat_solarschedule` */

DROP TABLE IF EXISTS `django_celery_beat_solarschedule`;

CREATE TABLE `django_celery_beat_solarschedule` (
  `id` int NOT NULL AUTO_INCREMENT,
  `event` varchar(24) NOT NULL,
  `latitude` decimal(9,6) NOT NULL,
  `longitude` decimal(9,6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_celery_beat_solar_event_latitude_longitude_ba64999a_uniq` (`event`,`latitude`,`longitude`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_celery_beat_solarschedule` */

/*Table structure for table `django_celery_results_chordcounter` */

DROP TABLE IF EXISTS `django_celery_results_chordcounter`;

CREATE TABLE `django_celery_results_chordcounter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` varchar(255) NOT NULL,
  `sub_tasks` longtext NOT NULL,
  `count` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`),
  CONSTRAINT `django_celery_results_chordcounter_chk_1` CHECK ((`count` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_celery_results_chordcounter` */

/*Table structure for table `django_celery_results_groupresult` */

DROP TABLE IF EXISTS `django_celery_results_groupresult`;

CREATE TABLE `django_celery_results_groupresult` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` varchar(255) NOT NULL,
  `date_created` datetime(6) NOT NULL,
  `date_done` datetime(6) NOT NULL,
  `content_type` varchar(128) NOT NULL,
  `content_encoding` varchar(64) NOT NULL,
  `result` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`),
  KEY `django_cele_date_cr_bd6c1d_idx` (`date_created`),
  KEY `django_cele_date_do_caae0e_idx` (`date_done`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_celery_results_groupresult` */

/*Table structure for table `django_celery_results_taskresult` */

DROP TABLE IF EXISTS `django_celery_results_taskresult`;

CREATE TABLE `django_celery_results_taskresult` (
  `id` int NOT NULL AUTO_INCREMENT,
  `task_id` varchar(255) NOT NULL,
  `status` varchar(50) NOT NULL,
  `content_type` varchar(128) NOT NULL,
  `content_encoding` varchar(64) NOT NULL,
  `result` longtext,
  `date_done` datetime(6) NOT NULL,
  `traceback` longtext,
  `meta` longtext,
  `task_args` longtext,
  `task_kwargs` longtext,
  `task_name` varchar(255) DEFAULT NULL,
  `worker` varchar(100) DEFAULT NULL,
  `date_created` datetime(6) NOT NULL,
  `periodic_task_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `task_id` (`task_id`),
  KEY `django_cele_task_na_08aec9_idx` (`task_name`),
  KEY `django_cele_status_9b6201_idx` (`status`),
  KEY `django_cele_worker_d54dd8_idx` (`worker`),
  KEY `django_cele_date_cr_f04a50_idx` (`date_created`),
  KEY `django_cele_date_do_f59aad_idx` (`date_done`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_celery_results_taskresult` */

insert  into `django_celery_results_taskresult`(`id`,`task_id`,`status`,`content_type`,`content_encoding`,`result`,`date_done`,`traceback`,`meta`,`task_args`,`task_kwargs`,`task_name`,`worker`,`date_created`,`periodic_task_name`) values 
(1,'ec190549-03c5-47cf-a800-c575606e6e85','SUCCESS','application/json','utf-8','null','2022-07-16 11:59:37.499472',NULL,'{\"children\": []}','\"({\'exec_id\': \'EXEC_B8451DB116D84535996CCDA11A3843D7\', \'body\': [{...}]},)\"','\"{}\"','sse.celery_job.tasks.celery_exec_request','celery@Zhangwenke','2022-07-16 11:59:37.499472',NULL),
(2,'54c5d593-9bcc-4639-954c-ed4a672c7d15','SUCCESS','application/json','utf-8','null','2022-07-16 11:59:38.288989',NULL,'{\"children\": []}','\"({\'exec_id\': \'EXEC_B8451DB116D84535996CCDA11A3843D7\', \'success\': True, \'path\': \'/home/volume/incoming/20220716/EXEC_B8451DB116D84535996CCDA11A3843D7/EXEC_B8451DB116D84535996CCDA11A3843D7.html\', \'duration\': \'0.194\'},)\"','\"{}\"','sse.celery_job.tasks.celery_update','celery@Zhangwenke','2022-07-16 11:59:38.288989',NULL),
(3,'c48bfb95-8866-4875-aaed-33b4bb3b14c9','SUCCESS','application/json','utf-8','null','2022-07-16 12:10:33.296662',NULL,'{\"children\": []}','\"[{\'exec_id\': \'EXEC_20A7E053BE10425C958FB48454D045BE\', \'body\': [{...}]}, False]\"','\"{}\"','sse.celery_job.tasks.celery_exec_request','celery@Zhangwenke','2022-07-16 12:10:33.296662',NULL),
(4,'f746d589-df40-42c6-bf2e-4e5b26bd17c9','SUCCESS','application/json','utf-8','null','2022-07-16 12:10:33.728042',NULL,'{\"children\": []}','\"({\'exec_id\': \'EXEC_20A7E053BE10425C958FB48454D045BE\', \'success\': True, \'path\': \'/home/volume/incoming/20220716/EXEC_20A7E053BE10425C958FB48454D045BE/EXEC_20A7E053BE10425C958FB48454D045BE.html\', \'duration\': \'0.140\'},)\"','\"{}\"','sse.celery_job.tasks.celery_update','celery@Zhangwenke','2022-07-16 12:10:33.728042',NULL),
(5,'d6d8522e-fe5c-472c-bea1-3decb5785d18','SUCCESS','application/json','utf-8','null','2022-07-16 12:17:00.040794',NULL,'{\"children\": []}','\"[{\'exec_id\': \'EXEC_E7B1259FF7E74D57B668E78BFFFF31EC\', \'body\': [{...}]}, False]\"','\"{}\"','sse.celery_job.tasks.celery_exec_request','celery@Zhangwenke','2022-07-16 12:17:00.040794',NULL),
(6,'3179f14e-f4a2-441f-b706-506209c57aed','SUCCESS','application/json','utf-8','null','2022-07-16 12:17:00.479306',NULL,'{\"children\": []}','\"({\'exec_id\': \'EXEC_E7B1259FF7E74D57B668E78BFFFF31EC\', \'success\': True, \'path\': \'/home/volume/incoming/20220716/EXEC_E7B1259FF7E74D57B668E78BFFFF31EC/EXEC_E7B1259FF7E74D57B668E78BFFFF31EC.html\', \'duration\': \'0.140\'},)\"','\"{}\"','sse.celery_job.tasks.celery_update','celery@Zhangwenke','2022-07-16 12:17:00.479306',NULL),
(7,'d99b6aa7-1850-4771-83e9-ef324008791d','SUCCESS','application/json','utf-8','null','2022-07-16 12:20:33.248060',NULL,'{\"children\": []}','\"[{\'exec_id\': \'EXEC_20A7E053BE10425C958FB48454D045BE\', \'body\': [{...}]}, False]\"','\"{}\"','sse.celery_job.tasks.celery_exec_request','celery@Zhangwenke','2022-07-16 12:20:33.248060',NULL),
(8,'881d706a-11de-401a-b500-f4033afbdb44','SUCCESS','application/json','utf-8','null','2022-07-16 12:20:33.671092',NULL,'{\"children\": []}','\"({\'exec_id\': \'EXEC_20A7E053BE10425C958FB48454D045BE\', \'success\': True, \'path\': \'/home/volume/incoming/20220716/EXEC_20A7E053BE10425C958FB48454D045BE/EXEC_20A7E053BE10425C958FB48454D045BE.html\', \'duration\': \'0.135\'},)\"','\"{}\"','sse.celery_job.tasks.celery_update','celery@Zhangwenke','2022-07-16 12:20:33.671092',NULL),
(9,'306772d0-2db0-42d5-a5f7-cb1b2e30e416','SUCCESS','application/json','utf-8','null','2022-07-16 12:30:33.253828',NULL,'{\"children\": []}','\"[{\'exec_id\': \'EXEC_20A7E053BE10425C958FB48454D045BE\', \'body\': [{...}]}, False]\"','\"{}\"','sse.celery_job.tasks.celery_exec_request','celery@Zhangwenke','2022-07-16 12:30:33.253828',NULL),
(10,'74af87e0-174b-4a83-8aee-d71ee2a9cb02','SUCCESS','application/json','utf-8','null','2022-07-16 12:30:33.697070',NULL,'{\"children\": []}','\"({\'exec_id\': \'EXEC_20A7E053BE10425C958FB48454D045BE\', \'success\': True, \'path\': \'/home/volume/incoming/20220716/EXEC_20A7E053BE10425C958FB48454D045BE/EXEC_20A7E053BE10425C958FB48454D045BE.html\', \'duration\': \'0.145\'},)\"','\"{}\"','sse.celery_job.tasks.celery_update','celery@Zhangwenke','2022-07-16 12:30:33.697070',NULL),
(11,'7ae0b62b-54af-47e4-a500-833711589779','SUCCESS','application/json','utf-8','null','2022-07-16 14:30:38.273953',NULL,'{\"children\": []}','\"()\"','\"{}\"','sse.celery_job.jobs.clean_reports_job','celery@Zhangwenke','2022-07-16 14:30:38.273953',NULL),
(12,'dee60033-af8b-404c-ab79-3acc47d62b7c','SUCCESS','application/json','utf-8','null','2022-07-16 16:30:38.293558',NULL,'{\"children\": []}','\"()\"','\"{}\"','sse.celery_job.jobs.clean_reports_job','celery@Zhangwenke','2022-07-16 16:30:38.293558',NULL),
(13,'9b661a3c-ff90-4ca0-8509-07115d7a4a44','SUCCESS','application/json','utf-8','null','2022-07-16 18:30:38.294546',NULL,'{\"children\": []}','\"()\"','\"{}\"','sse.celery_job.jobs.clean_reports_job','celery@Zhangwenke','2022-07-16 18:30:38.294546',NULL),
(14,'b3cc7d04-8b88-446c-854f-5ae91988b937','SUCCESS','application/json','utf-8','null','2022-07-16 20:30:38.292692',NULL,'{\"children\": []}','\"()\"','\"{}\"','sse.celery_job.jobs.clean_reports_job','celery@Zhangwenke','2022-07-16 20:30:38.292692',NULL),
(15,'5768016b-7365-44bc-8a26-8088d65bcabc','SUCCESS','application/json','utf-8','null','2022-07-16 22:30:38.282431',NULL,'{\"children\": []}','\"()\"','\"{}\"','sse.celery_job.jobs.clean_reports_job','celery@Zhangwenke','2022-07-16 22:30:38.282431',NULL),
(16,'a2e10c39-6b1a-4dde-a98d-531b7d5e6aa6','SUCCESS','application/json','utf-8','null','2022-07-17 09:26:33.881642',NULL,'{\"children\": []}','\"()\"','\"{}\"','sse.celery_job.jobs.clean_reports_job','celery@Zhangwenke','2022-07-17 09:26:33.881642',NULL),
(17,'cdfd8afa-dfc4-4afd-9458-717ca0722705','FAILURE','application/json','utf-8','{\"exc_type\": \"AttributeError\", \"exc_message\": [\"type object \'datetime.datetime\' has no attribute \'datetime\'\"], \"exc_module\": \"builtins\"}','2022-07-17 09:26:33.906174','Traceback (most recent call last):\n  File \"C:\\Users\\ZWK\\Desktop\\virtual\\django-rest\\lib\\site-packages\\celery\\app\\trace.py\", line 451, in trace_task\n    R = retval = fun(*args, **kwargs)\n  File \"C:\\Users\\ZWK\\Desktop\\virtual\\django-rest\\lib\\site-packages\\celery\\app\\trace.py\", line 734, in __protected_call__\n    return self.run(*args, **kwargs)\n  File \"C:\\Users\\ZWK\\Desktop\\homespace\\django-controller\\sse\\celery_job\\jobs.py\", line 123, in clean_logs_job\n    delta_days = (datetime.datetime.now() - datetime.timedelta(days=n))\nAttributeError: type object \'datetime.datetime\' has no attribute \'datetime\'\n','{\"children\": []}','\"[7]\"','\"{}\"','sse.celery_job.jobs.clean_logs_job','celery@Zhangwenke','2022-07-17 09:26:33.906174',NULL),
(18,'559f8655-ea2f-413f-8e32-0f478f21c81e','SUCCESS','application/json','utf-8','null','2022-07-17 09:26:33.907176',NULL,'{\"children\": []}','\"()\"','\"{}\"','celery.backend_cleanup','celery@Zhangwenke','2022-07-17 09:26:33.906174',NULL),
(19,'01944593-1a27-4441-8d6b-9e07b73dfe15','SUCCESS','application/json','utf-8','null','2022-07-17 09:26:33.919612',NULL,'{\"children\": []}','\"()\"','\"{}\"','sse.celery_job.jobs.clear_period_task_job','celery@Zhangwenke','2022-07-17 09:26:33.919612',NULL),
(20,'cf61b93f-433c-4d81-b60d-d98a5f1eb655','SUCCESS','application/json','utf-8','null','2022-07-17 09:26:33.920612',NULL,'{\"children\": []}','\"()\"','\"{}\"','sse.celery_job.jobs.update_expired_job','celery@Zhangwenke','2022-07-17 09:26:33.920612',NULL);

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(17,'api','crontabexecid'),
(18,'api','executionrecord'),
(19,'api','executionrequestbackup'),
(20,'api','project'),
(21,'api','scenario'),
(22,'api','sql'),
(23,'api','templates'),
(24,'api','testcase'),
(25,'api','testsuit'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'contenttypes','contenttype'),
(6,'django_apscheduler','djangojob'),
(7,'django_apscheduler','djangojobexecution'),
(16,'django_celery_beat','clockedschedule'),
(11,'django_celery_beat','crontabschedule'),
(12,'django_celery_beat','intervalschedule'),
(13,'django_celery_beat','periodictask'),
(14,'django_celery_beat','periodictasks'),
(15,'django_celery_beat','solarschedule'),
(9,'django_celery_results','chordcounter'),
(10,'django_celery_results','groupresult'),
(8,'django_celery_results','taskresult'),
(30,'public','apiwhitelist'),
(29,'public','coremodel'),
(31,'public','operationlog'),
(5,'sessions','session'),
(26,'user','menu'),
(27,'user','role'),
(28,'user','userprofile');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2022-07-16 10:51:05.673282'),
(2,'contenttypes','0002_remove_content_type_name','2022-07-16 10:51:05.741919'),
(3,'auth','0001_initial','2022-07-16 10:51:05.941214'),
(4,'auth','0002_alter_permission_name_max_length','2022-07-16 10:51:05.988058'),
(5,'auth','0003_alter_user_email_max_length','2022-07-16 10:51:05.994068'),
(6,'auth','0004_alter_user_username_opts','2022-07-16 10:51:06.001091'),
(7,'auth','0005_alter_user_last_login_null','2022-07-16 10:51:06.007082'),
(8,'auth','0006_require_contenttypes_0002','2022-07-16 10:51:06.010089'),
(9,'auth','0007_alter_validators_add_error_messages','2022-07-16 10:51:06.017164'),
(10,'auth','0008_alter_user_username_max_length','2022-07-16 10:51:06.023174'),
(11,'auth','0009_alter_user_last_name_max_length','2022-07-16 10:51:06.029179'),
(12,'auth','0010_alter_group_name_max_length','2022-07-16 10:51:06.046183'),
(13,'auth','0011_update_proxy_permissions','2022-07-16 10:51:06.054181'),
(14,'auth','0012_alter_user_first_name_max_length','2022-07-16 10:51:06.060187'),
(15,'user','0001_initial','2022-07-16 10:51:06.591800'),
(16,'admin','0001_initial','2022-07-16 10:51:06.712746'),
(17,'admin','0002_logentry_remove_auto_add','2022-07-16 10:51:06.724758'),
(18,'admin','0003_logentry_add_action_flag_choices','2022-07-16 10:51:06.736338'),
(19,'api','0001_initial','2022-07-16 10:51:06.961205'),
(20,'api','0002_initial','2022-07-16 10:51:07.815883'),
(21,'django_apscheduler','0001_initial','2022-07-16 10:51:07.916594'),
(22,'django_apscheduler','0002_auto_20180412_0758','2022-07-16 10:51:07.956532'),
(23,'django_apscheduler','0003_auto_20200716_1632','2022-07-16 10:51:07.980078'),
(24,'django_apscheduler','0004_auto_20200717_1043','2022-07-16 10:51:08.135197'),
(25,'django_apscheduler','0005_migrate_name_to_id','2022-07-16 10:51:08.157376'),
(26,'django_apscheduler','0006_remove_djangojob_name','2022-07-16 10:51:08.196183'),
(27,'django_apscheduler','0007_auto_20200717_1404','2022-07-16 10:51:08.241666'),
(28,'django_apscheduler','0008_remove_djangojobexecution_started','2022-07-16 10:51:08.273193'),
(29,'django_apscheduler','0009_djangojobexecution_unique_job_executions','2022-07-16 10:51:08.293191'),
(30,'django_celery_beat','0001_initial','2022-07-16 10:51:08.457187'),
(31,'django_celery_beat','0002_auto_20161118_0346','2022-07-16 10:51:08.528803'),
(32,'django_celery_beat','0003_auto_20161209_0049','2022-07-16 10:51:08.552499'),
(33,'django_celery_beat','0004_auto_20170221_0000','2022-07-16 10:51:08.559195'),
(34,'django_celery_beat','0005_add_solarschedule_events_choices','2022-07-16 10:51:08.566187'),
(35,'django_celery_beat','0006_auto_20180322_0932','2022-07-16 10:51:08.636427'),
(36,'django_celery_beat','0007_auto_20180521_0826','2022-07-16 10:51:08.685771'),
(37,'django_celery_beat','0008_auto_20180914_1922','2022-07-16 10:51:08.707188'),
(38,'django_celery_beat','0006_auto_20180210_1226','2022-07-16 10:51:08.722188'),
(39,'django_celery_beat','0006_periodictask_priority','2022-07-16 10:51:08.778786'),
(40,'django_celery_beat','0009_periodictask_headers','2022-07-16 10:51:08.837188'),
(41,'django_celery_beat','0010_auto_20190429_0326','2022-07-16 10:51:08.962356'),
(42,'django_celery_beat','0011_auto_20190508_0153','2022-07-16 10:51:09.044181'),
(43,'django_celery_beat','0012_periodictask_expire_seconds','2022-07-16 10:51:09.107193'),
(44,'django_celery_beat','0013_auto_20200609_0727','2022-07-16 10:51:09.114736'),
(45,'django_celery_beat','0014_remove_clockedschedule_enabled','2022-07-16 10:51:09.143719'),
(46,'django_celery_beat','0015_edit_solarschedule_events_choices','2022-07-16 10:51:09.151483'),
(47,'django_celery_beat','0016_alter_crontabschedule_timezone','2022-07-16 10:51:09.158416'),
(48,'django_celery_results','0001_initial','2022-07-16 10:51:09.203184'),
(49,'django_celery_results','0002_add_task_name_args_kwargs','2022-07-16 10:51:09.251432'),
(50,'django_celery_results','0003_auto_20181106_1101','2022-07-16 10:51:09.257418'),
(51,'django_celery_results','0004_auto_20190516_0412','2022-07-16 10:51:09.364183'),
(52,'django_celery_results','0005_taskresult_worker','2022-07-16 10:51:09.400203'),
(53,'django_celery_results','0006_taskresult_date_created','2022-07-16 10:51:09.461680'),
(54,'django_celery_results','0007_remove_taskresult_hidden','2022-07-16 10:51:09.505618'),
(55,'django_celery_results','0008_chordcounter','2022-07-16 10:51:09.535508'),
(56,'django_celery_results','0009_groupresult','2022-07-16 10:51:09.754192'),
(57,'django_celery_results','0010_remove_duplicate_indices','2022-07-16 10:51:09.767207'),
(58,'django_celery_results','0011_taskresult_periodic_task_name','2022-07-16 10:51:09.786189'),
(59,'public','0001_initial','2022-07-16 10:51:09.944188'),
(60,'sessions','0001_initial','2022-07-16 10:51:09.973202');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

/*Table structure for table `menu` */

DROP TABLE IF EXISTS `menu`;

CREATE TABLE `menu` (
  `_id` varchar(64) NOT NULL,
  `statue` smallint NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `rid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `title` varchar(64) NOT NULL,
  `icon` varchar(64) NOT NULL,
  `pid` smallint NOT NULL,
  `path` varchar(128) NOT NULL,
  `order` smallint NOT NULL,
  PRIMARY KEY (`rid`),
  UNIQUE KEY `_id` (`_id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `menu` */

insert  into `menu`(`_id`,`statue`,`create_time`,`update_time`,`rid`,`name`,`title`,`icon`,`pid`,`path`,`order`) values 
('c9b4b4797b554db8ae4ac4e22ec9f122',1,'2022-07-16 11:01:23.000000','2022-07-16 11:31:58.449327',1,'authority','权限管理','Setting',0,'/authority',0),
('c9b4b4797b554db8ae4ac4e22ec9e1w1',1,'2022-07-16 11:01:23.000000','2022-07-16 11:01:25.000000',2,'menu','菜单管理','Menu',1,'/authority/menuEdit',0),
('ce6ceb196898452ca54eab41a3fd2b6b',1,'2022-07-16 11:27:00.064487','2022-07-16 11:27:00.064487',3,'role','关联角色菜单','Connection',1,'/authority/authorityEdit',0),
('3bc264a6b9e343df8dc51ce774fc30b9',1,'2022-07-16 11:28:03.233028','2022-07-16 11:28:03.233028',4,'user','用户管理','User',1,'/authority/userList',0),
('03e161e73cc44098b2d2a6378869e268',1,'2022-07-16 11:33:15.923893','2022-07-16 11:33:15.923893',5,'api','API工作区','MoonNight',0,'/api',0),
('41b47f62745649dc9218d89dbba264a9',1,'2022-07-16 11:34:07.590519','2022-07-16 11:34:07.590519',6,'project','立项管理','MilkTea',5,'/api/project',0),
('37ab0862f0414acbb74bbc1cfe297611',1,'2022-07-16 11:34:56.590079','2022-07-16 11:34:56.590079',7,'module','测试套件','Notebook',5,'/api/module',0),
('58491173e7a140e98e636a9228546d42',1,'2022-07-16 11:36:39.918348','2022-07-16 11:36:39.918348',8,'template','请求模板','DocumentCopy',5,'/api/template',0),
('3a53216c8bce43279ac0d2f5137e4df8',1,'2022-07-16 11:37:41.449140','2022-07-16 11:37:41.449140',9,'case','测试用例','CoffeeCup',5,'/api/case',0),
('0b97052ef0ea4dc9b7cf85f1533b1880',1,'2022-07-16 11:38:20.825814','2022-07-16 11:38:20.825814',10,'scenario','场景设计','ColdDrink',5,'/api/scenario',0),
('74049e8f0919468bb9b45471739b5eea',1,'2022-07-16 11:39:52.342582','2022-07-16 11:39:52.342582',11,'report','调度任务','Odometer',0,'/report',0),
('7e2b0ce6ca73483ea415b4cd34d4babb',1,'2022-07-16 11:41:23.079766','2022-07-16 11:41:23.079766',12,'report-cron','测试报告','Tickets',11,'/api/report',0);

/*Table structure for table `project` */

DROP TABLE IF EXISTS `project`;

CREATE TABLE `project` (
  `uid` varchar(64) NOT NULL,
  `statue` smallint NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(64) NOT NULL,
  `description` varchar(320) DEFAULT NULL,
  `start` date DEFAULT NULL,
  `end` date DEFAULT NULL,
  `process` smallint unsigned NOT NULL,
  `last_execute` smallint unsigned NOT NULL,
  `owner_id` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `name` (`name`),
  KEY `project_owner_id_d7626fbc_fk_user_user_id` (`owner_id`),
  CONSTRAINT `project_owner_id_d7626fbc_fk_user_user_id` FOREIGN KEY (`owner_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `project_chk_1` CHECK ((`process` >= 0)),
  CONSTRAINT `project_chk_2` CHECK ((`last_execute` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `project` */

insert  into `project`(`uid`,`statue`,`create_time`,`update_time`,`name`,`description`,`start`,`end`,`process`,`last_execute`,`owner_id`) values 
('2c398ddc74b647a693b2ce11118144ed',1,'2022-07-16 11:44:10.003393','2022-07-16 11:47:00.532355','容器云','容器云','2022-07-16','2022-07-16',98,0,'root');

/*Table structure for table `public_coremodel` */

DROP TABLE IF EXISTS `public_coremodel`;

CREATE TABLE `public_coremodel` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `modifier` varchar(255) DEFAULT NULL,
  `update_datetime` datetime(6) DEFAULT NULL,
  `create_datetime` datetime(6) DEFAULT NULL,
  `creator_id` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `public_coremodel_creator_id_2d02999a` (`creator_id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `public_coremodel` */

insert  into `public_coremodel`(`id`,`description`,`modifier`,`update_datetime`,`create_datetime`,`creator_id`) values 
(1,NULL,NULL,'2022-07-16 11:10:05.783730','2022-07-16 11:10:05.780735',NULL),
(2,NULL,NULL,'2022-07-16 11:10:05.812662','2022-07-16 11:10:05.812662',NULL),
(3,NULL,NULL,'2022-07-16 11:10:13.044758','2022-07-16 11:10:13.039749',NULL),
(4,NULL,NULL,'2022-07-16 11:10:25.014929','2022-07-16 11:10:25.014929',NULL),
(5,NULL,NULL,'2022-07-16 11:10:42.118266','2022-07-16 11:10:42.118266',NULL),
(6,NULL,NULL,'2022-07-16 11:10:43.042718','2022-07-16 11:10:43.042718',NULL),
(7,NULL,NULL,'2022-07-16 11:10:43.260721','2022-07-16 11:10:43.260721',NULL),
(8,NULL,NULL,'2022-07-16 11:10:44.115862','2022-07-16 11:10:44.115862',NULL),
(9,NULL,NULL,'2022-07-16 11:10:44.305012','2022-07-16 11:10:44.305012',NULL),
(10,NULL,NULL,'2022-07-16 11:11:00.973796','2022-07-16 11:11:00.973796',NULL),
(11,NULL,NULL,'2022-07-16 11:13:16.070530','2022-07-16 11:13:16.065436',NULL),
(12,NULL,NULL,'2022-07-16 11:13:16.099750','2022-07-16 11:13:16.100751',NULL),
(13,NULL,NULL,'2022-07-16 11:16:13.161535','2022-07-16 11:16:13.158536',NULL),
(14,NULL,NULL,'2022-07-16 11:17:28.456212','2022-07-16 11:17:28.456212',NULL),
(15,NULL,NULL,'2022-07-16 11:17:37.668984','2022-07-16 11:17:37.668984',NULL),
(16,NULL,NULL,'2022-07-16 11:21:46.285296','2022-07-16 11:21:46.285296',NULL),
(17,NULL,NULL,'2022-07-16 11:21:47.896033','2022-07-16 11:21:47.896033',NULL),
(18,NULL,NULL,'2022-07-16 11:27:00.068491','2022-07-16 11:27:00.055935','root'),
(19,NULL,NULL,'2022-07-16 11:30:33.684734','2022-07-16 11:28:03.222604',NULL),
(20,NULL,NULL,'2022-07-16 11:32:00.851591','2022-07-16 11:31:58.441152',NULL),
(21,NULL,NULL,'2022-07-16 11:33:15.928742','2022-07-16 11:33:15.910687','root'),
(22,NULL,NULL,'2022-07-16 11:34:07.594498','2022-07-16 11:34:07.581616','root'),
(23,NULL,NULL,'2022-07-16 11:34:56.594213','2022-07-16 11:34:56.576593','root'),
(24,NULL,NULL,'2022-07-16 11:36:39.922941','2022-07-16 11:36:39.909843','root'),
(25,NULL,NULL,'2022-07-16 11:37:41.453706','2022-07-16 11:37:41.436803','root'),
(26,NULL,NULL,'2022-07-16 11:38:20.829818','2022-07-16 11:38:20.818824','root'),
(27,NULL,NULL,'2022-07-16 11:39:52.348588','2022-07-16 11:39:52.328958','root'),
(28,NULL,NULL,'2022-07-16 11:41:23.084778','2022-07-16 11:41:23.068751','root'),
(29,NULL,NULL,'2022-07-16 11:43:39.997357','2022-07-16 11:41:33.582104',NULL),
(30,NULL,NULL,'2022-07-16 11:44:10.011006','2022-07-16 11:44:09.993307','root'),
(31,NULL,NULL,'2022-07-16 11:46:06.672981','2022-07-16 11:46:06.656828','root'),
(32,NULL,NULL,'2022-07-16 11:54:22.307769','2022-07-16 11:47:00.518494',NULL),
(33,NULL,NULL,'2022-07-16 11:57:33.108627','2022-07-16 11:55:52.327171',NULL),
(34,NULL,NULL,'2022-07-16 11:58:25.014359','2022-07-16 11:57:46.994914',NULL),
(35,NULL,NULL,'2022-07-16 11:58:52.354400','2022-07-16 11:58:46.399565',NULL),
(36,NULL,NULL,'2022-07-16 13:39:09.531615','2022-07-16 11:59:21.533038',NULL),
(37,NULL,NULL,'2022-07-16 15:46:48.492959','2022-07-16 15:46:48.478946','root'),
(38,NULL,NULL,'2022-07-16 15:53:40.289673','2022-07-16 15:47:09.247494',NULL),
(39,NULL,NULL,'2022-07-16 16:06:05.533127','2022-07-16 16:06:05.533127',NULL),
(40,NULL,NULL,'2022-07-16 16:07:04.801706','2022-07-16 16:06:08.747984',NULL),
(41,NULL,NULL,'2022-07-16 16:08:22.172063','2022-07-16 16:08:22.160519','root'),
(42,NULL,NULL,'2022-07-16 16:11:41.128768','2022-07-16 16:11:36.410807',NULL),
(43,NULL,NULL,'2022-07-16 16:11:52.803483','2022-07-16 16:11:49.518886',NULL),
(44,NULL,NULL,'2022-07-16 16:12:25.599387','2022-07-16 16:12:25.587376','root'),
(45,NULL,NULL,'2022-07-16 16:12:49.327453','2022-07-16 16:12:49.315442','root'),
(46,NULL,NULL,'2022-07-16 16:14:47.265206','2022-07-16 16:14:47.236178','root'),
(47,NULL,NULL,'2022-07-16 16:15:17.303700','2022-07-16 16:15:17.285686','root'),
(48,NULL,NULL,'2022-07-16 16:15:46.514588','2022-07-16 16:15:38.831311',NULL),
(49,NULL,NULL,'2022-07-16 16:16:05.430443','2022-07-16 16:16:01.702670',NULL),
(50,NULL,NULL,'2022-07-16 16:17:02.325745','2022-07-16 16:16:16.963304',NULL),
(51,NULL,NULL,'2022-07-16 16:18:20.773205','2022-07-16 16:18:17.254909',NULL),
(52,NULL,NULL,'2022-07-16 17:49:15.487838','2022-07-16 16:18:48.349737',NULL),
(53,NULL,NULL,'2022-07-16 17:49:32.534327','2022-07-16 17:49:32.517431','root'),
(54,NULL,NULL,'2022-07-16 17:50:18.927048','2022-07-16 17:50:18.907029','root'),
(55,NULL,NULL,'2022-07-16 17:51:11.197707','2022-07-16 17:51:11.185132','root'),
(56,NULL,NULL,'2022-07-16 17:51:26.040287','2022-07-16 17:51:26.028275','root'),
(57,NULL,NULL,'2022-07-16 17:51:39.104277','2022-07-16 17:51:39.091729','root'),
(58,NULL,NULL,'2022-07-16 17:51:46.374926','2022-07-16 17:51:46.358491','root'),
(59,NULL,NULL,'2022-07-16 17:59:26.323075','2022-07-16 17:59:26.311078','root'),
(60,NULL,NULL,'2022-07-16 17:59:34.391091','2022-07-16 17:59:32.094417',NULL),
(61,NULL,NULL,'2022-07-16 17:59:56.440210','2022-07-16 17:59:53.891497',NULL),
(62,NULL,NULL,'2022-07-16 19:25:29.621428','2022-07-16 19:25:29.621428',NULL),
(63,NULL,NULL,'2022-07-16 19:25:52.520748','2022-07-16 19:25:52.520748',NULL),
(64,NULL,NULL,'2022-07-16 19:33:26.810339','2022-07-16 19:33:26.810339',NULL),
(65,NULL,NULL,'2022-07-16 19:33:28.666484','2022-07-16 19:33:28.666484',NULL),
(66,NULL,NULL,'2022-07-16 19:33:54.976396','2022-07-16 19:33:54.976396',NULL),
(67,NULL,NULL,'2022-07-16 19:34:09.261981','2022-07-16 19:34:09.261981',NULL),
(68,NULL,NULL,'2022-07-16 19:34:10.608414','2022-07-16 19:34:10.608414',NULL),
(69,NULL,NULL,'2022-07-16 19:35:41.980472','2022-07-16 19:35:41.980472',NULL),
(70,NULL,NULL,'2022-07-16 19:35:54.223144','2022-07-16 19:35:54.223144',NULL),
(71,NULL,NULL,'2022-07-16 19:35:54.996491','2022-07-16 19:35:54.996491',NULL),
(72,NULL,NULL,'2022-07-16 19:36:14.610501','2022-07-16 19:36:14.610501',NULL),
(73,NULL,NULL,'2022-07-16 19:41:17.673922','2022-07-16 19:41:17.673922',NULL),
(74,NULL,NULL,'2022-07-16 19:41:37.718592','2022-07-16 19:41:37.718592',NULL),
(75,NULL,NULL,'2022-07-16 19:45:16.587217','2022-07-16 19:45:16.587217',NULL),
(76,NULL,NULL,'2022-07-17 09:37:31.034017','2022-07-17 09:37:31.030448',NULL),
(77,NULL,NULL,'2022-07-17 09:37:31.064337','2022-07-17 09:37:31.064337',NULL),
(78,NULL,NULL,'2022-07-17 09:57:12.370965','2022-07-17 09:57:12.370965',NULL),
(79,NULL,NULL,'2022-07-17 09:57:50.725794','2022-07-17 09:57:50.725794',NULL),
(80,NULL,NULL,'2022-07-17 10:00:25.368217','2022-07-17 10:00:25.368217',NULL),
(81,NULL,NULL,'2022-07-17 10:01:37.901326','2022-07-17 10:01:37.901326',NULL),
(82,NULL,NULL,'2022-07-17 10:04:59.085155','2022-07-17 10:04:59.085155',NULL),
(83,NULL,NULL,'2022-07-17 10:05:55.698724','2022-07-17 10:05:55.698724',NULL),
(84,NULL,NULL,'2022-07-17 10:06:24.449322','2022-07-17 10:06:24.449322',NULL),
(85,NULL,NULL,'2022-07-17 11:14:26.696790','2022-07-17 11:14:26.696790',NULL),
(86,NULL,NULL,'2022-07-17 11:30:26.874018','2022-07-17 11:30:26.874018',NULL),
(87,NULL,NULL,'2022-07-17 11:30:38.255395','2022-07-17 11:30:38.255395',NULL),
(88,NULL,NULL,'2022-07-17 11:31:03.453902','2022-07-17 11:31:03.453902',NULL),
(89,NULL,NULL,'2022-07-17 11:31:28.269225','2022-07-17 11:31:28.269225',NULL),
(90,NULL,NULL,'2022-07-17 11:31:29.179327','2022-07-17 11:31:29.179327',NULL),
(91,NULL,NULL,'2022-07-17 11:32:19.830718','2022-07-17 11:32:19.830718',NULL),
(92,NULL,NULL,'2022-07-17 11:32:27.179184','2022-07-17 11:32:27.179184',NULL),
(93,NULL,NULL,'2022-07-17 11:32:43.745543','2022-07-17 11:32:43.746545',NULL),
(94,NULL,NULL,'2022-07-17 11:33:31.548178','2022-07-17 11:33:31.548178',NULL),
(95,NULL,NULL,'2022-07-17 12:05:09.701650','2022-07-17 12:05:09.701650',NULL),
(96,NULL,NULL,'2022-07-17 12:05:44.247322','2022-07-17 12:05:44.247322',NULL),
(97,NULL,NULL,'2022-07-17 12:07:23.461278','2022-07-17 12:07:23.461278',NULL),
(98,NULL,NULL,'2022-07-17 12:07:50.556827','2022-07-17 12:07:50.556827',NULL),
(99,NULL,NULL,'2022-07-17 12:08:31.409948','2022-07-17 12:08:31.409948',NULL),
(100,NULL,NULL,'2022-07-17 12:08:48.429824','2022-07-17 12:08:48.429824',NULL),
(101,NULL,NULL,'2022-07-17 12:09:22.172034','2022-07-17 12:09:22.172034',NULL),
(102,NULL,NULL,'2022-07-17 12:12:18.666619','2022-07-17 12:12:18.666619',NULL),
(103,NULL,NULL,'2022-07-17 12:12:40.685716','2022-07-17 12:12:40.685716',NULL);

/*Table structure for table `record` */

DROP TABLE IF EXISTS `record`;

CREATE TABLE `record` (
  `code` varchar(64) NOT NULL,
  `remark` varchar(128) DEFAULT NULL,
  `statue` smallint NOT NULL,
  `type` smallint NOT NULL,
  `cron_task_status` smallint DEFAULT NULL,
  `task_type` smallint NOT NULL,
  `stick_start_point` datetime(6) DEFAULT NULL,
  `loop_interval` smallint DEFAULT NULL,
  `start` varchar(32) NOT NULL,
  `path` varchar(128) DEFAULT NULL,
  `duration` varchar(32) DEFAULT NULL,
  `person` varchar(32) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `create_date` date NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`code`),
  KEY `record_code_ea7cf3_idx` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `record` */

insert  into `record`(`code`,`remark`,`statue`,`type`,`cron_task_status`,`task_type`,`stick_start_point`,`loop_interval`,`start`,`path`,`duration`,`person`,`create_time`,`create_date`,`update_time`) values 
('EXEC_20A7E053BE10425C958FB48454D045BE','dsads',0,2,4,2,NULL,1,'2022-07-16 12:00:28.664787','/home/volume/incoming/20220716/EXEC_20A7E053BE10425C958FB48454D045BE/EXEC_20A7E053BE10425C958FB48454D045BE.html','0.145','root','2022-07-16 12:00:28.666788','2022-07-16','2022-07-16 12:30:33.684053'),
('EXEC_B8451DB116D84535996CCDA11A3843D7','eeee',0,2,NULL,0,NULL,0,'2022-07-16 11:59:37.192446','/home/volume/incoming/20220716/EXEC_B8451DB116D84535996CCDA11A3843D7/EXEC_B8451DB116D84535996CCDA11A3843D7.html','0.194','root','2022-07-16 11:59:37.194438','2022-07-16','2022-07-16 11:59:38.273467'),
('EXEC_E7B1259FF7E74D57B668E78BFFFF31EC','dsd',0,2,2,1,'2022-07-16 12:17:09.000000',0,'2022-07-16 12:00:19.687527','/home/volume/incoming/20220716/EXEC_E7B1259FF7E74D57B668E78BFFFF31EC/EXEC_E7B1259FF7E74D57B668E78BFFFF31EC.html','0.140','root','2022-07-16 12:00:19.691532','2022-07-16','2022-07-16 12:17:00.463780');

/*Table structure for table `request_backup` */

DROP TABLE IF EXISTS `request_backup`;

CREATE TABLE `request_backup` (
  `code` varchar(64) NOT NULL,
  `body` json NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`code`),
  KEY `request_bac_code_85d3ff_idx` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `request_backup` */

insert  into `request_backup`(`code`,`body`,`create_time`,`update_time`) values 
('EXEC_20A7E053BE10425C958FB48454D045BE','{\"body\": [{\"uid\": \"3a1407fea7264dbb8a077b18cc8de6cf\", \"case\": \"auth_api\", \"owner\": \"root\", \"module\": \"PORTAINER\", \"statue\": 1, \"priority\": 0, \"template\": \"219baffcb4cb4c33956526fe2deef0ff\", \"testsuit\": \"9ecea461b8ef4b6fab80cc05451151a4\", \"scenarios\": [[{\"password\": \"aaaa1111!\", \"username\": \"admin\"}, \"用户名和密码正确\", {\"$.jwt@2\": \"e\"}]], \"case_title\": \"用例登录接口\", \"class_title\": \"容器云基本功能\", \"create_time\": \"2022-07-16 11:58:46\", \"update_time\": \"2022-07-16 11:58:46\", \"casetemplate\": {\"uid\": \"219baffcb4cb4c33956526fe2deef0ff\", \"url\": \"http://192.168.44.129:9000/api/auth\", \"data\": {\"password\": \"{{password}}\", \"username\": \"{{username}}\"}, \"name\": \"请求认证接口\", \"owner\": \"root\", \"header\": {\"Content-Type\": \"application/json\"}, \"method\": 1, \"statue\": 1, \"default\": [{\"val\": \"admin\", \"type\": 0, \"field\": \"username\"}, {\"val\": \"aaaa1111!\", \"type\": 0, \"field\": \"password\"}], \"table_name\": \"\", \"create_time\": \"2022-07-16 11:57:47\", \"update_time\": \"2022-07-16 11:57:47\", \"process_name\": \"\", \"method_display\": \"POST\", \"statue_display\": \"有效\", \"linux_order_str\": \"\"}, \"case_scenario\": [{\"uid\": \"e9b7c3b97f8d48739935e2c1f1633b85\", \"cases\": \"3a1407fea7264dbb8a077b18cc8de6cf\", \"owner\": \"root\", \"statue\": 1, \"scenario\": \"用户名和密码正确\", \"testcase\": \"auth_api\", \"parameter\": {\"password@0\": \"aaaa1111!\", \"username@0\": \"admin\"}, \"validator\": {\"$.jwt@2@0\": \"e\"}, \"case_title\": \"用例登录接口\", \"create_time\": \"2022-07-16 11:59:21\", \"update_time\": \"2022-07-16 11:59:21\", \"statue_display\": \"有效\"}], \"statue_display\": \"有效\", \"case_description\": \"用例登录接口\", \"priority_display\": \"高\"}], \"exec_id\": \"EXEC_20A7E053BE10425C958FB48454D045BE\"}','2022-07-16 12:10:33.263022','2022-07-16 12:10:33.263022'),
('EXEC_B8451DB116D84535996CCDA11A3843D7','{\"body\": [{\"uid\": \"3a1407fea7264dbb8a077b18cc8de6cf\", \"case\": \"auth_api\", \"owner\": \"root\", \"module\": \"PORTAINER\", \"statue\": 1, \"priority\": 0, \"template\": \"219baffcb4cb4c33956526fe2deef0ff\", \"testsuit\": \"9ecea461b8ef4b6fab80cc05451151a4\", \"scenarios\": [[{\"password\": \"aaaa1111!\", \"username\": \"admin\"}, \"用户名和密码正确\", {\"$.jwt@2\": \"e\"}]], \"case_title\": \"用例登录接口\", \"class_title\": \"容器云基本功能\", \"create_time\": \"2022-07-16 11:58:46\", \"update_time\": \"2022-07-16 11:58:46\", \"casetemplate\": {\"uid\": \"219baffcb4cb4c33956526fe2deef0ff\", \"url\": \"http://192.168.44.129:9000/api/auth\", \"data\": {\"password\": \"{{password}}\", \"username\": \"{{username}}\"}, \"name\": \"请求认证接口\", \"owner\": \"root\", \"header\": {\"Content-Type\": \"application/json\"}, \"method\": 1, \"statue\": 1, \"default\": [{\"val\": \"admin\", \"type\": 0, \"field\": \"username\"}, {\"val\": \"aaaa1111!\", \"type\": 0, \"field\": \"password\"}], \"table_name\": \"\", \"create_time\": \"2022-07-16 11:57:47\", \"update_time\": \"2022-07-16 11:57:47\", \"process_name\": \"\", \"method_display\": \"POST\", \"statue_display\": \"有效\", \"linux_order_str\": \"\"}, \"case_scenario\": [{\"uid\": \"e9b7c3b97f8d48739935e2c1f1633b85\", \"cases\": \"3a1407fea7264dbb8a077b18cc8de6cf\", \"owner\": \"root\", \"statue\": 1, \"scenario\": \"用户名和密码正确\", \"testcase\": \"auth_api\", \"parameter\": {\"password@0\": \"aaaa1111!\", \"username@0\": \"admin\"}, \"validator\": {\"$.jwt@2@0\": \"e\"}, \"case_title\": \"用例登录接口\", \"create_time\": \"2022-07-16 11:59:21\", \"update_time\": \"2022-07-16 11:59:21\", \"statue_display\": \"有效\"}], \"statue_display\": \"有效\", \"case_description\": \"用例登录接口\", \"priority_display\": \"高\"}], \"exec_id\": \"EXEC_B8451DB116D84535996CCDA11A3843D7\"}','2022-07-16 11:59:37.380850','2022-07-16 11:59:37.381831'),
('EXEC_E7B1259FF7E74D57B668E78BFFFF31EC','{\"body\": [{\"uid\": \"3a1407fea7264dbb8a077b18cc8de6cf\", \"case\": \"auth_api\", \"owner\": \"root\", \"module\": \"PORTAINER\", \"statue\": 1, \"priority\": 0, \"template\": \"219baffcb4cb4c33956526fe2deef0ff\", \"testsuit\": \"9ecea461b8ef4b6fab80cc05451151a4\", \"scenarios\": [[{\"password\": \"aaaa1111!\", \"username\": \"admin\"}, \"用户名和密码正确\", {\"$.jwt@2\": \"e\"}]], \"case_title\": \"用例登录接口\", \"class_title\": \"容器云基本功能\", \"create_time\": \"2022-07-16 11:58:46\", \"update_time\": \"2022-07-16 11:58:46\", \"casetemplate\": {\"uid\": \"219baffcb4cb4c33956526fe2deef0ff\", \"url\": \"http://192.168.44.129:9000/api/auth\", \"data\": {\"password\": \"{{password}}\", \"username\": \"{{username}}\"}, \"name\": \"请求认证接口\", \"owner\": \"root\", \"header\": {\"Content-Type\": \"application/json\"}, \"method\": 1, \"statue\": 1, \"default\": [{\"val\": \"admin\", \"type\": 0, \"field\": \"username\"}, {\"val\": \"aaaa1111!\", \"type\": 0, \"field\": \"password\"}], \"table_name\": \"\", \"create_time\": \"2022-07-16 11:57:47\", \"update_time\": \"2022-07-16 11:57:47\", \"process_name\": \"\", \"method_display\": \"POST\", \"statue_display\": \"有效\", \"linux_order_str\": \"\"}, \"case_scenario\": [{\"uid\": \"e9b7c3b97f8d48739935e2c1f1633b85\", \"cases\": \"3a1407fea7264dbb8a077b18cc8de6cf\", \"owner\": \"root\", \"statue\": 1, \"scenario\": \"用户名和密码正确\", \"testcase\": \"auth_api\", \"parameter\": {\"password@0\": \"aaaa1111!\", \"username@0\": \"admin\"}, \"validator\": {\"$.jwt@2@0\": \"e\"}, \"case_title\": \"用例登录接口\", \"create_time\": \"2022-07-16 11:59:21\", \"update_time\": \"2022-07-16 11:59:21\", \"statue_display\": \"有效\"}], \"statue_display\": \"有效\", \"case_description\": \"用例登录接口\", \"priority_display\": \"高\"}], \"exec_id\": \"EXEC_E7B1259FF7E74D57B668E78BFFFF31EC\"}','2022-07-16 12:17:00.015795','2022-07-16 12:17:00.015795');

/*Table structure for table `role` */

DROP TABLE IF EXISTS `role`;

CREATE TABLE `role` (
  `_id` varchar(64) NOT NULL,
  `name` varchar(64) NOT NULL,
  `describe` varchar(128) DEFAULT NULL,
  `statue` smallint NOT NULL,
  `order` smallint NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`_id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `role` */

insert  into `role`(`_id`,`name`,`describe`,`statue`,`order`,`create_time`,`update_time`) values 
('d9b4b4797b554db8ae4ac4e22ec9f1s1','超级管理员','超级管理员，拥有最高权限',1,0,'2022-07-16 11:06:07.000000','2022-07-16 17:59:32.112961');

/*Table structure for table `role_menu` */

DROP TABLE IF EXISTS `role_menu`;

CREATE TABLE `role_menu` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `role_id` varchar(64) NOT NULL,
  `menu_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_menu_role_id_menu_id_c692b7c4_uniq` (`role_id`,`menu_id`),
  KEY `role_menu_menu_id_b54bc904_fk_menu_rid` (`menu_id`),
  CONSTRAINT `role_menu_menu_id_b54bc904_fk_menu_rid` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`rid`),
  CONSTRAINT `role_menu_role_id_8f901c2d_fk_role__id` FOREIGN KEY (`role_id`) REFERENCES `role` (`_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `role_menu` */

insert  into `role_menu`(`id`,`role_id`,`menu_id`) values 
(2,'d9b4b4797b554db8ae4ac4e22ec9f1s1',2),
(3,'d9b4b4797b554db8ae4ac4e22ec9f1s1',3),
(4,'d9b4b4797b554db8ae4ac4e22ec9f1s1',4),
(5,'d9b4b4797b554db8ae4ac4e22ec9f1s1',6),
(6,'d9b4b4797b554db8ae4ac4e22ec9f1s1',7),
(7,'d9b4b4797b554db8ae4ac4e22ec9f1s1',8),
(8,'d9b4b4797b554db8ae4ac4e22ec9f1s1',9),
(9,'d9b4b4797b554db8ae4ac4e22ec9f1s1',10),
(10,'d9b4b4797b554db8ae4ac4e22ec9f1s1',12);

/*Table structure for table `scenario` */

DROP TABLE IF EXISTS `scenario`;

CREATE TABLE `scenario` (
  `uid` varchar(64) NOT NULL,
  `statue` smallint NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `scenario` varchar(64) NOT NULL,
  `parameter` json DEFAULT NULL,
  `validator` json DEFAULT NULL,
  `cases_id` varchar(64) NOT NULL,
  `owner_id` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `scenario` (`scenario`),
  KEY `scenario_cases_id_28770b85_fk_case_uid` (`cases_id`),
  KEY `scenario_owner_id_8c294113_fk_user_user_id` (`owner_id`),
  KEY `scenario_scenari_190d31_idx` (`scenario`),
  CONSTRAINT `scenario_cases_id_28770b85_fk_case_uid` FOREIGN KEY (`cases_id`) REFERENCES `case` (`uid`),
  CONSTRAINT `scenario_owner_id_8c294113_fk_user_user_id` FOREIGN KEY (`owner_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `scenario` */

insert  into `scenario`(`uid`,`statue`,`create_time`,`update_time`,`scenario`,`parameter`,`validator`,`cases_id`,`owner_id`) values 
('e9b7c3b97f8d48739935e2c1f1633b85',1,'2022-07-16 11:59:21.540034','2022-07-16 11:59:21.540034','用户名和密码正确','{\"password@0\": \"aaaa1111!\", \"username@0\": \"admin\"}','{\"$.jwt@2@0\": \"e\"}','3a1407fea7264dbb8a077b18cc8de6cf','root');

/*Table structure for table `suit` */

DROP TABLE IF EXISTS `suit`;

CREATE TABLE `suit` (
  `uid` varchar(64) NOT NULL,
  `statue` smallint NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `module` varchar(64) NOT NULL,
  `class_title` varchar(32) DEFAULT NULL,
  `owner_id` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `module` (`module`),
  KEY `suit_owner_id_a2d9fe00_fk_user_user_id` (`owner_id`),
  CONSTRAINT `suit_owner_id_a2d9fe00_fk_user_user_id` FOREIGN KEY (`owner_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suit` */

insert  into `suit`(`uid`,`statue`,`create_time`,`update_time`,`module`,`class_title`,`owner_id`) values 
('9ecea461b8ef4b6fab80cc05451151a4',1,'2022-07-16 11:55:52.336157','2022-07-16 11:55:52.336157','PORTAINER','容器云基本功能','root');

/*Table structure for table `suit_project` */

DROP TABLE IF EXISTS `suit_project`;

CREATE TABLE `suit_project` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `testsuit_id` varchar(64) NOT NULL,
  `project_id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `suit_project_testsuit_id_project_id_e88543ae_uniq` (`testsuit_id`,`project_id`),
  KEY `suit_project_project_id_75e525b2_fk_project_uid` (`project_id`),
  CONSTRAINT `suit_project_project_id_75e525b2_fk_project_uid` FOREIGN KEY (`project_id`) REFERENCES `project` (`uid`),
  CONSTRAINT `suit_project_testsuit_id_cd372324_fk_suit_uid` FOREIGN KEY (`testsuit_id`) REFERENCES `suit` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `suit_project` */

insert  into `suit_project`(`id`,`testsuit_id`,`project_id`) values 
(1,'9ecea461b8ef4b6fab80cc05451151a4','2c398ddc74b647a693b2ce11118144ed');

/*Table structure for table `system_operation_log` */

DROP TABLE IF EXISTS `system_operation_log`;

CREATE TABLE `system_operation_log` (
  `coremodel_ptr_id` bigint NOT NULL,
  `request_modular` varchar(64) DEFAULT NULL,
  `request_path` varchar(400) DEFAULT NULL,
  `request_body` longtext,
  `request_method` varchar(8) DEFAULT NULL,
  `request_msg` longtext,
  `request_ip` varchar(32) DEFAULT NULL,
  `request_browser` varchar(64) DEFAULT NULL,
  `response_code` varchar(32) DEFAULT NULL,
  `request_os` varchar(64) DEFAULT NULL,
  `json_result` longtext,
  `status` tinyint(1) NOT NULL,
  PRIMARY KEY (`coremodel_ptr_id`),
  CONSTRAINT `system_operation_log_coremodel_ptr_id_5a33ea8e_fk_public_co` FOREIGN KEY (`coremodel_ptr_id`) REFERENCES `public_coremodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `system_operation_log` */

insert  into `system_operation_log`(`coremodel_ptr_id`,`request_modular`,`request_path`,`request_body`,`request_method`,`request_msg`,`request_ip`,`request_browser`,`response_code`,`request_os`,`json_result`,`status`) values 
(1,'登录模块','/user/login/','{\'user_id\': \'root\', \'password\': \'*********\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0','1002','Windows 10','{\'code\': 1002, \'msg\': \'登录成功\'}',0),
(2,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(3,'登录模块','/user/login/','{\'user_id\': \'root\', \'password\': \'*********\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0','1002','Windows 10','{\'code\': 1002, \'msg\': \'登录成功\'}',0),
(4,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(5,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(6,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(7,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(8,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(9,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(10,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(11,'登录模块','/user/login/','{\'user_id\': \'root\', \'password\': \'*********\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0','1002','Windows 10','{\'code\': 1002, \'msg\': \'登录成功\'}',0),
(12,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(13,'登录模块','/user/login/','{\'user_id\': \'root\', \'password\': \'*********\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0','1002','Windows 10','{\'code\': 1002, \'msg\': \'登录成功\'}',0),
(14,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(15,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(16,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(17,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(18,'menu','/user/menu/','{\'name\': \'role\', \'icon\': \'Connection\', \'path\': \'/authority/authorityEdit\', \'title\': \'关联角色菜单\', \'pid\': 1}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(19,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(20,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(21,'menu','/user/menu/','{\'name\': \'api\', \'icon\': \'MoonNight\', \'path\': \'/api\', \'title\': \'API工作区\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(22,'menu','/user/menu/','{\'name\': \'project\', \'icon\': \'MilkTea\', \'path\': \'/api/project\', \'title\': \'立项管理\', \'pid\': 5}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(23,'menu','/user/menu/','{\'name\': \'module\', \'icon\': \'Notebook\', \'path\': \'/api/module\', \'title\': \'测试套件\', \'pid\': 5}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(24,'menu','/user/menu/','{\'name\': \'template\', \'icon\': \'DocumentCopy\', \'path\': \'/api/template\', \'title\': \'请求模板\', \'pid\': 5}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(25,'menu','/user/menu/','{\'name\': \'case\', \'icon\': \'CoffeeCup\', \'path\': \'/api/case\', \'title\': \'测试用例\', \'pid\': 5}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(26,'menu','/user/menu/','{\'name\': \'scenario\', \'icon\': \'ColdDrink\', \'path\': \'/api/scenario\', \'title\': \'场景设计\', \'pid\': 5}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(27,'menu','/user/menu/','{\'name\': \' report\', \'icon\': \'Odometer\', \'path\': \'/report\', \'title\': \'调度任务\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(28,'menu','/user/menu/','{\'name\': \'report-cron\', \'icon\': \'Tickets\', \'path\': \'/api/report\', \'title\': \'测试报告\', \'pid\': 11}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(29,'role','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(30,'','/api/project/','{\'name\': \'容器云\', \'description\': \'容器云\', \'start\': \'2022-07-16\', \'end\': \'2022-07-16\', \'process\': 98, \'statue\': \'1\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(31,'','/api/project/2c398ddc74b647a693b2ce11118144ed/','{\'uid\': \'2c398ddc74b647a693b2ce11118144ed\', \'statue_display\': \'有效\', \'testsuit_set\': [], \'statue\': \'1\', \'create_time\': \'2022-07-16 11:44:10\', \'update_time\': \'2022-07-16 11:44:10\', \'name\': \'容器云\', \'description\': \'容器云\', \'start\': \'2022-07-16\', \'end\': \'2022-07-16\', \'process\': 98, \'last_execute\': 0, \'owner\': \'root\'}','PUT',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'更新成功\'}',0),
(32,'','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(33,'test suit','/api/send/request/','{\'url\': \'http://192.168.44.129:9000/api/auth\', \'header\': [{\'field\': \'Content-Type\', \'val\': \'application/json\'}], \'method\': \'1\', \'data\': \'{\"username\": \"{{username}}\", \"password\": \"{{password}}\"}\', \'default\': [{\'field\': \'username\', \'type\': 0, \'val\': \'admin\'}, {\'field\': \'password\', \'type\': 0, \'val\': \'aaaa1111!\'}]}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(34,'templates','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(35,'test case','/api/parameter-fields/','{\'case\': \'3a1407fea7264dbb8a077b18cc8de6cf\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(36,'scenario','/api/send/request/','{\'url\': \'http://192.168.44.129:9000/api/auth\', \'header\': [{\'field\': \'Content-Type\', \'val\': \'application/json\'}], \'method\': \'1\', \'data\': \'{\\n    \"password\": \"{{password}}\",\\n    \"username\": \"{{username}}\"\\n}\', \'default\': [{\'field\': \'username\', \'type\': 0, \'val\': \'\'}, {\'field\': \'password\', \'type\': 0, \'val\': \'\'}]}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(37,'menu','/user/menu/','{\'name\': \'test\', \'icon\': \'menu\', \'path\': \'/test\', \'title\': \'test\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(38,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(39,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(40,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(41,'menu','/user/menu/','{\'name\': \'dsd\', \'icon\': \'menu\', \'path\': \'/test1\', \'title\': \'dsad\', \'pid\': 13}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(42,'role','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(43,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(44,'menu','/user/menu/','{\'name\': \'eee\', \'icon\': \'Mnue\', \'path\': \'/test\', \'title\': \'eee\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(45,'menu','/user/menu/','{\'name\': \'tee\', \'icon\': \'menu\', \'path\': \'/test2\', \'title\': \'tes\', \'pid\': 16}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(46,'role','/user/role/d9b4b4797b554db8ae4ac4e22ec9f1s1/','{\'name\': \'超级管理员\', \'menu\': [2, 3, 4, 6, 7, 8, 9, 10, 12, 17], \'_id\': \'d9b4b4797b554db8ae4ac4e22ec9f1s1\'}','PUT',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'更新成功\'}',0),
(47,'menu','/user/menu/','{\'name\': \'eeeeeee\', \'icon\': \'Menu\', \'path\': \'/dfdsfdsf\', \'title\': \'eeeee\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(48,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(49,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(50,'role','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(51,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(52,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(53,'menu','/user/menu/','{\'name\': \'rrr\', \'icon\': \'rrr\', \'path\': \'/rrr\', \'title\': \'rr\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(54,'menu','/user/menu/21/','{}','DELETE',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'删除成功\'}',0),
(55,'menu','/user/menu/','{\'name\': \'rrr\', \'icon\': \'rrr\', \'path\': \'/rrr\', \'title\': \'rrr\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(56,'menu','/user/menu/','{\'name\': \'ddd\', \'icon\': \'ddd\', \'path\': \'/ddd\', \'title\': \'ddd\', \'pid\': 22}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(57,'menu','/user/menu/','{\'name\': \'fff\', \'icon\': \'fff\', \'path\': \'/ffff\', \'title\': \'fff\', \'pid\': 22}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(58,'menu','/user/menu/22/','{}','DELETE',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'删除成功\'}',0),
(59,'menu','/user/menu/','{\'name\': \'eee\', \'icon\': \'eee\', \'path\': \'/eee\', \'title\': \'eee\', \'pid\': 11}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': \'创建成功\'}',0),
(60,'role','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(61,'menu','/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(62,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(63,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(64,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(65,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(66,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(67,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(68,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(69,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(70,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(71,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(72,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(73,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(74,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(75,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(76,'登录模块','/user/login/','{\'user_id\': \'root\', \'password\': \'*********\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0','1002','Windows 10','{\'code\': 1002, \'msg\': \'登录成功\'}',0),
(77,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(78,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(79,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(80,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(81,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(82,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(83,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(84,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(85,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(86,NULL,'/api/process-parameterized/','{\'{\\n    \"password\": \"{{password}}\",\\n    \"username\": \"{{username}}\"\\n}\': \'\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(87,NULL,'/api/process-parameterized/','{\'{\\n    \"password\": \"{{password}}\",\\n    \"username\": \"{{username}}\"\\n}\': \'\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(88,NULL,'/api/process-parameterized/','{\'{\\n    \"password\": \"{{password}}\",\\n    \"username\": \"{{username}}\"\\n}\': \'\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(89,NULL,'/api/process-parameterized/','{\'{\\n    \"password\": \"{{password}}\",\\n    \"username\": \"{{username}}\"\\n}\': \'\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(90,NULL,'/api/process-parameterized/','{\'{\\n    \"password\": \"{{password}}\",\\n    \"username\": \"{{username}}\"\\n}\': \'\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(91,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(92,NULL,'/api/process-parameterized/','{\'{\\n    \"password\": \"{{password}}\",\\n    \"username\": \"{{username}}\"\\n}\': \'\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(93,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(94,NULL,'/api/process-parameterized/','{\'{\\n    \"password\": \"{{password}}\",\\n    \"username\": \"{{username}}\"\\n}\': \'\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(95,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(96,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(97,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(98,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(99,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(100,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(101,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(102,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0),
(103,NULL,'/user/user-menus/','{\'user_id\': \'root\'}','POST',NULL,'127.0.0.1','Chrome 103.0.0',NULL,'Windows 10','{\'code\': None, \'msg\': None}',0);

/*Table structure for table `templates` */

DROP TABLE IF EXISTS `templates`;

CREATE TABLE `templates` (
  `uid` varchar(64) NOT NULL,
  `statue` smallint NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `name` varchar(64) NOT NULL,
  `url` varchar(128) NOT NULL,
  `method` smallint NOT NULL,
  `header` json DEFAULT NULL,
  `data` json DEFAULT NULL,
  `default` json DEFAULT NULL,
  `process_name` varchar(32) DEFAULT NULL,
  `linux_order_str` varchar(100) DEFAULT NULL,
  `table_name` varchar(32) DEFAULT NULL,
  `owner_id` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `name` (`name`),
  KEY `templates_owner_id_f964e65a_fk_user_user_id` (`owner_id`),
  KEY `templates_name_061fc9_idx` (`name`),
  CONSTRAINT `templates_owner_id_f964e65a_fk_user_user_id` FOREIGN KEY (`owner_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `templates` */

insert  into `templates`(`uid`,`statue`,`create_time`,`update_time`,`name`,`url`,`method`,`header`,`data`,`default`,`process_name`,`linux_order_str`,`table_name`,`owner_id`) values 
('219baffcb4cb4c33956526fe2deef0ff',1,'2022-07-16 11:57:47.055763','2022-07-16 11:57:47.055763','请求认证接口','http://192.168.44.129:9000/api/auth',1,'{\"Content-Type\": \"application/json\"}','{\"password\": \"{{password}}\", \"username\": \"{{username}}\"}','[{\"val\": \"admin\", \"type\": 0, \"field\": \"username\"}, {\"val\": \"aaaa1111!\", \"type\": 0, \"field\": \"password\"}]','','','','root');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `_id` varchar(64) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `statue` smallint NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_superuser` smallint NOT NULL,
  `user_id` varchar(32) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `name` varchar(32) NOT NULL,
  `sex` smallint NOT NULL,
  `upload` varchar(512) NOT NULL,
  `birthday` date DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `_id` (`_id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `mobile` (`mobile`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user` */

insert  into `user`(`_id`,`last_login`,`statue`,`create_time`,`update_time`,`email`,`password`,`is_superuser`,`user_id`,`mobile`,`name`,`sex`,`upload`,`birthday`) values 
('c9b4b4797b554db8ae4ac4e22ec9f121',NULL,1,'2022-07-16 10:52:13.303281','2022-07-16 10:52:13.311111','23142423@qq.com','pbkdf2_sha256$260000$1mfO2qnj9arwBuqW6VVnes$4KIK+65+nIW4xgan8xTMpuhl5N6C9lC7TTq+Ryt2gxU=',1,'root','18217334452','root',2,'icon/avatar.jpg/',NULL);

/*Table structure for table `user_groups` */

DROP TABLE IF EXISTS `user_groups`;

CREATE TABLE `user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userprofile_id` varchar(32) NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_groups_userprofile_id_group_id_4f89dcbd_uniq` (`userprofile_id`,`group_id`),
  KEY `user_groups_group_id_b76f8aba_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_groups_group_id_b76f8aba_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_groups_userprofile_id_beb76c2d_fk_user_user_id` FOREIGN KEY (`userprofile_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user_groups` */

/*Table structure for table `user_role` */

DROP TABLE IF EXISTS `user_role`;

CREATE TABLE `user_role` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userprofile_id` varchar(32) NOT NULL,
  `role_id` varchar(64) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_role_userprofile_id_role_id_1f6bfc60_uniq` (`userprofile_id`,`role_id`),
  KEY `user_role_role_id_6a11361a_fk_role__id` (`role_id`),
  CONSTRAINT `user_role_role_id_6a11361a_fk_role__id` FOREIGN KEY (`role_id`) REFERENCES `role` (`_id`),
  CONSTRAINT `user_role_userprofile_id_f484d27e_fk_user_user_id` FOREIGN KEY (`userprofile_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user_role` */

insert  into `user_role`(`id`,`userprofile_id`,`role_id`) values 
(1,'root','d9b4b4797b554db8ae4ac4e22ec9f1s1');

/*Table structure for table `user_user_permissions` */

DROP TABLE IF EXISTS `user_user_permissions`;

CREATE TABLE `user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userprofile_id` varchar(32) NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_user_permissions_userprofile_id_permission_id_4ee72930_uniq` (`userprofile_id`,`permission_id`),
  KEY `user_user_permission_permission_id_9deb68a3_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_user_permission_permission_id_9deb68a3_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_user_permissions_userprofile_id_e8e85966_fk_user_user_id` FOREIGN KEY (`userprofile_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `user_user_permissions` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
