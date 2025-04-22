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
    "abstract": "Эта функция позволяет бесшовно конвертировать WebForms DataGridView в PDF с использованием библиотеки Aspose.PDF for .NET. Эта функциональность упрощает процесс экспорта данных, интегрируя специализированный контроль экспорта GridView, обеспечивая высококачественный рендеринг PDF непосредственно из веб-приложений. Идеально подходит для разработчиков, ищущих эффективные решения для генерации документов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "226",
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
    "dateModified": "2025-04-11",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но также справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Как экспортировать WebForm в PDF с использованием Aspose.PDF/Aspose.HTML

### Введение

В общем, для конвертации WebForm в PDF документ используются дополнительные инструменты. Этот пример показывает, как использовать библиотеку Aspose.PDF для рендеринга WebForm в PDF. Контроль экспорта Aspose GridView в PDF также включен в этот пример, чтобы показать, как рендерить _контроль GridView в PDF документ._

## Как рендерить WebForm в PDF

Изначальная идея рендеринга WebForm в PDF заключается в создании вспомогательного класса, который наследуется от [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx) и переопределяет метод Render.</em></p>

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

Существует два инструмента Aspose, которые можно использовать для рендеринга HTML в PDF:

- Aspose.PDF for .NET.
- Контроль экспорта Aspose GridView (на основе Aspose.PDF).

## Исходные файлы

Вы можете найти код для всего проекта [здесь](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.Pdf.GridViewExport).

- _Default.aspx_ демонстрирует экспорт в PDF с использованием Aspose.PDF.
- _Report2.aspx_ демонстрирует экспорт в PDF с использованием контроля экспорта Aspose GridView (на основе Aspose.PDF).

## Дополнительные файлы

`Helpers\PdfPage.cs` - содержит вспомогательный класс, который показывает, как использовать API Aspose.PDF.</em>

Проект Aspose.Pdf.GridViewExport содержит расширенный контроль GridView для демонстрации в `Report2.aspx`