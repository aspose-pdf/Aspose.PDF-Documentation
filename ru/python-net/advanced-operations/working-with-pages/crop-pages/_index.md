---
title: Обрезка страниц PDF программно на Python
linktitle: Обрезка страниц
type: docs
weight: 70
url: ru/python-net/crop-pages/
description: Вы можете получить свойства страницы, такие как ширина, высота, bleed-, crop- и trimbox, используя Aspose.PDF для Python через .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Обрезка страниц PDF программно через Python",
    "alternativeHeadline": "Как обрезать страницы PDF на Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, обрезка страниц pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Вы можете получить свойства страницы, такие как ширина, высота, bleed-, crop- и trimbox, используя Aspose.PDF для Python через .NET."
}
</script>


## Получить свойства страницы

Каждая страница в PDF-файле имеет ряд свойств, таких как ширина, высота, bleed-, crop- и trimbox. Aspose.PDF для Python позволяет вам получить доступ к этим свойствам.

- **media_box**: Media box — это самый большой короб страницы. Он соответствует размеру страницы (например, A4, A5, US Letter и т. д.), выбранному при печати документа в PostScript или PDF. Другими словами, media box определяет физический размер носителя, на котором PDF-документ отображается или распечатывается.
- **bleed_box**: Если в документе есть вылет, в PDF будет также присутствовать bleed box. Вылет — это количество цвета (или графики), выходящее за край страницы. Он используется для того, чтобы при печати и обрезке документа до нужного размера ("обрезке") краска доходила до самого края страницы. Даже если страница обрезана неправильно - немного за пределами меток обрезки - на странице не появятся белые края.
- **trim_box**: Trim box указывает окончательный размер документа после печати и обрезки.
- **art_box**: Art box — это прямоугольник, нарисованный вокруг фактического содержимого страниц в ваших документах.
 Эта страница используется при импорте PDF документов в другие приложения.
- **crop_box**: Область обрезки — это размер "страницы", в котором ваш PDF документ отображается в Adobe Acrobat. В обычном режиме в Adobe Acrobat отображается только содержимое области обрезки. Для подробных описаний этих свойств прочитайте спецификацию Adobe.Pdf, особенно 10.10.1 Page Boundaries.

Ниже показано, как обрезать страницу:

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)

    # Создать новый прямоугольник Box
    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_pdf)
```

В этом примере мы использовали тестовый файл [здесь](crop_page.pdf). Изначально наша страница выглядит, как показано на Рисунке 1.
![Рисунок 1. Обрезанная страница](crop_page.png)

После изменения страница будет выглядеть, как на Рисунке 2.
![Рисунок 2. Обрезанная страница](crop_page2.png)

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python через .NET Библиотека",
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
    "applicationCategory": "Библиотека для манипуляции PDF для Python",
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