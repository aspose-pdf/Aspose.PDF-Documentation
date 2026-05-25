---
title: Pesquisar e Extrair Texto de PDF em Python
linktitle: Pesquisar e Obter Texto
type: docs
weight: 60
url: /pt/python-net/search-and-get-text-from-pdf/
description: Aprenda como pesquisar, inspecionar e extrair texto de documentos PDF em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pesquise texto em PDFs e inspecione fragmentos extraídos em Python
Abstract: Este artigo explica como pesquisar e extrair texto de documentos PDF usando Aspose.PDF for Python via .NET. Ele cobre `TextAbsorber` e `TextFragmentAbsorber`, incluindo extração baseada em região, buscas específicas por página, correspondência de frases e inspeção da posição do texto e das propriedades da fonte.
---

## Pesquisar texto do PDF

Pesquisar e extrair texto de uma área retangular definida em um documento PDF usando o `TextAbsorber` classe. Ele usa o modo de formatação de texto puro para saída limpa e não formatada, o que é útil para extrair conteúdo de regiões estruturadas, como cabeçalhos, rodapés ou áreas de tabela. Ao combinar `TextExtractionOptions` e `TextSearchOptions` com restrições retangulares, você pode controlar onde e como o texto é extraído.

Use esta página quando precisar auditar o conteúdo de texto de PDF, extrair texto para análise ou inspecionar posições e formatação dos fragmentos de texto correspondentes.

1. Carregue o arquivo PDF usando 'ap.Document'.
1. Configurar opções de extração de texto.
1. Definir Área de Pesquisa com Restrições de Retângulo.
1. Criar e Configurar TextAbsorber.
1. Processar todas as páginas do documento.
1. Recuperar e Exibir Texto Extraído.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
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

## Pesquisar texto de uma página PDF específica

Pesquise e extraia texto de uma página e região específicas em um PDF usando o TextAbsorber do Aspose.PDF. Ele direciona à página 2 do documento e extrai apenas o texto encontrado dentro de uma área retangular definida.
Ao combinar TextExtractionOptions (para controle de formatação) e TextSearchOptions (para limitação de área), você pode realizar extração de texto precisa e específica por página de forma eficiente.

1. Carregue o PDF Document.
1. Configurar Opções de Extração de Texto.
1. Restringir a extração de texto a uma área retangular específica na página.
1. Criar e Configurar TextAbsorber.
1. Processar uma página específica.
1. Recuperar e Exibir Texto Extraído.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
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

1. Carregue o PDF Document.
1. Inicializar TextFragmentAbsorber.
1. Processar todas as páginas do documento.
1. Iterar Através de Fragmentos de Texto Extraídos.
1. Imprimir informações básicas de texto.
1. Imprimir detalhes de fonte e formatação.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
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

## Pesquisar uma frase de texto específica em uma única página PDF

Pesquise uma frase de texto específica dentro de uma página de um documento PDF usando TextFragmentAbsorber. Ao contrário da pesquisa em todo o documento, esta abordagem limita a pesquisa a apenas uma página, tornando-a mais eficiente para confirmar a presença e a localização do texto em áreas direcionadas, como cabeçalhos, rodapés ou seções de conteúdo específicas.

1. Carregue o PDF Document.
1. Inicializar TextFragmentAbsorber com frase de pesquisa.
1. Aplicar Absorber a uma Página Específica.
1. Iterar Sobre Fragmentos Encontrados.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Pesquisa de Texto Sequencial Página a Página com Resultados Cumulativos

Pesquisar texto incrementalmente em várias páginas de um documento PDF usando o TextFragmentAbsorber da Aspose.PDF.
Ao contrário de uma pesquisa de página única ou em todo o documento, esta abordagem permite processar as páginas sequencialmente, coletar resultados progressivamente e analisar fragmentos de texto com contexto específico da página. Este método é ideal para documentos grandes ou fluxos de trabalho de processamento progressivo.

1. Carregue o PDF Document.
1. Inicializar TextFragmentAbsorber e Definir Frase de Busca.
1. Processar a Primeira Página. Pesquisar apenas a página 1. Imprime texto, número da página e posição. Forneça resultados isolados por página para maior clareza.
1. Processar a próxima página sequencialmente. Mover para a página 2 e, opcionalmente, continuar pelo resto do documento. O 'absorber.visit()' garante a acumulação de resultados de todas as páginas visitadas. Imprime os resultados cumulativos da pesquisa, mostrando tanto o texto quanto a localização.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
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

