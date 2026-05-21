---
title: Manipular documentos PDF em Python
linktitle: Manipular documento PDF
type: docs
weight: 20
url: /pt/python-net/manipulate-pdf-document/
description: Aprenda como validar, estruturar e modificar documentos PDF em Python, incluindo o gerenciamento de TOC e verificações de PDF/A.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guia sobre manipulação de documentos PDF usando Python
Abstract: Este artigo fornece um guia abrangente sobre a manipulação de documentos PDF usando Python, especificamente com a biblioteca Aspose.PDF. Ele cobre diversas funcionalidades, incluindo a validação de documentos PDF para conformidade PDF/A-1a e PDF/A-1b usando o método `validate` da classe `Document`. Ele também detalha como adicionar, personalizar e gerenciar um Sumário (TOC) em arquivos PDF, como definir diferentes TabLeaderTypes, ocultar números de página e personalizar a numeração de páginas com um prefixo. Além disso, o artigo explica como definir uma data de expiração para um documento PDF incorporando JavaScript para restrição de acesso e como achatar formulários preenchíveis em um PDF para torná‑los não editáveis. Cada seção é acompanhada por trechos de código que demonstram a implementação desses recursos usando Aspose.PDF em Python.
---

Esta página é útil quando você precisa validar a conformidade de PDF, criar ou personalizar um índice, definir o comportamento de expiração de documentos ou achatar PDFs preenchíveis em fluxos de trabalho Python.

## Manipular Documento PDF em Python

## Validar Documento PDF para o padrão PDF/A (A 1A e A 1B)

Para validar um documento PDF para compatibilidade PDF/A-1a ou PDF/A-1b, use o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método. Este método permite especificar o nome do arquivo no qual o resultado será salvo e o tipo de validação necessário da enumeração PdfFormat: PDF_A_1A ou PDF_A_1B.

O trecho de código a seguir mostra como validar um documento PDF para PDF/A-1A.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

O trecho de código a seguir mostra como validar um documento PDF para PDF/A-1b.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## Trabalhando com TOC

### Adicionar TOC a PDF Existente

TOC em PDF significa "Table of Contents". É um recurso que permite aos usuários navegar rapidamente por um documento, oferecendo uma visão geral de suas seções e cabeçalhos. 

Para adicionar um TOC a um arquivo PDF existente, use a classe Heading no [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace. O [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace pode criar novos e manipular PDFs existentes. Para adicionar um TOC a um PDF existente, use o namespace Aspose.Pdf. O trecho de código a seguir demonstra como criar um TOC dentro de um arquivo PDF existente usando Python via .NET.

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Defina diferentes TabLeaderType para diferentes níveis de TOC

Aspose.PDF for Python também permite definir diferentes TabLeaderType para diferentes níveis de TOC. Você precisa definir [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propriedade de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
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

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Ocultar números de página no TOC

Caso não queira exibir números de página, juntamente com os títulos no TOC, você pode usar [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propriedade de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Classe como falso. Por favor, verifique o trecho de código a seguir para ocultar os números de página no sumário:

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Personalizar números de página ao adicionar o TOC

É comum personalizar a numeração de páginas no TOC ao adicionar o TOC em um documento PDF. Por exemplo, pode ser necessário adicionar algum prefixo antes do número da página, como P1, P2, P3 e assim por diante. Nesse caso, Aspose.PDF for Python fornece [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propriedade de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) classe que pode ser usada para personalizar números de página como mostrado no exemplo de código a seguir.

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## Como definir a data de expiração do PDF

Aplicamos privilégios de acesso em arquivos PDF para que um determinado grupo de usuários possa acessar recursos/objetos específicos de documentos PDF. Para restringir o acesso ao arquivo PDF, normalmente aplicamos criptografia e podemos ter a necessidade de definir a expiração do arquivo PDF, de modo que o usuário que acessa/visualiza o documento receba um aviso válido sobre a expiração do arquivo PDF.

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## Achatar PDF preenchível em Python

Documentos PDF frequentemente incluem formulários com widgets interativos preenchíveis, como botões de opção, caixas de seleção, caixas de texto, listas, etc. Para torná-lo não editável para várias finalidades de aplicação, precisamos achatar o arquivo PDF.
Aspose.PDF fornece a função para achatar seu PDF em Python com apenas algumas linhas de código:

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## Tópicos de Documentos Relacionados

- [Trabalhe com documentos PDF em Python](/pdf/pt/python-net/working-with-documents/)
- [Formatar documentos PDF em Python](/pdf/pt/python-net/formatting-pdf-document/)
- [Criar arquivos PDF em Python](/pdf/pt/python-net/create-pdf-document/)
- [Otimize arquivos PDF em Python](/pdf/pt/python-net/optimize-pdf/)
