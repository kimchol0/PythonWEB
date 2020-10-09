-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: pro202
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `mid` int NOT NULL AUTO_INCREMENT,
  `mname` varchar(100) NOT NULL,
  `mdesc` text,
  `ming` varchar(120) NOT NULL,
  `mlink` varchar(200) NOT NULL,
  PRIMARY KEY (`mid`),
  UNIQUE KEY `mname` (`mname`)
) ENGINE=InnoDB AUTO_INCREMENT=274 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (1,'子时','23时—1时','甲子时','丙子时'),(2,'丑时','1时—3时','乙丑时','丁丑时'),(3,'寅时','3时—5时','丙寅时','戊寅时'),(4,'卯时','5时—7时','丁卯时','己卯时'),(5,'辰时','7时—9时','戊辰时','庚辰时'),(6,'巳时','9时—11时','己巳时','辛巳时'),(7,'午时','11时—13时','庚午时','壬午时'),(8,'未时','13时—15时','辛未时','癸未时'),(9,'申时','15时—17时','壬申时','甲申时'),(10,'酉时','17时—19时','癸酉时','乙酉时'),(11,'戌时','19时—21时','甲戌时','丙戌时'),(12,'亥时','21时—23时','乙亥时','丁亥时'),(13,'子时1','23时—1时','甲子时','丙子时'),(14,'丑时1','1时—3时','乙丑时','丁丑时'),(15,'寅时1','3时—5时','丙寅时','戊寅时'),(16,'卯时1','5时—7时','丁卯时','己卯时'),(17,'辰时1','7时—9时','戊辰时','庚辰时'),(18,'巳时1','9时—11时','己巳时','辛巳时'),(19,'午时1','11时—13时','庚午时','壬午时'),(20,'未时1','13时—15时','辛未时','癸未时'),(21,'申时1','15时—17时','壬申时','甲申时'),(22,'酉时1','17时—19时','癸酉时','乙酉时'),(23,'戌时1','19时—21时','甲戌时','丙戌时'),(24,'亥时1','21时—23时','乙亥时','丁亥时'),(25,'子时2','23时—1时','甲子时','丙子时'),(26,'丑时2','1时—3时','乙丑时','丁丑时'),(27,'寅时2','3时—5时','丙寅时','戊寅时'),(28,'卯时2','5时—7时','丁卯时','己卯时'),(29,'辰时2','7时—9时','戊辰时','庚辰时'),(30,'巳时2','9时—11时','己巳时','辛巳时'),(31,'午时2','11时—13时','庚午时','壬午时'),(32,'未时2','13时—15时','辛未时','癸未时'),(33,'申时2','15时—17时','壬申时','甲申时'),(34,'酉时2','17时—19时','癸酉时','乙酉时'),(35,'戌时2','19时—21时','甲戌时','丙戌时'),(36,'亥时2','21时—23时','乙亥时','丁亥时'),(37,'子时3','23时—1时','甲子时','丙子时'),(38,'丑时3','1时—3时','乙丑时','丁丑时'),(39,'寅时3','3时—5时','丙寅时','戊寅时'),(40,'卯时3','5时—7时','丁卯时','己卯时'),(41,'辰时3','7时—9时','戊辰时','庚辰时'),(42,'巳时3','9时—11时','己巳时','辛巳时'),(43,'午时3','11时—13时','庚午时','壬午时'),(44,'未时3','13时—15时','辛未时','癸未时'),(45,'申时3','15时—17时','壬申时','甲申时'),(46,'酉时3','17时—19时','癸酉时','乙酉时'),(47,'戌时3','19时—21时','甲戌时','丙戌时'),(48,'亥时3','21时—23时','乙亥时','丁亥时'),(49,'子时4','23时—1时','甲子时','丙子时'),(50,'丑时4','1时—3时','乙丑时','丁丑时'),(51,'寅时4','3时—5时','丙寅时','戊寅时'),(52,'卯时4','5时—7时','丁卯时','己卯时'),(53,'辰时4','7时—9时','戊辰时','庚辰时'),(54,'巳时4','9时—11时','己巳时','辛巳时'),(55,'午时4','11时—13时','庚午时','壬午时'),(56,'未时4','13时—15时','辛未时','癸未时'),(57,'申时4','15时—17时','壬申时','甲申时'),(58,'酉时4','17时—19时','癸酉时','乙酉时'),(59,'戌时4','19时—21时','甲戌时','丙戌时'),(60,'亥时4','21时—23时','乙亥时','丁亥时'),(61,'子时5','23时—1时','甲子时','丙子时'),(62,'丑时5','1时—3时','乙丑时','丁丑时'),(63,'寅时5','3时—5时','丙寅时','戊寅时'),(64,'卯时5','5时—7时','丁卯时','己卯时'),(65,'辰时5','7时—9时','戊辰时','庚辰时'),(66,'巳时5','9时—11时','己巳时','辛巳时'),(67,'午时5','11时—13时','庚午时','壬午时'),(68,'未时5','13时—15时','辛未时','癸未时'),(69,'申时5','15时—17时','壬申时','甲申时'),(70,'酉时5','17时—19时','癸酉时','乙酉时'),(71,'戌时5','19时—21时','甲戌时','丙戌时'),(72,'亥时5','21时—23时','乙亥时','丁亥时'),(73,'子时6','23时—1时','甲子时','丙子时');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-09 22:02:09
