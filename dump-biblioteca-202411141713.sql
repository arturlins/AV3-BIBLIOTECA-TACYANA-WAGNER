PGDMP  !                
    |         
   biblioteca    16.4    16.4 B    3           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            4           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            5           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            6           1262    16447 
   biblioteca    DATABASE     �   CREATE DATABASE biblioteca WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE biblioteca;
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                pg_database_owner    false            7           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   pg_database_owner    false    4            �            1259    16462    administradores    TABLE     %  CREATE TABLE public.administradores (
    id_administrador integer NOT NULL,
    matricula_administrador character varying(10) NOT NULL,
    nome_administrador character varying(1000) NOT NULL,
    email_administrador character varying(200) NOT NULL,
    senha_administrador bytea NOT NULL
);
 #   DROP TABLE public.administradores;
       public         heap    postgres    false    4            �            1259    16461 $   administradores_id_administrador_seq    SEQUENCE     �   CREATE SEQUENCE public.administradores_id_administrador_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.administradores_id_administrador_seq;
       public          postgres    false    4    216            8           0    0 $   administradores_id_administrador_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.administradores_id_administrador_seq OWNED BY public.administradores.id_administrador;
          public          postgres    false    215            �            1259    16475    alunos    TABLE     %  CREATE TABLE public.alunos (
    id_aluno integer NOT NULL,
    matricula_aluno character varying(10) NOT NULL,
    nome_aluno character varying(1000) NOT NULL,
    email_aluno character varying(200) NOT NULL,
    curso_aluno character varying(200) NOT NULL,
    senha_aluno bytea NOT NULL
);
    DROP TABLE public.alunos;
       public         heap    postgres    false    4            �            1259    16474    alunos_id_aluno_seq    SEQUENCE     �   CREATE SEQUENCE public.alunos_id_aluno_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.alunos_id_aluno_seq;
       public          postgres    false    4    218            9           0    0    alunos_id_aluno_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.alunos_id_aluno_seq OWNED BY public.alunos.id_aluno;
          public          postgres    false    217            �            1259    16504    autores    TABLE     �   CREATE TABLE public.autores (
    id_autor integer NOT NULL,
    nome_autor character varying(500) NOT NULL,
    sobrenome_autor character varying(500) NOT NULL
);
    DROP TABLE public.autores;
       public         heap    postgres    false    4            �            1259    16503    autores_id_autor_seq    SEQUENCE     �   CREATE SEQUENCE public.autores_id_autor_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.autores_id_autor_seq;
       public          postgres    false    4    224            :           0    0    autores_id_autor_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.autores_id_autor_seq OWNED BY public.autores.id_autor;
          public          postgres    false    223            �            1259    16495 
   categorias    TABLE     z   CREATE TABLE public.categorias (
    id_categoria integer NOT NULL,
    nome_categoria character varying(100) NOT NULL
);
    DROP TABLE public.categorias;
       public         heap    postgres    false    4            �            1259    16494    categorias_id_categoria_seq    SEQUENCE     �   CREATE SEQUENCE public.categorias_id_categoria_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.categorias_id_categoria_seq;
       public          postgres    false    4    222            ;           0    0    categorias_id_categoria_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.categorias_id_categoria_seq OWNED BY public.categorias.id_categoria;
          public          postgres    false    221            �            1259    16488    editoras    TABLE     �   CREATE TABLE public.editoras (
    id_editora integer NOT NULL,
    nome_editora character varying(200) NOT NULL,
    local_editora character varying(150)
);
    DROP TABLE public.editoras;
       public         heap    postgres    false    4            �            1259    16487    editoras_id_editora_seq    SEQUENCE     �   CREATE SEQUENCE public.editoras_id_editora_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.editoras_id_editora_seq;
       public          postgres    false    4    220            <           0    0    editoras_id_editora_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.editoras_id_editora_seq OWNED BY public.editoras.id_editora;
          public          postgres    false    219            �            1259    16513    livros    TABLE     8  CREATE TABLE public.livros (
    id_livro integer NOT NULL,
    id_autor integer,
    titulo_livro character varying(2000) NOT NULL,
    id_editora integer,
    isbn_livro character(13),
    ano_livro integer,
    idioma_livro character varying(100),
    id_categoria integer,
    quantidade integer NOT NULL
);
    DROP TABLE public.livros;
       public         heap    postgres    false    4            �            1259    16512    livros_id_livro_seq    SEQUENCE     �   CREATE SEQUENCE public.livros_id_livro_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.livros_id_livro_seq;
       public          postgres    false    4    226            =           0    0    livros_id_livro_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.livros_id_livro_seq OWNED BY public.livros.id_livro;
          public          postgres    false    225            �            1259    16539    locacoes    TABLE     �   CREATE TABLE public.locacoes (
    id_locacao integer NOT NULL,
    id_livro integer,
    id_aluno integer,
    data_emprestimo date NOT NULL,
    data_devolucao date NOT NULL
);
    DROP TABLE public.locacoes;
       public         heap    postgres    false    4            �            1259    16538    locacoes_id_locacao_seq    SEQUENCE     �   CREATE SEQUENCE public.locacoes_id_locacao_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.locacoes_id_locacao_seq;
       public          postgres    false    228    4            >           0    0    locacoes_id_locacao_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.locacoes_id_locacao_seq OWNED BY public.locacoes.id_locacao;
          public          postgres    false    227            n           2604    16465     administradores id_administrador    DEFAULT     �   ALTER TABLE ONLY public.administradores ALTER COLUMN id_administrador SET DEFAULT nextval('public.administradores_id_administrador_seq'::regclass);
 O   ALTER TABLE public.administradores ALTER COLUMN id_administrador DROP DEFAULT;
       public          postgres    false    216    215    216            o           2604    16478    alunos id_aluno    DEFAULT     r   ALTER TABLE ONLY public.alunos ALTER COLUMN id_aluno SET DEFAULT nextval('public.alunos_id_aluno_seq'::regclass);
 >   ALTER TABLE public.alunos ALTER COLUMN id_aluno DROP DEFAULT;
       public          postgres    false    217    218    218            r           2604    16507    autores id_autor    DEFAULT     t   ALTER TABLE ONLY public.autores ALTER COLUMN id_autor SET DEFAULT nextval('public.autores_id_autor_seq'::regclass);
 ?   ALTER TABLE public.autores ALTER COLUMN id_autor DROP DEFAULT;
       public          postgres    false    223    224    224            q           2604    16498    categorias id_categoria    DEFAULT     �   ALTER TABLE ONLY public.categorias ALTER COLUMN id_categoria SET DEFAULT nextval('public.categorias_id_categoria_seq'::regclass);
 F   ALTER TABLE public.categorias ALTER COLUMN id_categoria DROP DEFAULT;
       public          postgres    false    222    221    222            p           2604    16491    editoras id_editora    DEFAULT     z   ALTER TABLE ONLY public.editoras ALTER COLUMN id_editora SET DEFAULT nextval('public.editoras_id_editora_seq'::regclass);
 B   ALTER TABLE public.editoras ALTER COLUMN id_editora DROP DEFAULT;
       public          postgres    false    220    219    220            s           2604    16516    livros id_livro    DEFAULT     r   ALTER TABLE ONLY public.livros ALTER COLUMN id_livro SET DEFAULT nextval('public.livros_id_livro_seq'::regclass);
 >   ALTER TABLE public.livros ALTER COLUMN id_livro DROP DEFAULT;
       public          postgres    false    226    225    226            t           2604    16542    locacoes id_locacao    DEFAULT     z   ALTER TABLE ONLY public.locacoes ALTER COLUMN id_locacao SET DEFAULT nextval('public.locacoes_id_locacao_seq'::regclass);
 B   ALTER TABLE public.locacoes ALTER COLUMN id_locacao DROP DEFAULT;
       public          postgres    false    227    228    228            $          0    16462    administradores 
   TABLE DATA           �   COPY public.administradores (id_administrador, matricula_administrador, nome_administrador, email_administrador, senha_administrador) FROM stdin;
    public          postgres    false    216   %O       &          0    16475    alunos 
   TABLE DATA           n   COPY public.alunos (id_aluno, matricula_aluno, nome_aluno, email_aluno, curso_aluno, senha_aluno) FROM stdin;
    public          postgres    false    218   �O       ,          0    16504    autores 
   TABLE DATA           H   COPY public.autores (id_autor, nome_autor, sobrenome_autor) FROM stdin;
    public          postgres    false    224   KT       *          0    16495 
   categorias 
   TABLE DATA           B   COPY public.categorias (id_categoria, nome_categoria) FROM stdin;
    public          postgres    false    222   U       (          0    16488    editoras 
   TABLE DATA           K   COPY public.editoras (id_editora, nome_editora, local_editora) FROM stdin;
    public          postgres    false    220   �U       .          0    16513    livros 
   TABLE DATA           �   COPY public.livros (id_livro, id_autor, titulo_livro, id_editora, isbn_livro, ano_livro, idioma_livro, id_categoria, quantidade) FROM stdin;
    public          postgres    false    226   "V       0          0    16539    locacoes 
   TABLE DATA           c   COPY public.locacoes (id_locacao, id_livro, id_aluno, data_emprestimo, data_devolucao) FROM stdin;
    public          postgres    false    228   aX       ?           0    0 $   administradores_id_administrador_seq    SEQUENCE SET     R   SELECT pg_catalog.setval('public.administradores_id_administrador_seq', 2, true);
          public          postgres    false    215            @           0    0    alunos_id_aluno_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.alunos_id_aluno_seq', 11, true);
          public          postgres    false    217            A           0    0    autores_id_autor_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.autores_id_autor_seq', 10, true);
          public          postgres    false    223            B           0    0    categorias_id_categoria_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.categorias_id_categoria_seq', 6, true);
          public          postgres    false    221            C           0    0    editoras_id_editora_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.editoras_id_editora_seq', 9, true);
          public          postgres    false    219            D           0    0    livros_id_livro_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.livros_id_livro_seq', 10, true);
          public          postgres    false    225            E           0    0    locacoes_id_locacao_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.locacoes_id_locacao_seq', 1, false);
          public          postgres    false    227            v           2606    16473 7   administradores administradores_email_administrador_key 
   CONSTRAINT     �   ALTER TABLE ONLY public.administradores
    ADD CONSTRAINT administradores_email_administrador_key UNIQUE (email_administrador);
 a   ALTER TABLE ONLY public.administradores DROP CONSTRAINT administradores_email_administrador_key;
       public            postgres    false    216            x           2606    16471 ;   administradores administradores_matricula_administrador_key 
   CONSTRAINT     �   ALTER TABLE ONLY public.administradores
    ADD CONSTRAINT administradores_matricula_administrador_key UNIQUE (matricula_administrador);
 e   ALTER TABLE ONLY public.administradores DROP CONSTRAINT administradores_matricula_administrador_key;
       public            postgres    false    216            z           2606    16469 $   administradores administradores_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.administradores
    ADD CONSTRAINT administradores_pkey PRIMARY KEY (id_administrador);
 N   ALTER TABLE ONLY public.administradores DROP CONSTRAINT administradores_pkey;
       public            postgres    false    216            |           2606    16486    alunos alunos_email_aluno_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_email_aluno_key UNIQUE (email_aluno);
 G   ALTER TABLE ONLY public.alunos DROP CONSTRAINT alunos_email_aluno_key;
       public            postgres    false    218            ~           2606    16484 !   alunos alunos_matricula_aluno_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_matricula_aluno_key UNIQUE (matricula_aluno);
 K   ALTER TABLE ONLY public.alunos DROP CONSTRAINT alunos_matricula_aluno_key;
       public            postgres    false    218            �           2606    16482    alunos alunos_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.alunos
    ADD CONSTRAINT alunos_pkey PRIMARY KEY (id_aluno);
 <   ALTER TABLE ONLY public.alunos DROP CONSTRAINT alunos_pkey;
       public            postgres    false    218            �           2606    16511    autores autores_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.autores
    ADD CONSTRAINT autores_pkey PRIMARY KEY (id_autor);
 >   ALTER TABLE ONLY public.autores DROP CONSTRAINT autores_pkey;
       public            postgres    false    224            �           2606    16502 (   categorias categorias_nome_categoria_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_nome_categoria_key UNIQUE (nome_categoria);
 R   ALTER TABLE ONLY public.categorias DROP CONSTRAINT categorias_nome_categoria_key;
       public            postgres    false    222            �           2606    16500    categorias categorias_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_pkey PRIMARY KEY (id_categoria);
 D   ALTER TABLE ONLY public.categorias DROP CONSTRAINT categorias_pkey;
       public            postgres    false    222            �           2606    16493    editoras editoras_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.editoras
    ADD CONSTRAINT editoras_pkey PRIMARY KEY (id_editora);
 @   ALTER TABLE ONLY public.editoras DROP CONSTRAINT editoras_pkey;
       public            postgres    false    220            �           2606    16522    livros livros_isbn_livro_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.livros
    ADD CONSTRAINT livros_isbn_livro_key UNIQUE (isbn_livro);
 F   ALTER TABLE ONLY public.livros DROP CONSTRAINT livros_isbn_livro_key;
       public            postgres    false    226            �           2606    16520    livros livros_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.livros
    ADD CONSTRAINT livros_pkey PRIMARY KEY (id_livro);
 <   ALTER TABLE ONLY public.livros DROP CONSTRAINT livros_pkey;
       public            postgres    false    226            �           2606    16544    locacoes locacoes_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.locacoes
    ADD CONSTRAINT locacoes_pkey PRIMARY KEY (id_locacao);
 @   ALTER TABLE ONLY public.locacoes DROP CONSTRAINT locacoes_pkey;
       public            postgres    false    228            �           2606    16523    livros livros_id_autor_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.livros
    ADD CONSTRAINT livros_id_autor_fkey FOREIGN KEY (id_autor) REFERENCES public.autores(id_autor);
 E   ALTER TABLE ONLY public.livros DROP CONSTRAINT livros_id_autor_fkey;
       public          postgres    false    226    224    4744            �           2606    16533    livros livros_id_categoria_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.livros
    ADD CONSTRAINT livros_id_categoria_fkey FOREIGN KEY (id_categoria) REFERENCES public.categorias(id_categoria);
 I   ALTER TABLE ONLY public.livros DROP CONSTRAINT livros_id_categoria_fkey;
       public          postgres    false    222    226    4742            �           2606    16528    livros livros_id_editora_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.livros
    ADD CONSTRAINT livros_id_editora_fkey FOREIGN KEY (id_editora) REFERENCES public.editoras(id_editora);
 G   ALTER TABLE ONLY public.livros DROP CONSTRAINT livros_id_editora_fkey;
       public          postgres    false    220    4738    226            �           2606    16550    locacoes locacoes_id_aluno_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.locacoes
    ADD CONSTRAINT locacoes_id_aluno_fkey FOREIGN KEY (id_aluno) REFERENCES public.alunos(id_aluno);
 I   ALTER TABLE ONLY public.locacoes DROP CONSTRAINT locacoes_id_aluno_fkey;
       public          postgres    false    218    228    4736            �           2606    16545    locacoes locacoes_id_livro_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.locacoes
    ADD CONSTRAINT locacoes_id_livro_fkey FOREIGN KEY (id_livro) REFERENCES public.livros(id_livro);
 I   ALTER TABLE ONLY public.locacoes DROP CONSTRAINT locacoes_id_livro_fkey;
       public          postgres    false    4748    228    226            $   �   x�e�;n1D���"g8\���6�x��#r�P��4���-�r�����/���./�tena:Ch`l�,R&��$zU���9ٕ��$�_T*CӨ�K1�%*<<MA@���ly|}?���F0��Zͺ>t��6�d�K^�I/�r���3c���H�V�h����E�e�u���u���E~      &   O  x���Mn�F���)x��WE�2��1l���r6-��a ��(A��E�E�9�/���F-�l��)6�{�^���>���_~��!ן��3�|8�K������˲��M�7�c�P�������g����6�k�����EX�&�q+�"��VB
)�2��ANAb���u���)D֓6�5����>^��M>9Uu���W��~?-?�nχ��ʇ�����e���E���!I�����bJ"Ͳ�+��x���g$9��R#l�g�3�.v����"�v(�|<uސ��!�\?�c��@��S��������i9�}^���|��ߨܕBtqW=�E@u	���PiCÿ�V5�V(���6�&��B���6��"��
m�1"4Q��a+G	 �0��繾��������ח?�RM���\�6O����y�])J�E��<���Q|�ܖ%$�����
h(X@�"VRD���X�۔�(FB�Q�x+�r�z�"��"4�V��x��\ߗ=1�qY��&�n�������%����^�R -X���aFM��"o�?���:X���K0�pmb֐��?�ě⸑���k������~�o��\�ʉ��e�}{�[%~�U���@~������GES�pWXu�HF�ï.,pM�g�D��v��5�O�Q�w���V����O�6�+1]ճ42��h%�D;[���q<��3�55�m#�Q2M(�ӳ��o�������ȿ��n�q��9��~(��)����������
�X�>�j�b�3vX��XI֨�ì�M0����,?��lM!���u�?aQ:x~�U+����|���}Y��җv���B���KR���ϻ�i��/RA���W���x��%�҃��c8�_��-~�`H��#��v�;Y�5Z���.��%��k,��1JT}Χ)J�8a���{2
�������G��u����p�њ\l��ך+PЗ ��� M�-
(,4'�G�3«��!D��m{��(J�̴ꌆ{;4����L��z�\0�l�͆%Z&9�a��֔pJ������BڦNQݏ����Ԃ��s�������pĉ[�u��f����2      ,   �   x���N1�����O�E��.��,\L��a�I�i+���_��f���	���"9yz�!�љ^=a˖'�]�z͒�b#��}P��{�w漸��+�3��M.x������&���`m<�8)z>k�%z�F��ӱ�f�ɒ����ոnb��i��]�������Ҥn+I�7���?��C�      *   a   x�3�(�O/J�M<����|.#Nǜ���̒��b.c΀��������D.N����SN�̒ԢĒҢD�����̜�̢D.3N������Q1z\\\ �2"�      (   �   x�m�;�0D��S�D����e�iVf�H��1-g�(�rQ���5̟NA��<�3���D͝MM�%i�j�¥�d����O��F'���_5�^�V�����e� 6I��#�8v���8��D2т��|�ܮ�V�;�      .   /  x���M��0���)��v����h`��`$�ٸO�"N��%8��-G�ŨJ4R��,�"'J\��z�B��m���4y�<<�o>B���+L��pDD?9��o}<�0�����
�*]Za�1��4���'���JQ�8br�9�yJ~p�rii�-�*����e�V�~�S�>��:L������B���em��V�Rk�ⲃ��1�=�0E��aX���]Q/���(�M�1��zWp;u���iE!n1�#�X�`��p����0-�[����H�;�Iy�]��Dr�9��D!g�{�t]�r�ܘBh+K2V���ݼq,߯�@��NGi�/:��T�ā�'���Hȓ�.�g$ZJVd�k�C?§c�����׬`������'�n�E��DA�=�H��p�Ñn�������V� J�@7ױ����}\�=�M��J��~!O��Ĉ7$m���W���H�0S@)k�E�<{�3Y���S��Wٲ`�tum$����a9xG�ͮ�n���Qt2g�����#i��l�;`�֊SZ��#����Q>9J޿�R�n|O:      0      x������ � �     