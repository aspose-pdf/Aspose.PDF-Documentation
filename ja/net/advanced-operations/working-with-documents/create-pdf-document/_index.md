---
title: C#を使用してPDFを作成する方法
linktitle: PDFドキュメントの作成
type: docs
weight: 10
url: ja/net/create-pdf-document/
description: Aspose.PDF for .NETを使用してPDFドキュメントを作成およびフォーマットします。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#を使用してPDFを作成する方法",
    "alternativeHeadline": "ゼロからPDFドキュメントを作成する",
    "author": {
        "@type": "Person",
        "name":"アナスタシア・ホルブ",
        "givenName": "アナスタシア",
        "familyName": "ホルブ",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, dotnet, PDFドキュメント作成",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETを使用してPDFドキュメントを作成およびフォーマットします。"
}
</script>
私たちは常にC#プロジェクトでPDFドキュメントを生成し、それらをより正確で効果的に扱う方法を探しています。ライブラリから使いやすい機能を使用することで、作業の追跡が可能になり、PDFを生成しようとする際の時間がかかる詳細について心配することが少なくなります。これが.NETであるかどうかです。

以下のコードスニペットも[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリで動作します。

## C#言語を使用してPDFドキュメントを作成（または生成）

Aspose.PDF for .NET APIを使用すると、C#およびVB.NETを使用してPDFファイルを作成および読み取ることができます。このAPIは、WinForms、ASP.NETなど、さまざまな.NETアプリケーションで使用できます。この記事では、Aspose.PDF for .NET APIを使用して.NETアプリケーションでPDFファイルを簡単に生成および読み取る方法を示します。

### 簡単なPDFファイルの作成方法

C#を使用してPDFファイルを作成するには、以下の手順を使用できます。

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスのオブジェクトを作成する

1.
1. [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) をページの [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) コレクションに追加します。
1. 結果のPDF文書を保存します。

```csharp
// ドキュメントディレクトリへのパス
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// ドキュメントオブジェクトを初期化
Document document = new Document();
// ページを追加
Page page = document.Pages.Add();
// 新しいページにテキストを追加
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// 更新されたPDFを保存
document.Save(dataDir + "HelloWorld_out.pdf");
```

### 検索可能なPDF文書を作成する方法

Aspose.PDF for .NETは、PDF文書を作成および既存のPDF文書を操作する機能を提供します。
Aspose.PDF for .NETは、PDFドキュメントの作成および既存のPDFドキュメントの操作機能を提供します。

以下に指定されたロジックは、PDF画像のテキストを認識します。認識するためには、HOCR標準をサポートする外部OCRを使用できます。テスト目的で、無料のGoogle tesseract OCRを使用しました。そのため、まずシステムにTesseract-OCRをインストールし、tesseractコンソールアプリケーションを使用できるようにする必要があります。

以下は、この要件を達成するための完全なコードです：

```csharp
using System;

namespace Aspose.Pdf.Examples.Advanced.WorkingWithDocuments
{
    class ExampleCreateDocument
    {
        private const string _dataDir = "C:\\Samples";
        public static void CreateSearchableDocuments(string file)
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document(file);
            bool convertResult = false;
            try
            {
                convertResult = doc.Convert(CallBackGetHocr);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            doc.Save(file);
            doc.Dispose();
        }

        static string CallBackGetHocr(System.Drawing.Image img)
        {
            string tmpFile = System.IO.Path.GetTempFileName();
            try
            {
                System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(img);

                bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
                string inputFile = string.Concat('"', tmpFile, '"');
                string outputFile = string.Concat('"', tmpFile, '"');
                string arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
                string tesseractProcessName = @"C:\Program Files\Tesseract-OCR\Tesseract.exe";

                System.Diagnostics.ProcessStartInfo psi =
                    new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
                    {
                        UseShellExecute = true,
                        CreateNoWindow = true,
                        WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
                        WorkingDirectory = System.IO.Path.GetDirectoryName(tesseractProcessName)
                    };

                System.Diagnostics.Process p = new System.Diagnostics.Process
                {
                    StartInfo = psi
                };
                p.Start();
                p.WaitForExit();

                System.IO.StreamReader streamReader = new System.IO.StreamReader(tmpFile + ".hocr");
                string text = streamReader.ReadToEnd();
                streamReader.Close();

                return text;
            }
            finally
            {
                if (System.IO.File.Exists(tmpFile))
                    System.IO.File.Delete(tmpFile);
                if (System.IO.File.Exists(tmpFile + ".hocr"))
                    System.IO.File.Delete(tmpFile + ".hocr");
            }
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

