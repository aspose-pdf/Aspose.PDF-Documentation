---
title: Adicionar texto ao PDF em Python
linktitle: Adicionar texto ao PDF
type: docs
weight: 10
url: /pt/python-net/add-text-to-pdf-file/
description: Aprenda como adicionar texto, fragmentos HTML, listas, links e fontes personalizadas a documentos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione texto, links, HTML e fontes a arquivos PDF com Python
Abstract: Este artigo explica como adicionar e formatar texto em documentos PDF usando Aspose.PDF for Python via .NET. Ele cobre técnicas principais, como posicionamento de texto, aplicação de configurações de fonte e estilo, inserção de links e listas, e uso de HTML, LaTeX e fontes personalizadas em fluxos de trabalho Python.
---

Este guia explica como adicionar conteúdo de texto a documentos PDF usando Aspose.PDF for Python via .NET. Você aprenderá técnicas essenciais de inserção de texto — desde colocar um fragmento de texto simples em uma posição específica, até estilizar (fonte, tamanho, cor, estilo), lidar com idiomas da direita para a esquerda (RTL), incorporar hiperlinks e trabalhar com layouts de parágrafos, listas e efeitos de transparência. O artigo também aborda cenários avançados, como usar fragmentos HTML ou LaTeX, fontes personalizadas e opções de formatação de texto, como espaçamento entre linhas e espaçamento entre caracteres.

Quer você esteja criando anotações simples ou layouts tipográficos ricos, este recurso lhe fornece os blocos de construção fundamentais para trabalhar com texto em PDFs usando Aspose.PDF.

## Inserção básica de texto

Aspose.PDF for Python via .NET fornece uma API poderosa e flexível para manipular texto dentro de arquivos PDF.
Se você precisar de rótulos estáticos simples, conteúdo ricamente formatado, texto multilíngue ou hyperlinks interativos, o toolkit permite que você faça tudo isso com código Python conciso.

### Adicionar Texto Caso Simples

Aspose.PDF for Python via .NET mostra como adicionar um fragmento de texto simples em uma posição específica em uma página. Você aprenderá como criar um novo documento PDF, adicionar uma página, inserir texto em coordenadas dadas e salvar o arquivo resultante.

