---
title: Alterar Tamanho da Página do PDF com Python
linktitle: Alterar Tamanho da Página do PDF
type: docs
weight: 60
url: pt/python-net/change-page-size/
description: Alterar Tamanho da Página do seu documento PDF usando a biblioteca Aspose.PDF para Python via .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Alterar Tamanho da Página do PDF com Python",
    "alternativeHeadline": "Redimensionar Página do PDF com Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, alterar tamanho do pdf, redimensionar pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação do Aspose.PDF",
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
    "url": "/python-net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/change-page-size/"
    },
    "dateModified": "2023-04-04",
    "description": "Alterar Tamanho da Página do seu documento PDF usando a biblioteca Aspose.PDF para Python via .NET."
}
</script>


## Alterar Tamanho da Página PDF

O Aspose.PDF para Python via .NET permite que você altere o tamanho da página PDF com linhas simples de código em suas aplicações Python. Este tópico explica como atualizar/alterar as dimensões (tamanho) da página de um arquivo PDF existente.

A classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) contém o método [set_page_size()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) que permite definir o tamanho da página. O trecho de código abaixo atualiza as dimensões da página em alguns passos simples:

1. Carregar o arquivo PDF de origem.
1. Obter as páginas no objeto [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Obter uma determinada página.
1. Chamar o método set_page_size() para atualizar suas dimensões.
1. Chamar o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para gerar o arquivo PDF com as dimensões da página atualizadas.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Obter página específica
    page = document.pages[1]

    # Definir o tamanho da página como A4 (11.7 x 8.3 pol) e no Aspose.Pdf, 1 polegada = 72 pontos
    # Portanto, as dimensões A4 em pontos serão (842.4, 597.6)
    page.set_page_size(597.6, 842.4)

    # Salvar o documento atualizado
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para a Biblioteca .NET",
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