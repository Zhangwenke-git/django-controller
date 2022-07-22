/*Data for the table `menu` */

insert  into `menu`(`_id`,`statue`,`create_time`,`update_time`,`rid`,`name`,`title`,`icon`,`pid`,`path`,`order`) values
('c9b4b4797b554db8ae4ac4e22ec9f122',1,'2022-07-16 11:01:23.000000','2022-07-16 11:31:58.449327',1,'authority','权限管理','Setting',0,'/authority',9),
('c9b4b4797b554db8ae4ac4e22ec9e1w1',1,'2022-07-16 11:01:23.000000','2022-07-16 11:01:25.000000',2,'menu','菜单管理','Menu',1,'/authority/menuEdit',10),
('ce6ceb196898452ca54eab41a3fd2b6b',1,'2022-07-16 11:27:00.064487','2022-07-16 11:27:00.064487',3,'role','关联角色菜单','Connection',1,'/authority/authorityEdit',11),
('3bc264a6b9e343df8dc51ce774fc30b9',1,'2022-07-16 11:28:03.233028','2022-07-16 11:28:03.233028',4,'user','用户管理','User',1,'/authority/userList',12),
('03e161e73cc44098b2d2a6378869e268',1,'2022-07-16 11:33:15.923893','2022-07-16 11:33:15.923893',5,'api','API工作区','MoonNight',0,'/api',1),
('41b47f62745649dc9218d89dbba264a9',1,'2022-07-16 11:34:07.590519','2022-07-16 11:34:07.590519',6,'project','立项管理','MilkTea',5,'/api/project',2),
('37ab0862f0414acbb74bbc1cfe297611',1,'2022-07-16 11:34:56.590079','2022-07-16 11:34:56.590079',7,'module','测试套件','Notebook',5,'/api/module',3),
('58491173e7a140e98e636a9228546d42',1,'2022-07-16 11:36:39.918348','2022-07-16 11:36:39.918348',8,'template','请求模板','DocumentCopy',5,'/api/template',4),
('3a53216c8bce43279ac0d2f5137e4df8',1,'2022-07-16 11:37:41.449140','2022-07-16 11:37:41.449140',9,'case','测试用例','CoffeeCup',5,'/api/case',5),
('0b97052ef0ea4dc9b7cf85f1533b1880',1,'2022-07-16 11:38:20.825814','2022-07-16 11:38:20.825814',10,'scenario','场景设计','ColdDrink',5,'/api/scenario',6),
('74049e8f0919468bb9b45471739b5eea',1,'2022-07-16 11:39:52.342582','2022-07-16 11:39:52.342582',11,'report','调度任务','Odometer',0,'/report',7),
('7e2b0ce6ca73483ea415b4cd34d4babb',1,'2022-07-16 11:41:23.079766','2022-07-16 11:41:23.079766',12,'report-cron','测试报告','Tickets',11,'/api/report',8),
('9f7b45eeb9864084bc088a6e9a9ec370',1,'2022-07-18 15:23:01.728418','2022-07-18 15:23:01.728418',26,'about','关于我们','CoffeeCup',0,'/about',17),
('62e86e2b4825467fac4524be26f719b4',1,'2022-07-18 15:23:52.093622','2022-07-18 15:23:52.093622',27,'help','使用手册','Collection',26,'/about/help',18),
('cbcd33cdd6de4dbcb7b8a78fc6ef9c8b',1,'2022-07-18 15:25:26.647338','2022-07-18 15:25:26.647338',28,'team','团队介绍','Opportunity',26,'/about/us',19),
('6c5f549008174a559072bfc268572b91',1,'2022-07-20 10:12:53.850767','2022-07-20 10:12:53.850767',29,'public','信息配置','Setting',0,'/public',13),
('12691e274b414146a8480b722e607adc',1,'2022-07-20 10:27:31.763367','2022-07-20 10:27:31.763367',30,'dbinfo','数据库配置','Suitcase',29,'/public/dbinfo',14),
('402cabe7fa5642e1a3e2f52ae79867a7',1,'2022-07-20 10:28:44.821177','2022-07-20 10:28:44.821177',31,'redisinfo','Redis配置','Money',29,'/public/redis',15),
('4828cc1973ea4df191a3b52804aba982',1,'2022-07-20 11:53:44.699618','2022-07-20 11:53:44.699618',32,'mq','MQ配置信息','Coin',29,'/public/mq',16);


/*Data for the table `role` */

