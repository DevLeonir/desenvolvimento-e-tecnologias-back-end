create database tecNew;
use tecNew;

create table tb_cliente(
id_cliente_pk int primary key auto_increment,
nome varchar(20),
email varchar(40),
telefone varchar(15),
idade int
);

select * from tb_cliente;