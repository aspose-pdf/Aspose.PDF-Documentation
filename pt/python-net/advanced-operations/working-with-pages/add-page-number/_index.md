---
title: Adicionar Número de Página ao PDF com Python
linktitle: Adicionar Número de Página
type: docs
weight: 30
url: pt/python-net/add-page-number/
description: Aspose.PDF para Python via .NET permite que você adicione Carimbo de Número de Página ao seu arquivo PDF usando a classe PageNumberStamp.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adicionar Número de Página ao PDF com Python",
    "alternativeHeadline": "Como adicionar Carimbo de Número de Página ao PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, carimbo de número de página",
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
    "url": "/python-net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para Python via .NET permite que você adicione Carimbo de Número de Página ao seu arquivo PDF usando a classe PageNumberStamp."
}
</script>


All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document. **Aspose.PDF para Python via .NET** permite adicionar números de página com [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

Você pode usar a classe [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) para adicionar uma marca de número de página em um arquivo PDF.
 [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) class fornece propriedades necessárias para criar um carimbo baseado em número de página como formato, margens, alinhamentos, número inicial etc. Para adicionar um carimbo de número de página, você precisa criar um objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) e um objeto [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) usando as propriedades necessárias. Depois disso, você pode chamar o método [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) da [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para adicionar o carimbo no PDF. Você também pode definir os atributos de fonte do carimbo de número de página. O trecho de código a seguir mostra como adicionar números de página em um arquivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Criar carimbo de número de página
    page_number_stamp = ap.PageNumberStamp()
    # Se o carimbo é de fundo
    page_number_stamp.background = False
    page_number_stamp.format = "Página # de " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Definir propriedades do texto
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.aqua

    # Adicionar carimbo à página específica
    document.pages[1].add_stamp(page_number_stamp)

    # Salvar documento de saída
    document.save(output_pdf)
```

## Exemplo ao Vivo

[Adicionar números de página em PDF](https://products.aspose.app/pdf/page-number) é uma aplicação web gratuita online que permite investigar como a funcionalidade de adicionar números de página funciona.

[![Como adicionar número de página em pdf usando Python](page_number.png)](https://products.aspose.app/pdf/page-number)

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