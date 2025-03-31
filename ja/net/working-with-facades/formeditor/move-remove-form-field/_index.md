---
title: フォームフィールドの移動と削除
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ja/net/move-remove-form-field/
description: PDF内のフォームフィールドを管理する方法を探ります。移動または削除する方法についてはAspose.PDF for .NETを使用します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move and Remove Form Field",
    "alternativeHeadline": "Move and Remove Fields in PDF Forms Efficiently",
    "abstract": "FormEditorクラスのフォームフィールドの移動と削除機能により、ユーザーは既存のPDFドキュメント内でフォームフィールドをシームレスに再配置および削除できます。MoveFieldおよびRemoveFieldメソッドを利用することで、ユーザーはフォームを効率的にカスタマイズし、使いやすさとドキュメント管理を向上させることができます。この機能により、ユーザーは広範な技術的専門知識を必要とせずにPDFレイアウトを最適化できます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "416",
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
    "url": "/net/move-remove-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-remove-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 既存のPDFファイル内のフォームフィールドを新しい場所に移動する

フォームフィールドを新しい場所に移動したい場合は、[FormEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor)クラスの[MoveField](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/movefield)メソッドを使用できます。このメソッドには、フィールド名とこのフィールドの新しい位置を提供するだけで済みます。また、[FormEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor)クラスの[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/save/index)メソッドを使用して、更新されたPDFファイルを保存する必要があります。以下のコードスニペットは、PDFファイル内でフォームフィールドを新しい場所に移動する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "MoveField.pdf");
        editor.MoveField("textbox1", 262.56f, 496.75f, 382.28f, 514.03f);
        // Save PDF document
        editor.Save(dataDir + "MoveField_out.pdf");
    }
}
```

## 既存のPDFファイルからフォームフィールドを削除する

既存のPDFファイルからフォームフィールドを削除するには、FormEditorクラスのRemoveFieldメソッドを使用できます。このメソッドは、フィールド名という1つの引数のみを取ります。FormEditorクラスのオブジェクトを作成し、特定のフィールドをPDFから削除するために[RemoveField](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/removefield)メソッドを呼び出し、その後、更新されたPDFファイルを保存するためにSaveメソッドを呼び出す必要があります。以下のコードスニペットは、既存のPDFファイルからフォームフィールドを削除する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RemoveField("textbox1");
        // Save PDF document
        editor.Save(dataDir + "RemoveField_out.pdf");
    }
}
```

## PDF内のフォームフィールドの名前を変更する

また、[FormEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor)クラスの[RenameField](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/renamefield)メソッドを使用してフィールドの名前を変更することもできます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenameFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RenameField("textbox1", "FirstName");
        // Save PDF document
        editor.Save(dataDir + "RenameField_out.pdf");
    }
}
```