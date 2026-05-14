---
title: Optimizar archivos PDF en Python
linktitle: Optimizar PDF
type: docs
weight: 30
url: /es/python-net/optimize-pdf/
description: Aprenda cómo optimizar, comprimir y reducir el tamaño de archivo PDF en Python usando Aspose.PDF.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comprima páginas PDF usando Python
Abstract: Este artículo ofrece una guía completa sobre la optimización de archivos PDF para reducir su tamaño y mejorar el rendimiento en diversas plataformas, como páginas web, correos electrónicos y sistemas de almacenamiento. Las técnicas de optimización incluyen la reducción del tamaño de las imágenes, la eliminación de recursos no utilizados y la desincorporación de fuentes. Se discuten métodos específicos para optimizar PDFs para la web y reducir el tamaño total del archivo, utilizando los métodos `Optimize` y `OptimizeResources` en Aspose.PDF for Python. La personalización de las estrategias de optimización es posible a través de `OptimizationOptions`, lo que permite acciones dirigidas como comprimir imágenes, eliminar objetos y flujos no utilizados, vincular flujos duplicados y desincorporar fuentes. Estrategias adicionales cubren la aplanación de anotaciones, la eliminación de campos de formulario y la conversión de archivos PDF de RGB a escala de grises para reducir aún más el tamaño. El artículo también destaca el uso de la compresión FlateDecode para la optimización de imágenes, garantizando una gestión eficaz de archivos PDF mientras se mantiene la calidad y la funcionalidad.
---

Un documento PDF a veces puede contener datos adicionales. Reducir el tamaño de un archivo PDF le ayudará a optimizar la transferencia de red y el almacenamiento. Esto es especialmente útil para publicar en páginas web, compartir en redes sociales, enviar por correo electrónico o archivar en almacenamiento. Podemos usar varias técnicas para optimizar el PDF:

Utilice esta página cuando necesite reducir el tamaño del PDF para entrega web, compartir por correo electrónico, ahorro de almacenamiento o salida apta para impresión sin reconstruir el documento desde cero.

- Optimizar el contenido de la página para la navegación en línea
- Reducir o comprimir todas las imágenes
- Habilitar la reutilización del contenido de la página
- Combinar flujos duplicados
- Desincorporar fuentes
- Eliminar objetos no utilizados
- Eliminar el aplanado de los campos de formulario
- Eliminar o aplanar anotaciones

{{% alert color="primary" %}}

 Una explicación detallada de los métodos de optimización se puede encontrar en la página Visión general de los métodos de optimización.

{{% /alert %}}

## Optimizar documento PDF para la web

La optimización, o linealización para la web, se refiere al proceso de hacer que un archivo PDF sea adecuado para la navegación en línea mediante un navegador web. Para optimizar un archivo para su visualización en la web:

