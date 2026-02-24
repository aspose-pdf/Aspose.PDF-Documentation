---
title: Extrair Dados Vetoriais de um arquivo PDF usando Python
linktitle: Extrair Dados Vetoriais do PDF
type: docs
weight: 80
url: /pt/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF facilita a extração de dados vetoriais de um arquivo PDF. Você pode obter os dados vetoriais (caminho, polígono, polilinha), como posição, cor, espessura da linha, etc.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Acesso a Dados Vetoriais de documento PDF

O trecho de código a seguir usa a classe GraphicsAbsorber para mostrar como extrair elementos gráficos vetoriais de uma página específica de um documento PDF e examinar propriedades como limites do retângulo, operadores e posições.

1. Carregue o documento PDF usando 'ap.Document'.
1. Inicialize uma instância de 'GraphicsAbsorber'.
1. Chame 'gr_absorber.visit()' para inspecionar a segunda página.
1. Recupere os elementos extraídos via 'gr_absorber.elements'.
1. Itere sobre cada elemento e registre as propriedades - retângulo, posição e número de operadores.
1. Grave as informações em um arquivo de texto de saída.
1. Feche o documento para liberar recursos.

```python

import os
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
                f.write(f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n")
    finally:
        document.close()
```

## Salvar Gráficos Vetoriais de uma Página em um Arquivo SVG

Exportar gráficos vetoriais de uma página PDF para um arquivo SVG, preservando formas e caminhos vetoriais:

1. Carregue o documento PDF.
1. Acesse a página de destino().
1. Chame 'page.try_save_vector_graphics()', que exporta os caminhos vetoriais da página para um arquivo SVG.
1. Feche o documento.

```python

import os
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

Extrair cada subcaminho (componente) dos gráficos vetoriais em arquivos SVG separados usando um objeto de opções de extração.

1. Carregue o PDF.
1. Crie 'SvgExtractionOptions' e defina 'extract_every_subpath_to_svg'.
1. Acesse a primeira página do documento.
1. Instancie 'SvgExtractor' com as opções.
1. Chame 'extractor.extract()' para gerar arquivos SVG separados para cada subcaminho vetorial.
1. Feche o documento.

```python

import os
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

### Extrair lista de elementos para uma única imagem

Extrair vários elementos vetoriais de uma página PDF e salvá-los como uma única imagem SVG combinada usando Aspose.PDF para Python.
Isso é útil quando você deseja preservar a estrutura visual de formas ou desenhos agrupados, como diagramas ou exportações CAD.

1. Abra o PDF usando 'Document'.
1. Selecione uma página e prepare uma lista de elementos vetoriais.
1. Use 'SvgExtractor' para combinar esses elementos em um único SVG.
1. Salve o arquivo de saída.

```python

import os
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

Extrair um elemento vetorial específico de um PDF e salvá-lo como um arquivo SVG individual.
É benéfico para isolar e exportar logotipos, ícones ou formas independentes de PDFs vetoriais complexos.

1. Crie um 'GraphicsAbsorber' para capturar dados vetoriais.
1. Visite uma página específica para coletar seus elementos vetoriais.
1. Selecione um elemento alvo (por exemplo, um 'XFormPlacement').
1. Salve esse único elemento em um arquivo SVG.

```python

import os
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
