---
title: Extraer datos vectoriales de un archivo PDF usando Python
linktitle: Extraer datos vectoriales de PDF
type: docs
weight: 80
url: /es/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF facilita la extracción de datos vectoriales de un archivo PDF. Puedes obtener los datos vectoriales (ruta, polígono, polilínea), como posición, color, ancho de línea, etc.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Acceder a datos vectoriales de un documento PDF

Usar [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) para inspeccionar elementos gráficos vectoriales en una página de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Después de visitar la página objetivo, itere a través de los elementos extraídos para examinar propiedades como los límites del rectángulo, posiciones y operadores de dibujo.

1. Abre el PDF de origen como un `Document`.
1. Crear un `GraphicsAbsorber` instancia.
1. Llamar `gr_absorber.visit(page)` en la página de destino.
1. Leer los elementos extraídos de `gr_absorber.elements`.
1. Iterar a través de los elementos y escribir sus propiedades en un archivo de salida.

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

## Guardar gráficos vectoriales de una página en un archivo SVG

Exportar gráficos vectoriales de una página PDF a SVG para preservar rutas y formas escalables fuera del PDF original. Este método es útil para reutilizar arte vectorial en flujos de trabajo web, de diseño o de publicación.

1. Cargar el documento PDF.
1. Acceda a la página objetivo.
1. Llamar `page.try_save_vector_graphics()` exportar las rutas vectoriales de la página a SVG.
1. Cierre el documento.

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

### Extraer cada subruta a un SVG separado

Cuando una página contiene múltiples rutas vectoriales independientes, use [SvgExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractionoptions/) con [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) para escribir cada subruta en un archivo SVG separado.

1. Cargue el PDF.
1. Crear `SvgExtractionOptions` y establecer `extract_every_subpath_to_svg`.
1. Acceda a la primera página del documento.
1. Instanciar `SvgExtractor` con las opciones.
1. Llamar `extractor.extract()` escribir archivos SVG separados para cada subruta vectorial.
1. Cierre el documento.

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

### Extraer una lista de elementos a una sola imagen

Extrae varios elementos vectoriales de una página PDF y guárdalos como una única imagen SVG combinada. Esto es útil cuando deseas preservar la relación visual entre formas agrupadas, diagramas o fragmentos de dibujo.

1. Abrir el PDF usando [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Seleccione una página y prepare una lista de elementos vectoriales.
1. Usar [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) para combinar esos elementos en un solo SVG.
1. Guarde el archivo de salida.

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

### Extraer elemento único

Extraiga un elemento vectorial específico de un PDF y guárdelo como un archivo SVG individual. Esto es útil para aislar logotipos, íconos o formas independientes de páginas más complejas basadas en vectores.

1. Crear un [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) para capturar datos vectoriales.
1. Visite una página específica para recopilar sus elementos vectoriales.
1. Seleccione un elemento objetivo, como un [XFormPlacement](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/xformplacement/).
1. Guarda ese único elemento en un archivo SVG.

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
