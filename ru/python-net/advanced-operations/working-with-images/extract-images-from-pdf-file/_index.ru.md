---
title: Извлечение изображений из PDF файла с использованием Python
linktitle: Извлечение изображений
type: docs
weight: 30
url: /python-net/extract-images-from-pdf-file/
description: Этот раздел показывает, как извлечь изображения из PDF файла с использованием библиотеки Python.
lastmod: "2023-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Извлечение изображений из PDF файла с использованием Python",
    "alternativeHeadline": "Как извлечь изображения из PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, Python, извлечение изображений из pdf",
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
    "url": "/python-net/extract-images-from-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extract-images-from-pdf-file/"
    },
    "dateModified": "2023-02-04",
    "description": "Этот раздел показывает, как извлечь изображения из PDF файла с использованием библиотеки Python."
}
</script>


Вам нужно извлечь изображения из ваших PDF файлов? Для упрощенного управления, архивирования, анализа или обмена изображениями ваших документов используйте **Aspose.PDF for Python** и извлекайте изображения из PDF файлов.

Изображения хранятся в [ресурсах](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) каждой страницы в коллекции [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximagecollection/). Чтобы извлечь изображение с определенной страницы, получите изображение из коллекции Images, используя индекс конкретного изображения.

Индекс изображения возвращает объект [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/). Этот объект предоставляет метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), который может быть использован для сохранения извлеченного изображения. Следующий фрагмент кода показывает, как извлекать изображения из PDF файла.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_file)

    # Извлечь конкретное изображение
    xImage = document.pages[2].resources.images[1]
    outputImage = io.FileIO(output_image, "w")

    # Сохранить извлеченное изображение
    xImage.save(outputImage)
    outputImage.close()
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для Python",
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