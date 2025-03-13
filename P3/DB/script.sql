-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema SA-P3
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema SA-P3
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `SA-P3` DEFAULT CHARACTER SET utf8 ;
USE `SA-P3` ;

-- -----------------------------------------------------
-- Table `SA-P3`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SA-P3`.`Usuarios` (
  `idUsuarios` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(150) NULL,
  `email` VARCHAR(150) NULL,
  `password` VARCHAR(200) NULL,
  `rol` ENUM('empleado', 'aprobar', 'admin') NULL,
  `created_at` DATE NULL,
  `updated_at` DATE NULL,
  PRIMARY KEY (`idUsuarios`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SA-P3`.`Planillas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SA-P3`.`Planillas` (
  `idPlanillas` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(150) NULL,
  `fecha_creacion` DATE NULL,
  `estado` ENUM('pendiente', 'aprobado', 'rechazado') NULL,
  `created_at` DATE NULL,
  `updated_at` DATE NULL,
  `usuario_id` INT NULL,
  PRIMARY KEY (`idPlanillas`),
  INDEX `planillas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `planillas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `SA-P3`.`Usuarios` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SA-P3`.`Detalle_Planilla`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SA-P3`.`Detalle_Planilla` (
  `idDetalle` INT NOT NULL AUTO_INCREMENT,
  `salario_bruto` DOUBLE NULL,
  `descuentos` DOUBLE NULL,
  `salario_neto` DOUBLE NULL,
  `created_at` DATE NULL,
  `updated_at` DATE NULL,
  `planilla_id` INT NULL,
  `empleado_id` INT NULL,
  PRIMARY KEY (`idDetalle`),
  INDEX `detalle_planilla_idx` (`planilla_id` ASC) VISIBLE,
  INDEX `detalle_empleado_idx` (`empleado_id` ASC) VISIBLE,
  CONSTRAINT `detalle_planilla`
    FOREIGN KEY (`planilla_id`)
    REFERENCES `SA-P3`.`Planillas` (`idPlanillas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `detalle_empleado`
    FOREIGN KEY (`empleado_id`)
    REFERENCES `SA-P3`.`Usuarios` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SA-P3`.`Aprobaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SA-P3`.`Aprobaciones` (
  `idAprobaciones` INT NOT NULL AUTO_INCREMENT,
  `nivel_aprobacion` INT NULL,
  `estado` ENUM('pendiente', 'aprobado', 'rechazado') NULL,
  `fecha_aprobacion` DATE NULL,
  `crceated_at` DATE NULL,
  `updated_at` DATE NULL,
  `planilla_id` INT NULL,
  `usuario_id` INT NULL,
  PRIMARY KEY (`idAprobaciones`),
  INDEX `aprobaciones_planilla_idx` (`planilla_id` ASC) VISIBLE,
  INDEX `aprobaciones_usuario_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `aprobaciones_planilla`
    FOREIGN KEY (`planilla_id`)
    REFERENCES `SA-P3`.`Planillas` (`idPlanillas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `aprobaciones_usuario`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `SA-P3`.`Usuarios` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `SA-P3`.`Logs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `SA-P3`.`Logs` (
  `idLogs` INT NOT NULL AUTO_INCREMENT,
  `accion` VARCHAR(450) NULL,
  `fecha` DATE NULL,
  `usuario_id` INT NULL,
  PRIMARY KEY (`idLogs`),
  INDEX `logs_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `logs_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `SA-P3`.`Usuarios` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
