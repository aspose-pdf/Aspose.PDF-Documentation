---
title: Pesquisar e Obter Texto das Páginas de PDF
linktitle: Pesquisar e Obter Texto
type: docs
weight: 60
url: /pt/python-net/search-and-get-text-from-pdf/
description: Aprenda como pesquisar e extrair texto de documentos PDF em Python usando Aspose.PDF para análise de documentos.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Pesquisar e Obter Texto das Páginas em PDF
Abstract: O artigo oferece uma exploração aprofundada das capacidades de extração e manipulação de texto em documentos PDF usando a biblioteca Aspose.PDF for Python via .NET. Ele apresenta a classe TextFragmentAbsorber, que permite aos desenvolvedores pesquisar em todo o documento ou em páginas específicas por frases designadas ou padrões de expressão regular. A página descreve vários cenários práticos — como recuperar o conteúdo do texto, determinar sua posição (incluindo coordenadas e valores de recuo) e extrair propriedades da fonte como nome, tamanho, status de incorporação e cor — dos fragmentos de texto correspondentes. Exemplos de código detalhados demonstram o processo passo a passo, facilitando a integração de recursos de pesquisa de texto nas aplicações dos desenvolvedores.
---

## Pesquisar Texto em PDF

Pesquisar e extrair texto de uma área retangular definida em um documento PDF usando a classe TextAbsorber. Ela utiliza o modo de formatação de texto puro para gerar uma saída limpa e não formatada, tornando-a ideal para extrair conteúdo de regiões estruturadas como cabeçalhos, rodapés ou áreas de tabelas. Ao combinar TextExtractionOptions e TextSearchOptions com restrições retangulares, este exemplo oferece controle fino sobre onde e como o texto é extraído do documento.

1. Carregue o arquivo PDF usando 'ap.Document'.
1. Configure as Opções de Extração de Texto.
1. Defina a Área de Busca com Restrições Retangulares.
1. Crie e Configure o TextAbsorber.
1. Processar Todas as Páginas do Documento.
1. Recuperar e Exibir o Texto Extraído.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search(input_file_path):
    """
    Search and extract text from PDF using TextAbsorber with area constraints.

    Demonstrates basic text extraction from a PDF document using TextAbsorber
    with pure text formatting mode and rectangular boundary constraints.
    Extracts text from all pages within the specified rectangular area.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text to console.

    Note:
        - Uses PURE text formatting mode for clean text extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Processes all pages in the document
        - TextAbsorber provides high-level text extraction capabilities
        - Good for extracting text content without detailed positioning

    Example:
        >>> text_absorber_search("document.pdf")
        # Prints all text found in the specified rectangular area across all pages
    """
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Pesquisar Texto de uma Página PDF Específica

Pesquisar e extrair texto de uma página e região específicas em um PDF usando o TextAbsorber da Aspose.PDF. Ele foca na página 2 do documento e extrai apenas o texto encontrado dentro de uma área retangular definida.
Ao combinar TextExtractionOptions (para controle de formatação) e TextSearchOptions (para limitação de área), você pode realizar extração de texto precisa e específica por página de forma eficiente.

1. Carregue o Documento PDF.
1. Configure as Opções de Extração de Texto.
1. Restrinja a extração de texto a uma área retangular específica na página.
1. Crie e Configure o TextAbsorber.
1. Processar uma Página Específica.
1. Recuperar e Exibir o Texto Extraído.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search_page(input_file_path):
    """
    Search and extract text from a specific PDF page using TextAbsorber.

    Demonstrates targeted text extraction from a single page (page 2) using
    TextAbsorber with area constraints. Shows how to limit search scope to
    specific pages and rectangular regions.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text from page 2 to console.

    Note:
        - Targets only page 2 of the document (document.pages[2])
        - Uses PURE text formatting mode for clean extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Useful for page-specific text extraction
        - More efficient than processing entire document when targeting specific pages

    Example:
        >>> text_absorber_search_page("document.pdf")
        # Prints text found in the specified area on page 2 only
    """
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")

