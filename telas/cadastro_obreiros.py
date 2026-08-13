from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView
)

from database import Banco


class TelaCadastroObreiros(QWidget):

    def __init__(self):
        super().__init__()

        self.banco = Banco()

        self.setWindowTitle("Cadastro de Obreiros")
        self.resize(700, 500)

        self.criar_interface()
        self.carregar_obreiros()

    def criar_interface(self):

        layout_principal = QVBoxLayout()

        # Título
        titulo = QLabel("Cadastro de Obreiros")
        titulo.setStyleSheet("""
            QLabel {
                font-size: 22px;
                font-weight: bold;
                padding: 10px;
            }
        """)

        layout_principal.addWidget(titulo)

        # Nome
        layout_nome = QHBoxLayout()

        label_nome = QLabel("Nome:")
        self.input_nome = QLineEdit()
        self.input_nome.setPlaceholderText("Digite o nome do obreiro")

        layout_nome.addWidget(label_nome)
        layout_nome.addWidget(self.input_nome)

        layout_principal.addLayout(layout_nome)

        # Telefone
        layout_telefone = QHBoxLayout()

        label_telefone = QLabel("Telefone:")
        self.input_telefone = QLineEdit()
        self.input_telefone.setPlaceholderText("Digite o telefone")

        layout_telefone.addWidget(label_telefone)
        layout_telefone.addWidget(self.input_telefone)

        layout_principal.addLayout(layout_telefone)

        # Botões
        layout_botoes = QHBoxLayout()

        self.botao_adicionar = QPushButton("Adicionar")
        self.botao_editar = QPushButton("Editar")
        self.botao_desativar = QPushButton("Desativar")
        self.botao_limpar = QPushButton("Limpar")

        self.botao_adicionar.clicked.connect(
            self.adicionar_obreiro
        )

        self.botao_editar.clicked.connect(
            self.editar_obreiro
        )

        self.botao_desativar.clicked.connect(
            self.desativar_obreiro
        )

        self.botao_limpar.clicked.connect(
            self.limpar_campos
        )

        layout_botoes.addWidget(self.botao_adicionar)
        layout_botoes.addWidget(self.botao_editar)
        layout_botoes.addWidget(self.botao_desativar)
        layout_botoes.addWidget(self.botao_limpar)

        layout_principal.addLayout(layout_botoes)

        # Tabela
        self.tabela = QTableWidget()

        self.tabela.setColumnCount(3)

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Nome",
            "Telefone"
        ])

        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.tabela.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.tabela.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )

        self.tabela.cellClicked.connect(
            self.selecionar_obreiro
        )

        layout_principal.addWidget(self.tabela)

        self.setLayout(layout_principal)

    # =========================
    # CARREGAR OBRIEIROS
    # =========================

    def carregar_obreiros(self):

        obreiros = self.banco.listar_obreiros()

        self.tabela.setRowCount(0)

        for obreiro in obreiros:

            linha = self.tabela.rowCount()

            self.tabela.insertRow(linha)

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(str(obreiro["id"]))
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(obreiro["nome"])
            )

            self.tabela.setItem(
                linha,
                2,
                QTableWidgetItem(obreiro["telefone"] or "")
            )

    # =========================
    # ADICIONAR
    # =========================

    def adicionar_obreiro(self):

        nome = self.input_nome.text().strip()
        telefone = self.input_telefone.text().strip()

        if not nome:

            QMessageBox.warning(
                self,
                "Atenção",
                "Digite o nome do obreiro."
            )

            return

        self.banco.adicionar_obreiro(
            nome,
            telefone
        )

        QMessageBox.information(
            self,
            "Sucesso",
            "Obreiro cadastrado com sucesso!"
        )

        self.limpar_campos()
        self.carregar_obreiros()

    # =========================
    # SELECIONAR
    # =========================

    def selecionar_obreiro(self, linha, coluna):

        id_obreiro = int(
            self.tabela.item(linha, 0).text()
        )

        obreiro = self.banco.buscar_obreiro(
            id_obreiro
        )

        if obreiro:

            self.input_nome.setText(
                obreiro["nome"]
            )

            self.input_telefone.setText(
                obreiro["telefone"] or ""
            )

    # =========================
    # EDITAR
    # =========================

    def editar_obreiro(self):

        linha = self.tabela.currentRow()

        if linha < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um obreiro."
            )

            return

        id_obreiro = int(
            self.tabela.item(linha, 0).text()
        )

        nome = self.input_nome.text().strip()
        telefone = self.input_telefone.text().strip()

        if not nome:

            QMessageBox.warning(
                self,
                "Atenção",
                "Digite o nome do obreiro."
            )

            return

        self.banco.atualizar_obreiro(
            id_obreiro,
            nome,
            telefone
        )

        QMessageBox.information(
            self,
            "Sucesso",
            "Obreiro atualizado com sucesso!"
        )

        self.limpar_campos()
        self.carregar_obreiros()

    # =========================
    # DESATIVAR
    # =========================

    def desativar_obreiro(self):

        linha = self.tabela.currentRow()

        if linha < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione um obreiro."
            )

            return

        id_obreiro = int(
            self.tabela.item(linha, 0).text()
        )

        resposta = QMessageBox.question(
            self,
            "Confirmar",
            "Deseja desativar este obreiro?"
        )

        if resposta == QMessageBox.StandardButton.Yes:

            self.banco.desativar_obreiro(
                id_obreiro
            )

            self.limpar_campos()
            self.carregar_obreiros()

    # =========================
    # LIMPAR
    # =========================

    def limpar_campos(self):

        self.input_nome.clear()
        self.input_telefone.clear()

        self.tabela.clearSelection()

    # =========================
    # FECHAR
    # =========================

    def closeEvent(self, event):

        self.banco.fechar()

        event.accept()