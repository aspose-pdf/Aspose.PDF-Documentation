---
title: PDFページを画像に変換し、バーコードを認識する
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "この新機能により、PDFページをさまざまな画像形式にシームレスに変換し、Aspose.Barcode for .NETを使用して埋め込まれたバーコードを識別することができます。この機能は、ユーザーがPDFコンテンツを画像に変換し、効率的なデータ処理のためにバーコードを正確に認識できるようにすることで、文書処理を簡素化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "858",
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
    "url": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-pages-to-images-and-recognize-barcodes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

{{% alert color="primary" %}}

PDF文書は通常、テキスト、画像、表、添付ファイル、グラフ、注釈、その他のオブジェクトで構成されています。私たちの顧客の中には、文書にバーコードを埋め込み、その後PDFファイル内のバーコードを識別する必要がある方もいます。以下の記事では、PDFファイルのページを画像に変換し、Aspose.Barcode for .NETを使用して画像内のバーコードを識別する方法を説明します。

{{% /alert %}}

## ページを画像に変換し、バーコードを認識する

{{% alert color="primary" %}}

Aspose.PDF for .NETは、PDF文書を管理するための非常に強力な製品です。PDF文書のページを画像に変換するのが簡単です。Aspose.BarCode for .NETも、バーコードを生成および認識するための同様に強力な製品です。

Aspose.Pdf.Facades名前空間のPdfConverterクラスは、PDFページをさまざまな画像形式に変換することをサポートしています。Aspose.Pdf.Devices名前空間のPngDeviceは、PDFページをPNGファイルに変換することをサポートしています。これらのクラスのいずれかを使用して、PDFファイルのページを画像に変換できます。

ページが画像形式に変換されたら、Aspose.BarCode for .NETを使用してその中のバーコードを識別できます。以下のコードサンプルは、PdfConverterまたはPngDeviceを使用してページを変換する方法を示しています。

{{% /alert %}}

### Aspose.Pdf.Facadesを使用する

{{% alert color="primary" %}}

PdfConverterクラスには、現在のPDFページから画像を生成するGetNextImageというメソッドがあります。出力画像形式を指定するために、このメソッドはSystem.Drawing.Imaging.ImageFormat列挙体からの引数を受け入れます。

Aspose.Barcodeには、BarCodeRecognitionという名前空間があり、BarCodeReaderクラスが含まれています。BarCodeReaderクラスを使用すると、画像ファイルからバーコードを読み取り、判断し、識別できます。

この例の目的のために、まずAspose.Pdf.Facades.PdfConverterを使用してPDFファイルのページを画像に変換します。次に、Aspose.BarCodeRecognition.BarCodeReaderクラスを使用して画像内のバーコードを認識します。

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodesConverter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Create a PdfConverter object
    var converter = new Aspose.Pdf.Facades.PdfConverter();

    // Bind PDF document
    converter.BindPdf(dataDir + "IdentifyBarcodes.pdf");

    // Specify the start page to be processed
    converter.StartPage = 1;

    // Specify the end page for processing
    converter.EndPage = 1;

    // Create a Resolution object to specify the resolution of resultant image
    converter.Resolution = new Aspose.Pdf.Devices.Resolution(300);

    // Initialize the convertion process
    converter.DoConvert();

    // Create a MemoryStream object to hold the resultant image
    using (var imageStream = new MemoryStream())
    {
        // Check if pages exist and then convert to image one by one
        while (converter.HasNextImage())
        {
            // Save the image in the given image Format
            converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

            // Set the stream position to the beginning of the stream
            imageStream.Position = 0;

            // Instantiate a BarCodeReader object
            var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

            // String txtResult.Text = "";
            while (barcodeReader.Read())
            {
                // Get the barcode text from the barcode image
                var code = barcodeReader.GetCodeText();

                // Write the barcode text to Console output
                Console.WriteLine("BARCODE : " + code);
            }

            // Close the BarCodeReader object to release the image file
            barcodeReader.Close();
        }

        // Close the PdfConverter instance and release the resources
        converter.Close();
    }
}
```

{{% alert color="primary" %}}

上記のコードスニペットでは、出力画像がMemoryStreamオブジェクトに保存されます。画像はディスクにも保存できます。その場合は、MemoryStreamオブジェクトをPdfConverterクラスのGetNextImageメソッドに対するファイルパスを表す文字列オブジェクトに置き換えます。

{{% /alert %}}

#### PngDeviceクラスを使用する

Aspose.Pdf.Devicesには、PngDeviceがあります。このクラスを使用すると、PDF文書のページをPNG画像に変換できます。

この例の目的のために、ソースPDFファイルをDocumentに読み込み、文書のページをPNG画像に変換します。画像が作成されたら、Aspose.BarCodeRecognitionのBarCodeReaderクラスを使用して画像内のバーコードを識別し、読み取ります。

{{% alert color="primary" %}}

ここに示されたコードサンプルは、PDF文書のページを横断し、各ページのバーコードを識別しようとします。

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IdentifyBarcodes()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "IdentifyBarcodes.pdf"))
    {
        // Traverse through the individual pages of the PDF file
        for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            using (var imageStream = new MemoryStream())
            {
                // Create a Resolution object
                var resolution = new Aspose.Pdf.Devices.Resolution(300);

                // Instantiate a PngDevice object while passing a Resolution object as an argument to its constructor
                var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);

                // Convert a particular page and save the image to stream
                pngDevice.Process(document.Pages[pageCount], imageStream);

                // Set the stream position to the beginning of Stream
                imageStream.Position = 0;

                // Instantiate a BarCodeReader object
                var barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

                // String txtResult.Text = "";
                while (barcodeReader.Read())
                {
                    // Get the barcode text from the barcode image
                    var code = barcodeReader.GetCodeText();

                    // Write the barcode text to Console output
                    Console.WriteLine("BARCODE : " + code);
                }

                // Close the BarCodeReader object to release the image file
                barcodeReader.Close();
            }
        }
    }
}
```

{{% alert color="primary" %}}

この記事で取り上げたトピックに関する詳細情報は、以下のリンクをご覧ください：

- PDFページを異なる画像形式に変換する（Facades）
- すべてのPDFページをPNG画像に変換する
- [バーコードを読み取る](https://docs.aspose.com/barcode/net/barcode-recognition/)

{{% /alert %}}