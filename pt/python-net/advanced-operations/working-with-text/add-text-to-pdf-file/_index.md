---
title: Adicionar Texto ao PDF
linktitle: Adicionar Texto ao PDF
type: docs
weight: 10
url: /pt/python-net/add-text-to-pdf-file/
description: Este artigo descreve vários aspectos de trabalhar com texto no Aspose.PDF. Aprenda como adicionar texto ao PDF, adicionar fragmentos HTML ou usar fontes OTF personalizadas.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionando Texto ao PDF usando Python
Abstract: Este artigo oferece um guia completo sobre a manipulação de documentos PDF usando a biblioteca Aspose.PDF em Python. Ele abrange várias técnicas para adicionar e formatar texto, incluindo a definição de propriedades de texto como tamanho da fonte, tipo, cor e posicionamento.
---

Este guia explica como adicionar conteúdo de texto a documentos PDF usando Aspose.PDF para Python via .NET. Você aprenderá técnicas essenciais de inserção de texto — desde posicionar um fragmento de texto simples em uma posição específica, até estilizar (fonte, tamanho, cor, estilo), lidar com idiomas da direita para a esquerda (RTL), incorporar hiperlinks e trabalhar com layouts de parágrafo, listas e efeitos de transparência. O artigo também cobre cenários avançados, como usar fragmentos HTML ou LaTeX, fontes personalizadas e opções de formatação de texto como espaçamento entre linhas e entre caracteres.

Seja criando anotações simples ou layouts tipográficos ricos, este recurso fornece os blocos de construção fundamentais para trabalhar com texto em PDFs usando Aspose.PDF.

## Inserção básica de texto

Aspose.PDF para Python via .NET fornece uma API poderosa e flexível para manipular texto em arquivos PDF.
Se você precisar de rótulos estáticos simples, conteúdo ricamente formatado, texto multilíngue ou hiperlinks interativos, a ferramenta permite fazer tudo isso com código Python conciso.

### Caso Simples de Adição de Texto

Aspose.PDF para Python via .NET demonstra como adicionar um fragmento de texto simples a uma posição específica em uma página. Você aprenderá a criar um novo documento PDF, adicionar uma página, inserir texto em coordenadas definidas e salvar o arquivo resultante.

