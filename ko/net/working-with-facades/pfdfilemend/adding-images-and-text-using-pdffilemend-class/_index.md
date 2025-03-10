---
title: 이미지 및 텍스트 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/adding-images-and-text-using-pdffilemend-class/
description: 이 섹션에서는 PdfFileMend 클래스를 사용하여 이미지와 텍스트를 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Images and Text",
    "alternativeHeadline": "Enhance PDF by Adding Images and Text Precisely",
    "abstract": "새로운 PdfFileMend 클래스를 사용하여 기존 PDF 내의 지정된 위치에 이미지와 텍스트를 손쉽게 추가하여 PDF 문서를 향상시킵니다. 직관적인 AddImage 및 AddText 메서드를 활용하여 다양한 이미지 형식과 서식 있는 텍스트를 원활하게 통합하여 배치 및 페이지 선택의 정확성을 보장합니다. 이미지 오버레이 및 텍스트 래핑을 사용자 정의할 수 있는 기능으로 PDF 조작 작업을 간소화하여 문서를 시각적으로 매력적이고 유익하게 만듭니다.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 클래스는 기존 PDF 문서의 지정된 위치에 이미지와 텍스트를 추가하는 데 도움을 줄 수 있습니다. 이 클래스는 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 및 [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index)라는 두 가지 메서드를 제공합니다. [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 메서드는 JPG, GIF, PNG 및 BMP 형식의 이미지를 추가할 수 있습니다. [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) 메서드는 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 클래스의 인수를 받아 기존 PDF 파일에 추가합니다. 이미지는 좌하단 및 우상단 좌표로 지정된 사각형 영역에 추가될 수 있습니다. 이미지를 추가할 때 이미지 파일 경로 또는 이미지 파일의 스트림을 지정할 수 있습니다. 이미지 또는 텍스트를 추가할 페이지 번호를 지정하기 위해 이 두 메서드는 페이지 번호 인수를 제공합니다. 따라서 지정된 위치뿐만 아니라 지정된 페이지에도 이미지와 텍스트를 추가할 수 있습니다.

이미지는 PDF 문서 내용의 중요한 부분입니다. 기존 PDF 파일에서 이미지를 조작하는 것은 PDF 파일을 다루는 사람들에게 일반적인 요구 사항입니다. 이 기사에서는 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)를 사용하여 기존 PDF 파일에서 이미지를 조작하는 방법을 살펴보겠습니다. [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)의 모든 이미지 관련 작업이 이 기사에 통합되어 있습니다.

## 구현 세부정보

[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)는 기존 PDF 파일에 새로운 이미지를 추가할 수 있게 해줍니다. 기존 이미지를 교체하거나 제거할 수도 있습니다. PDF 파일을 이미지로 변환할 수도 있습니다. 각 개별 페이지를 하나의 이미지로 변환하거나 전체 PDF 파일을 하나의 이미지로 변환할 수 있습니다. JPEG, BMP, PNG 및 TIFF 등의 형식을 지원합니다. PDF 파일에서 이미지를 추출할 수도 있습니다. 이러한 작업을 구현하기 위해 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)의 네 가지 클래스를 사용할 수 있습니다: [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 및 [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## 이미지 작업

이 섹션에서는 이러한 이미지 작업을 자세히 살펴보겠습니다. 관련 클래스 및 메서드의 사용을 보여주는 코드 스니펫도 확인하겠습니다. 먼저, 기존 PDF 파일에 이미지를 추가하는 방법을 살펴보겠습니다. [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 클래스의 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) 메서드를 사용하여 새 이미지를 추가할 수 있습니다. 이 메서드를 사용하면 이미지를 추가할 페이지 번호뿐만 아니라 이미지의 위치도 지정할 수 있습니다.

## 기존 PDF 파일에 이미지 추가 (Facades)

[PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) 클래스의 [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) 메서드를 사용할 수 있습니다. [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) 메서드는 추가할 이미지, 이미지를 추가할 페이지 번호 및 좌표 정보를 요구합니다. 그 후, [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 예제에서는 imageStream을 사용하여 페이지에 이미지를 추가합니다:

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

![이미지 추가](/pdf/net/images/add_image1.png)

[CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1)의 도움으로 한 이미지를 다른 이미지 위에 겹쳐 놓을 수 있습니다:

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

![이미지 추가](/pdf/net/images/add_image2.png)

PDF 파일에 이미지를 저장하는 방법은 여러 가지가 있습니다. 다음 예제에서 그 중 하나를 보여드리겠습니다:

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

## 기존 PDF 파일에 텍스트 추가 (facades)

여러 가지 방법으로 텍스트를 추가할 수 있습니다. 첫 번째 방법을 고려해 보겠습니다. [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)를 가져와 페이지에 추가합니다. 그런 다음 좌하단 모서리의 좌표를 지정하고 페이지에 텍스트를 추가합니다.

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

어떻게 보이는지 확인해 보세요:

![텍스트 추가](/pdf/net/images/add_text.png)

두 번째 방법은 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext)를 추가하는 것입니다. 추가로, 텍스트가 들어가야 할 사각형을 지정합니다.

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

세 번째 예제는 지정된 페이지에 텍스트를 추가할 수 있는 기능을 제공합니다. 예제에서는 문서의 1페이지와 3페이지에 캡션을 추가해 보겠습니다.

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