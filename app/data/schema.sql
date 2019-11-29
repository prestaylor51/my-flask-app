
create table santas
(
    id serial primary key,
    code varchar(10),
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
('ORANGE', 'MOM' ),
('BEAR', 'DAD'),
('ROCK', 'SPENCER'),
('OAK', 'JENNY'),
('SAND', 'PRESTON'),
('OCEAN', 'CHRISTENA');