---
title: PDFフォームフィールドの追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/add-form-fields/
description: このトピックでは、FormEditorクラスを使用してAspose.PDFファサードでフォームフィールドを操作する方法について説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Form Fields",
    "alternativeHeadline": "Effortlessly Enhance PDFs with Custom Form Fields",
    "abstract": "Aspose.PDF for .NETのFormEditorクラスを使用してフォームフィールドを追加することで、動的なインタラクティブ性を持つPDFドキュメントを強化します。この機能により、テキストフィールド、URLを持つ送信ボタン、ボタンを押すためのJavaScript機能を簡単に組み込むことができ、PDF内のユーザー入力とデータ送信を効率化します。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 既存のPDFファイルにフォームフィールドを追加

既存のPDFファイルにフォームフィールドを追加するには、[FormEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor)クラスの[AddField](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/addfield/index)メソッドを使用する必要があります。このメソッドでは、追加したいフィールドのタイプとフィールドの名前および位置を指定する必要があります。[FormEditor](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor)クラスのオブジェクトを作成し、[AddField](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/addfield/index)メソッドを使用してPDFに新しいフィールドを追加します。また、[SetFieldLimit](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/setfieldlimit)を使用してフィールド内の文字数の制限を指定し、最後に[Save](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/form/methods/save/index)メソッドを使用して更新されたPDFファイルを保存します。以下のコードスニペットは、既存のPDFファイルにフォームフィールドを追加する方法を示しています。

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

## 既存のPDFファイルに送信ボタンのURLを追加

[AddSubmitBtn](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn)メソッドを使用すると、PDFファイル内の送信ボタンのURLを設定できます。これは、送信ボタンがクリックされたときにデータが送信されるURLです。例のコードでは、URL、フィールドの名前、追加したいページ番号、およびボタンの配置座標を指定します。[AddSubmitBtn](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn)メソッドには、送信ボタンフィールドの名前とURLが必要です。このメソッドは[FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor)クラスによって提供されます。以下のコードスニペットは、送信ボタンのURLを設定する方法を示しています。

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

## プッシュボタン用のJavaScriptを追加

[AddFieldScript](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/formeditor/methods/addfieldscript)メソッドを使用すると、PDFファイル内のプッシュボタンにJavaScriptを追加できます。このメソッドでは、プッシュボタンの名前とJavaScriptが必要です。このメソッドは[FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor)クラスによって提供されます。以下のコードスニペットは、プッシュボタンにJavaScriptを設定する方法を示しています。

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