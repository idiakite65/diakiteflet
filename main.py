
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
alter table dg  SERIES constraint se_unique unique (nom_se)
alter table SERIES constraint se_fkey foreign key (id_se) references to (ECOLE) on update cascade on delete cascade;
--- ============ ennd contraint table SERIES ==================

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
alter table MATIERES constraint ma_fkey foreign key (id_ma) references to (ECOLE) on update cascade on delete cascade;
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
alter table MATIERECLASSE constraint macl2_fkey foreign key (id_em) references to (ECOLE) on update cascade on delete cascade;
--- ============ ennd contraint table MATIERECLASSE ==================
