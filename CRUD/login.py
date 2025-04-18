def login_usuarios(self, email, password):

        # Criptografia e hash para comparacao
        hashed = password
        
        self.cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
        comp_password = self.cursor.fetchone()[0]

        # Implementar a comfirmacao da senha
        if comp_password == password:
            print("Login realizado com sucesso!")
        else:
            print("Email ou senha incorretos.")

def registro(self, name, email, password, birthday_date, cpf, client_type,):
    
    # Implementar criptografia e hash
    hashed = password

    try:
        self.conn.autocommit = False  # Desativa commit automático
    
        # Insere o usuário na tabela de usuários
        self.cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed))
        self.cursor.execute("SELECT userID FROM users WHERE email = ?", (email,))
        user_id = self.cursor.fetchone()[0]

        # Verifica se o CPF já existe na tabela de clientes
        self.cursor.execute("SELECT * FROM clients WHERE cpf = ?", (cpf,))
        if self.cursor.fetchone():
            raise Exception("CPF já cadastrado.")
        
        # Insere o cliente na tabela de clientes
        self.cursor.execute("""INSERT INTO clients (name, birthday_date, cpf, client_type, userID)
                            VALUES (?, ?, ?, ?, ?)""",
                            (name, birthday_date, cpf, client_type, user_id))
        
        self.conn.commit()  # Faz o commit das alterações
        print("Usuário registrado com sucesso!")
    
    except Exception as e:
        self.conn.rollback()
        print(f"Erro ao registrar usuário: {e}")

    finally:
        self.conn.autocommit = True
