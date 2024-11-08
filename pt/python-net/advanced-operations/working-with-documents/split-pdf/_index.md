---
title: Dividir PDF programaticamente em Python
linktitle: Dividir arquivos PDF
type: docs
weight: 60
url: /pt/python-net/split-pdf-document/
keywords: dividir pdf em vários arquivos, dividir pdf em pdfs separados, dividir pdf python
description: Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais em suas aplicações Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Dividir PDF programaticamente",
    "alternativeHeadline": "Como dividir PDF com Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, dividir pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe Aspose.PDF Doc",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais em suas aplicações Python."
}
</script>


Dividir páginas de PDF pode ser um recurso útil para aqueles que desejam dividir um arquivo grande em páginas separadas ou grupos de páginas.

## Exemplo Ao Vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) é uma aplicação web gratuita que permite investigar como a funcionalidade de divisão de apresentação funciona.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais em suas aplicações Python. Para dividir páginas de PDF em arquivos PDF de uma única página usando Python, os seguintes passos podem ser seguidos:

1. Percorra as páginas do documento PDF através da coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Para cada iteração, crie um novo objeto Document e adicione o objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) individual no documento vazio

1. Salve o novo PDF usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)

## Dividir PDF em vários arquivos ou pdfs separados em Python

O seguinte trecho de código Python mostra como dividir páginas de PDF em arquivos PDF individuais.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    page_count = 1

    # Percorrer todas as páginas
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
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
    "applicationCategory": "PDF Manipulation Library for Python",
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