---
title: Работа с изображениями в PDF с использованием C#
linktitle: Работа с изображениями
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/working-with-images/
description: В этом разделе описаны особенности работы с изображениями в файле PDF с использованием библиотеки C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/manipulate-images/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Images in PDF using C#",
    "alternativeHeadline": "Comprehensive Image Handling in PDF with C#",
    "abstract": "Новый функционал в Aspose.PDF для .NET расширяет ваши возможности по управлению изображениями в PDF-документах, предлагая расширенные функции, такие как изменение размера изображений, замена, извлечение и получение подробных свойств изображений. Эта мощная библиотека упрощает процесс добавления графики и работы с ней в ваших PDF-файлах, что делает её важным инструментом для разработчиков, стремящихся эффективно создавать динамические цифровые документы",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF manipulation, Aspose.PDF library, image extraction, add image to PDF, replace image in PDF, set image size, search images in PDF, DICOM image support",
    "wordcount": "578",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/working-with-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-images/"
    },
    "dateModified": "2024-11-26",
    "description": "Этот раздел описывает особенности работы с изображениями в файле PDF с помощью библиотеки C#."
}
</script>

Изображения могут быть довольно сложной темой в формате PDF. Пользователя ждёт широкий спектр манипуляций с изображениями, когда он сталкивается с работой над PDF-документами. Мы привыкли к тому, что картинки можно только добавлять или удалять из файлов, но библиотека Aspose.PDF также позволит вам устанавливать размер изображений, заменять изображения, извлекать изображения, искать и получать изображения из PDF-документов и т. д.

**Как добавить изображение в PDF?** Вы получите ответ на самый популярный вопрос об изображениях в PDF с помощью Aspose.PDF.

**Aspose.PDF for .NET** — это умный и эффективный инструмент для работы с цифровыми документами, который позволяет быстро импортировать и размещать любые графические объекты в существующем PDF-файле.
Наша библиотека C# также будет полезна, если вам нужно вставить диаграмму в отчёт, добавить план этажа к проекту или просто включить фотографию в своё резюме. Если вы ищете продвинутый способ вставки и редактирования изображений в PDF-документ, мы настоятельно рекомендуем изучить следующие статьи для решения ваших задач.

Вы можете:

- [Добавить изображение в существующий PDF-файл](/pdf/net/add-image-to-existing-pdf-file/) — добавляйте изображения и ссылки на одно изображение в документ PDF, а затем контролируйте качество.
- [Удалить изображения из файла PDF](/pdf/net/delete-images-from-pdf-file/) — проверьте фрагмент кода для удаления изображений из файла PDF.
- [Извлечь изображения из файла PDF](/pdf/net/extract-images-from-pdf-file/) — используйте коллекцию Images для извлечения изображений из файла PDF.
- [Получить разрешение и размеры встроенных изображений](/pdf/net/get-resolution-and-dimensions-of-embedded-images/) — используйте классы операторов в пространстве имён Aspose.PDF, которые позволяют получить информацию о разрешении и размерах.
- [Работа с размещением изображений](/pdf/net/working-with-image-placement/) — можно получить разрешение и положение изображения в документе PDF.
- [Поиск и получение изображений из документа PDF](/pdf/net/search-and-get-images-from-pdf-document/) — вы можете получить изображение с отдельной страницы и выполнить поиск среди изображений на всех страницах с помощью C#.
- [Замена изображения в существующем файле PDF](/pdf/net/replace-image-in-existing-pdf-file/) — ознакомьтесь с нашим фрагментом кода, он покажет вам, как заменить изображение в файле PDF.
- [Установка размера изображения](/pdf/net/set-image-size/) — библиотека C# позволяет установить размер изображения.
- [Установка имени шрифта по умолчанию](/pdf/net/set-default-font-name/) — установка имени шрифта по умолчанию для процесса преобразования.
- [Создание уменьшенных изображений из документов PDF](/pdf/net/generate-thumbnail-images-from-pdf-documents/) — в следующей статье показано, как создавать уменьшенные изображения из документов PDF сначала с использованием Acrobat SDK, а затем Aspose.PDF.
- Поддержка изображений DICOM — Aspose.PDF for .NET поддерживает специальный медицинский графический стандарт изображений. Aspose.PDF for .NET позволяет конвертировать изображения DICOM и SVG. Пожалуйста, ознакомьтесь с разделом [Преобразование DICOM в PDF](/pdf/net/convert-images-format-to-pdf/#convert-dicom-to-pdf).
- [Работа с векторной графикой](/pdf/net/working-with-vector-graphics) — в этом разделе описаны возможности работы с инструментом GraphicsAbsorber с использованием C#.

<!-- 5544781043 -->
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "Программное приложение",
    "название": "Библиотека Aspose.PDF for .NET",
    "изображение": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "издательство": {
        "@type": "Организация",
        "название": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "логотип": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.
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