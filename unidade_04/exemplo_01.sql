create database XPTO;
use XPTO;

CREATE TABLE tb_departamento (
    id_departamento_pk INT AUTO_INCREMENT PRIMARY KEY,
    nome_departamento VARCHAR(100) NOT NULL
);

insert into tb_departamento (nome_departamento) values('Contabilidade');
insert into tb_departamento (nome_departamento) values('Financeiro');
insert into tb_departamento (nome_departamento) values('Estoque');
insert into tb_departamento (nome_departamento) values('Administrativo');
insert into tb_departamento (nome_departamento) values('T.I');

select * from tb_departamento;

CREATE TABLE tb_empregado(
id_empregado_pk INT PRIMARY KEY AUTO_INCREMENT,
nome CHAR(30),
cpf CHAR(14),
cargo CHAR(30),
salario FLOAT,
departamento_fk INT,
CONSTRAINT departamento_fk FOREIGN KEY (departamento_fk)
REFERENCES tb_departamento(id_departamento_pk)
);

insert into tb_empregado (nome, cpf, cargo, salario, departamento_fk)
	values('Bruno','856.854.468-32','Programador',4005.45,5);
insert into tb_empregado (nome, cpf, cargo, salario, departamento_fk)
	values('Paulo','102.888.632-85','DBA',6167.01,5);
insert into tb_empregado (nome, cpf, cargo, salario, departamento_fk)
	values('Maria','104.333.444-33','Administradora','7367.02',4);
insert into tb_empregado (nome, cpf, cargo, salario, departamento_fk)
	values('Isabel','666.555.444-55','Contadora','2222.30',1);
insert into tb_empregado (nome, cpf, cargo, salario, departamento_fk)
	values('João','444.444.333-22','Estoquista','2323.40',3);
insert into tb_empregado (nome, cpf, cargo, salario, departamento_fk)
	values('Rosana','222.333.444-43','Analista Financeiro','3333.44',2);
    
select * from tb_empregado

select nome, cargo from tb_empregado;

select * from tb_empregado where nome = 'Isabel';

select * from tb_empregado where salario > 5000;

select * from tb_empregado where salario > 5000 and salario < 7000;

select sum(salario), min(salario), max(salario) from tb_empregado;

SET SQL_SAFE_UPDATES = 0;

delete from tb_empregado where nome ='Paulo';

update tb_empregado set salario = 4357.45 where nome='Bruno';

alter table tb_empregado add column rg char(15);