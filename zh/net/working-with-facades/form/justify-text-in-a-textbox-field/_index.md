---
title: 在文本框字段中对齐文本
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/justify-text-in-a-textbox-field/
description: 本文展示了如何使用 Form 类在文本框字段中对齐文本。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Justify Text in a Textbox Field",
    "alternativeHeadline": "Justify Text in PDF Textbox Fields Effortlessly",
    "abstract": "该功能允许用户使用 Aspose.Pdf.Facades 命名空间中的 FormEditor 类在 PDF 文档的文本框字段中对齐文本。通过利用 AlignJustified 选项，用户可以实现视觉上吸引人的文本对齐，同时保持功能性，尽管在输入时不支持对齐。这样可以增强 PDF 文件中表单数据的呈现。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "283",
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
    "url": "/net/justify-text-in-a-textbox-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/justify-text-in-a-textbox-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发者的信息。"
}
</script>

{{% alert color="primary" %}}

在本文中，我们将向您展示如何在 PDF 文件的文本框字段中对齐文本。

{{% /alert %}}

## 实现细节

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) 类在 [Aspose.Pdf.Facades 命名空间](https://reference.aspose.com/pdf/net/aspose.pdf.facades) 中提供了装饰 PDF 表单字段的能力。现在，如果您的需求是在文本框字段中对齐文本，您可以轻松地使用 [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) 枚举的 [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) 值，并调用 [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index) 方法。在下面的示例中，我们将首先使用 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类的 [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) 方法填充一个文本框字段。之后，我们将使用 FormEditor 类在文本框字段中对齐文本。以下代码片段向您展示了如何在文本框字段中对齐文本。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void JustifyTextInTextboxField()
{
    // The path to the documents directory 
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Open PDF document
    using (var source = File.Open(dataDir + "JustifyText.pdf", FileMode.Open))
    {
        using (var ms = new MemoryStream())
        {
            // Create Form Object
            var form = new Aspose.Pdf.Facades.Form();
            // Bind PDF document
            form.BindPdf(source);
            // Fill Text Field
            form.FillField("Text1", "Thank you for using Aspose");
            // Save PDF document in Memory Stream
            form.Save(ms);
            ms.Seek(0, SeekOrigin.Begin);

            using (var dest = new FileStream(dataDir + "JustifyText_out.pdf", FileMode.Create))
            {
                // Create formEditor Object
                using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
                {
                    // Open PDF from memory stream
                    formEditor.BindPdf(ms);
                    // Set Text Alignment as Justified
                    formEditor.Facade.Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignJustified;
                    // Decorate form field
                    formEditor.DecorateField();
                    // Save PDF document
                    formEditor.Save(dest);
                }
            }
        }
    }
}
```
请注意，PDF 不支持对齐，因此在您输入文本框字段中的文本时，文本将左对齐。但是，当字段不处于活动状态时，文本是对齐的。