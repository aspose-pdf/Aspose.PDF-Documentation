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
AlternativeHeadline: Comprima páginas PDF usando Python.
Abstract: Este artículo ofrece una guía completa sobre la optimización de archivos PDF para reducir su tamaño y mejorar el rendimiento en diversas plataformas, como páginas web, correos electrónicos y sistemas de almacenamiento. Las técnicas de optimización incluyen reducir el tamaño de las imágenes, eliminar recursos no utilizados y desincorporar fuentes. Se discuten métodos específicos para optimizar PDFs para la web y reducir el tamaño total del archivo, utilizando los métodos `Optimize` y `OptimizeResources` en Aspose.PDF for Python. La personalización de las estrategias de optimización es posible mediante `OptimizationOptions`, permitiendo acciones específicas como comprimir imágenes, eliminar objetos y flujos no usados, vincular flujos duplicados y desincorporar fuentes. Estrategias adicionales cubren aplanar anotaciones, eliminar campos de formulario y convertir archivos PDF de RGB a escala de grises para disminuir aún más el tamaño. El artículo también destaca el uso de la compresión FlateDecode para la optimización de imágenes, garantizando una gestión eficaz de archivos PDF mientras se mantiene la calidad y funcionalidad.
---

Un documento PDF a veces puede contener datos adicionales. Reducir el tamaño de un archivo PDF te ayudará a optimizar la transferencia de red y el almacenamiento. Esto es especialmente útil para publicar en páginas web, compartir en redes sociales, enviar por correo electrónico o archivar en almacenamiento. Podemos usar varias técnicas para optimizar PDF:

Utilice esta página cuando necesite reducir el tamaño del PDF para entrega web, compartir por correo electrónico, ahorrar espacio de almacenamiento o generar una salida apta para impresión sin volver a crear el documento desde cero.

- Optimizar el contenido de la página para la navegación en línea
- Reducir o comprimir todas las imágenes
- Habilitar reutilización del contenido de la página
- Fusionar flujos duplicados
- Desincorporar fuentes
- Eliminar objetos no utilizados
- Eliminar aplanado de campos de formulario
- Eliminar o aplanar anotaciones

{{% alert color="primary" %}}

 Se puede encontrar una explicación detallada de los métodos de optimización en la página Visión general de los métodos de optimización.

{{% /alert %}}

## Optimizar documento PDF para la Web

Optimización, o linealización para la Web, se refiere al proceso de hacer que un archivo PDF sea adecuado para su navegación en línea mediante un navegador web. Para optimizar un archivo para la visualización web:

1. Abra el documento de entrada en un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto.
1. Usa el [Optimizar](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.
1. Guarde el documento optimizado usando el [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```python
import aspose.pdf as ap

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
document.optimize()
document.save(path_outfile)
```

## Reducir tamaño PDF

El [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método le permite reducir el tamaño del documento al eliminar la información innecesaria. Por defecto, este método funciona de la siguiente manera:

- Los recursos que no se utilizan en las páginas del documento se eliminan
- Los recursos iguales se unen en un solo objeto
- Los objetos no utilizados se eliminan

El fragmento siguiente es un ejemplo. Sin embargo, tenga en cuenta que este método no puede garantizar la reducción del documento.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)
# Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
document.optimize_resources()
# Save updated document
document.save(output_pdf)
```

## Gestión de la Estrategia de Optimización

También podemos personalizar la estrategia de optimización. Actualmente, el [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) el método utiliza 5 técnicas. Estas técnicas pueden aplicarse usando el método OptimizeResources() con el [OpcionesDeOptimización](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) parámetro.

### Reducir o Comprimir Todas las Imágenes

Tenemos dos formas de trabajar con imágenes: reducir la calidad de la imagen y/o cambiar su resolución. En cualquier caso, [OpcionesDeCompresiónDeImagen](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) debe aplicarse. En el siguiente ejemplo, reducimos las imágenes disminuyendo ImageQuality al 50.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)
# Initialize OptimizationOptions
optimizeOptions = ap.optimization.OptimizationOptions()
# Set CompressImages option
optimizeOptions.image_compression_options.compress_images = True
# Set ImageQuality option
optimizeOptions.image_compression_options.image_quality = 50
# Optimize PDF document using OptimizationOptions
document.optimize_resources(optimizeOptions)
# Save updated document
document.save(output_pdf)
```

### Eliminando objetos no utilizados

Un documento PDF a veces contiene los objetos PDF que no son referenciados por ningún otro objeto en el documento. Esto puede suceder, por ejemplo, cuando una página se elimina del árbol de páginas del documento pero el propio objeto de página no se elimina. Eliminar estos objetos no hace que el documento sea inválido, sino que lo reduce.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)
# Set RemoveUsedObject option
optimizeOptions = ap.optimization.OptimizationOptions()
optimizeOptions.remove_unused_objects = True

# Optimize PDF document using OptimizationOptions
document.optimize_resources(optimizeOptions)
# Save updated document
document.save(output_pdf)
```

### Eliminando flujos no utilizados

A veces el documento contiene los flujos de recursos no utilizados. Estos flujos no son “objetos no utilizados” porque están referenciados desde un diccionario de recursos de página. Por lo tanto, no se eliminan con el método “remove unused objects”. Pero estos flujos nunca se usan con el contenido de la página. Esto puede ocurrir en casos en que una imagen se ha eliminado de la página pero no de los recursos de la página. Además, esta situación a menudo ocurre cuando se extraen páginas del documento y las páginas del documento tienen recursos “comunes”, es decir, el mismo objeto Resources. El contenido de la página se analiza para determinar si un flujo de recursos se usa o no. Los flujos no utilizados se eliminan. A veces disminuye el tamaño del documento. El uso de esta técnica es similar al paso anterior:

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)
# Set RemoveUsedStreams option
optimizeOptions = ap.optimization.OptimizationOptions()
optimizeOptions.remove_unused_streams = True
# Optimize PDF document using OptimizationOptions
document.optimize_resources(optimizeOptions)
# Save updated document
document.save(output_pdf)
```

### Vinculación de flujos duplicados

Algunos documentos pueden contener varios flujos de recursos idénticos (como imágenes, por ejemplo). Esto puede suceder, por ejemplo, cuando un documento se concatena consigo mismo. El documento de salida contiene dos copias independientes del mismo flujo de recursos. Analizamos todos los flujos de recursos y los comparamos. Si los flujos están duplicados, se fusionan, es decir, solo queda una copia. Las referencias se cambian adecuadamente y se eliminan las copias del objeto. En algunos casos, ayuda a reducir el tamaño del documento.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)
# Set LinkDuplicateStreams option
optimizeOptions = ap.optimization.OptimizationOptions()
optimizeOptions.link_duplcate_streams = True
# Optimize PDF document using OptimizationOptions
document.optimize_resources(optimizeOptions)
# Save updated document
document.save(output_pdf)
```

### Desincorporar fuentes

Si el documento usa fuentes incrustadas, significa que todos los datos de la fuente están almacenados en el documento. La ventaja es que el documento se puede visualizar sin importar si la fuente está instalada en la máquina del usuario o no. Pero incrustar fuentes hace que el documento sea más grande. El método de desincrustar fuentes elimina todas las fuentes incrustadas. Así, el tamaño del documento disminuye, pero el propio documento puede volverse ilegible si la fuente correcta no está instalada.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)
# Set UnembedFonts  option
optimizeOptions = ap.optimization.OptimizationOptions()
optimizeOptions.unembed_fonts = True
# Optimize PDF document using OptimizationOptions
document.optimize_resources(optimizeOptions)
# Save updated document
document.save(output_pdf)
file_stats_1 = os.stat(input_pdf)
file_stats_2 = os.stat(output_pdf)
print(
    "Original file size: {}. Reduced file size: {}".format(
        file_stats_1.st_size, file_stats_2.st_size
    )
)
```

