---
title: Extract AcroForm - PDFからフォームデータを抽出するC#
linktitle: Extract AcroForm
type: docs
weight: 30
url: /ja/net/extract-form/
keywords: extract form data from pdf c#
description: Aspose.PDF for .NETライブラリを使用して、PDFドキュメントからフォームを抽出します。PDFファイルの個々のフィールドから値を取得します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm",
    "alternativeHeadline": "PDFからAcroFormを抽出する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, extract acroform",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETライブラリを使用して、PDFドキュメントからフォームを抽出します。PDFファイルの個々のフィールドから値を取得します。"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリとも連携します。

## フォームからデータを抽出する

### PDFドキュメントのすべてのフィールドから値を取得する

PDFドキュメントのすべてのフィールドから値を取得するには、すべてのフォームフィールドをナビゲートし、Valueプロパティを使用して値を取得する必要があります。フォームコレクションから各フィールドを取得し、Fieldと呼ばれる基本フィールドタイプにアクセスして、そのValueプロパティを利用します。

次のC# コードスニペットは、PDFドキュメントのすべてのフィールドの値を取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// すべてのフィールドから値を取得する
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("フィールド名 : {0} ", formField.PartialName);
    Console.WriteLine("値 : {0} ", formField.Value);
}
```
### PDFドキュメントの個々のフィールドから値を取得する

フォームフィールドのValueプロパティを使用して、特定のフィールドの値を取得できます。値を取得するには、DocumentオブジェクトのFormコレクションからフォームフィールドを取得します。このC#例では、[TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) を選択し、Valueプロパティを使用してその値を取得します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// フィールドを取得
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// フィールド値を取得
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

送信ボタンのURLを取得するには、次のコード行を使用します。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// ドキュメントを開く
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated as SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### PDFファイルの特定の領域からフォームフィールドを取得する

時には、ドキュメント内のフォームフィールドがどこにあるかは分かっていても、その名前が分からないことがあります。例えば、印刷されたフォームの図面だけが手がかりの場合などです。Aspose.PDF for .NETを使用すれば、問題ありません。PDFファイルの指定された領域にどのフィールドがあるかを調べることができます。PDFファイルの特定の領域からフォームフィールドを取得するには：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)オブジェクトを使用してPDFファイルを開きます。
1. ドキュメントのFormsコレクションからフォームを取得します。
1. 矩形領域を指定し、FormオブジェクトのGetFieldsInRectメソッドに渡します。Fieldsコレクションが返されます。
1. これを使用してフィールドを操作します。

以下のC#コードスニペットは、PDFファイルの特定の矩形領域内のフォームフィールドを取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// PDFファイルを開く
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// そのエリアのフィールドを取得するための矩形オブジェクトを作成
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// PDFフォームを取得
Aspose.Pdf.Forms.Form form = doc.Form;

// 矩形エリア内のフィールドを取得
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// フィールド名と値を表示
foreach (Field field in fields)
{
    // すべての配置について画像配置プロパティを表示
    Console.Out.WriteLine("フィールド名: " + field.FullName + "-" + "フィールド値: " + field.Value);
}
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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
                "areaServed": "AU",
                "availableLanguage": "英語"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET用PDF操作ライブラリ",
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
```

