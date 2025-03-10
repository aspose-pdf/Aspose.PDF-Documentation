---
title: 将PDF页面转换为图像并识别条形码
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "此新功能实现了PDF页面无缝转换为各种图像格式，便于使用Aspose.Barcode for .NET识别嵌入的条形码。此功能通过允许用户将PDF内容转换为图像并准确识别条形码，从而简化了文档处理，以实现高效的数据处理。",
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
    "description": "Aspose.PDF不仅可以执行简单易行的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

{{% alert color="primary" %}}

PDF文档通常包含文本、图像、表格、附件、图形、注释和其他对象。我们的部分客户需要在文档中嵌入条形码，然后识别PDF文件中的条形码。以下文章解释了如何将PDF文件中的页面转换为图像，并使用Aspose.Barcode for .NET识别图像中的条形码。

{{% /alert %}}

## 将页面转换为图像并识别条形码

{{% alert color="primary" %}}

Aspose.PDF for .NET是一个非常强大的PDF文档管理产品。它使得将PDF文档中的页面转换为图像变得简单。Aspose.BarCode for .NET同样是一个强大的生成和识别条形码的产品。

Aspose.Pdf.Facades命名空间下的PdfConverter类支持将PDF页面转换为各种图像格式。Aspose.Pdf.Devices命名空间下的PngDevice支持将PDF页面转换为PNG文件。这两个类都可以用于将PDF文件的页面转换为图像。

当页面被转换为图像格式后，我们可以使用Aspose.BarCode for .NET来识别其中的条形码。以下代码示例展示了如何使用PdfConverter或PngDevice转换页面。

{{% /alert %}}

### 使用Aspose.Pdf.Facades

{{% alert color="primary" %}}

PdfConverter类包含一个名为GetNextImage的方法，该方法从当前PDF页面生成图像。为了指定输出图像格式，此方法接受来自System.Drawing.Imaging.ImageFormat枚举的参数。

Aspose.Barcode包含一个命名空间BarCodeRecognition，其中包含BarCodeReader类。BarCodeReader类允许您从图像文件中读取、确定和识别条形码。

为了本示例的目的，首先使用Aspose.Pdf.Facades.PdfConverter将PDF文件中的一页转换为图像。然后使用Aspose.BarCodeRecognition.BarCodeReader类识别图像中的条形码。

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

在上述代码片段中，输出图像被保存到MemoryStream对象中。图像也可以保存到磁盘。为此，将MemoryStream对象替换为表示文件路径的字符串对象，传递给PdfConverter类的GetNextImage方法。

{{% /alert %}}

#### 使用PngDevice类

在Aspose.Pdf.Devices中，有PngDevice类。此类允许您将PDF文档中的页面转换为PNG图像。

为了本示例的目的，将源PDF文件加载到Document中，并将文档的页面转换为PNG图像。当图像创建完成后，使用Aspose.BarCodeRecognition下的BarCodeReader类识别和读取图像中的条形码。

{{% alert color="primary" %}}

这里给出的代码示例遍历PDF文档的页面，并尝试识别每个页面上的条形码。

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

有关本文中涵盖主题的更多信息，请访问：

- 将PDF页面转换为不同的图像格式（Facades）
- 将所有PDF页面转换为PNG图像
- [读取条形码](https://docs.aspose.com/barcode/net/barcode-recognition/)

{{% /alert %}}