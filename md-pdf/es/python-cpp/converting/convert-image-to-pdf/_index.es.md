---
title: Convertir Imagen a PDF en Python
linktitle: Convertir Imagen a archivo PDF
type: docs
weight: 10
url: /python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: Este tema te muestra cómo convertir Imagen a PDF usando Aspose.PDF para Python a través de la biblioteca C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Nuestra biblioteca demuestra fragmentos de código para convertir los formatos de imagen más populares - JPEG. Puedes convertir muy fácilmente imágenes JPG a PDF con Aspose.PDF para Python a través de C++ siguiendo los pasos:

## Convertir Imagen a PDF

Puedes convertir muy fácilmente imágenes JPG a PDF con Aspose.PDF para C++ siguiendo los pasos:

1. Abre el archivo de imagen de entrada usando la biblioteca PIL
1. Obtén el ancho y la altura de la imagen
1. Crea una nueva instancia de Documento usando la biblioteca AsposePDFPythonWrappers
1. Establece la altura y el ancho fijos de la imagen
1. Agrega una nueva página al documento
1. Agrega la imagen a la página
1. Guarda el PDF de salida con el método 'document.save'.

El fragmento de código a continuación muestra cómo convertir Imagen JPG a PDF usando Python a través de C++:

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# Establecer la ruta del directorio para los archivos de datos
dataDir = os.path.join(os.getcwd(), "samples")

# Establecer la ruta del archivo de entrada
input_file = os.path.join(dataDir, "sample.jpg")

# Establecer la ruta del archivo de salida
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# Abrir el archivo de imagen de entrada usando la biblioteca PIL
pil_img = Image.open(input_file)

# Obtener el ancho y la altura de la imagen
width, height = pil_img.size

# Crear una nueva instancia de Documento usando la biblioteca AsposePDFPythonWrappers
document = apw.Document()

# Crear una nueva instancia de Imagen usando la biblioteca AsposePDFPythonWrappers
image = apw.Image()

# Establecer la ruta del archivo de la imagen
image.file = input_file

# Establecer la altura y el ancho fijos de la imagen
image.fix_height = height
image.fix_width = width

# Añadir una nueva página al documento
page = document.pages.add()

# Añadir la imagen a la página
page.paragraphs.add(image)

# Guardar el documento en la ruta del archivo de salida
document.save(output_file)
```