---
title: Adicionar Tabelas ao PDF usando Python
linktitle: Adicionar Tabelas
type: docs
weight: 10
url: /pt/python-net/adding-tables/
description: Aspose.PDF for Python via .NET é uma biblioteca usada para criar, ler e editar Tabelas PDF. Confira outras funções avançadas neste tópico.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar Tabela em PDF usando Python
Abstract: Este artigo fornece um guia abrangente para criar e manipular tabelas em documentos PDF usando a biblioteca Aspose.PDF for Python via .NET. Ele detalha os passos para adicionar tabelas a arquivos PDF existentes, incluindo a configuração de bordas de tabela, margens e preenchimento. Além disso, explora funcionalidades avançadas como mesclar colunas e linhas usando `col_span` e `row_span`, aplicar diferentes configurações de AutoFit e recuperar dinamicamente a largura da tabela. O artigo também demonstra a inserção de imagens SVG em células de tabela e a aplicação de quebras de página ou a renderização de tabelas em novas páginas. Trechos de código ilustram cada funcionalidade, mostrando como gerenciar eficazmente o layout e o conteúdo de tabelas em documentos PDF.
---

Adicionar tabelas a documentos PDF existentes é uma necessidade comum para melhorar a apresentação de dados, estruturar informações ou gerar relatórios. **Aspose.PDF for Python via .NET** oferece uma solução abrangente para essa tarefa, permitindo que desenvolvedores insiram tabelas em PDFs existentes de forma perfeita.

Este guia fornece uma abordagem passo a passo para adicionar tabelas a documentos PDF existentes usando Aspose.PDF for Python via .NET. Ele cobre a inicialização de uma tabela, definição das larguras das colunas, definição de bordas, preenchimento de linhas e células, e salvamento do documento modificado. Além disso, o guia explora recursos avançados, como tratamento de bordas de células, aplicação de margens e preenchimento, e utilização das configurações de AutoFit para ajustar dinamicamente as dimensões da tabela.

Se você deseja melhorar o apelo visual dos seus PDFs ou organizar os dados de forma mais eficaz, este guia serve como um recurso valioso para aproveitar as poderosas capacidades de manipulação de tabelas do Aspose.PDF for Python.

## Criando Tabelas Básicas

## Criando Tabela

Este exemplo demonstra como criar uma Tabela em um documento PDF com bordas e várias linhas.

1. Crie um novo documento PDF.
1. Adiciona uma página em branco ao documento.
1. Inicialize a Tabela.
1. Defina a borda geral da tabela.
1. Defina a borda para células individuais.
1. Adicione Linhas e Células.
1. Insira a tabela na página.
1. Salve o PDF no caminho especificado.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")
    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save updated document containing table object
    document.save(path_outfile)
```

### Adicionando Imagens às Células da Tabela

Este trecho de código mostra como inserir imagens nas células da Tabela em um documento PDF.

1. Crie um novo documento PDF.
1. Inicialize a Tabela.
1. Defina as larguras das colunas em pontos.
1. Um fragmento de texto é adicionado à primeira célula.
1. Uma instância 'ap.Image()' é adicionada à segunda célula.
1. Defina o caminho para o arquivo de imagem com 'img.file'.
1. Os 'img.fix_width' e 'img.fix_height' controlam o tamanho da imagem dentro da célula.
1. Insira a Tabela na página PDF.
1. Salve o PDF.

```python

    import aspose.pdf as ap
    from os import path

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"

    # Create row object and add it to table instance
    row = table.rows.add()
    # Create cell object and add it to row instance
    cell = row.cells.add()
    # Add textfragment to paragraphs collection of cell object
    cell.paragraphs.add(ap.text.TextFragment(image))
    # Create an image instance
    img = ap.Image()
    # Set image type as SVG
    # Path for source file
    img.file = path.join(self.data_dir, image)
    # Set width for image instance
    img.fix_width = 50
    # Set height for image instance
    img.fix_height = 50
    # Add another cell to row object
    cell = row.cells.add()
    # Add SVG image to paragraphs collection of recently added cell instance
    cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(path_outfile)
