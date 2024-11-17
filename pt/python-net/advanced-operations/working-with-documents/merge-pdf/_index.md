---
title: Como Mesclar PDF usando Python
linktitle: Mesclar arquivos PDF
type: docs
weight: 50
url: /pt/python-net/merge-pdf-documents/
description: Esta página explica como mesclar documentos PDF em um único arquivo PDF com Python.
lastmod: "2023-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Como Mesclar PDF usando Python",
    "alternativeHeadline": "Combine documentos PDF via Python",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "manipulação de documentos pdf",
    "keywords": "pdf, python, mesclar pdf, concatenar, combinar pdf",
    "wordcount": "212",
    "proficiencyLevel": "Iniciante",
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
    "url": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/python-net/merge-pdf-documents/"
    },
    "dateModified": "2023-04-14",
    "description": "Esta página explica como mesclar documentos PDF em um único arquivo PDF com Python via .NET."
}
</script>


## Mesclar ou combinar vários PDFs em um único PDF em Python

Combinar arquivos PDF é uma consulta muito popular entre os usuários. Isso pode ser útil quando você tem vários arquivos PDF que deseja compartilhar ou armazenar juntos como um único documento.

Mesclar arquivos PDF pode ajudá-lo a organizar seus documentos, liberar espaço de armazenamento no seu PC e compartilhar vários arquivos PDF com outras pessoas combinando-os em um único documento.

Mesclar PDF em Python via .NET não é uma tarefa simples sem usar uma biblioteca de terceiros. Este artigo mostra como mesclar vários arquivos PDF em um único documento PDF usando Aspose.PDF para Python via .NET.

## Mesclar Arquivos PDF usando Python e DOM

Para concatenar dois arquivos PDF:

1. Crie dois objetos [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), cada um contendo um dos arquivos PDF de entrada.

1. Em seguida, chame o método [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) da coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) para o objeto Document que você deseja adicionar o outro arquivo PDF.
1. Passe a coleção PageCollection do segundo objeto Document para o método [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) da primeira coleção PageCollection.
1. Finalmente, salve o arquivo PDF de saída usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

O seguinte trecho de código mostra como concatenar arquivos PDF.

```python

    import aspose.pdf as ap

    # Abrir o primeiro documento
    document1 = ap.Document(input_pdf_1)
    # Abrir o segundo documento
    document2 = ap.Document(input_pdf_2)

    # Adicionar páginas do segundo documento ao primeiro
    document1.pages.add(document2.pages)

    # Salvar arquivo de saída concatenado
    document1.save(output_pdf)
```

## Exemplo ao Vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) é um aplicativo web gratuito online que permite investigar como a funcionalidade de mesclagem de apresentações funciona.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

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
    "applicationCategory": "Biblioteca de Manipulação de PDF para Python",
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