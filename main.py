--- ============ table CLASSES ==================
create table CLASSES(
    id_cl serial,
    nom_cl varchar(35),
    Coef  int,
    Niveau varchar(10),
    
);
--- ============ end table CLASSES ==================


--- ============ contraint table CLASSES ==================
alter table CLASSES add constraint dg_pkey primary key (id_cl);
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
alter table SERIES add constraint dg_pkey primary key (id_se);
alter table SERIES  add constraint not null nom_se;
alter table dg  SERIES constraint dg_unique unique (nom_se)
alter table ecoles SERIES constraint eco_fkey foreign key (id_dg) references to (dg) on update cascade on delete cascade;
--- ============ ennd contraint table CLASSES ==================
