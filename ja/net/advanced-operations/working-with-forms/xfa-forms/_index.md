---
title: XFAフォームの操作
linktitle: XFAフォーム
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/xfa-forms/
description: Aspose.PDF for .NET APIを使用すると、PDFドキュメント内のXFAおよびXFA Acroformフィールドを操作できます。Aspose.Pdf.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with XFA Forms",
    "alternativeHeadline": "Enhance PDF handling with XFA form support",
    "abstract": "Aspose.PDF for .NETは、XFAフォームを操作するための高度な機能を提供し、開発者がPDFドキュメント内のXFA Acroformフィールドを入力、変換、管理できるようにします。この機能は動的フォームの操作を簡素化し、フィールド値やプロパティへのシームレスなアクセスを提供し、XFAから標準AcroFormsへの効率的な変換を実現します。この堅牢なソリューションで複雑なフォーム構造を処理するPDF処理ワークフローを強化してください。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "XFA Forms, Aspose.PDF for .NET, fill XFA form, convert XFA to Acroform, get XFA field properties, dynamic forms, XML Forms Architecture, manipulate XFA fields, AcroForm fields, PDF document generation",
    "wordcount": "684",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET APIを使用すると、PDFドキュメント内のXFAおよびXFA Acroformフィールドを操作できます。Aspose.Pdf.Facades."
}
</script>

{{% alert color="primary" %}}

動的フォームは、XFA（XMLフォームアーキテクチャ）として知られるXML仕様に基づいています。また、動的XFAフォームを標準Acroformに変換することもできます。フォームに関する情報（PDFに関して）は非常に曖昧であり、フィールドが存在し、プロパティやJavaScriptイベントがあることを指定していますが、レンダリングについては指定していません。XFAフォームのオブジェクトは、ドキュメントを読み込む際に描画されます。

{{% /alert %}}

Formクラスは、静的AcroFormを扱う機能を提供し、FormクラスのGetFieldFacade(..)メソッドを使用して特定のフィールドインスタンスを取得できます。ただし、XFAフィールドにはForm.GetFieldFacade(..)メソッドを介してアクセスできません。代わりに、[Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa)を使用してフィールド値を取得/設定し、XFAフィールドテンプレートを操作します（フィールドプロパティを設定します）。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## XFAフィールドの入力

以下のコードスニペットは、XFAフォームのフィールドに入力する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillXFAFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FillXFAFields.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
}
```

## XFAからAcroformへの変換

{{% alert color="primary" %}}

オンラインで試す
Aspose.PDFの変換品質を確認し、次のリンクで結果をオンラインで表示できます: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

動的フォームは、XFA（XMLフォームアーキテクチャ）として知られるXML仕様に基づいています。フォームに関する情報（PDFに関して）は非常に曖昧であり、フィールドが存在し、プロパティやJavaScriptイベントがあることを指定していますが、レンダリングについては指定していません。

現在、PDFはデータとPDFフォームを統合するための2つの異なる方法をサポートしています：

- AcroForms（Acrobatフォームとも呼ばれ）、PDF 1.2形式仕様に導入され、含まれています。
- Adobe XMLフォームアーキテクチャ（XFA）フォーム、PDF 1.5形式仕様にオプション機能として導入されました（XFA仕様はPDF仕様に含まれておらず、参照のみです）。

XFAフォームのページを抽出または操作することはできません。なぜなら、フォームの内容は、XFAフォームを表示またはレンダリングしようとするアプリケーション内でランタイムに生成されるからです。Aspose.PDFには、開発者がXFAフォームを標準AcroFormsに変換できる機能があります。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDynamicXFAToAcroForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load dynamic XFA form
    using (var document = new Aspose.Pdf.Document(dataDir + "DynamicXFAToAcroForm.pdf"))
    {
        // Set the form fields type as standard AcroForm
        document.Form.Type = Aspose.Pdf.Forms.FormType.Standard;

        // Save PDF document
        document.Save(dataDir + "StandardAcroForm_out.pdf");
    }
}
```

## XFAフィールドプロパティの取得

フィールドプロパティにアクセスするには、まずDocument.Form.XFA.Templateを使用してフィールドテンプレートにアクセスします。以下のコードスニペットは、XFAフォームフィールドのX座標とY座標を取得する手順を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXFAProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXFAProperties.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Get field position
        if (names.Length > 0)
        {
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
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