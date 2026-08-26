import sqlite3
import os
import sys


class Banco:

    def __init__(self):

        # ==================================================
        # LOCAL DO BANCO DE DADOS
        # ==================================================

        if getattr(sys, "frozen", False):

            # Quando estiver rodando pelo EXE
            pasta_projeto = os.path.dirname(
                sys.executable
            )

        else:

            # Quando estiver rodando pelo Python
            pasta_projeto = os.path.dirname(
                os.path.abspath(__file__)
            )

        self.caminho_banco = os.path.join(
            pasta_projeto,
            "banco",
            "santa_ceia.db"
        )
        
        print(
            "BANCO USADO PELO PROGRAMA:",
            self.caminho_banco
        )

        # Cria a pasta banco caso não exista
        os.makedirs(
            os.path.dirname(
                self.caminho_banco
            ),
            exist_ok=True
        )

        # ==================================================
        # CONEXÃO COM O BANCO
        # ==================================================

        self.conexao = sqlite3.connect(
            self.caminho_banco
        )

        self.conexao.row_factory = sqlite3.Row

        self.criar_tabelas()

    # ==================================================
    # CRIAÇÃO DAS TABELAS
    # ==================================================

    def criar_tabelas(self):

        cursor = self.conexao.cursor()

        # ==================================================
        # OBRIEIROS
        # ==================================================

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS obreiros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                ativo INTEGER DEFAULT 1
            )
        """)

        # ==================================================
        # SANTA CEIAS
        # ==================================================

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS santa_ceias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL UNIQUE
            )
        """)

        # ==================================================
        # RELAÇÃO SANTA CEIA X OBREIROS
        # ==================================================

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS santa_ceia_obreiros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                santa_ceia_id INTEGER NOT NULL,

                obreiro_id INTEGER NOT NULL,

                FOREIGN KEY (santa_ceia_id)
                    REFERENCES santa_ceias(id)
                    ON DELETE CASCADE,

                FOREIGN KEY (obreiro_id)
                    REFERENCES obreiros(id)
                    ON DELETE CASCADE,

                UNIQUE (
                    santa_ceia_id,
                    obreiro_id
                )
            )
        """)

        self.conexao.commit()

    # ==================================================
    # OBRIEIROS
    # ==================================================

    def adicionar_obreiro(
        self,
        nome,
        telefone=""
        ):

        cursor = self.conexao.cursor()

        cursor.execute("""
            INSERT INTO obreiros (
                nome,
                telefone
            )
            VALUES (?, ?)
        """, (
            nome,
            telefone
        ))

        self.conexao.commit()

        return cursor.lastrowid

    # ==================================================
    # LISTAR OBRIEIROS
    # ==================================================

    def listar_obreiros(
        self,
        apenas_ativos=True
        ):

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

    # ==================================================
    # BUSCAR OBRIEIRO
    # ==================================================

    def buscar_obreiro(
        self,
        id
        ):

        cursor = self.conexao.cursor()

        cursor.execute("""
            SELECT *
            FROM obreiros
            WHERE id = ?
        """, (
            id,
        ))

        return cursor.fetchone()

    # ==================================================
    # ATUALIZAR OBRIEIRO
    # ==================================================

    def atualizar_obreiro(
        self,
        id,
        nome,
        telefone=""
    ):

        cursor = self.conexao.cursor()

        cursor.execute("""
            UPDATE obreiros
            SET
                nome = ?,
                telefone = ?
            WHERE id = ?
        """, (
            nome,
            telefone,
            id
        ))

        self.conexao.commit()

    # ==================================================
    # DESATIVAR OBRIEIRO
    # ==================================================

    def desativar_obreiro(
        self,
        id
    ):

        cursor = self.conexao.cursor()

        cursor.execute("""
            UPDATE obreiros
            SET ativo = 0
            WHERE id = ?
        """, (
            id,
        ))

        self.conexao.commit()

    # ==================================================
    # ATIVAR OBRIEIRO
    # ==================================================

    def ativar_obreiro(
        self,
        id
    ):

        cursor = self.conexao.cursor()

        cursor.execute("""
            UPDATE obreiros
            SET ativo = 1
            WHERE id = ?
        """, (
            id,
        ))

        self.conexao.commit()

    # ==================================================
    # SANTA CEIA
    # ==================================================

    def adicionar_santa_ceia(
        self,
        data,
        obreiros_ids
    ):

        cursor = self.conexao.cursor()

        try:

            # ------------------------------------------
            # Cria a Santa Ceia
            # ------------------------------------------

            cursor.execute("""
                INSERT INTO santa_ceias (
                    data
                )
                VALUES (?)
            """, (
                data,
            ))

            santa_ceia_id = cursor.lastrowid

            # ------------------------------------------
            # Adiciona os obreiros participantes
            # ------------------------------------------

            for obreiro_id in obreiros_ids:

                cursor.execute("""
                    INSERT INTO santa_ceia_obreiros (
                        santa_ceia_id,
                        obreiro_id
                    )
                    VALUES (?, ?)
                """, (
                    santa_ceia_id,
                    obreiro_id
                ))

            self.conexao.commit()

            return santa_ceia_id

        except Exception:

            self.conexao.rollback()

            raise

    # ==================================================
    # LISTAR SANTA CEIAS
    # ==================================================

    def listar_santa_ceias(self):

        cursor = self.conexao.cursor()

        cursor.execute("""
            SELECT
                sc.id,
                sc.data,

                GROUP_CONCAT(
                    o.nome,
                    ', '
                ) AS obreiros

            FROM santa_ceias sc

            LEFT JOIN santa_ceia_obreiros sco
                ON sco.santa_ceia_id = sc.id

            LEFT JOIN obreiros o
                ON o.id = sco.obreiro_id

            GROUP BY sc.id

            ORDER BY sc.data
        """)

        return cursor.fetchall()

    # ==================================================
    # BUSCAR SANTA CEIA
    # ==================================================

    def buscar_santa_ceia(
        self,
        santa_ceia_id
    ):

        cursor = self.conexao.cursor()

        cursor.execute("""
            SELECT
                sc.id,
                sc.data,
                o.id AS obreiro_id,
                o.nome AS obreiro_nome

            FROM santa_ceias sc

            INNER JOIN santa_ceia_obreiros sco
                ON sco.santa_ceia_id = sc.id

            INNER JOIN obreiros o
                ON o.id = sco.obreiro_id

            WHERE sc.id = ?

            ORDER BY o.nome
        """, (
            santa_ceia_id,
        ))

        return cursor.fetchall()

    # ==================================================
    # ATUALIZAR SANTA CEIA
    # ==================================================

    def atualizar_santa_ceia(
        self,
        santa_ceia_id,
        data,
        obreiros_ids
    ):

        cursor = self.conexao.cursor()

        try:

            santa_ceia_id = int(
                santa_ceia_id
            )

            # ------------------------------------------
            # Atualiza a data
            # ------------------------------------------

            cursor.execute("""
                UPDATE santa_ceias
                SET data = ?
                WHERE id = ?
            """, (
                str(data),
                santa_ceia_id
            ))

            # ------------------------------------------
            # Remove participantes antigos
            # ------------------------------------------

            cursor.execute("""
                DELETE FROM santa_ceia_obreiros
                WHERE santa_ceia_id = ?
            """, (
                santa_ceia_id,
            ))

            # ------------------------------------------
            # Adiciona os novos participantes
            # ------------------------------------------

            for obreiro_id in obreiros_ids:

                obreiro_id = int(
                    obreiro_id
                )

                cursor.execute("""
                    INSERT INTO santa_ceia_obreiros (
                        santa_ceia_id,
                        obreiro_id
                    )
                    VALUES (?, ?)
                """, (
                    santa_ceia_id,
                    obreiro_id
                ))

            self.conexao.commit()

        except Exception:

            self.conexao.rollback()

            raise

    # ==================================================
    # EXCLUIR SANTA CEIA
    # ==================================================

    def excluir_santa_ceia(
        self,
        santa_ceia_id
    ):

        cursor = self.conexao.cursor()

        # Remove os obreiros vinculados
        cursor.execute("""
            DELETE FROM santa_ceia_obreiros
            WHERE santa_ceia_id = ?
        """, (
            santa_ceia_id,
        ))

        # Remove a Santa Ceia
        cursor.execute("""
            DELETE FROM santa_ceias
            WHERE id = ?
        """, (
            santa_ceia_id,
        ))

        self.conexao.commit()

    # ==================================================
    # FECHAR BANCO
    # ==================================================

    def fechar(self):

        if self.conexao:

            self.conexao.close()