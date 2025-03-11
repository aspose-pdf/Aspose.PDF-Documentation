---
title: 페이지 속성 가져오기 및 설정
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /ko/net/get-and-set-page-properties/
description: Aspose.PDF for .NET를 사용하여 PDF 문서의 페이지 속성을 가져오고 설정하는 방법을 배우고, 사용자 정의 문서 형식을 허용합니다.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Set Page Properties",
    "alternativeHeadline": "Manage PDF Page Properties with Ease",
    "abstract": "Aspose.PDF for .NET의 페이지 속성 가져오기 및 설정 기능은 개발자가 PDF 페이지 속성에 쉽게 접근하고 조작할 수 있도록 합니다. 이 기능을 통해 사용자는 페이지 수 및 색상 유형, 미디어 박스, 트림 박스와 같은 특정 속성과 같은 중요한 정보를 몇 줄의 코드로 검색할 수 있습니다. .NET 애플리케이션에서 효율적인 PDF 조작을 위해 이 강력한 기능을 활용하여 오늘 PDF 문서 관리 기능을 향상시키십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1117",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

Aspose.PDF for .NET는 .NET 애플리케이션에서 PDF 파일의 페이지 속성을 읽고 설정할 수 있게 해줍니다. 이 섹션에서는 PDF 파일의 페이지 수를 가져오고, 색상과 같은 PDF 페이지 속성에 대한 정보를 가져오고, 페이지 속성을 설정하는 방법을 보여줍니다. 제공된 예제는 C#로 되어 있지만 VB.NET과 같은 다른 .NET 언어를 사용하여 동일한 작업을 수행할 수 있습니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

## PDF 파일의 페이지 수 가져오기

문서 작업을 할 때, 문서에 몇 페이지가 포함되어 있는지 알고 싶어하는 경우가 많습니다. Aspose.PDF를 사용하면 두 줄의 코드로 해결할 수 있습니다.

PDF 파일의 페이지 수를 가져오려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 PDF 파일을 엽니다.
1. 그런 다음 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션의 Count 속성(문서 객체에서)을 사용하여 문서의 총 페이지 수를 가져옵니다.

다음 코드 조각은 PDF 파일의 페이지 수를 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetNumberOfPagesInAPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetNumberofPages.pdf"))
    {
        // Get page count
        System.Console.WriteLine("Page Count : {0}", document.Pages.Count);
    }
}
```

### 문서를 저장하지 않고 페이지 수 가져오기

때때로 우리는 PDF 파일을 즉석에서 생성하며, PDF 파일 생성 중에 시스템이나 스트림에 파일을 저장하지 않고 페이지 수를 가져와야 하는 요구 사항(목차 생성 등)이 발생할 수 있습니다. 이러한 요구 사항을 충족하기 위해 Document 클래스에 [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) 메서드가 도입되었습니다. 문서를 저장하지 않고 페이지 수를 가져오는 단계를 보여주는 다음 코드 조각을 살펴보십시오.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPageCountWithoutSavingTheDocument()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create loop instance
        for (var i = 0; i < 300; i++)
        {
            // Add TextFragment to paragraphs collection of page object
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Pages count test"));
        }
        // Process the paragraphs in PDF file to get accurate page count
        document.ProcessParagraphs();
        // Print number of pages in document
        Console.WriteLine("Number of pages in document = " + document.Pages.Count);
    }
}
```

## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 블리드 박스, 크롭 박스 및 트림 박스와 같은 여러 속성이 있습니다. Aspose.PDF를 사용하면 이러한 속성에 접근할 수 있습니다.

### **페이지 속성 이해하기: Artbox, BleedBox, CropBox, MediaBox, TrimBox 및 Rect 속성의 차이점**

- **미디어 박스**: 미디어 박스는 가장 큰 페이지 박스입니다. 이는 문서가 PostScript 또는 PDF로 인쇄될 때 선택된 페이지 크기(예: A4, A5, 미국 레터 등)에 해당합니다. 즉, 미디어 박스는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **블리드 박스**: 문서에 블리드가 있는 경우 PDF에도 블리드 박스가 있습니다. 블리드는 페이지의 가장자리를 넘어 확장된 색상(또는 아트워크)의 양입니다. 이는 문서가 인쇄되고 크기가 조정될 때(“트림”) 잉크가 페이지의 가장자리까지 가도록 보장하는 데 사용됩니다. 페이지가 잘못 잘리더라도 - 트림 마크에서 약간 벗어나 잘리더라도 - 페이지에 흰색 가장자리가 나타나지 않습니다.
- **트림 박스**: 트림 박스는 인쇄 및 트림 후 문서의 최종 크기를 나타냅니다.
- **아트 박스**: 아트 박스는 문서의 페이지에 실제 내용 주위에 그려진 박스입니다. 이 페이지 박스는 다른 애플리케이션에서 PDF 문서를 가져올 때 사용됩니다.
- **크롭 박스**: 크롭 박스는 Adobe Acrobat에서 PDF 문서가 표시되는 “페이지” 크기입니다. 일반 보기에서는 Adobe Acrobat에서 크롭 박스의 내용만 표시됩니다.
  이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **Page.Rect**: 미디어 박스와 드롭 박스의 교차점(일반적으로 보이는 사각형)입니다. 아래 그림은 이러한 속성을 설명합니다.

