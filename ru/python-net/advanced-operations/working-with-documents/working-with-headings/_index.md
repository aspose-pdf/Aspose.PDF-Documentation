---
title: Работа с заголовками в PDF
type: docs
weight: 40
url: /ru/python-net/working-with-headings/
description: Создайте нумерацию в заголовках вашего PDF документа с помощью Python. Aspose.PDF для Python через .NET предлагает различные стили нумерации.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с заголовками в PDF",
    "alternativeHeadline": "Создание заголовков в PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "создание PDF документа",
    "keywords": "pdf, python, заголовки в pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда Aspose.PDF Документов",
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
    "url": "/net/working-with-headings/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-headings/"
    },
    "dateModified": "2022-02-04",
    "description": "Создайте нумерацию в заголовках вашего PDF документа с помощью Python. Aspose.PDF для Python через .NET предлагает различные стили нумерации."
}
</script>


## Применение стиля нумерации в заголовках

Заголовки являются важными частями любого документа. Авторы всегда стараются сделать заголовки более заметными и значимыми для своих читателей. Если в документе больше одного заголовка, у автора есть несколько вариантов организации этих заголовков. Один из самых распространенных подходов к организации заголовков — это написание заголовков в стиле нумерации.

[Aspose.PDF для Python через .NET](/pdf/ru/python-net/) предлагает множество предопределенных стилей нумерации. Эти предопределенные стили нумерации хранятся в перечислении, [NumberingStyle](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/). Предопределенные значения перечисления NumberingStyle и их описания приведены ниже:

|**Типы заголовков**|**Описание**|
| :- | :- |
|NumeralsArabic|Арабский тип, например, 1,1.1,...|
|NumeralsRomanUppercase|Римский верхний тип, например, I,I.II, ...|
|NumeralsRomanLowercase|Римский нижний тип, например, i,i.ii, ...|
|LettersUppercase|Английский верхний тип, например, A,A.B, ...|

|LettersLowercase|Английский нижний тип, например, a,a.b, ...|
Свойство [style](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/#properties) класса [Heading](https://reference.aspose.com/pdf/python-net/aspose.pdf/heading/) используется для установки стилей нумерации заголовков.

|**Рисунок: Предопределенные стили нумерации**|
| :- |
Исходный код, для получения вывода, показанного на рисунке выше, приведен ниже в примере.

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
    heading.text = "Список 1"
    heading.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading.is_auto_sequence = True

    float_box.paragraphs.add(heading)

    heading2 = ap.Heading(1)
    heading2.is_in_list = True
    heading2.start_number = 13
    heading2.text = "Список 2"
    heading2.style = ap.NumberingStyle.NUMERALS_ROMAN_LOWERCASE
    heading2.is_auto_sequence = True

    float_box.paragraphs.add(heading2)

    heading3 = ap.Heading(2)
    heading3.is_in_list = True
    heading3.start_number = 1
    heading3.text = "стоимость, на дату вступления плана в силу, имущества, подлежащего распределению по плану в счет каждого разрешенного"
    heading3.style = ap.NumberingStyle.LETTERS_LOWERCASE
    heading3.is_auto_sequence = True

    float_box.paragraphs.add(heading3)
    document.save(output_pdf)
```


{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для Python через .NET",
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