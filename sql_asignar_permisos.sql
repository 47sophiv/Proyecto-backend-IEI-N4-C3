GRANT SELECT, INSERT, UPDATE, DELETE
ON `mi_tienda`.*
TO 'mi_tienda'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE
ON `mi_tienda`.*
TO 'mi_tienda'@'%';

FLUSH PRIVILEGES;
