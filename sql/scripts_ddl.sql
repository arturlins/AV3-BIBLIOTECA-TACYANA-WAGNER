CREATE TABLE funcionarios (
	id_funcionario SERIAL PRIMARY KEY,
	matricula_funcionario VARCHAR(10) NOT NULL UNIQUE,
	nome_funcionario VARCHAR(1000) NOT NULL,
	email_funcionario VARCHAR(200) NOT NULL UNIQUE,
	senha_funcionario BYTEA NOT NULL
);

CREATE TABLE alunos (
	id_aluno SERIAL PRIMARY KEY,
	matricula_aluno VARCHAR(10) NOT NULL UNIQUE,
	nome_aluno VARCHAR(1000) NOT NULL,
	email_aluno VARCHAR(200) NOT NULL UNIQUE,
	curso_aluno VARCHAR(200) NOT NULL,
	reservas INT DEFAULT 0,
	emprestimos INT DEFAULT 0,
	senha_aluno BYTEA NOT NULL
);

CREATE TABLE editoras (
	id_editora SERIAL PRIMARY KEY,
	nome_editora VARCHAR(200) NOT NULL,
	local_editora varchar(150)
);

CREATE TABLE categorias (
	id_categoria SERIAL PRIMARY KEY,
	nome_categoria VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE autores (
	id_autor SERIAL PRIMARY KEY,
	nome_autor VARCHAR(500) NOT NULL
);

CREATE TABLE livros (
	id_livro SERIAL PRIMARY KEY,
	titulo_livro VARCHAR(2000) NOT NULL,
	id_editora INT REFERENCES editoras(id_editora),
	isbn_livro VARCHAR(17),
	ano_livro VARCHAR(4),
	idioma_livro VARCHAR(100),
	id_categoria INT REFERENCES categorias(id_categoria),
	quantidade_catalogo INT NOT NULL,
	id_funcionario INT REFERENCES funcionarios(id_funcionario),
	quantidade_reservado INT DEFAULT 0,
	quantidade_locado INT DEFAULT 0
);

CREATE TABLE autores_do_livro (
	id_autores_do_livro SERIAL PRIMARY KEY,
	id_livro INT REFERENCES livros(id_livro),
	id_autor INT REFERENCES autores(id_autor)
);

CREATE TABLE reservas (
	id_reserva SERIAL PRIMARY KEY,
	id_livro INT REFERENCES livros(id_livro),
	id_aluno INT REFERENCES alunos(id_aluno),
	data_reserva DATE NOT NULL,
	prazo_reserva DATE NOT NULL
);

CREATE TABLE locacoes (
	id_locacao SERIAL PRIMARY KEY,
	id_reserva INT REFERENCES reservas(id_reserva),
	id_livro INT REFERENCES livros(id_livro),
	id_aluno INT REFERENCES alunos(id_aluno),
	id_funcionario INT REFERENCES funcionarios(id_funcionario),
	data_emprestimo DATE,
	prazo_emprestimo_devolucao DATE,
	data_devolucao DATE,
	status_devolucao BOOLEAN DEFAULT FALSE,
	valor_multa DECIMAL(10, 2) DEFAULT 0
);