1. Criar um novo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto.
1. Usar `document.pages.add()` para criar um novo em branco [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Criar um [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) com o conteúdo do texto.
1. Defina a posição do texto usando o [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) classe. Se você especificar `Position`, o texto será localizado em seu documento da esquerda para a direita e deslocado para baixo.
1. Personalize a aparência do texto. Você pode definir o tamanho da fonte, cor, estilo da fonte e muito mais via o [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Anexar o `TextFragment` para a coleção de parágrafos da página com `page.paragraphs.add(text_fragment)`.
1. Salvar o documento.

O seguinte trecho de código mostra como adicionar texto em um arquivo PDF existente:

```python
import math
import sys
import os
import aspose.pdf as ap

# region Basic text insertion
def add_text_simple_case(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

Este exemplo de código usa um TextFragment. Você também pode adicionar texto a uma página PDF usando um TextParagraph.
O **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** é um único trecho de texto. Representa uma string de texto que pode ser colocada, estilizada e posicionada independentemente. É ideal quando você precisa adicionar conteúdo de texto pequeno e simples.

O **[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** é um grupo de TextFragments. Ele pode adicionar múltiplas linhas de texto. TextParagraph é um contêiner ou coleção de um ou mais objetos TextFragment. É ideal quando você precisa agrupar múltiplos fragments — por exemplo, para criar um bloco de texto com várias linhas, palavras ou elementos formatados.
Um TextParagraph também gerencia o alinhamento de texto, o espaçamento entre linhas e o layout automático na página. O uso da linha vermelha só é possível com TextParagraph.

Para mais informações sobre como trabalhar com texto, veja [Formatação de Texto dentro do PDF](/pdf/pt/python-net/text-formatting-inside-pdf/) e [Pesquisar e Obter Texto de PDF](/pdf/pt/python-net/search-and-get-text-from-pdf/).

### Adicionar texto usando TextParagraph

Aspose.PDF for Python via .NET pode adicionar um parágrafo de texto usando [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) e [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) com opções de quebra.

1. Criar um novo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) e um em branco [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) usando `document.pages.add()`.
1. Ler texto de um arquivo ou usar o texto padrão.
1. Criar um [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) para adicionar conteúdo ao nível de parágrafo com controle de layout e de quebra de linha.
1. Criar um [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) e defina o modo de quebra (o exemplo usa `DISCRETIONARY_HYPHENATION`).
1. Criar um [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), aplique estilos e anexe o fragmento ao parágrafo.
1. Anexe o parágrafo à página usando o `TextBuilder`.
1. Salvar o documento.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraph(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

    document.save(output_file_name)
```

![Adicionar texto usando TextParagraph](text_paragraph.png)

### Adicionar parágrafos com recuos em PDF

O trecho de código a seguir mostra como criar um novo documento PDF e adicionar dois parágrafos de texto com estilos de recuo diferentes:

- O primeiro parágrafo demonstra um recuo de primeira linha (apenas a primeira linha está recuada).

- O segundo parágrafo demonstra um recuo de linhas subsequentes (todas as linhas após a primeira são recuadas).

Ele usa as classes 'TextParagraph', 'TextBuilder' e 'TextFragment' da Aspose.PDF para controlar com precisão o layout e a formatação.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraphs_indents(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

### Adicionar uma nova linha de texto no PDF

Aspose.PDF for Python via .NET permite inserir texto de várias linhas em um documento PDF usando as classes TextFragment, TextParagraph e TextBuilder.

1. Criar um novo documento.
1. Defina um TextFragment contendo um caractere de nova linha.
1. Definir estilo de texto.
1. Adicione o fragmento a um parágrafo.
1. Posicione o parágrafo.
1. Renderizar parágrafo na página.
1. Salvar o documento.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Determinar Quebras de Linha e Notificações de Log em um PDF

Mostra como criar um documento PDF contendo múltiplos fragmentos de texto e habilitar o registro de notificações do Aspose.PDF para monitorar eventos de layout — como quebras de linha e quebra de texto — durante a renderização.

1. Crie um novo documento PDF.
1. Ativar registro de notificações.
1. Use document.pages.add() para criar a primeira página.
1. Adicionar múltiplos fragmentos de texto.
1. Use page.paragraphs.add(text) para renderizar cada fragmento de texto.
1. Salvar o documento.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Medir a largura do texto dinamicamente em PDF

Meça dinamicamente a largura de caracteres e strings em uma fonte específica usando Aspose.PDF for Python via .NET. Ele usa os métodos 'Font.measure_string()' e 'TextState.measure_string()' para verificar se as larguras das strings medidas são consistentes e precisas.

1. Use 'FontRepository.find_font()' para recuperar o objeto de fonte Arial do repositório.
1. Crie um objeto TextState para gerenciar as propriedades da fonte.
1. Meça caracteres individuais.
1. Compare os resultados de ambos os métodos para todos os caracteres entre 'A' e 'z'.
1. Certifique-se de que ambas as abordagens de medição produzam os mesmos resultados.

```python
import math
import sys
import os
import aspose.pdf as ap

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

Adicione hyperlinks clicáveis ao texto em um PDF usando Aspose.PDF for Python via .NET. Nossa biblioteca demonstra como adicionar múltiplos segmentos de texto dentro de um único TextFragment e aplicar um hyperlink a um segmento específico, e estilizar os segmentos de texto individualmente (por exemplo, cor, fonte itálica).

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Criar um TextFragment.
1. Adicione vários objetos TextSegment. Cada segmento pode ter seu próprio conteúdo e estilo. Por exemplo, texto simples ou texto de hiperlink.
1. Aplique um hyperlink a um segmento. Crie um objeto WebHyperlink com a URL desejada.
1. Estilize o segmento. Personalize cor, estilo de fonte, tamanho, etc., usando text_state.
1. Adicione o fragmento à página usando o 'page.paragraphs.add()'.
1. Salvar o PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_hyperlink(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Sample Text Fragment")

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
    document.save(output_file_name)
```

![Fragmento de texto exibido em um PDF mostrando conteúdo misto com Fragmento de Texto de Exemplo seguido por Segmento de Texto 1, então um texto hiperlíneo azul lendo Link para Aspose (linkando para https://products.aspose.com/pdf), e terminando com TextSegment sem hyperlink em formatação de texto preto regular](hyperlink_text.png)

### Adicionar texto da direita para a esquerda (RTL) ao documento PDF

RTL (da Direita para a Esquerda) é uma propriedade que indica a direção da escrita de texto, onde o texto é escrito da direita para a esquerda.
Aspose.PDF for Python via .NET demonstra como adicionar texto da direita para a esquerda (RTL), como árabe ou hebraico, a um documento PDF.

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Crie um TextFragment com conteúdo RTL. Insira seu texto em árabe, hebraico ou outro idioma RTL como o conteúdo do fragmento.
Defina a fonte e o estilo. Escolha uma fonte que suporte o script RTL (por exemplo, Tahoma, Arial Unicode MS). Defina font_size e foreground_color conforme necessário.
1. Defina o alinhamento horizontal para a direita usando 'text_fragment.horizontal_alignment'.
1. Adicionar o TextFragment à página.
1. Salve o documento PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_rtl_text(output_file_name):
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
    document.save(output_file_name)
```

![Texto da direita para a esquerda](rtl_text.png)

## Estilização de texto

### Adicionar Texto com Estilização de Fonte

Este é um exemplo mais avançado que demonstra a estilização de texto, a personalização de Font e texto de formato misto (usando segmentos de texto em sobrescrito). Aspose.PDF explica como aplicar propriedades de Font, como família de Font, tamanho, cor, negrito, itálico e sublinhado, a um fragmento de texto.
Além disso, este trecho de código mostra como usar múltiplos segmentos de texto dentro de um único fragmento para criar expressões de texto complexas — por exemplo, incluindo caracteres subscritos ou sobrescritos, frequentemente necessários em fórmulas ou notações científicas.

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Crie um TextFragment para texto simples com estilo.
1. Definir conteúdo de texto.
1. Defina a posição usando as coordenadas Position(x, y).
1. Aplique estilos via a 'text_state property' - font, font_size, foreground_color, font_style, underline.
1. Crie uma expressão complexa com múltiplos objetos TextSegment. Cada TextSegment representa uma parte do texto que pode ter seu próprio estilo. Isso permite que você construa expressões, como fórmulas matemáticas ou químicas.
1. Defina vários objetos TextState. Um para o texto principal (text_state_letters). Outro para texto em subscrito ou sobrescrito (text_state_index).
1. Combine os segmentos de texto. Anexe cada segmento a um 'TextFragment' usando 'segments.append()'.
1. Adicione ambos os objetos de texto à página. Use 'page.paragraphs.add()' para colocá-los no documento.
1. Salve o documento final.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_font_styling(output_file_name):
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
    document.save(output_file_name)
```

![Fragmento de texto exibido com fonte Arial itálica azul contendo o texto Hello, Aspose! seguido por uma fórmula matemática mostrando S = a subscrito 2n + a subscrito 2n+1 + a subscrito 2n+2 com formatação de texto principal azul e subscrito vermelho](styled_text.png)

## Adicionar Texto transparente

Adicione formas semitransparentes e texto a um documento PDF usando Aspose.PDF para Python.
Ele cria um retângulo colorido com opacidade parcial e sobrepõe um TextFragment com cor de primeiro plano transparente.

1. Inicialize um objeto Document e adicione uma página em branco para desenhar conteúdo.
1. Use 'ap.drawing.Graph' para criar uma tela que permite desenhar formas.
1. Adicione um retângulo com preenchimento semitransparente.
1. Impedir o deslocamento da posição do canvas.
1. Adicione o canvas à página. Insira as formas gráficas na coleção de parágrafos da página.
1. Crie um fragmento de texto transparente.
1. Insira o fragmento de texto na coleção de parágrafos da página.
1. Salve o documento PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_transparent(output_file_name):
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

    document.save(output_file_name)
```

### Adicionar Texto Invisível ao PDF

Este exemplo demonstra como criar um documento PDF contendo texto visível e invisível. O texto invisível continua fazendo parte da estrutura do documento, mas está oculto da visualização, tornando-o útil para incorporar metadados, tags de acessibilidade ou conteúdo pesquisável sem alterar o layout.

1. Criar PDF Document e Page.
1. Crie um fragmento de texto com conteúdo visível repetido.
1. Adicione um segundo TextFragment e marque-o como invisível.
1. Salvar o Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_invisible(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. This is the visible text. This is the visible text."
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

    document.save(output_file_name)
```

### Adicionar texto com estilo de borda em PDF

A biblioteca Aspose.PDF mostra como criar um documento PDF contendo um fragmento de texto estilizado com uma borda visível. O método aplica cores de fundo e de primeiro plano, configurações de Font e um stroke (border) ao redor do retângulo de texto para melhorar a ênfase visual.

1. Criar um PDF Document e um Page.
1. Criar e posicionar Fragmento de Texto. Adicionar um Fragmento de Texto com a mensagem e definir sua posição.
1. Aplicar Estilização de Texto. Definir fonte para Times New Roman, tamanho 12. Aplicar um fundo cinza claro e cor de primeiro plano (texto) vermelha.
1. Configurar estilo da borda.
1. Adicionar texto à página. Use TextBuilder para acrescentar o texto formatado à página.
1. Salvar o Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_border(output_file_name):
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

### Adicionar texto tachado a um PDF

Adicione formatação de tachado (strikeout) a um fragmento de texto em um documento PDF. Texto tachado é útil para indicar exclusões, revisões ou ênfase em documentos anotados.

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Criar e estilizar Fragmento de Texto.
1. Aplicar formatação de cor e tachado. Defina o fundo como cinza claro, a cor do texto como vermelha e habilite o tachado.
1. Posicione o Texto.
1. Use 'TextBuilder' para anexar o texto formatado à página.
1. Salvar o Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_strikeout_text(output_file_name):
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

## Efeitos de cor avançados

### Aplicando um Gradiente Axial ao Texto em um PDF

Aspose.PDF for Python via .NET demonstra como aplicar um efeito de gradiente linear ao texto em um documento PDF. O gradiente axial transita suavemente do vermelho ao azul ao longo do texto, criando um cabeçalho visualmente impressionante. Esta técnica é ideal para títulos estilizados, branding ou elementos decorativos em layouts de documentos PDF.

1. Inicialize um novo documento e adicione uma página em branco.
1. Criar e Estilizar Fragmento de Texto. Adicionar título, definir posição, fonte e tamanho.
1. Aplique sombreamento gradiente axial com 'GradientAxialShading'. Defina a cor de primeiro plano usando GradientAxialShading de vermelho para azul.
1. Adicionar estilo de sublinhado.
1. Insira o fragmento de texto estilizado na página.
1. Salvar o Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_axial_shading_to_text(output_file_name):
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

Um gradiente radial cria uma transição de cores circular que se irradia a partir do centro do texto, oferecendo uma opção de estilo visualmente dinâmica para títulos, cabeçalhos ou elementos decorativos.

1. Inicialize um novo documento e adicione uma página em branco.
1. Criar e Estilizar Fragmento de Texto. Adicionar título, definir posição, fonte e tamanho.
1. Aplicar Gradiente Radial com 'GradientRadialShading'. Definir a cor de primeiro plano usando GradientRadialShading de vermelho a azul.
1. Adicionar estilo de sublinhado.
1. Insira o fragmento de texto estilizado na página.
1. Salvar o Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_radial_shading_to_text(output_file_name):
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

## fragmentos HTML e LaTeX

### Adicionar texto HTML ao Documento PDF

A biblioteca Aspose.PDF for Python via .NET permite inserir conteúdo formatado em HTML em um documento PDF usando a classe HtmlFragment. Ao usar tags HTML, você pode renderizar texto com estilo, estruturado ou semelhante a fórmulas diretamente em um PDF.

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Crie uma instância da classe HtmlFragment e passe sua string HTML como parâmetro.
1. Adicione o fragmento à página usando 'page.paragraphs.add()' para inserir o conteúdo HTML.
1. Salvar o PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_html_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Adicionar texto HTML a um Documento PDF](html_fragment.png)

### Adicionar fragmento HTML estilizado com várias formatações a um documento PDF

Podemos definir um fragmento HTML e definir o estilo do texto diretamente usando tags HTML. Incorporar conteúdo HTML estilizado em um documento PDF. Este trecho de código cria um novo arquivo PDF, adiciona uma página, insere um fragmento HTML com vários elementos de formatação (títulos, parágrafos, links e estilos embutidos), e salva o resultado no caminho especificado.

1. Inicializa um novo objeto Document para representar o PDF.
1. Anexa uma página em branco ao documento onde o conteúdo HTML será colocado.
1. Prepare o conteúdo HTML. A string HTML contém um cabeçalho h1, um parágrafo de cor verde com texto em negrito, itálico e sublinhado, e um hyperlink para um site com tamanho de fonte aumentado.
1. Criar Fragmento HTML. Envolva a string HTML em um objeto HtmlFragment.
1. Inserir HTML na Página. Adiciona o fragmento HTML à coleção de parágrafos da página, renderizando o HTML como conteúdo PDF nativo.
1. Salvar o Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment(output_file_name):
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
    document.save(output_file_name)
```

![Adicionar conteúdo HTML a um documento PDF](html_content.png)

### Adicionar fragmento HTML com estado de texto substituído

Como vimos no exemplo anterior, é possível definir estilos diretamente no código HTML. Isso tem suas vantagens, mas também algumas desvantagens. Suponha que estamos trabalhando com o HTML de um cliente e queremos unificar a aparência da nossa saída.
Neste caso, podemos substituir o estilo do cliente usando nosso próprio TextState, como mostrado no exemplo a seguir.

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Prepare o conteúdo HTML. A string HTML contém um cabeçalho h1 com fonte Verdana, um parágrafo em verde com texto em negrito, itálico e sublinhado, e um hyperlink para um site com tamanho de fonte maior.
1. Criar Fragmento HTML. Envolva a string HTML em um objeto HtmlFragment.
1. Substitua a formatação de texto. Crie um objeto TextState e defina a Fonte, o Tamanho da Fonte e a Cor do Texto.
1. Adicione o fragmento HTML à coleção de parágrafos da página.
1. Salvar o Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment_override_text_state(output_file_name):
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
    document.save(output_file_name)
```

![Adicionar estado de sobrescrita de texto do fragmento HTML](html_override.png)

### Adicionar texto LaTeX ao documento PDF

Adicionar expressões matemáticas formatadas em LaTeX a um documento PDF usando a classe TeXFragment no Aspose.PDF for Python via .NET.
LaTeX é um poderoso sistema de composição tipográfica amplamente usado para criar documentos científicos e matemáticos. Usando o TeXFragment, você pode renderizar diretamente a notação e os símbolos matemáticos em LaTeX dentro de uma página PDF.

1. Crie um novo documento e página usando 'Document()', e 'document.pages.add()' para adicionar uma página em branco.
1. Use a classe TeXFragment para renderizar a sintaxe LaTeX diretamente.
1. Adicione o conteúdo LaTeX ao layout do PDF com 'page.paragraphs.add()'.
1. Salvar o PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_latex_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Expressão matemática complexa exibida em um PDF mostrando a fórmula LaTeX com notação overbrace sobre (a+b)⁶, notação underbrace sob a expressão inteira (a+b)⁶ · (c+d)⁷, rotulada como exemplo de texto, e igual a 42. A fórmula demonstra tipografia matemática avançada com espaçamento adequado e estilo de colchetes típico da renderização LaTeX](latex_fragment.png)

## Fontes personalizadas

### Use uma Font personalizada a partir de um arquivo

Este exemplo permite que você adicione texto a um arquivo PDF usando uma fonte OpenType personalizada no Aspose.PDF for Python via .NET. Ele mostra como criar um novo documento PDF, posicionar o texto com precisão na página e aplicar formatação personalizada, como tipo de fonte, tamanho, cor e estilo itálico.

1. Crie um novo documento PDF e adicione uma página.
1. Defina o conteúdo de texto que você deseja adicionar ao PDF.
1. Defina a posição do texto.
1. Adicione o TextFragment à página.
1. Salve o documento PDF.

Esta função funciona não apenas com fontes OTF, mas também com fontes TTF.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_file(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![Fragmento de texto exibido em um documento PDF mostrando Hello, Aspose! renderizado em fonte BriosoPro azul itálico, demonstrando a integração de fontes OpenType personalizadas e as capacidades de estilização dentro da formatação de texto PDF](custom_font.png)

### Use uma Font personalizada a partir de um stream

Este trecho de código demonstra como adicionar texto a um documento PDF usando uma fonte OpenType (OTF) personalizada incorporada com Aspose.PDF for Python via .NET. Ele mostra como abrir um arquivo de fonte como um fluxo, incorporá-lo ao PDF para garantir a disponibilidade da fonte em diferentes sistemas e aplicar formatação de texto, como tamanho da fonte, cor e estilo itálico. Essa abordagem é ideal para criar PDFs visualmente consistentes que preservam a tipografia mesmo quando compartilhados ou visualizados em dispositivos sem a fonte instalada.

1. Carregue o arquivo de fonte como um fluxo binário.
1. Abra e incorpore a fonte usando 'FontRepository.open_font'.
1. Crie um novo documento PDF e adicione uma página.
1. Adicionar um fragmento de texto estilizado com:
    - Fonte personalizada incorporada.
    - Estilo itálico e cor azul.
    - Tamanho de fonte específico e posição.
1. Salve o documento final em um caminho de saída especificado.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_stream(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
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
        document.save(output_file_name)
```

Incorporar fontes garante renderização consistente em todas as plataformas, tornando essa abordagem ideal para branding, fidelidade de design e suporte multilíngue.

## Tópicos de Texto Relacionados

- [Trabalhe com texto em PDF usando Python](/pdf/pt/python-net/working-with-text/)
- [Formatar texto PDF em Python](/pdf/pt/python-net/text-formatting-inside-pdf/)
- [Substituir texto em PDF via Python](/pdf/pt/python-net/replace-text-in-pdf/)
- [Pesquisar e extrair texto de PDF em Python](/pdf/pt/python-net/search-and-get-text-from-pdf/)