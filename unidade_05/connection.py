import mysql.connector

# Conecta ao banco de dados
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123321',
    database = 'tecNew',
)

NewConexao = conexao.cursor()

# ====== Insert ======
nomeCliente = "Cleber"
emailCliente = "cleber@cruzeirodosul.edu.br"
telefoneCliente = "11985862242"
idadeCliente = 18

comando_insert = f'INSERT INTO tb_cliente (nome, email, telefone, idade) VALUES ("{nomeCliente}","{emailCliente}", "{telefoneCliente}", "{idadeCliente}")'

NewConexao.execute(comando_insert)
conexao.commit()

# ====== Update ======
cliente = "Cleber"
idade = 26

comando_update = f'UPDATE tb_cliente SET idade = "{idade}" WHERE NOME = "{cliente}"'

NewConexao.execute(comando_update)
conexao.commit()

# ====== Delete ======
cliente = "Cleber"

comando_delete = f'DELETE from tb_cliente WHERE nome = "{cliente}"'

NewConexao.execute(comando_delete)
conexao.commit()

# ====== Select ======
cliente = "Bruno"

#comando_select = 'SELECT * FROM tb_cliente'
#comando_select = 'SELECT * FROM tb_cliente order by nome'
comando_select = f'SELECT * FROM tb_cliente Where nome = "{cliente}"'

NewConexao.execute(comando_select)

retorno = NewConexao.fetchall()
print(retorno)

# Fechar NewConexao e conexão
NewConexao.close()
conexao.close()