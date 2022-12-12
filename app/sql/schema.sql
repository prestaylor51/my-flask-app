
create table givers
(
    id serial primary key,
    code varchar(10),
    name varchar(256) 
);

create table giver_receiver
(
    giver_id int references givers(id),
    receiver_id int references givers(id),
    constraint unique_giver_receiver unique(giver_id, receiver_id)
);

insert into givers
(code, name)
values
('ORANGE', 'MOM' ),
('BEAR', 'DAD'),
('ROCK', 'SPENCER'),
('OAK', 'JENNY'),
('SAND', 'PRESTON'),
('OCEAN', 'CAP'),
('SKY', 'OLIVE');