---
title: Optimizar, Comprimir o Reducir el Tamaño de PDF en Python
linktitle: Optimizar PDF
type: docs
weight: 30
url: /python-net/optimize-pdf/
keywords: "optimizar pdf python"
description: Optimizar archivo PDF, reducir todas las imágenes, reducir tamaño de PDF, Desincrustar fuentes, Eliminar objetos no utilizados con Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimizar PDF usando Python",
    "alternativeHeadline": "Cómo optimizar PDF con Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, optimizar pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Optimizar archivo PDF, reducir todas las imágenes, reducir tamaño de PDF, Desincrustar fuentes, Eliminar objetos no utilizados con Python."
}
</script>


Un documento PDF a veces puede contener datos adicionales. Reducir el tamaño de un archivo PDF te ayudará a optimizar la transferencia de red y el almacenamiento. Esto es especialmente útil para publicar en páginas web, compartir en redes sociales, enviar por correo electrónico o archivar en almacenamiento. Podemos usar varias técnicas para optimizar PDF:

- Optimizar el contenido de la página para la navegación en línea
- Reducir o comprimir todas las imágenes
- Permitir la reutilización del contenido de la página
- Unir flujos duplicados
- Desincrustar fuentes
- Eliminar objetos no utilizados
- Eliminar campos de formulario aplanados
- Eliminar o aplanar anotaciones

{{% alert color="primary" %}}

Se puede encontrar una explicación detallada de los métodos de optimización en la página Resumen de Métodos de Optimización.

{{% /alert %}}

## Optimizar Documento PDF para la Web

La optimización, o linealización para la Web, se refiere al proceso de hacer un archivo PDF adecuado para la navegación en línea usando un navegador web. Para optimizar un archivo para visualización web:

