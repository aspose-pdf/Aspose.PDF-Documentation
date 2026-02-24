---
title: Substituir Texto em PDF via Python
linktitle: Substituir Texto em PDF
type: docs
weight: 40
url: /pt/python-net/replace-text-in-pdf/
description: Saiba mais sobre várias maneiras de substituir e remover texto da biblioteca Aspose.PDF for Python via .NET.
lastmod: "2025-10-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
aliases: 
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Como substituir Texto em PDF usando Python
Abstract: O artigo fornece um guia abrangente sobre várias técnicas de manipulação de texto em documentos PDF usando Aspose.PDF for Python via .NET. Ele abrange várias estratégias de substituição de texto, incluindo a substituição de texto em todas as páginas, em regiões específicas da página e usando expressões regulares. O artigo também explica como substituir fontes em PDFs, garantindo que fontes não utilizadas sejam removidas, e como gerenciar a substituição de texto para reorganizar automaticamente o conteúdo da página. Além disso, aprofunda-se na renderização de símbolos substituíveis durante a criação de PDFs, incluindo seu uso em áreas de cabeçalho/rodapé, para melhorar a personalização do documento. Por fim, detalha métodos para remover todo o texto de um documento PDF, otimizando as operações para cenários onde a remoção completa de texto é necessária. Cada seção é complementada com trechos de código em Python e outras linguagens suportadas para demonstrar a implementação prática.
---

Estes exemplos demonstram como **modificar ou remover texto em um PDF existente**.

## Substituir texto existente

### Substituir Texto em todas as páginas do documento PDF

{{% alert color="primary" %}}

