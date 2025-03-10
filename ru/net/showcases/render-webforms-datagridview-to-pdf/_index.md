---
title: Рендеринг DataGridView из WebForms в PDF
linktitle: Рендеринг DataGridView из WebForms в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/render-webforms-datagridview-to-pdf/
description: Этот пример показывает, как использовать библиотеку Aspose.PDF для рендеринга WebForm в PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render WebForms DataGridView to PDF",
    "alternativeHeadline": "Effortlessly Convert WebForms DataGridView to PDF",
    "abstract": "Функция позволяет легко преобразовывать DataGridView веб-форм в PDF с помощью библиотеки Aspose.PDF для .NET. Эта функция упрощает процесс экспорта данных за счёт интеграции специального элемента управления экспортом GridView, обеспечивая высококачественное отображение PDF непосредственно из веб-приложений. Идеально подходит для разработчиков, ищущих эффективные решения для создания документов",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "266",
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
    "url": "/net/render-webforms-datagridview-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-webforms-datagridview-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Как экспортировать WebForm в PDF с использованием Aspose.PDF/Aspose.HTML

### Введение

Обычно для преобразования WebForm в документ PDF используются дополнительные инструменты. Этот пример показывает, как использовать библиотеку Aspose.PDF для рендеринга WebForm в PDF. В этот пример также включён элемент управления Aspose Export GridView To Pdf для демонстрации того, как отобразить элемент управления _GridView в документе PDF._

## Как отобразить WebForm в PDF

Основная идея отображения WebForm в PDF заключается в создании вспомогательного класса, который наследуется от [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), и переопределении метода Render.</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // render web page for PDF document
    }
    else
    {
        // render web page in browser
        base.Render(writer);
    }
}
```

Для отображения HTML в PDF можно использовать два инструмента Aspose:

- Aspose.PDF for .NET.
- Элемент управления Aspose Export GridView (на основе Aspose.PDF).

## Исходные файлы

В этом примере у нас есть два демонстрационных отчёта.

- _Default.aspx_ демонстрирует экспорт в PDF с использованием Aspose.PDF.
- _Report2.aspx_ демонстрирует экспорт в PDF с использованием элемента управления Aspose Export GridView (на основе Aspose.PDF).

## Дополнительные файлы

`Helpers\PdfPage.cs` — содержит вспомогательный класс, который показывает, как использовать API Aspose.PDF.</em>

Проект Aspose.Pdf.GridViewExport содержит расширенный элемент управления GridView для демонстрации в `Report2.aspx`