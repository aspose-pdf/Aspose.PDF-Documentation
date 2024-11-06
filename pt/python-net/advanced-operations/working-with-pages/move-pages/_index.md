---
title: Mover Páginas de PDF programaticamente via Python
linktitle: Mover Páginas de PDF
type: docs
weight: 100
url: pt/python-net/move-pages/
description: Tente mover páginas para a localização desejada ou para o final de um arquivo PDF usando Aspose.PDF para Python via .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mover Páginas de PDF programaticamente Python",
    "alternativeHeadline": "Como mover Páginas de PDF com Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, mover página pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Tente mover páginas para a localização desejada ou para o final de um arquivo PDF usando Aspose.PDF para Python via .NET."
}
</script>


## Movendo uma Página de um Documento PDF para Outro

Este tópico explica como mover uma página de um documento PDF para o final de outro documento usando Python.
Para mover uma página, devemos:

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o arquivo PDF de origem.
1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o arquivo PDF de destino.
1. Obter a Página da coleção do [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página ao documento de destino.
1. Salvar o PDF de saída usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página no documento de origem.

1. Salve o PDF de origem usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

O snippet de código a seguir mostra como mover uma página.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # Salvar arquivo de saída
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## Movendo um Conjunto de Páginas de um Documento PDF para Outro

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o arquivo PDF de origem.
1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o arquivo PDF de destino.
1. Defina um array com os números das páginas a serem movidas.
1. Execute um loop através do array:

1. Obter Página da coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página ao documento de destino.
1. Salvar o PDF de saída usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página no documento de origem usando array.
1. Salvar o PDF de origem usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

O seguinte trecho de código mostra como inserir uma página vazia no final de um arquivo PDF.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # Salvar arquivos de saída
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```


## Movendo uma Página para um novo local no Documento PDF atual

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com o arquivo PDF de origem.
1. Obtenha a Página da coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página para o novo local (por exemplo, para o final).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) página na localização anterior.
1. Salve o PDF de saída usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)

    page = srcDocument.pages[2]
    srcDocument.pages.add(page)
    srcDocument.pages.delete(2)

    # Salvar arquivo de saída
    srcDocument.save(output_pdf)
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