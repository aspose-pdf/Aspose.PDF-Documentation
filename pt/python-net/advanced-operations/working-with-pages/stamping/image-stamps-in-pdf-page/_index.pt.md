---
title: Adicionar Carimbos de Imagem em PDF usando Python
linktitle: Carimbos de Imagem em Arquivo PDF
type: docs
weight: 10
url: /python-net/image-stamps-in-pdf-page/
description: Adicione o Carimbo de Imagem em seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF para Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Carimbos de Imagem em PDF usando Python",
    "alternativeHeadline": "Adicionar Carimbos de Imagem em PDF usando Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, geração de documentos",
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
    "url": "/python-net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2023-04-04",
    "description": "Adicione o Carimbo de Imagem em seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF para Python."
}
</script>


## Adicionar Carimbo de Imagem em Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) para adicionar um carimbo de imagem a um arquivo PDF. A classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) fornece as propriedades necessárias para criar um carimbo baseado em imagem, como altura, largura, opacidade e assim por diante.

Para adicionar um carimbo de imagem:

1. Crie um objeto Document e um objeto ImageStamp usando as propriedades necessárias.
1. Chame o método [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) da classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para adicionar o carimbo ao PDF.

O trecho de código a seguir mostra como adicionar um carimbo de imagem no arquivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Criar carimbo de imagem
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5
    # Adicionar carimbo a uma página específica
    document.pages[1].add_stamp(image_stamp)

    # Salvar documento de saída
    document.save(output_pdf)
```


## Controlar a Qualidade da Imagem ao Adicionar Carimbo

Ao adicionar uma imagem como um objeto de carimbo, você pode controlar a qualidade da imagem. A propriedade [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) da classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) é usada para esse propósito. Ela indica a qualidade da imagem em porcentagem (valores válidos são 0..100).

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Criar carimbo de imagem
    image_stamp = ap.ImageStamp(input_jpg)
    image_stamp.quality = 10
    # Adicionar carimbo a uma página específica
    document.pages[1].add_stamp(image_stamp)

    # Salvar documento de saída
    document.save(output_pdf)
```

## Carimbo de Imagem como Fundo em Caixa Flutuante

A API Aspose.PDF para Python permite adicionar carimbo de imagem como fundo em uma caixa flutuante.
 O atributo [background](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) da classe [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) pode ser usado para definir a imagem de fundo para um caixa flutuante, como mostrado no exemplo de código a seguir.

```python

    import aspose.pdf as ap

    # Instanciar objeto Document
    document = ap.Document()
    # Adicionar página ao documento PDF
    page = document.pages.add()
    # Criar objeto FloatingBox
    box = ap.FloatingBox(200.0, 100.0)
    # Definir posição à esquerda para FloatingBox
    box.left = 40
    # Definir posição superior para FloatingBox
    box.top = 80
    # Definir o alinhamento horizontal para FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Adicionar fragmento de texto à coleção de parágrafos de FloatingBox
    box.paragraphs.add(ap.text.TextFragment("texto principal"))
    # Definir borda para FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Adicionar imagem de fundo
    box.background_image = img
    # Definir cor de fundo para FloatingBox
    box.background_color = ap.Color.yellow
    # Adicionar FloatingBox à coleção de parágrafos do objeto page
    page.paragraphs.add(box)
    # Salvar o documento PDF
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python via Biblioteca .NET",
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