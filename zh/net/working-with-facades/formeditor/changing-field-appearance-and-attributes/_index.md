---
title: 字段外观和属性
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/changing-field-appearance-and-attributes/
description: 本节解释了如何使用 FormEditor 类更改字段外观和属性。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Field appearance and attributes",
    "alternativeHeadline": "Enhance Form Fields with Custom Appearance and Behavior",
    "abstract": "Aspose.Pdf.Facades 命名空间中的 FormEditor 类引入的功能使用户能够自定义 PDF 中表单字段的外观和属性。通过利用 SetFieldAppearance 和 SetFieldAttributes 等方法，开发人员可以轻松修改视觉元素和行为，包括字段限制，以增强用户交互和数据输入效率。此功能在设计针对特定应用需求的表单字段时提供了更大的灵活性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/changing-field-appearance-and-attributes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-field-appearance-and-attributes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

[FormEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/FormEditor) 类属于 [Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades)，允许您不仅更改表单字段的外观和感觉，还可以更改字段的行为。在本文中，我们将看到如何使用 FormEditor 类更改字段外观、字段属性和字段限制。

{{% /alert %}}

## 实现细节

[SetFieldAppearance](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) 方法用于更改表单字段的外观。它接受 AnnotationFlag 作为参数。AnnotationFlag 是一个枚举，具有不同的成员，如 Hidden 或 NoRotate 等。

[SetFieldAttributes](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) 方法用于更改表单字段的属性。传递给此方法的参数是 PropertyFlag 枚举，其中包含 ReadOnly 或 Required 等成员。

[FormEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/FormEditor) 类还提供了一个方法来设置字段限制。它告诉字段可以填充多少个字符。下面的代码片段展示了如何使用这些方法。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddFieldAndSetAttributes()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var doc = new Aspose.Pdf.Document(dataDir + "FilledForm.pdf"))
     {
         // Create an instance of FormEditor to manipulate form fields
         using (var formEditor = new Aspose.Pdf.Facades.FormEditor(doc))
         {
             // Add a new text field to the form on page 1 at the specified coordinates and size
             formEditor.AddField(Aspose.Pdf.Facades.FieldType.Text, "text1", 1, 200, 550, 300, 575);

             // Set the field attribute to make the text field required (user must fill it)
             formEditor.SetFieldAttribute("text1", Aspose.Pdf.Facades.PropertyFlag.Required);

             // Set a character limit for the field (maximum 20 characters)
             formEditor.SetFieldLimit("text1", 20);

             // Save PDF document
             formEditor.Save(dataDir + "ChangingFieldAppearance_out.pdf");
         }
     }
 }
```