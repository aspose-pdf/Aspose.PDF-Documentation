---
title: Извлечение векторных данных из PDF-файла с помощью C#
linktitle: Извлечение векторных данных из PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ru/net/extract-vector-data-from-pdf/
description: С помощью Aspose.PDF можно легко извлечь векторные данные из PDF-файла. Можно получить векторные данные (путь, многоугольник, полилинию), такие как положение, цвет, ширина линии и т. д.
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
    "abstract": "Aspose.PDF для .NET теперь предлагает инновационную функцию, которая позволяет пользователям легко извлекать векторные данные из PDF-файлов. Эта функциональность включает детальный доступ к графическим элементам, таким как контуры и многоугольники, а также к их свойствам, таким как положение, цвет и ширина линии, что даёт разработчикам возможность эффективно работать с векторной графикой в своих приложениях.",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Доступ к векторным данным из PDF-документа

Начиная с версии 24.2 библиотека Aspose.PDF for .NET позволяет извлекать векторные данные из PDF-файла.
Следующий фрагмент кода создаёт новый объект Document, используя некоторые входные данные, инициализирует GraphicsAbsorber (GraphicsAbsorber возвращает векторные данные) для обработки графических элементов, а затем переходит ко второй странице документа для извлечения и анализа этих элементов.
Он извлекает различные свойства второго графического элемента, такие как связанные с ним операторы, прямоугольник и положение.

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

## Извлечение векторных данных из PDF-документа

Для извлечения векторных данных из PDF мы можем использовать SVG-экстрактор:

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

### Извлечь все подпути к изображениям отдельно

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

### Извлечь список элементов в одно изображение

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

### Извлечь один элемент

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