1. Crie um novo objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Use `document.pages.add()` para criar uma nova [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) em branco.
1. Crie um [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) com o conteúdo de texto.
1. Defina a posição do texto usando a classe [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/). Se você especificar `Position`, o texto será colocado no documento da esquerda para a direita e deslocado para baixo.
1. Personalize a aparência do texto. Você pode definir tamanho da fonte, cor, estilo da fonte e mais através da [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Anexe o `TextFragment` à coleção de parágrafos da página usando `page.paragraphs.add(text_fragment)`.
1. Salve o documento.

O trecho de código a seguir mostra como adicionar texto em um arquivo PDF existente:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_simple_case(outfile):
    """
    Add simple text to a PDF document.
    Creates a new PDF document with a single page and adds a text fragment
    "Hello, Aspose!" at position (100, 600) on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_simple_case("output.pdf")
        # Creates a PDF file named "output.pdf" with "Hello, Aspose!" text
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

Este exemplo de código usa um TextFragment. Mas você também pode adicionar texto a uma página PDF usando um TextParagraph. Vamos explorar a diferença.
O **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** é uma única peça de Texto. TextFragment representa uma única unidade de texto — essencialmente, uma string de texto que pode ser posicionada, estilizada e posicionada independentemente. É ideal quando você precisa adicionar quantidades simples e pequenas de texto.

O **[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** é um grupo de TextFragments. Ele pode adicionar várias linhas de texto. TextParagraph é um contêiner ou coleção de um ou mais objetos TextFragment. É ideal quando você precisa agrupar vários fragmentos — por exemplo, para criar um bloco de texto com várias linhas, palavras ou elementos formatados.
Um TextParagraph também gerencia o alinhamento de texto, espaçamento entre linhas e layout automático na página. O uso da linha vermelha só é possível com TextParagraph.

Para mais informações sobre Trabalhar com Texto, consulte as seções de documentação [Text Formatting inside PDF](/pdf/python-net/text-formatting-inside-pdf/) e [Extract Text from PDF using Python](/pdf/python-net/extract-text-from-pdf/).

### Adicionar Texto usando TextParagraph

Aspose.PDF para Python via .NET pode adicionar um parágrafo de texto usando [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) e [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) com opções de quebra.

1. Crie um novo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) e uma [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) em branco usando `document.pages.add()`.
1. Leia o texto de um arquivo ou use o texto padrão.
1. Crie um [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) para adicionar conteúdo a nível de parágrafo com controle de layout e quebras.
1. Crie um [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) e defina o modo de quebra (o exemplo usa `DISCRETIONARY_HYPHENATION`).
1. Crie um [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), aplique estilos e anexe o fragmento ao parágrafo.
1. Anexe o parágrafo à página usando o `TextBuilder`.
1. Salve o documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_paragraph(outfile):
    """
    Add formatted text paragraph with indentation and wrapping to a PDF document.

    Creates a PDF document with a text paragraph that demonstrates advanced text
    formatting including first line indentation, text wrapping with discretionary
    hyphenation, and loading text content from an external file.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Uses Times New Roman font at 12pt size
        - First line indent: 20 points
        - Rectangle bounds: (80, 800, 400, 200)
        - Text wrapping: DISCRETIONARY_HYPHENATION mode for better line breaks

    Example:
        >>> add_text_paragraph("paragraph_text.pdf")
        # Creates a PDF with formatted paragraph text
    """
    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(outfile)
```

![Adicionar Texto usando TextParagraph](text_paragraph.png)

### Adicionar Parágrafos com Indentações em PDF

O trecho de código a seguir mostra como criar um novo documento PDF e adicionar dois parágrafos de texto com estilos de indentação diferentes:

- O primeiro parágrafo demonstra uma indentação de primeira linha (apenas a primeira linha está indentada).

- O segundo parágrafo demonstra uma indentação nas linhas subsequentes (todas as linhas após a primeira são indentadas).

Ele usa as classes 'TextParagraph', 'TextBuilder' e 'TextFragment' do Aspose.PDF para controlar precisamente o layout e a formatação.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_paragraphs_indents(output_file_name):
    """Add text with indents to a PDF document.
    Creates a PDF document with two text paragraphs demonstrating different
    indent styles. The first paragraph uses first line indent, while the
    second paragraph uses subsequent lines indent. Text content is loaded
    from a lorem.txt file if available, otherwise uses a fallback message.
    Args:
        output_file_name (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF document to the specified output file.
    Note:
        - Uses Times New Roman font at 12pt size
        - Text wrapping is set to wrap by words
        - First paragraph: 20pt first line indent, positioned at (80, 800, 300, 50)
        - Second paragraph: 20pt subsequent lines indent, positioned at (320, 800, 500, 50)
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### Adicionar uma Nova Linha de Texto no PDF

Aspose.PDF para Python via .NET permite inserir texto multilinha em um documento PDF usando as classes TextFragment, TextParagraph e TextBuilder.

1. Crie um novo documento.
1. Defina um TextFragment contendo um caractere de nova linha.
1. Defina o estilo do texto.
1. Adicione o fragmento a um parágrafo.
1. Posicione o parágrafo.
1. Renderize o parágrafo na página.
1. Salve o documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### Determinar Quebras de Linha e Registrar Notificações em um PDF

Mostra como criar um documento PDF contendo vários fragmentos de texto e habilitar o registro de notificações do Aspose.PDF para monitorar eventos de layout — como quebras de linha e quebra de texto — durante a renderização.

1. Crie um novo documento PDF.
1. Habilite o registro de notificações.
1. Use document.pages.add() para criar a primeira página.
1. Adicione vários fragmentos de texto.
1. Use page.paragraphs.add(text) para renderizar cada fragmento de texto.
1. Salve o documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### Medir a Largura do Texto Dinamicamente em PDF

Meça dinamicamente a largura de caracteres e cadeias em uma fonte específica usando Aspose.PDF for Python via .NET. Ele usa os métodos 'Font.measure_string()' e 'TextState.measure_string()' para verificar se as larguras das strings medida são consistentes e precisas.

1. Use 'FontRepository.find_font()' para obter o objeto de fonte Arial do repositório.
1. Crie um objeto TextState para gerenciar as propriedades da fonte.
1. Meça Caracteres Individuais.
1. Compare os resultados de ambos os métodos para todos os caracteres entre 'A' e 'z'.
1. Garanta que ambas as abordagens de medição produzam os mesmos resultados.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_text_width_dynamically(output_file):

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### Adicionar Texto com Hiperlinks

Adicione hiperlinks clicáveis ao texto em um PDF usando Aspose.PDF for Python via .NET. Nossa biblioteca demonstra como adicionar vários segmentos de texto dentro de um único TextFragment e aplicar um hiperlink a um segmento específico, e estilizar os segmentos de texto individualmente (por exemplo, cor, fonte itálica).

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Crie um TextFragment.
1. Adicione vários objetos TextSegment. Cada segmento pode ter seu próprio conteúdo e estilo. Por exemplo, texto simples ou texto com hiperlink.
1. Aplique um hiperlink a um segmento. Crie um objeto WebHyperlink com a URL desejada.
1. Estilize o segmento. Personalize cor, estilo da fonte, tamanho, etc., usando text_state.
1. Adicione o fragmento à página usando 'page.paragraphs.add()'.
1. Salve o PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_hyperlink(outfile):
    """
    Add text with embedded hyperlinks to a PDF document.

    Creates a PDF document with a text fragment containing multiple segments,
    including one with a hyperlink to Aspose. Demonstrates how to create
    clickable links within PDF text content with different formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates 4 text segments within a single text fragment
        - One segment contains a hyperlink to "https://products.aspose.com/pdf"
        - Hyperlinked text is styled in blue italic font
        - Other segments are regular text without links

    Example:
        >>> add_text_with_hyperlink("hyperlink_text.pdf")
        # Creates a PDF with clickable Aspose link in the text
    """

    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment(
        "Sample Text Fragment"
    )

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Fragmento de texto exibido em um PDF mostrando conteúdo misto com Sample Text Fragment seguido por Text Segment 1, então um texto azul com hiperlink lendo Link to Aspose (linkando para https://products.aspose.com/pdf), e terminando com TextSegment sem hyperlink em formatação de texto preto regular](hyperlink_text.png)

### Adicionar Texto da Direita para a Esquerda (RTL) ao Documento PDF

RTL (da Direita para a Esquerda) é uma propriedade que indica a direção da escrita do texto, onde o texto é escrito da direita para a esquerda.
Aspose.PDF for Python via .NET demonstra como adicionar texto da Direita para a Esquerda (RTL), como árabe ou hebraico, a um documento PDF.

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Crie um TextFragment com conteúdo RTL. Insira seu texto em árabe, hebraico ou outro idioma RTL como conteúdo do fragmento.
Defina a fonte e o estilo. Escolha uma fonte que suporte o script RTL (por exemplo, Tahoma, Arial Unicode MS). Defina font_size e foreground_color conforme necessário.
1. Defina o alinhamento horizontal para a direita usando 'text_fragment.horizontal_alignment'.
1. Adicione o fragmento de texto à página.
1. Salve o documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_rtl_text(outfile):
    """
    Add right-to-left (RTL) text to a PDF document.

    Creates a PDF document with Arabic text that demonstrates right-to-left text
    rendering and alignment. The text uses the Tahoma font which supports Arabic
    characters and is aligned to the right side of the page.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses Tahoma font at 14pt size for proper Arabic character support
        - Text color is set to blue
        - Horizontal alignment is set to RIGHT for proper RTL display
        - The Arabic text describes Nasreddin Hodja, a folklore character

    Example:
        >>> add_text_with_rtl_text("arabic_text.pdf")
        # Creates a PDF with right-to-left Arabic text
    """

    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Texto da Direita para a Esquerda](rtl_text.png)

## Estilização de Texto

### Adicionar Texto com Estilização de Fonte

Este é um exemplo mais avançado que demonstra a estilização de texto, personalização de fontes e texto de formato misto (usando segmentos de texto em subscrito). Aspose.PDF explica como aplicar propriedades de fonte como família, tamanho, cor, negrito, itálico e sublinhado a um fragmento de texto.
Além disso, este trecho de código mostra como usar múltiplos segmentos de texto dentro de um único fragmento para criar expressões de texto complexas — por exemplo, incluindo caracteres em subscrito ou sobrescrito, frequentemente necessários em fórmulas ou notações científicas.

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Crie um TextFragment para texto simples estilizado.
1. Defina o conteúdo do texto.
1. Defina a posição usando coordenadas Position(x, y).
1. Aplique estilo por meio da propriedade 'text_state' - fonte, font_size, foreground_color, font_style, sublinhado.
1. Crie uma expressão complexa com múltiplos objetos TextSegment. Cada TextSegment representa uma porção de texto que pode ter seu próprio estilo. Isso permite construir expressões, como fórmulas matemáticas ou químicas.
1. Defina vários objetos TextState. Um para o texto principal (text_state_letters). Outro para texto subscrito ou sobrescrito (text_state_index).
1. Combine segmentos de texto. Anexe cada segmento a um 'TextFragment' usando 'segments.append()'.
1. Adicione ambos os objetos de texto à página. Use 'page.paragraphs.add()' para inseri‑los no documento.
1. Salve o documento final.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_font_styling(outfile):
    """
    Add styled text fragments to a PDF document.
    Creates a new PDF document with a single page and adds a styled text fragment
    "Hello, Aspose!" at position (100, 600) and a formula with styled segments at position (100, 500).
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_with_font_styling("styled_text.pdf")
        # Creates a PDF file named "styled_text.pdf" with styled text and a formula
    """

    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(outfile)
```

![Fragmento de texto exibido com fonte Arial azul itálica contendo o texto Hello, Aspose! seguido por uma fórmula matemática mostrando S = a subscript 2n + a subscript 2n+1 + a subscript 2n+2 com texto principal azul e formatação de subscrito vermelha](styled_text.png)

## Adicionar Texto transparente

Adicione formas semitransparentes e texto a um documento PDF usando Aspose.PDF para Python.
Ele cria um retângulo colorido com opacidade parcial e sobrepõe um TextFragment com cor de primeiro plano transparente.

1. Inicialize um objeto Document e adicione uma página em branco para desenhar o conteúdo.
1. Use 'ap.drawing.Graph' para criar uma tela que permite desenhar formas.
1. Adicione um retângulo com preenchimento semitransparente.
1. Impeça o deslocamento da posição da tela.
1. Adicione a tela à página. Insira as formas gráficas na coleção de parágrafos da página.
1. Crie um fragmento de texto transparente.
1. Insira o fragmento de texto na coleção de parágrafos da página.
1. Salve o documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_transparent(outfile):
    """
    Add transparent text over a semi-transparent background to a PDF document.

    Creates a PDF document with a semi-transparent filled rectangle as background
    and transparent green text overlaid on top. This demonstrates how to create
    transparency effects in PDF documents using ARGB color values.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Background rectangle: 128 alpha, light purple color (0xC5, 0xB5, 0xFF)
        - Text transparency: 30 alpha, green color (0, 255, 0)
        - The canvas is set to not change position to prevent layout shifts

    Example:
        >>> add_text_transparent("transparent_output.pdf")
        # Creates a PDF with transparent text effects
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(outfile)
```

### Adicionar Texto Invisível ao PDF

Este exemplo demonstra como criar um documento PDF contendo texto visível e invisível. Texto invisível permanece parte da estrutura do documento, mas está oculto da visualização, sendo útil para incorporar metadados, tags de acessibilidade ou conteúdo pesquisável sem afetar o layout.

1. Crie um Documento PDF e uma Página.
1. Crie um fragmento de texto com conteúdo visível repetido.
1. Adicione um segundo fragmento de texto e marque‑o como invisível.
1. Salve o Documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_invisible(outfile):
    """
    Creates a PDF document with both visible and invisible text.
    This function generates a PDF file containing two text fragments:
    one visible text that will be displayed normally, and one invisible
    text that will be hidden from view but still present in the document.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF to the specified file path.
    Example:
        add_text_invisible("output.pdf")
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. "
        "This is the visible text. "
        "This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Adicionar Texto com Estilo de Borda em PDF

A biblioteca Aspose.PDF mostra como criar um documento PDF contendo um fragmento de texto estilizado com uma borda visível. O método aplica cores de fundo e de primeiro plano, configurações de fonte e um traço (borda) ao redor do retângulo de texto para realçar visualmente.

1. Crie um Documento PDF e uma Página.
1. Crie e posicione o Fragmento de Texto. Adicione um fragmento de texto com a mensagem e defina sua posição.
1. Aplique Estilização de Texto. Defina a fonte para Times New Roman, tamanho 12. Aplique um fundo cinza claro e cor de primeiro plano (texto) vermelha.
1. Configure o Estilo da Borda.
1. Adicione o Texto à Página. Use TextBuilder para anexar o texto estilizado à página.
1. Salve o Documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_border(output_file_name):
    """
    Add text with border styling to a PDF document.

    Creates a PDF document with a text fragment that has border styling applied.
    The text includes background color, foreground color, and a configurable
    border (stroke) around the text rectangle.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample text with border."
        - Font: Times New Roman, 12pt
        - Background: Light gray
        - Foreground: Red text
        - Border: Dark red stroke around text rectangle
        - Position: (10, 700)
        - Border is only visible when draw_text_rectangle_border is True

    Example:
        >>> add_text_border("bordered_text.pdf")
        # Creates a PDF with bordered text styling
    """
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### Adicionar Texto Tachado a um PDF

Adicione formatação de tachado (riscado) a um fragmento de texto em um documento PDF. Texto tachado é útil para indicar exclusões, revisões ou ênfase em documentos anotados.

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Crie e estilize o Fragmento de Texto.
1. Aplique cor e formatação de tachado. Defina o fundo como cinza claro, a cor do texto como vermelha e habilite o tachado.
1. Posicione o Texto.
1. Use 'TextBuilder' para anexar o texto estilizado à página.
1. Salve o Documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_strikeout_text(output_file_name):
    """
    Add text with strikeout (strikethrough) formatting to a PDF document.

    Creates a PDF document with a text fragment that has strikeout formatting applied.
    The text appears with a line through it, along with additional styling including
    background color, foreground color, and bold font style.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample strikeout text."
        - Font: Times New Roman, 12pt, Bold
        - Background: Light gray
        - Foreground: Red text
        - Strikeout: Enabled (line through text)
        - Position: (100, 600)

    Example:
        >>> add_strikeout_text("strikeout_text.pdf")
        # Creates a PDF with strikethrough text formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## Efeitos avançados de cor

### Aplicando um Gradiente Axial ao Texto em um PDF

Aspose.PDF para Python via .NET demonstra como aplicar um efeito de gradiente linear ao texto em um documento PDF. O gradiente axial transita suavemente do vermelho ao azul ao longo do texto, criando um título visualmente impactante. Essa técnica é ideal para títulos estilizados, branding ou elementos decorativos em layouts de documentos PDF.

1. Inicialize um novo documento e adicione uma página em branco.
1. Crie e estilize o Fragmento de Texto. Adicione o título, defina a posição, a fonte e o tamanho.
1. Aplique sombreamento de Gradiente Axial com 'GradientAxialShading'. Defina a cor de primeiro plano usando GradientAxialShading do vermelho ao azul.
1. Adicione Estilização de Sublinhado.
1. Insira o fragmento de texto estilizado na página.
1. Salve o Documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_axial_shading_to_text(output_file_name):
    """
    Apply axial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has an axial (linear) gradient
    effect applied. The gradient transitions from red to blue in a linear fashion
    across the text. This demonstrates advanced text styling with gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Linear gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientAxialShading for linear gradient effect

    Example:
        >>> apply_gradient_axial_shading_to_text("gradient_axial.pdf")
        # Creates a PDF with linear gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### Aplicando um Gradiente Radial ao Texto em um PDF

Um gradiente radial cria uma transição de cores circular que irradia a partir do centro do texto, oferecendo uma opção de estilo visualmente dinâmica para títulos, cabeçalhos ou elementos decorativos.

1. Inicialize um novo documento e adicione uma página em branco.
1. Crie e estilize um fragmento de texto. Adicione o título, defina a posição, a fonte e o tamanho.
1. Aplique gradiente radial com 'GradientRadialShading'. Defina a cor de primeiro plano usando GradientRadialShading de vermelho a azul.
1. Adicione estilo sublinhado.
1. Insira o fragmento de texto estilizado na página.
1. Salve o documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_radial_shading_to_text(output_file_name):
    """
    Apply radial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has a radial (circular) gradient
    effect applied. The gradient radiates from the center outward, transitioning from
    red to blue. This demonstrates advanced text styling with radial gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Radial gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientRadialShading for circular gradient effect

    Example:
        >>> apply_gradient_radial_shading_to_text("gradient_radial.pdf")
        # Creates a PDF with radial gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Aplicar sombreamento de gradiente radial](gradient_radial_shading.png)

## Fragmentos HTML e LaTeX

### Adicionar texto HTML ao documento PDF

A biblioteca Aspose.PDF for Python via .NET permite inserir conteúdo formatado em HTML em um documento PDF usando a classe HtmlFragment. Ao usar tags HTML, você pode renderizar texto estilizado, estruturado ou semelhante a fórmulas diretamente em um PDF.

1. Crie um novo documento e página usando 'Document()' e 'document.pages.add()' para adicionar uma página em branco.
1. Crie uma instância da classe HtmlFragment e passe sua string HTML como parâmetro.
1. Adicione o fragmento à página usando 'page.paragraphs.add()' para inserir o conteúdo HTML.
1. Salve o PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_html_fragment(outfile):
    """
    Add HTML fragment with mathematical notation to a PDF document.

    Creates a PDF document containing an HTML fragment that displays mathematical
    notation using HTML tags including subscript and superscript elements.
    This demonstrates how to embed formatted HTML content directly into PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <pre> tags to preserve formatting
        - Includes <sub> for subscript (2n) and <sup> for superscript (2)
        - Formula displayed: S=a₂ₙ+a²
        - HTML is rendered as formatted content within the PDF

    Example:
        >>> add_text_html_fragment("html_math.pdf")
        # Creates a PDF with HTML mathematical notation
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Adicionar texto HTML a um documento PDF](html_fragment.png)

### Adicionar fragmento HTML estilizado com várias formatações a um documento PDF

Podemos definir um fragmento HTML e definir o estilo do texto diretamente usando tags HTML. Incorpore conteúdo HTML estilizado em um documento PDF. Este trecho de código cria um novo arquivo PDF, adiciona uma página, insere um fragmento HTML com vários elementos de formatação (títulos, parágrafos, links e estilos embutidos) e salva o resultado no caminho especificado.

1. Inicializa um novo objeto Document para representar o PDF.
1. Anexa uma página em branco ao documento onde o conteúdo HTML será colocado.
1. Prepare o conteúdo HTML. A string HTML contém um título h1, um parágrafo com cor verde e texto em negrito, itálico e sublinhado, e um hiperlink para um site com tamanho de fonte aumentado.
1. Crie um fragmento HTML. Envolva a string HTML em um objeto HtmlFragment.
1. Insira HTML na página. Adiciona o fragmento HTML à coleção de parágrafos da página, renderizando o HTML como conteúdo nativo do PDF.
1. Salve o documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment(outfile):
    """
    Add styled HTML fragment with various formatting to a PDF document.

    Creates a PDF document containing rich HTML content including headings,
    paragraphs with inline formatting, colored text, and hyperlinks.
    Demonstrates comprehensive HTML rendering capabilities in PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Includes HTML heading (h1) with blue color styling
        - Contains paragraph with bold, italic, and underlined text
        - Features green-colored paragraph text
        - Includes styled hyperlink to Aspose website
        - All HTML styling is preserved in the PDF output

    Example:
        >>> add_html_fragment("rich_html.pdf")
        # Creates a PDF with various HTML formatting elements
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Adicionar conteúdo HTML a um documento PDF](html_content.png)

### Adicionar fragmento HTML com estado de texto substituído

Como vimos no exemplo anterior, é possível definir estilos diretamente no código HTML. Isso tem suas vantagens, mas também algumas desvantagens. Suponha que estejamos trabalhando com o HTML de um cliente e queremos unificar a aparência da nossa saída.
Nesse caso, podemos substituir o estilo do cliente usando nosso próprio TextState, como mostrado no exemplo a seguir.

1. Crie um novo documento e página usando 'Document()' e 'document.pages.add()' para adicionar uma página em branco.
1. Prepare o conteúdo HTML. A string HTML contém um título h1 com fonte Verdana, um parágrafo de cor verde com texto em negrito, itálico e sublinhado, e um hiperlink para um site com tamanho de fonte maior.
1. Crie um fragmento HTML. Envolva a string HTML em um objeto HtmlFragment.
1. Substitua a formatação do texto. Crie um objeto TextState e defina a fonte, o tamanho da fonte e a cor do texto.
1. Adicione o fragmento HTML à coleção de parágrafos da página.
1. Salve o documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment_override_text_state(outfile):
    """
    Add HTML fragment with overridden text styling to a PDF document.

    Creates a PDF document with HTML content where the default text styling
    is overridden using TextState properties. This demonstrates how to apply
    global text formatting that supersedes HTML styling for consistent appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - HTML includes heading, paragraphs, and links with original styling
        - TextState override applies: Arial font, 14pt size, red color
        - Override styling takes precedence over HTML inline styles
        - Useful for enforcing consistent document-wide text appearance
        - Original HTML styling is replaced by the TextState properties

    Example:
        >>> add_html_fragment_override_text_state("html_override.pdf")
        # Creates a PDF where HTML styling is overridden with red Arial text
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Adicionar fragmento HTML que substitui o estado de texto](html_override.png)

### Adicionar texto LaTeX ao documento PDF

Adicione expressões matemáticas formatadas em LaTeX a um documento PDF usando a classe TeXFragment no Aspose.PDF for Python via .NET.
LaTeX é um poderoso sistema de tipografia amplamente usado para criar documentos científicos e matemáticos. Ao usar TeXFragment, você pode renderizar diretamente notação e símbolos matemáticos LaTeX dentro de uma página PDF.

1. Crie um novo documento e página usando 'Document()' e 'document.pages.add()' para adicionar uma página em branco.
1. Use a classe TeXFragment para renderizar a sintaxe LaTeX diretamente.
1. Adicione o conteúdo LaTeX ao layout do PDF com 'page.paragraphs.add()'.
1. Salve o PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_latex_fragment(outfile):
    """
    Add LaTeX mathematical expression to a PDF document.

    Creates a PDF document containing a complex mathematical expression rendered
    from LaTeX markup. This demonstrates advanced mathematical typesetting
    capabilities using LaTeX syntax within PDF documents.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX TeXFragment for mathematical expression rendering
        - Expression includes overbrace and underbrace notation
        - Formula: (a+b)⁶ · (c+d)⁷ with braces and labels = 42
        - LaTeX commands: \\overbrace, \\underbrace, \\text, \\cdot
        - Provides professional mathematical typography

    Example:
        >>> add_text_latex_fragment("latex_math.pdf")
        # Creates a PDF with complex LaTeX mathematical expression
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Expressão matemática complexa exibida em um PDF mostrando a fórmula LaTeX com notação de overbrace sobre (a+b)⁶, notação de underbrace sob a expressão inteira (a+b)⁶ · (c+d)⁷, rotulada como exemplo de texto, e igual a 42. A fórmula demonstra tipografia matemática avançada com espaçamento adequado e estilo de colchetes típico da renderização LaTeX](latex_fragment.png)

