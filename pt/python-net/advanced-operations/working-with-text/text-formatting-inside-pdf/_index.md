---
title: Formatar texto PDF em Python
linktitle: Formatar texto PDF em Python
type: docs
weight: 70
url: /python-net/text-formatting-inside-pdf/
description: Aprenda a formatar texto em documentos PDF em Python utilizando espaçamento, margens, avanço e opções de estilo.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formate e estilize texto em ficheiros PDF com Python.
Abstract: Este artigo explica como formatar texto em documentos PDF utilizando o Aspose.PDF para Python via .NET. Aprenda a controlar o espaçamento, o avanço, as margens, os sublinhados, os efeitos de tachado e outras opções de estilo de texto em Python.
---

## Espaçamento entre linhas e caracteres

### Utilização do espaçamento entre linhas

#### Como formatar texto com espaçamento entre linhas personalizado em Python - Caso simples

O Aspose.PDF for Python oferece uma abordagem direta para controlar o layout e a legibilidade do texto através de ajustes de espaçamento entre linhas.

O nosso excerto de código mostra como controlar o espaçamento entre linhas num documento PDF. Lê o texto de um ficheiro (ou utiliza uma mensagem de fallback), aplica o tamanho de letra e o espaçamento entre linhas personalizados e adiciona o texto formatado a uma nova página PDF.

1. Crie um novo documento PDF.
1. Carregue o texto de partida.
1. Inicialize um objeto TextFragment e atribua-lhe o texto carregado.
1. Defina as propriedades de tipo de letra e espaçamento para o texto. Estes valores determinam o quão estreitas ou espaçadas as linhas de texto aparecem:
    - Tamanho da letra: 12 pontos
    - Espaçamento entre linhas: 16 pontos
1. Insira o fragmento de texto formatado na coleção de parágrafos da página.
1. Guarde o documento.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_simple_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Como formatar texto com espaçamento entre linhas personalizado em Python - Caso específico

Vamos ver como aplicar diferentes modos de espaçamento entre linhas num documento PDF utilizando uma fonte TrueType (TTF) personalizada.
It loads text from a file, embeds a specific font, and renders the same text twice on a PDF page—each time using a different line spacing mode:

- FONT_SIZE mode: The line spacing equals the font size.
- FULL_SIZE mode: The line spacing accounts for the full height of the font, including ascenders and descenders.

O exemplo mostra como o comportamento do espaçamento entre linhas pode variar consoante o modo selecionado.

1. Create a new PDF document.
1. Specify the paths for both the custom font file and the text source file.
1. Load text content.
1. Open the custom font.
1. Create and configure the first TextFragment (FONT_SIZE mode). Set line_spacing to 'TextFormattingOptions.LineSpacingMode.FONT_SIZE', meaning line spacing equals the font size.
1. Create and configure the second TextFragment (FULL_SIZE mode). Set line_spacing to 'TextFormattingOptions.LineSpacingMode.FULL_SIZE', which uses the font’s full height.
1. Append both text fragments to the same PDF page.
1. Save the finished document to the specified output location.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_specific_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    font_file = path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

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

![PDF document displaying text with custom line spacing demonstrating 16-point spacing between lines for improved readability and text layout formatting](line_spacing.png)

### Utilização do espaçamento entre caracteres

#### Como controlar o espaçamento entre caracteres em texto PDF utilizando a classe TextFragment

O espaçamento entre caracteres determina a distância entre caracteres individuais numa linha de texto, sendo útil para ajustar o aspeto do texto com precisão ou obter efeitos tipográficos específicos.

1. Initializes a new Document object and adds a blank page for placing text.
1. Define Fragment Generator. Implements a helper function make_fragment(spacing):
    - create a TextFragment with the sample text.
    - set the font.
1. Add text fragments with different spacing values.
1. Save the Document.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_fragment(outfile):
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

![PDF document displaying three lines of identical text Sample Text with character spacing demonstrating progressively tighter character spacing from top to bottom, with the first line having wider spacing between letters, the middle line having moderate spacing, and the bottom line having the closest character spacing, illustrating the visual effect of different character spacing values in PDF text formatting](character_spacing_simple.png)

#### Como controlar o espaçamento entre caracteres em texto PDF utilizando TextParagraph e TextBuilder

O Aspose.PDF permite aplicar espaçamento personalizado entre caracteres ao adicionar texto a um documento PDF utilizando `TextParagraph` e `TextBuilder`.
O exemplo define uma área específica na página, configura a quebra de texto e apresenta um fragmento de texto com espaçamento ajustado entre os caracteres.

Utilizar `TextParagraph` é ideal quando precisa de controlo preciso sobre a colocação e o layout do texto, por exemplo ao construir blocos de texto estruturados ou com várias colunas.