insert  into `role`(`_id`,`name`,`describe`,`statue`,`create_time`,`update_time`) values
('0b1f9548af594740938e4c8c86652dfa','普通用户','普通使用权限，无权限管理模块权限',1,'2022-07-20 09:26:47.899841','2022-07-20 10:32:50.274102'),
('38710147e7f14a1d96f29c49515e0784','管理员','二级权限，无角色和菜单管理操作权限',1,'2022-07-20 09:26:01.937094','2022-07-20 10:32:56.660090'),
('942b0ba155b044b798ac7d58af8fccbd','审查用户','仅有调度任务权限',1,'2022-07-20 09:27:22.576319','2022-07-20 09:27:32.273298'),
('d9b4b4797b554db8ae4ac4e22ec9f1s1','超级管理员','超级管理员，拥有最高权限',1,'2022-07-16 11:06:07.000000','2022-07-20 10:30:43.099361');



insert  into `role_menu`(`id`,`role_id`,`menu_id`) values
(25,'0b1f9548af594740938e4c8c86652dfa',6),
(26,'0b1f9548af594740938e4c8c86652dfa',7),
(27,'0b1f9548af594740938e4c8c86652dfa',8),
(28,'0b1f9548af594740938e4c8c86652dfa',9),
(29,'0b1f9548af594740938e4c8c86652dfa',10),
(30,'0b1f9548af594740938e4c8c86652dfa',12),
(31,'0b1f9548af594740938e4c8c86652dfa',27),
(32,'0b1f9548af594740938e4c8c86652dfa',28),
(38,'0b1f9548af594740938e4c8c86652dfa',30),
(39,'0b1f9548af594740938e4c8c86652dfa',31),
(16,'38710147e7f14a1d96f29c49515e0784',4),
(17,'38710147e7f14a1d96f29c49515e0784',6),
(18,'38710147e7f14a1d96f29c49515e0784',7),
(19,'38710147e7f14a1d96f29c49515e0784',8),
(20,'38710147e7f14a1d96f29c49515e0784',9),
(21,'38710147e7f14a1d96f29c49515e0784',10),
(22,'38710147e7f14a1d96f29c49515e0784',12),
(23,'38710147e7f14a1d96f29c49515e0784',27),
(24,'38710147e7f14a1d96f29c49515e0784',28),
(40,'38710147e7f14a1d96f29c49515e0784',30),
(41,'38710147e7f14a1d96f29c49515e0784',31),
(34,'942b0ba155b044b798ac7d58af8fccbd',12),
(33,'942b0ba155b044b798ac7d58af8fccbd',27),
(35,'942b0ba155b044b798ac7d58af8fccbd',28),
(2,'d9b4b4797b554db8ae4ac4e22ec9f1s1',2),
(3,'d9b4b4797b554db8ae4ac4e22ec9f1s1',3),
(4,'d9b4b4797b554db8ae4ac4e22ec9f1s1',4),
(5,'d9b4b4797b554db8ae4ac4e22ec9f1s1',6),
(6,'d9b4b4797b554db8ae4ac4e22ec9f1s1',7),
(7,'d9b4b4797b554db8ae4ac4e22ec9f1s1',8),
(8,'d9b4b4797b554db8ae4ac4e22ec9f1s1',9),
(9,'d9b4b4797b554db8ae4ac4e22ec9f1s1',10),
(10,'d9b4b4797b554db8ae4ac4e22ec9f1s1',12),
(14,'d9b4b4797b554db8ae4ac4e22ec9f1s1',27),
(15,'d9b4b4797b554db8ae4ac4e22ec9f1s1',28),
(36,'d9b4b4797b554db8ae4ac4e22ec9f1s1',30),
(37,'d9b4b4797b554db8ae4ac4e22ec9f1s1',31);


/*Data for the table `user` */

insert  into `user`(`_id`,`last_login`,`statue`,`create_time`,`update_time`,`email`,`password`,`is_superuser`,`user_id`,`mobile`,`name`,`sex`,`upload`,`birthday`) values
('c9b4b4797b554db8ae4ac4e22ec9f121',NULL,1,'2022-07-16 10:52:13.303281','2022-07-16 10:52:13.311111','23142423@qq.com','pbkdf2_sha256$260000$1mfO2qnj9arwBuqW6VVnes$4KIK+65+nIW4xgan8xTMpuhl5N6C9lC7TTq+Ryt2gxU=',1,'root','18217334452','root',2,'icon/avatar.jpg/',NULL),
('dccf60b3c2584cad9087648073f981eb',NULL,1,'2022-07-20 09:28:44.771319','2022-07-20 09:28:44.771319','18217223323@qq.com','pbkdf2_sha256$260000$6U3GduWvjcQHFnofzR15Zy$M9P3/ocxXy+UrvmmaCEnS8u8DjXLC42NKITkkZ/WWpU=',0,'zhubaobao','18217223323','猪宝宝',2,'icon/avatar.jpg/',NULL);

insert  into `user_role`(`id`,`userprofile_id`,`role_id`) values
(1,'root','d9b4b4797b554db8ae4ac4e22ec9f1s1'),
(7,'zhubaobao','38710147e7f14a1d96f29c49515e0784');