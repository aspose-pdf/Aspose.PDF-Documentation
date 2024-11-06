---
title: Удалить таблицы из существующего PDF
linktitle: Удалить таблицы
type: docs
weight: 50
url: ru/python-net/remove-tables-from-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Удалить таблицы из существующего PDF",
    "alternativeHeadline": "Как удалить таблицы из PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF-документов",
    "keywords": "pdf, python, удалить таблицу, удалить таблицы",
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
    "url": "/python-net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


{{% alert color="primary" %}}

Aspose.PDF for Python via .NET предлагает возможности вставки/создания таблицы в PDF-документе, когда он создается с нуля, или вы также можете добавить объект таблицы в любой существующий PDF-документ. Однако у вас может возникнуть необходимость [манипулировать таблицами в существующем PDF](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/), где вы можете обновлять содержимое в существующих ячейках таблицы. Однако вы можете столкнуться с требованием удалить объекты таблицы из существующего PDF-документа.

{{% /alert %}}

Чтобы удалить таблицы, нам необходимо использовать класс [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/), чтобы получить доступ к таблицам в существующем PDF, а затем вызвать метод [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods).

## Удаление таблицы из PDF-документа

Мы добавили новую функцию, т.е.
 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) к существующему классу [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) для удаления таблицы из PDF-документа. Как только абсорбер успешно находит таблицы на странице, он становится способен их удалять. Пожалуйста, ознакомьтесь с следующим фрагментом кода, показывающим, как удалить таблицу из PDF-документа:

```python

    import aspose.pdf as ap

    # Загрузить существующий PDF документ
    pdf_document = ap.Document(input_file)
    # Создать объект TableAbsorber для поиска таблиц
    absorber = ap.text.TableAbsorber()
    # Посетить первую страницу с абсорбером
    absorber.visit(pdf_document.pages[1])
    # Получить первую таблицу на странице
    table = absorber.table_list[0]
    # Удалить таблицу
    absorber.remove(table)
    # Сохранить PDF
    pdf_document.save(output_file)
```

## Удаление нескольких таблиц из PDF-документа

Иногда PDF-документ может содержать более одной таблицы, и может возникнуть необходимость удалить из него несколько таблиц. Для удаления нескольких таблиц из PDF-документа, используйте следующий фрагмент кода:

```python

    import aspose.pdf as ap

    # Загрузить существующий PDF-документ
    pdf_document = ap.Document(input_file)
    # Создать объект TableAbsorber для поиска таблиц
    absorber = ap.text.TableAbsorber()
    # Посетить вторую страницу с поглотителем
    absorber.visit(pdf_document.pages[1])
    # Получить копию коллекции таблиц
    tables = absorber.table_list
    # Перебирать копию коллекции и удалять таблицы
    for table in tables:
        absorber.remove(table)
    # Сохранить документ
    pdf_document.save(output_file)
```

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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
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