1. Create a new PDF document.
1. Initialize a TextBuilder instance for the page.
1. Create and configure a TextParagraph.
    - Set the word wrap mode to 'TextFormattingOptions.WordWrapMode.BY_WORDS'.
1. Create a TextFragment with custom character spacing.
    - Create a new TextFragment and set its text (e.g., "Sample Text with character spacing").
    - Specify font attributes such as Arial and font size 14 pt.
    - Apply character spacing = 2.0, which increases the space between characters.
1. Add the TextFragment to the TextParagraph.
1. Add the TextParagraph to the page.
1. Save the PDF document.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_paragraph(outfile):
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

## Criar listas

Ao trabalhar com ficheiros PDF, pode precisar de apresentar informações estruturadas, como listas, quer sejam com marcadores, numeradas ou formatadas com HTML ou LaTeX.
O Aspose.PDF for Python via .NET oferece várias formas flexíveis de criar e formatar listas diretamente nos seus documentos PDF, permitindo controlo total sobre layout, fonte e estilo.

Este artigo demonstra várias abordagens para criar listas em PDFs, desde formatação em texto simples até renderização avançada com HTML e LaTeX. Cada método atende a um caso de uso específico, quer prefira controlo programático preciso, quer um estilo conveniente baseado em marcação.

No final deste artigo, saberá como:

- Criar listas personalizadas com marcadores e listas numeradas utilizando `TextParagraph` e `TextBuilder`.

- Utilizar fragmentos HTML (`HtmlFragment`) para renderizar facilmente listas `<ul>` e `<ol>` em PDFs.

- Tirar partido de fragmentos LaTeX (`TeXFragment`) para formatação de listas matemáticas ou científicas.

- Controlar a quebra de texto, os estilos de fonte e o posicionamento do layout dentro de uma página.

- Compreender a diferença entre a construção manual de listas e as abordagens orientadas por marcação.

### Criar lista numerada

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list(outfile):
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

### Criar lista com marcadores

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list(outfile):
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

### Criar uma lista numerada em versão HTML

Crie uma lista numerada (ordenada) num documento PDF utilizando fragmentos HTML. O exemplo converte uma lista Python de cadeias de texto num elemento HTML `<ol>` e insere-o numa página PDF como `HtmlFragment`.

Utilizar fragmentos HTML permite incorporar diretamente no PDF funcionalidades de formatação baseadas em HTML, como listas numeradas, negrito, itálico e muito mais.

1. Create a new PDF document and add a page.
1. Prepare the list items.
1. Convert the list to an HTML ordered list.
    - Use the `<ol>` tag for a numbered list.
    - Wrap each item with 'li' tags using a list comprehension.
1. Convert the HTML string into an HtmlFragment object that can be added to the PDF page.
1. Insert the HtmlFragment into the page’s paragraphs collection.
1. Save the PDF document.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_html_version(outfile):
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

![Numbered list displayed in a PDF document showing four automatically numbered items: 1. First item in the list, 2. Second item with more text to demonstrate wrapping behavior, 3. Third item, and 4. Fourth item. The list demonstrates HTML-formatted ordered list rendering within PDF structure with proper numeric sequencing, indentation, and spacing between items](numbered_list_html.png)

### Criar uma lista com marcadores em versão HTML

A nossa biblioteca mostra como criar uma lista com marcadores (não ordenada) num documento PDF utilizando fragmentos HTML. O exemplo converte uma lista Python de cadeias de texto num elemento HTML `<ul>` e insere-o numa página PDF como `HtmlFragment`. Utilizar fragmentos HTML permite aproveitar diretamente no PDF recursos de formatação HTML, como listas, negrito e itálico.

1. Create a new PDF document and add a page.
1. Prepare the list items.
1. Convert the list to an HTML unordered list.
    - Use the `<ul>` tag for an unordered (bulleted) list.
    - Wrap each item with 'li' tags using a list comprehension.
1. Create an HtmlFragment. Convert the HTML string into an HtmlFragment object that can be added to the PDF page.
1. Insert the HtmlFragment into the page’s paragraphs collection.
1. Save the PDF document.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_html_version(outfile):
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

![Bulleted list displayed in a PDF document showing four items: First item in the list, Second item with more text to demonstrate wrapping behavior, Third item, and Fourth item. Each item is preceded by a standard bullet point and demonstrates HTML-formatted list rendering within the PDF structure with proper indentation and spacing](bullet_list_html.png)

### Criar uma lista com marcadores em versão LaTeX

Crie uma lista com marcadores (não ordenada) num PDF utilizando fragmentos LaTeX (`TeXFragment`). O exemplo converte uma lista Python de cadeias de texto num ambiente LaTeX `itemize` e insere-o numa página PDF. Os fragmentos LaTeX são ideais quando pretende renderizar fórmulas matemáticas, símbolos ou listas estruturadas com formatação precisa.

