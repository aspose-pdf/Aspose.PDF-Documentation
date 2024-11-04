---
title: Trabalhando com Títulos em PDF
type: docs
weight: 40
url: /python-net/working-with-headings/
description: Crie numeração no título do seu documento PDF com Python. Aspose.PDF para Python via .NET oferece diferentes tipos de estilos de numeração.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Títulos em PDF",
    "alternativeHeadline": "Crie Títulos em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, títulos em pdf",
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
    "url": "/net/working-with-headings/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-headings/"
    },
    "dateModified": "2022-02-04",
    "description": "Crie numeração no título do seu documento PDF com Python. Aspose.PDF para Python via .NET oferece diferentes tipos de estilos de numeração."
}
</script>


## Aplicar Estilo de Numeração em Cabeçalhos

Cabeçalhos são partes importantes de qualquer documento. Os escritores sempre tentam tornar os cabeçalhos mais proeminentes e significativos para seus leitores. Se houver mais de um cabeçalho em um documento, um escritor tem várias opções para organizar esses cabeçalhos. Uma das abordagens mais comuns para organizar cabeçalhos é escrever cabeçalhos no Estilo de Numeração.

[Aspose.PDF para Python via .NET](/pdf/python-net/) oferece muitos estilos de numeração predefinidos. Esses estilos de numeração predefinidos são armazenados em uma enumeração, [NumberingStyle](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/). Os valores predefinidos da enumeração NumberingStyle e suas descrições são apresentados abaixo:

|**Tipos de Cabeçalhos**|**Descrição**|
| :- | :- |
|NumeralsArabic|Tipo árabe, por exemplo, 1,1.1,...|
|NumeralsRomanUppercase|Tipo romano maiúsculo, por exemplo, I,I.II, ...|
|NumeralsRomanLowercase|Tipo romano minúsculo, por exemplo, i,i.ii, ...|
|LettersUppercase|Tipo inglês maiúsculo, por exemplo, A,A.B, ...|

|LettersLowercase|Tipo inglês minúsculo, por exemplo, a,a.b, ...|
A propriedade [style](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/#properties) da classe [Heading](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/) é usada para definir os estilos de numeração dos cabeçalhos.

|**Figura: Estilos de numeração predefinidos**|
| :- |
O código-fonte, para obter a saída mostrada na figura acima, é fornecido abaixo no exemplo.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.page_info.width = 612.0
    document.page_info.height = 792.0
    document.page_info.margin = ap.MarginInfo()
    document.page_info.margin.left = 72
    document.page_info.margin.right = 72
    document.page_info.margin.top = 72
    document.page_info.margin.bottom = 72

    page = document.pages.add()
    page.page_info.width = 612.0
    page.page_info.height = 792.0
    page.page_info.margin = ap.MarginInfo()
    page.page_info.margin.left = 72
    page.page_info.margin.right = 72
    page.page_info.margin.top = 72
    page.page_info.margin.bottom = 72

    float_box = ap.FloatingBox()
    float_box.margin = page.page_info.margin

    page.paragraphs.add(float_box)

    heading = ap.Heading(1)
    heading.is_in_list = True
    heading.start_number = 1
    heading.text = "Lista 1"
    heading.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading.is_auto_sequence = True

    float_box.paragraphs.add(heading)

    heading2 = ap.Heading(1)
    heading2.is_in_list = True
    heading2.start_number = 13
    heading2.text = "Lista 2"
    heading2.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading2.is_auto_sequence = True

    float_box.paragraphs.add(heading2)

    heading3 = ap.Heading(2)
    heading3.is_in_list = True
    heading3.start_number = 1
    heading3.text = "o valor, na data efetiva do plano, da propriedade a ser distribuída sob o plano em relação a cada permitido"
    heading3.style = ap.NumberingStyle.LETTERS_LOWERCASE
    heading3.is_auto_sequence = True

    float_box.paragraphs.add(heading3)
    document.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Biblioteca .NET",
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para Python via .NET",
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