1. Abra el documento de entrada en un [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto.
1. Usa el [Optimizar](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.
1. Guarde el documento optimizado usando el [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Reducir tamaño PDF

El [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) El método le permite reducir el tamaño del documento eliminando la información innecesaria. De forma predeterminada, este método funciona de la siguiente manera:

- Los recursos que no se utilizan en las páginas del documento se eliminan
- Los recursos iguales se unen en un solo objeto
- Los objetos no utilizados se eliminan

El fragmento a continuación es un ejemplo. Sin embargo, tenga en cuenta que este método no puede garantizar la reducción del documento.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Gestión de Estrategia de Optimización

También podemos personalizar la estrategia de optimización. Actualmente, la [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) el método usa 5 técnicas. Estas técnicas pueden aplicarse usando el método OptimizeResources() con el [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) parámetro.

### Reducir o comprimir todas las imágenes

Tenemos dos formas de trabajar con imágenes: reducir la calidad de la imagen y/o cambiar su resolución. En cualquier caso, [OpcionesDeCompresiónDeImagen](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) debe aplicarse. En el siguiente ejemplo, reducimos las imágenes al disminuir ImageQuality al 50.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Eliminando objetos no utilizados

Un documento PDF a veces contiene objetos PDF que no están referenciados desde ningún otro objeto en el documento. Esto puede suceder, por ejemplo, cuando se elimina una página del árbol de páginas del documento pero el propio objeto de la página no se elimina. Eliminar estos objetos no invalida el documento, sino que lo reduce.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Eliminando flujos sin usar

A veces el documento contiene flujos de recursos no utilizados. Estos flujos no son “unused objects” porque están referenciados desde un diccionario de recursos de página. Por lo tanto, no se eliminan con un método “remove unused objects”. Pero estos flujos nunca se usan con el contenido de la página. Esto puede ocurrir en casos en que una imagen ha sido eliminada de la página pero no de los recursos de la página. Además, esta situación ocurre a menudo cuando se extraen páginas del documento y las páginas del documento tienen recursos “common”, es decir, el mismo objeto Resources. El contenido de la página se analiza para determinar si un flujo de recurso se usa o no. Los flujos no utilizados se eliminan. A veces disminuye el tamaño del documento. El uso de esta técnica es similar al paso anterior:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Vinculación de flujos duplicados

Algunos documentos pueden contener varios flujos de recursos idénticos (como imágenes, por ejemplo). Esto puede ocurrir, por ejemplo, cuando un documento se concatena consigo mismo. El documento de salida contiene dos copias independientes del mismo flujo de recursos. Analizamos todos los flujos de recursos y los comparamos. Si los flujos están duplicados, se fusionan, es decir, solo queda una copia. Las referencias se modifican adecuadamente y se eliminan las copias del objeto. En algunos casos, ayuda a reducir el tamaño del documento.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Desincorporar fuentes

Si el documento utiliza fuentes incrustadas, significa que todos los datos de la fuente se almacenan en el documento. La ventaja es que el documento se puede visualizar independientemente de si la fuente está instalada en la máquina del usuario o no. Pero incrustar fuentes hace que el documento sea más grande. El método de desaplicar fuentes elimina todas las fuentes incrustadas. Así, el tamaño del documento disminuye, pero el propio documento puede volverse ilegible si la fuente correcta no está instalada.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Los recursos de optimización aplican estos métodos al documento. Si se aplica cualquiera de estos métodos, el tamaño del documento probablemente disminuya. Si no se aplica ninguno de estos métodos, el tamaño del documento no cambiará, lo cual es obvio.

## Formas adicionales de reducir el tamaño del documento PDF

### Eliminar o aplanar anotaciones

Las anotaciones pueden eliminarse cuando son innecesarias. Cuando son necesarias pero no requieren edición adicional, pueden aplanarse. Ambas técnicas reducirán el tamaño del archivo.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### Eliminando campos de formulario

Si el documento PDF contiene AcroForms, podemos intentar reducir el tamaño del archivo aplanando los campos de formulario.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Convertir un PDF del espacio de color RGB a escala de grises

Un archivo PDF comprende Text, Image, Attachment, Annotations, Graphs y otros objetos. Puede encontrarse con la necesidad de convertir un PDF del espacio de color RGB a escala de grises para que la impresión de esos archivos PDF sea más rápida. Además, cuando el archivo se convierte a escala de grises, el tamaño del documento también se reduce, pero también puede provocar una disminución de la calidad del documento. Esta funcionalidad está soportada actualmente por la característica Pre-Flight de Adobe Acrobat, pero al hablar de automatización de Office, Aspose.PDF es una solución definitiva para proporcionar tales ventajas en la manipulación de documentos. Para cumplir con este requerimiento, se puede usar el siguiente fragmento de código.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### Compresión FlateDecode

Aspose.PDF for Python via .NET brinda soporte de compresión FlateDecode para la funcionalidad de Optimización de PDF. El siguiente fragmento de código muestra cómo usar la opción en Optimización para almacenar imágenes con compresión **FlateDecode**:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## Temas de documentos relacionados

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Fusionar archivos PDF en Python](/pdf/es/python-net/merge-pdf-documents/)
- [Dividir archivos PDF en Python](/pdf/es/python-net/split-document/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)

