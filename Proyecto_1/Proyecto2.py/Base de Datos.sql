CREATE TABLE IF NOT EXISTS USUARIOS (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(30) NOT NULL,
    APELLIDO VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS TAREAS (
    CODIGO INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR(30) NOT NULL,
    FECHA_CREACION DATETIME NOT NULL,
    USUARIO_ID INT,
    FOREIGN KEY (USUARIO_ID) REFERENCES USUARIOS(ID)
);

CREATE TABLE IF NOT EXISTS NOTAS (
    CODIGO_NOTA INT AUTO_INCREMENT PRIMARY KEY,
    NOMBRE_NOTA VARCHAR(30) NOT NULL,
    FECHA_CREA_NOTA DATETIME NOT NULL,
    USUARIO_ID INT,
    FOREIGN KEY (USUARIO_ID) REFERENCES USUARIOS(ID)
);
