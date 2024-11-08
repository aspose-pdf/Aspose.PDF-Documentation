---
title: Adicionar Cabeçalho e Rodapé ao PDF usando Python
linktitle: Adicionar Cabeçalho e Rodapé ao PDF
type: docs
weight: 50
url: /pt/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para Python via .NET permite que você adicione cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Cabeçalho e Rodapé ao PDF usando Python",
    "alternativeHeadline": "Como adicionar Cabeçalho e Rodapé ao Arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, adicionar cabeçalho, adicionar rodapé no pdf",
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
    "url": "/python-net/add-headers-and-footers-of-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-headers-and-footers-of-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para Python via .NET permite que você adicione cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp."
}
</script>


**Aspose.PDF for Python via .NET** permite que você adicione cabeçalho e rodapé em seu arquivo PDF existente. Você pode adicionar imagens ou texto a um documento PDF. Além disso, tente adicionar diferentes cabeçalhos em um arquivo PDF com Python.

## Adicionando Texto no Cabeçalho do Arquivo PDF

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) para adicionar texto no cabeçalho de um arquivo PDF. A classe TextStamp fornece as propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no cabeçalho, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Depois disso, você pode chamar o método 'add_stamp' da Página para adicionar o texto no cabeçalho do PDF.

Você precisa definir a propriedade [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) de forma que ajuste o texto na área do cabeçalho do seu PDF. Você também precisa definir 'horizontal_alignment' para Center e 'vertical_alignment' para Top.

O seguinte trecho de código mostra como adicionar texto no cabeçalho de um arquivo PDF com Python:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Criar cabeçalho
    textStamp = ap.TextStamp("Texto do Cabeçalho")
    # Definir propriedades do carimbo
    textStamp.top_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Adicionar cabeçalho em todas as páginas
    for page in document.pages:
        page.add_stamp(textStamp)

    # Salvar documento atualizado
    document.save(output_pdf)
```

## Adicionando Texto no Rodapé do Arquivo PDF

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) para adicionar texto no rodapé de um arquivo PDF.
 Classe TextStamp fornece propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no rodapé, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Após isso, você pode chamar o método 'add_stamp' da Page para adicionar o texto no rodapé do PDF.

O trecho de código a seguir mostra como adicionar texto no rodapé de um arquivo PDF com Python:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Criar rodapé
    textStamp = ap.TextStamp("Texto do Rodapé")
    # Definir propriedades do carimbo
    textStamp.bottom_margin = 10
    textStamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    textStamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Adicionar rodapé em todas as páginas
    for page in document.pages:
        page.add_stamp(textStamp)

    # Salvar arquivo PDF atualizado
    document.save(output_pdf)
```

## Adicionando Imagem no Cabeçalho do Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) para adicionar imagem no cabeçalho de um arquivo PDF. Classe Image Stamp fornece as propriedades necessárias para criar um selo baseado em imagem, como tamanho de fonte, estilo de fonte e cor de fonte, etc. Para adicionar uma imagem no cabeçalho, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método 'add_stamp' da Página para adicionar a imagem no cabeçalho do PDF.

O seguinte trecho de código mostra como adicionar uma imagem no cabeçalho de um arquivo PDF com Python:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Criar cabeçalho
    image_stamp = ap.ImageStamp(input_image)
    # Definir propriedades do selo
    image_stamp.top_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.TOP
    # Adicionar cabeçalho em todas as páginas
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Salvar documento atualizado
    document.save(output_pdf)
```

## Adicionando Imagem no Rodapé do Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) para adicionar uma imagem no rodapé de um arquivo PDF. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) class fornece as propriedades necessárias para criar um carimbo baseado em imagem, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar uma imagem no rodapé, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método 'add_stamp' da Página para adicionar a imagem no rodapé do PDF.

O seguinte trecho de código mostra como adicionar uma imagem no rodapé de um arquivo PDF com Python:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Criar rodapé
    image_stamp = ap.ImageStamp(input_image)
    # Definir propriedades do carimbo
    image_stamp.bottom_margin = 10
    image_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    image_stamp.vertical_alignment = ap.VerticalAlignment.BOTTOM
    # Adicionar rodapé em todas as páginas
    for page in document.pages:
        page.add_stamp(image_stamp)

    # Salvar arquivo PDF atualizado
    document.save(output_pdf)
```

## Adicionando diferentes Cabeçalhos em um Arquivo PDF

Sabemos que podemos adicionar TextStamp na seção de Cabeçalho/Rodapé do documento usando as propriedades [top_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) ou [bottom_margin](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties), mas às vezes podemos ter a necessidade de adicionar múltiplos cabeçalhos/rodapés em um único documento PDF. **Aspose.PDF para Python via .NET** explica como fazer isso.

Para realizar essa necessidade, iremos criar objetos TextStamp individuais (o número de objetos depende do número de Cabeçalhos/Rodapés necessários) e os adicionaremos ao documento PDF.
 Podemos também especificar diferentes informações de formatação para cada objeto de carimbo individual. No exemplo a seguir, criamos um objeto Documento e três objetos TextStamp e, em seguida, usamos o método 'add_stamp' da Página para adicionar o texto na seção de cabeçalho do PDF. O trecho de código a seguir mostra como adicionar uma imagem no rodapé de um arquivo PDF com Aspose.PDF para Python:

```python

    import aspose.pdf as ap

    # Criar três carimbos
    stamp1 = ap.TextStamp("Cabeçalho 1")
    stamp2 = ap.TextStamp("Cabeçalho 2")
    stamp3 = ap.TextStamp("Cabeçalho 3")

    # Definir alinhamento do carimbo (colocar carimbo no topo da página, centralizado horizontalmente)
    stamp1.vertical_alignment = ap.VerticalAlignment.TOP
    stamp1.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Especificar o estilo da fonte como Negrito
    stamp1.text_state.font_style = ap.text.FontStyles.BOLD
    # Definir a informação da cor do texto como vermelho
    stamp1.text_state.foreground_color = ap.Color.red
    # Especificar o tamanho da fonte como 14
    stamp1.text_state.font_size = 14

    # Agora precisamos definir o alinhamento vertical do segundo objeto carimbo como Top
    stamp2.vertical_alignment = ap.VerticalAlignment.TOP
    # Definir informação de alinhamento Horizontal para carimbo como Centralizado
    stamp2.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Definir o fator de zoom para o objeto carimbo
    stamp2.zoom = 10

    # Definir a formatação do terceiro objeto carimbo
    # Especificar a informação de alinhamento Vertical para o objeto carimbo como TOPO
    stamp3.vertical_alignment = ap.VerticalAlignment.TOP
    # Definir a informação de alinhamento Horizontal para o objeto carimbo como Centralizado
    stamp3.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Definir o ângulo de rotação para o objeto carimbo
    stamp3.rotate_angle = 35
    # Definir rosa como cor de fundo para o carimbo
    stamp3.text_state.background_color = ap.Color.pink
    # Alterar a informação da fonte do carimbo para Verdana
    stamp3.text_state.font = ap.text.FontRepository.find_font("Verdana")
    # Primeiro carimbo é adicionado na primeira página;
    document.pages[1].add_stamp(stamp1)
    # Segundo carimbo é adicionado na segunda página;
    document.pages[2].add_stamp(stamp2)
    # Terceiro carimbo é adicionado na terceira página.
    document.pages[3].add_stamp(stamp3)

    # Salvar o documento atualizado
    document.save(output_pdf)
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
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>