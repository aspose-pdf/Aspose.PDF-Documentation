---
title: Manipular Documento PDF em Python via .NET
linktitle: Manipular Documento PDF
type: docs
weight: 20
url: /pt/python-net/manipulate-pdf-document/
description: Este artigo contém informações sobre como validar Documento PDF para o Padrão PDF A usando Python, como trabalhar com TOC, como definir a data de validade do PDF, etc.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guia sobre manipulação de documentos PDF usando Python
Abstract: Este artigo fornece um guia abrangente sobre a manipulação de documentos PDF usando Python, especificamente com a biblioteca Aspose.PDF. Ele abrange várias funcionalidades, incluindo a validação de documentos PDF para conformidade PDF/A-1a e PDF/A-1b usando o método `validate` da classe `Document`. Também detalha como adicionar, personalizar e gerenciar uma Tabela de Conteúdos (TOC) em arquivos PDF, como definir diferentes TabLeaderTypes, ocultar números de página e personalizar a numeração de páginas com um prefixo. Além disso, o artigo explica como definir uma data de expiração para um documento PDF incorporando JavaScript para restrição de acesso e como achatar formulários preenchíveis em um PDF para torná-los não editáveis. Cada seção é acompanhada por trechos de código que demonstram a implementação dessas funcionalidades usando Aspose.PDF em Python.
---

## Manipular Documento PDF em Python

## Validar Documento PDF para o Padrão PDF A (A 1A e A 1B)

Para validar um documento PDF para compatibilidade PDF/A-1a ou PDF/A-1b, use o método [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Este método permite especificar o nome do arquivo onde o resultado será salvo e o tipo de validação requerido da enumeração PdfFormat: PDF_A_1A ou PDF_A_1B.

O trecho de código a seguir mostra como validar um documento PDF para PDF/A-1A.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

O trecho de código a seguir mostra como validar um documento PDF para PDF/A-1b.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```

## Trabalhando com TOC

### Adicionar TOC a PDF Existente

TOC em PDF significa "Table of Contents" (Tabela de Conteúdos). É um recurso que permite aos usuários navegar rapidamente por um documento, fornecendo uma visão geral de suas seções e títulos.

Para adicionar um TOC a um arquivo PDF existente, use a classe Heading no namespace [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). O namespace [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) pode tanto criar novos quanto manipular arquivos PDF existentes. Para adicionar um TOC a um PDF existente, use o namespace Aspose.Pdf. O trecho de código a seguir mostra como criar uma tabela de conteúdos dentro de um arquivo PDF existente usando Python via .NET.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)

    # Get access to first page of PDF file
    tocPage = doc.pages.insert(1)

    # Create object to represent TOC information
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Set the title for TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Create string objects which will be used as TOC elements
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 2]

        # Destination page
        heading2.top = doc.pages[i + 2].rect.height

        # Destination coordinate
        segment2.text = titles[i]

        # Add heading to page containing TOC
        tocPage.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)
```

### Definir TabLeaderType diferente para diferentes níveis de TOC

Aspose.PDF for Python também permite definir TabLeaderType diferente para diferentes níveis de TOC. É necessário definir a propriedade [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) da [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # set LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title

    # Add the list section to the sections collection of the Pdf document
    tocPage.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins
    # and
    # text format settings of each level

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Create a section in the Pdf document
    page = doc.pages.add()

    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Sample Heading" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Add the heading into Table Of Contents.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # save the Pdf
    doc.save(output_pdf)
```

### Ocultar Números de Página no TOC

Caso não deseje exibir números de página junto com os títulos no TOC, você pode usar a propriedade [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) da classe [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) como false. Veja o trecho de código a seguir para ocultar os números de página na tabela de conteúdos:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Add the list section to the sections collection of the Pdf document
    toc_page.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins and
    # text format settings of each level

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "this is heading of level " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```

### Personalizar Números de Página ao adicionar TOC

É comum personalizar a numeração de páginas no TOC ao adicioná-lo em um documento PDF. Por exemplo, podemos precisar adicionar um prefixo antes do número da página, como P1, P2, P3 e assim por diante. Nesse caso, Aspose.PDF for Python fornece a propriedade [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) da classe [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) que pode ser usada para personalizar os números de página, como mostrado no exemplo de código a seguir.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)
    # Get access to first page of PDF file
    toc_page = doc.pages.insert(1)
    # Create object to represent TOC information
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Set the title for TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 1]
        # Destination page
        heading2.top = doc.pages[i + 1].rect.height
        # Destination coordinate
        segment2.text = "Page " + str(i)
        # Add heading to page containing TOC
        toc_page.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)

```

## Como definir a data de validade do PDF

Aplicamos privilégios de acesso em arquivos PDF para que um determinado grupo de usuários possa acessar recursos/objetos específicos dos documentos PDF. Para restringir o acesso ao arquivo PDF, geralmente aplicamos criptografia e pode haver a necessidade de definir a expiração do arquivo PDF, de modo que o usuário que acessa/visualiza o documento receba um aviso válido sobre a validade do PDF.

```python

    import aspose.pdf as ap

    # Instantiate Document object
    doc = ap.Document()
    # Add page to pages collection of PDF file
    doc.pages.add()
    # Add text fragment to paragraphs collection of page object
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # Create JavaScript object to set PDF expiry date
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # Set JavaScript as PDF open action
    doc.open_action = javaScript

    # Save PDF Document
    doc.save(output_pdf)
```

## Achatar PDF Preenchível em Python

Documentos PDF frequentemente incluem formulários com widgets interativos preenchíveis, como botões de opção, caixas de seleção, campos de texto, listas, etc. Para torná-los não editáveis para diversos propósitos de aplicação, precisamos achatar o arquivo PDF.
Aspose.PDF fornece a função para achatar seu PDF em Python com apenas algumas linhas de código:

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Flatten Fillable PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```


