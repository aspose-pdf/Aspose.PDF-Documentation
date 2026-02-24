---
title: Formatação de Texto em PDF usando Python
linktitle: Formatação de Texto em PDF
type: docs
weight: 70
url: /pt/python-net/text-formatting-inside-pdf/
description: Explore opções de formatação de texto em arquivos PDF em Python usando Aspose.PDF para estilos de documento personalizados.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como editar Texto em PDF com Python
Abstract: O artigo fornece um guia abrangente sobre várias técnicas de formatação de texto em documentos PDF usando Aspose.PDF para Python via .NET. Ele cobre uma gama de funcionalidades incluindo adição de recuo de linha, criação de bordas de texto, sublinhar texto e adicionar texto tachado, entre outros.
---

## Espaçamento de Linha e Caracteres

### Usando Espaçamento de Linha

#### Como formatar texto com espaçamento de linha personalizado em Python - Caso simples

Aspose.PDF para Python ilustra uma abordagem simples para controlar o layout e a legibilidade do texto por meio de ajustes de espaçamento de linha.

Nosso trecho de código mostra como controlar o espaçamento de linha em um documento PDF. Ele lê texto de um arquivo (ou usa uma mensagem alternativa), aplica tamanho de fonte e espaçamento de linha personalizados, e adiciona o texto formatado a uma nova página em um PDF.

