select nombres, apellidos, cedula, cod_grado_seccion, responsable from estudiante
select names, lastnames, password, id from "user"
INSERT INTO public."grado_seccion"(cod_grado_seccion, grado_seccion)
VALUES ('11', '1er Año Seccion A');
INSERT INTO public."grado_seccion"(cod_grado_seccion, grado_seccion)
VALUES ('12', '1er Año Seccion B');
INSERT INTO public."grado_seccion"(cod_grado_seccion, grado_seccion)
VALUES ('13', '1er Año Seccion C');

INSERT INTO public."grado_seccion"(cod_grado_seccion, grado_seccion)
VALUES ('21', '2do Año Seccion A');
INSERT INTO public."grado_seccion"(cod_grado_seccion, grado_seccion)
VALUES ('22', '2do Año Seccion B');
INSERT INTO public."grado_seccion"(cod_grado_seccion, grado_seccion)
VALUES ('23', '2do Año Seccion C');

INSERT INTO public."grado_seccion"(cod_grado_seccion, grado_seccion)
VALUES ('31', '3er Año Seccion A');
INSERT INTO public."grado_seccion"(cod_grado_seccion, grado_seccion)
VALUES ('32', '3er Año Seccion B');
INSERT INTO public."grado_seccion"(cod_grado_seccion, grado_seccion)
VALUES ('33', '3er Año Seccion C');

INSERT INTO public."profesor"(cedula_prof, nombre, apellido)
VALUES ('12345', 'Marco', 'Perez');
INSERT INTO public."profesor"(cedula_prof, nombre, apellido)
VALUES ('54321', 'Rafael', 'Caldera');
INSERT INTO public."profesor"(cedula_prof, nombre, apellido)
VALUES ('6789', 'Simon', 'Bolivar');
INSERT INTO public."profesor"(cedula_prof, nombre, apellido)
VALUES ('9876', 'Antonio', 'Guzman');



select * from grado_seccion
select * from nota
select * from materia
select * from profesor
select * from asigna
select * from imparte

insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('1','cast10','11');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('2','ing10','11');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('3','mat10','11');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('4','edufis10','11');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('5','artpa10','11');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('6','ciennat10','11');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('7','ghc10','11');

insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('8','cast10','12');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('9','ing10','12');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('10','mat10','12');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('11','edufis10','12');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('12','artpa10','12');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('13','ciennat10','12');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('14','ghc10','12');

insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('15','cast10','13');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('16','ing10','13');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('17','mat10','13');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('18','edufis10','13');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('19','artpa10','13');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('20','ciennat10','13');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('21','ghc10','13');



insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('22','cast10','21');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('23','ing10','21');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('24','mat10','21');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('25','edufis10','21');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('26','artpa10','21');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('27','ciennat10','21');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('28','ghc10','21');

insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('29','cast10','22');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('30','ing10','22');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('31','mat10','22');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('32','edufis10','22');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('33','artpa10','22');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('34','ciennat10','22');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('35','ghc10','22');

insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('36','cast10','23');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('37','ing10','23');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('38','mat10','23');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('39','edufis10','23');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('40','artpa10','23');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('41','ciennat10','23');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('42','ghc10','23');



insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('43','cast10','31');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('44','ing10','31');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('45','mat10','31');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('46','edufis10','31');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('47','fis10','31');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('48','qui10','31');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('49','bio10','31');

insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('50','cast10','32');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('51','ing10','32');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('52','mat10','32');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('53','edufis10','32');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('54','fis10','32');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('55','qui10','32');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('56','bio10','32');

insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('57','cast10','33');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('58','ing10','33');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('59','mat10','33');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('60','edufis10','33');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('61','fis10','33');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('62','qui10','33');
insert into imparte(cod_imparte, cod_materia, cod_grado_seccion)
values ('63','bio10','33');

