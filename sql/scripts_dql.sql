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

SELECT * FROM biblioteca.autores_do_livro JOIN biblioteca.autores ON autores.id_autor = autores_do_livro.id_autor WHERE autores_do_livro.id_livro = 1;

SELECT livros.id_livro, titulo_livro, nome_editora, nome_categoria, ano_livro, idioma_livro, isbn_livro, quantidade_catalogo, quantidade_reservado, quantidade_locado FROM biblioteca.livros JOIN biblioteca.autores_do_livro ON autores_do_livro.id_livro = livros.id_livro JOIN biblioteca.autores ON autores_do_livro.id_autor = autores.id_autor JOIN biblioteca.editoras ON livros.id_editora = editoras.id_editora JOIN biblioteca.categorias ON livros.id_categoria = categorias.id_categoria GROUP BY livros.id_livro, biblioteca.livros.titulo_livro, editoras.nome_editora, categorias.nome_categoria ORDER BY biblioteca.livros.titulo_livro;

SELECT livros.id_livro, titulo_livro FROM biblioteca.livros JOIN biblioteca.autores_do_livro ON autores_do_livro.id_livro = livros.id_livro GROUP BY livros.id_livro ORDER BY biblioteca.livros.titulo_livro;

SELECT id_editora, nome_editora, local_editora FROM biblioteca.editoras ORDER BY nome_editora;

SELECT id_categoria, nome_categoria FROM biblioteca.categorias ORDER BY nome_categoria;

SELECT nome_aluno, matricula_aluno, curso_aluno, id_aluno FROM biblioteca.alunos ORDER BY nome_aluno;

SELECT locacoes.id_locacao, livros.id_livro, livros.titulo_livro, alunos.id_aluno, alunos.nome_aluno FROM biblioteca.locacoes JOIN biblioteca.livros ON locacoes.id_livro = livros.id_livro JOIN biblioteca.alunos ON locacoes.id_aluno = alunos.id_aluno WHERE locacoes.status_devolucao = FALSE;

SELECT id_reserva, titulo_livro, data_reserva, prazo_reserva, nome_aluno, reservas.id_aluno FROM biblioteca.reservas JOIN biblioteca.livros ON reservas.id_livro = livros.id_livro JOIN biblioteca.alunos ON reservas.id_aluno  = alunos.id_aluno;

SELECT id_locacao, multa_aplicada, valor_multa FROM biblioteca.locacoes WHERE data_devolucao IS NULL AND multa_aplicada = False AND prazo_emprestimo_devolucao < '2024-12-04';

SELECT id_locacao, multa_aplicada, valor_multa FROM biblioteca.locacoes WHERE multa_aplicada = TRUE AND id_locacao = 1;

SELECT id_reserva, titulo_livro, data_reserva, prazo_reserva FROM biblioteca.reservas JOIN biblioteca.livros ON reservas.id_livro = livros.id_livro WHERE id_aluno = 1;

SELECT id_locacao, titulo_livro, data_emprestimo, prazo_emprestimo_devolucao FROM biblioteca.locacoes JOIN biblioteca.livros ON locacoes.id_livro = livros.id_livro WHERE id_aluno = 1 AND status_devolucao = FALSE;