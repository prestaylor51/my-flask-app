create database secret_santa;
use secret_santa;

create table santas
(
    id serial primary key,
    code varchar(4),
    name varchar(256) 
);

create table giver_receiver
(
    giver int references santas(id),
    receiver int references santas(id),
    constraint unique_giver_receiver unique(giver, receiver)
);

insert into santas
(code, name)
values
(random_string(4), 'MOM' ),
(random_string(4), 'DAD'),
(random_string(4), 'SPENCER'),
(random_string(4), 'JENNY'),
(random_string(4), 'PRESTON'),
(random_string(4), 'CHRISTENA');