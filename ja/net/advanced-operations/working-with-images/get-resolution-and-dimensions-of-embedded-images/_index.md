---
title: 画像の解像度と寸法を取得する
linktitle: 解像度と寸法を取得する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ja/net/get-resolution-and-dimensions-of-embedded-images/
description: Aspose.PDFを使用して、.NETでPDFから埋め込まれた画像の解像度と寸法を取得する方法を学びます。
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Resolution and Dimensions of Images",
    "alternativeHeadline": "Extract Image Resolution and Dimensions Efficiently",
    "abstract": "Aspose.PDFライブラリを使用して、PDF文書内の埋め込まれた画像の解像度と寸法を効率的に取得する方法を発見してください。この機能により、開発者は抽出せずに画像プロパティに直接アクセスでき、PDFファイル内の画像操作プロセスを簡素化し、画像データに対する機能と制御を強化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Get Resolution, Dimensions of Images, Embedded Images, Aspose.PDF.Drawing, ArrayList, Image Placement Classes, ConcatenateMatrix, XImage, PDF Manipulation Library, Image Resolution Computation",
    "wordcount": "827",
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
    "url": "/net/get-resolution-and-dimensions-of-embedded-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-resolution-and-dimensions-of-embedded-images/"
    },
    "dateModified": "2024-11-26",
    "description": "このセクションでは、埋め込まれた画像の解像度と寸法を取得する方法の詳細を示します。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

このトピックでは、画像を抽出せずに解像度と寸法情報を取得する機能を提供するAspose.PDF名前空間のオペレータクラスの使用方法を説明します。

これを達成する方法はいくつかあります。この記事では、`arraylist`と[画像配置クラス](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement)を使用する方法を説明します。

1. まず、ソースPDFファイル（画像を含む）をロードします。
1. 次に、ドキュメント内の画像の名前を保持するためにArrayListオブジェクトを作成します。
1. Page.Resources.Imagesプロパティを使用して画像を取得します。
1. 画像のグラフィックス状態を保持するためのスタックオブジェクトを作成し、異なる画像状態を追跡します。
1. 現在の変換を定義するConcatenateMatrixオブジェクトを作成します。これにより、コンテンツのスケーリング、回転、歪みをサポートします。新しい行列を以前の行列と連結します。最初から変換を定義することはできず、既存の変換のみを変更できることに注意してください。
1. ConcatenateMatrixで行列を変更できるため、元の画像状態に戻す必要がある場合もあります。GSaveおよびGRestoreオペレータを使用します。これらのオペレータはペアになっているため、一緒に呼び出す必要があります。たとえば、複雑な変換でグラフィックス作業を行い、最終的に変換を初期状態に戻す場合、アプローチは次のようになります。

```csharp
// Draw some text
GSave

ConcatenateMatrix  // rotate contents after the operator

// Some graphics work

ConcatenateMatrix // scale (with previous rotation) contents after the operator

// Some other graphics work

GRestore

// Draw some text
```

その結果、テキストは通常の形式で描画されますが、テキストオペレータの間にいくつかの変換が行われます。画像を表示したり、形状オブジェクトや画像を描画するためには、Doオペレータを使用する必要があります。

また、画像の寸法を取得するために使用できるWidthおよびHeightという2つのプロパティを提供するXImageというクラスもあります。

1. 画像解像度を計算するためのいくつかの計算を実行します。
1. 画像名とともにコマンドプロンプトに情報を表示します。

次のコードスニペットは、PDF文書から画像を抽出せずに画像の寸法と解像度を取得する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageInformationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageInformation.pdf"))
    {
        // Define the default resolution for image
        int defaultResolution = 72;
        var graphicsState = new Stack();

        // Define list which will hold image names
        var imageNames = new List<string>(document.Pages[1].Resources.Images.Names);

        // Insert an object to stack
        graphicsState.Push(new System.Drawing.Drawing2D.Matrix(1, 0, 0, 1, 0, 0));

        // Get all the operators on first page of document
        foreach (var op in document.Pages[1].Contents)
        {
            // Use GSave/GRestore operators to revert the transformations back to previously set
            var opSaveState = op as Aspose.Pdf.Operators.GSave;
            var opRestoreState = op as Aspose.Pdf.Operators.GRestore;
            var opCtm = op as Aspose.Pdf.Operators.ConcatenateMatrix;
            var opDo = op as Aspose.Pdf.Operators.Do;

            if (opSaveState != null)
            {
                // Save previous state and push current state to the top of the stack
                graphicsState.Push(((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Clone());
            }
            else if (opRestoreState != null)
            {
                // Throw away current state and restore previous one
                graphicsState.Pop();
            }
            else if (opCtm != null)
            {
                var cm = new System.Drawing.Drawing2D.Matrix(
                   (float)opCtm.Matrix.A,
                   (float)opCtm.Matrix.B,
                   (float)opCtm.Matrix.C,
                   (float)opCtm.Matrix.D,
                   (float)opCtm.Matrix.E,
                   (float)opCtm.Matrix.F);

                // Multiply current matrix with the state matrix
                ((System.Drawing.Drawing2D.Matrix)graphicsState.Peek()).Multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // In case this is an image drawing operator
                if (imageNames.Contains(opDo.Name))
                {
                    var lastCTM = (System.Drawing.Drawing2D.Matrix)graphicsState.Peek();
                    // Create XImage object to hold images of first pdf page
                    var image = document.Pages[1].Resources.Images[opDo.Name];

                    // Get image dimensions
                    double scaledWidth = Math.Sqrt(Math.Pow(lastCTM.Elements[0], 2) + Math.Pow(lastCTM.Elements[1], 2));
                    double scaledHeight = Math.Sqrt(Math.Pow(lastCTM.Elements[2], 2) + Math.Pow(lastCTM.Elements[3], 2));
                    // Get Height and Width information of image
                    double originalWidth = image.Width;
                    double originalHeight = image.Height;

                    // Compute resolution based on above information
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Display Dimension and Resolution information of each image
                    Console.Out.WriteLine(
                            string.Format(dataDir + "image {0} ({1:.##}:{2:.##}): res {3:.##} x {4:.##}",
                                         opDo.Name, scaledWidth, scaledHeight, resHorizontal,
                                         resVertical));
                }
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