---
title: Criando um PDF complexo
linktitle: Criando um PDF complexo
type: docs
weight: 30
url: /python-net/complex-pdf-example/
description: Aspose.PDF para Python via .NET permite que você crie documentos mais complexos que contêm imagens, fragmentos de texto e tabelas em um único documento.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

O exemplo [Hello, World](/pdf/python-net/hello-world-example/) mostrou passos simples para criar um documento PDF usando Python e Aspose.PDF. Neste artigo, vamos dar uma olhada em como criar um documento mais complexo com o Aspose.PDF para Python. Como exemplo, pegaremos um documento de uma empresa fictícia que opera serviços de ferry para passageiros. Nosso documento conterá uma imagem, dois fragmentos de texto (cabeçalho e parágrafo) e uma tabela.

Se criarmos um documento do zero, precisamos seguir certas etapas:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Neste passo, criaremos um documento PDF vazio com alguns metadados, mas sem páginas.
1. Adicionar uma [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ao objeto do documento. Assim, nosso documento terá uma página.
1. Adicionar uma [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) à Página.
1. Criar um [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para o cabeçalho. Para o cabeçalho, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento centralizado.
1. Adicionar o cabeçalho aos [parágrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página.
1. Criar um [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para a descrição. Para a descrição, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento centralizado.
1. Adicionar a (descrição) aos Parágrafos da página.
1. Criar uma tabela, adicionar propriedades à tabela.

1. Adicione (tabela) à página [parágrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Salve um documento "Complex.pdf".

```python

    import aspose.pdf as ap

    # Inicializar objeto de documento
    document = ap.Document()
    # Adicionar página
    page = document.pages.add()

    # Adicionar imagem
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # Adicionar Cabeçalho
    header = ap.text.TextFragment("Novas rotas de ferry no outono de 2020")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Adicionar descrição
    descriptionText = "Os visitantes devem comprar ingressos online e os ingressos são limitados a 5.000 por dia. \
    O serviço de ferry está operando com metade da capacidade e em um horário reduzido. Espere filas."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Adicionar tabela
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Sai da Cidade")
    headerRow.cells.add("Sai da Ilha")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(output_pdf)
```