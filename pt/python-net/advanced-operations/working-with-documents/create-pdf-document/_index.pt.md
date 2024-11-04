---
title: Como Criar PDF usando Python
linktitle: Criar Documento PDF
type: docs
weight: 10
url: /python-net/create-pdf-document/
description: Crie e formate o Documento PDF com Aspose.PDF para Python via .NET.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Como Criar PDF usando Python",
    "alternativeHeadline": "Criar documento PDF do zero via Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, dotnet, criar documento pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
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
    "url": "/python-net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Crie e formate o Documento PDF com Aspose.PDF para Python via .NET."
}
</script>


**Aspose.PDF para Python via .NET** é uma API de manipulação de PDF que permite aos desenvolvedores criar, carregar, modificar e converter arquivos PDF diretamente de aplicações Python para .NET com apenas algumas linhas de código.

## Como Criar um Arquivo PDF Simples

Para criar um PDF usando Python via .NET com Aspose.PDF, você pode seguir estas etapas:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Adicione um objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à coleção [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) do objeto Document
1. Adicione [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à coleção [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página
1. Salve o documento PDF resultante

```python

    import aspose.pdf as ap

    # Inicializar objeto do documento
    document = ap.Document()
    # Adicionar página
    page = document.pages.add()
    # Adicionar texto à nova página
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    # Salvar PDF atualizado
    document.save(output_pdf)
```