1. Crie um novo documento PDF.
1. Carregue o texto fonte.
1. Inicialize um objeto TextFragment e atribua a ele o texto carregado.
1. Defina as propriedades de fonte e espaçamento para o texto. Esses valores determinam o quão apertadas ou espaçadas as linhas de texto aparecem:
- Tamanho da fonte: 12 pontos
- Espaçamento de linha: 16 pontos
1. Insira o fragmento de texto formatado na coleção de parágrafos da página.
1. Salve o documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_simple_case(outfile):
    """
    Specify custom line spacing for text in a PDF document.

    Creates a PDF document with text that has custom line spacing applied.
    Loads text content from an external file and applies 16-point line spacing
    to improve readability and text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Font size: 12 points
        - Line spacing: 16 points (increased from default for better readability)
        - Demonstrates basic line spacing control in PDF text formatting

    Example:
        >>> specify_line_spacing_simple_case("line_spacing.pdf")
        # Creates a PDF with custom 16-point line spacing
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Como formatar texto com espaçamento de linha personalizado em Python - Caso específico

Vamos verificar como aplicar diferentes modos de espaçamento de linha em um documento PDF usando uma fonte TrueType (TTF) personalizada.
Ele carrega texto de um arquivo, incorpora uma fonte específica e renderiza o mesmo texto duas vezes em uma página PDF — cada vez usando um modo de espaçamento de linha diferente:

- modo FONT_SIZE: O espaçamento de linha equivale ao tamanho da fonte.
- modo FULL_SIZE: O espaçamento de linha considera a altura total da fonte, incluindo ascendentes e descendentes.

O exemplo mostra como o comportamento do espaçamento de linha pode variar dependendo do modo selecionado.

1. Crie um novo documento PDF.
1. Especifique os caminhos para o arquivo de fonte personalizada e o arquivo de origem do texto.
1. Carregue o conteúdo do texto.
1. Abra a fonte personalizada.
1. Crie e configure o primeiro TextFragment (modo FONT_SIZE). Defina line_spacing para 'TextFormattingOptions.LineSpacingMode.FONT_SIZE', indicando que o espaçamento de linha equivale ao tamanho da fonte.
1. Crie e configure o segundo TextFragment (modo FULL_SIZE). Defina line_spacing para 'TextFormattingOptions.LineSpacingMode.FULL_SIZE', que utiliza a altura total da fonte.
1. Anexe ambos os fragmentos de texto à mesma página PDF.
1. Salve o documento final no local de saída especificado.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_specific_case(outfile):
    """
    Create a PDF document demonstrating different line spacing modes with custom font.
    This function creates a PDF with two text fragments using the same custom TTF font
    but different line spacing modes to demonstrate the visual differences between
    FONT_SIZE and FULL_SIZE line spacing options.
    Args:
        outfile (str): Path where the output PDF file will be saved.
    Notes:
        - Requires 'HPSimplified.ttf' font file in DATA_DIR
        - Requires 'lorem.txt' text file in DATA_DIR for content
        - Falls back to default text if lorem.txt is not found
        - First fragment uses FONT_SIZE line spacing mode
        - Second fragment uses FULL_SIZE line spacing mode
    Dependencies:
        - aspose.pdf (ap) library
        - os module for file path operations
        - DATA_DIR constant must be defined
    """

    document = ap.Document()
    page = document.pages.add()

    font_file = os.path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![Documento PDF exibindo texto com espaçamento de linha personalizado demonstrando espaçamento de 16 pontos entre linhas para melhorar a legibilidade e a formatação do layout de texto](line_spacing.png)

### Usando Espaçamento de Caracteres

#### Como controlar o espaçamento de caracteres em texto PDF usando a classe TextFragment

O espaçamento de caracteres determina a distância entre caracteres individuais em uma linha de texto — útil para ajustar finamente a aparência do texto ou alcançar efeitos tipográficos específicos.

1. Inicializa um novo objeto Document e adiciona uma página em branco para inserir texto.
1. Define o Fragment Generator. Implementa uma função auxiliar make_fragment(spacing):
- cria um TextFragment com o texto de exemplo.
- define a fonte.
1. Adicione fragmentos de texto com diferentes valores de espaçamento.
1. Salve o Document.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_fragment(outfile):
    """
    Demonstrate character spacing control using TextFragment objects.

    Creates a PDF document showing different character spacing values applied
    to text fragments. Each line demonstrates progressively increased character
    spacing to illustrate the visual effect on text appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates multiple TextFragment objects with varying character spacing
        - Character spacing values: 0, 1, 2, 3, and 4 points
        - Font: Times Roman, 12 points
        - Each fragment is positioned on a new line for comparison
        - Character spacing affects only horizontal letter spacing
        - Higher values create more space between individual characters

    Example:
        >>> character_spacing_using_text_fragment("char_spacing_fragment.pdf")
        # Creates a PDF showing progressive character spacing effects
    """
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![Documento PDF exibindo três linhas de texto idêntico Sample Text com espaçamento de caracteres demonstrando espaçamento progressivamente mais apertado de cima para baixo, com a primeira linha tendo espaçamento maior entre as letras, a linha do meio tendo espaçamento moderado e a linha inferior tendo o espaçamento mais próximo, ilustrando o efeito visual de diferentes valores de espaçamento de caracteres na formatação de texto PDF](character_spacing_simple.png)

#### Como controlar o espaçamento de caracteres no texto PDF usando TextParagraph e TextBuilder

Aspose.PDF permite aplicar espaçamento de caracteres personalizado ao adicionar texto a um documento PDF usando um TextParagraph e TextBuilder.
Ele define uma área específica na página, configura a quebra de texto e renderiza um fragmento de texto com espaçamento ajustado entre os caracteres.

Usar TextParagraph é ideal quando você precisa de controle preciso sobre a colocação e o layout do texto, como ao criar blocos de texto estruturados ou em múltiplas colunas.

1. Crie um novo documento PDF.
1. Inicialize uma instância de TextBuilder para a página.
1. Crie e configure um TextParagraph.
- Defina o modo de quebra de palavras para 'TextFormattingOptions.WordWrapMode.BY_WORDS'.
1. Crie um TextFragment com espaçamento de caracteres personalizado.
- Crie um novo TextFragment e defina seu texto (ex., "Sample Text with character spacing").
- Especifique atributos de fonte como Arial e tamanho de fonte 14 pt.
- Aplique espaçamento de caracteres = 2.0, que aumenta o espaço entre os caracteres.
1. Adicione o TextFragment ao TextParagraph.
1. Adicione o TextParagraph à página.
1. Salve o documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_paragraph(outfile):
    """
    Demonstrate character spacing control using TextParagraph objects.

    Creates a PDF document with text paragraph that has custom character spacing
    applied. Shows how to set character spacing at the paragraph level and
    demonstrates the visual effect on text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses TextParagraph for paragraph-level formatting
        - Character spacing: 2.0 points
        - Font: Times Roman, 12 points
        - Demonstrates paragraph-based character spacing control
        - Character spacing applies to all text within the paragraph
        - Alternative approach to fragment-based character spacing

    Example:
        >>> character_spacing_using_text_paragraph("char_spacing_paragraph.pdf")
        # Creates a PDF with paragraph-level character spacing
    """
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## Criando Listas

Ao trabalhar com arquivos PDF, pode ser necessário exibir informações estruturadas como listas — seja com marcadores, numeradas ou formatadas com HTML ou LaTeX.
Aspose.PDF for Python via .NET fornece várias maneiras flexíveis de criar e formatar listas diretamente em seus documentos PDF, proporcionando controle total sobre layout, fonte e estilo.

Este artigo demonstra várias abordagens para criar listas em PDFs, desde formatação em texto simples até renderização avançada de HTML e LaTeX. Cada método atende a um caso de uso específico — seja você quem prefere controle programático preciso ou estilização conveniente baseada em marcação.

Ao final deste artigo, você saberá como:

- Criar listas personalizadas com marcadores e numeradas usando TextParagraph e TextBuilder.

- Usar fragmentos HTML (HtmlFragment) para renderizar facilmente listas '<ul>' e '<ol>' em PDFs.

- Aproveitar fragmentos LaTeX (TeXFragment) para formatação de listas matemáticas ou científicas.

- Controlar a quebra de texto, estilos de fonte e posicionamento de layout dentro de uma página.

- Entender a diferença entre construção manual de listas e abordagens dirigidas por marcação.

### Criar uma lista com marcadores

Crie uma lista personalizada com marcadores em um PDF usando TextParagraph e TextBuilder, sem depender de formatação HTML ou LaTeX.
Cada item da lista é prefixado com um caractere de marcador (•) e adicionado como um TextFragment separado.

1. Inicialize um objeto Document e adicione uma página em branco.
1. Defina uma lista Python de strings que será convertida em marcadores.
1. Crie um TextBuilder e um TextParagraph.
1. Use o 'TextBuilder' para adicionar o parágrafo configurado à página.
1. Salve o documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list(outfile):
    """
    Create a PDF document with a bullet list using plain text formatting.
    This function generates a PDF document containing a bullet list with predefined items.
    The list is formatted with bullet points, uses Times New Roman font, and includes
    text wrapping behavior for longer items.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path.
    Note:
        The bullet list is positioned within a rectangle at coordinates (80, 200, 400, 800)
        and uses word wrapping mode for text formatting.
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Criar uma lista numerada

