---
title: Adicionar Imagem ao PDF usando Python
linktitle: Adicionar Imagem
type: docs
weight: 10
url: /python-net/add-image-to-existing-pdf-file/
description: Esta seção descreve como adicionar imagem a um arquivo PDF existente usando a biblioteca Python.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Imagem ao PDF usando Python",
    "alternativeHeadline": "Como adicionar Imagem ao PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, adicionar imagem ao pdf",
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
    "url": "/python-net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção descreve como adicionar imagem a um arquivo PDF existente usando a biblioteca Python."
}
</script>


## Adicionar Imagem em um Arquivo PDF Existente

O trecho de código a seguir mostra como adicionar uma imagem no arquivo PDF.

1. Carregue o arquivo PDF de entrada.
1. Especifique o número da página na qual a imagem será colocada.
1. Para definir a posição da imagem na página, chame o método [add_image](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) da classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Chame o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_file)

    document.pages[1].add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    document.save(output_pdf)
```

## Adicionar Imagem em um Arquivo PDF Existente (Facades)

Há também uma maneira alternativa e mais fácil de adicionar uma imagem a um arquivo PDF.
 Você pode usar o método [AddImage](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/methods/addimage/index) da classe [PdfFileMend](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/). O método [add_image()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) requer a imagem a ser adicionada, o número da página na qual a imagem precisa ser adicionada e as informações de coordenadas. Depois disso, salve o arquivo PDF atualizado e feche o objeto PdfFileMend usando o método [close()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods). O trecho de código a seguir mostra como adicionar uma imagem em um arquivo PDF existente.

```python

    import aspose.pdf as ap

    # Abrir documento
    mender = ap.facades.PdfFileMend()

    # Criar objeto PdfFileMend para adicionar texto
    mender.bind_pdf(input_file)

    # Adicionar imagem no arquivo PDF
    mender.add_image(image_file, 1, 100.0, 600.0, 200.0, 700.0)

    # Salvar alterações
    mender.save(output_pdf)

    # Fechar objeto PdfFileMend
    mender.close()

```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python via .NET Library",
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