```

## Analisar e Extrair Propriedades Detalhadas de Fragmentos de Texto de um PDF

Ao contrário do TextAbsorber, que extrai texto bruto, o TextFragmentAbsorber fornece informações detalhadas e de baixo nível sobre cada fragmento de texto — como sua posição, atributos da fonte, cor e detalhes de incorporação.

1. Carregue o Documento PDF.
1. Inicializar o TextFragmentAbsorber.
1. Processar Todas as Páginas do Documento.
1. Iterar pelos Fragmentos de Texto Extraídos.
1. Imprimir Informações Básicas do Texto.
1. Imprimir Detalhes da Fonte e Formatação.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search(input_file_path):
    """
    Search and analyze all text fragments in a PDF with detailed properties.

    Demonstrates comprehensive text fragment analysis using TextFragmentAbsorber
    to extract all text with detailed positioning, font, and formatting information.
    Provides low-level access to text properties for detailed analysis.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints detailed text fragment information to console.

    Note:
        - Extracts all text fragments from all pages
        - Provides detailed properties: position, font info, colors, sizes
        - Shows font accessibility, embedding, and subset information
        - Useful for detailed text analysis and formatting inspection
        - TextFragmentAbsorber offers more granular control than TextAbsorber

    Example:
        >>> text_fragment_absorber_search("document.pdf")
        # Prints comprehensive details about every text fragment in the document
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## Pesquisar por uma Frase de Texto Específica em uma Única Página PDF

Pesquisar por uma frase de texto específica dentro de uma página de um documento PDF usando o TextFragmentAbsorber. Ao contrário da pesquisa em todo o documento, esta abordagem limita a busca a apenas uma página, tornando-a mais eficiente para confirmar a presença e a localização do texto em áreas direcionadas como cabeçalhos, rodapés ou seções de conteúdo específicas.

1. Carregue o Documento PDF.
1. Inicializar o TextFragmentAbsorber com a Frase de Busca.
1. Aplicar o Absorber à Página Específica.
1. Iterar Sobre os Fragmentos Encontrados.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_page(input_file_path):
    """
    Search for specific text phrase on a particular PDF page.

    Demonstrates targeted text search for a specific phrase ("whale") on
    a single page. Shows how to combine phrase searching with page-specific
    scope for efficient and focused text location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and their positions to console.

    Note:
        - Searches for the phrase "whale" on page 2 only
        - Returns text fragments with position information
        - More efficient than document-wide search when targeting specific pages
        - Useful for validating content presence in specific document sections
        - Provides exact positioning coordinates for found text

    Example:
        >>> text_fragment_absorber_search_page("document.pdf")
        # Prints all instances of "whale" found on page 2 with their positions
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Busca Sequencial de Texto Página a Página com Resultados Cumulativos

Pesquisar texto incrementalmente em várias páginas de um documento PDF usando o TextFragmentAbsorber da Aspose.PDF.
Ao contrário de uma busca de página única ou em todo o documento, esta abordagem permite processar as páginas sequencialmente, coletar resultados progressivamente e analisar fragmentos de texto com contexto específico de página. Esse método é ideal para documentos grandes ou fluxos de trabalho de processamento progressivo.

1. Carregue o Documento PDF.
1. Inicializar o TextFragmentAbsorber e Definir a Frase de Busca.
1. Processar a Primeira Página. Pesquisar somente a página 1. Imprime texto, número da página e posição. Fornece resultados isolados específicos da página para clareza.
1. Processar a página seguinte sequencialmente. Mova para a página 2 e, opcionalmente, continue através do restante do documento. O 'absorber.visit()' garante a acumulação de resultados de todas as páginas visitadas. Imprime os resultados de busca cumulativos, mostrando tanto o texto quanto a localização.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_sequential_search(input_file_path):
    """
    Demonstrate sequential page-by-page text search with cumulative results.

    Shows how to perform incremental text searches across multiple pages,
    accumulating results from each page. Demonstrates both individual page
    processing and document-wide search continuation.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints text fragments from sequential page searches to console.

    Note:
        - Searches for "whale" on page 1, then continues to page 2
        - Uses absorber.visit(document) to process remaining pages
        - Demonstrates incremental search accumulation
        - Shows page numbers for found fragments
        - Useful for progressive document processing and result accumulation

    Example:
        >>> text_fragment_absorber_sequential_search("document.pdf")
        # Prints "whale" instances from page 1, then from all remaining pages
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## Busca de Frase Direcionada dentro de uma Área Retangular

Buscar uma frase específica dentro de um PDF, restringindo a busca a uma área retangular específica em uma única página.
Ao combinar a busca de frases com restrições espaciais, você pode localizar conteúdo com precisão em regiões designadas sem analisar toda a página ou documento. Isso é particularmente útil para formulários, cabeçalhos, rodapés ou relatórios estruturados onde o conteúdo aparece em locais previsíveis.

1. Carregar o Documento PDF.
1. Inicializar TextFragmentAbsorber com Frase e Restrições Retangulares
1. Aplicar o Absorber na Página 2. Restringe o processamento à página 2, reduzindo cálculos desnecessários. Garante que a busca seja específica da página.
1. Iterar pelos Fragmentos Encontrados e Imprimir

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_phrase(input_file_path):
    """
    Search for specific phrase within a rectangular area constraint.

    Demonstrates targeted phrase searching with both text matching and
    spatial constraints. Combines phrase search with rectangular boundary
    limitations for precise content location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Searches for "elephant" phrase on page 2
        - Constrains search to rectangle (0, 0, 842, 250)
        - Combines text matching with spatial filtering
        - Useful for finding content in specific document regions
        - More precise than page-wide or document-wide searches

    Example:
        >>> text_fragment_absorber_search_phrase("document.pdf")
        # Prints "elephant" instances found within the specified rectangular area on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Busca de Padrões de Texto em PDF Usando Expressões Regulares

Buscar padrões de texto em um PDF usando expressões regulares. Ao habilitar o modo regex no TextFragmentAbsorber, você pode localizar padrões complexos como números, datas, preços, coordenadas ou formatos de texto personalizados. A função limita a busca a uma página específica, tornando-a eficiente para extração direcionada de dados estruturados.

1. Carregar o Documento PDF.
1. Inicializar TextFragmentAbsorber com Padrão Regex.
1. Aplicar o Absorber na Página 2. Limita a busca à página 2 para eficiência e precisão. Apenas o texto desta página é analisado.
1. Iterar pelos Fragmentos Encontrados. Imprime os fragmentos de texto correspondentes e suas coordenadas. Fornece informações de localização precisas para os padrões extraídos.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_regex(input_file_path):
    """
    Search for text patterns using regular expressions.

    Demonstrates advanced text searching using regular expression patterns
    to find complex text structures like numbers, dates, or custom formats.
    Shows how to enable regex mode in TextFragmentAbsorber.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Uses regex pattern r"\\d+\\.\\d+" to find decimal numbers
        - Enables regex mode with is_regular_expression_used=True
        - Searches on page 2 only
        - Powerful for finding formatted data like prices, coordinates, dates
        - Regular expressions provide flexible pattern matching capabilities

    Example:
        >>> text_fragment_absorber_search_regex("document.pdf")
        # Prints all decimal numbers (e.g., "12.34", "0.99") found on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True))

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Converter Correspondências de Texto em Hiperligações no PDF Usando TextFragmentAbsorber

Buscar frases de texto específicas em um PDF e convertê‑las em hiperligações clicáveis. Usando TextFragmentAbsorber com padrões regex, ele localiza palavras‑alvo e aplica estilo visual (cor e sublinhado) juntamente com links interativos.

1. Carregar o Documento PDF.
1. Inicializar TextFragmentAbsorber com Padrão Regex.
1. Aplicar o Absorber na Página 1.
1. Estilizar e Adicionar Hiperligações às Correspondências.
1. Salvar o PDF Modificado.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    """
    Search for text and convert matches to hyperlinks with styling.

    Demonstrates advanced text processing by finding specific words and
    converting them into clickable hyperlinks with visual styling. Shows
    how to combine text search with document modification.

    Args:
        input_file_path (str): Path to the input PDF file to process.

    Returns:
        None: Saves modified PDF with hyperlinks to output file.

    Note:
        - Searches for "whale|elephant" using regex pattern on page 1
        - Converts found text to Wikipedia hyperlinks
        - Applies blue color and underline styling to hyperlinks
        - Creates new output file with "_out.pdf" suffix
        - Demonstrates practical text enhancement and interactivity
        - Combines search, styling, and hyperlinking in one operation

    Example:
        >>> text_fragment_absorber_search_and_add_hyperlink("document_in.pdf")
        # Creates "document_out.pdf" with "whale" and "elephant" as clickable Wikipedia links
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## Buscar e Identificar Texto Estilizado em PDF Usando TextFragmentAbsorber

Buscar fragmentos de texto em um PDF com base em suas propriedades de formatação, e não no seu conteúdo. Usando TextFragmentAbsorber, ele identifica texto com estilos específicos, como texto em negrito.

1. Carregar o Documento PDF.
1. Inicializar TextFragmentAbsorber.
1. Aplicar o Absorber na Página 1.
1. Inspecionar Fragmentos de Texto com Base na Formatação. Verifica o estilo da fonte para formatação em negrito.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
```

