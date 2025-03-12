---
title: PDFから画像を抽出し、バーコードを認識する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/extract-images-from-pdf-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images from PDF and recognize BarCodes",
    "alternativeHeadline": "Extract Images and Barcodes from PDF files in C#",
    "abstract": "PDF文書から画像を効率的に抽出し、埋め込まれたバーコードを正確に認識する方法を発見してください。新しい機能は、PDFの各ページから抽出された画像を処理することによってバーコード情報を特定するプロセスを簡素化し、データの取得と管理を向上させます。文書処理ワークフローを最適化するための詳細な手順とコード実装を探求してください。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "317",
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
    "url": "/net/extract-images-from-pdf-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images-from-pdf-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

PDF文書は通常、テキスト、画像、表、添付ファイル、グラフ、注釈、およびその他の関連オブジェクトで構成されています。バーコードがPDFファイル内に埋め込まれている場合があり、一部の顧客はPDFファイル内に存在するバーコードを特定する必要があります。以下の記事では、PDFページから画像を抽出し、それらの中のバーコードを特定する手順を説明します。

{{% /alert %}}

Aspose.PDF for .NETのドキュメントオブジェクトモデルによれば、PDFファイルは1つ以上のページを含み、各ページにはリソースオブジェクト内に画像、フォーム、フォントのコレクションが含まれています。したがって、PDFファイルから画像を抽出するために、PDFファイルの各ページを個別にトラバースし、特定のページから画像のコレクションを取得し、Aspose.BarCodeRecognitionのBarCodeReaderクラスでのさらなる処理のためにMemoryStreamオブジェクトに保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through individual pages of PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Traverse through each image extracted from PDF pages
            foreach (var xImage in document.Pages[pageCount].Resources.Images)
            {
                using (var imageStream = new MemoryStream())
                {
                    // Save PDF document image
                    xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
        
                    // Set the stream position to the begining of Stream
                    imageStream.Position = 0;
        
                    // Instantiate BarCodeReader object
                    var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
        
                    while (barcodeReader.Read())
                    {
                        // Get BarCode text from BarCode image
                        var code = barcodeReader.GetCodeText();
        
                        // Write the BarCode text to Console output
                        Console.WriteLine("BARCODE : " + code);
                    }
        
                    // Close BarCodeReader object to release the Image file
                    barcodeReader.Close();
                }
            }
        }
    }
}
```

この記事で取り上げられているトピックの詳細については、以下のリンクを訪問してください：

- [PDFファイルから画像を抽出する](/net/extract-images-from-the-pdf-file/)
- [バーコードを読み取る](https://docs.aspose.com/barcode/net/barcode-recognition/)