Crie uma lista numerada (ordenada) personalizada em um PDF usando TextParagraph e TextBuilder, sem depender de formatação HTML ou LaTeX.
Cada item da lista é prefixado com seu número (ex., 1., 2.) e adicionado como um TextFragment separado.

1. Inicialize um objeto Document e adicione uma página em branco.
1. Defina uma lista Python de strings que será convertida em itens de lista numerada.
1. Crie um TextBuilder e um TextParagraph.
1. Adicione cada item como um TextFragment com um número.
1. Use o TextBuilder para adicionar o parágrafo configurado à página.
1. Salve o documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list(outfile):
    """
    Create a numbered list in a PDF document using plain text formatting.
    This function generates a PDF document containing a numbered list with predefined
    items. The list is formatted with Times New Roman font and includes text wrapping
    by words within a specified rectangular area on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path but does
              not return any value.
    Note:
        - Uses Aspose.PDF library (imported as 'ap')
        - List items are hardcoded within the function
        - Font: Times New Roman, size 12
        - Text wrapping: BY_WORDS mode
        - Rectangle bounds: (80, 200, 400, 800)
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Criar uma versão HTML de lista com marcadores

Nossa biblioteca demonstra como criar uma lista com marcadores (não ordenada) em um documento PDF usando fragmentos HTML. Ela converte uma lista Python de strings em um elemento HTML `<ul>` e o insere em uma página PDF como um HtmlFragment. Usar fragmentos HTML permite aproveitar recursos de formatação HTML (como listas, negrito, itálico) diretamente no PDF.

1. Crie um novo documento PDF e adicione uma página.
1. Prepare os itens da lista.
1. Converta a lista para uma lista HTML não ordenada.
- Use a tag `<ul>` para uma lista não ordenada (com marcadores).
- Envolva cada item com tags 'li' usando uma compreensão de lista.
1. Crie um HtmlFragment. Converta a string HTML em um objeto HtmlFragment que pode ser adicionado à página PDF.
1. Insira o HtmlFragment na coleção de parágrafos da página.
1. Salve o documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_html_version(outfile):
    """
    Create a bulleted list using HTML formatting in a PDF document.

    Generates a PDF with an unordered (bulleted) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML list structures directly
    into PDF documents with proper formatting and styling.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ul> and <li> tags for list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering
        - Lists maintain proper bullet formatting and indentation
        - Simpler alternative to manual list creation with TextFragments
        - Supports nested lists and HTML styling if needed

    Example:
        >>> create_bullet_list_html_version("bullet_list_html.pdf")
        # Creates a PDF with HTML-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Lista com marcadores exibida em um documento PDF mostrando quatro itens: Primeiro item da lista, Segundo item com mais texto para demonstrar comportamento de quebra de linha, Terceiro item e Quarto item. Cada item é precedido por um ponto de marcadores padrão e demonstra renderização de lista formatada em HTML dentro da estrutura PDF com recuo e espaçamento adequados](bullet_list_html.png)

