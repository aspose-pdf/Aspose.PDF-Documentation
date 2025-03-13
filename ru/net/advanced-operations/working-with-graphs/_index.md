---
title: Работа с графиками в PDF файле
linktitle: Работа с графиками
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ru/net/working-with-graphs/
description: Эта статья объясняет, что такое график, как создать объект заполненного прямоугольника и другие функции
lastmod: "2022-02-17"
sitemap:
changefreq: "weekly"
priority: 0.7
aliases:
- /net/working-with-graphs/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Graphs in PDF file",
    "alternativeHeadline": "Create and Manipulate Graphs in PDF Files",
    "abstract": "Откройте для себя мощную новую функцию для генерации и манипуляции графиками в PDF документах с использованием Aspose.PDF for .NET. Эта функциональность позволяет разработчикам создавать различные формы графиков, включая дуги, круги, линии и прямоугольники, улучшая визуальное представление данных в их приложениях. Оптимизируйте процесс генерации PDF и легко предоставляйте динамические визуализации данных.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Graph, PDF documents, Aspose.PDF for .NET, Graph class, Shapes, Arc, Circle, Line graph, Rectangle, PDF manipulation",
    "wordcount": "329",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2024-11-25",
    "description": "Эта статья объясняет, что такое график, как создать объект заполненного прямоугольника и другие функции"
}
</script>

## Что такое график

Добавление графиков в PDF документы является очень распространенной задачей для разработчиков при работе с Adobe Acrobat Writer или другими приложениями для обработки PDF. Существует множество типов графиков, которые можно использовать в PDF приложениях.
[Aspose.PDF for .NET](/pdf/net/) также поддерживает добавление графиков в PDF документы. Для этой цели предоставляется класс Graph. График является элементом на уровне абзаца и может быть добавлен в коллекцию Paragraphs в экземпляре Page. Экземпляр Graph содержит коллекцию Shapes.

Следующие типы фигур поддерживаются классом [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [Arc](/pdf/net/add-arc/) - иногда также называется флагом, представляет собой упорядоченную пару смежных вершин, но иногда также называется направленной линией.
- [Circle](/pdf/net/add-circle/) - отображает данные с использованием круга, разделенного на сектора. Мы используем круговой график (также называемый круговой диаграммой), чтобы показать, как данные представляют собой части одного целого или одной группы.
- [Curve](/pdf/net/add-curve/) - это связное объединение проективных линий, каждая из которых пересекается с тремя другими в обычных двойных точках.
- [Line](/pdf/net/add-line) - линейные графики используются для отображения непрерывных данных и могут быть полезны для прогнозирования будущих событий, когда они показывают тенденции с течением времени.
- [Rectangle](/pdf/net/add-rectangle/) - это одна из многих основных фигур, которые вы увидите в графиках, она может быть очень полезной для решения проблемы.
- [Ellipse](/pdf/net/add-ellipse/) - это множество точек на плоскости, создающее овальную, изогнутую форму.

Следующие операции поддерживаются для типов фигур:
- [Check bounds](/pdf/net/aspose-pdf-drawing-graph-shapes-bounds-check/) - проверка границ фигуры в коллекции Shapes.

Вышеуказанные детали также изображены на рисунках ниже:

![Фигуры в графиках](graphs.png)

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