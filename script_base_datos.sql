-- ============================================================================
-- SCRIPT DE BASE DE DATOS: mi_tienda
-- Proyecto: Backend Django - Tienda Online (IEI N4 C3)
-- Generado: 2026-10-23 17:18:33
-- Motor: MySQL 8.x / 9.x / MariaDB
-- Descripción:
--   Este script crea la base de datos `mi_tienda`, configura tablas, índices,
--   relaciones foráneas e inserta los datos iniciales de la aplicación y del
--   sistema Django (incluyendo usuarios administradores y permisos).
-- ============================================================================

-- 1. Creación de la base de datos
CREATE DATABASE IF NOT EXISTS `mi_tienda` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `mi_tienda`;

-- 2. Creación opcional de usuario y permisos (según README del proyecto)
-- CREATE USER IF NOT EXISTS 'mi_tienda'@'%' IDENTIFIED BY 'Tienda1';
-- GRANT ALL PRIVILEGES ON `mi_tienda`.* TO 'mi_tienda'@'%';
-- FLUSH PRIVILEGES;

-- 3. Configuración del entorno de importación
SET FOREIGN_KEY_CHECKS = 0;
SET NAMES utf8mb4;

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `auth_group`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- (Sin registros iniciales para `auth_group`)

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `auth_group_permissions`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- (Sin registros iniciales para `auth_group_permissions`)

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `auth_permission`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `auth_permission` (44 registros)
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
  (25, 'Can add Categoría', 7, 'add_categoria'),
  (26, 'Can change Categoría', 7, 'change_categoria'),
  (27, 'Can delete Categoría', 7, 'delete_categoria'),
  (28, 'Can view Categoría', 7, 'view_categoria'),
  (29, 'Can add Cliente', 8, 'add_cliente'),
  (30, 'Can change Cliente', 8, 'change_cliente'),
  (31, 'Can delete Cliente', 8, 'delete_cliente'),
  (32, 'Can view Cliente', 8, 'view_cliente'),
  (33, 'Can add Pedido', 9, 'add_pedido'),
  (34, 'Can change Pedido', 9, 'change_pedido'),
  (35, 'Can delete Pedido', 9, 'delete_pedido'),
  (36, 'Can view Pedido', 9, 'view_pedido'),
  (37, 'Can add Producto', 10, 'add_producto'),
  (38, 'Can change Producto', 10, 'change_producto'),
  (39, 'Can delete Producto', 10, 'delete_producto'),
  (40, 'Can view Producto', 10, 'view_producto'),
  (41, 'Can add Detalle del Pedido', 11, 'add_detallepedido'),
  (42, 'Can change Detalle del Pedido', 11, 'change_detallepedido'),
  (43, 'Can delete Detalle del Pedido', 11, 'delete_detallepedido'),
  (44, 'Can view Detalle del Pedido', 11, 'view_detallepedido');

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `auth_user`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `auth_user` (2 registros)
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
  (1, 'pbkdf2_sha256$1000000$ZygUySn2ScgW2QW4vK1AVd$a+rM0q+VDz7QrMIBd4gB8m47qwmDaRA5SKxjn7LEtXc=', '2026-10-23 16:02:04.769736', 1, 'caros', '', '', 'sophia.caro@inacap.cl', 1, 1, '2026-10-01 18:58:10.439450'),
  (2, 'pbkdf2_sha256$1000000$CrYG5I61LM5pPS4g9gfX3F$Ue5pvlHxXLw5nAaT59DNNDyCj/hJ9raXxrEbV5SXSXw=', NULL, 1, 'cony', '', '', 'cony@gmail.com', 1, 1, '2026-10-01 19:06:53.154562');

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `auth_user_groups`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- (Sin registros iniciales para `auth_user_groups`)

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `auth_user_user_permissions`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- (Sin registros iniciales para `auth_user_user_permissions`)

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `django_admin_log`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- (Sin registros iniciales para `django_admin_log`)

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `django_content_type`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `django_content_type` (11 registros)
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
  (1, 'admin', 'logentry'),
  (3, 'auth', 'group'),
  (2, 'auth', 'permission'),
  (4, 'auth', 'user'),
  (5, 'contenttypes', 'contenttype'),
  (6, 'sessions', 'session'),
  (7, 'tienda_online', 'categoria'),
  (8, 'tienda_online', 'cliente'),
  (11, 'tienda_online', 'detallepedido'),
  (9, 'tienda_online', 'pedido'),
  (10, 'tienda_online', 'producto');

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `django_migrations`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `django_migrations` (19 registros)
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
  (1, 'contenttypes', '0001_initial', '2026-09-25 20:47:43.504156'),
  (2, 'auth', '0001_initial', '2026-09-25 20:47:44.158412'),
  (3, 'admin', '0001_initial', '2026-09-25 20:47:44.293925'),
  (4, 'admin', '0002_logentry_remove_auto_add', '2026-09-25 20:47:44.301611'),
  (5, 'admin', '0003_logentry_add_action_flag_choices', '2026-09-25 20:47:44.310369'),
  (6, 'contenttypes', '0002_remove_content_type_name', '2026-09-25 20:47:44.391600'),
  (7, 'auth', '0002_alter_permission_name_max_length', '2026-09-25 20:47:44.453309'),
  (8, 'auth', '0003_alter_user_email_max_length', '2026-09-25 20:47:44.477013'),
  (9, 'auth', '0004_alter_user_username_opts', '2026-09-25 20:47:44.485994'),
  (10, 'auth', '0005_alter_user_last_login_null', '2026-09-25 20:47:44.586688'),
  (11, 'auth', '0006_require_contenttypes_0002', '2026-09-25 20:47:44.588689'),
  (12, 'auth', '0007_alter_validators_add_error_messages', '2026-09-25 20:47:44.601213'),
  (13, 'auth', '0008_alter_user_username_max_length', '2026-09-25 20:47:44.710734'),
  (14, 'auth', '0009_alter_user_last_name_max_length', '2026-09-25 20:47:44.780619'),
  (15, 'auth', '0010_alter_group_name_max_length', '2026-09-25 20:47:44.800716'),
  (16, 'auth', '0011_update_proxy_permissions', '2026-09-25 20:47:44.809178'),
  (17, 'auth', '0012_alter_user_first_name_max_length', '2026-09-25 20:47:44.874913'),
  (18, 'sessions', '0001_initial', '2026-09-25 20:47:44.910980'),
  (19, 'tienda_online', '0001_initial', '2026-09-25 20:47:45.226647');

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `django_session`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `django_session` (1 registros)
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
  ('ad0fgraswk0kugydqbbz9l24zbcbpan2', '.eJxVjDkOwjAUBe_iGlnxGpuSnjNY_ktwANlSnFSIu0OkFNC-mXkvkfK2lrR1XtJM4iyUOP1ukPHBdQd0z_XWJLa6LjPIXZEH7fLaiJ-Xw_07KLmXb20GawgcePIWRs9krULr2IbgoomU_eSCoQlZo3I6MKCJwMNoNEd2Xrw_3gQ35w:1xKHiW:I7jEk_0GgxKeFaRHKpmEB-lCch7_Dq6S3DUenh2uyTg', '2026-11-06 16:02:04.772734');

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `tienda_online_categoria`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `tienda_online_categoria`;
CREATE TABLE `tienda_online_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci,
  `activo` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `tienda_online_categoria` (3 registros)
INSERT INTO `tienda_online_categoria` (`id`, `nombre`, `descripcion`, `activo`, `created_at`, `updated_at`) VALUES
  (1, 'Electrónica y Computación', 'Dispositivos electrónicos, componentes y accesorios de computación.', 1, '2026-09-25 10:00:00', '2026-09-25 10:00:00'),
  (2, 'Hogar y Oficina', 'Muebles, iluminación y artículos de oficina para trabajo remoto.', 1, '2026-09-25 10:00:00', '2026-09-25 10:00:00'),
  (3, 'Accesorios y Periféricos', 'Teclados, ratones, auriculares y complementos para setup.', 1, '2026-09-25 10:00:00', '2026-09-25 10:00:00');

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `tienda_online_cliente`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `tienda_online_cliente`;
CREATE TABLE `tienda_online_cliente` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_unicode_ci NOT NULL,
  `telefono` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `direccion` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `activo` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `tienda_online_cliente` (2 registros)
INSERT INTO `tienda_online_cliente` (`id`, `nombre`, `email`, `telefono`, `direccion`, `activo`, `created_at`, `updated_at`) VALUES
  (1, 'Carlos Soto Rodríguez', 'carlos.soto@ejemplo.com', '+56911223344', 'Av. Libertador Bernardo O\'Higgins 1234, Santiago', 1, '2026-09-25 10:30:00', '2026-09-25 10:30:00'),
  (2, 'Camila Morales Venegas', 'camila.morales@ejemplo.com', '+56988776655', 'Calle Los Alerces 567, Providencia, Santiago', 1, '2026-09-25 10:35:00', '2026-09-25 10:35:00');

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `tienda_online_producto`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `tienda_online_producto`;
CREATE TABLE `tienda_online_producto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int NOT NULL,
  `disponible` tinyint(1) NOT NULL,
  `imagen_url` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `categoria_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tienda_online_produc_categoria_id_6acde150_fk_tienda_on` (`categoria_id`),
  CONSTRAINT `tienda_online_produc_categoria_id_6acde150_fk_tienda_on` FOREIGN KEY (`categoria_id`) REFERENCES `tienda_online_categoria` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `tienda_online_producto` (4 registros)
