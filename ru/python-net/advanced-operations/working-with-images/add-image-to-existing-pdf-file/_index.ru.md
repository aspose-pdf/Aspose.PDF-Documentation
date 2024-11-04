---
title: Добавить изображение в PDF с использованием Python
linktitle: Добавить изображение
type: docs
weight: 10
url: /python-net/add-image-to-existing-pdf-file/
description: Этот раздел описывает, как добавить изображение в существующий PDF файл, используя библиотеку Python.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавить изображение в PDF с использованием Python",
    "alternativeHeadline": "Как добавить изображение в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "создание PDF документов",
    "keywords": "pdf, python, добавить изображение в pdf",
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
    "url": "/python-net/add-image-to-existing-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-image-to-existing-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел описывает, как добавить изображение в существующий PDF файл, используя библиотеку Python."
}
</script>


## Добавить изображение в существующий PDF файл

Следующий фрагмент кода показывает, как добавить изображение в PDF файл.

1. Загрузите входной PDF файл.
1. Укажите номер страницы, на которой будет размещено изображение.
1. Чтобы определить позицию изображения на странице, вызовите метод [add_image](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) класса [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Вызовите метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_file)

    document.pages[1].add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    document.save(output_pdf)
```

## Добавить изображение в существующий PDF файл (Facades)

Существует также альтернативный, более простой способ добавить изображение в PDF файл.
 Вы можете использовать метод [AddImage](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/methods/addimage/index) класса [PdfFileMend](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/). Метод [add_image()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods) требует указать изображение для добавления, номер страницы, на которую необходимо добавить изображение, и информацию о координатах. После этого сохраните обновленный PDF файл и закройте объект PdfFileMend с помощью метода [close()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilemend/#methods). Следующий фрагмент кода показывает, как добавить изображение в существующий файл PDF.

```python

    import aspose.pdf as ap

    # Открыть документ
    mender = ap.facades.PdfFileMend()

    # Создать объект PdfFileMend для добавления текста
    mender.bind_pdf(input_file)

    # Добавить изображение в файл PDF
    mender.add_image(image_file, 1, 100.0, 600.0, 200.0, 700.0)

    # Сохранить изменения
    mender.save(output_pdf)

    # Закрыть объект PdfFileMend
    mender.close()

```

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
    "applicationCategory": "Библиотека для манипуляции с PDF для Python",
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