```

Você pode adicionar imagens SVG em células de tabela em um documento PDF:

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"
    for image in images:
        # Create row object and add it to table instance
        row = table.rows.add()
        # Create cell object and add it to row instance
        cell = row.cells.add()
        # Add textfragment to paragraphs collection of cell object
        cell.paragraphs.add(ap.text.TextFragment(image))
        # Create an image instance
        img = ap.Image()
        # Set image type as SVG
        img.file_type = ap.ImageFileType.SVG
        # Path for source file
        img.file = path.join(self.data_dir, image)
        # Set width for image instance
        img.fix_width = 50
        # Set height for image instance
        img.fix_height = 50
        # Add another cell to row object
        cell = row.cells.add()
        # Add SVG image to paragraphs collection of recently added cell instance
        cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(path_outfile)
```

### ColSpan e RowSpan em Tabelas

Este exemplo mostra como mesclar células de tabela verticalmente e horizontalmente para criar layouts de tabela complexos.

1. Defina a borda geral da tabela.
1. Defina as bordas padrão das células.
1. Mescle duas células horizontalmente em uma.
1. Mescle a célula verticalmente através de duas linhas.
1. A linha 5 considera o rowspan ao pular a coluna mesclada.
1. Insira a tabela na página.
1. Salve o PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.black
    )
    # Add 1st row to table
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Add table cells
        row1.cells.add("Test 1" + str(cellCount))

    # Add 2nd row to table
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Add 3rd row to table
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Add 4th row to table
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Add 5th row to table
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

![Demonstração de ColSpan e RowSpan](colspan_rowspan.png)

### Aplicando Bordas a Tabelas e Células

Este exemplo mostra como definir o preenchimento de células, margens da tabela e controlar a quebra de linha para texto em células da tabela.

1. Defina as larguras das colunas.
1. Defina as bordas da tabela e das células.
1. Defina o preenchimento dentro das células para espaçamento consistente.
1. Aplique o preenchimento a todas as células por padrão.
1. Adicione texto e controle da quebra de linha.
1. Adicione linhas e células.
1. Salve o PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)
    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    tab1 = ap.Table()
    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(tab1)
    # Set with column widths of the table
    tab1.column_widths = "50 50 50"
    # Set default cell border using BorderInfo object
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Set table border using another customized BorderInfo object
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Set the default cell padding to the MarginInfo object
    tab1.default_cell_padding = margin
    # Create rows in the table and then cells in the rows
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    text = ap.text.TextFragment("col3 with large text string")
    # Row1.Cells.Add("col3 with large text string to be placed inside cell")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Save updated document containing table object
    document.save(path_outfile)
```

![Margem e borda em tabela PDF](margin-border.png)

## Layout e dimensionamento da tabela

### Ajuste automático de colunas e linhas

Este trecho de código mostra como ajustar automaticamente as larguras das colunas da tabela para caber na página.
Observe que no parâmetro table.column_widths = "50 50 50" - são pontos. Mas você também pode especificar centímetros (cm), polegadas ou %.

1. Defina as larguras iniciais das colunas.
1. Ajusta automaticamente as colunas para caber na largura da página.
1. Defina as bordas das células e da tabela.
1. O 'table.default_cell_padding' usa 'MarginInfo()' para um espaçamento consistente dentro das células.
1. Adicione linhas com 'table.rows.add()' e adicione células com 'row.cells.add()'.
1. Salve o PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    page.paragraphs.add(table)

    table.column_widths = "50 50 50"
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW

    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    table.default_cell_padding = margin

    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    document.save(path_outfile)
```

### Ajustando o espaçamento ao redor do conteúdo

Este exemplo mostra como criar tabelas que se estendem por várias páginas, tratar texto longo em células e aplicar preenchimento e bordas.

1. Adicione uma nova tabela à página usando 'page.paragraphs.add(table)'.
1. Defina as larguras das colunas com 'table.column_widths'.
1. Define bordas individuais das células com 'table.default_cell_border'.
1. Defina a borda geral da tabela com 'table.border'.
1. Defina o preenchimento padrão para as células usando 'MarginInfo()'.
1. Adicione texto usando 'TextFragment'.
1. Adicione outra linha.
1. Salve o PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object that will be nested inside outerTable that will break inside the same page
    table = ap.Table()
    # Add page
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(table)

    # Set column widths of the table
    table.column_widths = "50 50 50"

    # Set default cell border using BorderInfo object
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    # Set table border using another customized BorderInfo object
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    # Set the default cell padding to the MarginInfo object
    table.default_cell_padding = margin

    # Create rows and cells
    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()

    # Add a long text fragment into the third cell
    text = ap.text.TextFragment("col3 with large text string")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False

    # Add another row
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    # Save PDF document
    document.save(path_outfile)
