---
title: Копирование внутренних и внешних полей
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ru/net/copy-inner-and-outer-field/
description: Этот раздел объясняет, как копировать внутренние и внешние поля с помощью Aspose.PDF Facades, используя класс FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Copy Inner and Outer Field",
    "alternativeHeadline": "Seamlessly Copy Inner and Outer Fields in PDF",
    "abstract": "Функциональность копирования внутренних и внешних полей в Aspose.PDF for .NET улучшает редактирование форм, позволяя пользователям дублировать поля в одном и том же PDF или переносить их из внешнего PDF файла. С помощью простых в использовании методов CopyInnerField и CopyOuterField, предоставляемых классом FormEditor, пользователи могут эффективно управлять полями форм, обеспечивая согласованность и экономя время на подготовку документов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "337",
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
    "url": "/net/copy-inner-and-outer-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/copy-inner-and-outer-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

[CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) метод позволяет вам копировать поле в том же файле, в тех же координатах, на указанной странице. Этот метод требует имя поля, которое вы хотите скопировать, новое имя поля и номер страницы, на которой поле должно быть скопировано. [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) класс предоставляет этот метод. Следующий фрагмент кода показывает, как скопировать поле в том же месте в том же файле.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyInnerField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor object
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Form-01.pdf"))
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the field "Last Name" from the first page to "Last Name 2" on the second page
            formEditor.CopyInnerField("Last Name", "Last Name 2", 2);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
        }
    }
}
```

## Копирование внешнего поля в существующем PDF файле

[CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) метод позволяет вам копировать поле формы из внешнего PDF файла и затем добавлять его в входной PDF файл в том же месте и на указанном номере страницы. Этот метод требует PDF файл, из которого поле должно быть скопировано, имя поля и номер страницы, на которой поле должно быть скопировано. Этот метод предоставляется классом [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Следующий фрагмент кода показывает, как скопировать поле из внешнего PDF файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyOuterField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor 
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Create empty document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the outer field "First Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "First Name", 1);

            // Copy the outer field "Last Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "Last Name", 1);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-02-mod.pdf");
        }
    }
}
```