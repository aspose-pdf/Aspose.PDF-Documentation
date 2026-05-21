---
title: Extrair Dados Vetoriais de um arquivo PDF usando Python
linktitle: Extrair Dados Vetoriais de PDF
type: docs
weight: 80
url: /pt/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF facilita a extração de dados vetoriais de um arquivo PDF. Você pode obter os dados vetoriais (caminho, polígono, polilinha), como posição, cor, espessura da linha, etc.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Acessar Dados Vetoriais de um Document PDF

Usar [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) para inspecionar elementos gráficos vetoriais em uma página de um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Após visitar a página de destino, itere pelos elementos extraídos para examinar propriedades como limites de retângulo, posições e operadores de desenho.

1. Abra o PDF de origem como um `Document`.
1. Criar um `GraphicsAbsorber` instância.
1. Chamar `gr_absorber.visit(page)` na página de destino.
1. Leia os itens extraídos de `gr_absorber.elements`.
1. Itere pelos elementos e escreva suas propriedades em um arquivo de saída.

```python
import aspose.pdf as ap


def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)
    try:
        gr_absorber = ap.vector.GraphicsAbsorber()
        # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])

        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(
                    f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n"
                )
    finally:
        document.close()
```

## Salvar Gráficos Vetoriais de uma Página para um Arquivo SVG

Exportar gráficos vetoriais de uma página PDF para SVG para preservar caminhos e formas escaláveis fora do PDF original. Esse método é útil para reutilizar arte vetorial na Web, design ou fluxos de trabalho de publicação.

1. Carregue o documento PDF.
1. Acesse a página de destino.
1. Chamar `page.try_save_vector_graphics()` exportar os caminhos vetoriais da página para SVG.
1. Feche o documento.

```python
import aspose.pdf as ap


def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        # Try to save vector graphics into SVG
        page.try_save_vector_graphics(svg_outfile)
    finally:
        document.close()
```

### Extrair Cada Subcaminho para um SVG Separado

Quando uma página contém vários caminhos vetoriais independentes, use [SvgExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractionoptions/) com [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) para gravar cada subcaminho em um arquivo SVG separado.

1. Carregue o PDF.
1. Criar `SvgExtractionOptions` e definir `extract_every_subpath_to_svg`.
1. Acesse a primeira página do documento.
1. Instanciar `SvgExtractor` com as opções.
1. Chamar `extractor.extract()` para escrever arquivos SVG separados para cada subcaminho vetorial.
1. Feche o documento.

```python
import aspose.pdf as ap


def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    try:
        options = ap.vector.SvgExtractionOptions()
        options.extract_every_subpath_to_svg = True

        page = document.pages[1]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### Extrair uma Lista de Elementos para uma Única Imagem

Extrair múltiplos elementos vetoriais de uma página PDF e salvá-los como uma única imagem SVG combinada. Isso é útil quando você deseja preservar a relação visual entre formas agrupadas, diagramas ou fragmentos de desenho.

1. Abra o PDF usando [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Selecione uma página e prepare uma lista de elementos vetoriais.
1. Usar [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) para combinar esses elementos em um único SVG.
1. Salve o arquivo de saída.

```python
import aspose.pdf as ap


def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        svg_extractor = ap.vector.SvgExtractor()
        elements = []  # Fill this list with specific graphic elements as needed
        svg_extractor.extract(elements, page, outfile)
    finally:
        document.close()
```

### Extrair elemento único

Extraia um elemento vetorial específico de um PDF e salve‑o como um arquivo SVG individual. Isso é útil para isolar logotipos, ícones ou formas independentes de páginas mais complexas baseadas em vetor.

1. Criar um [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) para capturar dados vetoriais.
1. Visite uma página específica para coletar seus elementos vetoriais.
1. Selecione um elemento alvo, como um [XFormPlacement](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/xformplacement/).
1. Salve esse único elemento em um arquivo SVG.

```python
import aspose.pdf as ap


def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        graphics_absorber = ap.vector.GraphicsAbsorber()
        page = document.pages[1]
        graphics_absorber.visit(page)
        xform_placement = graphics_absorber.elements[1]
        if isinstance(xform_placement, ap.vector.XFormPlacement):
            xform_placement.elements[2].save_to_svg(outfile)
    finally:
        document.close()
```
