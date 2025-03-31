---
title: 画像とテキストの追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/adding-images-and-text-using-pdffilemend-class/
description: このセクションでは、PdfFileMendクラスを使用して画像とテキストを追加する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Images and Text",
    "alternativeHeadline": "Enhance PDF by Adding Images and Text Precisely",
    "abstract": "新しいPdfFileMendクラスを使用して、既存のPDF内の指定された位置に画像とテキストを簡単に追加できます。直感的なAddImageおよびAddTextメソッドを利用して、さまざまな画像形式とフォーマットされたテキストをシームレスに統合し、配置とページ選択の精度を確保します。画像オーバーレイとテキストラッピングをカスタマイズすることで、視覚的に魅力的で情報豊富な文書を作成し、PDF操作タスクを効率化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1324",
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
    "url": "/net/adding-images-and-text-using-pdffilemend-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-images-and-text-using-pdffilemend-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend)クラスは、既存のPDF文書に指定された位置で画像とテキストを追加するのに役立ちます。 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index)および[AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index)という名前の2つのメソッドを提供します。[AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index)メソッドを使用すると、JPG、GIF、PNG、BMP形式の画像を追加できます。[AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index)メソッドは、[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)クラスの引数を取り、既存のPDFファイルに追加します。画像とテキストは、左下と右上の座標で指定された矩形領域に追加できます。画像を追加する際には、画像ファイルのパスまたは画像ファイルのストリームを指定できます。画像またはテキストを追加するページ番号を指定するために、これらのメソッドはページ番号の引数を提供します。したがって、指定された位置だけでなく、指定されたページにも画像とテキストを追加できます。

画像はPDF文書の内容の重要な部分です。既存のPDFファイル内の画像を操作することは、PDFファイルを扱う人々にとって一般的な要件です。この記事では、[Aspose.Pdf.Facades名前空間](https://reference.aspose.com/pdf/net/aspose.pdf.facades)を使用して、既存のPDFファイル内の画像を操作する方法を探ります。[Aspose.PDF for .NET](/pdf/ja/net/)のすべての画像関連操作は、この文書にまとめられています。

## 実装の詳細

[Aspose.Pdf.Facades名前空間](https://reference.aspose.com/pdf/net/aspose.pdf.facades)を使用すると、既存のPDFファイルに新しい画像を追加できます。また、既存の画像を置き換えたり削除したりすることもできます。PDFファイルを画像に変換することもできます。各ページを個別の画像に変換することも、完全なPDFファイルを1つの画像に変換することもできます。JPEG、BMP、PNG、TIFFなどの形式をサポートしています。また、PDFファイルから画像を抽出することもできます。これらの操作を実装するために、[Aspose.Pdf.Facades名前空間](https://reference.aspose.com/pdf/net/aspose.pdf.facades)の4つのクラス、すなわち[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend)、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)、[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor)、および[PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter)を使用できます。

## 画像操作

このセクションでは、これらの画像操作を詳しく見ていきます。関連するクラスとメソッドの使用を示すコードスニペットも見ていきます。まず、既存のPDFファイルに画像を追加する方法を見てみましょう。[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend)クラスの[AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index)メソッドを使用して新しい画像を追加できます。このメソッドを使用すると、画像を追加したいページ番号だけでなく、画像の位置も指定できます。

## 既存のPDFファイルに画像を追加する（ファサード）

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend)クラスの[AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage)メソッドを使用できます。[AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage)メソッドは、追加する画像、画像を追加するページ番号、および座標情報を必要とします。その後、[Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close)メソッドを使用して更新されたPDFファイルを保存します。

次の例では、imageStreamを使用してページに画像を追加します：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images(); 

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                // Add image to first page
                mender.AddImage(imageStream, 1, 10, 650, 110, 750);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![画像を追加](/pdf/ja/net/images/add_image1.png)

[CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1)を使用すると、1つの画像を別の画像の上に重ねることができます：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters for the image
                var compositingParameters = new Aspose.Pdf.CompositingParameters(Aspose.Pdf.BlendMode.Multiply);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![画像を追加](/pdf/ja/net/images/add_image2.png)

PDFファイルに画像を保存する方法はいくつかあります。次の例でそのうちの1つを示します：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Exclusion and ImageFilterType.Flate
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Exclusion,
                    Aspose.Pdf.ImageFilterType.Flate);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Multiply, ImageFilterType.Flate and false
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Multiply,
                    Aspose.Pdf.ImageFilterType.Flate,
                    false);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_outp.pdf");
            }
        }
    }
}
```

## 既存のPDFファイルにテキストを追加する（ファサード）

テキストを追加する方法はいくつかあります。最初の方法を考えてみましょう。[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)を取得し、ページに追加します。その後、左下の角の座標を指定し、テキストをページに追加します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

        // Add text to the first page at position (10, 750)
        mender.AddText(message, 1, 10, 750);

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

どのように見えるか確認してください：

![テキストを追加](/pdf/ja/net/images/add_text.png)

[FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)を追加する2番目の方法です。さらに、テキストが収まる矩形を指定します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose! Welcome to Aspose!");

        // Add text to the first page at the specified position with wrapping
        mender.AddText(message, 1, 10, 700, 55, 810);

        // Set word wrapping mode to wrap by words
        mender.WrapMode = Aspose.Pdf.Facades.WordWrapMode.ByWords;

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

3番目の例では、指定されたページにテキストを追加する機能を提供します。私たちの例では、文書のページ1と3にキャプションを追加しましょう。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();

        // Create PdfFileMend object
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Bind PDF document
            mender.BindPdf(document);

            // Create formatted text
            var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

            // Specify the pages where text should be added
            int[] pageNums = new int[] { 1, 3 };

            // Add text to the specified pages at the specified coordinates
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // Save PDF document
            mender.Save(dataDir + "AddText_out.pdf");
        }
    }
}
```