자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

### **페이지 속성 접근하기**

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스는 특정 PDF 페이지와 관련된 모든 속성을 제공합니다. PDF 파일의 모든 페이지는 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션에 포함되어 있습니다.

거기에서 인덱스를 사용하여 개별 Page 객체에 접근하거나 foreach 루프를 사용하여 컬렉션을 반복하여 모든 페이지를 가져올 수 있습니다. 개별 페이지에 접근하면 해당 속성을 가져올 수 있습니다. 다음 코드 조각은 페이지 속성을 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessingPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetProperties.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Get page properties
        System.Console.WriteLine("ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.ArtBox.Height, pdfPage.ArtBox.Width, pdfPage.ArtBox.LLX,
            pdfPage.ArtBox.LLY, pdfPage.ArtBox.URX, pdfPage.ArtBox.URY);
        System.Console.WriteLine("BleedBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.BleedBox.Height, pdfPage.BleedBox.Width, pdfPage.BleedBox.LLX,
            pdfPage.BleedBox.LLY, pdfPage.BleedBox.URX, pdfPage.BleedBox.URY);
        System.Console.WriteLine("CropBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.CropBox.Height, pdfPage.CropBox.Width, pdfPage.CropBox.LLX,
            pdfPage.CropBox.LLY, pdfPage.CropBox.URX, pdfPage.CropBox.URY);
        System.Console.WriteLine("MediaBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.MediaBox.Height, pdfPage.MediaBox.Width, pdfPage.MediaBox.LLX,
            pdfPage.MediaBox.LLY, pdfPage.MediaBox.URX, pdfPage.MediaBox.URY);
        System.Console.WriteLine("TrimBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.TrimBox.Height, pdfPage.TrimBox.Width, pdfPage.TrimBox.LLX,
            pdfPage.TrimBox.LLY, pdfPage.TrimBox.URX, pdfPage.TrimBox.URY);
        System.Console.WriteLine("Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.Rect.Height, pdfPage.Rect.Width, pdfPage.Rect.LLX, pdfPage.Rect.LLY,
            pdfPage.Rect.URX, pdfPage.Rect.URY);
        System.Console.WriteLine("Page Number : {0}", pdfPage.Number);
        System.Console.WriteLine("Rotate : {0}", pdfPage.Rotate);
    }
}
```

## PDF 파일의 특정 페이지 가져오기

Aspose.PDF를 사용하면 [PDF를 개별 페이지로 분할](/pdf/ko/net/split-pdf-document/)하고 이를 PDF 파일로 저장할 수 있습니다. PDF 파일에서 특정 페이지를 가져와 새 PDF로 저장하는 것은 매우 유사한 작업입니다: 원본 문서를 열고, 페이지에 접근하고, 새 문서를 만들고, 페이지를 추가합니다.

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)은 PDF 파일의 페이지를 보유합니다. 이 컬렉션에서 특정 페이지를 가져오려면:

1. Pages 속성을 사용하여 페이지 인덱스를 지정합니다.
1. 새 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체를 새 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체에 추가합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력을 저장합니다.

다음 코드 조각은 PDF 파일에서 특정 페이지를 가져와 새 파일로 저장하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAParticularPageOfThePdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get particular page
        var pdfPage = document.Pages[2];
        // Save the page as PDF file
        using (var newDocument = new Aspose.Pdf.Document())
        {
            newDocument.Pages.Add(pdfPage);
            // Save PDF document
            newDocument.Save(dataDir + "GetParticularPage_out.pdf");
        }
    }
}
```

## 페이지 색상 결정하기

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스는 PDF 문서의 특정 페이지와 관련된 속성을 제공하며, 페이지가 사용하는 색상 유형 - RGB, 흑백, 그레이스케일 또는 정의되지 않음 - 을 포함합니다.

PDF 파일의 모든 페이지는 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션에 포함되어 있습니다. ColorType 속성은 페이지의 요소 색상을 지정합니다. 특정 PDF 페이지의 색상 정보를 가져오거나 결정하려면 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) 속성을 사용하십시오.

다음 코드 조각은 PDF 파일의 개별 페이지를 반복하여 색상 정보를 가져오는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeterminePageColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through all the page of PDF file
        for (var pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Get the color type information for particular PDF page
            Aspose.Pdf.ColorType pageColorType = document.Pages[pageCount].ColorType;
            switch (pageColorType)
            {
                case Aspose.Pdf.ColorType.BlackAndWhite:
                    Console.WriteLine("Page # -" + pageCount + " is Black and white..");
                    break;
                case Aspose.Pdf.ColorType.Grayscale:
                    Console.WriteLine("Page # -" + pageCount + " is Gray Scale...");
                    break;
                case Aspose.Pdf.ColorType.Rgb:
                    Console.WriteLine("Page # -" + pageCount + " is RGB..", pageCount);
                    break;
                case Aspose.Pdf.ColorType.Undefined:
                    Console.WriteLine("Page # -" + pageCount + " Color is undefined..");
                    break;
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