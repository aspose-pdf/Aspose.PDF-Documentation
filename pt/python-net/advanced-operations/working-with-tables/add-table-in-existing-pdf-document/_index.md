---
title: Criar ou Adicionar Tabela em PDF usando Python 
linktitle: Criar ou Adicionar Tabela
type: docs
weight: 10
url: /pt/python-net/add-table-in-existing-pdf-document/
description: Aspose.PDF para Python via .NET é uma biblioteca usada para criar, ler e editar Tabelas em PDF. Verifique outras funções avançadas neste tópico.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Criar ou Adicionar Tabela em PDF usando Python ",
    "alternativeHeadline": "Como adicionar Tabela em PDF com Python via .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, criar tabela em pdf, adicionar tabela",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF para Python via .NET é uma biblioteca usada para criar, ler e editar Tabelas em PDF. Verifique outras funções avançadas neste tópico."
}
</script>


## Criando Tabela usando Python

Tabelas são importantes ao trabalhar com documentos PDF. Elas oferecem ótimos recursos para exibir informações de maneira sistemática. O namespace Aspose.PDF contém classes chamadas [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/) e [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) que fornecem funcionalidade para criar tabelas ao gerar documentos PDF do zero.

A tabela pode ser criada criando um objeto da Classe Table.

```python

    table = ap.Table()
```

### Adicionando Tabela em Documento PDF Existente

Para adicionar uma tabela a um arquivo PDF existente com Aspose.PDF para Python via .NET, siga os seguintes passos:

1. Carregue o arquivo fonte.
1. Inicialize uma tabela e defina suas colunas e linhas.
1. Defina a configuração da tabela (definimos as bordas).
1. Preencha a tabela.
1. Adicione a tabela a uma página.
1. Salve o arquivo.

Os snippets de código a seguir mostram como adicionar texto em um arquivo PDF existente.

```python

    import aspose.pdf as ap

    # Carregar documento PDF de origem
    doc = ap.Document(input_file)
    # Inicializa uma nova instância da Tabela
    table = ap.Table()
    # Definir a cor da borda da tabela como Cinza Claro
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Definir a borda para as células da tabela
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Criar um loop para adicionar 10 linhas
    for row_count in range(0, 10):
        # Adicionar linha à tabela
        row = table.rows.add()
        # Adicionar células à tabela
        row.cells.add("Coluna (" + str(row_count) + ", 1)")
        row.cells.add("Coluna (" + str(row_count) + ", 2)")
        row.cells.add("Coluna (" + str(row_count) + ", 3)")
    # Adicionar objeto de tabela à primeira página do documento de entrada
    doc.pages[1].paragraphs.add(table)
    # Salvar documento atualizado contendo o objeto de tabela
    doc.save(output_file)
```

### ColSpan e RowSpan em Tabelas

Aspose.PDF para Python via .NET fornece a propriedade [col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) para mesclar as colunas em uma tabela e a propriedade [row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) para mesclar as linhas.


Nós usamos a propriedade `col_span` ou `row_span` no objeto `Cell`, que cria a célula da tabela. Após aplicar as propriedades necessárias, a célula criada pode ser adicionada à tabela.

```python

    import aspose.pdf as ap

    # Inicializa o objeto Document chamando seu construtor vazio
    pdf_document = ap.Document()
    pdf_document.pages.add()
    # Inicializa uma nova instância da Tabela
    table = ap.Table()
    # Define a cor da borda da tabela como LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Define a borda para as células da tabela
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Adiciona a 1ª linha à tabela
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Adiciona células à tabela
        row1.cells.add("Teste 1" + str(cellCount))

    # Adiciona a 2ª linha à tabela
    row2 = table.rows.add()
    row2.cells.add("Teste 2 1")
    cell = row2.cells.add("Teste 2 2")
    cell.col_span = 2
    row2.cells.add("Teste 2 4")

    # Adiciona a 3ª linha à tabela
    row3 = table.rows.add()
    row3.cells.add("Teste 3 1")
    row3.cells.add("Teste 3 2")
    row3.cells.add("Teste 3 3")
    row3.cells.add("Teste 3 4")

    # Adiciona a 4ª linha à tabela
    row4 = table.rows.add()
    row4.cells.add("Teste 4 1")
    cell = row4.cells.add("Teste 4 2")
    cell.row_span = 2
    row4.cells.add("Teste 4 3")
    row4.cells.add("Teste 4 4")

    # Adiciona a 5ª linha à tabela
    row5 = table.rows.add()
    row5.cells.add("Teste 5 1")
    row5.cells.add("Teste 5 3")
    row5.cells.add("Teste 5 4")

    # Adiciona o objeto tabela à primeira página do documento de entrada
    pdf_document.pages[1].paragraphs.add(table)
    # Salva o documento atualizado contendo o objeto tabela
    pdf_document.save(output_file)
```


