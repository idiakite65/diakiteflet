--- ============ table CLASSES ==================
create table CLASSES(
    id_cl serial,
    nom_cl varchar(35),
    Coef  int,
    Niveau varchar(10),    
);
--- ============ end table CLASSES ==================


--- ============ contraint table CLASSES ==================
alter table CLASSES add constraint cl_pkey primary key (id_cl);
alter table CLASSES  add constraint not null nom_cl;
alter table dg  CLASSES constraint not null Coef;
alter table dg  CLASSES constraint dg_unique unique (nom_cl)
--- ============ ennd contraint table CLASSES ==================



--- ============ table SERIES ==================
create table SERIES(
    id_se serial,
    nom_se varchar(35),
    id_ecol  int, 
);
--- ============ contraint table SERIES ==================
alter table SERIES add constraint se_pkey primary key (id_se);
alter table SERIES  add constraint not null nom_se;
alter table SERIES constraint se_unique unique (nom_se)
alter table SERIES constraint se_fkey foreign key (id_se) references to (ecoles) on update cascade on delete cascade;
--- ============ ennd contraint table SERIES ==================

--- ============ table EMPLOYEURS ==================
create table EMPLOYEURS(
    id_em serial,
    nom_em varchar(20),
    ader_em varchar(40),
    tel_em varchar(40), 
    typeem varchar(20),
    diplome varchar(20),
    fonction varchar(20),
    dateen date
    sexe varchar(10),
    id_ecol  int, 
);
--- ============ contraint table EMPLOYEURS ==================
alter table EMPLOYEURS add constraint emp_pkey primary key (id_em);
alter table EMPLOYEURS  add constraint not null nom_em;
alter table EMPLOYEURS  add constraint not null ader_em;
alter table EMPLOYEURS  add constraint not null tel_em;
alter table EMPLOYEURS  add constraint not null typeem;
alter table EMPLOYEURS  add constraint not null diplome;
alter table EMPLOYEURS  add constraint not null fonction;
alter table EMPLOYEURS  add constraint not null dateen;
alter table EMPLOYEURS  add constraint not null sexe;

alter table EMPLOYEURS constraint emp_fkey foreign key (id_ecol) references to (ecoles) on update cascade on delete cascade;
--- ============ ennd contraint table EMPLOYEURS ==================

--- ============ table MATIERES ==================
create table MATIERES(
    id_ma serial,
    nom_ma1 varchar(50),
    nom_ma2 varchar(50),
    coef_ma int,
    id_ecol  int, 
);
--- ============ contraint table MATIERES ==================
alter table MATIERES add constraint ma_pkey primary key (id_ma);
alter table MATIERES  add constraint not null nom_ma1;
alter table MATIERES  add constraint not null nom_ma2;
alter table MATIERES constraint ma_unique unique (nom_ma1)
alter table MATIERES constraint ma_fkey foreign key (id_ecol) references to (ecoles) on update cascade on delete cascade;
--- ============ ennd contraint table MATIERES ==================




--- ============ table MATIERECLASSE ==================
create table MATIERECLASSE(
    id_ma_cl serial,
    id_ma int,
    id_cl int,
    id_em int,   
);
--- ============ contraint table MATIERECLASSE ==================
alter table MATIERECLASSE add constraint ma_pkey primary key (id_ma_cl);
alter table MATIERECLASSE constraint macl1_fkey foreign key (id_ma) references to (MATIERES) on update cascade on delete cascade;
alter table MATIERECLASSE constraint macl2_fkey foreign key (id_cl) references to (CLASSES) on update cascade on delete cascade;
alter table MATIERECLASSE constraint macl2_fkey foreign key (id_em) references to (employeurs) on update cascade on delete cascade;
--- ============ ennd contraint table MATIERECLASSE ==================
