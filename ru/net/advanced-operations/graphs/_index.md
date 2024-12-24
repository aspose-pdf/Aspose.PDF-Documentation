---
title: Работа с графиками в PDF файле
linktitle: Работа с графиками
type: docs
weight: 70
url: /ru/net/graphs/
description: В этой статье рассказывается, что такое график, как создать объект заполненного прямоугольника и другие функции
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с графиками в PDF файле",
    "alternativeHeadline": "Как создать графики в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, графики в pdf",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2022-02-04",
    "description": "В этой статье рассказывается, что такое график, как создать объект заполненного прямоугольника и другие функции"
}
</script>
## Что такое граф

Добавление графиков в PDF-документы — это очень распространенная задача для разработчиков при работе с Adobe Acrobat Writer или другими приложениями для обработки PDF. Существует множество типов графиков, которые могут быть использованы в приложениях PDF.
[Aspose.PDF для .NET](/pdf/ru/net/) также поддерживает добавление графиков в PDF-документы. Для этой цели предоставляется класс Graph. Graph является элементом уровня абзаца и может быть добавлен в коллекцию Paragraphs на экземпляре страницы. Экземпляр Graph содержит коллекцию фигур.

Следующие типы фигур поддерживаются классом [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph):

- [Arc](/pdf/ru/net/add-arc/) - иногда также называется флагом, представляет собой упорядоченную пару смежных вершин, но иногда также называется направленной линией.
- [Circle](/pdf/ru/net/add-circle/) - отображает данные с использованием круга, разделенного на секторы. Мы используем круговую диаграмму (также называемую круговой диаграммой), чтобы показать, как данные представляют части целого или одной группы.
- [Curve](/pdf/ru/net/add-curve/) - это соединенный союз проективных линий, каждая линия соединяется с тремя другими в обычных двойных точках.
- [Кривая](/pdf/ru/net/add-curve/) - это соединённый союз проективных линий, каждая линия пересекается с тремя другими в обычных двойных точках.
- [Линия](/pdf/ru/net/add-line) - линейные графики используются для отображения непрерывных данных и могут быть полезны в прогнозировании будущих событий, когда они показывают тенденции со временем.
- [Прямоугольник](/pdf/ru/net/add-rectangle/) - это одна из множества фундаментальных форм, которые вы увидите на графиках, она может быть очень полезной в решении проблем.
- [Эллипс](/pdf/ru/net/add-ellipse/) - это набор точек на плоскости, создающий овальную, изогнутую форму.

Вышеуказанные детали также изображены на рисунках ниже:

![Фигуры в графиках](graphs.png)