```

![Bordas, margens e preenchimento](set-border-style-margins-and-padding-of-table_1.png)

### Estilizando cantos da tabela

Aspose.PDF for Python via .NET mostra como aplicar cantos arredondados a uma tabela e personalizar o raio da borda.

1. Crie uma nova instância de tabela.
1. Inicialize uma borda para todos os lados.
1. Defina o raio do canto.
1. Aplique o estilo de canto arredondado.
1. Adicione linhas e células.
1. Insira a tabela na página PDF com 'page.paragraphs.add(table)'.
1. Salve o documento PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Load source PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()

    # Create a table
    table = ap.Table()

    # Create a blank BorderInfo object
    b_info = ap.BorderInfo(ap.BorderSide.ALL)

    # Set the border a rounded border where radius of round is 15
    b_info.rounded_border_radius = 15

    # Set the table corner style as Round
    table.corner_style = ap.BorderCornerStyle.ROUND

    # Set the table border information
    table.border = b_info

    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

## Adicionando conteúdo às tabelas

### Usando fragmentos HTML em células

Este exemplo mostra como inserir conteúdo formatado em HTML nas células da tabela.

1. Defina as bordas da tabela e das células.
1. Adicione conteúdo HTML.
1. Adicione linhas. Um loop adiciona múltiplas linhas com conteúdo formatado em HTML em cada célula.
1. Insira a tabela na página PDF com 'page.paragraphs.add(table)'.
1. Salve o documento PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <strong>({row_count}, 1)</strong>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='color:red'>({row_count}, 2)</span>"
            )
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='text-decoration: underline'>({row_count}, 3)</span>"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

### Usando fragmentos LaTeX em células

Este exemplo mostra como inserir conteúdo formatado em LaTeX nas células da tabela para expressões matemáticas ou estilizadas.

1. Defina as bordas da tabela e das células.
1. Adicionar conteúdo LaTeX.
1. Adicionar linhas. Um loop adiciona várias linhas com conteúdo formatado em LaTeX em cada célula.
1. Inserir a tabela na página PDF com 'page.paragraphs.add(table)'.
1. Salvar o documento PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\mathbf{{({row_count}, 1)}}$")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\textcolor{{red}}{{({row_count}, 2)}}$"
            )
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(
                f"Column $\\underline{{({row_count}, 3)}}$"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(path_outfile)
```

## Recursos avançados de tabelas

### Inserindo tabelas em várias páginas

Este exemplo mostra como criar várias tabelas em um PDF, definir margens da página e forçar uma tabela a começar em uma nova página.

1. Definir margens da página usando 'page_info.margin'.
1. Definir a orientação da página para paisagem com 'page_info.is_landscape'.
1. Primeira tabela:
- definir duas colunas com larguras especificadas.
- adicionar as linhas em um loop com 'row.fixed_row_height'.
- preencher as células com fragmentos de texto.
1. Segunda tabela:
- criar uma nova tabela com 'table1.column_widths'.
- forçar a tabela a iniciar em uma nova página.
1. Adicionar a primeira tabela.
1. Adicionar a segunda tabela em uma nova página.
1. Salvar o documento

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Set page and margin information
    page_info = document.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37
    page_info.is_landscape = True

    # First table with 120 rows
    table = ap.Table()
    table.column_widths = "50 100"

    cur_page = document.pages.add()

    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 2"))

    cur_page.paragraphs.add(table)

    # Second table with 10 rows
    table1 = ap.Table()
    table1.column_widths = "100 100"

    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 3"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("Content 4"))

    table1.is_in_new_page = True  # Force table to new page
    cur_page.paragraphs.add(table1)

    # Save updated document containing table object
    document.save(path_outfile)
