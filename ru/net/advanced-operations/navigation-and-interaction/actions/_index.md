---
title: Работа с действиями в PDF
linktitle: Действия
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/actions/
description: В этом разделе объясняется, как программно добавлять действия в документ и поля формы с помощью C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Actions in PDF",
    "alternativeHeadline": "Programmatic Actions in PDF with C#",
    "abstract": "Новая функция в Aspose.PDF for .NET позволяет разработчикам программно добавлять действия в PDF, повышая интерактивность документов. Пользователи могут реализовывать гиперссылки для навигации внутри документа или на внешние URL, а также управлять действиями при открытии документа, чтобы контролировать отображение PDF при открытии. Эта мощная функциональность упрощает создание и взаимодействие с документами для приложений на C#.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF actions, hyperlink creation, LinkAnnotation, LocalHyperlink, FreeTextAnnotation, document open action, XYZExplicitDestination, Aspose.PDF, PDF manipulation",
    "wordcount": "3258",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2025-03-29",
    "description": "Этот раздел объясняет, как программно добавлять действия к документу и полям формы с использованием C#."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/ru/net/drawing/) library.

## Добавление гиперссылки в PDF-файл

Можно добавлять гиперссылки в PDF-файлы, чтобы позволить читателям переходить к другой части PDF или к внешнему контенту.

