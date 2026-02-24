---
title: Extraer datos vectoriales de un archivo PDF usando Python
linktitle: Extraer datos vectoriales de PDF
type: docs
weight: 80
url: /es/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF facilita la extracción de datos vectoriales de un archivo PDF. Puedes obtener los datos vectoriales (ruta, polígono, polilínea), como posición, color, ancho de línea, etc.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Acceso a datos vectoriales del documento PDF

El siguiente fragmento de código usa la clase GraphicsAbsorber para mostrar cómo extraer elementos gráficos vectoriales de una página específica de un documento PDF y examinar propiedades como los límites del rectángulo, los operadores y las posiciones.

1. Cargar el documento PDF usando 'ap.Document'.
1. Inicializar una instancia de 'GraphicsAbsorber'.
1. Llamar a 'gr_absorber.visit()' para inspeccionar la segunda página.
1. Recuperar los elementos extraídos mediante 'gr_absorber.elements'.
1. Iterar sobre cada elemento y registrar propiedades: rectángulo, posición y número de operadores.
1. Escribir la información en un archivo de texto de salida.
1. Cerrar el documento para liberar recursos.

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

## Guardar gráficos vectoriales de una página en un archivo SVG

Exportar gráficos vectoriales de una página PDF a un archivo SVG, preservando las formas y rutas vectoriales:

1. Cargar el documento PDF.
1. Acceder a la página objetivo().
1. Llamar a 'page.try_save_vector_graphics()' que exporta las rutas vectoriales de la página a un archivo SVG.
1. Cerrar el documento.

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

### Extraer cada subruta a un SVG separado

Extraer cada subruta (componente) de los gráficos vectoriales en archivos SVG separados mediante un objeto de opciones de extracción.

1. Cargar el PDF.
1. Crear 'SvgExtractionOptions' y establecer 'extract_every_subpath_to_svg'.
1. Acceder a la primera página del documento.
1. Instanciar 'SvgExtractor' con las opciones.
1. Llamar a 'extractor.extract()' para generar archivos SVG separados para cada subruta vectorial.
1. Cerrar el documento.

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

### Extraer lista de elementos a una sola imagen

Extraer múltiples elementos vectoriales de una página PDF y guardarlos como una única imagen SVG combinada usando Aspose.PDF para Python.
Esto es útil cuando deseas preservar la estructura visual de formas o dibujos agrupados, como diagramas o exportaciones CAD.

1. Abrir el PDF usando 'Document'.
1. Seleccionar una página y preparar una lista de elementos vectoriales.
1. Usar 'SvgExtractor' para combinar esos elementos en un SVG.
1. Guardar el archivo de salida.

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

### Extraer un solo elemento

Extraer un elemento vectorial específico de un PDF y guardarlo como un archivo SVG individual.
Es beneficioso para aislar y exportar logotipos, íconos o formas independientes de PDFs complejos basados en vectores.

1. Crear un 'GraphicsAbsorber' para capturar datos vectoriales.
1. Visitar una página específica para recopilar sus elementos vectoriales.
1. Seleccionar un elemento objetivo (p.ej., un 'XFormPlacement').
1. Guardar ese único elemento en un archivo SVG.

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
