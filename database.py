import sqlite3
import os


class Banco:
    def __init__(self):
        # Pasta onde está o projeto/programa
        pasta_projeto = os.path.dirname(os.path.abspath(__file__))

        # Caminho do banco
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

        # Permite acessar as colunas pelo nome
        self.conexao.row_factory = sqlite3.Row

        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS obreiros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                ativo INTEGER DEFAULT 1
            )
        """)

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

    # =========================
    # OBRIEIROS
    # =========================

    def adicionar_obreiro(self, nome, telefone=""):
        cursor = self.conexao.cursor()

        cursor.execute("""
            INSERT INTO obreiros (nome, telefone)
            VALUES (?, ?)
        """, (nome, telefone))

        self.conexao.commit()

        return cursor.lastrowid

    def listar_obreiros(self, apenas_ativos=True):
        cursor = self.conexao.cursor()

        if apenas_ativos:
            cursor.execute("""
                SELECT *
                FROM obreiros
                WHERE ativo = 1
                ORDER BY nome
            """)
        else:
            cursor.execute("""
                SELECT *
                FROM obreiros
                ORDER BY nome
            """)

        return cursor.fetchall()

    def buscar_obreiro(self, id):
        cursor = self.conexao.cursor()

        cursor.execute("""
            SELECT *
            FROM obreiros
            WHERE id = ?
        """, (id,))

        return cursor.fetchone()

    def atualizar_obreiro(self, id, nome, telefone=""):
        cursor = self.conexao.cursor()

        cursor.execute("""
            UPDATE obreiros
            SET nome = ?, telefone = ?
            WHERE id = ?
        """, (nome, telefone, id))

        self.conexao.commit()

    def desativar_obreiro(self, id):
        cursor = self.conexao.cursor()

        cursor.execute("""
            UPDATE obreiros
            SET ativo = 0
            WHERE id = ?
        """, (id,))

        self.conexao.commit()

    def ativar_obreiro(self, id):
        cursor = self.conexao.cursor()

        cursor.execute("""
            UPDATE obreiros
            SET ativo = 1
            WHERE id = ?
        """, (id,))

        self.conexao.commit()

    # =========================
    # ESCALAS
    # =========================

    def adicionar_escala(self, data, obreiro_id):
        cursor = self.conexao.cursor()

        cursor.execute("""
            INSERT INTO escalas (data, obreiro_id)
            VALUES (?, ?)
        """, (data, obreiro_id))

        self.conexao.commit()

        return cursor.lastrowid

    def listar_escalas(self):
        cursor = self.conexao.cursor()

        cursor.execute("""
            SELECT
                escalas.id,
                escalas.data,
                escalas.obreiro_id,
                obreiros.nome AS nome_obreiro
            FROM escalas
            INNER JOIN obreiros
                ON obreiros.id = escalas.obreiro_id
            ORDER BY escalas.data
        """)

        return cursor.fetchall()

    def buscar_escala(self, id):
        cursor = self.conexao.cursor()

        cursor.execute("""
            SELECT
                escalas.id,
                escalas.data,
                escalas.obreiro_id,
                obreiros.nome AS nome_obreiro
            FROM escalas
            INNER JOIN obreiros
                ON obreiros.id = escalas.obreiro_id
            WHERE escalas.id = ?
        """, (id,))

        return cursor.fetchone()

    def atualizar_escala(self, id, data, obreiro_id):
        cursor = self.conexao.cursor()

        cursor.execute("""
            UPDATE escalas
            SET data = ?, obreiro_id = ?
            WHERE id = ?
        """, (data, obreiro_id, id))

        self.conexao.commit()

    def excluir_escala(self, id):
        cursor = self.conexao.cursor()

        cursor.execute("""
            DELETE FROM escalas
            WHERE id = ?
        """, (id,))

        self.conexao.commit()

    # =========================
    # FECHAR BANCO
    # =========================

    def fechar(self):
        if self.conexao:
            self.conexao.close()