INSERT INTO `tienda_online_producto` (`id`, `nombre`, `descripcion`, `precio`, `stock`, `disponible`, `imagen_url`, `created_at`, `updated_at`, `categoria_id`) VALUES
  (1, 'Laptop Ultrabook Pro 15', 'Procesador Intel Core i7, 16GB RAM, SSD 512GB NVMe, Pantalla FHD IPS 15.6 pulgadas.', 899990.00, 15, 1, 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853', '2026-09-25 10:05:00', '2026-09-25 10:05:00', 1),
  (2, 'Teclado Mecánico RGB Inalámbrico', 'Switches mecánicos táctiles, conectividad Bluetooth y 2.4GHz, retroiluminación RGB configurable.', 64990.00, 35, 1, 'https://images.unsplash.com/photo-1587829741301-dc798b83add3', '2026-09-25 10:10:00', '2026-09-25 10:10:00', 3),
  (3, 'Mouse Ergonómico Vertical', 'Sensor óptico de alta precisión 4000 DPI, diseño ergonómico para reducir fatiga de muñeca.', 39990.00, 50, 1, 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7', '2026-09-25 10:15:00', '2026-09-25 10:15:00', 3),
  (4, 'Silla Ergonómica de Oficina', 'Soporte lumbar ajustable, apoyabrazos 3D, malla transpirable y pistón de gas clase 4.', 179990.00, 10, 1, 'https://images.unsplash.com/photo-1580481077195-c3f995874258', '2026-09-25 10:20:00', '2026-09-25 10:20:00', 2);

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `tienda_online_pedido`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `tienda_online_pedido`;
CREATE TABLE `tienda_online_pedido` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_pedido` datetime(6) NOT NULL,
  `estado` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `total` decimal(12,2) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `cliente_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tienda_online_pedido_cliente_id_cd9617b7_fk_tienda_on` (`cliente_id`),
  CONSTRAINT `tienda_online_pedido_cliente_id_cd9617b7_fk_tienda_on` FOREIGN KEY (`cliente_id`) REFERENCES `tienda_online_cliente` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `tienda_online_pedido` (1 registros)
INSERT INTO `tienda_online_pedido` (`id`, `fecha_pedido`, `estado`, `total`, `created_at`, `updated_at`, `cliente_id`) VALUES
  (1, '2026-09-25 10:40:00', 'PAGADO', 964980.00, '2026-09-25 10:40:00', '2026-09-25 10:40:00', 1);

-- ----------------------------------------------------------------------------
-- Estructura y datos de la tabla `tienda_online_detallepedido`
-- ----------------------------------------------------------------------------
DROP TABLE IF EXISTS `tienda_online_detallepedido`;
CREATE TABLE `tienda_online_detallepedido` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int unsigned NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL,
  `pedido_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tienda_online_detall_pedido_id_5b2bc3c8_fk_tienda_on` (`pedido_id`),
  KEY `tienda_online_detall_producto_id_90dc62fb_fk_tienda_on` (`producto_id`),
  CONSTRAINT `tienda_online_detall_pedido_id_5b2bc3c8_fk_tienda_on` FOREIGN KEY (`pedido_id`) REFERENCES `tienda_online_pedido` (`id`),
  CONSTRAINT `tienda_online_detall_producto_id_90dc62fb_fk_tienda_on` FOREIGN KEY (`producto_id`) REFERENCES `tienda_online_producto` (`id`),
  CONSTRAINT `tienda_online_detallepedido_chk_1` CHECK ((`cantidad` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Datos para `tienda_online_detallepedido` (2 registros)
INSERT INTO `tienda_online_detallepedido` (`id`, `cantidad`, `precio_unitario`, `pedido_id`, `producto_id`) VALUES
  (1, 1, 899990.00, 1, 1),
  (2, 1, 64990.00, 1, 2);

-- Reactivar restricciones de claves foráneas
SET FOREIGN_KEY_CHECKS = 1;

-- ============================================================================
-- FIN DEL SCRIPT
-- ============================================================================