---
title: Crear archivos PDF en Python
linktitle: Crear documento PDF
type: docs
weight: 10
url: /es/python-net/create-pdf-document/
description: Aprenda cómo crear archivos PDF y generar PDFs buscables en Python usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Crear archivo PDF con Python
Abstract: Aspose.PDF for Python via .NET es una API versátil diseñada para que los desarrolladores manipulen archivos PDF dentro de aplicaciones Python dirigidas al framework .NET. Permite a los usuarios crear, cargar, modificar y convertir documentos PDF sin esfuerzo. Este artículo ofrece una guía paso a paso para crear un archivo PDF simple usando Aspose.PDF. El proceso implica inicializar un objeto `Document`, agregar una `Page` al documento, insertar un `TextFragment` en los párrafos de la página y guardar el archivo como PDF. El fragmento de código Python incluido muestra estos pasos creando un documento PDF que contiene el texto "Hello World!". Esta API simplifica el manejo de PDFs con un código mínimo, mejorando la productividad de los desarrolladores que trabajan con PDFs en entornos .NET.
---

**Aspose.PDF for Python via .NET** es una API de manipulación de PDF que permite a los desarrolladores crear, cargar, modificar y convertir archivos PDF directamente desde Python para aplicaciones .NET con solo unas pocas líneas de código.

Utilice estos ejemplos cuando necesite generar nuevos archivos PDF desde cero o convertir la salida de OCR en documentos PDF buscables en Python.

## Cómo crear un archivo PDF simple

Para crear un PDF usando Python vía .NET con Aspose.PDF, puede seguir estos pasos:

1. Crear un objeto de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) clase
1. Añadir un [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objeto a la [páginas](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) colección del objeto Document
1. Añadir [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) a [párrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) colección de la página
1. Guardar el documento PDF resultante

```python
import aspose.pdf as ap

# Initialize document object
document = ap.Document()
# Add page
page = document.pages.add()
# Add text to new page
page.paragraphs.add(ap.text.TextFragment("Hello World!"))
# Save updated PDF
document.save(output_pdf)
```

## Cómo crear un documento PDF buscable

Aspose.PDF for Python via .NET permite crear y manipular documentos PDF existentes. Al añadir elementos de Text a un archivo PDF, el PDF resultante es buscable. Sin embargo, al convertir una imagen que contiene texto a un archivo PDF, el contenido del PDF resultante no es buscable. Como solución alternativa, podemos aplicar OCR al archivo resultante para que se vuelva buscable.

El siguiente es el código completo para cumplir con este requisito:

1. Cargar el PDF usando 'ap.Document'.
1. Configurar la resolución de renderizado.
1. Usar 'PngDevice.process' para convertir la página PDF seleccionada en una imagen.
1. Ejecutar OCR en la imagen generada.
1. Crear un nuevo PDF a partir de la salida de OCR.
1. Guardar el PDF buscable.

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## Temas de documentos relacionados

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Formatear documentos PDF en Python](/pdf/es/python-net/formatting-pdf-document/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)
- [Optimizar archivos PDF en Python](/pdf/es/python-net/optimize-pdf/)

