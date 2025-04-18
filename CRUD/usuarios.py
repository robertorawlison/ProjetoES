"""
CREATE TABLE users (
  userID INT AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  PRIMARY KEY (userID),
  UNIQUE KEY unique_email (email)
);

CREATE TABLE clients (
  clientID INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  birthday DATE,
  cpf VARCHAR(11) NOT NULL, -- sera feita a limpeza para manter apenas os numeros 
  rating DOUBLE,
  type INT,
  userID INT,
  PRIMARY KEY (clientID),
  UNIQUE KEY unique_cpf (cpf),
  FOREIGN KEY (userID) REFERENCES users(userID)
);

CREATE TABLE services (
  serviceID INT AUTO_INCREMENT,
  label VARCHAR(255),
  description VARCHAR(1000),
  location_x DOUBLE,
  location_y DOUBLE,
  coverage DOUBLE,
  providerID INT,
  PRIMARY KEY (serviceID),
  FOREIGN KEY (providerID) REFERENCES clients(clientID)
);

CREATE TABLE services_images (
  imageID INT AUTO_INCREMENT,
  filepath VARCHAR(255) NOT NULL,
  serviceID INT,
  PRIMARY KEY (imageID),
  FOREIGN KEY (serviceID) REFERENCES services(serviceID)
);

CREATE TABLE services_taken (
  takenID INT AUTO_INCREMENT,
  timestamp_service DATETIME,
  serviceID INT,
  clientID INT,
  providerID INT,
  PRIMARY KEY (takenID),
  FOREIGN KEY (serviceID) REFERENCES services(serviceID),
  FOREIGN KEY (clientID) REFERENCES clients(clientID),
  FOREIGN KEY (providerID) REFERENCES clients(clientID)
);
"""

class Usuarios:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor
    # Implementação do Crud de usuarios
    def inserir_usuario(self, name, birthday_date, cpf, rating, client_type, email, password):
        # Implementar criptografia e hash
        hashed = password

        try:
            self.conn.autocommit = False  # Desativa commit automático

            # Verifica se o cpf ja existe
            self.cursor.execute("SELECT * FROM clients WHERE cpf = ?", (cpf,))
            if self.cursor.fetchone():
                raise Exception("CPF já cadastrado.")
            
            
            

                    

        

    
        