### Criar versão HTML de lista numerada

Crie uma lista numerada (ordenada) em um documento PDF usando fragmentos HTML. Ele converte uma lista Python de strings em um elemento HTML `<ol>` e a insere em uma página PDF como um HtmlFragment.

Usar fragmentos HTML permite incorporar recursos de formatação baseados em HTML, como listas numeradas, negrito, itálico e muito mais, diretamente no seu PDF.

1. Crie um novo documento PDF e adicione uma página.
1. Prepare os itens da lista.
1. Converta a lista em uma lista ordenada HTML.
- Use a tag `<ol>` para uma lista numerada.
- Envolva cada item com tags 'li' usando uma list comprehension.
1. Converta a string HTML em um objeto HtmlFragment que pode ser adicionado à página PDF.
1. Insira o HtmlFragment na coleção de parágrafos da página.
1. Salve o documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_html_version(outfile):
    """
    Create a numbered list using HTML formatting in a PDF document.

    Generates a PDF with an ordered (numbered) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML ordered list structures
    directly into PDF documents with automatic numbering and formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ol> and <li> tags for ordered list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering and numbering
        - Lists maintain proper numeric formatting and indentation
        - Numbers are automatically generated (1, 2, 3, etc.)
        - Supports nested lists and custom numbering styles if needed

    Example:
        >>> create_numbered_list_html_version("numbered_list_html.pdf")
        # Creates a PDF with HTML-formatted numbered list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Lista numerada exibida em um documento PDF mostrando quatro itens numerados automaticamente: 1. Primeiro item da lista, 2. Segundo item com mais texto para demonstrar comportamento de quebra de linha, 3. Terceiro item e 4. Quarto item. A lista demonstra renderização de lista ordenada formatada em HTML dentro da estrutura PDF com sequência numérica correta, recuo e espaçamento entre os itens](numbered_list_html.png)

### Criar versão LaTeX de lista com marcadores

Crie uma lista com marcadores (não ordenada) em um PDF usando fragmentos LaTeX (TeXFragment). Ele converte uma lista Python de strings em um ambiente LaTeX itemize e a insere em uma página PDF. Usar fragmentos LaTeX é ideal quando você deseja renderizar fórmulas matemáticas, símbolos ou listas estruturadas com formatação precisa.

1. Crie um novo documento PDF e adicione uma página.
1. Defina uma lista Python de strings que se tornarão marcadores no ambiente LaTeX itemize.
1. Converta a lista em um ambiente LaTeX itemize:
- Envolva os itens com \begin{itemize} e \end{itemize}.
- Cada item é prefixado com \item usando uma list comprehension.
1. Converta a string LaTeX em um objeto TeXFragment que pode ser renderizado no PDF.
1. Adicione o fragmento LaTeX à página.
1. Salve o documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_latex_version(outfile):
    """
    Create a bulleted list using LaTeX formatting in a PDF document.

    Generates a PDF with an unordered list created using LaTeX markup.
    Demonstrates how to use TeXFragment to embed LaTeX itemize environments
    directly into PDF documents with proper mathematical and scientific formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX \\begin{itemize} and \\item commands
        - TeXFragment handles LaTeX compilation and rendering
        - Supports mathematical expressions and scientific notation
        - Lists maintain proper bullet formatting and indentation
        - More powerful than HTML for mathematical content
        - Can include LaTeX math modes and special symbols

    Example:
        >>> create_bullet_list_latex_version("bullet_list_latex.pdf")
        # Creates a PDF with LaTeX-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Lista com marcadores exibida em PDF mostrando formatação renderizada em LaTeX com o texto Listas são fáceis de criar: seguida por quatro itens com marcadores: Primeiro item, Segundo item com mais texto para demonstrar comportamento de quebra de linha, Terceiro item e Quarto item. A lista demonstra tipografia LaTeX profissional com formatação de marcadores adequada, espaçamento consistente e capacidades de quebra de texto dentro de um layout limpo de documento PDF](bullet_list_latex.png)

