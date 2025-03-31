---
title: テキストボックスフィールドでのテキストの均等配置
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/justify-text-in-a-textbox-field/
description: この記事では、Formクラスを使用してテキストボックスフィールドでテキストを均等配置する方法を示します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Justify Text in a Textbox Field",
    "alternativeHeadline": "Justify Text in PDF Textbox Fields Effortlessly",
    "abstract": "この機能により、ユーザーはAspose.Pdf.Facades名前空間のFormEditorクラスを使用してPDFドキュメント内のテキストボックスフィールド内でテキストを均等配置できます。AlignJustifiedオプションを利用することで、ユーザーは機能性を維持しながら視覚的に魅力的なテキストの配置を実現できます。ただし、アクティブな入力中は均等配置はサポートされていません。これにより、PDFファイル内のフォームデータのプレゼンテーションが向上します。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

この記事では、PDFファイルのテキストボックスフィールドでテキストを均等配置する方法を示します。

{{% /alert %}}

## 実装の詳細

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor)クラスは、[Aspose.Pdf.Facades名前空間](https://reference.aspose.com/pdf/net/aspose.pdf.facades)でPDFフォームフィールドを装飾する機能を提供します。テキストボックスフィールド内のテキストを均等配置する必要がある場合は、[FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade)列挙型の[AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified)値を使用し、[FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index)メソッドを呼び出すことで簡単に実現できます。以下の例では、まず[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form)クラスの[FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index)メソッドを使用してテキストボックスフィールドを入力します。その後、FormEditorクラスを使用してテキストボックスフィールド内のテキストを均等配置します。以下のコードスニペットは、テキストボックスフィールドでテキストを均等配置する方法を示しています。

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
PDFでは均等配置がサポートされていないため、テキストボックスフィールドにテキストを入力すると、テキストは左揃えになります。ただし、フィールドがアクティブでない場合、テキストは均等配置されます。