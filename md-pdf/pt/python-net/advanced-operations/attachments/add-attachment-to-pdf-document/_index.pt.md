---
title: Adicionando Anexo a um Documento PDF usando Python
linktitle: Adicionando Anexo a um Documento PDF
type: docs
weight: 10
url: /python-net/add-attachment-to-pdf-document/
description: Esta página descreve como adicionar um anexo a um arquivo PDF com Aspose.PDF para Python via biblioteca .NET.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionando Anexo a um Documento PDF via Python",
    "alternativeHeadline": "Como adicionar anexos ao PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, anexos em pdf",
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
    "url": "/python-net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Esta página descreve como adicionar um anexo a um arquivo PDF com Aspose.PDF para Python via biblioteca .NET"
}
</script>


Attachments podem conter uma ampla variedade de informações e podem ser de vários tipos de arquivos. Este artigo explica como adicionar um anexo a um arquivo PDF.

1. Crie um novo projeto Python.
1. Importe o pacote Aspose.PDF
1. Crie um objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie um objeto [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) com o arquivo que você está adicionando e a descrição do arquivo.
1. Adicione o objeto [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) à coleção [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), com o método [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) da coleção.

A coleção [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) contém todos os anexos no arquivo PDF.
 O seguinte trecho de código mostra como adicionar um anexo em um documento PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Configurar novo arquivo para ser adicionado como anexo
    fileSpecification = ap.FileSpecification(attachment_file, "Arquivo de texto de exemplo")

    # Adicionar anexo à coleção de anexos do documento
    document.embedded_files.append(fileSpecification)

    # Salvar nova saída
    document.save(output_pdf)
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>