### Criar versão LaTeX de lista numerada

Crie uma lista numerada (ordenada) em um PDF usando fragmentos LaTeX (TeXFragment). Ele converte uma lista Python de strings em um ambiente LaTeX enumerate e a insere em uma página PDF. Usar fragmentos LaTeX é ideal quando você deseja formatação precisa, listas estruturadas ou notação matemática em PDFs.

1. Crie um novo documento PDF e adicione uma página.
1. Defina uma lista Python de strings que se tornarão itens numerados no ambiente LaTeX enumerate.
1. Converta a lista em um ambiente LaTeX enumerate.
1. Converta a string LaTeX em um objeto TeXFragment que pode ser renderizado no PDF.
1. Adicione o fragmento LaTeX à página.
1. Salve o documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_latex_version(outfile):
    """Create a numbered list using LaTeX."""

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Lista numerada exibida em PDF mostrando formatação renderizada em LaTeX com os itens 1. Primeiro item, 2. Segundo item com mais texto para demonstrar comportamento de quebra de linha, 3. Terceiro item e 4. Quarto item, precedida pelo texto Listas são fáceis de criar](numbered_list_latex.png)

## Notas de rodapé e notas finais

### Adicionar notas de rodapé

Notas de rodapé são usadas para referenciar notas dentro do corpo de um documento colocando números sobrescritos consecutivos ao lado do texto relevante. Esses números correspondem a notas detalhadas que normalmente são recuadas e posicionadas na parte inferior da mesma página, fornecendo contexto adicional, citações ou comentários.

Adicione uma nota de rodapé a um fragmento de texto em um documento PDF usando Aspose.PDF para Python via .NET. Notas de rodapé são úteis para fornecer informações suplementares, citações ou esclarecimentos sem bagunçar o conteúdo principal. Este método garante que as notas de rodapé sejam integradas visual e estruturalmente ao layout do PDF.

1. Crie um novo documento.
1. Crie um TextFragment com o conteúdo principal.
1. Adicione texto em linha. Crie outro TextFragment que continua no mesmo parágrafo.
1. Salve o documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote(outfile):
    """Add footnote to a PDF document."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### Adicionar nota de rodapé com estilo personalizado no PDF

1. Inicialize um novo documento PDF e adicione uma página em branco.
1. Crie o fragmento de texto principal.
1. Crie e estilize a nota de rodapé (fonte, tamanho, cor, estilo).
1. Insira o fragmento de texto estilizado com a nota de rodapé na página.
1. Adicione outro fragmento de texto sem nota de rodapé.
1. Salve o Documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text_style(outfile):
    """Add footnote with custom text style."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### Adicionar Notas de Rodapé com Símbolos Personalizados em PDF

