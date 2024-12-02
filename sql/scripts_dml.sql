INSERT INTO administradores(matricula_administrador, nome_administrador, email_administrador, senha_administrador)
VALUES
	('admin00', 'admin', 'admin', 'admin');

insert into alunos(matricula_aluno, nome_aluno, email_aluno, curso_aluno, senha_aluno)
values 
	('0000000001', 'João da Silva Santos', 'joaosilva@cesmac.edu.br', 'Medicina', '1234'),
	('0000000002', 'Ana Bispo da Cunha', 'anacunha@cesmac.edu.br', 'Design', '5678'),
	('0000000003', 'Maria Pereira Costa', 'mariacosta@cesmac.edu.br', 'Sistemas de Informação', '0910'),
	('1002000501', 'Ivo José Bulhões', 'ivobulhoes@cesmac.edu.br', 'Engenharia Civil', '1011'),
	('1002003007', 'Larrisa Lemos', 'larissalemos@cesmac.edu.br', 'Direito', '1213'),
	('2000301021', 'Letícia Sabino', 'leticiasabino@cesmac.edu.br', 'Medicina', '1415'),
	('0002005214', 'João da Silva dos Santos', 'joaosantos@cesmac.edu.br', 'Direito', '1617'),
	('2201000521', 'Carlos Eduardo Menezes', 'carlosmenezes@cesmac.edu.br', 'Sistemas de Informação', '1819'),
	('0005230001', 'Mauro Gomes Juscelino Lins', 'maurolins@cesmac.edu.br', 'Psicologia', '2021'),
	('1000002201', 'Tatiane Pinto Martins', 'tatianemartins@cesmac.edu.br', 'Pedagogia', '2223'),
	('0000000000', 'Aluno', 'aluno', 'Teste', 'aluno');

insert into editoras(nome_editora, local_editora)
values
	('Ágora', null),
	('Sextante', 'Rio de Janeiro/RJ'),
	('Alta Books', 'Rio de Janeiro/RJ'),
	('Novatec', 'São Paulo/SP'),
	('Rocco', null),
	('Principis', null),
	('Cengage', 'São Paulo/SP'),
	('Saraiva', 'São Paulo/SP'),
	('Bookman', null)
	('Vozes', Petrópolis/RJ);
	
insert into categorias(nome_categoria)
values
	('Programação'),
	('Algoritmos'),
	('Psicologia'),
	('Gestão'),
	('Literatura brasileira'),
	('Legislação'),
	('História'),
	('Medicina');
	
insert into autores(nome_autor)
values
	('Jeff Shutterland'),
	('Tim Brown'),
	('Marshall B. Rosenberg'),
	('Marco A. Furlan de Souza'),
	('Andrew Hunt'),
	('Clarice Lispector'),
	('Graciliano Ramos'),
	('Rodrigo de Barros Paes'),
	('Adita Y. Bhargava'),
	('Nilo Ney Coutinho Menezes'),
	('René Armand Dreifuss'),
	('Coletânea Saraiva Jur');

insert into livros(id_autor, titulo_livro, id_editora, isbn_livro, ano_livro, idioma_livro, id_categoria, quantidade)
values
	('1', 'Scrum: a arte de fazer o dobro do trabalho na metade do tempo', '2', '9788543107165', '2022', 'Português', '4', '10'),
	('6', 'A hora da estrela', '5', '9786555320350', '2024', 'Português', '5', '5'),
	('5', 'O programador pragmático', '9', '9768577807000', '2023', 'Português', '1', '25'),
	('4', 'Algoritmos e lógica da programação', '7', '9788522128143', '2020', 'Português', '2', '20'),
	('3', 'Comunicação não violenta: técnicas para aprimorar relacionamentos pessoais e profissionais', '1', '9788571832640', '2024', 'Português', '3', '15'),
	('10', 'Introdução à programação com Python: algoritmos e lógica de programação para iniciantes', '4', '9788575228869', '2024', 'Português', '1', '30'),
	('2', 'Design Thinking: uma metodologia poderosa para decretar o fim das velhas ideias', '3', '9788550814360', '2019', 'Português', '4', '5'),
	('7', 'Vidas secas', '6', '9786550971298', '2024', 'Português', '5', '3'),
	('9', 'Entendendo algoritmos: um guia ilustrado para programadores e outros curiosos', '4', '9788575225639', '2017', 'Português', '2', '12'),
	('8', 'Introdução à programação com a Linguagem C: aprenda a resolver problemas com uma abordagem prática', '4', null, '2016', 'Português', '1', '20'),
	('11', 'Vade Mecum Saraiva Tradicional - 2024', '8', '9786553628571', '2024', 'Português', '6', '1');
	;