1. Abra el documento de entrada en un objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Use el método [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. Guarde el documento optimizado usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```python 

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Optimizar para la web
    document.optimize()

    # Guardar documento de salida
    document.save(output_pdf)
```

## Reducir Tamaño PDF

El método [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) le permite reducir el tamaño del documento eliminando la información innecesaria. Por defecto, este método funciona de la siguiente manera:

- Se eliminan los recursos que no se utilizan en las páginas del documento
- Los recursos iguales se unen en un solo objeto

- Se eliminan los objetos no utilizados

El fragmento a continuación es un ejemplo. Sin embargo, tenga en cuenta que este método no puede garantizar la reducción del documento.

```python

    import aspose.pdf as ap

    # Abrir documento
    documento = ap.Document(input_pdf)
    # Optimizar documento PDF. Sin embargo, tenga en cuenta que este método no puede garantizar la reducción del documento
    documento.optimize_resources()
    # Guardar documento actualizado
    documento.save(output_pdf)
```

## Gestión de Estrategia de Optimización

También podemos personalizar la estrategia de optimización. Actualmente, el método [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) utiliza 5 técnicas. Estas técnicas se pueden aplicar utilizando el método OptimizeResources() con el parámetro [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/).

### Reduciendo o Comprimendo Todas las Imágenes

Tenemos dos maneras de trabajar con imágenes: reducir la calidad de la imagen y/o cambiar su resolución.
 En cualquier caso, se deben aplicar [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/). En el siguiente ejemplo, reducimos las imágenes disminuyendo la Calidad de Imagen a 50.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Inicializar OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Configurar opción CompressImages
    optimizeOptions.image_compression_options.compress_images = True
    # Configurar opción ImageQuality
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimizar documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Guardar documento actualizado
    document.save(output_pdf)
```

### Eliminación de Objetos No Utilizados

Un documento PDF a veces contiene objetos PDF que no están referenciados desde ningún otro objeto en el documento. Esto puede suceder, por ejemplo, cuando una página se elimina del árbol de páginas del documento pero el objeto de la página en sí no se elimina. Eliminar estos objetos no invalida el documento, sino que lo reduce.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Establecer opción RemoveUsedObject
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimizar documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Guardar documento actualizado
    document.save(output_pdf)
```

### Eliminando Flujos No Usados

A veces el documento contiene flujos de recursos no utilizados. Estos flujos no son “objetos no utilizados” porque se referencian desde un diccionario de recursos de la página. Por lo tanto, no se eliminan con un método de “eliminar objetos no utilizados”. Pero estos flujos nunca se utilizan con el contenido de la página. Esto puede suceder en casos cuando una imagen ha sido eliminada de la página pero no de los recursos de la página. Además, esta situación a menudo ocurre cuando las páginas se extraen del documento y las páginas del documento tienen recursos “comunes”, es decir, el mismo objeto de Recursos. Se analizan los contenidos de la página para determinar si un flujo de recursos se utiliza o no. Los flujos no utilizados se eliminan. A veces disminuye el tamaño del documento. El uso de esta técnica es similar al paso anterior:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Establecer la opción RemoveUsedStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimizar documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Guardar documento actualizado
    document.save(output_pdf)
```

### Vinculación de Flujos Duplicados

Algunos documentos pueden contener varios flujos de recursos idénticos (como imágenes, por ejemplo). Esto puede ocurrir, por ejemplo, cuando un documento se concatena consigo mismo. El documento de salida contiene dos copias independientes del mismo flujo de recursos. Analizamos todos los flujos de recursos y los comparamos. Si los flujos están duplicados, se fusionan, es decir, solo queda una copia. Las referencias se cambian adecuadamente, y las copias del objeto se eliminan. En algunos casos, esto ayuda a disminuir el tamaño del documento.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Establecer la opción LinkDuplcateStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimizar documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Guardar documento actualizado
    document.save(output_pdf)
```

### Desincrustación de Fuentes

Si el documento usa fuentes incrustadas, significa que todos los datos de las fuentes están almacenados en el documento.
 La ventaja es que el documento es visible independientemente de si la fuente está instalada en la máquina del usuario o no. Pero incrustar fuentes hace que el documento sea más grande. El método de desincrustar fuentes elimina todas las fuentes incrustadas. Por lo tanto, el tamaño del documento disminuye, pero el documento en sí puede volverse ilegible si la fuente correcta no está instalada.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Establecer la opción UnembedFonts
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimizar documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Guardar documento actualizado
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Tamaño del archivo original: {}. Tamaño del archivo reducido: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Los recursos de optimización aplican estos métodos al documento. Si se aplica cualquiera de estos métodos, el tamaño del documento probablemente disminuirá. Si no se aplica ninguno de estos métodos, el tamaño del documento no cambiará, lo cual es obvio.

## Formas Adicionales de Reducir el Tamaño del Documento PDF

### Eliminar o Aplanar Anotaciones

Las anotaciones pueden eliminarse cuando no son necesarias. Cuando son necesarias pero no requieren edición adicional, pueden aplanarse. Ambas técnicas reducirán el tamaño del archivo.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Aplanar anotaciones
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Guardar documento actualizado
    document.save(output_pdf)
```

### Eliminar Campos de Formularios

Si el documento PDF contiene AcroForms, podemos intentar reducir el tamaño del archivo aplanando los campos de formulario.

```python

    import aspose.pdf as ap

    # Cargar formulario PDF fuente
    doc = ap.Document(input_pdf)

    # Aplanar Formularios
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Guardar el documento actualizado
    doc.save(output_pdf)
```

### Convertir un PDF de espacio de color RGB a escala de grises

Un archivo PDF comprende Texto, Imagen, Adjunto, Anotaciones, Gráficos y otros objetos. Puede surgir la necesidad de convertir un PDF de espacio de color RGB a escala de grises para que sea más rápido al imprimir esos archivos PDF. Además, cuando el archivo se convierte a escala de grises, el tamaño del documento también se reduce, pero igualmente puede causar una disminución en la calidad del documento. Esta característica es compatible actualmente con la función Pre-Flight de Adobe Acrobat, pero cuando se habla de automatización de Office, Aspose.PDF es una solución definitiva para proporcionar tales ventajas para manipulaciones de documentos. Para cumplir con este requisito, se puede usar el siguiente fragmento de código.

```python

    import aspose.pdf as ap

    # Cargar archivo PDF de origen
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convertir la imagen de espacio de color RGB a espacio de color de escala de grises
        strategy.convert(page)

    # Guardar archivo resultante
    document.save(output_pdf)
```


### Compresión FlateDecode

Aspose.PDF para Python a través de .NET proporciona soporte de compresión FlateDecode para la funcionalidad de Optimización de PDF. El siguiente fragmento de código muestra cómo usar la opción en Optimización para almacenar imágenes con compresión **FlateDecode**:

```python

    import aspose.pdf as ap

    # Abrir Documento
    doc = ap.Document(input_pdf)
    # Inicializar OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # Para optimizar la imagen usando Compresión FlateDecode, establecer opciones de optimización en Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Establecer Opciones de Optimización
    doc.optimize_resources(optimizationOptions)
    # Guardar Documento
    doc.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>