---
title: Adicionar Cabeçalho e Rodapé ao PDF usando Python
linktitle: Adicionar Cabeçalho e Rodapé ao PDF
type: docs
weight: 50
url: /pt/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET permite que você adicione cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar Cabeçalho e Rodapé ao PDF usando Python
Abstract: O artigo oferece um guia abrangente sobre como usar **Aspose.PDF for Python via .NET** para adicionar cabeçalhos e rodapés a arquivos PDF, com a capacidade de incorporar texto ou imagens. Ele começa detalhando o uso da classe `TextStamp` para inserir texto no cabeçalho de um documento PDF. Propriedades chave como tamanho da fonte, estilo e cor são ajustáveis, e o método para adicionar texto ao cabeçalho é demonstrado com um trecho de código Python. O artigo explica de forma semelhante como adicionar texto ao rodapé, seguindo os mesmos passos procedimentais. Para adicionar imagens, a classe `ImageStamp` é empregada, e o processo é descrito tanto para cabeçalhos quanto para rodapés, novamente suportado por exemplos de código Python. Além disso, o artigo discute a adição de múltiplos cabeçalhos em um único arquivo PDF. Isso inclui criar múltiplos objetos `TextStamp`, cada um com formatação distinta, e aplicá‑los em diferentes páginas. A explicação é complementada por um trecho de código detalhado demonstrando essa funcionalidade.
---

Esta página fornece uma visão concisa sobre a adição de cabeçalhos e rodapés a documentos PDF usando Aspose.PDF for Python via .NET, abrangendo abordagens baseadas em texto, HTML, LaTeX, imagem e tabela, bem como numeração dinâmica de páginas e múltiplos cabeçalhos por página; explica como criar e estilizar objetos [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) (usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), etc.), ajustar [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) e [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) para posicionamento preciso, e anexar os resultados às páginas com exemplos práticos de código Python.

**Aspose.PDF for Python via .NET** permite que você adicione cabeçalho e rodapé no seu [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Você pode adicionar imagens ou texto a um documento PDF. Também, experimente adicionar cabeçalhos diferentes em um arquivo PDF com Python.

## Adicionando Cabeçalhos e Rodapés como Fragmentos de Texto

Adicione cabeçalhos e rodapés de texto simples a todas as páginas de um PDF. Ele cria objetos [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/), insere elementos [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) neles, define [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) para posicionamento adequado e os anexa a cada página do documento. O resultado é um PDF onde cada página exibe texto de cabeçalho e rodapé consistente.

O trecho de código a seguir demonstra como adicionar cabeçalhos e rodapés como fragmentos de texto em um PDF usando Python:

1. Crie fragmentos de texto para o cabeçalho e o rodapé.
1. Crie objetos HeaderFooter e adicione os fragmentos de texto a eles.
1. Defina as configurações de margem para controlar a posição do cabeçalho e do rodapé.
1. Carregue o documento PDF a partir do arquivo de entrada.
1. Itere por todas as páginas do documento.
1. Atribua o cabeçalho e o rodapé a cada página.
1. Salve o PDF modificado no arquivo de saída.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Este método é útil para adicionar títulos consistentes, indicadores de página ou avisos legais na parte superior e inferior de cada página. Você também pode estendê‑lo para incluir imagens ou conteúdo dinâmico, como números de página.

## Adicionando Cabeçalhos e Rodapés para Numeração de Páginas

Adicione numeração automática de páginas aos cabeçalhos e rodapés de um documento PDF usando Aspose.PDF for Python. Usando as variáveis internas $p (número da página atual) e $P (número total de páginas), o script insere dinamicamente a numeração em cada página. Os cabeçalhos exibem o formato 'Page X from Y', enquanto os rodapés mostram 'Page X / Y'. O [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) garante o posicionamento adequado em cada página.

1. Crie um TextFragment para o cabeçalho usando "Page $p from $P" para mostrar a página atual e o total.
1. Crie um objeto HeaderFooter e adicione o texto do cabeçalho a ele.
1. Crie um TextFragment para o rodapé usando "Page $p / $P" como estilo de numeração alternativo.
1. Crie um objeto Footer e adicione o texto do rodapé.
1. Defina as configurações de margem (esquerda = 50, superior = 20) e aplique‑as tanto ao cabeçalho quanto ao rodapé.
1. Abra o documento PDF a partir do arquivo de entrada.
1. Percorra todas as páginas e atribua o cabeçalho e o rodapé a cada uma.
1. Salve o PDF atualizado no caminho de saída.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Adicionando Cabeçalhos e Rodapés como Fragmentos HTML

Aplique cabeçalhos e rodapés formatados em HTML a cada página de um documento PDF usando Aspose.PDF for Python. Ao usar [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), o script permite que estilos de texto avançados — como negrito e itálico — apareçam no cabeçalho e no rodapé. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) é aplicado para posicionamento adequado, e os mesmos elementos formatados são anexados a cada página do documento.

O trecho de código a seguir demonstra como adicionar cabeçalhos e rodapés como fragmentos HTML a um PDF usando Python:

