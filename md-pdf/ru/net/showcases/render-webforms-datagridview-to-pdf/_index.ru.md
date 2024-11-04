---
title: Рендеринг WebForms DataGridView в PDF
linktitle: Рендеринг WebForms DataGridView в PDF
type: docs
weight: 20
url: /net/render-webforms-datagridview-to-pdf/
description: Этот пример показывает, как использовать библиотеку Aspose.PDF для рендеринга WebForm в PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Как экспортировать WebForm в PDF с использованием Aspose.PDF/Aspose.HTML

### Введение

В общем случае, для конвертации WebForm в PDF документ требуются дополнительные инструменты. Этот пример демонстрирует, как использовать библиотеку Aspose.PDF для рендеринга WebForm в PDF. В этом примере также включен контроль Aspose Export GridView To Pdf для демонстрации рендеринга _GridView control в PDF документ._

## Как рендерить WebForm в PDF

Основная идея рендеринга WebForm в PDF заключается в создании вспомогательного класса, который наследуется от [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), и переопределении метода Render.

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // рендеринг веб-страницы для PDF документа
    }
    else
    {
        // рендеринг веб-страницы в браузере
        base.Render(writer);
    }
}
```
Для рендеринга HTML в PDF можно использовать два инструмента Aspose:

- Aspose.PDF для .NET
- Aspose Export GridView control (на базе Aspose.PDF)

## Исходные файлы

В этом примере у нас есть 2 демонстрационных отчета.

- _Default.aspx_ демонстрирует экспорт в PDF с использованием Aspose.PDF
- _Report2.aspx_ демонстрирует экспорт в PDF с использованием Aspose Export GridView control (на базе Aspose.PDF)

## Дополнительные файлы

`Helpers\PdfPage.cs` - содержит вспомогательный класс, который показывает, как использовать API Aspose.PDF.

Проект Aspose.Pdf.GridViewExport содержит расширенный контроль GridView для демонстрации в `Report2.aspx`