O resultado do código de execução abaixo é a tabela mostrada na imagem a seguir:

![Demonstração de ColSpan e RowSpan](colspan_rowspan.png)

## Trabalhando com Bordas, Margens e Espaçamento Interno

Note que também suporta o recurso de definir estilo de borda, margens e espaçamento interno para tabelas. Antes de entrar em mais detalhes técnicos, é importante entender os conceitos de borda, margens e espaçamento interno, que são apresentados abaixo em um diagrama:

![Bordas, margens e espaçamento interno](set-border-style-margins-and-padding-of-table_1.png)

Na figura acima, você pode ver que as bordas da tabela, linha e célula se sobrepõem. Usando Aspose.PDF, uma tabela pode ter margens e as células podem ter espaçamentos internos. Para definir margens de célula, temos que definir o espaçamento interno da célula.

### Bordas

Para definir as bordas dos objetos [Tabela](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Linha](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) e [Célula](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/), use as propriedades Table.border, Row.border e Cell.border.
 Os bordas das células também podem ser definidas usando a propriedade [default_cell_border](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) da classe [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) ou Row. Todas as propriedades relacionadas às bordas discutidas acima são atribuídas a uma instância da classe Row, que é criada chamando seu construtor. A classe Row tem muitas sobrecargas que aceitam quase todos os parâmetros necessários para personalizar a borda.

### Margens ou Padding

