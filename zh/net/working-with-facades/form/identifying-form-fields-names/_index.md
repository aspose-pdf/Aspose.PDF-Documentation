---
title: 识别表单字段名称
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/identifying-form-fields-names/
description: Aspose.Pdf.Facades 允许您使用 Form 类识别表单字段名称。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Identifying form fields names",
    "alternativeHeadline": "Identify and Label PDF Form Fields Easily",
    "abstract": "Aspose.PDF for .NET 中的功能简化了识别 PDF 文档中表单字段名称的过程。通过利用 Form 类及其属性，用户可以轻松检索并显示字段名称及其对应的字段，从而简化 PDF 表单的填写和编辑。此功能通过确保准确的字段操作来增强用户体验，特别是在处理使用外部工具（如 Adobe Designer）创建的表单时。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "511",
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
    "url": "/net/identifying-form-fields-names/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/identifying-form-fields-names/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

[Aspose.PDF for .NET](/pdf/zh/net/) 提供创建、编辑和填写已创建的 Pdf 表单的能力。[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 命名空间包含 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类，该类包含名为 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) 的函数，它接受两个参数，即字段名称和字段值。因此，为了填写表单字段，您必须知道确切的表单字段名称。

## 实现细节

我们经常遇到需要填写在某些工具（如 Adobe Designer）中创建的表单的场景，而我们不确定表单字段名称。因此，为了填写表单字段，我们首先需要读取所有 Pdf 表单字段的名称。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类提供名为 [FieldNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/properties/fieldnames) 的属性，该属性返回所有字段的名称，如果 PDF 不包含任何字段，则返回 null。然而，在使用此属性时，我们会获得 PDF 表单中所有字段的名称，我们可能不确定哪个名称对应于表单上的哪个字段。

作为解决此问题的方案，我们将使用每个字段的外观属性。Form 类有一个名为 [GetFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getfieldfacade) 的函数，该函数返回属性，包括位置、颜色、边框样式、字体、列表项等。为了保存这些值，我们需要使用 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade) 类，该类用于记录字段的视觉属性。一旦我们拥有这些属性，我们可以在每个字段下方添加一个文本字段，以显示字段名称。

{{% alert color="primary" %}}
此时，出现一个问题：“我们将如何确定添加文本字段的位置？”
{{% /alert %}}

{{% alert color="primary" %}}
解决此问题的方法是 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormFieldFacade) 类中的 Box 属性，该属性保存字段的位置。我们需要将这些值保存到一个矩形类型的数组中，并使用这些值来确定添加新文本字段的位置。
{{% /alert %}}

在 [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 命名空间中，我们有一个名为 [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) 的类，该类提供操作 PDF 表单的能力。打开一个 pdf 表单；在每个现有表单字段下方添加一个文本字段，并使用新名称保存 Pdf 表单。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyFormFieldsNames()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // First a input pdf file should be assigned
    var form = new Aspose.Pdf.Facades.Form(dataDir + "FilledForm.pdf");
    // Get all field names
    var allfields = form.FieldNames;
    // Create an array which will hold the location coordinates of Form fields
    var box = new System.Drawing.Rectangle[allfields.Length];
    for (int i = 0; i < allfields.Length; i++)
    {
        // Get the appearance attributes of each field, consequtively
        var facade = form.GetFieldFacade(allfields[i]);
        // Box in FormFieldFacade class holds field's location
        box[i] = facade.Box;
    }
    // Save PDF document
    form.Save(dataDir + "IdentifyFormFields_1_out.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FilledForm - 2.pdf"))
    {
        // Now we need to add a textfield just upon the original one
        using (var editor = new Aspose.Pdf.Facades.FormEditor(document))
        {
            for (int i = 0; i < allfields.Length; i++)
            {
                // Add text field beneath every existing form field
                editor.AddField(Aspose.Pdf.Facades.FieldType.Text, 
                "TextField" + i, allfields[i], 1, 
                box[i].Left, box[i].Top, box[i].Left + 50, box[i].Top + 10);
            }
            // Save PDF document
            editor.Save(dataDir + "IdentifyFormFields_out.pdf");
        }
    }
}
```