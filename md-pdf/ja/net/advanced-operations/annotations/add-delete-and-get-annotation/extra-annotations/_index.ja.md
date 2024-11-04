---
title: C#を使用した追加の注釈
linktitle: 追加の注釈
type: docs
weight: 60
url: /net/extra-annotations/
description: このセクションでは、PDFドキュメントから追加の種類の注釈を追加、取得、削除する方法について説明します。
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用した追加の注釈",
    "alternativeHeadline": "PDFに追加注釈を追加する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, リンク注釈, キャレット注釈",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、PDFドキュメントから追加の種類の注釈を追加、取得、削除する方法について説明します。"
}
</script>

## 既存のPDFファイルにキャレット注釈を追加する方法

キャレット注釈は、テキスト編集を示す記号です。キャレット注釈はマークアップ注釈でもあるため、CaretクラスはMarkupクラスから派生し、キャレット注釈のプロパティを取得または設定し、キャレット注釈の外観の流れをリセットする機能も提供します。

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも動作します。

キャレット注釈を作成する手順：

1. PDFファイルを読み込む - 新しい [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)。
1. 新しい [Caret Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) を作成し、キャレットパラメーター（新しいRectangle、タイトル、サブジェクト、フラグ、色、幅、StartingStyleおよびEndingStyle）を設定します。この注釈はテキストの挿入を示すために使用されます。
1. 新しい[StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation)を作成し、パラメーターを設定します（新しいRectangle、タイトル、色、新しいQuadPointsと新しいポイント、Subject、InReplyTo、ReplyType）。
1. その後、ページにアノテーションを追加できます。

以下のコードスニペットは、PDFファイルにCaret Annotationを追加する方法を示しています：

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // ドキュメントディレクトリへのパス。
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCaretAnnotation()
        {
            // PDFファイルを読み込む
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // このアノテーションはテキストの挿入を示すために使用されます
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "Aspose User",
                Subject = "Inserted text 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // このアノテーションはテキストの置換を示すために使用されます
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "Inserted text 2",
                Title = "Aspose User",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "Cross-out",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
```
### キャレット注釈を取得する

次のコードスニペットを使用して、PDFドキュメントでキャレット注釈を取得してください。

```csharp
public static void GetCaretAnnotation()
{
    // PDFファイルをロードする
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();
    foreach (var ca in caretAnnotations)
    {
        Console.WriteLine($"{ca.Rect}");
    }
}
```

### キャレット注釈を削除する

次のコードスニペットは、PDFファイルからキャレット注釈を削除する方法を示しています。

```csharp
public static void DeleteCaretAnnotation()
{
    // PDFファイルをロードする
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();

    foreach (var ca in caretAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
}
```
## 特定のページ領域をRedaction Annotationで塗りつぶす方法 - Aspose.PDF for .NET

Aspose.PDF for .NETは、既存のPDFファイルでアノテーションを追加および操作する機能をサポートしています。最近、いくつかのお客様からPDFドキュメントの特定のページ領域からテキストや画像などの要素を削除する（塗りつぶす）要望がありました。この要求を満たすために、特定のページ領域を塗りつぶすために使用できるRedactionAnnotationというクラスが提供されています。また、既存のRedactionAnnotationsを操作して塗りつぶすこともできます（つまり、アノテーションをフラット化し、その下のテキストを削除します）。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// ドキュメントを開く
Document doc = new Document(dataDir + "input.pdf");

// 特定のページ領域のRedactionAnnotationインスタンスを作成
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// 塗りつぶしアノテーションに印刷されるテキスト
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// 塗りつぶしアノテーションにオーバーレイテキストを繰り返す
annot.Repeat = true;
// アノテーションを最初のページのアノテーションコレクションに追加
doc.Pages[1].Annotations.Add(annot);
// アノテーションをフラット化し、ページの内容（テキストや画像を削除）を塗りつぶす
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
### ファサードアプローチ

Aspose.PDF.Facades 名前空間には、PDFファイル内の既存のアノテーションを操作する機能を提供する [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) というクラスもあります。このクラスには、特定のページ領域を削除する機能を提供する [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) というメソッドが含まれています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// 特定のページ領域を隠蔽
editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
editor.BindPdf(dataDir + "input.pdf");
editor.Save(dataDir + "FacadesApproach_out.pdf");
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

