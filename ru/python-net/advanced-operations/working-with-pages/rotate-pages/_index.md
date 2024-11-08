---
title: Поворот страниц PDF с использованием Python
linktitle: Поворот страниц PDF
type: docs
weight: 110
url: /ru/python-net/rotate-pages/
description: Эта тема описывает, как программно изменить ориентацию страниц в существующем PDF-файле с помощью Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Поворот страниц PDF с использованием Python",
    "alternativeHeadline": "Как повернуть страницы PDF с помощью Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF-документов",
    "keywords": "pdf, python, поворот страницы pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/rotate-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Эта тема описывает, как программно изменить ориентацию страниц в существующем PDF-файле с помощью Python."
}
</script>


Этот топик описывает, как обновить или изменить ориентацию страниц в существующем PDF-файле программно с помощью Python.

## Изменение Ориентации Страницы

Aspose.PDF для Python через .NET поддерживает отличные функции, такие как изменение ориентации страницы с альбомной на портретную и наоборот. Чтобы изменить ориентацию страницы, установите MediaBox страницы, используя следующий фрагмент кода. Вы также можете изменить ориентацию страницы, установив угол поворота с помощью метода 'rotate'.

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    for page in doc.pages:
        r = page.media_box
        newHeight = r.width
        newWidth = r.height
        newLLX = r.llx
        #  Мы должны переместить страницу вверх, чтобы компенсировать изменение размера страницы
        # (нижняя граница страницы - это 0,0, и информация обычно размещается с
        #  верхней части страницы. Поэтому мы перемещаем нижнюю границу вверх на разницу между
        #  старой и новой высотой.
        newLLY = r.lly + (r.height - newHeight)
        page.media_box = ap.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight, True)
        # Иногда нам также нужно установить CropBox (если он был установлен в оригинальном файле)
        page.crop_box = ap.Rectangle(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight, True)

        # Установка угла поворота страницы
        page.rotate = ap.Rotation.ON90

    # Сохранить выходной файл
    doc.save(output_pdf)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python через .NET библиотека",
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
    "applicationCategory": "Библиотека для работы с PDF для Python",
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