## Fontes personalizadas

### Usar uma fonte personalizada a partir de um arquivo

Este exemplo permite adicionar texto a um arquivo PDF usando uma fonte OpenType personalizada no Aspose.PDF for Python via .NET. Ele mostra como criar um novo documento PDF, posicionar o texto com precisão na página e aplicar formatação personalizada, como tipo de fonte, tamanho, cor e estilo itálico.

1. Crie um novo documento PDF e adicione uma página.
1. Defina o conteúdo de texto que deseja adicionar ao PDF.
1. Defina a posição do texto.
1. Adicione o TextFragment à página.
1. Salve o documento PDF.

Esta função funciona não apenas com fontes OTF, mas também com fontes TTF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_file(outfile):
    """
    Creates a PDF document with text using a custom font loaded from a file.
    This function demonstrates how to load a custom OpenType font (.otf) from the file system
    and apply it to text in a PDF document. The text is styled with blue color, italic style,
    and positioned at specific coordinates on the page.
    Args:
        outfile (str): The output file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires the "BriosoPro Italic.otf" font file to be present in the DATA_DIR directory
        - Uses Aspose.PDF library for PDF generation and text manipulation
        - The text fragment is positioned at coordinates (100, 600) on the page
        - Font size is set to 24 points with blue foreground color and italic style
    """

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Fragmento de texto exibido em um documento PDF mostrando Hello, Aspose! renderizado em fonte BriosoPro azul itálica, demonstrando a integração de fonte OpenType personalizada e capacidades de estilização dentro da formatação de texto PDF](custom_font.png)

### Usar uma Fonte personalizada a partir de um fluxo

Este trecho de código demonstra como adicionar texto a um documento PDF usando uma fonte OpenType (OTF) personalizada incorporada com Aspose.PDF para Python via .NET. Ele mostra como abrir um arquivo de fonte como um fluxo, incorporá-lo ao PDF para garantir a disponibilidade da fonte em diferentes sistemas, e aplicar formatação de texto como tamanho da fonte, cor e estilo itálico. Esta abordagem é ideal para criar PDFs visualmente consistentes que preservam a tipografia mesmo quando compartilhados ou visualizados em dispositivos sem a fonte instalada.

1. Carregue o arquivo de fonte como um fluxo binário.
1. Abra e incorpore a fonte usando 'FontRepository.open_font'.
1. Crie um novo documento PDF e adicione uma página.
1. Adicione um fragmento de texto estilizado com:
- Fonte personalizada incorporada.
- Estilo itálico e cor azul.
- Tamanho e posição específicos da fonte.
1. Salve o documento final em um caminho de saída especificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_stream(outfile):
    """Use custom font from stream."""

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(outfile)
```

Incorporar fontes garante renderização consistente em todas as plataformas, tornando esta abordagem ideal para branding, fidelidade de design e suporte multilíngue.

