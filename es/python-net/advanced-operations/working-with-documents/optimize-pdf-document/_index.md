---
title: Optimizar, Comprimir o Reducir el Tamaño de PDF en Python
linktitle: Optimizar PDF
type: docs
weight: 30
url: /es/python-net/optimize-pdf/
description: Aprende cómo optimizar documentos PDF en Python para mejorar el rendimiento web y reducir el tamaño del archivo usando Aspose.PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comprimir páginas PDF usando Python
Abstract: Este artículo ofrece una guía completa sobre la optimización de archivos PDF para reducir su tamaño y mejorar el rendimiento en diversas plataformas, como páginas web, correos electrónicos y sistemas de almacenamiento. Las técnicas de optimización incluyen reducir el tamaño de las imágenes, eliminar recursos no utilizados y desincorporar fuentes. Se discuten métodos específicos para optimizar PDFs para la web y reducir el tamaño total del archivo, utilizando los métodos `Optimize` y `OptimizeResources` en Aspose.PDF para Python. La personalización de las estrategias de optimización es posible mediante `OptimizationOptions`, permitiendo acciones específicas como comprimir imágenes, eliminar objetos y flujos no utilizados, enlazar flujos duplicados y desincorporar fuentes. Estrategias adicionales cubren aplanar anotaciones, eliminar campos de formulario y convertir archivos PDF de RGB a escala de grises para disminuir aún más el tamaño. El artículo también destaca el uso de compresión FlateDecode para la optimización de imágenes, asegurando una gestión eficaz de archivos PDF manteniendo la calidad y funcionalidad.
---

Un documento PDF a veces puede contener datos adicionales. Reducir el tamaño de un archivo PDF te ayudará a optimizar la transferencia de red y el almacenamiento. Esto es especialmente útil para publicar en páginas web, compartir en redes sociales, enviar por correo electrónico o archivar en almacenamiento. Podemos usar varias técnicas para optimizar PDF:

- Optimizar el contenido de la página para la navegación en línea
- Reducir o comprimir todas las imágenes
- Habilitar la reutilización del contenido de la página
- Fusionar flujos duplicados
- Desincorporar fuentes
- Eliminar objetos no utilizados
- Eliminar aplanado de campos de formulario
- Eliminar o aplanar anotaciones

{{% alert color="primary" %}}

Una explicación detallada de los métodos de optimización se puede encontrar en la página Resumen de Métodos de Optimización.

{{% /alert %}}

## Optimizar Documento PDF para la Web

La optimización, o linealización para la Web, se refiere al proceso de hacer que un archivo PDF sea apto para la navegación en línea usando un navegador web. Para optimizar un archivo para su visualización en la web:

1. Abra el documento de entrada en un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Utilice el método [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) .
1. Guarde el documento optimizado usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) .

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## Reducir Tamaño PDF

El método [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) permite reducir el tamaño del documento eliminando la información innecesaria. Por defecto, este método funciona de la siguiente manera:

- Los recursos que no se usan en las páginas del documento se eliminan
- Los recursos idénticos se unen en un solo objeto
- Los objetos no utilizados se eliminan

El fragmento a continuación es un ejemplo. Note, sin embargo, que este método no puede garantizar la reducción del documento.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## Gestión de Estrategias de Optimización

También podemos personalizar la estrategia de optimización. Actualmente, el método [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) utiliza 5 técnicas. Estas técnicas pueden aplicarse usando el método OptimizeResources() con el parámetro [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) .

### Reducir o Comprimir Todas las Imágenes

Tenemos dos formas de trabajar con imágenes: reducir la calidad de la imagen y/o cambiar su resolución. En cualquier caso, se debe aplicar [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) . En el siguiente ejemplo, reducimos las imágenes disminuyendo ImageQuality a 50.

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

### Eliminación de Objetos No Utilizados

Un documento PDF a veces contiene objetos PDF que no están referenciados por ningún otro objeto en el documento. Esto puede suceder, por ejemplo, cuando una página se elimina del árbol de páginas del documento pero el propio objeto de página no se elimina. Eliminar estos objetos no invalida el documento, sino que lo reduce.

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

### Eliminación de Flujos No Utilizados

A veces el documento contiene flujos de recursos no utilizados. Estos flujos no son “objetos no utilizados” porque están referenciados desde un diccionario de recursos de página. Por lo tanto, no se eliminan con un método de “eliminar objetos no utilizados”. Pero estos flujos nunca se usan con el contenido de la página. Esto puede ocurrir cuando una imagen se ha eliminado de la página pero no de los recursos de la página. Además, esta situación suele ocurrir cuando se extraen páginas del documento y las páginas del documento tienen recursos “comunes”, es decir, el mismo objeto Resources. El contenido de la página se analiza para determinar si un flujo de recursos se usa o no. Los flujos no utilizados se eliminan. A veces disminuye el tamaño del documento. El uso de esta técnica es similar al paso anterior:

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

### Enlazando Flujos Duplicados

Algunos documentos pueden contener varios flujos de recursos idénticos (como imágenes, por ejemplo). Esto puede ocurrir, por ejemplo, cuando un documento se concatena consigo mismo. El documento de salida contiene dos copias independientes del mismo flujo de recursos. Analizamos todos los flujos de recursos y los comparamos. Si los flujos están duplicados, se fusionan, es decir, solo queda una copia. Las referencias se modifican adecuadamente y las copias del objeto se eliminan. En algunos casos, ayuda a disminuir el tamaño del documento.

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

### Desincorporar Fuentes

Si el documento usa fuentes incrustadas, significa que todos los datos de la fuente están almacenados en el documento. La ventaja es que el documento se puede visualizar sin importar si la fuente está instalada en la máquina del usuario o no. Pero incrustar fuentes hace que el documento sea más grande. El método de desincorporar fuentes elimina todas las fuentes incrustadas. Así, el tamaño del documento disminuye, pero el documento mismo puede volverse ilegible si la fuente correcta no está instalada.

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

Los recursos de optimización aplican estos métodos al documento. Si se aplica cualquiera de estos métodos, el tamaño del documento probablemente disminuya. Si no se aplica ninguno de estos métodos, el tamaño del documento no cambiará, lo cual es obvio.

## Formas adicionales de reducir el tamaño del documento PDF

### Eliminar o aplanar anotaciones

Las anotaciones pueden eliminarse cuando no son necesarias. Cuando son necesarias pero no requieren edición adicional, pueden aplastarse. Ambas técnicas reducirán el tamaño del archivo.

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

### Eliminar campos de formulario

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

Un archivo PDF está compuesto por Texto, Imagen, Adjuntos, Anotaciones, Gráficos y otros objetos. Puede encontrarse con la necesidad de convertir un PDF del espacio de color RGB a escala de grises para que la impresión de esos archivos PDF sea más rápida. Además, cuando el archivo se convierte a escala de grises, el tamaño del documento también se reduce, aunque también puede causar una disminución en la calidad del documento. Esta función es actualmente compatible con la función Pre-Flight de Adobe Acrobat, pero al hablar de automatización de Office, Aspose.PDF es una solución definitiva para proporcionar tales ventajas en la manipulación de documentos. Para cumplir con este requisito, se puede usar el siguiente fragmento de código.

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
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```


