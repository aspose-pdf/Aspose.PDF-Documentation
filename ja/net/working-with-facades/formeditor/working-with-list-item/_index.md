---
title: リストアイテムの操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/working-with-list-item/
description: このセクションでは、FormEditorクラスを使用してAspose.PDF Facadesでリストアイテムを操作する方法について説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with List Item",
    "alternativeHeadline": "Enhance PDF Forms with List Item Management",
    "abstract": "Aspose.PDF for .NETのリストアイテム機能を使用してPDFフォームを強化します。FormEditorクラスを使用してListBoxフィールドからアイテムを簡単に追加または削除でき、動的でカスタマイズ可能なユーザー入力を可能にします。この機能はフォーム管理を効率化し、ニーズに合わせてコンテンツを調整するのを簡単にします。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "325",
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
    "url": "/net/working-with-list-item/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-list-item/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 既存のPDFファイルにリストアイテムを追加

[AddListItem](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/addlistitem)メソッドを使用すると、[ListBox](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/listboxfield)フィールドにアイテムを追加できます。最初の引数はフィールド名で、2番目の引数はフィールドアイテムです。単一のフィールドアイテムを渡すことも、アイテムのリストを含む文字列の配列を渡すこともできます。このメソッドは[FormEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor)クラスによって提供されています。以下のコードスニペットは、PDFファイルにリストアイテムを追加する方法を示しています。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a ListBox field for selecting country, placed at the specified coordinates on page 1
         formEditor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f,
             514.03f);

         // Add list items to the 'Country' ListBox field
         formEditor.AddListItem("Country", "USA");
         formEditor.AddListItem("Country", "Canada");
         formEditor.AddListItem("Country", "France");
         formEditor.AddListItem("Country", "Spain");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## 既存のPDFファイルからリストアイテムを削除

[DelListItem](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/dellistitem)メソッドを使用すると、[ListBox](https://reference.aspose.com/pdf/ja/net/aspose.pdf.forms/listboxfield)から特定のアイテムを削除できます。最初のパラメータはフィールド名で、2番目のパラメータはリストから削除したいアイテムです。このメソッドは[FormEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor)クラスによって提供されています。以下のコードスニペットは、PDFファイルからリストアイテムを削除する方法を示しています。

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void DelListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-04.pdf");

         // Delete the list item "France" from the 'Country' ListBox field
         formEditor.DelListItem("Country", "France");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-04-mod.pdf");
     }
 }
```