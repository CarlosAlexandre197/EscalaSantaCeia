from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


def gerar_pdf(
    caminho,
    data,
    obreiros
):

    documento = SimpleDocTemplate(
        caminho,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm
    )

    estilos = getSampleStyleSheet()

    estilo_titulo = ParagraphStyle(
        "Titulo",
        parent=estilos["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        spaceAfter=8
    )

    estilo_subtitulo = ParagraphStyle(
        "Subtitulo",
        parent=estilos["Normal"],
        alignment=TA_CENTER,
        fontSize=14,
        spaceAfter=20
    )

    estilo_normal = ParagraphStyle(
        "NormalPersonalizado",
        parent=estilos["Normal"],
        fontSize=11
    )

    elementos = []

    # ==============================================
    # CABEÇALHO
    # ==============================================

    elementos.append(
        Paragraph(
            "ADSAM 317 Ministério Madureira",
            estilo_titulo
        )
    )

    elementos.append(
        Paragraph(
            "ESCALA DA SANTA CEIA",
            estilo_subtitulo
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Data:</b> {data}",
            estilo_normal
        )
    )

    elementos.append(
        Spacer(1, 20)
    )

    # ==============================================
    # TABELA
    # ==============================================

    dados = [
        [
            "Nº",
            "Obreiro"
        ]
    ]

    for numero, obreiro in enumerate(
        obreiros,
        start=1
    ):

        dados.append(
            [
                str(numero),
                obreiro
            ]
        )

    tabela = Table(
        dados,
        colWidths=[
            2 * cm,
            14 * cm
        ]
    )

    tabela.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#1976D2")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                "Helvetica-Bold"
            ),
            (
                "ALIGN",
                (0, 0),
                (0, -1),
                "CENTER"
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "FONTNAME",
                (0, 1),
                (-1, -1),
                "Helvetica"
            ),
            (
                "FONTSIZE",
                (0, 0),
                (-1, -1),
                11
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                8
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                8
            )
        ])
    )

    elementos.append(
        tabela
    )

    elementos.append(
        Spacer(1, 40)
    )

    elementos.append(
        Paragraph(
            "Escala Santa Ceia",
            estilo_normal
        )
    )

    elementos.append(
        Spacer(1, 30)
    )

    elementos.append(
        Paragraph(
            "Carlos Alexandre",
            estilo_normal
        )
    )

    # ==============================================
    # GERAR
    # ==============================================

    documento.build(
        elementos
    )