Você pode tentar encontrar e substituir o texto no documento usando Aspose.PDF e obter os resultados online neste [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Substituição de texto é uma necessidade comum ao atualizar ou corrigir conteúdo em documentos PDF existentes — por exemplo, alterar nomes de produtos, corrigir erros de digitação ou atualizar terminologia em várias páginas.

Aspose.PDF for Python via .NET oferece um método poderoso e eficiente para pesquisar e substituir texto programaticamente através da classe [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).

Este exemplo demonstra como encontrar todas as ocorrências de uma frase específica (neste caso, "Black cat") e substituí‑las por uma nova frase ("White dog") em todo o documento PDF.

1. Especifique as frases de pesquisa e substituição. Defina o texto que deseja encontrar e o texto que deseja substituir.
1. Carregue o documento PDF.
1. Crie um Absorvedor de Texto. Um TextFragmentAbsorber é inicializado com a frase de pesquisa. Ele varre o documento em busca de todas as ocorrências da frase fornecida.
1. Aplique o Absorvedor a todas as páginas. Isso itera por todas as páginas e coleta fragmentos de texto que correspondem à frase.
1. Substitua cada fragmento encontrado. Cada ocorrência de "Black cat" deve ser alterada para "White dog".
1. Salve o PDF atualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Substituir Texto em região de página específica

Às vezes, pode ser necessário substituir texto apenas dentro de uma área específica de uma página PDF em vez de pesquisar todo o documento — por exemplo, atualizar um cabeçalho, rodapé ou uma célula de tabela em uma posição conhecida.

A biblioteca Aspose.PDF for Python via .NET permite essa funcionalidade usando o [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) em conjunto com a pesquisa de texto baseada em região.

Este exemplo demonstra como encontrar e substituir todas as ocorrências de uma frase‑alvo dentro de uma região retangular definida em uma página específica.

1. Especifique as frases de pesquisa e substituição.
1. Carregue o documento PDF.
1. Crie um Absorvedor de Texto para pesquisa. Inicialize um TextFragmentAbsorber para encontrar o texto desejado.
1. Restrinja a área de pesquisa. O retângulo especifica os limites das coordenadas x e y na página.
1. Aplique o Absorvedor a uma página específica. Isso realiza a pesquisa e coleta fragmentos de texto correspondentes dentro da área especificada.
1. Substitua o texto encontrado. Cada ocorrência de 'doc' na região definida torna‑se 'DOC'.
1. Salve o PDF atualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
    """
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Redimensionar e Deslocar Texto Sem Alterar o Tamanho da Fonte

Ao substituir texto em um PDF, às vezes você deseja encaixar ou reposicionar o novo texto dentro de uma área específica sem modificar o tamanho da fonte.
Aspose.PDF for Python via .NET oferece opções para ajustar o layout e o espaçamento do texto, mantendo o tamanho original da fonte.

1. Carregue o documento PDF.
1. Colete todos os fragmentos de texto na página usando um 'TextFragmentAbsorber'.
1. Selecione o fragmento a ser modificado.
1. Desloque e redimensione o retângulo de texto.
1. Ajuste o espaçamento do texto. Ative o ajuste de espaçamento para encaixar o texto dentro do retângulo modificado.
1. Substitua o texto do fragmento.
1. Salve o PDF atualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Redimensionar e Deslocar um Parágrafo em PDF

Ao trabalhar com PDFs, às vezes você precisa substituir ou expandir um parágrafo mantendo-o visualmente alinhado ao layout da página. O Aspose.PDF permite redimensionar o retângulo delimitador do parágrafo e ajustar o espaçamento para caber o novo texto, tudo sem alterar o tamanho da fonte.

1. Carregar o Documento PDF.
1. Use 'TextFragmentAbsorber' para coletar todos os fragmentos de texto na página.
1. Selecione o Fragmento a Modificar.
1. Redimensione e Desloque o Parágrafo. Use a caixa de mídia da página para determinar os limites e ajustar o retângulo.
1. Ajuste o Espaçamento. Isso modifica o espaçamento entre palavras/letras ao invés de mudar o tamanho da fonte.
1. Substitua o texto do fragmento.
1. Salve o PDF Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Substituir Texto e Expandir Automaticamente a Fonte para Preencher a Área Alvo

Substitua texto em um PDF enquanto redimensiona e expande automaticamente a fonte para preencher uma área retangular específica. Usando a biblioteca Aspose.PDF for Python via .NET, o código ajusta dinamicamente o tamanho da fonte e o espaçamento para que o novo conteúdo de texto se ajuste perfeitamente dentro de uma caixa delimitadora definida — sem cálculos manuais de fonte.

1. Carregue o PDF.
1. Capture Fragmentos de Texto.
1. Selecione um Fragmento Específico.
1. Defina o Retângulo Alvo.
1. Habilite as Opções de Ajuste de Texto.
1. Substitua o Texto.
1. Salve o Documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)

```

### Substituir Texto e Ajustá-lo em um Retângulo

Substitua texto em um documento PDF garantindo que o novo conteúdo se ajuste à área retangular original do texto, reduzindo automaticamente o tamanho da fonte quando necessário.

Usando a biblioteca Aspose.PDF for Python via .NET, esta função ajusta dinamicamente o layout do texto e o tamanho da fonte, preservando a estrutura do documento enquanto impede o transbordamento.

1. Crie um objeto TextFragmentAbsorber para extrair todos os fragmentos de texto da primeira página.
1. Acesse um Fragmento de Texto Específico.
1. Defina a Área de Substituição.
1. Configure as Opções de Ajuste de Texto. Defina duas opções principais de substituição:
- Ajuste de tamanho da fonte - 'SHRINK_TO_FIT' reduz automaticamente o tamanho da fonte se o novo texto for muito longo.
- Ajuste de espaçamento - 'ADJUST_SPACE_WIDTH' mantém o espaçamento proporcional.
1. Substitua o Texto.
1. Salve o PDF Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH

        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Substituir Automaticamente Texto de Espaço Reservado e Reorganizar o Layout do PDF

Substitua texto de espaço reservado dentro de um PDF (por exemplo, modelos ou formulários) por dados reais como nomes ou informações da empresa.
Ele ajusta automaticamente o layout da página para acomodar o novo texto enquanto aplica formatação personalizada (fonte, cor, tamanho).

1. Importe e Carregue o PDF.
1. Crie um Text Absorber para o Espaço Reservado.
1. Aplique o Absorber a Todas as Páginas.
1. Percorra os Fragmentos de Texto Encontrados.
1. Aplique Formatação de Texto Personalizada.
1. Salve o Documento Atualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Substituir Texto com Base em uma Expressão Regular

Ao trabalhar com documentos PDF, pode ser necessário substituir texto que segue um padrão ao invés de uma frase específica — por exemplo, números de telefone, códigos ou formatos semelhantes a datas.

O Aspose.PDF for Python via .NET permite executar essas substituições usando expressões regulares (regex) com a classe TextFragmentAbsorber.

Este exemplo demonstra como encontrar padrões de texto (neste caso, qualquer texto que corresponda ao formato ####-####, como 1234-5678) e substituí-los por uma string formatada 'ABC1-2XZY'. Também mostra como personalizar a fonte, cor e tamanho do texto substituído.

O trecho de código a seguir mostra como substituir texto com base em uma expressão regular.

1. Carregue o Documento PDF.
1. Crie um Text Absorber baseado em Regex. Inicialize o TextFragmentAbsorber com um padrão de expressão regular.
1. Ative o Modo de Expressão Regular. O parâmetro 'True' ativa o modo de busca por expressão regular.
1. Aplique o Absorber a uma Página. Isto escaneia a página em busca de todos os fragmentos de texto que correspondem ao padrão regex definido.
1. Substitua cada ocorrência por novo texto e aplique estilo personalizado.
1. Salve o Documento Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Substituir fontes ou remover fontes não utilizadas

### Substituir fontes em arquivo PDF existente

Ocasionalmente, você precisa padronizar ou atualizar fontes em um PDF — por exemplo, substituir uma fonte desatualizada ou proprietária por uma mais acessível. A biblioteca Aspose.PDF para Python via .NET permite detectar e substituir fontes programaticamente, garantindo tipografia consistente e compatibilidade do documento.

Este exemplo demonstra como substituir todas as ocorrências de uma fonte específica (por exemplo, 'Arial-BoldMT') por outra fonte (por exemplo, 'Verdana') em todo o documento PDF.

O trecho de código a seguir mostra como substituir a fonte dentro de um documento PDF:

1. Abra o Documento PDF.
1. Inicialize um TextFragmentAbsorber.
1. Use o Absorber para extrair fragmentos de texto de cada página do documento.
1. Identifique e Substitua Fontes. O script verifica se a fonte atual de um fragmento é 'Arial-BoldMT'. Se for, substitui-a pela fonte 'Verdana' usando o método FontRepository.find_font().
1. Salve o Documento Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Remover fontes não utilizadas

Com o tempo, documentos PDF podem acumular fontes não utilizadas ou incorporadas que aumentam o tamanho do arquivo e tornam o processamento mais lento. Essas fontes não utilizadas frequentemente permanecem mesmo após edições ou substituições de texto, especialmente ao trabalhar com PDFs grandes ou complexos.

A biblioteca Aspose.PDF para Python via .NET fornece uma maneira eficiente de remover essas fontes redundantes usando a classe TextEditOptions. Isso não apenas otimiza seu documento, mas também garante que ele use apenas as fontes realmente aplicadas ao texto visível.

O método 'remove_unused_fonts()' é uma forma simples, porém poderosa, de otimizar arquivos PDF removendo dados de fonte redundantes.

Este exemplo demonstra como:

- Digitalizar um PDF em busca de fontes não utilizadas.
- Removê-las com segurança.
- Realocar fragmentos de texto ativos para uma fonte consistente (por exemplo, Times New Roman).

1. Abra o Documento PDF.
1. Configure as Opções de Edição de Texto. Isso instrui o mecanismo a eliminar quaisquer fontes incorporadas que não estejam sendo usadas no texto visível.
1. Crie um Text Absorber com Opções. Um TextFragmentAbsorber extrai fragmentos de texto do documento para edição.
1. Realocar uma Fonte Padrão. Uma vez que o absorber tenha coletado todos os fragmentos, itere sobre eles e aplique uma fonte consistente.
1. Salve o PDF Limpo.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## Remover todo o Texto

### Remover Texto de PDF

Remova todo o conteúdo de texto de um arquivo PDF mantendo imagens, formas e estruturas de layout intactas.
Usando o TextFragmentAbsorber, o código escaneia eficientemente todo o documento e exclui cada fragmento de texto encontrado em cada página.

1. Carregue o Documento PDF.
1. Um objeto TextFragmentAbsorber é criado para detectar e manipular fragmentos de texto no PDF.
1. Remover Todo o Conteúdo de Texto. O método 'absorber.remove_all_text()' remove todos os elementos de texto do documento carregado, deixando os componentes não textuais intocados.
1. Salve o Documento Atualizado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Remover todo o Texto de uma Página Específica

Remova todo o texto de uma única página de um documento PDF usando a classe TextFragmentAbsorber no Aspose.PDF.
Ao contrário da remoção de todo o documento, este método realiza a limpeza de texto em nível de página, excluindo texto apenas da página escolhida enquanto deixa todas as outras páginas intocadas.

1. Carregue o Arquivo PDF.
1. Crie uma Instância de TextFragmentAbsorber.
1. Remova todo o Texto da Primeira Página.
1. Salve o PDF Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Remover todo o Texto de uma área específica na página PDF

Remova todo o texto de uma região retangular específica em uma página usando o TextFragmentAbsorber da Aspose.PDF.
Em vez de limpar uma página inteira, este método realiza remoção de texto direcionada, permitindo controle preciso sobre qual parte da página será afetada.

1. Carregue o Documento PDF.
1. Crie um TextFragmentAbsorber.
1. Defina a Área Alvo (Retângulo).
1. Remova Texto da Região Especificada.
1. Preserve o Restante do Documento.
1. Salve o PDF Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### Remover todo o Texto escondido de um documento PDF

Remova todo o texto de uma região retangular específica em uma página usando o TextFragmentAbsorber da Aspose.PDF.
Em vez de limpar uma página inteira, este método realiza remoção de texto direcionada, permitindo controle preciso sobre qual parte da página será afetada.

1. Carregue o Documento PDF.
1. Crie um TextFragmentAbsorber.
1. Defina a Área Alvo (Retângulo).
1. Remova o Texto da Região Especificada.
1. Preserve o Restante do Documento.
1. Salve o PDF Modificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```
