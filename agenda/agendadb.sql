create database IF NOT EXISTS agenda_db;
use agenda_db;

CREATE TABLE IF NOT EXISTS CP(
	CP VARCHAR(6) NOT NULL,
    cp_ciudad VARCHAR(35) NOT NULL,
    cp_estado VARCHAR(35) NOT NULL,
    PRIMARY KEY(CP)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS contactos(
	id_contacto INT NOT NULL AUTO_INCREMENT,
	c_nombre VARCHAR(35) NOT NULL,
    c_apaterno VARCHAR(35) NOT NULL,
    c_amaterno VARCHAR(35),
    c_correo VARCHAR(35),
    c_telefono VARCHAR(13),
    PRIMARY KEY(id_contacto)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS lugar(
	id_lugar INT NOT NULL AUTO_INCREMENT,
    l_calle VARCHAR(35) NOT NULL,
    l_noext vARCHAR(7) NOT NULL,
    l_noint VARCHAR(7),
    l_col VARCHAR(35),
    l_cp VARCHAR(6),
    l_descrip VARCHAR(100),
    PRIMARY KEY(id_lugar),
    CONSTRAINT fkcp_lugar FOREIGN KEY(l_cp)
    REFERENCES CP(CP)
		ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS cita(
	id_cita INT NOT NULL AUTO_INCREMENT,
    cita_fecha DATE NOT NULL,
    cita_hora TIME NOT NULL,
    cita_asunto VARCHAR(100),
    id_contacto INT NOT NULL,
    id_lugar INT NOT NULL,
    PRIMARY KEY(id_cita),
    CONSTRAINT fkcontactos_cita FOREIGN KEY(id_contacto)
    REFERENCES contactos(id_contacto)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fklugar_cita FOREIGN KEY(id_lugar)
    REFERENCES lugar(id_lugar)
		ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;