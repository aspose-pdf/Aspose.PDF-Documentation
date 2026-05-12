---
title: Cambiar el tamaño de página de PDF en Python
linktitle: Cambiar tamaño de página
type: docs
weight: 40
url: /es/python-net/change-page-size/
description: Aprenda cómo leer y cambiar las dimensiones de la página PDF en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cambiar tamaño de página usando Python
Abstract: Este artículo demuestra cómo leer y modificar las dimensiones de la página PDF usando Aspose.PDF. El ejemplo Get Page Size recupera el ancho y la altura de una página PDF específica, lo que permite a los usuarios inspeccionar el diseño de la página, validar el formato o analizar la estructura del documento. El ejemplo Set Page Size muestra cómo cambiar las dimensiones de una página—por ejemplo, convertir la primera página al tamaño A4—mientras también muestra las propiedades de caja (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) antes y después de la modificación.
---

Aspose.PDF for Python via .NET le permite cambiar el tamaño de la página PDF con simples líneas de código. Este tema muestra cómo actualizar las dimensiones de la página usando el [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) y [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) APIs.

Utilice esta guía cuando necesite cambiar el tamaño de páginas PDF existentes, normalizar las dimensiones del documento o inspeccionar la configuración de cajas de página en Python.

{{% alert color="primary" %}}

Tenga en cuenta que las propiedades de altura y anchura utilizan puntos como unidad básica, donde 1 pulgada = 72 puntos y 1 cm = 1/2.54 pulgada = 0.3937 pulgada = 28.3 puntos.

{{% /alert %}}

## Establezca el tamaño de página de una página PDF a A4

El ejemplo actualiza el tamaño de la primera página de un documento PDF a las dimensiones estándar de A4. También muestra las dimensiones de los recuadros de la página (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) antes y después del redimensionado para que pueda verificar los cambios.

El siguiente fragmento de código muestra cómo cambiar las dimensiones de la página PDF al tamaño A4:

1. Acceder al primero [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) del [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Mostrar los tamaños de caja de la página antes de la modificación (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Aplicar dimensiones A4 (597.6 × 842.4 points) usando la API de página.
1. Mostrar los tamaños de caja de página actualizados.
1. Guarde lo modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) a la ruta de salida especificada.

```python
import aspose.pdf as ap

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## Obtener tamaño de página PDF

Este fragmento lee un PDF y recupera las dimensiones (ancho y alto) de la primera página. Utiliza el [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API para extraer el límite de la página [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) y muestra su tamaño en la consola. Esto es útil para inspeccionar el diseño de la página, verificar formatos o preparar documentos para un procesamiento adicional.

1. Cargar el PDF como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acceder al primero [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Recuperar el rectángulo delimitador de la página usando `get_page_rect()`.
1. Extraer los valores de ancho y alto.
1. Imprimir las dimensiones de la página.

```python
import aspose.pdf as ap

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### Obtener el tamaño de página PDF antes y después de la rotación

Recupere las dimensiones de una página PDF antes y después de aplicar una rotación de 90°. Esto demuestra cómo la rotación afecta el ancho y la altura y cómo usar `get_page_rect()` con o sin consideración de rotación.

1. Abre el PDF como un [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acceder al primero [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Aplicar una rotación de 90° usando `page.rotate = ap.Rotation.ON90` (ver el [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) enum).
1. Recuperar el rectángulo de la página sin rotación usando `get_page_rect(False)` y muestra su ancho y altura.
1. Recuperar el rectángulo de la página considerando la rotación usando `get_page_rect(True)` y muestra su ancho y altura.
1. Compare cómo cambian las dimensiones debido a la rotación.

```python
import aspose.pdf as ap

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## Temas de página relacionados

- [Trabajar con páginas PDF en Python](/pdf/es/python-net/working-with-pages/)
- [Recortar páginas PDF en Python](/pdf/es/python-net/crop-pages/)
- [Obtener y establecer propiedades de página PDF en Python](/pdf/es/python-net/get-and-set-page-properties/)
- [Rotar páginas PDF en Python](/pdf/es/python-net/rotate-pages/)