SELECT * FROM alunos;

SELECT nome_aluno,email_aluno FROM alunos;

SELECT nome_aluno,email_aluno FROM alunos ORDER BY nome_aluno;

SELECT nome_aluno, email_aluno FROM alunos WHERE nome_aluno ILIKE 'João';

SELECT nome_aluno, email_aluno FROM alunos WHERE nome_aluno  LIKE  '_A%';

SELECT nome_aluno, email_aluno FROM alunos WHERE nome_aluno  LIKE  'A%';

SELECT nome_aluno, email_aluno FROM alunos WHERE nome_aluno  ILIKE  '%A%';

SELECT id_livro FROM livros WHERE isbn_livro IS NULL;

SELECT titulo_livro, nome_autor, nome_editora FROM biblioteca.livros JOIN biblioteca.autores_do_livro ON livros.id_livro = autores_do_livro.id_livro JOIN biblioteca.autores ON autores_do_livro.id_autor = autores.id_autor JOIN biblioteca.editoras ON livros.id_editora = editoras.id_editora WHERE titulo_livro ILIKE '%algoritmo%' OR nome_autor ILIKE '%algoritmo%' OR nome_editora ILIKE '%algoritmo%' ORDER BY livros.titulo_livro;

SELECT id_reserva, titulo_livro, data_reserva, prazo_reserva FROM biblioteca.reservas JOIN biblioteca.livros ON reservas.id_livro = livros.id_livro WHERE id_aluno = 1;

SELECT last_value + 1 FROM pg_sequences WHERE schemaname = 'biblioteca' AND sequencename = 'livros_id_livro_seq';

SELECT livros.id_livro, titulo_livro, nome_editora, nome_categoria, ano_livro, idioma_livro, isbn_livro, quantidade_catalogo, quantidade_reservado, quantidade_locado FROM biblioteca.livros JOIN biblioteca.autores_do_livro ON autores_do_livro.id_livro = livros.id_livro JOIN biblioteca.autores ON autores_do_livro.id_autor = autores.id_autor JOIN biblioteca.editoras ON livros.id_editora = editoras.id_editora JOIN biblioteca.categorias ON livros.id_categoria = categorias.id_categoria GROUP BY livros.id_livro, biblioteca.livros.titulo_livro, editoras.nome_editora, categorias.nome_categoria ORDER BY biblioteca.livros.titulo_livro;