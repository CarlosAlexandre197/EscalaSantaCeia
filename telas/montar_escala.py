from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QDateEdit,
    QListWidget,
    QListWidgetItem,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView
)

from PyQt6.QtCore import QDate, Qt

from database import Banco


class TelaMontarEscala(QWidget):

    def __init__(self):
        super().__init__()

        self.banco = Banco()
        self.escala_editando_id = None

        self.setWindowTitle("Montar Escala - Santa Ceia")
        self.resize(900, 650)

        self.criar_interface()
        self.carregar_obreiros()
        self.carregar_escalas()

    # ==================================================
    # INTERFACE
    # ==================================================

    def criar_interface(self):

        layout_principal = QVBoxLayout()

        # ----------------------------------------------
        # TÍTULO
        # ----------------------------------------------

        titulo = QLabel(
            "Montar Escala da Santa Ceia"
        )

        titulo.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                padding: 15px;
            }
        """)

        titulo.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout_principal.addWidget(titulo)

        # ----------------------------------------------
        # DATA
        # ----------------------------------------------

        layout_data = QHBoxLayout()

        label_data = QLabel(
            "Data da Santa Ceia:"
        )

        self.data_santa_ceia = QDateEdit()

        self.data_santa_ceia.setCalendarPopup(
            True
        )

        self.data_santa_ceia.setDisplayFormat(
            "dd/MM/yyyy"
        )

        self.data_santa_ceia.setDate(
            QDate.currentDate()
        )

        layout_data.addWidget(
            label_data
        )

        layout_data.addWidget(
            self.data_santa_ceia
        )

        layout_data.addStretch()

        layout_principal.addLayout(
            layout_data
        )

        # ----------------------------------------------
        # OBRIEIROS
        # ----------------------------------------------

        label_obreiros = QLabel(
            "Selecione os obreiros participantes:"
        )

        label_obreiros.setStyleSheet("""
            QLabel {
                font-weight: bold;
                padding-top: 10px;
            }
        """)

        layout_principal.addWidget(
            label_obreiros
        )

        self.lista_obreiros = QListWidget()

        self.lista_obreiros.setMinimumHeight(
            180
        )

        layout_principal.addWidget(
            self.lista_obreiros
        )

        # ----------------------------------------------
        # BOTÕES DE SELEÇÃO
        # ----------------------------------------------

        layout_selecao = QHBoxLayout()

        self.botao_selecionar_todos = QPushButton(
            "Selecionar Todos"
        )

        self.botao_desmarcar_todos = QPushButton(
            "Desmarcar Todos"
        )

        self.botao_selecionar_todos.clicked.connect(
            self.selecionar_todos
        )

        self.botao_desmarcar_todos.clicked.connect(
            self.desmarcar_todos
        )

        layout_selecao.addWidget(
            self.botao_selecionar_todos
        )

        layout_selecao.addWidget(
            self.botao_desmarcar_todos
        )

        layout_selecao.addStretch()

        layout_principal.addLayout(
            layout_selecao
        )

        # ----------------------------------------------
        # ADICIONAR ESCALA
        # ----------------------------------------------

        self.botao_adicionar = QPushButton(
            "Adicionar Escala"
        )
        
        self.botao_salvar_edicao = QPushButton(
            "Salvar Alterações"
        )

        self.botao_salvar_edicao.setEnabled(
            False
        )

        self.botao_salvar_edicao.clicked.connect(
            self.salvar_edicao
        )

        self.botao_adicionar.setStyleSheet("""
            QPushButton {
                padding: 10px;
                font-weight: bold;
            }
        """)

        self.botao_adicionar.clicked.connect(
            self.adicionar_escala
        )

        layout_principal.addWidget(
            self.botao_adicionar
        )
        
        layout_principal.addWidget(
            self.botao_salvar_edicao
        )

        # ----------------------------------------------
        # ESCALAS CADASTRADAS
        # ----------------------------------------------

        label_escalas = QLabel(
            "Escalas cadastradas:"
        )

        label_escalas.setStyleSheet("""
            QLabel {
                font-weight: bold;
                padding-top: 15px;
            }
        """)

        layout_principal.addWidget(
            label_escalas
        )

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(3)

        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Data",
            "Obreiros"
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
            self.selecionar_escala
        )

        layout_principal.addWidget(
            self.tabela
        )

        # ----------------------------------------------
        # EXCLUIR ESCALA
        # ----------------------------------------------

        self.botao_excluir = QPushButton(
            "Excluir Escala Selecionada"
        )

        self.botao_excluir.clicked.connect(
            self.excluir_escala
        )

        layout_principal.addWidget(
            self.botao_excluir
        )

        self.setLayout(
            layout_principal
        )

    # ==================================================
    # CARREGAR OBRIEIROS
    # ==================================================

    def carregar_obreiros(self):

        self.lista_obreiros.clear()

        obreiros = self.banco.listar_obreiros()

        for obreiro in obreiros:

            item = QListWidgetItem(
                obreiro["nome"]
            )

            item.setData(
                Qt.ItemDataRole.UserRole,
                obreiro["id"]
            )

            item.setFlags(
                item.flags()
                | Qt.ItemFlag.ItemIsUserCheckable
            )

            item.setCheckState(
                Qt.CheckState.Unchecked
            )

            self.lista_obreiros.addItem(
                item
            )

    # ==================================================
    # SELECIONAR TODOS
    # ==================================================

    def selecionar_todos(self):

        for i in range(
            self.lista_obreiros.count()
        ):

            item = self.lista_obreiros.item(i)

            item.setCheckState(
                Qt.CheckState.Checked
            )

    # ==================================================
    # DESMARCAR TODOS
    # ==================================================

    def desmarcar_todos(self):

        for i in range(
            self.lista_obreiros.count()
        ):

            item = self.lista_obreiros.item(i)

            item.setCheckState(
                Qt.CheckState.Unchecked
            )

    # ==================================================
    # PEGAR OBRIEIROS SELECIONADOS
    # ==================================================

    def obter_obreiros_selecionados(self):

        obreiros_ids = []

        for i in range(
            self.lista_obreiros.count()
        ):

            item = self.lista_obreiros.item(i)

            if item.checkState() == (
                Qt.CheckState.Checked
            ):

                obreiro_id = item.data(
                    Qt.ItemDataRole.UserRole
                )

                obreiros_ids.append(
                    obreiro_id
                )

        return obreiros_ids

    # ==================================================
    # ADICIONAR ESCALA
    # ==================================================

    def adicionar_escala(self):

        obreiros_ids = (
            self.obter_obreiros_selecionados()
        )

        if not obreiros_ids:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione pelo menos um obreiro."
            )

            return

        data = (
            self.data_santa_ceia
            .date()
            .toString("yyyy-MM-dd")
        )

        # ----------------------------------------------
        # VERIFICAR DATA DUPLICADA
        # ----------------------------------------------

        escalas = (
            self.banco.listar_santa_ceias()
        )

        for escala in escalas:

            if escala["data"] == data:

                QMessageBox.warning(
                    self,
                    "Atenção",
                    "Já existe uma escala cadastrada "
                    "para esta data."
                )

                return

        # ----------------------------------------------
        # SALVAR
        # ----------------------------------------------

        try:

            self.banco.adicionar_santa_ceia(
                data,
                obreiros_ids
            )

            QMessageBox.information(
                self,
                "Sucesso",
                "Escala da Santa Ceia adicionada "
                "com sucesso!"
            )

            self.desmarcar_todos()

            self.carregar_escalas()

        except Exception as erro:

            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível salvar a escala:\n\n{erro}"
            )

    # ==================================================
    # CARREGAR ESCALAS
    # ==================================================

    def carregar_escalas(self):

        escalas = (
            self.banco.listar_santa_ceias()
        )

        self.tabela.setRowCount(0)

        for escala in escalas:

            linha = self.tabela.rowCount()

            self.tabela.insertRow(
                linha
            )

            data = QDate.fromString(
                escala["data"],
                "yyyy-MM-dd"
            )

            data_formatada = data.toString(
                "dd/MM/yyyy"
            )

            self.tabela.setItem(
                linha,
                0,
                QTableWidgetItem(
                    str(escala["id"])
                )
            )

            self.tabela.setItem(
                linha,
                1,
                QTableWidgetItem(
                    data_formatada
                )
            )

            self.tabela.setItem(
                linha,
                2,
                QTableWidgetItem(
                    escala["obreiros"] or ""
                )
            )

    # ==================================================
    # EXCLUIR ESCALA
    # ==================================================

    def excluir_escala(self):

        linha = self.tabela.currentRow()

        if linha < 0:

            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma escala."
            )

            return

        id_escala = int(
            self.tabela.item(
                linha,
                0
            ).text()
        )

        resposta = QMessageBox.question(
            self,
            "Confirmar exclusão",
            "Deseja realmente excluir esta escala?"
        )

        if resposta == (
            QMessageBox.StandardButton.Yes
        ):

            self.banco.excluir_santa_ceia(
                id_escala
            )

            self.carregar_escalas()

    # ==================================================
    # FECHAR
    # ==================================================

    def closeEvent(
        self,
        event
    ):

        self.banco.fechar()

        event.accept()