---
title: 添加 PDF 表单字段
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/add-form-fields/
description: 本主题解释了如何使用 FormEditor 类与 Aspose.PDF Facades 一起处理表单字段。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Form Fields",
    "alternativeHeadline": "Effortlessly Enhance PDFs with Custom Form Fields",
    "abstract": "通过使用 Aspose.PDF for .NET 中的 FormEditor 类添加表单字段，为您的 PDF 文档增强动态交互性。此功能允许您轻松地将文本字段、带有 URL 的提交按钮和 JavaScript 功能添加到按钮中，从而简化用户输入和数据提交。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "548",
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
    "url": "/net/add-form-fields/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-form-fields/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 在现有 PDF 文件中添加表单字段

为了在现有 PDF 文件中添加表单字段，您需要使用 [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) 方法的 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类。此方法要求您指定要添加的字段类型，以及字段的名称和位置。您需要创建一个 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类的对象，使用 [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) 方法在 PDF 中添加新字段。此外，您可以使用 [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) 方法指定字段中的字符数限制，最后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) 方法保存更新后的 PDF 文件。以下代码片段演示了如何在现有 PDF 文件中添加表单字段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a text field named "Country" to the first page of the PDF
        // Specify the coordinates of the field (left, bottom, right, top)
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);

        // Set a character limit for the "Country" field to 20 characters
        editor.SetFieldLimit("Country", 20);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```

## 在现有 PDF 文件中添加提交按钮 URL

[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) 方法允许您在 PDF 文件中设置提交按钮的 URL。这是提交按钮被点击时数据发布的 URL。在我们的示例代码中，我们指定 URL、字段名称、要添加的页面编号以及按钮放置坐标。[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) 方法需要提交按钮字段的名称和 URL。此方法由 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 类提供。以下代码片段演示了如何设置提交按钮 URL。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddSubmitBtn()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var editor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a submit button named "Submit" to the first page of the PDF
         // Specify the button text ("Submit"), the URL to which the form data will be submitted,
         // and the coordinates of the button (left, bottom, right, top)
         editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);

         // Save PDF document
         editor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## 为按钮添加 JavaScript

[AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) 方法允许您在 PDF 文件中的按钮上添加 JavaScript。此方法需要按钮的名称和 JavaScript。此方法由 [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) 类提供。以下代码片段演示了如何为按钮设置 JavaScript。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFieldScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Add a JavaScript action to the field named "Last Name"
        // The script displays an alert box with the message "Only one last name"
        editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-mod.pdf");
    }
}
```