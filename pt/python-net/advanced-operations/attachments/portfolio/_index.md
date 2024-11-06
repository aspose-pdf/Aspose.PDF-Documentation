---
title: Trabalhando com Portfólio em PDF usando Python
linktitle: Portfólio
type: docs
weight: 20
url: pt/python-net/portfolio/
description: Como Criar um Portfólio em PDF com Python. Você deve usar um arquivo Microsoft Excel, um documento Word e um arquivo de imagem para criar um Portfólio em PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Portfólio em PDF usando Python",
    "alternativeHeadline": "Criar Portfólio em documento PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf em pdf",
    "keywords": "pdf, python, portfólio",
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
    "url": "/python-net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/portfolio/"
    },
    "dateModified": "2023-02-04",
    "description": "Como Criar um Portfólio em PDF com Python. Você deve usar um arquivo Microsoft Excel, um documento Word e um arquivo de imagem para criar um Portfólio em PDF."
}
</script>


Criar um portfólio em PDF permite consolidar e arquivar diferentes tipos de arquivos em um único documento consistente. Tal documento pode incluir arquivos de texto, imagens, planilhas, apresentações e outros materiais, garantindo que todo o material relevante esteja armazenado e organizado em um só lugar.

O portfólio em PDF ajudará a mostrar sua apresentação de uma maneira de alta qualidade, onde quer que você a utilize. Em geral, criar um portfólio em PDF é uma tarefa muito atual e moderna.

## Como Criar um Portfólio em PDF

Aspose.PDF para Python via .NET permite criar documentos de Portfólio em PDF usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Adicione um arquivo ao objeto document.collection depois de obtê-lo com a classe [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/). Quando os arquivos tiverem sido adicionados, use o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) da classe Document para salvar o documento do portfólio.

O exemplo a seguir usa um arquivo do Microsoft Excel, um documento do Word e um arquivo de imagem para criar um portfólio em PDF.

O código abaixo resulta no seguinte portfólio.

### Um Portfólio PDF criado com Aspose.PDF para Python

![Um Portfólio PDF criado com Aspose.PDF para Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instanciar Objeto Documento
    document = ap.Document()

    # Instanciar objeto Collection do documento
    document.collection = ap.Collection()

    # Obter arquivos para adicionar ao Portfólio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Fornecer descrição dos arquivos
    excel.description = "Arquivo Excel"
    word.description = "Arquivo Word"
    image.description = "Arquivo de Imagem"

    # Adicionar arquivos à coleção do documento
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Salvar documento do Portfólio
    document.save(output_pdf)
```

## Remover Arquivos do Portfólio PDF

Para excluir/remover arquivos do portfólio PDF, tente usar as seguintes linhas de código.

```python

    import aspose.pdf as ap

    # Abrir documento
    documento = ap.Document(input_pdf)
    documento.collection.delete()

    # Salvar arquivo atualizado
    documento.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>