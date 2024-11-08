---
title: XFDF形式で注釈のインポートとエクスポート
linktitle: XFDF形式で注釈のインポートとエクスポート
type: docs
weight: 40
url: /ja/net/import-export-xfdf/
description: C#およびAspose.PDF for .NETライブラリを使用して、XFDF形式で注釈をインポートおよびエクスポートできます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "XFDF形式で注釈のインポートとエクスポート",
    "alternativeHeadline": "XFDFファイルへの注釈データのインポートとエクスポート方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, import export to XFDF",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2022-02-04",
    "description": "C#およびAspose.PDF for .NETライブラリを使用して、XFDF形式で注釈をインポートおよびエクスポートできます。"
}
</script>

{{% alert color="primary" %}}

XFDFはXML Forms Data Formatの略です。これはXMLベースのファイル形式です。このファイル形式は、PDFフォームに含まれるフォームデータまたは注釈を表すために使用されます。XFDFはさまざまな目的で使用できますが、この場合、他のコンピューターやサーバー等へのフォームデータや注釈の送受信、またはフォームデータや注釈のアーカイブのために使用できます。この記事では、Aspose.Pdf.Facadesがこのコンセプトをどのように考慮しているか、そしてXFDFファイルへの注釈データのインポートとエクスポートをどのように行うかを見ていきます。

{{% /alert %}}

**Aspose.PDF for .NET**はPDFドキュメントの編集に関しては機能豊富なコンポーネントです。XFDFはPDFフォーム操作の重要な側面であることを考慮して、Aspose.PDF for .NETのAspose.Pdf.Facades名前空間はこれを非常によく考慮しており、XFDFファイルへの注釈データのインポートとエクスポートの方法を提供しています。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) クラスには、XFDFファイルへの注釈のインポートとエクスポートを行うための2つのメソッドが含まれています。
[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) クラスには、XFDFファイルへの注釈のインポートとエクスポートを操作するための2つのメソッドが含まれています。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/) ライブラリとも動作します。

次のコードスニペットは、XFDFファイルへの注釈のエクスポート方法を示しています：

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Facades;
using System.IO;


namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleAnnotationImportExport
    {
        // ドキュメントディレクトリへのパス。
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        /// <summary>
        /// XFDFファイルからの注釈のインポート
        /// アドビアクロバットによって作成されたXMLフォームデータフォーマット(XFDF)ファイル;
        /// ページフォーム要素とその値の説明を格納し、テキストフィールドの名前や値などが含まれます。
        /// PdfAnnotationEditorクラスのImportAnnotationsFromXfdfメソッドを使用して、XFDFファイルからPDFへ注釈データをインポートできます。
        /// </summary>       
   
        public static void ExportAnnotationXFDF()
        {
            // PdfAnnotationEditorオブジェクトを作成
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

            // PDFドキュメントをアノテーションエディタにバインド
            AnnotationEditor.BindPdf(Path.Combine(_dataDir, "AnnotationDemo1.pdf"));
           
            // 注釈をエクスポート
            var fileStream = File.OpenWrite(Path.Combine(_dataDir, "exportannotations.xfdf"));
            var annotType = new AnnotationType[] { AnnotationType.Line, AnnotationType.Square };
            AnnotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
            fileStream.Close();
        }
        //...
    }
}
```
次のコードスニペットは、XFDFファイルにアノテーションをインポートする方法を説明しています：

```csharp
public static void ImportAnnotationXFDF()
{
    // PdfAnnotationEditor オブジェクトを作成する
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // 新しいPDFドキュメントを作成する
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // アノテーションをインポートする
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // 出力PDFを保存する
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## アノテーションのエクスポート/インポートを一度に行う別の方法

以下のコードでは、ImportAnnotationsメソッドを使用して、別のPDFドキュメントから直接アノテーションをインポートします。

```csharp
        /// <summary>
        /// ImportAnnotationsメソッドは、別のPDFドキュメントから直接アノテーションをインポートすることを可能にします
        /// </summary>

        public static void ImportAnnotationFromPDF()
        {
            // PdfAnnotationEditor オブジェクトを作成する
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
            // 新しいPDFドキュメントを作成する
            var document = new Document();
            document.Pages.Add();
            AnnotationEditor.BindPdf(document);
            var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
            if (!File.Exists(exportFileName))
                ExportAnnotationXFDF();

            // アノテーションエディターは複数のPDFドキュメントからのアノテーションのインポートを許可しますが、
            // この例では1つだけを使用します。
            AnnotationEditor.ImportAnnotations(new[] { Path.Combine(_dataDir, "AnnotationDemo1.pdf") });

            // 出力PDFを保存する
            document.Save(Path.Combine(_dataDir, "AnnotationDemo3.pdf"));
        }
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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
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

