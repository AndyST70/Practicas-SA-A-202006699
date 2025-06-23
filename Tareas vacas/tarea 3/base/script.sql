-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ci
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ci
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ci` DEFAULT CHARACTER SET utf8 ;
USE `ci` ;

-- -----------------------------------------------------
-- Table `ci`.`ambiente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ci`.`ambiente` (
  `idambiente` INT NOT NULL,
  `usuario` VARCHAR(150) NULL,
  `password_ci` VARCHAR(150) NULL,
  `rol` VARCHAR(50) NULL,
  PRIMARY KEY (`idambiente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ci`.`ci`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ci`.`ci` (
  `id_ci` INT NOT NULL AUTO_INCREMENT,
  `nombre_ci` VARCHAR(150) NULL,
  `tipo_ci` BIGINT(1) NULL DEFAULT 0,
  `descripcion` VARCHAR(2000) NULL,
  `numero_serie` VARCHAR(10) NULL,
  `version` VARCHAR(10) NULL,
  `estado` VARCHAR(15) NULL,
  `responsable` VARCHAR(150) NULL,
  `fecha_adquisicion` DATETIME NULL,
  `ubicacion` VARCHAR(250) NULL,
  `licencia` VARCHAR(150) NULL,
  `idambiente` INT NULL,
  PRIMARY KEY (`id_ci`),
  INDEX `ci_ambiente_idx` (`idambiente` ASC) VISIBLE,
  CONSTRAINT `ci_ambiente`
    FOREIGN KEY (`idambiente`)
    REFERENCES `ci`.`ambiente` (`idambiente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ci`.`documento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ci`.`documento` (
  `iddocumento` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `ruta` VARCHAR(45) NULL,
  PRIMARY KEY (`iddocumento`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ci`.`bitacora_cambio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ci`.`bitacora_cambio` (
  `idbitacora` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL,
  `fec_actual` DATETIME NULL,
  `fec_anterior` DATETIME NULL,
  PRIMARY KEY (`idbitacora`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ci`.`cambio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ci`.`cambio` (
  `idcambio` INT NOT NULL AUTO_INCREMENT,
  `nombre_ci` VARCHAR(45) NULL,
  `descripcion` VARCHAR(250) NULL,
  `id_doc` INT NULL,
  `id_ci` INT NULL,
  `id_bitacora` INT NULL,
  PRIMARY KEY (`idcambio`),
  INDEX `cambio_documento_idx` (`id_doc` ASC) VISIBLE,
  INDEX `cambio_ci_idx` (`id_ci` ASC) VISIBLE,
  INDEX `cambio_bitacora_idx` (`id_bitacora` ASC) VISIBLE,
  CONSTRAINT `cambio_documento`
    FOREIGN KEY (`id_doc`)
    REFERENCES `ci`.`documento` (`iddocumento`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `cambio_ci`
    FOREIGN KEY (`id_ci`)
    REFERENCES `ci`.`ci` (`id_ci`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `cambio_bitacora`
    FOREIGN KEY (`id_bitacora`)
    REFERENCES `ci`.`bitacora_cambio` (`idbitacora`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ci`.`arbol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ci`.`arbol` (
  `idarbol` INT NOT NULL AUTO_INCREMENT,
  `padre` INT NULL,
  `hijo` INT NULL,
  `tipo` VARCHAR(150) NULL,
  `idci` INT NULL,
  PRIMARY KEY (`idarbol`),
  INDEX `arbol_ci_idx` (`idci` ASC) INVISIBLE,
  CONSTRAINT `arbol_ci`
    FOREIGN KEY (`idci`)
    REFERENCES `ci`.`ci` (`id_ci`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- ambiente

INSERT INTO ambiente (idambiente, usuario, password_ci, rol)VALUES (1, 'admin', 'admin123', 'DEV');
-- CI 
INSERT INTO ci (nombre_ci, tipo_ci, descripcion, numero_serie, version, estado, responsable, fecha_adquisicion, ubicacion, licencia, idambiente)
VALUES 
('Servidor App', 0, 'Servidor de aplicaciones principal', 'SRV001', '1.0', 'Activo', 'Infraestructura', NOW(), 'DataCenter 1', 'LIC123', 1),
('Base de Datos', 0, 'MySQL para app financiera', 'DB001', '5.7', 'Activo', 'DBA', NOW(), 'DataCenter 2', 'LIC456', 1);

-- Documento
INSERT INTO documento (nombre, ruta)
VALUES ('Manual Configuración', '/docs/manual_config.pdf');

-- Bitácora de cambio
INSERT INTO bitacora_cambio (descripcion, fec_actual, fec_anterior)
VALUES ('Actualización de versión', NOW(), '2023-01-01 00:00:00');

-- Cambio (relacionado a CI id 1)
INSERT INTO cambio (nombre_ci, descripcion, id_doc, id_ci, id_bitacora)
VALUES ('Servidor App', 'Se actualizó a versión 1.0', 1, 1, 1);

-- Arbol (relación padre-hijo: servidor -> base de datos)
INSERT INTO arbol (padre, hijo, tipo, idci)
VALUES (1, 2, 'dependencia', 1);