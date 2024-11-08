---
title: XFAフォームの操作
linktitle: XFAフォーム
type: docs
weight: 20
url: /ja/net/xfa-forms/
description: Aspose.PDF for .NET APIを使用すると、PDFドキュメント内のXFAおよびXFAアクロフォームフィールドを操作できます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "XFAフォームの操作",
    "alternativeHeadline": "PDF内のXFAフォームの入力、変換、取得",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, fill xfa form, get xfa form, convert xfa form",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET APIを使用すると、PDFドキュメント内のXFAおよびXFAアクロフォームフィールドを操作できます。"
}
</script>

{{% alert color="primary" %}}

動的フォームは、XFA（「XML Forms Architecture」）として知られるXML仕様に基づいています。また、動的XFAフォームを標準のAcroformに変換することもできます。フォームに関する情報（PDFに関して言えば）は非常にあいまいです - フィールドが存在すること、プロパティとJavaScriptイベントがあることを指定しますが、レンダリングについては指定しません。XFAフォームのオブジェクトは、ドキュメントをロードする際に描画されます。

{{% /alert %}}

Formクラスは、静的なAcroFormを扱う機能を提供し、FormクラスのGetFieldFacade(..)メソッドを使用して特定のフィールドインスタンスを取得できます。しかし、XFAフィールドはForm.GetFieldFacade(..)メソッドを介してアクセスすることはできません。代わりに、[Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa)を使用してフィールド値を取得/設定し、XFAフィールドテンプレートを操作します（フィールドプロパティを設定します）。

以下のコードスニペットも[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリで動作します。

## XFAフィールドを埋める

以下のコードスニペットは、XFAフォームのフィールドを埋める方法を示しています。
次のコードスニペットは、XFAフォームのフィールドを埋める方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// XFAフォームをロード
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// XFAフォームフィールドの名前を取得
string[] names = doc.Form.XFA.FieldNames;

// フィールド値を設定
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// 更新されたドキュメントを保存
doc.Save(dataDir);
```

## XFAからAcroformへの変換

{{% alert color="primary" %}}

オンラインで試す
Aspose.PDFの変換品質を確認し、このリンクで結果をオンラインで表示できます: [products.aspose.app/pdf/xfa/](https://products.aspose.app/pdf/xfa/)

{{% /alert %}}

動的フォームは、"XML Forms Architecture" として知られるXML仕様に基づいています。
動的フォームは、「XML Forms Architecture」として知られるXML仕様に基づいています。

現在、PDFはデータとPDFフォームを統合するための2つの異なる方法をサポートしています：

- AcroForms（Acrobatフォームとしても知られています）、PDF 1.2形式の仕様で導入され、含まれています。
- Adobe XML Forms Architecture（XFA）フォームは、PDF 1.5形式の仕様でオプション機能として導入されました（XFA仕様はPDF仕様には含まれておらず、参照のみです。）

XFAフォームのページを抽出または操作することはできません。なぜなら、フォームの内容はランタイム（XFAフォームの表示中）にアプリケーション内で生成されるからです。Aspose.PDFには、開発者がXFAフォームを標準のAcroFormsに変換する機能があります。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET にアクセスしてください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// 動的XFAフォームを読み込む
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// フォームフィールドのタイプを標準AcroFormに設定する
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// 結果のPDFを保存する
document.Save(dataDir);
```

## XFAフィールドプロパティを取得する

フィールドプロパティにアクセスするには、まず Document.Form.XFA.Teamplate を使用してフィールドテンプレートにアクセスします。次のコードスニペットは、XFAフォームフィールドのX座標とY座標を取得する手順を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// XFAフォームをロード
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// フィールド値を設定
doc.Form.XFA[names[0]] = "Field 0";
doc.Form.XFA[names[1]] = "Field 1";

// フィールド位置を取得
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// フィールド位置を取得
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// 更新されたドキュメントを保存
doc.Save(dataDir);
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

