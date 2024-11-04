---
title: Работа со страницами PDF в C#
linktitle: Работа со страницами
type: docs
weight: 20
url: /net/working-with-pages/
description: Как добавить страницы, добавить колонтитулы, добавить водяные знаки, вы можете узнать в этом разделе. Aspose.PDF для .NET объяснит вам все детали по этой теме.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа со страницами PDF в C#",
    "alternativeHeadline": "Как работать со страницами PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, страница pdf, добавление страницы pdf, добавление номера страницы, поворот страницы, удаление страницы",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Как добавить страницы, добавить колонтитулы, добавить водяные знаки, вы можете узнать в этом разделе. Aspose.PDF для .NET объяснит вам все детали по этой теме."
}
</script>
**Aspose.PDF для .NET** позволяет вставлять страницу в документ PDF в любом месте файла, а также добавлять страницы в конец файла PDF. Этот раздел показывает, как добавлять страницы в PDF без Acrobat Reader.
Вы можете добавлять текст или изображения в колонтитулы вашего файла PDF, а также выбирать разные колонтитулы в вашем документе с помощью библиотеки C# от Aspose.
Также попробуйте программно обрезать страницы в документе PDF с помощью C#.

Этот раздел научит вас, как добавлять водяные знаки в ваш файл PDF с использованием класса Artifact. Вы ознакомитесь с программным примером для этой задачи.
Добавьте номер страницы с помощью класса PageNumberStamp. Для добавления штампа в ваш документ используйте классы ImageStamp и TextStamp. Используйте добавление водяного знака для создания фоновых изображений в вашем файле PDF с **Aspose.PDF для .NET**.

Вы можете делать следующее:

- [Добавить страницы](/pdf/net/add-pages/) - добавить страницы в нужное место или в конец файла PDF и удалить страницу из вашего документа.
- [Переместить страницы](/pdf/net/move-pages/) - переместить страницы из одного документа в другой.
- [Переместить страницы](/pdf/net/move-pages/) - переместить страницы из одного документа в другой.
- [Удалить страницы](/pdf/net/delete-pages/) - удалить страницу из вашего PDF-файла с использованием коллекции PageCollection.
- [Изменить размер страницы](/pdf/net/change-page-size/) - вы можете изменить размер страницы PDF с помощью фрагмента кода, используя библиотеку Aspose.PDF.
- [Повернуть страницы](/pdf/net/rotate-pages/) - вы можете изменить ориентацию страниц в существующем PDF-файле.
- [Разделить страницы](/pdf/net/split-document/) - вы можете разделить PDF-файлы на один или несколько PDF.
- [Добавить заголовки и/или нижние колонтитулы](/pdf/net/add-headers-and-footers-of-pdf-file/) - добавить текст или изображения в заголовки и нижние колонтитулы вашего PDF-файла.
- [Обрезать страницы](/pdf/net/crop-pages/) - вы можете программно обрезать страницы в PDF-документе с использованием различных свойств страницы.
- [Добавить водяные знаки](/pdf/net/add-watermarks/) - добавить водяные знаки в ваш PDF-файл с использованием класса Artifact.
- [Добавить нумерацию страниц в PDF-файл](/pdf/net/add-page-number/) - класс PageNumberStamp поможет вам добавить номер страницы в ваш PDF-файл.
- [Добавление нумерации страниц в PDF-файле](/pdf/net/add-page-number/) - Класс PageNumberStamp поможет вам добавить номера страниц в ваш PDF-файл.
- [Добавление фонов](/pdf/net/add-backgrounds/) - фоновые изображения могут использоваться для добавления водяных знаков.
- [Штамповка](/pdf/net/stamping/) - вы можете использовать класс ImageStamp для добавления изображения-штампа в PDF-файл и класс TextStamp для добавления текста.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