```

### Criando tabelas sem borda

Este exemplo mostra como criar uma tabela grande que pode ser dividida verticalmente entre páginas, repetir colunas e aplicar cores de fundo diferentes às células de cabeçalho.

1. Inicializar a tabela.
1. Definir uma borda padrão para todas as células.
1. Células de cabeçalho usam 'col_span' para mesclar várias colunas.
1. Definir o fundo da célula para melhor distinção visual com 'background_color set'
1. Adicionar linhas.
1. Inserir a tabela na página PDF com 'page.paragraphs.add(table)'.
1. Salvar o documento PDF.

```python

    import aspose.pdf as ap
    from os import path

    # The path to the documents directory
    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)
    table.repeating_columns_count = 2
    page.paragraphs.add(table)

    # Add header Row
    row = table.rows.add()
    cell = row.cells.add("header 1")
    cell.col_span = 2
    cell.background_color = ap.Color.light_gray
    row.cells.add("header 3")

    cell2 = row.cells.add("header 4")
    cell2.col_span = 2
    cell2.background_color = ap.Color.light_blue
    row.cells.add("header 6")

    cell3 = row.cells.add("header 7")
    cell3.col_span = 2
    cell3.background_color = ap.Color.light_green
    cell4 = row.cells.add("header 9")

    cell4.col_span = 3
    cell4.background_color = ap.Color.light_coral
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")

    row_counter = 0
    while row_counter < 3:
        # Create rows in the table and then cells in the rows
        row1 = table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 8")
        row1.cells.add("col " + str(row_counter) + ", 9")
        row1.cells.add("col " + str(row_counter) + ", 10")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
        row_counter += 1

    document.save(path_outfile)
```

### Repetindo linhas de cabeçalho em várias páginas

Este exemplo mostra como criar uma tabela que se estende por várias páginas mantendo as linhas de cabeçalho visíveis em cada página.

1. Inicializar a tabela.
1. Repetir linhas de cabeçalho incluindo fonte, tamanho e cor.
1. Definir larguras das colunas e aplicar bordas à tabela.
1. Adicionar linhas de cabeçalho.
1. Adicionar muitas linhas de dados para forçar a tabela a atravessar várias páginas.
1. Inserir a tabela na página PDF com 'page.paragraphs.add(table)'.
1. Salvar o documento PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Set the table to break across pages
    table.broken = ap.TableBroken.VERTICAL

    # Set number of repeating header rows
    table.repeating_rows_count = 2

    text_state = ap.text.TextState()
    text_state.font_size = 12
    text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_state.foreground_color = ap.Color.red
    table.repeating_rows_style =  text_state

    # Set column widths
    table.column_widths = "100 100 100"

    # Set borders
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.black)

    # Add header rows that will repeat on each page
    header_row1 = table.rows.add()
    header_row1.cells.add("Header 1-1")
    header_row1.cells.add("Header 1-2")
    header_row1.cells.add("Header 1-3")

    # Set background color for header rows
    for cell in header_row1.cells:
        cell.background_color = ap.Color.light_gray

    header_row2 = table.rows.add()
    header_row2.cells.add("Header 2-1")
    header_row2.cells.add("Header 2-2")
    header_row2.cells.add("Header 2-3")

    for cell in header_row2.cells:
        cell.background_color = ap.Color.light_blue

    # Add many data rows to force table across multiple pages
    for i in range(1, 101):
        row = table.rows.add()
        row.cells.add(f"Data {i}-1")
        row.cells.add(f"Data {i}-2")
        row.cells.add(f"Data {i}-3")

    # Add table to page
    page.paragraphs.add(table)

    # Save document
    document.save(path_outfile)
```

### Repetindo colunas

A função 'add_repeating_columns' cria um documento PDF com uma tabela que possui colunas repetidas. Ela configura uma tabela com bordas, adiciona cabeçalhos, preenche linhas de dados e salva o arquivo PDF gerado no local especificado. Definir esta propriedade fará com que a tabela quebre para a próxima página por colunas e repita a contagem de colunas fornecida no início da próxima página.

1. Inicializa um novo documento PDF.
1. Adiciona uma página com dimensões personalizadas.
1. Definir o estilo da borda da tabela.
1. Inicializar a tabela.
1. Adicionar a tabela à página PDF.
1. Adicionar linha de cabeçalho.
1. Adicionar linhas de dados.
1. Salvar documento PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_outfile = path.join(self.data_dir, outfile)

    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()
    page.set_page_size(ap.PageSize.A5.height, ap.PageSize.A5.width)

    # Define border
    border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)

    # Create table
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    table.repeating_columns_count = 5
    table.border = border
    table.default_cell_border = border

    # Add table to page
    page.paragraphs.add(table)

    # Add header row
    row = table.rows.add()
    for i in range(1, 6):
        cell = row.cells.add(f"header {i}")
        cell.background_color = ap.Color.light_gray

    for i in range(6, 18):
        row.cells.add(f"header {i}")

    # Add data rows
    for row_counter in range(1, 6):
        row = table.rows.add()
        for i in range(1, 6):
            cell = row.cells.add(f"cell {row_counter},{i}")
            cell.background_color = ap.Color.light_gray
        for i in range(6, 18):
            row.cells.add(f"cell {row_counter},{i}")

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
