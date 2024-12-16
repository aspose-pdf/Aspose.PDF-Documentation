---
title: Manipular Tabelas em PDF existente
linktitle: Manipular Tabelas
type: docs
weight: 40
url: /pt/python-net/manipulate-tables-in-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipular Tabelas em PDF existente",
    "alternativeHeadline": "Como atualizar o conteúdo das Tabelas em PDF existente",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, manipular tabelas",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


## Manipular tabelas em PDF existente

Uma das primeiras funcionalidades suportadas pelo Aspose.PDF para Python via .NET é a sua capacidade de Trabalhar com Tabelas e fornece ótimo suporte para adicionar tabelas em arquivos PDF sendo gerados do zero ou em qualquer arquivo PDF existente. Nesta nova versão, implementamos uma nova funcionalidade de pesquisa e análise de tabelas simples que já existem na página de um documento PDF. Uma nova classe chamada [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) fornece essas capacidades. O uso do TableAbsorber é muito semelhante à classe existente [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/). O trecho de código a seguir mostra as etapas para atualizar o conteúdo em uma célula específica da tabela.

```python

    import aspose.pdf as ap

    # Carregar arquivo PDF existente
    pdf_document = ap.Document(input_file)
    # Criar objeto TableAbsorber para encontrar tabelas
    absorber = ap.text.TableAbsorber()
    # Visitar a primeira página com o absorvedor
    absorber.visit(pdf_document.pages[1])
    # Obter acesso à primeira tabela na página, sua primeira célula e fragmentos de texto nela
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # Alterar o texto do primeiro fragmento de texto na célula
    fragment.text = "olá mundo"
    pdf_document.save(output_file)
```


## Substituir tabela antiga por uma nova em documento PDF

Caso você precise encontrar uma tabela específica e substituí-la pela desejada, você pode usar o método [replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) da classe [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) para fazer isso. O exemplo a seguir demonstra a funcionalidade de substituir a tabela dentro de um documento PDF:

```python

    import aspose.pdf as ap

    # Carregar documento PDF existente
    pdf_document = ap.Document(input_file)
    # Criar objeto TableAbsorber para encontrar tabelas
    absorber = ap.text.TableAbsorber()
    # Visitar a primeira página com o absorvedor
    absorber.visit(pdf_document.pages[1])
    # Obter a primeira tabela na página
    table = absorber.table_list[0]
    # Criar nova tabela
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")

    # Substituir a tabela pela nova
    absorber.replace(pdf_document.pages[1], table, new_table)
    # Salvar documento
    pdf_document.save(output_file)
```


## Como determinar se a tabela vai quebrar na página atual

Este código gera um documento PDF contendo uma tabela, calcula o espaço disponível na página e verifica se adicionar mais linhas à tabela levará a uma quebra de página com base nas restrições de espaço. O resultado é salvo em um arquivo de saída.

```python

    import aspose.pdf as ap

    # Instanciar um objeto da classe PDF
    pdf = ap.Document()
    # Adicionar a seção à coleção de seções do documento PDF
    page = pdf.pages.add()
    # Instanciar um objeto de tabela
    table1 = ap.Table()
    table1.margin.top = 300
    # Adicionar a tabela na coleção de parágrafos da seção desejada
    page.paragraphs.add(table1)
    # Definir as larguras das colunas da tabela
    table1.column_widths = "100 100 100"
    # Definir borda de célula padrão usando o objeto BorderInfo
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Definir borda da tabela usando outro objeto BorderInfo personalizado
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Criar objeto MarginInfo e definir suas margens esquerda, inferior, direita e superior
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Definir o preenchimento de célula padrão para o objeto MarginInfo
    table1.default_cell_padding = margin
    # Se você aumentar o contador para 17, a tabela irá quebrar
    # Porque não pode ser acomodada mais nesta página
    for row_counter in range(0, 17):
        # Criar linhas na tabela e depois células nas linhas
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # Obter a informação de altura da página
    page_height = pdf.page_info.height
    # Obter a informação total de altura das margens superior e inferior da página,
    # Margem superior da tabela e altura da tabela.
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # Exibir a altura da página, altura da tabela, margem superior da tabela e
    # Informações sobre as margens superior e inferior da página
    print("Altura do documento PDF = " + str(pdf.page_info.height) + "\nInformação da Margem Superior = " + str(page.page_info.margin.top)
          + "\nInformação da Margem Inferior = " + str(page.page_info.margin.bottom) + "\n\nInformação da Margem Superior da Tabela = "
          + str(table1.margin.top) + "\nAltura Média da Linha = " + str(table1.rows[0].min_row_height) + " \nAltura da Tabela "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\nAltura Total da Página ="
          + str(page_height) + "\nAltura cumulativa incluindo a Tabela =" + str(total_objects_height))
    # Verificar se subtrairmos a soma da margem superior da página + margem inferior da página
    # + Margem superior da tabela e altura da tabela da altura da página e é menor
    # Que 10 (uma linha média pode ser maior que 10)
    if (page_height - total_objects_height) <= 10:
        # Se o valor for menor que 10, então exibir a mensagem.
        # Que mostra que outra linha não pode ser colocada e se adicionarmos uma nova
        # Linha, a tabela irá quebrar. Isso depende do valor da altura da linha.
        print("Altura da Página - Altura dos Objetos < 10, então a tabela irá quebrar")
    # Salvar o documento PDF
    pdf.save(output_file)
```


## Adicionar Coluna Repetida na Tabela

Na classe [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), você pode definir um [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) que repetirá linhas se a tabela for muito longa verticalmente e transbordar para a próxima página. No entanto, em alguns casos, as tabelas são muito largas para caber em uma única página e precisam ser continuadas na próxima página. Para atender a esse propósito, implementamos a propriedade [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) na classe [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/). Definir essa propriedade fará com que a tabela quebre para a próxima página em colunas e repita a contagem de colunas especificada no início da próxima página. O trecho de código a seguir mostra o uso da propriedade [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties):

```python

    import aspose.pdf as ap

    # Criar um novo documento
    doc = ap.Document()
    page = doc.pages.add()
    # Instanciar uma tabela externa que ocupa toda a página
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Instanciar um objeto de tabela que será aninhado dentro de outerTable que quebrará dentro da mesma página
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Adicionar a outerTable aos parágrafos da página
    # Adicionar minha tabela à outerTable
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # Adicionar Linha de Cabeçalho
    row = my_table.rows.add()
    row.cells.add("cabeçalho 1")
    row.cells.add("cabeçalho 2")
    row.cells.add("cabeçalho 3")
    row.cells.add("cabeçalho 4")
    row.cells.add("cabeçalho 5")
    row.cells.add("cabeçalho 6")
    row.cells.add("cabeçalho 7")
    row.cells.add("cabeçalho 11")
    row.cells.add("cabeçalho 12")
    row.cells.add("cabeçalho 13")
    row.cells.add("cabeçalho 14")
    row.cells.add("cabeçalho 15")
    row.cells.add("cabeçalho 16")
    row.cells.add("cabeçalho 17")
    for row_counter in range(0, 6):
        # Criar linhas na tabela e depois células nas linhas
        row1 = my_table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python via Biblioteca .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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