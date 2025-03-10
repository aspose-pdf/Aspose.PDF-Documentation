---
title: Добавление действий Javascript в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/adding-javascript-actions/
description: Узнайте, как добавить действия JavaScript, такие как нажатия кнопок или отправка форм, в PDF в .NET с использованием Aspose.PDF.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Javascript actions PDF",
    "alternativeHeadline": "Enhance PDF with Interactive JavaScript Actions",
    "abstract": "Улучшите ваш PDF, интегрируя интерактивные действия Javascript с классом Aspose.PDF for .NET PdfContentEditor. Эта функция позволяет пользователям создавать динамические ссылки и выполнять действия определенных пунктов меню, обогащая опыт работы с документом настраиваемыми интерактивными элементами. Упростите ваш рабочий процесс, добавляя действия на основе событий, которые легко реагируют на взаимодействия пользователей.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "216",
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
    "url": "/net/adding-javascript-actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-javascript-actions/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

Класс [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor), представленный в пакете Aspose.Pdf.Facades, предоставляет гибкость для добавления действий Javascript в PDF файл. Вы можете создать ссылку с последовательными действиями, соответствующими выполнению пункта меню в просмотрщике PDF. Этот класс также предоставляет возможность создавать дополнительные действия для событий документа.

Прежде всего, объект рисуется в [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document), в нашем примере это [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle). И устанавливается действие [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) для прямоугольника. После этого вы можете сохранить ваш документ.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavascriptAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        // Create Javascript link
        var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

        var code = "app.alert('Welcome to Aspose!');";
        editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

        // Save PDF document
        editor.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavascriptAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");

    // Create Javascript link
    var rect = new System.Drawing.Rectangle(50, 750, 50, 50);

    var code = "app.alert('Welcome to Aspose!');";
    editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);

    // Save PDF document
    editor.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}