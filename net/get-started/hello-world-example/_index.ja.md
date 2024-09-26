---
title: C#言語を使用したHello Worldの例
linktitle: Hello Worldの例
type: docs
weight: 40
url: /net/hello-world-example/
description: このサンプルは、Aspose.PDFを使用して「Hello World」というテキストを含むシンプルなPDFドキュメントを作成する方法を示しています
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#言語を使用したHello Worldの例",
    "alternativeHeadline": "Aspose.PDF C#の例",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, ドキュメント生成",
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "このサンプルは、Aspose.PDFを使用して「Hello World」というテキストを含むシンプルなPDFドキュメントを作成する方法を示しています",
    "articleBody": "「Hello World」の例は、プログラミング言語やソフトウェアの機能をシンプルなユースケースで紹介するために伝統的に使用されます。\nAspose.PDF for .NETは、PDFドキュメントの作成、操作、変換機能を.NETアプリケーションに組み込むことができる豊富なPDF APIです。PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX、画像ファイル形式を含む多くの人気ファイル形式をサポートしています。この記事では、「Hello World!」というテキストを含むPDFドキュメントを作成しています。Aspose.PDF for .NETを環境にインストールした後、以下のコードサンプルを実行して、Aspose.PDF APIの動作を確認できます。\n以下のコードスニペットは、次のステップに従います：\n1. Documentオブジェクトをインスタンス化する\n2. ドキュメントオブジェクトにページを追加する\n3. TextFragmentを作成する\n4. TextFragmentをページのParagraphコレクションに追加する\n5. 結果のPDFドキュメントを保存する\n次のコードスニペットは、Aspose.PDF for .NET APIの動作を示すHello Worldプログラムです。"
}
</script>
"Hello World"の例は、プログラミング言語やソフトウェアの特徴を簡単な使用例で紹介するために伝統的に使用されます。

Aspose.PDF for .NETは、開発者が自分の.NETアプリケーションにPDFドキュメントの作成、操作、変換機能を組み込むことができる機能豊富なPDF APIです。PDF、XFA、TXT、HTML、PCL、XML、XPS、EPUB、TEX、画像ファイル形式を含む多くの人気ファイル形式をサポートしています。この記事では、テキスト「Hello World!」を含むPDFドキュメントを作成しています。Aspose.PDF for .NETを環境にインストールした後、以下のコードサンプルを実行してAspose.PDF APIの動作を確認できます。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

以下のコードスニペットは、これらのステップに従います：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) オブジェクトをインスタンス化します
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)を追加します
1.
1. ページの[Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs)コレクションにTextFragmentを追加する
1. 結果のPDFドキュメントを[保存](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4)する

以下のコードスニペットは、Aspose.PDF for .NET APIの動作を示すHello Worldプログラムです。

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // ドキュメントオブジェクトを初期化
            Document document = new Document();
            // ページを追加
            Page page = document.Pages.Add();
            // 新しいページにテキストを追加
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // 更新されたPDFを保存
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
