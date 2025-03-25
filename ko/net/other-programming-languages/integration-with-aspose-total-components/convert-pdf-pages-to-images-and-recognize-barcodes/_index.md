---
title: PDF 페이지를 이미지로 변환하고 바코드 인식하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/convert-pdf-pages-to-images-and-recognize-barcodes/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF Pages to Images and Recognize Barcodes",
    "alternativeHeadline": "Convert PDF Pages to Images with Barcode Recognition in C#",
    "abstract": "이 새로운 기능은 PDF 페이지를 다양한 이미지 형식으로 원활하게 변환할 수 있게 하며, Aspose.Barcode for .NET을 사용하여 내장된 바코드를 식별할 수 있도록 합니다. 이 기능은 사용자가 PDF 콘텐츠를 이미지로 변환하고 바코드를 정확하게 인식하여 효율적인 데이터 처리를 가능하게 함으로써 문서 처리를 간소화합니다.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

{{% alert color="primary" %}}

PDF 문서는 일반적으로 텍스트, 이미지, 표, 첨부 파일, 그래프, 주석 및 기타 객체로 구성됩니다. 일부 고객은 문서에 바코드를 삽입한 다음 PDF 파일에서 바코드를 식별해야 합니다. 다음 기사는 PDF 파일의 페이지를 이미지로 변환하고 Aspose.Barcode for .NET을 사용하여 이미지에서 바코드를 식별하는 방법을 설명합니다.

{{% /alert %}}

## 페이지를 이미지로 변환하고 바코드 인식하기

{{% alert color="primary" %}}

Aspose.PDF for .NET은 PDF 문서를 관리하기 위한 매우 강력한 제품입니다. PDF 문서의 페이지를 이미지로 변환하는 작업을 쉽게 만들어 줍니다. Aspose.BarCode for .NET 또한 바코드를 생성하고 인식하는 데 강력한 제품입니다.

Aspose.Pdf.Facades 네임스페이스의 PdfConverter 클래스는 PDF 페이지를 다양한 이미지 형식으로 변환하는 것을 지원합니다. Aspose.Pdf.Devices 네임스페이스의 PngDevice는 PDF 페이지를 PNG 파일로 변환하는 것을 지원합니다. 이 두 클래스 중 하나를 사용하여 PDF 파일의 페이지를 이미지로 변환할 수 있습니다.

페이지가 이미지 형식으로 변환되면 Aspose.BarCode for .NET을 사용하여 그 안의 바코드를 식별할 수 있습니다. 아래의 코드 샘플은 PdfConverter 또는 PngDevice를 사용하여 페이지를 변환하는 방법을 보여줍니다.

{{% /alert %}}

### Aspose.Pdf.Facades 사용하기

{{% alert color="primary" %}}

PdfConverter 클래스에는 현재 PDF 페이지에서 이미지를 생성하는 GetNextImage라는 메서드가 포함되어 있습니다. 출력 이미지 형식을 지정하기 위해 이 메서드는 System.Drawing.Imaging.ImageFormat 열거형의 인수를 받습니다.

Aspose.Barcode에는 BarCodeRecognition이라는 네임스페이스가 있으며, 그 안에는 BarCodeReader 클래스가 포함되어 있습니다. BarCodeReader 클래스는 이미지 파일에서 바코드를 읽고, 결정하고, 식별할 수 있게 해줍니다.

이 예제의 목적을 위해, 먼저 Aspose.Pdf.Facades.PdfConverter를 사용하여 PDF 파일의 페이지를 이미지로 변환합니다. 그런 다음 Aspose.BarCodeRecognition.BarCodeReader 클래스를 사용하여 이미지에서 바코드를 인식합니다.

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

위의 코드 스니펫에서 출력 이미지는 MemoryStream 객체에 저장됩니다. 이미지는 디스크에 저장할 수도 있습니다. 그렇게 하려면, PdfConverter 클래스의 GetNextImage 메서드에 대한 문자열 객체로 MemoryStream 객체를 교체하십시오.

{{% /alert %}}

#### PngDevice 클래스 사용하기

Aspose.Pdf.Devices에는 PngDevice가 있습니다. 이 클래스는 PDF 문서의 페이지를 PNG 이미지로 변환할 수 있게 해줍니다.

이 예제의 목적을 위해, 소스 PDF 파일을 Document에 로드한 다음 문서의 페이지를 PNG 이미지로 변환합니다. 이미지가 생성되면 Aspose.BarCodeRecognition의 BarCodeReader 클래스를 사용하여 이미지에서 바코드를 식별하고 읽습니다.

{{% alert color="primary" %}}

여기 제공된 코드 샘플은 PDF 문서의 페이지를 순회하며 각 페이지에서 바코드를 식별하려고 시도합니다.

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

이 기사에서 다룬 주제에 대한 추가 정보는 다음을 참조하십시오:

- PDF 페이지를 다른 이미지 형식으로 변환하기 (Facades)
- 모든 PDF 페이지를 PNG 이미지로 변환하기
- [바코드 읽기](https://docs.aspose.com/barcode/net/barcode-recognition/)

{{% /alert %}}