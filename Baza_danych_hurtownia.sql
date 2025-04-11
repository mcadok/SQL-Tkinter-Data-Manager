CREATE TABLE `dostawcy` (
    `id_dostawcy` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
    `nazwa_dostawcy` VARCHAR(255),
    `adres` VARCHAR(255),
    `telefon` VARCHAR(255),
    `NIP` VARCHAR(255),
    `REGON` VARCHAR(255),
    `status` VARCHAR(255),
    PRIMARY KEY(`id_dostawcy`)
);

CREATE TABLE `produkty` (
    `id_produktu` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
    `id_dostawcy` VARCHAR(255),
    `cena_netto` VARCHAR(255) NULL,
    `cena_brutto` VARCHAR(255) NULL,
    `jednostka_miary` VARCHAR(255) NULL,
    `nazwa_produktu` VARCHAR(255) NULL,
    `status` VARCHAR(255) NULL,
    PRIMARY KEY(`id_produktu`)
);

CREATE TABLE `klienci` (
    `id_klienta` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
    `nazwa_klienta` VARCHAR(255) NULL,
    `biznes_tak_nie` VARCHAR(10) NULL,
    `NIP` VARCHAR(255),
    `REGON` VARCHAR(255),
    `PESEL` VARCHAR(255),
    `adres` VARCHAR(255) NULL,
    `telefon` VARCHAR(255),
    `email` VARCHAR(255) NULL,
    `status` VARCHAR(255) NULL,
    PRIMARY KEY(`id_klienta`)
);

CREATE TABLE `faktury` (
    `id_faktury` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
    `nr_faktury` VARCHAR(50) NULL,
    `data_wystawienia` VARCHAR(255) NULL,
    `data_sprzedazy` VARCHAR(255) NULL,
    `id_klienta` VARCHAR(255) NULL,
    `id_dostawcy` VARCHAR(255) NULL,
    `kwota_netto` DECIMAL(10,2) NULL,
    `kwota_brutto` DECIMAL(10,2) NULL,
    `sposob_platnosci` VARCHAR(255) NULL,
    PRIMARY KEY(`id_faktury`)
);

CREATE TABLE `zam_do_hurtowni` (
    `id_zdh` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
    `dostawca` VARCHAR(255) NULL,
    `data_zamowienia` VARCHAR(255) NULL,
    `status` VARCHAR(255) NULL,
    `calkowita_kwota` VARCHAR(255) NULL,
    PRIMARY KEY(`id_zdh`)
);

CREATE TABLE `szczegoly_zam_do_hurtowni` (
    `id_sz_zdh` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
    `id_zdh` VARCHAR(255) NULL,
    `id_produktu` VARCHAR(255) NULL,
    `ilosc` VARCHAR(255) NULL,
    `cena_suma` VARCHAR(255) NULL,
    PRIMARY KEY(`id_sz_zdh`)
);

CREATE TABLE `sprzedaz_z_hurtowni` (
    `id_sprz_zh` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
    `klient` VARCHAR(255) NULL,
    `data_sprzedazy` VARCHAR(255) NULL,
    `status` VARCHAR(255) NULL,
    `calkowita_kwota` VARCHAR(255) NULL,
    PRIMARY KEY(`id_sprz_zh`)
);

CREATE TABLE `szczegoly_sprz_z_hurtowni` (
    `id_sz_sprz_zh` BIGINT NOT NULL AUTO_INCREMENT UNIQUE,
    `id_sprz_zh` VARCHAR(255) NULL,
    `id_produktu` VARCHAR(255) NULL,
    `ilosc` VARCHAR(255) NULL,
    `cena_suma` VARCHAR(255) NULL,
    PRIMARY KEY(`id_sz_sprz_zh`)
);

-- Foreign Keys:
ALTER TABLE `produkty`
ADD FOREIGN KEY(`id_dostawcy`) REFERENCES `dostawcy`(`id_dostawcy`)
ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `faktury`
ADD FOREIGN KEY(`id_klienta`) REFERENCES `klienci`(`id_klienta`)
ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `faktury`
ADD FOREIGN KEY(`id_dostawcy`) REFERENCES `dostawcy`(`id_dostawcy`)
ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `zam_do_hurtowni`
ADD FOREIGN KEY(`dostawca`) REFERENCES `dostawcy`(`id_dostawcy`)
ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `szczegoly_zam_do_hurtowni`
ADD FOREIGN KEY(`id_zdh`) REFERENCES `zam_do_hurtowni`(`id_zdh`)
ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `szczegoly_zam_do_hurtowni`
ADD FOREIGN KEY(`id_produktu`) REFERENCES `produkty`(`id_produktu`)
ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `sprzedaz_z_hurtowni`
ADD FOREIGN KEY(`klient`) REFERENCES `klienci`(`id_klienta`)
ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `szczegoly_sprz_z_hurtowni`
ADD FOREIGN KEY(`id_sprz_zh`) REFERENCES `sprzedaz_z_hurtowni`(`id_sprz_zh`)
ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE `szczegoly_sprz_z_hurtowni`
ADD FOREIGN KEY(`id_produktu`) REFERENCES `produkty`(`id_produktu`)
ON UPDATE CASCADE ON DELETE CASCADE;
