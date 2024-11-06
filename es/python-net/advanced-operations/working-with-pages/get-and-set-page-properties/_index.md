---
title: Obtener y Establecer Propiedades de Página usando Python
linktitle: Obtener y Establecer Propiedades de Página
type: docs
weight: 90
url: es/python-net/get-and-set-page-properties/
description: Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre las propiedades de la página PDF como el color y establecer propiedades de página.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obtener y Establecer Propiedades de Página usando Python",
    "alternativeHeadline": "Obteniendo y Estableciendo Propiedades de Página PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, obtener propiedades de página, establecer propiedades de página",
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
    "url": "/python-net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-and-set-page-properties/"
    },
    "dateModified": "2023-04-04",
    "description": ""
}
</script>


Aspose.PDF para Python a través de .NET te permite leer y establecer propiedades de páginas en un archivo PDF en tus aplicaciones Python. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre las propiedades de las páginas del PDF como el color y establecer propiedades de la página. Los ejemplos dados están en Python.

## Obtener el Número de Páginas en un Archivo PDF

Cuando trabajas con documentos, a menudo deseas saber cuántas páginas contienen. Con Aspose.PDF esto no toma más de dos líneas de código.

Para obtener el número de páginas en un archivo PDF:

1. Abre el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Luego usa la propiedad Count de la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (del objeto Document) para obtener el número total de páginas en el documento.

El siguiente fragmento de código muestra cómo obtener el número de páginas de un archivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obtener conteo de páginas
    print("Conteo de Páginas:", str(len(document.pages)))
```


### Obtener el número de páginas sin guardar el documento

A veces generamos archivos PDF sobre la marcha y durante la creación del archivo PDF, podemos encontrar el requisito (crear tabla de contenidos, etc.) de obtener el número de páginas del archivo PDF sin guardarlo en el sistema o flujo. Por lo tanto, para satisfacer este requisito, se ha introducido un método [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) en la clase Document. Por favor, eche un vistazo al siguiente fragmento de código que muestra los pasos para obtener el número de páginas sin guardar el documento.

```python

    import aspose.pdf as ap

    # Instanciar instancia de Document
    document = ap.Document()
    # Agregar página a la colección de páginas del archivo PDF
    page = document.pages.add()
    # Crear instancia de bucle
    for i in range(0, 300):
        # Agregar TextFragment a la colección de párrafos del objeto página
        page.paragraphs.add(ap.text.TextFragment("Prueba de conteo de páginas"))
    # Procesar los párrafos en el archivo PDF para obtener un conteo de páginas preciso
    document.process_paragraphs()
    # Imprimir número de páginas en el documento
    print("Número de páginas en el documento =", str(len(document.pages)))
```


## Obtener Propiedades de la Página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, alto, caja de sangrado, de recorte y de corte. Aspose.PDF te permite acceder a estas propiedades.

### **Entendiendo las Propiedades de la Página: la Diferencia entre Artbox, BleedBox, CropBox, MediaBox, TrimBox y la propiedad Rect**

- **Caja de medios**: La caja de medios es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo A4, A5, Carta de EE. UU., etc.) seleccionado cuando el documento fue impreso en PostScript o PDF. En otras palabras, la caja de medios determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **Caja de sangrado**: Si el documento tiene sangrado, el PDF también tendrá una caja de sangrado.
 Bleed es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprima y corte al tamaño ("recortado"), la tinta llegue hasta el borde de la página. Incluso si la página se corta incorrectamente, cortada ligeramente fuera de las marcas de recorte, no aparecerán bordes blancos en la página.

- **Caja de recorte**: La caja de recorte indica el tamaño final de un documento después de imprimir y recortar.
- **Caja de arte**: La caja de arte es la caja dibujada alrededor del contenido real de las páginas en tus documentos. Esta caja de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Caja de cultivo**: La caja de cultivo es el tamaño de "página" en el que se muestra tu documento PDF en Adobe Acrobat. En vista normal, solo se muestran los contenidos de la caja de cultivo en Adobe Acrobat.  
  Para descripciones detalladas de estas propiedades, lee la especificación de Adobe.Pdf, particularmente 10.10.1 Límites de Página.
- **Page.Rect**: la intersección (comúnmente rectángulo visible) de la MediaBox y DropBox. La imagen a continuación ilustra estas propiedades.

Para más detalles, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Accediendo a las Propiedades de la Página**

La clase [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) proporciona todas las propiedades relacionadas con una página PDF en particular. Todas las páginas de los archivos PDF están contenidas en la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) del objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Desde allí, es posible acceder a objetos de página individuales usando su índice, o recorrer la colección utilizando un bucle foreach, para obtener todas las páginas. Una vez que se accede a una página individual, podemos obtener sus propiedades. El siguiente fragmento de código muestra cómo obtener las propiedades de la página.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Obtener página particular
    page = document.pages[1]
    # Obtener propiedades de la página
    print(
        "ArtBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : Height={},Width={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("Número de Página :", page.number)
    print("Rotar :", page.rotate)
```

## Obtener una Página Particular del Archivo PDF

Aspose.PDF para Python permite [dividir un PDF en páginas individuales](/pdf/python-net/split-pdf-document/) y guardarlas como archivos PDF. Obtener una página especificada en un archivo PDF y guardarla como un nuevo PDF es una operación muy similar: abrir el documento fuente, acceder a la página, crear un nuevo documento y agregar la página a este.

El [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) object's [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection) contiene las páginas en el archivo PDF. Para obtener una página particular de esta colección:

1. Especifique el índice de la página usando la propiedad Pages.
1. Cree un nuevo objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Agregue el objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) al nuevo objeto Document.
1. Guarde la salida usando el método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

El siguiente fragmento de código muestra cómo obtener una página particular de un archivo PDF y guardarla como un nuevo archivo.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obtener página particular
    page = document.pages[2]

    # Guardar la página como archivo PDF
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## Determinar el Color de la Página

La clase [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) proporciona las propiedades relacionadas con una página particular en un documento PDF, incluyendo qué tipo de color - RGB, blanco y negro, escala de grises o indefinido - la página utiliza.

Todas las páginas de los archivos PDF están contenidas por la colección [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
 El atributo [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) especifica el color de los elementos en la página. Para obtener o determinar la información de color para una página PDF en particular, use la propiedad [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) del objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

El siguiente fragmento de código muestra cómo iterar a través de cada página de un archivo PDF para obtener información de color.

```python

    import aspose.pdf as ap

    # Abrir archivo PDF de origen
    document = ap.Document(input_pdf)
    # Iterar a través de todas las páginas del archivo PDF
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # Obtener la información del tipo de color para una página PDF en particular
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("La página # " + str(page_number) + " es en blanco y negro.")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("La página # " + str(page_number) + " es en escala de grises.")

        if page_color_type == ap.ColorType.RGB:
            print("La página # " + str(page_number) + " es RGB.")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("El color de la página # " + str(page_number) + " es indefinido.")
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python a través de .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de manipulación de PDF para Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>