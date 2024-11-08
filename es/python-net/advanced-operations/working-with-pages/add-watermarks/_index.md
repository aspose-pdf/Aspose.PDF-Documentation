---
title: Añadir marca de agua a PDF usando Python
linktitle: Añadir marca de agua
type: docs
weight: 40
url: /es/python-net/add-watermarks/
description: Este artículo explica las características de trabajar con artefactos y obtener marcas de agua en PDFs utilizando Python de forma programática.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir marca de agua a PDF usando Python",
    "alternativeHeadline": "Cómo añadir marca de agua a PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf,python, añadir marca de agua",
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
    "url": "/python-net/add-watermarks/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-watermarks/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo explica las características de trabajar con artefactos y obtener marcas de agua en PDFs utilizando Python."
}
</script>


**Aspose.PDF para Python a través de .NET** permite agregar marcas de agua a su documento PDF utilizando Artefactos. Por favor, consulte este artículo para resolver su tarea.

Para trabajar con artefactos, Aspose.PDF tiene dos clases: [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) y [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/).

Para obtener todos los artefactos en una página particular, la clase [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) tiene la propiedad Artifacts. Este tema explica cómo trabajar con artefactos en archivos PDF.

## Trabajando con Artefactos

La clase [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) contiene las siguientes propiedades:

**contents** – Obtiene una colección de operadores internos del artefacto. Su tipo soportado es System.Collections.ICollection.  
**form** – Obtiene el XForm de un artefacto (si se usa XForm). Las marcas de agua, encabezados y pies de página contienen XForm que muestra todos los contenidos del artefacto.

**image** – Obtiene la imagen de un artefacto (si hay una imagen presente, de lo contrario null).
**text** – Obtiene el texto de un artefacto.  
**rectangle** – Obtiene la posición de un artefacto en la página.  
**rotation** – Obtiene la rotación de un artefacto (en grados, un valor positivo indica rotación en sentido contrario a las agujas del reloj).  
**opacity** – Obtiene la opacidad de un artefacto. Los valores posibles están en el rango de 0…1, donde 1 es completamente opaco.

## Ejemplos de Programación: Cómo Añadir una Marca de Agua en Archivos PDF

El siguiente fragmento de código muestra cómo obtener cada marca de agua en la primera página de un archivo PDF con Python.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    artifact = ap.WatermarkArtifact()

    ts = ap.text.TextState()
    ts.font_size = 72
    ts.foreground_color = ap.Color.blue
    ts.font = ap.text.FontRepository.find_font("Courier")

    artifact.set_text_and_state("WATERMARK", ts)
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    artifact.rotation = 45
    artifact.opacity = 0.5
    artifact.is_background = True
    document.pages[1].artifacts.append(artifact)
    document.save(output_pdf)
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