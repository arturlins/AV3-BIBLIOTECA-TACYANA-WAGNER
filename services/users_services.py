from config.db import criar_conexao
from config.seguranca import checar_password, criotpgrafar

def inserir_usuario(email, password):
    
    try:
        hashed_password = criotpgrafar(password)
        conn = criar_conexao()
        cursor = conn.cursor()

        sql = "INSERT INTO usuarios (email, password) VALUES (%s, %s)"        
        cursor.execute(sql, (email, hashed_password))
        conn.commit()

        print("Usuário criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
    finally:
        conn.close()

def login(email, password):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()

        sql = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(sql, (email,))
        resultado = cursor.fetchone()
        
    except Exception as e:
        print(f"Erro ao realizar login: {e}")
        return False
    finally:
        conn.close()
    if resultado:
        senha_hash = resultado[2]        
        if isinstance(senha_hash, memoryview):
            senha_hash = bytes(senha_hash)  # POSTGRES

        if checar_password(password, senha_hash):
            return resultado 
    return False