1. Create a new PDF document and add a page.
1. Define a Python list of strings that will become bullet points in the LaTeX itemize environment.
1. Convert the list into a LaTeX itemize environment:
    - Wrap the items with \begin{itemize} and \end{itemize}.
    - Each item is prefixed with \item using a list comprehension.
1. Convert the LaTeX string into a TeXFragment object that can be rendered in the PDF.
1. Add the LaTeX fragment to the page.
1. Save the PDF document.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_latex_version(outfile):
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

![Bulleted list displayed in PDF showing LaTeX-rendered formatting with text Lists are easy to create: followed by four bullet-pointed items: First item, Second item with more text to demonstrate wrapping behavior, Third item, and Fourth item. The list demonstrates professional LaTeX typesetting with proper bullet formatting, consistent spacing, and text wrapping capabilities within a clean PDF document layout](bullet_list_latex.png)

### Criar uma lista numerada em versão LaTeX

Crie uma lista numerada (ordenada) num PDF utilizando fragmentos LaTeX (`TeXFragment`). O exemplo converte uma lista Python de cadeias de texto num ambiente LaTeX `enumerate` e insere-o numa página PDF. Os fragmentos LaTeX são ideais quando pretende formatação precisa, listas estruturadas ou notação matemática em PDFs.

1. Create a new PDF document and add a page.
1. Define a Python list of strings that will become numbered items in the LaTeX enumerate environment.
1. Convert the list into a LaTeX enumerate environment.
1. Convert the LaTeX string into a TeXFragment object that can be rendered in the PDF.
1. Add the LaTeX fragment to the page.
1. Save the PDF document.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_latex_version(outfile):
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

![Numbered list displayed in PDF showing LaTeX-rendered formatting with items 1. First item, 2. Second item with more text to demonstrate wrapping behavior, 3. Third item, and 4. Fourth item, preceded by the text Lists are easy to create](numbered_list_latex.png)

## Notas de rodapé e notas finais

### Adicionar notas de rodapé

As notas de rodapé são utilizadas para referenciar anotações no corpo de um documento através da colocação de números sobrescritos junto ao texto relevante. Esses números correspondem a notas detalhadas, normalmente indentadas e posicionadas no rodapé da mesma página, fornecendo contexto adicional, citações ou comentários.

Adicione uma nota de rodapé a um fragmento de texto num documento PDF utilizando Aspose.PDF for Python via .NET. As notas de rodapé são úteis para fornecer informações suplementares, citações ou esclarecimentos sem sobrecarregar o conteúdo principal. Este método garante que as notas de rodapé ficam integradas visual e estruturalmente no layout do PDF.

1. Create a New Document.
1. Create a TextFragment with the main content.
1. Add Inline Text. Create another TextFragment that continues in the same paragraph.
1. Save the Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote(outfile):
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

### Adicionar uma nota de rodapé com estilo personalizado no PDF

1. Initialize a new PDF document and add a blank page.
1. Create Main Text Fragment.
1. Create and Style the Footnote (Font, Size, Color, Style).
1. Insert the styled text fragment with footnote into the page.
1. Add another text fragment without a footnote.
1. Save the Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text_style(outfile):
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

### Adicionar notas de rodapé com símbolos personalizados no PDF

Adicione notas de rodapé a fragmentos de texto num documento PDF utilizando Aspose.PDF for Python via .NET, com a possibilidade de personalizar o símbolo do marcador da nota de rodapé.

1. Create PDF Document and Page.
1. Add first Text Fragment with Custom Footnote Symbol.
1. Add another Text Fragment that continues the paragraph without a footnote.
1. Add second Text Fragment with Default Footnote.
1. Save the Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text(outfile):
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

### Adicionar notas de rodapé com estilo de linha personalizado no PDF

Personalize o aspeto visual das linhas de notas de rodapé num documento PDF com a biblioteca Python. Personalizar essas linhas melhora a clareza visual e permite consistência estilística em documentos como relatórios, artigos académicos e publicações anotadas.

1. Create a new PDF document and add a page.
1. Define a custom line style for footnote connectors (color, width, and dash pattern).
1. Add multiple text fragments with footnotes.
1. Save the final document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_custom_line_style(outfile):
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

### Adicionar notas de rodapé com imagem e tabela no PDF

Como enriquecer notas de rodapé num documento PDF incorporando imagens, texto formatado e tabelas com Aspose.PDF for Python via .NET?

1. Create a new PDF document and add a page.
1. Add a text fragment with an attached footnote.
1. Embed an image, styled text, and a table inside the footnote.
1. Save the Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_image_and_table(outfile):
    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = path.join(DATA_DIR, "logo.jpg")
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

### Adicionar notas finais a documentos PDF