## Pesquisa de Frase Direcionada dentro de uma Área Retangular

Pesquisar uma frase específica dentro de um PDF restringindo a pesquisa a uma área retangular específica em uma única página.
Ao combinar a pesquisa de frases com restrições espaciais, você pode localizar o conteúdo com precisão em regiões designadas sem analisar a página ou o documento inteiro. Isso é particularmente útil para formulários, cabeçalhos, rodapés ou relatórios estruturados onde o conteúdo aparece em locais previsíveis.

1. Carregue o PDF Document.
1. Inicializar TextFragmentAbsorber com Frase e Restrições Retangulares
1. Aplicar Absorber na página 2. Restringe o processamento à página 2, reduzindo a computação desnecessária. Garante que a pesquisa seja específica da página.
1. Iterar pelos fragmentos encontrados e imprimir

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Pesquisa de Padrão de Texto em PDF Usando Expressões Regulares

Pesquise padrões de texto em um PDF usando expressões regulares. Ao habilitar o modo regex em TextFragmentAbsorber, você pode localizar padrões complexos como números, datas, preços, coordenadas ou formatos de texto personalizados. A função limita a pesquisa a uma página específica, tornando-a eficiente para extração direcionada de dados estruturados.

1. Carregue o PDF Document.
1. Inicialize TextFragmentAbsorber com padrão Regex.
1. Aplicar Absorber à Página 2. Limita a busca à página 2 para eficiência e precisão. Apenas o texto nesta página é analisado.
1. Iterar através dos fragmentos encontrados. Imprime os fragmentos de texto correspondentes e suas coordenadas. Fornece informações de localização precisas para padrões extraídos.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Converter Correspondências de Texto em Hiperlinks no PDF Usando TextFragmentAbsorber

Pesquisar frases de texto específicas em um PDF e convertê-las em hyperlinks clicáveis. Usando TextFragmentAbsorber com padrões regex, ele localiza palavras-alvo e aplica estilo visual (cor e sublinhado) junto com links interativos.

1. Carregue o PDF Document.
1. Inicialize TextFragmentAbsorber com padrão Regex.
1. Aplicar Absorber à página 1.
1. Estilizar e Adicionar Hiperlinks às Correspondências.
1. Salvar PDF Modificado.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
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

## Pesquisar e Identificar Texto Estilizado em PDF Usando TextFragmentAbsorber

Pesquise fragmentos de texto em um PDF com base em suas propriedades de formatação em vez de seu conteúdo. Usando TextFragmentAbsorber, ele identifica texto com estilos específicos, como texto em negrito.

1. Carregue o PDF Document.
1. Inicializar TextFragmentAbsorber.
1. Aplicar Absorber à página 1.
1. Inspecionar Fragmentos de Texto com Base na Formatação. Verifica o estilo da fonte para formatação em negrito.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Realce Visual de Texto em Páginas PDF

Esta função combina reconhecimento de texto e renderização em um único fluxo de trabalho. Ela não apenas extrai o texto, mas também o visualiza destacando fragmentos, segmentos e caracteres em retângulos codificados por cores em imagens PNG de cada página.

Nosso exemplo realiza visualização avançada de texto em um PDF por:

- pesquisando por todos os fragmentos de texto visíveis usando expressões regulares
- renderizando cada página PDF em uma imagem PNG de alta resolução
- desenhando retângulos coloridos ao redor de fragmentos de texto, segmentos de texto e caracteres individuais

1. Defina a resolução da imagem de saída. Cada página PDF é convertida em uma imagem PNG de 150 DPI.
1. Abra o PDF e inicialize o Text Absorber.
1. Processar Cada Página. Aplicar o absorvedor a cada página. Coletar todos os fragmentos de texto detectados e suas posições geométricas.
1. Converter Page para PNG Stream.
1. Prepare o objeto Graphics para desenho.
1. Aplicar Transformação de Coordenadas. Converter coordenadas PDF para pixels de imagem.
1. Desenhar retângulos para elementos de texto.
1. Salvar o Resultado.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
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

## Tópicos de Texto Relacionados

- [Trabalhar com texto em PDF usando Python](/pdf/pt/python-net/working-with-text/)
- [Substituir texto em PDF via Python](/pdf/pt/python-net/replace-text-in-pdf/)
- [Adicionar dicas de ferramenta ao texto PDF em Python](/pdf/pt/python-net/pdf-tooltip/)
- [Adicionando texto ao PDF](/pdf/pt/python-net/add-text-to-pdf-file/)