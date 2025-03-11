---
title: PDF 파일에서 벡터 데이터 추출하기 C#
linktitle: PDF에서 벡터 데이터 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ko/net/extract-vector-data-from-pdf/
description: Aspose.PDF는 PDF 파일에서 벡터 데이터를 쉽게 추출할 수 있게 해줍니다. 위치, 색상, 선 너비 등과 같은 벡터 데이터(경로, 다각형, 폴리라인)를 얻을 수 있습니다.
lastmod: "2024-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Vector Data from a PDF file using C#",
    "alternativeHeadline": "Effortless Vector Data Extraction from PDF with C#",
    "abstract": "Aspose.PDF for .NET는 사용자가 PDF 파일에서 벡터 데이터를 원활하게 추출할 수 있는 혁신적인 기능을 제공합니다. 이 기능은 경로 및 다각형과 같은 그래픽 요소에 대한 자세한 접근을 포함하며, 위치, 색상 및 선 너비와 같은 속성을 통해 개발자가 애플리케이션에서 벡터 그래픽을 효율적으로 처리할 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "361",
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
    "url": "/net/extract-vector-data-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-vector-data-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## PDF 문서에서 벡터 데이터 접근

24.2 릴리스 이후, Aspose.PDF for .NET 라이브러리는 PDF 파일에서 벡터 데이터 추출을 허용합니다.
다음 코드 스니펫은 일부 입력 데이터를 사용하여 새로운 Document 객체를 생성하고, 그래픽 요소를 처리하기 위해 'GraphicsAbsorber'(GraphicsAbsorber는 벡터 데이터를 반환합니다)를 초기화한 다음, 문서의 두 번째 페이지를 방문하여 이러한 요소를 추출하고 분석합니다.
두 번째 그래픽 요소의 관련 연산자, 사각형 및 위치와 같은 다양한 속성을 검색합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ProcessGraphicsInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate a new GraphicsAbsorber object to process graphic elements
        using (var grAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Visit the second page of the document to extract graphic elements
            grAbsorber.Visit(document.Pages[1]);

            // Retrieve the list of graphic elements from the GraphicsAbsorber
            var elements = grAbsorber.Elements;

            // Access the operators associated with the second graphic element
            var operations = elements[1].Operators;

            // Retrieve the rectangle associated with the second graphic element
            var rectangle = elements[1].Rectangle;

            // Get the position of the second graphic element
            var position = elements[1].Position;
        }
    }
}
```

## PDF 문서에서 벡터 데이터 추출

PDF에서 벡터 데이터를 추출하기 위해 SVG 추출기를 사용할 수 있습니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveVectorGraphicsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Save vector graphics from the first page to an SVG file
        document.Pages[1].TrySaveVectorGraphics(dataDir + "VectorGraphics_out.svg");
    }
}
```

### 모든 서브 경로를 개별 이미지로 추출

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAllSubpathsToImagesSeparately()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Path to the directory where SVGs will be saved
    var svgDirPath = dataDir + "SvgOutput/";

    // Create extraction options
    var options = new Aspose.Pdf.Vector.SvgExtractionOptions
    {
        ExtractEverySubPathToSvg = true
    };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Get the first page of the document
        var page = document.Pages[1];

        // Create SVG extractor
        var extractor = new Aspose.Pdf.Vector.SvgExtractor(options);
        // Extract SVGs from the page
        extractor.Extract(page, svgDirPath);
    }
}
```

### 요소 목록을 단일 이미지로 추출

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractListOfElementsToSingleImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Initialize the list of graphic elements
    var elements = new List<Aspose.Pdf.Vector.GraphicElement>();

    // Example: Fill elements list with needed graphic elements (implement your logic here)

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Get the first page of the document
        var page = document.Pages[1];

        // Use SvgExtractor to extract SVGs
        var svgExtractor = new Aspose.Pdf.Vector.SvgExtractor();

        // Extract SVGs from graphic elements on the page
        svgExtractor.Extract(elements, page, Path.Combine(dataDir, "SvgOutput", "VectorGraphics_out.svg"));
    }
}
```

### 단일 요소 추출

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSingleElement()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();


    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "VectorGraphics.pdf"))
    {
        // Create a GraphicsAbsorber object to extract graphic elements
        var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber();

        // Get the first page of the document
        var page = document.Pages[1];

        // Process the page to extract graphic elements
        graphicsAbsorber.Visit(page);

        // Extract the graphic element (XFormPlacement) and save it as SVG
        var xFormPlacement = graphicsAbsorber.Elements[1] as Aspose.Pdf.Vector.XFormPlacement;
        xFormPlacement.Elements[2].SaveToSvg(Path.Combine(dataDir, "SvgOutput", "VectorGraphics_out.svg"));
    }
}
```