COR_AZUL = "#1976D2"

COR_AZUL_ESCURO = "#0D47A1"

COR_VERDE = "#2E7D32"

COR_VERDE_CLARO = "#43A047"

COR_FUNDO = "#f4f6f8"

ESTILO_GERAL = """

QWidget {
background-color: #f4f6f8;
font-family: Arial;
font-size: 14px;
}

QMainWindow {
background-color: #f4f6f8;
}

QLabel {
color: #1f2937;
}

/* ==============================
BOTÕES
============================== */

QPushButton {
background-color: #1976D2;
color: white;
border: none;
border-radius: 6px;
padding: 10px 18px;
font-weight: bold;
}

QPushButton:hover {
background-color: #1565C0;
}

QPushButton:pressed {
background-color: #0D47A1;
}

/* ==============================
CAMPOS DE TEXTO
============================== */

QLineEdit {
background-color: white;
color: #1f2937;
border: 1px solid #b0bec5;
border-radius: 5px;
padding: 7px;
}

QLineEdit:focus {
border: 2px solid #1976D2;
color: #1f2937;
}

/* ==============================
COMBOBOX
============================== */

QComboBox {
background-color: white;
color: #1f2937;
border: 1px solid #b0bec5;
border-radius: 5px;
padding: 7px;
}

QComboBox:focus {
border: 2px solid #1976D2;
color: #1f2937;
}

QComboBox QAbstractItemView {
background-color: white;
color: #1f2937;
selection-background-color: #1976D2;
selection-color: white;
}

/* ==============================
DATA E NÚMEROS
============================== */

QDateEdit {
background-color: white;
color: #1f2937;
border: 1px solid #b0bec5;
border-radius: 5px;
padding: 7px;
}

QDateEdit:focus {
border: 2px solid #1976D2;
color: #1f2937;
}

QSpinBox {
background-color: white;
color: #1f2937;
border: 1px solid #b0bec5;
border-radius: 5px;
padding: 7px;
}

QSpinBox:focus {
border: 2px solid #1976D2;
color: #1f2937;
}

/* ==============================
TABELAS
============================== */

QTableWidget {
background-color: white;
color: #1f2937;
border: 1px solid #b0bec5;
gridline-color: #d0d7de;
}

QTableWidget::item {
color: #1f2937;
}

QTableWidget::item:selected {
background-color: #1976D2;
color: white;
}

QHeaderView::section {
background-color: #1976D2;
color: white;
padding: 8px;
font-weight: bold;
border: none;
}

/* ==============================
TEXTOS MULTILINHA
============================== */

QTextEdit,
QPlainTextEdit {
background-color: white;
color: #1f2937;
border: 1px solid #b0bec5;
border-radius: 5px;
padding: 7px;
}

QTextEdit:focus,
QPlainTextEdit:focus {
border: 2px solid #1976D2;
color: #1f2937;
}

"""
