
create table givers
(
    id serial primary key,
    code varchar(10),
    name varchar(256) 
);

create table giver_receiver
(
    giver int references givers(id),
    receiver int references givers(id),
    constraint unique_giver_receiver unique(giver, receiver)
);

insert into givers
(code, name)
values
('ORANGE', 'MOM' ),
('BEAR', 'DAD'),
('ROCK', 'SPENCER'),
('OAK', 'JENNY'),
('SAND', 'PRESTON'),
('OCEAN', 'CHRISTENA');