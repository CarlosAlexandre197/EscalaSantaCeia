import sqlite3
import os


class Banco:
    def __init__(self):
        # Caminho da pasta onde está o projeto/programa
        pasta_projeto = os.path.dirname(os.path.abspath(__file__))

        # Banco de dados dentro da pasta banco
        self.caminho_banco = os.path.join(
            pasta_projeto,
            "banco",
            "santa_ceia.db"
        )

        # Garante que a pasta banco exista
        os.makedirs(
            os.path.dirname(self.caminho_banco),
            exist_ok=True
        )

        self.conexao = sqlite3.connect(self.caminho_banco)
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conexao.cursor()

        # Tabela de obreiros
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS obreiros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                ativo INTEGER DEFAULT 1
            )
        """)

        # Tabela de escalas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS escalas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                obreiro_id INTEGER NOT NULL,
                FOREIGN KEY (obreiro_id)
                    REFERENCES obreiros (id)
            )
        """)

        self.conexao.commit()

    def fechar(self):
        self.conexao.close()