1. Crie um fragmento de cabeçalho HTML usando HtmlFragment — incluindo texto formatado como '<strong>' para negrito.
1. Crie um objeto HeaderFooter e adicione o cabeçalho HTML a ele.
1. Crie um fragmento de rodapé HTML usando '<i>' para estilo itálico.
1. Crie um objeto Footer e adicione o HTML do rodapé.
1. Configure as margens (esquerda = 50, superior = 20) e atribua‑as tanto ao cabeçalho quanto ao rodapé.
1. Carregue o documento PDF usando 'ap.Document()'.
1. Percorra todas as páginas e atribua o cabeçalho e o rodapé a cada uma.
1. Salve o PDF modificado no caminho de saída especificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Usar HtmlFragment permite formatação rica com estilos embutidos ou marcação HTML, proporcionando mais flexibilidade de design em comparação ao texto simples.

## Adicionando Cabeçalhos e Rodapés como Imagens

Adicione cabeçalhos e rodapés baseados em imagem a cada página de um documento PDF usando Aspose.PDF for Python. O mesmo arquivo de imagem é usado tanto para o cabeçalho quanto para o rodapé em todas as páginas. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) posiciona as imagens, e a imagem ajusta‑se automaticamente para caber na área de cabeçalho/rodapé.

O trecho de código a seguir demonstra como adicionar cabeçalhos e rodapés como imagens a um PDF usando Python:

1. Carregue a imagem em um objeto 'ap.Image' e prepare-a para uso como cabeçalho.
1. Crie um objeto HeaderFooter e anexe a imagem do cabeçalho a ele.
1. Carregue a mesma imagem novamente para uso como rodapé.
1. Crie um objeto Footer e adicione a imagem do rodapé a ele.
1. Carregue o documento PDF de entrada usando 'ap.Document()'.
1. Itere por todas as páginas do documento.
1. Aplique margens (esquerda = 50) para posicionar tanto o cabeçalho quanto o rodapé.
1. Atribua o cabeçalho e o rodapé a cada página do PDF.
1. Salve o PDF atualizado no arquivo de saída especificado.

Esta técnica é ideal para marcar documentos com logotipos ou marcas d'água na área de cabeçalho/rodapé.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Adicionando Cabeçalhos e Rodapés como Tabela

Adicione cabeçalhos e rodapés estruturados, baseados em tabelas, a todas as páginas de um documento PDF usando Aspose.PDF para Python. Objetos [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) fornecem melhor controle de layout, alinhamento e formatação consistente para cabeçalhos e rodapés complexos. O texto do cabeçalho é centralizado enquanto o texto do rodapé é alinhado à esquerda, ambos usando fonte Arial 12pt. As larguras das colunas são calculadas dinamicamente com base nas dimensões da página para garantir o posicionamento adequado.

Este trecho de código adiciona cabeçalhos e rodapés (usando tabelas) a cada página de um documento PDF com Aspose.PDF para Python via .NET.

1. Defina estilos de texto usando [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) para cabeçalho e rodapé (fonte, tamanho, alinhamento).
1. Crie objetos [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) para o cabeçalho e o rodapé.
1. Construa a [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) de cabeçalho com uma única linha e uma célula contendo o texto do cabeçalho.
1. Construa a [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) de rodapé com uma única linha e uma célula contendo o texto do rodapé.
1. Adicione as tabelas aos objetos [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) correspondentes.
1. Defina o [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) do rodapé para posicionamento horizontal adequado.
1. Abra o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando os métodos apropriados.
1. Itere por todas as páginas e atribua o cabeçalho e rodapé baseados em tabela a cada página.
1. Salve o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado no arquivo de saída.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Adicionando Cabeçalhos e Rodapés como LaTeX

Adicione cabeçalhos e rodapés contendo conteúdo formatado em LaTeX a todas as páginas de um documento PDF usando Aspose.PDF para Python. LaTeX permite a renderização de símbolos matemáticos, datas, marcas de direitos autorais e outras formatações avançadas. O cabeçalho inclui uma data dinâmica, enquanto o rodapé exibe um símbolo de direitos autorais juntamente com o número da página atual e o total de páginas.

O trecho de código a seguir mostra como usar [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) em cabeçalhos e rodapés de um PDF usando Aspose.PDF para Python via .NET.

1. Abra o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando os métodos apropriados.
1. Determine o total de páginas para usar em rodapés dinâmicos.
1. Itere por todas as páginas do documento.
1. Crie um objeto [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) para o cabeçalho.
1. Crie um [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para o texto do cabeçalho contendo comandos LaTeX (por exemplo, `\\today\\`).
1. Crie um objeto [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) para o rodapé.
1. Crie um [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) para o texto do rodapé incluindo símbolos LaTeX e numeração de páginas.
1. Adicione o [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) ao objeto de cabeçalho/rodapé correspondente.
1. Vincule o cabeçalho e o rodapé à página atual.
1. Salve o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado no arquivo de saída.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```