Adicionar notas de rodapé a fragmentos de texto em um documento PDF usando Aspose.PDF for Python via .NET, com a capacidade de personalizar o símbolo do marcador da nota de rodapé.

1. Crie o Documento PDF e a Página.
1. Adicione o primeiro Fragmento de Texto com Símbolo de Nota de Rodapé Personalizado.
1. Adicione outro Fragmento de Texto que continua o parágrafo sem uma nota de rodapé.
1. Adicione o segundo Fragmento de Texto com Nota de Rodapé Padrão.
1. Salve o Documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text(outfile):
    """
    Add footnote with custom text marker to a PDF document.
    Creates a PDF document with text fragments that include footnotes with custom
    styling. The function demonstrates how to add footnotes with custom text markers
    and standard footnotes to different text fragments within the same document.
    Args:
        outfile (str): The output file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        add_footnote_custom_text("output_with_footnotes.pdf")
    Note:
        The document will contain:
        - Text with a custom footnote marker ("*")
        - Text without footnotes
        - Text with a standard footnote
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### Adicionar Notas de Rodapé com Estilo de Linha Personalizado em PDF

Personalize a aparência visual das linhas de notas de rodapé em um documento PDF com a biblioteca Python. Personalizar as linhas de notas de rodapé melhora a clareza visual e permite consistência estilística em documentos como relatórios, trabalhos acadêmicos e publicações anotadas.

1. Crie um novo documento PDF e adicione uma página.
1. Defina um estilo de linha personalizado para os conectores de notas de rodapé (cor, largura e padrão de traço).
1. Adicione vários fragmentos de texto com notas de rodapé.
1. Salve o documento final.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_custom_line_style(outfile):
    """
    Add footnotes with custom line style to a PDF document.
    Creates a PDF document with text fragments that have footnotes and applies
    a custom line style for the footnote separator line. The custom style includes
    red color, increased line width, and dashed pattern.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_footnote_with_custom_line_style("output.pdf")
        # Creates a PDF with footnoted text and custom separator line styling
    """

    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Adicionar Notas de Rodapé com Imagem e Tabela em PDF

Como enriquecer notas de rodapé em um documento PDF incorporando imagens, texto formatado e tabelas usando Aspose.PDF for Python via .NET?

1. Crie um novo documento PDF e adicione uma página.
1. Adicione um fragmento de texto com uma nota de rodapé anexada.
1. Incorpore uma imagem, texto formatado e uma tabela dentro da nota de rodapé.
1. Salve o Documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_image_and_table(outfile):
    """
    Add a footnote containing an image and table to a PDF document.
    Creates a new PDF document with sample text that includes a footnote. The footnote
    contains three elements: an image (logo.jpg), descriptive text, and a simple table
    with two cells. The image is resized to 20x20 pixels and the footnote text uses
    a 20pt font size.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Note:
        - Requires the logo.jpg file to be present in the DATA_DIR directory
        - Uses the Aspose.PDF library (imported as 'ap')
        - The footnote is attached to the main text fragment on the page
    """

    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = os.path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### Adicionando Notas de Fim a Documentos PDF

Uma Nota de Fim é um tipo de citação que direciona os leitores a uma seção designada ao final de um documento, onde podem encontrar a referência completa de uma citação, ideia parafraseada ou conteúdo resumido. Ao usar notas de fim, um número sobrescrito é colocado imediatamente após o material referenciado, guiando o leitor para a nota correspondente ao final do texto.

Este trecho de código demonstra como adicionar uma nota de fim a um fragmento de texto em um documento PDF. Ao contrário das notas de rodapé, que aparecem próximas ao texto referenciado, as notas de fim geralmente são colocadas ao final de um documento ou seção. Este método também simula um documento mais longo para ilustrar como as notas de fim se comportam em conteúdo extenso.

1. Crie o Documento PDF e a Página.
1. Adicione um Fragmento de Texto com Nota de Fim.
1. Carregue Conteúdo de Texto Externo.
1. Simule um Documento Longo. Adicione o texto carregado várias vezes para simular um documento mais extenso.
1. Salve o Documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote(outfile):
    """Add endnote to a PDF document.
    Creates a new PDF document with a text fragment containing an endnote,
    followed by additional lorem ipsum content to simulate a longer document.
    The endnote is attached to the first text fragment and will be displayed
    according to the PDF viewer's endnote handling.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        This function requires the aspose-pdf library and assumes the existence
        of a DATA_DIR variable pointing to a directory containing 'lorem.txt'.
        If the lorem.txt file is not found, fallback text will be used.
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Adicionar Notas de Fim com Texto de Marcador Personalizado em PDF

