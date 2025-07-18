--- ============ table DG ==================
create table dg(
    id_dg serial,
    nom_dg varchar(35),
    prenom_dg varchar(35),
    email_dg varchar(65),
    tel_dg varchar(85),
    pass_dg varchar(250),
    pass_dg_info varchar(50)
);
--- ============ end table DG ==================


--- ============ contraint table DG ==================
alter table dg add constraint dg_pkey primary key (id_dg);
alter table dg  add constraint not null email_dg;
alter table dg  add constraint not null pass_dg;
alter table dg  add constraint dg_unique unique (nom_dg,)
--- ============ ennd contraint table DG ==================
