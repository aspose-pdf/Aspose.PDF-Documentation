---
title: Usando FloatingBox para geração de texto com Python
linktitle: Usando FloatingBox
type: docs
weight: 30
url: /pt/python-net/floating-box/
description: Esta página explica como formatar texto dentro de uma caixa flutuante.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: A ferramenta FloatingBox para geração de texto
Abstract: Este artigo oferece um guia abrangente sobre como usar a ferramenta FloatingBox no Aspose.PDF para Python, que permite aos desenvolvedores colocar texto e outros conteúdos em contêineres móveis e estilizados nas páginas PDF. Ele cobre tanto o uso básico quanto o avançado, demonstrando como criar caixas flutuantes, aplicar bordas e cores de fundo, controlar layouts de múltiplas colunas, gerenciar o posicionamento de parágrafos e alinhar as caixas vertical e horizontalmente. O artigo também destaca recursos‑chave como recorte de texto, conteúdo repetido em várias páginas, posicionamento absoluto e controle aprimorado de layout, permitindo a personalização precisa do conteúdo PDF. Por meio de exemplos práticos de código, os leitores aprendem a criar PDFs visualmente atraentes e bem estruturados que aproveitam todo o potencial do contêiner FloatingBox.
---

## Conceitos básicos de uso da ferramenta FloatingBox

A ferramenta [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) é um contêiner especializado para posicionar texto e outros conteúdos em uma página PDF. Seu principal recurso é o recorte de texto quando o conteúdo ultrapassa os limites da caixa. Crie e adicione um `FloatingBox` a um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando Aspose.PDF para Python. Um `FloatingBox` funciona como um contêiner de texto móvel, permitindo maior controle sobre o posicionamento do layout, bordas e estilização em comparação com parágrafos de texto regulares.

