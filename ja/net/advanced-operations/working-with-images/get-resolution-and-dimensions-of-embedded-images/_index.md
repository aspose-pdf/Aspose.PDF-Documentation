---
title: 画像の解像度と寸法を取得する
linktitle: 解像度と寸法を取得
type: docs
weight: 40
url: ja/net/get-resolution-and-dimensions-of-embedded-images/
description: このセクションは、埋め込み画像の解像度と寸法を取得する詳細を示しています
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "画像の解像度と寸法を取得する",
    "alternativeHeadline": "埋め込み画像の解像度と寸法を取得する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "PDF, C#, 解像度を取得, 寸法を取得",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションは、埋め込み画像の解像度と寸法を取得する詳細を示しています"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリとも連携します。

このトピックでは、画像を抽出することなく、画像の解像度や寸法情報を取得する機能を提供する Aspose.PDF 名前空間のオペレータークラスの使用方法について説明します。

これを達成する方法はいくつかあります。この記事では、`arraylist` と [image placement classes](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement) の使用方法について説明します。

1. 最初に、画像が含まれるソースPDFファイルを読み込みます。
1. 次に、ドキュメント内の画像の名前を保持するための ArrayList オブジェクトを作成します。
1. Page.Resources.Images プロパティを使用して画像を取得します。
1. 画像のグラフィックステートを保持するスタックオブジェクトを作成し、異なる画像状態を追跡するために使用します。
1.
1.
1. マトリックスをConcatenateMatrixで修正できるため、元の画像状態に戻す必要がある場合もあります。GSaveおよびGRestoreオペレーターを使用してください。これらのオペレーターはペアになっているため、一緒に呼び出す必要があります。たとえば、複雑な変換を伴うグラフィック作業を行い、最終的に変換を初期状態に戻す場合、アプローチは次のようになります：

```csharp
// テキストを描画
GSave

ConcatenateMatrix  // オペレーターの後で内容を回転

// グラフィック作業

ConcatenateMatrix // オペレーターの後で内容を拡大（前の回転を含む）

// その他のグラフィック作業

GRestore

// テキストを描画
```

その結果、テキストは通常の形で描画されますが、テキストオペレーター間でいくつかの変換が実行されます。画像を表示するため、またはフォームオブジェクトや画像を描画するために、Doオペレーターを使用する必要があります。

また、XImageというクラスがあり、WidthとHeightの2つのプロパティを提供しており、画像の寸法を取得するために使用できます。

1.
1. コマンドプロンプトで画像名とともに情報を表示します。

次のコードスニペットは、PDFドキュメントから画像を抽出せずに画像の寸法と解像度を取得する方法を示しています。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパスです。
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// ソースPDFファイルをロードします
Document doc = new Document(dataDir+ "ImageInformation.pdf");

// 画像のデフォルト解像度を定義します
int defaultResolution = 72;
System.Collections.Stack graphicsState = new System.Collections.Stack();
// 画像名を保持するための配列リストオブジェクトを定義します
System.Collections.ArrayList imageNames = new System.Collections.ArrayList(doc.Pages[1].Resources.Images.Names);
// スタックにオブジェクトを挿入します
graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

// ドキュメントの最初のページのすべてのオペレーターを取得します
foreach (Operator op in doc.Pages[1].Contents)
{
    // GSave/GRestoreオペレーターを使って、以前に設定された変換に戻します
    Aspose.Pdf.Operators.GSave opSaveState = op as Aspose.Pdf.Operators.GSave;
    Aspose.Pdf.Operators.GRestore opRestoreState = op as Aspose.Pdf.Operators.GRestore;
    // 現在の変換行列を定義するConcatenateMatrixオブジェクトをインスタンス化します。
    Aspose.Pdf.Operators.ConcatenateMatrix opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
    // リソースからオブジェクトを描画するDoオペレーターを作成します。FormオブジェクトとImageオブジェクトを描画します
    Aspose.Pdf.Operators.Do opDo = op as Aspose.Pdf.Operators.Do;

    if (opSaveState != null)
    {
        // 以前の状態を保存し、現在の状態をスタックの一番上にプッシュします
        graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
    }
    else if (opRestoreState != null)
    {
        // 現在の状態を捨てて、以前の状態を復元します
        graphicsState.Pop();
    }
    else if (opCtm != null)
    {
        System.Drawing.Drawing2D.Matrix cm = new System.Drawing.Drawing2D.Matrix(
           (float)opCtm.Matrix.A,
           (float)opCtm.Matrix.B,
           (float)opCtm.Matrix.C,
           (float)opCtm.Matrix.D,
           (float)opCtm.Matrix.E,
           (float)opCtm.Matrix.F);

        // 現在の行列と状態行列を乗算します
        ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

        continue;
    }
    else if (opDo != null)
    {
        // これが画像描画オペレーターの場合
        if (imageNames.Contains(opDo.Name))
        {
            System.Drawing.Drawing2D.Matrix lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
            // 最初のPDFページの画像を保持するXImageオブジェクトを作成します
            XImage image = doc.Pages[1].Resources.Images[opDo.Name];

            // 画像の寸法を取得します
            double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
            double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
            // 画像の高さと幅の情報を取得します
            double originalWidth = image.Width;
            double originalHeight = image.Height;

            // 上記の情報に基づいて解像度を計算します
            double resHorizontal = originalWidth * defaultResolution / scaledWidth;
            double resVertical = originalHeight * defaultResolution / scaledHeight;

            // 各画像の寸法と解像度の情報を表示します
            Console.Out.WriteLine(
                    string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                 opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                 resVertical));
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