Чтобы добавить веб-гиперссылки в PDF-документы:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).
1. Получите [Page](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page), на которую нужно добавить ссылку.
1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/linkannotation), используя объекты Page и [Rectangle](https://reference.aspose.com/pdf/ru/net/aspose.pdf/rectangle). Объект Rectangle используется для указания местоположения на странице, куда следует добавить ссылку.
1. Установите свойство Action в объект [GoToURIAction](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/gotouriaction), который указывает местоположение удаленного URI.
1. Чтобы отобразить текст гиперссылки, добавьте текстовую строку в место, аналогичное тому, где размещен объект [LinkAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/linkannotation).
1. Чтобы добавить свободный текст:

- Создайте объект [FreeTextAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/freetextannotation). Он также принимает объекты Page и Rectangle в качестве аргументов, поэтому можно указать те же значения, что и в конструкторе LinkAnnotation.
- Используя свойство Contents объекта [FreeTextAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/freetextannotation), укажите строку, которая должна отображаться в выходном PDF.
- При желании установите ширину границы объектов [LinkAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/linkannotation) и FreeTextAnnotation в 0, чтобы они не отображались в PDF-документе.
- После определения объектов [LinkAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/linkannotation) и [FreeTextAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/freetextannotation) добавьте эти ссылки в коллекцию Annotations объекта [Page](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page).
- Наконец, сохраните обновленный PDF с помощью метода [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save) объекта [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).

Следующий фрагмент кода показывает, как добавить гиперссылку в PDF-файл.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf"))
    {
        // Get page
        var page = document.Pages[1];
        // Create Link annotation object
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        // Create border object for LinkAnnotation
        var border = new Aspose.Pdf.Annotations.Border(link);
        // Set the border width value as 0
        border.Width = 0;
        // Set the border for LinkAnnotation
        link.Border = border;
        // Specify the link type as remote URI
        link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
        // Add link annotation to annotations collection of first page of PDF file
        page.Annotations.Add(link);

        // Create Free Text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
        // String to be added as Free text
        textAnnotation.Contents = "Link to Aspose website";
        // Set the border for Free Text Annotation
        textAnnotation.Border = border;
        // Add FreeText annotation to annotations collection of first page of Document
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf");
    // Get page
    var page = document.Pages[1];
    // Create Link annotation object
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    // Create border object for LinkAnnotation
    var border = new Aspose.Pdf.Annotations.Border(link);
    // Set the border width value as 0
    border.Width = 0;
    // Set the border for LinkAnnotation
    link.Border = border;
    // Specify the link type as remote URI
    link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
    // Add link annotation to annotations collection of first page of PDF file
    page.Annotations.Add(link);

    // Create Free Text annotation
    var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
    // String to be added as Free text
    textAnnotation.Contents = "Link to Aspose website";
    // Set the border for Free Text Annotation
    textAnnotation.Border = border;
    // Add FreeText annotation to annotations collection of first page of Document
    document.Pages[1].Annotations.Add(textAnnotation);

    // Save PDF document
    document.Save(dataDir + "AddHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

Другой распространенный сценарий — найти заданный текст в документе с помощью TextFragmentAbsorber и установить его область как гиперссылки на сайт. Ниже приведен фрагмент кода, реализующий это.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlinkForExistingText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf"))
    {
        // Get page
        var page = document.Pages[1];

        // The text in the document for which we want to create a link
        string textForLink = "Portable Document Format";

        // Finding the location of text on a page
        var textFragmentAbsosrber = new Aspose.Pdf.Text.TextFragmentAbsorber(textForLink);
        page.Accept(textFragmentAbsosrber);
        foreach(Aspose.Pdf.Text.TextFragment textFragment in textFragmentAbsosrber.TextFragments)
        {
            // Create Link annotation object
            var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, textFragment.Rectangle);
            // Create border object for LinkAnnotation
            var border = new Aspose.Pdf.Annotations.Border(link);
            // Set the border width value as 0
            border.Width = 0;
            // Set the border for LinkAnnotation
            link.Border = border;
            // Specify the link type as remote URI
            link.Action = new Aspose.Pdf.Annotations.GoToURIAction("https://www.pdfa-inc.org/");
            // Add link annotation to annotations collection of first page of PDF file
            page.Annotations.Add(link);
        }

        // Save PDF document
        document.Save(dataDir + "AddHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlinkForExistingText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf");

    // Get page
    var page = document.Pages[1];

    // The text in the document for which we want to create a link
    string textForLink = "Portable Document Format";

    // Finding the location of text on a page
    var textFragmentAbsosrber = new Aspose.Pdf.Text.TextFragmentAbsorber(textForLink);
    page.Accept(textFragmentAbsosrber);
    foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentAbsosrber.TextFragments)
    {
        // Create Link annotation object
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, textFragment.Rectangle);
        // Create border object for LinkAnnotation
        var border = new Aspose.Pdf.Annotations.Border(link);
        // Set the border width value as 0
        border.Width = 0;
        // Set the border for LinkAnnotation
        link.Border = border;
        // Specify the link type as remote URI
        link.Action = new Aspose.Pdf.Annotations.GoToURIAction("https://www.pdfa-inc.org/");
        // Add link annotation to annotations collection of first page of PDF file
        page.Annotations.Add(link);
    }

    // Save PDF document
    document.Save(dataDir + "AddHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Создание гиперссылки на страницы в том же PDF

Aspose.PDF for .NET предоставляет отличные возможности для создания PDF, а также для его редактирования. Также предлагается функция добавления ссылок на страницы PDF, и ссылка может вести на страницы в другом PDF-файле, веб-URL, запускать приложение или даже ссылаться на страницы в том же PDF-файле. Чтобы добавить локальные гиперссылки (ссылки на страницы в том же PDF-файле), в пространство имен Aspose.PDF добавлен класс [LocalHyperlink](https://reference.aspose.com/pdf/ru/net/aspose.pdf/localhyperlink), у которого есть свойство TargetPageNumber, используемое для указания целевой страницы для гиперссылки.

Чтобы добавить локальную гиперссылку, необходимо создать TextFragment, чтобы ссылка могла быть связана с TextFragment. Класс [TextFragment](https://reference.aspose.com/pdf/ru/net/aspose.pdf.text/textfragment) имеет свойство Hyperlink, которое используется для связывания экземпляра LocalHyperlink. Следующий фрагмент кода показывает шаги для выполнения этого требования.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create Text Fragment instance
        var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
        // Create local hyperlink instance
        var link = new Aspose.Pdf.LocalHyperlink();
        // Set target page for link instance
        link.TargetPageNumber = 7;
        // Set TextFragment hyperlink
        text.Hyperlink = link;
        // Add text to paragraphs collection of Page
        page.Paragraphs.Add(text);
        // Create new TextFragment instance
        text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
        // TextFragment should be added over new page
        text.IsInNewPage = true;
        // Create another local hyperlink instance
        link = new Aspose.Pdf.LocalHyperlink();
        // Set Target page for second hyperlink
        link.TargetPageNumber = 1;
        // Set link for second TextFragment
        text.Hyperlink = link;
        // Add text to paragraphs collection of page object
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    // Add page
    var page = document.Pages.Add();
    // Create Text Fragment instance
    var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
    // Create local hyperlink instance
    var link = new Aspose.Pdf.LocalHyperlink();
    // Set target page for link instance
    link.TargetPageNumber = 7;
    // Set TextFragment hyperlink
    text.Hyperlink = link;
    // Add text to paragraphs collection of Page
    page.Paragraphs.Add(text);
    // Create new TextFragment instance
    text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
    // TextFragment should be added over new page
    text.IsInNewPage = true;
    // Create another local hyperlink instance
    link = new Aspose.Pdf.LocalHyperlink();
    // Set Target page for second hyperlink
    link.TargetPageNumber = 1;
    // Set link for second TextFragment
    text.Hyperlink = link;
    // Add text to paragraphs collection of page object
    page.Paragraphs.Add(text);

    // Save PDF document
    document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Получение назначения гиперссылки (URL) в PDF

Ссылки представлены в виде аннотаций в PDF-файле, и их можно добавлять, обновлять или удалять. Aspose.PDF for .NET также поддерживает получение назначения (URL) гиперссылки в PDF-файле.

Чтобы получить URL ссылки:

1. Создайте объект [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).
1. Получите [Page](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page), из которой нужно извлечь ссылки.
1. Используйте класс [AnnotationSelector](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/annotationselector) для извлечения всех объектов [LinkAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/linkannotation) с указанной страницы.
1. Передайте объект [AnnotationSelector](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/annotationselector) в метод Accept объекта [Page](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page).
1. Получите все выбранные аннотации ссылок в объект IList, используя свойство Selected объекта [AnnotationSelector](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/annotationselector).
1. Наконец, извлеките действие LinkAnnotation как GoToURIAction.

Следующий фрагмент кода показывает, как получить назначения гиперссылок (URL) из PDF-файла.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Traverse through all the page of PDF
        foreach (var page in document.Pages)
        {
            // Get the link annotations from particular page
            var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

            page.Accept(selector);

            // Create list holding all the links
            var list = selector.Selected;

            // Iterate through individual item inside list
            foreach (var a in list)
            {
                // Print the destination URL
                Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Traverse through all the page of PDF
    foreach (var page in document.Pages)
    {
        // Get the link annotations from particular page
        var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

        page.Accept(selector);

        // Create list holding all the links
        var list = selector.Selected;

        // Iterate through individual item inside list
        foreach (var a in list)
        {
            // Print the destination URL
            Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Получение текста гиперссылки

Гиперссылка состоит из двух частей: текста, который отображается в документе, и URL назначения. В некоторых случаях нам нужен именно текст, а не URL.

Текст и аннотации/действия в PDF-файле представлены разными сущностями. Текст на странице — это просто набор слов и символов, а аннотации добавляют некоторую интерактивность, например, как в гиперссылке.

Чтобы найти содержимое URL, необходимо работать как с аннотацией, так и с текстом. Объект [Annotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/annotation) сам по себе не содержит текст, а находится под текстом на странице. Таким образом, чтобы получить текст, аннотация предоставляет границы URL, а объект Text — содержимое URL. Пожалуйста, ознакомьтесь со следующим фрагментом кода.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through each page of PDF
        foreach (var page in document.Pages)
        {
            // Show link annotation
            ShowLinkAnnotations(page);
        }
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Iterate through each page of PDF
    foreach (var page in document.Pages)
    {
        // Show link annotation
        ShowLinkAnnotations(page);
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Удаление действия открытия документа из PDF-файла

[Как указать страницу PDF при просмотре документа](#how-to-specify-pdf-page-when-viewing-document) объяснил, как указать документу открываться на другой странице, а не на первой. При объединении нескольких документов, один или несколько из которых имеют установленное действие GoTo, вероятно, вы захотите удалить их. Например, при объединении двух документов, второй из которых имеет действие GoTo, перенаправляющее на вторую страницу, выходной документ откроется на второй странице второго документа, а не на первой странице объединенного документа. Чтобы избежать такого поведения, удалите команду открытия действия.

Чтобы удалить действие открытия:

1. Установите свойство [OpenAction](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/properties/openaction) объекта [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document) в null.
1. Сохраните обновленный PDF с помощью метода [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save) объекта Document.

Следующий фрагмент кода показывает, как удалить действие открытия документа из PDF-файла.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf"))
    {
        // Remove document open action
        document.OpenAction = null;

        // Save PDF document
        document.Save(dataDir + "RemoveOpenAction_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf");

    // Remove document open action
    document.OpenAction = null;

    // Save PDF document
    document.Save(dataDir + "RemoveOpenAction_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Как указать страницу PDF при просмотре документа {#how-to-specify-pdf-page-when-viewing-document}

При просмотре PDF-файлов в программе для просмотра PDF, такой как Adobe Reader, файлы обычно открываются на первой странице. Однако можно установить, чтобы файл открывался на другой странице.

Класс [XYZExplicitDestination](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/xyzexplicitdestination) позволяет указать страницу в PDF-файле, которую вы хотите открыть. При передаче значения объекта GoToAction в свойство OpenAction класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document) документ открывается на странице, указанной в объекте XYZExplicitDestination. Следующий фрагмент кода показывает, как указать страницу в качестве действия открытия документа.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf"))
    {
        // Get the instance of second page of document
        var page2 = document.Pages[2];
        // Create the variable to set the zoom factor of target page
        double zoom = 1;
        // Create GoToAction instance
        var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
        // Go to 2 page
        action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
        // Set the document open action
        document.OpenAction = action;
        // Save PDF document
        document.Save(dataDir + "Goto2page_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf");
    // Get the instance of second page of document
    var page2 = document.Pages[2];
    // Create the variable to set the zoom factor of target page
    double zoom = 1;
    // Create GoToAction instance
    var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
    // Go to 2 page
    action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
    // Set the document open action
    document.OpenAction = action;
    // Save PDF document
    document.Save(dataDir + "Goto2page_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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