Los recursos de optimización aplican estos métodos al documento. Si se aplica cualquiera de estos métodos, el tamaño del documento probablemente disminuirá. Si no se aplica ninguno de estos métodos, el tamaño del documento no cambiará, lo cual es evidente.

## Formas adicionales de reducir el tamaño del documento PDF

### Eliminar o aplanar anotaciones

Las anotaciones pueden eliminarse cuando son innecesarias. Cuando son necesarias pero no requieren edición adicional, pueden aplanarse. Ambas técnicas reducirán el tamaño del archivo.

```python
import aspose.pdf as ap

# Open document
document = ap.Document(input_pdf)
# Flatten annotations
for page in document.pages:
    for annotation in page.annotations:
        annotation.flatten()

# Save updated document
document.save(output_pdf)
```

### Eliminando campos de Form

Si el documento PDF contiene AcroForms, podemos intentar reducir el tamaño del archivo aplanando los campos de formulario.

```python
import aspose.pdf as ap

# Load source PDF form
doc = ap.Document(input_pdf)

# Flatten Forms
if len(doc.form.fields) > 0:
    for item in doc.form.fields:
        item.flatten()

# Save the updated document
doc.save(output_pdf)
```

### Convertir un PDF del espacio de color RGB a escala de grises

Un archivo PDF comprende Texto, Imagen, Adjuntos, Anotaciones, Gráficos y otros objetos. Puede encontrarse con la necesidad de convertir un PDF del espacio de color RGB a escala de grises para que la impresión de esos archivos PDF sea más rápida. Además, cuando el archivo se convierte a escala de grises, el tamaño del documento también se reduce, aunque también puede provocar una disminución en la calidad del documento. Esta característica está actualmente soportada por la función Pre-Flight de Adobe Acrobat, pero cuando se habla de automatización de Office, Aspose.PDF es una solución definitiva para proporcionar tales ventajas en la manipulación de documentos. Para cumplir con este requisito, se puede usar el siguiente fragmento de código.

```python
import aspose.pdf as ap

# Load source PDF file
document = ap.Document(input_pdf)
strategy = ap.RgbToDeviceGrayConversionStrategy()
for page in document.pages:
    # Convert the RGB colorspace image to GrayScale colorspace
    strategy.convert(page)

# Save resultant file
document.save(output_pdf)
```

### Compresión FlateDecode

Aspose.PDF for Python via .NET ofrece soporte de compresión FlateDecode para la funcionalidad de Optimización de PDF. El siguiente fragmento de código muestra cómo usar la opción en Optimización para almacenar imágenes con compresión **FlateDecode**:

```python
import aspose.pdf as ap

# Open Document
doc = ap.Document(input_pdf)
# Initialize OptimizationOptions
optimizationOptions = ap.optimization.OptimizationOptions()
# To optimise image using FlateDecode Compression set optimization options to Flate
optimizationOptions.image_compression_options.encoding = (
    ap.optimization.ImageEncoding.FLATE
)
# Set Optimization Options
doc.optimize_resources(optimizationOptions)
# Save Document
doc.save(output_pdf)
```

## Temas de documentos relacionados

- [Trabajar con documentos PDF en Python](/pdf/es/python-net/working-with-documents/)
- [Combinar archivos PDF en Python](/pdf/es/python-net/merge-pdf-documents/)
- [Dividir archivos PDF en Python](/pdf/es/python-net/split-document/)
- [Manipular documentos PDF en Python](/pdf/es/python-net/manipulate-pdf-document/)

