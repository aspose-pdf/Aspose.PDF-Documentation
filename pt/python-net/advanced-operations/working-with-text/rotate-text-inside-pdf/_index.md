---
title: Rotacionar Texto Dentro de PDF usando Python
linktitle: Rotacionar Texto Dentro de PDF
type: docs
weight: 50
url: /pt/python-net/rotate-text-inside-pdf/
description: Explore how to rotate text inside a PDF document in Python for flexible document formatting with Aspose.PDF for Python.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como rotacionar Texto em PDF com Python
Abstract: O artigo fornece um guia detalhado sobre como rotacionar texto dentro de um documento PDF usando a biblioteca Aspose.PDF para Python via .NET. Ele descreve a utilização da propriedade `Rotation` da classe `TextFragment` para alcançar rotação de texto em vários ângulos, o que é útil em múltiplos cenários de geração de documentos. Demonstra a criação de fragmentos de texto com ângulos de rotação especificados e sua adição a uma página PDF usando um `TextBuilder`. Ilustra como anexar fragmentos de texto rotacionados a um `TextParagraph` e então adicionar o parágrafo a uma página PDF. Mostra como adicionar fragmentos de texto rotacionados diretamente à coleção de parágrafos da página. Explica a rotação de um parágrafo inteiro com múltiplos fragmentos de texto.
---

Rotacione fragmentos de texto em um documento PDF usando Aspose.PDF para Python via .NET. Ele mostra como controlar com precisão a posição e a rotação de elementos de texto individuais combinando as classes 'TextFragment', 'TextState' e 'TextBuilder'. Ajustando o ângulo de rotação de cada fragmento de texto, você pode criar layouts visualmente dinâmicos, como cabeçalhos diagonais, rótulos verticais ou anotações rotacionadas.

## Rotacionar Fragmentos de Texto Usando TextBuilder em PDF

Cria um arquivo PDF chamado rotated_fragments.pdf contendo três fragmentos de texto alinhados horizontalmente:

- o primeiro texto não está rotacionado
- o segundo está rotacionado 45°
- o terceiro está rotacionado 90°

1. Crie um Novo Documento PDF.
1. Insira uma nova página para hospedar o texto rotacionado.
1. Crie o Primeiro Fragmento de Texto - Sem Rotação.
1. Crie o Segundo Fragmento de Texto - Rotação de 45°.
1. Crie o Terceiro Fragmento de Texto - Rotação de 90°.
1. Adicione Fragmentos de Texto Usando TextBuilder.
1. Salve o Documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotacionar Fragmentos de Texto Individuais Dentro de um Parágrafo em PDF

Rotacione fragmentos de texto individuais dentro de um parágrafo. Ele mostra como construir um parágrafo de várias linhas (TextParagraph) contendo múltiplos fragmentos (TextFragment), cada um com seu próprio ângulo de rotação. Esta técnica é útil para criar documentos visualmente ricos que combinam texto orientado horizontalmente e diagonalmente — por exemplo, cabeçalhos estilizados, diagramas ou rótulos anotados.

Cria um PDF chamado rotated_paragraph_fragments.pdf contendo um parágrafo com três linhas de texto, cada linha rotacionada de forma diferente:

- a primeira linha está rotacionada 45°
- a segunda linha permanece horizontal (0°)
- a terceira linha está rotacionada -45°

1. Crie um Novo Documento PDF.
1. Adicione uma página em branco onde o texto rotacionado aparecerá.
1. Crie um TextParagraph.
1. Crie e Configure o Primeiro Fragmento de Texto - Rotação de 45°.
1. Crie o Segundo Fragmento de Texto - Sem Rotação.
1. Crie o Terceiro Fragmento de Texto - Rotação de 45°.
1. Anexe Fragmentos de Texto ao Parágrafo.
1. Adicione o Parágrafo à Página Usando TextBuilder.
1. Salve o Documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Rotacionar Texto Usando Parágrafos de Página em PDF

Método simplificado para rotacionar texto dentro de um PDF usando Aspose.PDF para Python via .NET.
Ao contrário de abordagens de nível mais baixo com TextBuilder ou TextParagraph, este método adiciona fragmentos de texto rotacionados diretamente à coleção de parágrafos da página (page.paragraphs). É ideal para casos em que você precisa de rotação de texto básica, mas não requer posicionamento preciso ou estruturação de parágrafos. Esta abordagem simplifica a criação de layout, manipulando automaticamente a colocação do texto na página, ao mesmo tempo permitindo controle individual de rotação de texto.

Gera um arquivo chamado 'simple_rotated_text.pdf' contendo:

- um fragmento de texto horizontal principal com rotação 0°
- fragmento rotacionado 315°
- fragmento rotacionado 270°

1. Inicialize um novo documento PDF.
1. Crie uma página onde o texto rotacionado será colocado.
1. Crie o Primeiro Fragmento de Texto - Sem Rotação.
1. Crie o Segundo Fragmento de Texto - Rotação de 315°.
1. Crie o Terceiro Fragmento de Texto - Rotação de 270°.
1. Adicione Fragmentos de Texto Diretamente aos Parágrafos da Página.
1. Salve o Documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotacione Parágrafos Inteiros em um PDF

Nossa biblioteca demonstra rotação avançada de texto em nível de parágrafo em um PDF. Diferente da rotação em nível de fragmento (onde cada pedaço de texto é rotacionado individualmente), este método gira parágrafos inteiros como blocos unificados em ângulos diferentes.
Cada parágrafo contém múltiplos fragmentos de texto estilizados, e o parágrafo completo é rotacionado em ângulos específicos — permitindo transformações de layout complexas e consistentes.
Isso é ideal para layouts artísticos, marcas d'água ou PDFs com muito design, onde seções de texto inteiras precisam ser orientadas em várias direções.

Cria 'rotated_paragraphs.pdf', contendo quatro parágrafos totalmente estilizados e rotacionados:

- cada um rotacionado em um ângulo único (45°, 135°, 225° e 315°)
- cada parágrafo tem três linhas de texto com fundos coloridos, sublinhado e estilização consistente

1. Crie um Novo Documento PDF.
1. Adicione uma página em branco para conter os parágrafos rotacionados.
1. Itere para Criar Múltiplos Parágrafos.
1. Crie e Posicione o Parágrafo.
1. Crie Fragmentos de Texto com Formatação.
1. Aplique Formatação de Texto.
1. Adicione Fragmentos de Texto ao Parágrafo.
1. Anexe o Parágrafo à Página Usando TextBuilder.
1. Repita para Todas as Quatro Rotações.
1. Salve o Documento PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```
