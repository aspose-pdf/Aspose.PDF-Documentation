---
title: Recortar Páginas de PDF programáticamente en Python
linktitle: Recortar Páginas
type: docs
weight: 70
url: es/python-net/crop-pages/
description: Puede obtener propiedades de página, como el ancho, altura, bleed-, crop- y trimbox utilizando Aspose.PDF para Python vía .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Recortar Páginas de PDF programáticamente vía Python",
    "alternativeHeadline": "Cómo recortar Páginas de PDF en Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, recortar páginas de pdf",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Puede obtener propiedades de página, como el ancho, altura, bleed-, crop- y trimbox utilizando Aspose.PDF para Python vía .NET."
}
</script>


## Obtener Propiedades de la Página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, alto, sangrado, caja de recorte y caja de corte. Aspose.PDF para Python te permite acceder a estas propiedades.

- **media_box**: La caja de medios es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo, A4, A5, Carta de EE. UU., etc.) seleccionado cuando el documento fue impreso en PostScript o PDF. En otras palabras, la caja de medios determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **bleed_box**: Si el documento tiene sangrado, el PDF también tendrá una caja de sangrado. El sangrado es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprime y se corta al tamaño ("corte"), la tinta llegue hasta el borde de la página. Incluso si la página se corta mal - cortada ligeramente fuera de las marcas de corte - no aparecerán bordes blancos en la página.
- **trim_box**: La caja de corte indica el tamaño final de un documento después de imprimir y cortar.
- **art_box**: La caja de arte es la caja dibujada alrededor del contenido real de las páginas en tus documentos.
 Esta caja de página se utiliza al importar documentos PDF en otras aplicaciones.
- **crop_box**: La caja de recorte es el tamaño de "página" en el que se muestra su documento PDF en Adobe Acrobat. En la vista normal, solo se muestran los contenidos de la caja de recorte en Adobe Acrobat. Para descripciones detalladas de estas propiedades, lea la especificación de Adobe.Pdf, particularmente 10.10.1 Límites de Página.

El fragmento a continuación muestra cómo recortar la página:

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Crear nuevo Rectángulo de Caja
    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_pdf)
```

En este ejemplo, utilizamos un archivo de muestra [aquí](crop_page.pdf). Inicialmente, nuestra página se ve como se muestra en la Figura 1.
![Figura 1. Página Recortada](crop_page.png)

Después del cambio, la página se verá como la Figura 2.
![Figura 2. Página Recortada](crop_page2.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python a través de la Biblioteca .NET",
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
    "applicationCategory": "Biblioteca de Manipulación de PDF para Python",
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