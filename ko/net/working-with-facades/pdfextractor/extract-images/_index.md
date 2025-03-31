---
title: PdfExtractor를 사용하여 이미지 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/extract-images/
description: 이 섹션에서는 PdfExtractor 클래스를 사용하여 Aspose.PDF Facades로 이미지를 추출하는 방법을 설명합니다.
lastmod: "2021-07-15"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images using PdfExtractor",
    "alternativeHeadline": "Extract Images from PDF with PdfExtractor Class",
    "abstract": "Aspose.PDF의 PdfExtractor 기능은 사용자가 PDF 문서에서 이미지를 효율적으로 추출할 수 있도록 하며, 전체 문서, 특정 페이지 또는 지정된 범위에서 이미지를 추출하는 여러 옵션을 제공합니다. 이미지를 파일이나 메모리 스트림에 직접 저장할 수 있어 PDF 자산을 다루는 개발자에게 유연성을 제공합니다. 이 강력한 기능은 이미지 추출 모드에 대한 정밀한 제어를 가능하게 하여 다양한 PDF 콘텐츠 유형을 처리하기 쉽게 만듭니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1789",
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
    "url": "/net/extract-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 전체 PDF에서 파일로 이미지 추출 (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor) 클래스는 PDF 파일에서 이미지를 추출할 수 있게 해줍니다. 먼저, [PdfExtractor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [ExtractImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출하여 모든 이미지를 메모리로 추출합니다. 이미지가 추출되면 [HasNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 사용하여 해당 이미지를 가져올 수 있습니다. while 루프를 사용하여 모든 추출된 이미지를 반복해야 합니다. 이미지를 디스크에 저장하려면 파일 경로를 인수로 받는 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드의 오버로드를 호출할 수 있습니다. 다음 코드 스니펫은 전체 PDF에서 파일로 이미지를 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract all the images
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
    }
}
```

## 전체 PDF에서 스트림으로 이미지 추출 (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor) 클래스는 PDF 파일에서 이미지를 스트림으로 추출할 수 있게 해줍니다. 먼저, [PdfExtractor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [ExtractImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출하여 모든 이미지를 메모리로 추출합니다. 이미지가 추출되면 [HasNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 사용하여 해당 이미지를 가져올 수 있습니다. while 루프를 사용하여 모든 추출된 이미지를 반복해야 합니다. 이미지를 스트림에 저장하려면 Stream을 인수로 받는 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드의 오버로드를 호출할 수 있습니다. 다음 코드 스니펫은 전체 PDF에서 스트림으로 이미지를 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDFStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract images
        extractor.ExtractImage();
        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## PDF의 특정 페이지에서 이미지 추출 (Facades)

PDF 파일의 특정 페이지에서 이미지를 추출할 수 있습니다. 이를 위해 [StartPage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/properties/startpage) 및 [EndPage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/properties/endpage) 속성을 추출할 페이지로 설정해야 합니다. 먼저, [PdfExtractor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 다음, [StartPage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/properties/startpage) 및 [EndPage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/properties/endpage) 속성을 설정해야 합니다. 그 후, [ExtractImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출하여 모든 이미지를 메모리로 추출합니다. 이미지가 추출되면 [HasNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 사용하여 해당 이미지를 가져올 수 있습니다. while 루프를 사용하여 모든 추출된 이미지를 반복해야 합니다. 이미지를 디스크나 스트림에 저장할 수 있습니다. 적절한 오버로드의 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 호출하기만 하면 됩니다. 다음 코드 스니펫은 PDF의 특정 페이지에서 스트림으로 이미지를 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();
        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## PDF의 페이지 범위에서 이미지 추출 (Facades)

PDF 파일의 페이지 범위에서 이미지를 추출할 수 있습니다. 이를 위해 [StartPage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/properties/startpage) 및 [EndPage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/properties/endpage) 속성을 추출할 페이지 범위로 설정해야 합니다. 먼저, [PdfExtractor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 다음, [StartPage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/properties/startpage) 및 [EndPage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/properties/endpage) 속성을 설정해야 합니다. 그 후, [ExtractImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출하여 모든 이미지를 메모리로 추출합니다. 이미지가 추출되면 [HasNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 사용하여 해당 이미지를 가져올 수 있습니다. while 루프를 사용하여 모든 추출된 이미지를 반복해야 합니다. 이미지를 디스크나 스트림에 저장할 수 있습니다. 적절한 오버로드의 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 호출하기만 하면 됩니다. 다음 코드 스니펫은 PDF의 페이지 범위에서 스트림으로 이미지를 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesRangePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open input PDF
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();

        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new
            FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## 이미지 추출 모드를 사용하여 이미지 추출 (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor) 클래스는 PDF 파일에서 이미지를 추출할 수 있게 해줍니다. Aspose.PDF는 두 가지 추출 모드를 지원합니다. 첫 번째는 PDF 문서에서 실제로 사용된 이미지를 추출하는 ActuallyUsedImage입니다. 두 번째 모드는 PDF 문서의 리소스에 정의된 이미지를 추출하는 [DefinedInResources](https://reference.aspose.com/pdf/ko/net/aspose.pdf/extractimagemode)입니다(기본 추출 모드). 먼저, [PdfExtractor](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode) 속성을 사용하여 이미지 추출 모드를 지정합니다. 그런 다음, 지정한 모드에 따라 모든 이미지를 메모리로 추출하기 위해 [ExtractImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/extractimage) 메서드를 호출합니다. 이미지가 추출되면 [HasNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) 및 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드를 사용하여 해당 이미지를 가져올 수 있습니다. while 루프를 사용하여 모든 추출된 이미지를 반복해야 합니다. 이미지를 디스크에 저장하려면 파일 경로를 인수로 받는 [GetNextImage](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1) 메서드의 오버로드를 호출할 수 있습니다.

다음 코드 스니펫은 ExtractImageMode 옵션을 사용하여 PDF 파일에서 이미지를 추출하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesImageExtractionMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Specify Image Extraction Mode
        //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
        extractor.ExtractImageMode = Aspose.Pdf.ExtractImageMode.DefinedInResources;

        // Extract Images based on Image Extraction Mode
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
        }
    }
}
```

PDF에 텍스트 또는 이미지가 포함되어 있는지 확인하려면 다음 코드 스니펫을 사용하세요:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```