Uma nota final é um tipo de citação que direciona os leitores para uma secção no final do documento, onde podem encontrar a referência completa de uma citação, ideia parafraseada ou conteúdo resumido. Ao utilizar notas finais, é colocado um número sobrescrito imediatamente após o material referenciado, guiando o leitor para a nota correspondente no final do documento.

This code snippet demonstrates how to add an endnote to a text fragment in a PDF document. Unlike footnotes, which appear near the referenced text, endnotes are typically placed at the end of a document or section. This method also simulates a longer document to illustrate how endnotes behave in extended content.

1. Create PDF Document and Page.
1. Add Text Fragment with Endnote.
1. Load External Text Content.
1. Simulate Long Document. Add the loaded text multiple times to simulate a longer document.
1. Save the Document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Adicionar notas finais com texto de marcador personalizado no PDF

Adicione uma nota final a um fragmento de texto num documento PDF com um símbolo de marcador personalizado, por exemplo `"***"`. As notas finais são normalmente colocadas no final de um documento ou secção e são úteis para fornecer contexto adicional, citações ou comentários.

1. Create PDF Document and Page.
1. Add a styled text fragment with an endnote.
1. Customize the endnote marker text.
1. Load external content from a .txt file.
1. Simulate long-form content to illustrate endnote placement.
1. Save the PDF document.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## Controlo de layout e páginas

### Forçar uma tabela a iniciar numa nova página no PDF

Adicione conteúdo específico para começar numa nova página de um documento PDF utilizando Aspose.PDF for Python via .NET.
By setting the property 'is_in_new_page', you can precisely control page layout and structure, ensuring that particular sections (such as tables, reports, or summaries) always begin on a fresh page — ideal for document formatting, print-ready reports, or organized output generation.

1. Create and configure a table.
1. Add data to the table.
1. Force a new page for the table. This ensures that the table starts at the top of a new page, even if there is existing content on the current one.
1. Add the table to the page. Use 'page.paragraphs.add()' to include the table in the PDF layout.
1. Save the document.

```python
import aspose.pdf as ap
import sys
from os import path

def force_new_page(output_file_name):
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

### Utilizar a propriedade de parágrafo inline num PDF

A nossa biblioteca permite utilizar a propriedade `is_in_line_paragraph` para controlar o fluxo inline entre texto e imagens dentro de um PDF.
Normally, when you add new elements (like text fragments or images), each one starts on a new line or new paragraph.
By setting 'is_in_line_paragraph = True', you can make elements appear on the same line or within the same paragraph, creating smooth inline layouts—perfect for combining text and images inline, such as adding logos, icons, or symbols within sentences.

The first text fragment, image, and second text fragment appear on the same line, forming a continuous inline paragraph.
The third text fragment starts a new paragraph, demonstrating the default line-breaking behavior.

1. Create a new PDF document.
1. Add the first text fragment.
1. Insert an inline image.
1. Add more inline text.
1. Add a new paragraph.
1. Save the PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def using_inline_paragraph_property(output_file_name):
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
    image.file = path.join(DATA_DIR, "logo.jpg")
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

### Criar um PDF com várias colunas

Crie um layout em várias colunas, ao estilo de jornal, num PDF utilizando Aspose.PDF for Python via .NET.
It showcases how to combine text, HTML formatting, and graphics within a FloatingBox, enabling advanced layout control similar to multi-column magazine or newsletter designs.

1. Initialize the PDF document.
1. Add a horizontal separator line at the top.
1. Add a styled HTML heading.
1. Create the FloatingBox for layout control.
1. Configure multi-column layout.
1. Add author info.
1. Draw another internal horizontal line.
1. Add the article text.
1. Save the final PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_multi_column_pdf(output_file_name):
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
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            lorem_text = f.read()
    else:
        lorem_text = "Lorem ipsum text not found."
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Tabulações personalizadas para alinhamento de texto em PDF

Crie um layout de texto semelhante a uma tabela num PDF utilizando tabulações personalizadas, sem recorrer a estruturas de tabela.
By defining tab stop positions, alignments, and leader styles, you can align text precisely across columns. This is useful for invoices, reports, or structured text data.

1. Create a new PDF document.
1. Define custom tab stops.
1. Use #$TAB placeholders in text.
1. Add text to the PDF.
1. Save the PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def custom_tab_stops(output_file_name):
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

### Tópicos relacionados com texto

- [Trabalhar com texto em PDF com Python](/pdf/python-net/working-with-text/)
- [Adicionar texto ao PDF](/pdf/python-net/add-text-to-pdf-file/)
- [Rodar texto dentro do PDF com Python](/pdf/python-net/rotate-text-inside-pdf/)
- [Substituir texto em PDF com Python](/pdf/python-net/replace-text-in-pdf/)