Detecta texto oculto ou invisível em um documento PDF ao analisar as propriedades de formatação do texto:

1. Carregar o Documento PDF.
1. Inicializar TextFragmentAbsorber.
1. Aplicar o Absorber na Página 1.
1. Inspecionar Fragmentos de Texto com Base na Formatação. Verifique 'fragment.text_state.invisible' para texto oculto.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Realce Visual de Texto em Páginas PDF

Esta função combina reconhecimento de texto e renderização em um único fluxo de trabalho. Ela não apenas extrai o texto, mas também o visualiza destacando fragmentos, segmentos e caracteres em retângulos codificados por cores nas imagens PNG de cada página.

Nosso exemplo realiza visualização avançada de texto em um PDF ao:

- pesquisar todos os fragmentos de texto visíveis usando expressões regulares
- renderizar cada página do PDF em uma imagem PNG de alta resolução
- desenhar retângulos coloridos ao redor de fragmentos de texto, segmentos de texto e caracteres individuais

1. Definir Resolução da Imagem de Saída. Cada página PDF é convertida em uma imagem PNG de 150 DPI.
1. Abrir o PDF e Inicializar o Text Absorber.
1. Processar Cada Página. Aplicar o absorber em cada página. Coletar todos os fragmentos de texto detectados e suas posições geométricas.
1. Converter a Página para um Stream PNG.
1. Preparar o Objeto Gráfico para Desenho.
1. Aplicar Transformação de Coordenadas. Converter coordenadas PDF para pixels da imagem.
1. Desenhar Retângulos para Elementos de Texto.
1. Salvar o Resultado.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_highlight(infile):
    """
    Search text and create visual highlighting with PNG output.

    Advanced function that combines text search with visual highlighting.
    Converts PDF pages to PNG images and draws colored rectangles around
    found text fragments, segments, and individual characters.

    Args:
        infile (str): Path to the input PDF file to process.

    Returns:
        None: Saves highlighted PNG images for each page.

    Note:
        - Uses regex pattern r"[\\S]+" to find all non-whitespace sequences
        - Converts each page to 150 DPI PNG image using PngDevice
        - Draws yellow rectangles around text fragments
        - Draws green rectangles around text segments
        - Draws black rectangles around individual characters
        - Creates detailed visual analysis of text structure
        - Output files named with page numbers: "filename1_out.png", etc.
        - Complex coordinate transformation for proper overlay positioning

    Example:
        >>> text_fragment_absorber_search_and_highlight("document_in.pdf")
        # Creates PNG files with visual highlighting of all text elements
    """
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```
