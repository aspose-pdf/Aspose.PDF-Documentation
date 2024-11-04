---
title: Работа с портфолио в PDF с использованием Python
linktitle: Portfolio
type: docs
weight: 20
url: /python-net/portfolio/
description: Как создать PDF-портфолио с помощью Python. Вы должны использовать файл Microsoft Excel, документ Word и файл изображения для создания PDF-портфолио.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с портфолио в PDF с использованием Python",
    "alternativeHeadline": "Создание портфолио в PDF документе",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, портфолио",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда Aspose.PDF Doc",
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
    "url": "/python-net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/portfolio/"
    },
    "dateModified": "2023-02-04",
    "description": "Как создать PDF-портфолио с помощью Python. Вы должны использовать файл Microsoft Excel, документ Word и файл изображения для создания PDF-портфолио."
}
</script>


Создание PDF-портфолио позволяет консолидировать и архивировать различные типы файлов в одном, согласованном документе. Такой документ может включать текстовые файлы, изображения, электронные таблицы, презентации и другие материалы, обеспечивая хранение и организацию всех соответствующих материалов в одном месте.

PDF-портфолио поможет продемонстрировать вашу презентацию в высоком качестве, где бы вы ни использовали её. В общем, создание PDF-портфолио — это очень актуальная и современная задача.

## Как создать PDF-портфолио

Aspose.PDF для Python через .NET позволяет создавать документы PDF-портфолио с использованием класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Добавьте файл в объект document.collection после получения его с помощью класса [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/). Когда файлы добавлены, используйте метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) класса Document для сохранения портфолио-документа.

Следующий пример использует файл Microsoft Excel, документ Word и файл изображения для создания PDF-портфолио.

The code below results in the following portfolio.

### PDF Портфолио, созданное с помощью Aspose.PDF для Python

![PDF Портфолио, созданное с помощью Aspose.PDF для Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Создать объект документа
    document = ap.Document()

    # Создать объект коллекции документа
    document.collection = ap.Collection()

    # Получить файлы для добавления в портфолио
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Указать описание файлов
    excel.description = "Файл Excel"
    word.description = "Файл Word"
    image.description = "Файл изображения"

    # Добавить файлы в коллекцию документа
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Сохранить документ портфолио
    document.save(output_pdf)
```

## Удаление файлов из PDF Портфолио

Чтобы удалить файлы из PDF портфолио, попробуйте использовать следующие строки кода.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Сохранить обновленный файл
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
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
    "applicationCategory": "PDF Manipulation Library for Python",
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