1. Crie um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Adicione uma [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ao documento.
1. Crie um [`FloatingBox`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/).
1. Defina a borda da caixa usando [`BorderInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) e [`BorderSide`](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderside/).
1. Controle a repetição da caixa com a propriedade [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties).
1. Adicione conteúdo de texto usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/).
1. Adicione o `FloatingBox` à [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Salve o documento PDF final usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def create_and_add_floating_box(outfile):
    """
    Create and add a basic floating box to a PDF document.

    Demonstrates the fundamental usage of FloatingBox to create a bordered
    text container with Lorem ipsum content. Shows basic box creation,
    styling, and text content addition.

    Args:
        outfile (str): Path where the PDF with floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a floating box.

    Note:
        - Creates a FloatingBox with dimensions 400x30
        - Applies dark green border with 1.5 width
        - Sets is_need_repeating to False for single occurrence
        - Contains Lorem ipsum text fragment
        - Demonstrates basic floating box functionality

    Example:
        >>> create_and_add_floating_box("basic_floating_box.pdf")
        # Creates a PDF with a simple bordered floating text box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.is_need_repeating = False
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        box.paragraphs.add(ap.text.TextFragment(phrase))
        # Add box
        page.paragraphs.add(box)
        document.save(outfile)
```  

No exemplo acima, estamos criando um FloatingBox com largura de 400 pt e altura de 30 pt.
Além disso, neste exemplo, mais texto foi intencionalmente criado do que cabe no tamanho dado.
Como resultado, o texto foi cortado.

![Image 1](image01.png)

A propriedade [`is_need_repeating`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) com valor `False` limita o texto a uma única página.

Se definirmos esta propriedade como `True`, o texto será redistribuído para as páginas subsequentes na mesma posição.

![Image 2](image02.png)

## Recursos avançados do FloatingBox

### Suporte a múltiplas colunas

#### Layout de múltiplas colunas (caso simples)

O `FloatingBox` suporta layout de múltiplas colunas. Para criar esse layout, você deve definir os valores das propriedades [`ColumnInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/columninfo/).

* `column_widths` é uma string com enumeração de larguras em pt.
* `column_spacing` é uma string com a largura do intervalo entre colunas.
* `column_count` é um número de colunas.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout(outfile):
    """
    Create a multi-column layout using FloatingBox.

    Demonstrates advanced layout capabilities by creating a three-column
    text layout within a floating box. Shows dynamic width calculation
    and column spacing configuration.

    Args:
        outfile (str): Path where the PDF with multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with multi-column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Calculates column width based on page margins and spacing
        - Uses is_need_repeating for content continuation across columns
        - Adds multiple Lorem ipsum paragraphs for column demonstration
        - Automatically distributes content across columns

    Example:
        >>> multi_column_layout("multi_column.pdf")
        # Creates a PDF with text arranged in three columns
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            box.paragraphs.add(ap.text.TextFragment(paragraph))
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

Usamos a biblioteca adicional LoremNET no exemplo acima e criamos 20 parágrafos. Esses parágrafos foram divididos em três colunas e preencheram as páginas seguintes até que o texto se esgotasse.

#### Layout de múltiplas colunas com início de coluna forçado

Faremos o mesmo com o exemplo a seguir como o anterior. A diferença é que criamos 3 parágrafos. Podemos forçar o FloatingBox a renderizar cada parágrafo na nova coluna. Para isso, precisamos definir `is_first_paragraph_in_column` ao adicionar texto ao objeto FloatingBox.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def multi_column_layout_2(outfile):
    """
    Create a multi-column layout with paragraph column control.

    Demonstrates advanced multi-column layout with explicit control over
    paragraph positioning within columns. Uses is_first_paragraph_in_column
    to control text flow and column breaks.

    Args:
        outfile (str): Path where the PDF with controlled multi-column layout will be saved.

    Returns:
        None: The function creates and saves a PDF file with controlled column text.

    Note:
        - Creates 3 equal-width columns with 10-unit spacing
        - Uses is_first_paragraph_in_column for explicit column control
        - Calculates column width dynamically based on page dimensions
        - Demonstrates precise paragraph positioning within columns
        - Shows advanced column layout management techniques

    Example:
        >>> multi_column_layout_2("controlled_columns.pdf")
        # Creates a PDF with precisely controlled multi-column text flow
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Set margin settings
        page.page_info.margin = ap.MarginInfo(36, 18, 36, 18)
        column_count = 3
        spacing = 10
        width = (
            page.page_info.width
            - page.page_info.margin.left
            - page.page_info.margin.right
            - (column_count - 1) * spacing
        )
        column_width = width / 3
        # Create FloatingBox
        box = ap.FloatingBox()
        box.is_need_repeating = True
        box.column_info.column_widths = f"{column_width} {column_width} {column_width}"
        box.column_info.column_spacing = f"{spacing}"
        box.column_info.column_count = 3
        phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi."
        paragraphs = [
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
            phrase,
        ]
        for paragraph in paragraphs:
            text = ap.text.TextFragment(paragraph)
            text.is_first_paragraph_in_column = True
            box.paragraphs.add(text)
        # Add a box to a page
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Suporte a plano de fundo

Aplique uma cor de fundo a um FloatingBox em um documento PDF usando Aspose.PDF para Python via .NET.
Um `FloatingBox` é um contêiner para texto ou outros elementos, e ao atribuir um [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) como cor de fundo, você pode fazer o conteúdo se destacar visualmente — útil para cabeçalhos, realces ou seções estilizadas.

Este trecho de código mostra como criar uma caixa de texto verde‑clara simples com conteúdo de exemplo.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def background_support(outfile):
    """
    Demonstrate FloatingBox background color support.

    Shows how to apply background colors to floating boxes to create
    visually distinct text containers. Demonstrates basic styling
    capabilities for enhanced visual presentation.

    Args:
        outfile (str): Path where the PDF with colored background box will be saved.

    Returns:
        None: The function creates and saves a PDF file with a colored floating box.

    Note:
        - Applies light green background color to the floating box
        - Creates a 400x30 box with sample text content
        - Sets is_need_repeating to False for single occurrence
        - Demonstrates visual styling options for floating boxes
        - Shows how background colors enhance text presentation

    Example:
        >>> background_support("colored_background.pdf")
        # Creates a PDF with a light green background floating box
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.background_color = ap.Color.light_green
        box.is_need_repeating = False
        box.paragraphs.add(ap.text.TextFragment("text example"))
        # Add box
        page.paragraphs.add(box)
        # Save PDF document
        document.save(outfile)
```

### Suporte a posicionamento

A localização do FloatingBox na página gerada é determinada pelas propriedades `positioning_mode`, `left`, `top`.
Quando o valor de `positioning_mode` é

* [`ParagraphPositioningMode.DEFAULT`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/) (valor padrão)

A localização é determinada pelos elementos previamente colocados; adicionar um elemento afeta a localização dos elementos subsequentes. Se [`Left`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) ou [`Top`](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/#properties) forem diferentes de zero, também são considerados, mas a lógica combinada pode não ser óbvia.

* [`ParagraphPositioningMode.ABSOLUTE`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paragraphpositioningmode/)

A localização é especificada pelos valores `Left` e `Top`; não depende dos elementos anteriores e não afeta a localização dos subsequentes.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def offset_support(outfile):
    """
    Demonstrate FloatingBox positioning and offset support.

    Shows how to position floating boxes at specific coordinates using
    absolute positioning mode. Demonstrates integration of floating boxes
    with regular text content and precise layout control.

    Args:
        outfile (str): Path where the PDF with positioned floating box will be saved.

    Returns:
        None: The function creates and saves a PDF file with positioned floating box.

    Note:
        - Uses absolute positioning mode for precise box placement
        - Sets box position to top=45, left=15 coordinates
        - Creates bordered box with dark green border
        - Integrates floating box with regular text paragraphs
        - Demonstrates layered content with mixed positioning

    Example:
        >>> offset_support("positioned_box.pdf")
        # Creates a PDF with a floating box at specific coordinates
    """

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create and fill box
        box = ap.FloatingBox(400, 30)
        box.top = 45
        box.left = 15
        box.positioning_mode = ap.ParagraphPositioningMode.ABSOLUTE
        box.border = ap.BorderInfo(ap.BorderSide.ALL, 1.5, ap.Color.dark_green)
        box.paragraphs.add(ap.text.TextFragment("text example 1"))
        page.paragraphs.add(ap.text.TextFragment("text example 2"))
        # Add the box to the page
        page.paragraphs.add(box)
        page.paragraphs.add(ap.text.TextFragment("text example 3"))
        document.save(outfile)
```

### Alinhar Caixas Flutuantes com Alinhamento Vertical e Horizontal em PDF

Alinhe elementos `FloatingBox` dentro de uma página PDF usando diferentes opções de [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) e [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) no Aspose.PDF para Python via .NET. Ele mostra como controlar o posicionamento do layout (topo, centro, inferior, esquerda, direita) para alcançar um alinhamento visual preciso de contêineres flutuantes. Cada caixa flutuante recebe uma posição distinta para demonstrar a flexibilidade de alinhamento para layout de página, posicionamento de cabeçalho/rodapé ou anotações laterais.

1. Crie um Novo Documento PDF.
1. Adicione uma Página ao Documento.
1. Crie o Primeiro FloatingBox (Alinhamento Inferior-Direito).
1. Crie o Segundo FloatingBox (Alinhamento Central-Direito).
1. Crie o Terceiro FloatingBox (Alinhamento Superior-Direito).
1. Salve o Documento.

```python

import math
import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def align_text_to_float(outfile):
    """
    Demonstrate text alignment options for FloatingBox elements.

    Shows different vertical and horizontal alignment options for floating
    boxes. Creates multiple boxes with different alignment settings to
    demonstrate positioning flexibility.

    Args:
        outfile (str): Path where the PDF with aligned floating boxes will be saved.

    Returns:
        None: The function creates and saves a PDF file with variously aligned boxes.

    Note:
        - Creates three 100x100 floating boxes with different alignments
        - First box: bottom-right alignment
        - Second box: center-right alignment
        - Third box: top-right alignment
        - All boxes have blue borders for visual distinction
        - Demonstrates comprehensive alignment control options

    Example:
        >>> align_text_to_float("aligned_boxes.pdf")
        # Creates a PDF with floating boxes in different alignment positions
    """
    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(outfile)
```
