---
title: 从 PDF 中删除表单 C#
linktitle: 删除表单
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /zh/net/remove-form/
description: 基于子类型/表单使用 Aspose.PDF for .NET 库删除文本。 从 PDF 中删除所有表单。
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete Forms from PDF in C#",
    "alternativeHeadline": "Effortless Removal of Forms from PDFs in C#",
    "abstract": "介绍使用 Aspose.PDF 库在 C# 中从 PDF 文档中删除表单的新功能。此功能简化了特定表单元素（例如子表单）或甚至从 PDF 文件中删除所有表单的过程，提高了开发人员的文档管理和自定义能力。通过精确的代码片段优化您的 PDF 编辑过程，以确保高效的文本片段删除和文档保存。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "delete forms, remove text, PDF C#, Aspose.PDF for .NET library, TextFragmentAbsorber, remove all forms",
    "wordcount": "378",
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
    "url": "/net/remove-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 基于子类型/表单删除文本

下一个代码片段使用包含 PDF 文件路径的输入变量创建一个新的 Document 对象。该示例访问文档第 2 页上呈现的表单，并检查具有某些属性的表单。如果找到类型为“打字机”和子类型为“表单”的表单，则使用 TextFragmentAbsorber 访问并删除该表单中的所有文本片段。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ClearTextInForm(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBox.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        foreach (var form in forms)
        {
            // Check if the form is of type "Typewriter" and subtype "Form"
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                // Create a TextFragmentAbsorber to find text fragments
                var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
                absorber.Visit(form);

                // Clear the text in each fragment
                foreach (var fragment in absorber.TextFragments)
                {
                    fragment.Text = "";
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }	
}
```

## 从 PDF 中删除类型为“打字机”和子类型为“表单”的表单

此代码片段在 PDF 文档的第一页上搜索意图（IT）为“打字机”和子类型（Subtype）为“表单”的表单。如果满足这两个条件，则从 PDF 中删除该表单。然后将修改后的文档保存到指定的输出文件。

Aspose.PDF 库提供两种方法来从 PDF 中删除此类表单：

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteSpecifiedForm(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        for (int i = forms.Count; i > 0; i--)
        {
            if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
            {
                forms.Delete(forms[i].Name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

方法 2：

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteSpecifiedForm(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
        foreach (var form in forms)
        {
            if (form.IT == "Typewriter" && form.Subtype == "Form")
            {
                var name = forms.GetFormName(form);
                forms.Delete(name);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

## 从 PDF 中删除所有表单

此代码从 PDF 文档的第一页删除所有表单元素，然后将修改后的文档保存到指定的输出路径。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveAllForms(string input, string output)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the forms from the first page
        var forms = document.Pages[1].Resources.Forms;

        // Clear all forms
        forms.Clear();

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```