O padding das células pode ser gerenciado usando a propriedade [default_cell_padding](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/#properties) da classe Table. Todas as propriedades relacionadas ao padding são atribuídas a uma instância da classe [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) que recebe informações sobre os parâmetros `left`, `right`, `top` e `bottom` para criar margens personalizadas.
No exemplo a seguir, a largura da borda da célula é definida para 0,1 ponto, a largura da borda da tabela é definida para 1 ponto e o preenchimento da célula é definido para 5 pontos.

![Margem e Borda na Tabela PDF](margin-border.png)

```python

    import aspose.pdf as ap

    # Instanciar o objeto Document chamando seu construtor vazio
    doc = ap.Document()
    page = doc.pages.add()
    # Instanciar um objeto de tabela
    tab1 = ap.Table()
    # Adicionar a tabela na coleção de parágrafos da seção desejada
    page.paragraphs.add(tab1)
    # Definir larguras das colunas da tabela
    tab1.column_widths = "50 50 50"
    # Definir borda padrão da célula usando o objeto BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Definir borda da tabela usando outro objeto BorderInfo personalizado
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Criar objeto MarginInfo e definir suas margens esquerda, inferior, direita e superior
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Definir o preenchimento padrão da célula para o objeto MarginInfo
    tab1.default_cell_padding = margin
    # Criar linhas na tabela e depois células nas linhas
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    my_text = ap.text.TextFragment("col3 com string de texto grande")
    # Row1.Cells.Add("col3 com string de texto grande para ser colocada dentro da célula")
    row1.cells[2].paragraphs.add(my_text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Salvar o Pdf
    doc.save(output_file)
```


Para criar uma tabela com canto arredondado, use o valor [rounded_border_radius](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/#properties) da [classe BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) e defina o estilo do canto da tabela como arredondado.

```python
    
    import aspose.pdf as ap
    
    tab1 = ap.Table()
    graph = ap.GraphInfo()
    graph.color = ap.Color.red
    # Cria um objeto BorderInfo em branco
    b_info = ap.BorderInfo(ap.BorderSide.ALL, graph)
    # Define a borda como uma borda arredondada onde o raio do arredondamento é 15
    b_info.rounded_border_radius = 15
    # Define o estilo do canto da tabela como Arredondado
    tab1.corner_style = ap.BorderCornerStyle.ROUND
    # Define as informações da borda da tabela
    tab1.border = b_info
```

## Aplicando Diferentes Configurações de AutoAjuste a uma Tabela

Ao projetar uma tabela usando uma ferramenta visual como o Microsoft Word, você frequentemente utilizará um dos recursos de AutoAjuste para ajustar convenientemente o tamanho da tabela à largura desejada.
 Por exemplo, você pode usar a opção "AUTO_FIT_TO_WINDOW" para ajustar a largura da tabela à página ou AUTO_FIT_TO_CONTENT. Por padrão, ao usar o Aspose.Pdf para criar uma nova tabela, ele emprega o [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) com um valor "Customized". No trecho de código a seguir, configuramos os parâmetros do objeto [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) e objetos [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) na tabela. Teste o exemplo e avalie o resultado.

```python

    import aspose.pdf as ap

    # Instanciar o objeto Pdf chamando seu construtor vazio
    doc = ap.Document()
    # Criar a seção no objeto Pdf
    sec1 = doc.pages.add()
    # Instanciar um objeto de tabela
    tab1 = ap.Table()
    # Adicionar a tabela na coleção de parágrafos da seção desejada
    sec1.paragraphs.add(tab1)
    # Definir as larguras das colunas da tabela
    tab1.column_widths = "50 50 50"
    tab1.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
    # Definir a borda padrão da célula usando o objeto BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Definir a borda da tabela usando outro objeto BorderInfo personalizado
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Criar objeto MarginInfo e definir suas margens esquerda, inferior, direita e superior
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Definir o preenchimento padrão da célula para o objeto MarginInfo
    tab1.default_cell_padding = margin
    # Criar linhas na tabela e depois células nas linhas
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Salvar documento atualizado contendo o objeto tabela
    doc.save(output_file)
```

### Obter Largura da Tabela

Às vezes, é necessário obter a largura da tabela dinamicamente. A classe Aspose.PDF.Table tem um método [get_width()](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#methods) para essa finalidade. Por exemplo, você não definiu a largura das colunas da tabela explicitamente e definiu [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) como 'AUTO_FIT_TO_CONTENT'. Nesse caso, você pode obter a largura da tabela da seguinte forma.

```python

    import aspose.pdf as ap

    # Criar um novo documento
    doc = ap.Document()
    # Adicionar página no documento
    page = doc.pages.add()
    # Inicializar nova tabela
    table = ap.Table()
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Adicionar linha na tabela
    row = table.rows.add()
    # Adicionar célula na tabela
    cell = row.cells.add("Texto da Célula 1")
    cell = row.cells.add("Texto da Célula 2")
    # Obter largura da tabela
    print(table.get_width())
```

## Adicionar Imagem SVG à Célula da Tabela

Aspose.PDF para Python via .NET fornece a capacidade de inserir células de tabela em um arquivo PDF.
 When constructing a table, you can include both text and images within these cells. Additionally, the API offers the functionality to transform SVG files into PDF format. By leveraging these functionalities together, you can load an SVG image and place it within a table cell.

Ao construir uma tabela, você pode incluir tanto texto quanto imagens dentro dessas células. Além disso, a API oferece a funcionalidade de transformar arquivos SVG em formato PDF. Ao utilizar essas funcionalidades em conjunto, você pode carregar uma imagem SVG e colocá-la dentro de uma célula da tabela.

The following code excerpt demonstrates the process of creating a table object and embedding an SVG image inside one of its cells.

O trecho de código a seguir demonstra o processo de criação de um objeto de tabela e a incorporação de uma imagem SVG dentro de uma de suas células.

```python

    import aspose.pdf as ap

    # Instantiate Document object
    # Instanciar objeto Documento
    doc = ap.Document()
    # Create an image instance
    # Criar uma instância de imagem
    img = ap.Image()
    # Set image type as SVG
    # Definir tipo de imagem como SVG
    img.file_type = ap.ImageFileType.SVG
    # Path for source file
    # Caminho para o arquivo de origem
    img.file = DIR_INPUT_TABLE + "SVGToPDF.svg"
    # Set width for image instance
    # Definir largura para a instância de imagem
    img.fix_width = 50
    # Set height for image instance
    # Definir altura para a instância de imagem
    img.fix_height = 50
    # Create table instance
    # Criar instância de tabela
    table = ap.Table()
    # Set width for table cells
    # Definir largura para as células da tabela
    table.column_widths = "100 100"
    # Create row object and add it to table instance
    # Criar objeto linha e adicioná-lo à instância de tabela
    row = table.rows.add()
    # Create cell object and add it to row instance
    # Criar objeto célula e adicioná-lo à instância de linha
    cell = row.cells.add()
    # Add textfragment to paragraphs collection of cell object
    # Adicionar fragmento de texto à coleção de parágrafos do objeto célula
    cell.paragraphs.add(ap.text.TextFragment("First cell"))
    # Add another cell to row object
    # Adicionar outra célula ao objeto linha
    cell = row.cells.add()
    # Add SVG image to paragraphs collection of recently added cell instance
    # Adicionar imagem SVG à coleção de parágrafos da instância de célula recentemente adicionada
    cell.paragraphs.add(img)
    # Create page object and add it to pages collection of document instance
    # Criar objeto página e adicioná-lo à coleção de páginas da instância de documento
    page = doc.pages.add()
    # Add table to paragraphs collection of page object
    # Adicionar tabela à coleção de parágrafos do objeto página
    page.paragraphs.add(table)
    # Save PDF file
    # Salvar arquivo PDF
    doc.save(output_file)
```

## Inserir uma Quebra de Página entre as linhas da tabela

Por padrão, quando você cria uma tabela dentro de um arquivo PDF, a tabela se estenderá por várias páginas se ultrapassar a margem inferior da tabela. No entanto, há situações em que precisamos impor quebras de página após um número específico de linhas terem sido adicionadas à tabela. O trecho de código a seguir descreve o processo de inserção de uma quebra de página quando 10 linhas foram incluídas na tabela.

```python

    import aspose.pdf as ap

    # Instanciar a instância do Documento
    doc = ap.Document()
    # Adicionar página à coleção de páginas do arquivo PDF
    doc.pages.add()
    # Criar instância da tabela
    tab = ap.Table()
    # Definir estilo de borda para a tabela
    tab.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Definir estilo de borda padrão para a tabela com cor de borda como Vermelho
    tab.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Especificar a largura das colunas da tabela
    tab.column_widths = "100 100"
    # Criar um loop para adicionar 200 linhas à tabela
    for counter in range(0, 201):
        row = ap.Row()
        tab.rows.add(row)
        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment("Célula " + str(counter) + ", 0"))
        row.cells.add(cell1)
        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment("Célula " + str(counter) + ", 1"))
        row.cells.add(cell2)
        # Quando 10 linhas são adicionadas, renderizar nova linha em nova página
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True
    # Adicionar tabela à coleção de parágrafos do arquivo PDF
    doc.pages[1].paragraphs.add(tab)
    # Salvar o documento PDF
    doc.save(output_file)
```


## Renderizar uma Tabela em uma Nova Página

Por padrão, parágrafos são adicionados à coleção de Parágrafos de um objeto Page. No entanto, é possível renderizar uma tabela em uma nova página ao invés de diretamente após o objeto de nível de parágrafo adicionado anteriormente na página.

### Exemplo: Como Renderizar uma Tabela em uma Nova Página usando Python

Para renderizar uma tabela em uma nova página, use a propriedade [is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) na classe [BaseParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/baseparagraph/). O trecho de código a seguir mostra como fazer isso.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    page_info = doc.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37

    page_info.is_landscape = True

    table = ap.Table()
    table.column_widths = "50 100"
    # Página adicionada.
    cur_page = doc.pages.add()
    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Conteúdo 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("HHHHH"))
    paragraphs = cur_page.paragraphs
    paragraphs.add(table)

    table1 = ap.Table()
    table1.column_widths = "100 100"
    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("LAAAAAAA"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("LAAGGGGGG"))
    table1.is_in_new_page = True
    # Eu quero manter a tabela 1 na próxima página, por favor...
    paragraphs.add(table1)
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulação de PDF para Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>