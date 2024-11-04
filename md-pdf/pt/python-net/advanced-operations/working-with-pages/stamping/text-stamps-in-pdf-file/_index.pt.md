---
title: Adicionar Carimbos de Texto em PDF via Python
linktitle: Carimbos de Texto em Arquivo PDF
type: docs
weight: 20
url: /python-net/text-stamps-in-the-pdf-file/
description: Adicione um carimbo de texto a um documento PDF usando a classe TextStamp com a biblioteca Aspose.PDF para Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Carimbos de Texto em PDF Python",
    "alternativeHeadline": "Adicionar Carimbos de Texto em PDF Python",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, geração de documentos",
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
    "url": "/python-net/text-stamps-in-the-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-stamps-in-the-pdf-file/"
    },
    "dateModified": "2023-04-04",
    "description": "Adicione um carimbo de texto a um documento PDF usando a classe TextStamp com a biblioteca Aspose.PDF para Python."
}
</script>


## Adicionar Carimbo de Texto com Python

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) para adicionar um carimbo de texto em um arquivo PDF. A classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) fornece propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar um carimbo de texto, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Após isso, você pode chamar o método [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) da Página para adicionar o carimbo no PDF. O trecho de código a seguir mostra como adicionar um carimbo de texto no arquivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Criar carimbo de texto
    text_stamp = ap.TextStamp("Carimbo de Exemplo")
    # Definir se o carimbo é de fundo
    text_stamp.background = True
    # Definir origem
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotacionar carimbo
    text_stamp.rotate = ap.Rotation.ON90
    # Definir propriedades do texto
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # Adicionar carimbo a uma página específica
    document.pages[1].add_stamp(text_stamp)

    # Salvar documento de saída
    document.save(output_pdf)
```


## Definir alinhamento para o objeto TextStamp

Adicionar marcas d'água a documentos PDF é um dos recursos frequentemente exigidos e o Aspose.PDF para Python é totalmente capaz de adicionar marcas d'água de imagem, bem como de texto. Temos uma classe chamada [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) que fornece o recurso de adicionar carimbos de texto sobre o arquivo PDF. Recentemente, houve a necessidade de suportar o recurso de especificar o alinhamento do texto ao usar o objeto TextStamp. Portanto, para atender a esse requisito, introduzimos a propriedade [text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) na classe [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/). Usando essa propriedade, podemos especificar o alinhamento de texto [horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties).

Os trechos de código a seguir mostram um exemplo de como carregar um documento PDF existente e adicionar TextStamp sobre ele.

```python

    import aspose.pdf as ap

    # Instanciar objeto Document com arquivo de entrada
    doc = ap.Document(input_pdf)
    # Instanciar objeto FormattedText com string de exemplo
    text = ap.facades.FormattedText("This")
    # Adicionar nova linha de texto ao FormattedText
    text.add_new_line_text("is sample")
    text.add_new_line_text("Center Aligned")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Object")
    # Criar objeto TextStamp usando FormattedText
    stamp = ap.TextStamp(text)
    # Especificar o Alinhamento Horizontal do carimbo de texto como Alinhado ao Centro
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Especificar o Alinhamento Vertical do carimbo de texto como Alinhado ao Centro
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # Especificar o Alinhamento Horizontal do Texto do TextStamp como Alinhado ao Centro
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # Definir margem superior para o objeto de carimbo
    stamp.top_margin = 20
    # Adicionar o objeto de carimbo sobre a primeira página do documento
    doc.pages[1].add_stamp(stamp)

    # Salvar o documento atualizado
    doc.save(output_pdf)
```


## Preencher Texto de Contorno como Carimbo em Arquivo PDF

Implementamos a configuração do modo de renderização para cenários de adição e edição de texto. Para renderizar texto de contorno, por favor, crie um objeto TextState para transferir propriedades avançadas. Defina a cor para o contorno. Depois, defina o modo de renderização de texto. O próximo passo é vincular o TextState e adicionar o Carimbo.

O trecho de código a seguir demonstra a adição de Texto de Contorno Preenchido:

```python

    import aspose.pdf as ap

    # Criar objeto TextState para transferir propriedades avançadas
    ts = ap.text.TextState()
    # Definir cor para o contorno
    ts.stroking_color = ap.Color.gray
    # Definir modo de renderização de texto
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # Carregar um documento PDF de entrada
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAGO INTEGRALMENTE",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # Vincular TextState
    stamp.bind_text_state(ts)
    # Definir origem X,Y
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # Adicionar Carimbo
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
```


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