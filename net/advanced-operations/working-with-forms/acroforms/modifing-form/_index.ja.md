---
title: Modifing AcroForm
linktitle: Modifing AcroForm
type: docs
weight: 40
url: /net/modifing-form/
description: Aspose.PDF for .NET ライブラリを使用してPDFファイル内のフォームを修正します。既存のフォームにフィールドを追加または削除し、フィールドリミットの取得と設定などができます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modifing AcroForm",
    "alternativeHeadline": "How to Modifing AcroForm",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, modifing acroform",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET ライブラリを使用してPDFファイル内のフォームを修正します。既存のフォームにフィールドを追加または削除し、フィールドリミットの取得と設定などができます。"
}
</script>
以下のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

## フィールド制限の取得または設定

FormEditorクラスのSetFieldLimit(field, limit)メソッドを使用すると、フィールドに入力できる最大文字数であるフィールド制限を設定できます。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 制限を持つフィールドを追加
FormEditor form = new FormEditor();

form.BindPdf(dataDir + "input.pdf");
form.SetFieldLimit("textbox1", 15);
dataDir = dataDir + "SetFieldLimit_out.pdf";
form.Save(dataDir);
```

同様に、Aspose.PDFにはDOMアプローチを使用してフィールド制限を取得するメソッドがあります。次のコードスニペットはその手順を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// DOMを使用して最大フィールド制限を取得
Document doc = new Document(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + (doc.Form["textbox1"] as TextBoxField).MaxLen);
```
*Aspose.PDF.Facades* 名前空間を使用して同じ値を取得することもできます。以下のコードスニペットを使用します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Facadesを使用して最大フィールド制限を取得
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "FieldLimit.pdf");
Console.WriteLine("制限: " + form.GetFieldLimit("textbox1"));
```

## フォームフィールドのカスタムフォントを設定する

Adobe PDFファイルのフォームフィールドは、特定のデフォルトフォントを使用するように設定できます。
Adobe PDFファイルのフォームフィールドは、特定のデフォルトフォントを使用するように設定できます。

次のコードスニペットは、PDFフォームフィールドのデフォルトフォントを設定する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "FormFieldFont14.pdf");

// ドキュメントから特定のフォームフィールドを取得
Aspose.Pdf.Forms.Field field = pdfDocument.Form["textbox1"] as Aspose.Pdf.Forms.Field;

// フォントオブジェクトを作成
Aspose.Pdf.Text.Font font = FontRepository.FindFont("ComicSansMS");

// フォームフィールドのフォント情報を設定
// Field.DefaultAppearance = new Aspose.Pdf.Forms.in.DefaultAppearance(font, 10, System.Drawing.Color.Black);

dataDir = dataDir + "FormFieldFont14_out.pdf";
// 更新されたドキュメントを保存
pdfDocument.Save(dataDir);
```

## 既存のフォームにフィールドを追加/削除

すべてのフォームフィールドは、DocumentオブジェクトのFormコレクションに含まれています。
すべてのフォームフィールドは、DocumentオブジェクトのFormコレクションに含まれています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "DeleteFormField.pdf");

// 名前で特定のフィールドを削除
pdfDocument.Form.Delete("textbox1");
dataDir = dataDir + "DeleteFormField_out.pdf";
// 変更されたドキュメントを保存
pdfDocument.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