Adicione uma nota de fim a um fragmento de texto em um documento PDF, com um símbolo de marcador personalizado (ex.: "***"). As notas de fim são tipicamente colocadas ao final de um documento ou seção e são úteis para fornecer contexto adicional, citações ou comentários.

1. Crie o Documento PDF e a Página.
1. Adicione um fragmento de texto formatado com uma nota de fim.
1. Personalize o texto do marcador da nota de fim.
1. Carregue conteúdo externo de um arquivo .txt.
1. Simule conteúdo extenso para ilustrar a colocação da nota de fim.
1. Salve o documento PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote_custom_text(outfile):
    """
    Add endnote with custom text marker to a PDF document.
    Creates a PDF document with a text fragment that contains an endnote with
    a custom marker ("***"). The document is populated with sample text content
    from a lorem.txt file, repeated multiple times to simulate a longer document.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires lorem.txt file in DATA_DIR for sample content
        - Falls back to default text if lorem.txt is not found
        - Uses Arial font with 14pt size for all text elements
        - The endnote marker is set to "***" instead of default numbering
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## Layout e controle de página

### Forçar uma Tabela a Iniciar em uma Nova Página em PDF

Adicione conteúdo específico para iniciar em uma nova página em um documento PDF usando Aspose.PDF for Python via .NET.
Ao definir a propriedade 'is_in_new_page', você pode controlar com precisão o layout e a estrutura da página, garantindo que seções específicas (como tabelas, relatórios ou resumos) sempre comecem em uma nova página — ideal para formatação de documentos, relatórios prontos para impressão ou geração de saída organizada.

1. Crie e configure uma tabela.
1. Adicione dados à tabela.
1. Force uma nova página para a tabela. Isso garante que a tabela inicie no topo de uma nova página, mesmo que haja conteúdo existente na atual.
1. Adicione a tabela à página. Use 'page.paragraphs.add()' para incluir a tabela no layout do PDF.
1. Salve o documento.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def force_new_page(output_file_name):
    """
    Create a PDF document demonstrating forced page breaks with tables.

    Creates a PDF document with a table that is forced to start on a new page
    using the is_in_new_page property. This is useful for controlling page layout
    and ensuring specific content starts on fresh pages.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates a 3-column table with 5 rows of sample data
        - Table uses uniform column widths of 150 units each
        - All cells have borders for clear visual separation
        - is_in_new_page=True forces the table to start on a new page
        - Useful for reports, documents with sections, or content organization

    Example:
        >>> force_new_page("new_page_table.pdf")
        # Creates a PDF with a table that starts on a new page
    """
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### Usando a Propriedade de Parágrafo Inline em PDF

Nossa biblioteca permite que você use a propriedade 'is_in_line_paragraph' para controlar o fluxo inline entre texto e imagens dentro de um PDF.
Normalmente, ao adicionar novos elementos (como fragmentos de texto ou imagens), cada um começa em uma nova linha ou novo parágrafo.
Ao definir 'is_in_line_paragraph = True', você pode fazer com que os elementos apareçam na mesma linha ou dentro do mesmo parágrafo, criando layouts inline suaves — perfeito para combinar texto e imagens inline, como adicionar logos, ícones ou símbolos dentro de frases.

O primeiro fragmento de texto, a imagem e o segundo fragmento de texto aparecem na mesma linha, formando um parágrafo inline contínuo.
O terceiro fragmento de texto inicia um novo parágrafo, demonstrando o comportamento padrão de quebra de linha.

1. Crie um novo documento PDF.
1. Adicione o primeiro fragmento de texto.
1. Insira uma imagem embutida.
1. Adicione mais texto embutido.
1. Adicione um novo parágrafo.
1. Salve o PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def using_inline_paragraph_property(output_file_name):
    """
    Demonstrate inline paragraph behavior in PDF document layout.

    Creates a PDF document showing how the is_in_line_paragraph property affects
    the flow of text and images. Elements with this property continue the flow
    of the previous paragraph instead of starting a new one.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - First text fragment starts a new paragraph
        - Image with is_in_line_paragraph=True continues the same line
        - Second text fragment also continues the same paragraph line
        - Third text fragment starts a new paragraph (default behavior)
        - Demonstrates inline flow control for mixed content (text + images)
        - Image is resized to 30x30 pixels and flows inline with text

    Example:
        >>> using_inline_paragraph_property("inline_paragraph.pdf")
        # Creates a PDF demonstrating inline paragraph flow
    """
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = os.path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### Criar um PDF de Múltiplas Colunas

Crie um layout de jornal em múltiplas colunas em um PDF usando Aspose.PDF para Python via .NET.
Ele demonstra como combinar texto, formatação HTML e gráficos dentro de um FloatingBox, permitindo controle avançado de layout semelhante a designs de revistas ou boletins de várias colunas.

1. Inicialize o documento PDF.
1. Adicione uma linha separadora horizontal no topo.
1. Adicione um cabeçalho HTML estilizado.
1. Crie o FloatingBox para controle de layout.
1. Configure o layout de múltiplas colunas.
1. Adicione informações do autor.
1. Desenhe outra linha horizontal interna.
1. Adicione o texto do artigo.
1. Salve o PDF final.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_multi_column_pdf(output_file_name):
    """
    Create a PDF document with multi-column layout using FloatingBox.

    Creates a professional-looking PDF with a multi-column newspaper-style layout.
    Demonstrates advanced layout techniques including floating boxes, column
    configuration, and mixed content with graphics and text.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Document margins: 40 points left and right
        - Top horizontal line for visual separation
        - HTML-formatted heading with custom styling
        - FloatingBox with 2-column layout (105 units wide each)
        - Column spacing: 5 units between columns
        - Includes author attribution with italic styling
        - Internal horizontal line within the floating box
        - Long text content automatically flows between columns
        - Demonstrates professional document layout techniques

    Example:
        >>> create_multi_column_pdf("multi_column_layout.pdf")
        # Creates a PDF with newspaper-style multi-column layout
    """
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    lorem_text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Paradas de Tabulação Personalizadas para Alinhamento de Texto em PDF

Crie um layout de texto semelhante a uma tabela em um PDF usando paradas de tabulação personalizadas — sem depender de estruturas de tabela.
Ao definir posições de paradas de tabulação, alinhamentos e estilos de líder, você pode alinhar o texto com precisão entre colunas. Isso é útil para faturas, relatórios ou dados de texto estruturados.

1. Crie um novo documento PDF.
1. Defina paradas de tabulação personalizadas.
1. Use marcadores #$TAB no texto.
1. Adicione texto ao PDF.
1. Salve o PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def custom_tab_stops(output_file_name):
    """
    Create a PDF document demonstrating custom tab stops for table-like formatting.

    Creates a PDF document that uses custom tab stops to format text in a table-like
    structure without using actual table elements. This demonstrates advanced text
    formatting with precise positioning and leader styles.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Tab stop 1: Position 100, right-aligned, solid leader line
        - Tab stop 2: Position 200, center-aligned, dashed leader line
        - Tab stop 3: Position 300, left-aligned, dotted leader line
        - Uses #$TAB placeholder for tab positions in text
        - Creates table-like structure with headers and data rows
        - Demonstrates mixing TextFragment and TextSegment approaches
        - Leader lines provide visual guides between columns
        - Alternative to HTML tables for precise text positioning

    Example:
        >>> custom_tab_stops("custom_tabs.pdf")
        # Creates a PDF with custom tab stop formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```
