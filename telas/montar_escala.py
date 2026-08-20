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
    QHeaderView,
    QFrame,
    QSpinBox
)

from PyQt6.QtCore import QDate, Qt

from database import Banco

from style import (
    COR_AZUL,
    COR_AZUL_ESCURO,
    COR_VERDE
)


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

        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_principal.setSpacing(0)

        # ==================================================
        # BARRA AZUL SUPERIOR
        # ==================================================

        barra_superior = QFrame()

        barra_superior.setFixedHeight(65)

        barra_superior.setStyleSheet(f"""
            QFrame {{
                background-color: {COR_AZUL};
            }}
        """)

        layout_barra = QHBoxLayout()

        layout_barra.setContentsMargins(
            20,
            0,
            20,
            0
        )

        barra_superior.setLayout(
            layout_barra
        )

        titulo_barra = QLabel(
            "MONTAR ESCALA DA SANTA CEIA"
        )

        titulo_barra.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 21px;
                font-weight: bold;
            }
        """)

        layout_barra.addWidget(
            titulo_barra
        )

        layout_barra.addStretch()

        sistema = QLabel(
            "Escala Santa Ceia"
        )

        sistema.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 13px;
            }
        """)

        layout_barra.addWidget(
            sistema
        )

        layout_principal.addWidget(
            barra_superior
        )

        # ==================================================
        # ÁREA CENTRAL
        # ==================================================

        area_central = QWidget()

        layout_central = QVBoxLayout()

        layout_central.setContentsMargins(
            30,
            20,
            30,
            20
        )

        layout_central.setSpacing(12)

        area_central.setLayout(
            layout_central
        )

        # ==================================================
        # DATA
        # ==================================================

        layout_data = QHBoxLayout()

        label_data = QLabel(
            "Data da Santa Ceia:"
        )

        label_data.setStyleSheet(f"""
            QLabel {{
                color: {COR_AZUL_ESCURO};
                font-size: 15px;
                font-weight: bold;
            }}
        """)

        self.data_santa_ceia = QDateEdit()

        self.data_santa_ceia.setCalendarPopup(
            True
        )

        self.data_santa_ceia.setDisplayFormat(
            "dd/MM/yyyy"
        )

        self.data_santa_ceia.setMinimumWidth(
            140
        )

        self.data_santa_ceia.setFixedHeight(
            35
        )

        # ==================================================
        # DATA INICIAL
        # ==================================================

        data_inicial = QDate(
            2000,
            1,
            1
        )

        self.data_santa_ceia.setMinimumDate(
            data_inicial
        )

        self.data_santa_ceia.setDate(
            data_inicial
        )

        self.data_santa_ceia.setSpecialValueText(
            "Selecione..."
        )

        # ==================================================
        # ESTILO DO CAMPO DE DATA
        # ==================================================

        self.data_santa_ceia.setStyleSheet(f"""
            QDateEdit {{
                background-color: white;
                color: #1f2937;
                border: 1px solid #b0bec5;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 14px;
                min-width: 140px;
            }}

            QDateEdit:hover {{
                border: 2px solid {COR_AZUL};
            }}

            QDateEdit:focus {{
                border: 2px solid {COR_AZUL};
            }}

            QDateEdit::drop-down {{
                width: 32px;
                border-left: 1px solid #b0bec5;
                background-color: {COR_AZUL};
            }}

            QCalendarWidget {{
                background-color: white;
            }}

            QCalendarWidget QWidget {{
                background-color: white;
            }}

            /*
            IMPORTANTE:
            Não estamos mais estilizando todos os
            QToolButton do calendário.
            Isso evita interferência nas setas
            de alteração do mês e do ano.
            */

            QCalendarWidget QAbstractItemView {{
                background-color: white;
                color: #1f2937;
                selection-background-color: {COR_AZUL};
                selection-color: white;
                outline: none;
            }}
        """)
        
        self.configurar_calendario()

        layout_data.addWidget(
            label_data
        )

        layout_data.addWidget(
            self.data_santa_ceia
        )

        layout_data.addStretch()

        layout_central.addLayout(
            layout_data
        )

        # ==================================================
        # OBREIROS
        # ==================================================

        label_obreiros = QLabel(
            "Selecione os obreiros participantes:"
        )

        label_obreiros.setStyleSheet(f"""
            QLabel {{
                color: {COR_AZUL_ESCURO};
                font-size: 16px;
                font-weight: bold;
                padding-top: 8px;
            }}
        """)

        layout_central.addWidget(
            label_obreiros
        )

        self.lista_obreiros = QListWidget()

        self.lista_obreiros.setMinimumHeight(
            180
        )

        layout_central.addWidget(
            self.lista_obreiros
        )

        # ==================================================
        # BOTÕES DE SELEÇÃO
        # ==================================================

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

        layout_central.addLayout(
            layout_selecao
        )

        # ==================================================
        # BOTÕES DA ESCALA
        # ==================================================

        layout_escala = QHBoxLayout()

        self.botao_adicionar = QPushButton(
            "Adicionar Escala"
        )

        self.botao_salvar_edicao = QPushButton(
            "Salvar Alterações"
        )

        self.botao_excluir = QPushButton(
            "Excluir Escala Selecionada"
        )

        self.botao_salvar_edicao.setEnabled(
            False
        )

        self.botao_adicionar.clicked.connect(
            self.adicionar_escala
        )

        self.botao_salvar_edicao.clicked.connect(
            self.salvar_edicao
        )

        self.botao_excluir.clicked.connect(
            self.excluir_escala
        )

        estilo_botao = f"""
            QPushButton {{
                background-color: {COR_AZUL};
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 16px;
                font-weight: bold;
            }}

            QPushButton:hover {{
                background-color: {COR_AZUL_ESCURO};
            }}

            QPushButton:pressed {{
                background-color: {COR_VERDE};
            }}

            QPushButton:disabled {{
                background-color: #b0bec5;
                color: #eeeeee;
            }}
        """

        self.botao_adicionar.setStyleSheet(
            estilo_botao
        )

        self.botao_salvar_edicao.setStyleSheet(
            estilo_botao
        )

        self.botao_excluir.setStyleSheet(
            estilo_botao
        )

        layout_escala.addWidget(
            self.botao_adicionar
        )

        layout_escala.addWidget(
            self.botao_salvar_edicao
        )

        layout_escala.addWidget(
            self.botao_excluir
        )

        layout_central.addLayout(
            layout_escala
        )

        # ==================================================
        # ESCALAS CADASTRADAS
        # ==================================================

        label_escalas = QLabel(
            "Escalas cadastradas:"
        )

        label_escalas.setStyleSheet(f"""
            QLabel {{
                color: {COR_AZUL_ESCURO};
                font-size: 16px;
                font-weight: bold;
                padding-top: 8px;
            }}
        """)

        layout_central.addWidget(
            label_escalas
        )

        self.tabela = QTableWidget()

        self.tabela.setColumnCount(
            3
        )

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

        layout_central.addWidget(
            self.tabela
        )

        layout_principal.addWidget(
            area_central
        )

        # ==================================================
        # BARRA VERDE INFERIOR
        # ==================================================

        barra_inferior = QFrame()

        barra_inferior.setFixedHeight(
            40
        )

        barra_inferior.setStyleSheet(f"""
            QFrame {{
                background-color: {COR_VERDE};
            }}
        """)

        layout_rodape = QHBoxLayout()

        layout_rodape.setContentsMargins(
            20,
            0,
            20,
            0
        )

        barra_inferior.setLayout(
            layout_rodape
        )

        rodape = QLabel(
            "Montagem e gerenciamento das escalas"
        )

        rodape.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;
            }
        """)

        layout_rodape.addWidget(
            rodape
        )

        layout_rodape.addStretch()

        sistema = QLabel(
            "Escala Santa Ceia"
        )

        sistema.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12px;
            }
        """)

        layout_rodape.addWidget(
            sistema
        )

        layout_principal.addWidget(
            barra_inferior
        )

        self.setLayout(
            layout_principal
        )
        
    # ==================================================
    # CONFIGURAR CALENDÁRIO
    # ==================================================

    def configurar_calendario(self):

        calendario = self.data_santa_ceia.calendarWidget()

        # ==================================================
        # ESTILO DO CALENDÁRIO
        # ==================================================

        calendario.setStyleSheet(f"""
            QCalendarWidget {{
                background-color: white;
            }}

            QCalendarWidget QWidget {{
                background-color: white;
            }}

            QCalendarWidget QToolButton {{
                color: white;
                background-color: {COR_AZUL};
                font-size: 14px;
                font-weight: bold;
                border: none;
                padding: 6px;
            }}

            QCalendarWidget QToolButton:hover {{
                background-color: {COR_AZUL_ESCURO};
            }}

            QCalendarWidget QSpinBox {{
                color: white;
                background-color: {COR_AZUL};
                font-size: 14px;
                font-weight: bold;
                border: none;
            }}

            QCalendarWidget QAbstractItemView {{
                background-color: white;
                color: #1f2937;
                selection-background-color: {COR_AZUL};
                selection-color: white;
                outline: none;
            }}
        """)

        # ==================================================
        # CONFIGURAR CAMPO DO ANO
        # ==================================================

        spinboxes = calendario.findChildren(QSpinBox)

        for spinbox in spinboxes:

            # Limite de anos
            spinbox.setMinimum(2000)
            spinbox.setMaximum(2100)

            # Garante que as setas padrão estejam disponíveis
            spinbox.setButtonSymbols(
                QSpinBox.ButtonSymbols.UpDownArrows
            )

            # Permite digitar o ano
            spinbox.setKeyboardTracking(True)

            # Mantém o controle habilitado
            spinbox.setEnabled(True)

            # Garante que possa receber foco
            spinbox.setFocusPolicy(
                Qt.FocusPolicy.StrongFocus
            )
    

    # ==================================================
    # CARREGAR OBREIROS
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
    # PEGAR OBREIROS SELECIONADOS
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

                if obreiro_id is not None:
                    obreiros_ids.append(
                        int(obreiro_id)
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

    # ==================================================
    # SELECIONAR ESCALA
    # ==================================================

    def selecionar_escala(
        self,
        linha,
        coluna
    ):

        escala_id = int(
            self.tabela.item(
                linha,
                0
            ).text()
        )

        escalas = self.banco.buscar_santa_ceia(
            escala_id
        )

        if not escalas:
            return

        self.escala_editando_id = escala_id

        # ----------------------------------------------
        # DATA
        # ----------------------------------------------

        data = QDate.fromString(
            escalas[0]["data"],
            "yyyy-MM-dd"
        )

        self.data_santa_ceia.setDate(
            data
        )

        # ----------------------------------------------
        # OBREIROS PARTICIPANTES
        # ----------------------------------------------

        obreiros_selecionados = {
            escala["obreiro_id"]
            for escala in escalas
        }

        for i in range(
            self.lista_obreiros.count()
        ):

            item = self.lista_obreiros.item(i)

            obreiro_id = item.data(
                Qt.ItemDataRole.UserRole
            )

            if obreiro_id in obreiros_selecionados:

                item.setCheckState(
                    Qt.CheckState.Checked
                )

            else:

                item.setCheckState(
                    Qt.CheckState.Unchecked
                )

        # ----------------------------------------------
        # BOTÕES
        # ----------------------------------------------

        self.botao_salvar_edicao.setEnabled(
            True
        )

        self.botao_adicionar.setEnabled(
            False
        )

    # ==================================================
    # SALVAR EDIÇÃO
    # ==================================================

    def salvar_edicao(self):

        if self.escala_editando_id is None:
            return

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

        try:

            self.banco.atualizar_santa_ceia(
                self.escala_editando_id,
                data,
                obreiros_ids
            )

            QMessageBox.information(
                self,
                "Sucesso",
                "Escala atualizada com sucesso!"
            )

            self.cancelar_edicao()

            self.carregar_escalas()

        except Exception as erro:

            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível atualizar a escala:\n\n{erro}"
            )

    # ==================================================
    # CANCELAR EDIÇÃO
    # ==================================================

    def cancelar_edicao(self):

        self.escala_editando_id = None

        self.desmarcar_todos()

        self.botao_salvar_edicao.setEnabled(
            False
        )

        self.botao_adicionar.setEnabled(
            True
        )