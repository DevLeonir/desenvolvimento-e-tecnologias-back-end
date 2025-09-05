create database tecNew;
use tecNew;

create table tb_client(
id_client_pk int primary key auto_increment,
nome varchar(20),
email varchar(40),
telefone varchar(15),
idade int
);

insert into tb_client(nome, email, telefone, idade) values ("Hugo", "hugogoes@gmail.com", "54-997888353", 31);

select * from tb_client;

insert into tb_client(nome, email, telefone, idade) values ("Bruno", "Bruno123@gmail.com", "31-997578253", 25);

select * from tb_client;

select nome from tb_client;

select nome, idade from tb_client;

select * from tb_client where nome = 'Hugo';

select * from tb_client where idade > 27;

update tb_client set idade = 29 where nome = 'Hugo';

set sql_safe_updates = 0;

select * from tb_client;

delete from tb_client where nome = 'Bruno';

drop table tb_client;