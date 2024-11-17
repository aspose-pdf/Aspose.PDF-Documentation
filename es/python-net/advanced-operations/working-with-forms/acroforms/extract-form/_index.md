---
title: Extraer AcroForm - Extraer datos de formularios de PDF en Python
linktitle: Extraer AcroForm
type: docs
weight: 30
url: /es/python-net/extract-form/
description: Extrae formularios de tu documento PDF con la biblioteca Aspose.PDF para Python. Obtén el valor de un campo individual de un archivo PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extraer AcroForm",
    "alternativeHeadline": "Cómo extraer AcroForm de PDF en Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, python, extraer acroform",
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
            "https://www.youtube.com/@AsposePDF",
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
    "url": "/python-net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extract-form/"
    },
    "dateModified": "2023-02-04",
    "description": "Extrae formularios de tu documento PDF con la biblioteca Aspose.PDF para Python. Obtén el valor de un campo individual de un archivo PDF."
}
</script>


## Extraer datos del formulario

### Obtener valores de todos los campos del documento PDF

Para obtener valores de todos los campos en un documento PDF, necesitas navegar a través de todos los campos del formulario y luego obtener el valor usando la propiedad Value. Obtén cada campo de la colección Form, en el tipo base de campo llamado [Field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) y accede a su propiedad [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties).

Los siguientes fragmentos de código en Python muestran cómo obtener los valores de todos los campos de un documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    pdfDocument = ap.Document(input_file)

    # Obtener valores de todos los campos
    for formField in pdfDocument.form.fields:
        # Analizar nombres y valores si es necesario
        print("Nombre del campo : " + formField.partial_name)
        print("Valor : " + str(formField.value))