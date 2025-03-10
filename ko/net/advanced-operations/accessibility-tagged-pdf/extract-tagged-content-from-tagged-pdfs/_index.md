---
title: PDF에서 태그가 있는 콘텐츠 추출
linktitle: 태그가 있는 콘텐츠 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/extract-tagged-content-from-tagged-pdfs/
description: 이 문서에서는 Aspose.PDF for .NET을 사용하여 태그가 있는 콘텐츠 PDF 문서를 추출하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Tagged Content from PDF",
    "alternativeHeadline": "Extract Content from Tagged PDFs Effortlessly",
    "abstract": "Aspose.PDF for .NET의 새로운 PDF에서 태그가 있는 콘텐츠 추출 기능을 통해 사용자는 C#을 사용하여 PDF 문서에서 태그가 있는 콘텐츠를 효율적으로 추출하고 조작할 수 있습니다. 이 기능은 문서 구조에 대한 원활한 접근을 제공하여 PDF 접근성과 준수를 향상시키며, 개발자가 태그가 있는 PDF 내에서 텍스트, 이미지 및 메타데이터를 프로그래밍 방식으로 관리할 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extract, Tagged Content, PDF Document, Aspose.PDF, C#, Root Structure, Child Elements, Tagging Images, PDF/UA Compliance, StructureElement",
    "wordcount": "872",
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
    "url": "/net/extract-tagged-content-from-tagged-pdfs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-tagged-content-from-tagged-pdfs/"
    },
    "dateModified": "2022-11-25",
    "description": "이 문서에서는 Aspose.PDF for .NET을 사용하여 태그가 있는 콘텐츠 PDF 문서를 추출하는 방법을 설명합니다."
}
</script>

이 문서에서는 C#을 사용하여 태그가 있는 콘텐츠 PDF 문서를 추출하는 방법을 배웁니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 태그가 있는 PDF 콘텐츠 가져오기

태그가 있는 텍스트가 포함된 PDF 문서의 콘텐츠를 가져오기 위해 Aspose.PDF는 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 [TaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) 속성을 제공합니다.

다음 코드 스니펫은 태그가 있는 텍스트가 포함된 PDF 문서의 콘텐츠를 가져오는 방법을 보여줍니다:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTaggedContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with Tagged PDF
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Work with Tagged PDF content
        // Set Title and Language for Document
        taggedContent.SetTitle("Simple Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        // Save Tagged PDF Document
        document.Save(dataDir + "TaggedPDFContent_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTaggedContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Work with Tagged PDF content
    // Set Title and Language for Document
    taggedContent.SetTitle("Simple Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // Save Tagged PDF Document
    document.Save(dataDir + "TaggedPDFContent_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 루트 구조 가져오기

태그가 있는 PDF 문서의 루트 구조를 가져오기 위해 Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) 인터페이스의 [StructTreeRootElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement) 속성과 [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement)를 제공합니다. 다음 코드 스니펫은 태그가 있는 PDF 문서의 루트 구조를 가져오는 방법을 보여줍니다:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetRootStructure()
{
    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with Tagged PDF
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        // Properties StructTreeRootElement and RootElement are used for access to
        // StructTreeRoot object of pdf document and to root structure element (Document structure element).
        Aspose.Pdf.LogicalStructure.StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetRootStructure()
{
    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with Tagged PDF
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // Properties StructTreeRootElement and RootElement are used for access to
    // StructTreeRoot object of pdf document and to root structure element (Document structure element).
    Aspose.Pdf.LogicalStructure.StructTreeRootElement structTreeRootElement = taggedContent.StructTreeRootElement;
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;
}
```
{{< /tab >}}
{{< /tabs >}}

## 자식 요소 접근하기

태그가 있는 PDF 문서의 자식 요소에 접근하기 위해 Aspose.PDF는 [ElementList](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist) 클래스를 제공합니다. 다음 코드 스니펫은 태그가 있는 PDF 문서의 자식 요소에 접근하는 방법을 보여줍니다:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessChildElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF Document
    using (var document = new Aspose.Pdf.Document(dataDir + "StructureElementsTree.pdf"))
    {
        // Get Content for work with Tagged PDF
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Access to root element(s)
        Aspose.Pdf.LogicalStructure.ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;

        foreach (Aspose.Pdf.LogicalStructure.Element element in elementList)
        {
            if (element is Aspose.Pdf.LogicalStructure.StructureElement)
            {
                var structureElement = element as Aspose.Pdf.LogicalStructure.StructureElement;

                // Get properties
                string title = structureElement.Title;
                string language = structureElement.Language;
                string actualText = structureElement.ActualText;
                string expansionText = structureElement.ExpansionText;
                string alternativeText = structureElement.AlternativeText;
            }
        }

        // Access to child elements of first element in root element
        elementList = taggedContent.RootElement.ChildElements[1].ChildElements;

        foreach (Aspose.Pdf.LogicalStructure.Element element in elementList)
        {
            if (element is Aspose.Pdf.LogicalStructure.StructureElement)
            {
                var structureElement = element as Aspose.Pdf.LogicalStructure.StructureElement;

                // Set properties
                structureElement.Title = "title";
                structureElement.Language = "fr-FR";
                structureElement.ActualText = "actual text";
                structureElement.ExpansionText = "exp";
                structureElement.AlternativeText = "alt";
            }
        }

        // Save Tagged PDF Document
        document.Save(dataDir + "AccessChildElements_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessChildElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF Document
    using var document = new Aspose.Pdf.Document(dataDir + "StructureElementsTree.pdf");

    // Get Content for work with Tagged PDF
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Access to root element(s)
    Aspose.Pdf.LogicalStructure.ElementList elementList = taggedContent.StructTreeRootElement.ChildElements;

    foreach (Aspose.Pdf.LogicalStructure.Element element in elementList)
    {
        if (element is Aspose.Pdf.LogicalStructure.StructureElement)
        {
            var structureElement = element as Aspose.Pdf.LogicalStructure.StructureElement;

            // Get properties
            string title = structureElement.Title;
            string language = structureElement.Language;
            string actualText = structureElement.ActualText;
            string expansionText = structureElement.ExpansionText;
            string alternativeText = structureElement.AlternativeText;
        }
    }

    // Access to child elements of first element in root element
    elementList = taggedContent.RootElement.ChildElements[1].ChildElements;

    foreach (Aspose.Pdf.LogicalStructure.Element element in elementList)
    {
        if (element is Aspose.Pdf.LogicalStructure.StructureElement)
        {
            var structureElement = element as Aspose.Pdf.LogicalStructure.StructureElement;

            // Set properties
            structureElement.Title = "title";
            structureElement.Language = "fr-FR";
            structureElement.ActualText = "actual text";
            structureElement.ExpansionText = "exp";
            structureElement.AlternativeText = "alt";
        }
    }

    // Save Tagged PDF Document
    document.Save(dataDir + "AccessChildElements_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 기존 PDF에서 이미지 태깅하기

기존 PDF 문서에서 이미지를 태깅하기 위해 Aspose.PDF는 [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement) 클래스의 [FindElements](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1) 메서드를 제공합니다. [FigureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement) 클래스의 [AlternativeText](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext) 속성을 사용하여 그림에 대한 대체 텍스트를 추가할 수 있습니다.

다음 코드 스니펫은 기존 PDF 문서에서 이미지를 태깅하는 방법을 보여줍니다:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TagImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document1 = new Aspose.Pdf.Document(dataDir + "TH.pdf"))
    {
        // Gets tagged content and root structure element
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document1.TaggedContent;
        Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

        // Set title for tagged PDF document
        taggedContent.SetTitle("Document with images");

        foreach (Aspose.Pdf.LogicalStructure.FigureElement figureElement in rootElement.FindElements<Aspose.Pdf.LogicalStructure.FigureElement>(true))
        {
            // Set AlternativeText for Figure
            figureElement.AlternativeText = "Figure alternative text (technique 2)";

            // Create and Set BBox Attribute
            var bboxAttribute = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.BBox);
            bboxAttribute.SetRectangleValue(new Aspose.Pdf.Rectangle(0.0, 0.0, 100.0, 100.0));

            Aspose.Pdf.LogicalStructure.StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);
            figureLayoutAttributes.SetAttribute(bboxAttribute);
        }

        // Move Span Element into Paragraph (find wrong span and paragraph in first TD)
        Aspose.Pdf.LogicalStructure.TableElement tableElement = rootElement.FindElements<Aspose.Pdf.LogicalStructure.TableElement>(true)[0];
        Aspose.Pdf.LogicalStructure.SpanElement spanElement = tableElement.FindElements<Aspose.Pdf.LogicalStructure.SpanElement>(true)[0];
        Aspose.Pdf.LogicalStructure.TableTDElement firstTdElement = tableElement.FindElements<Aspose.Pdf.LogicalStructure.TableTDElement>(true)[0];
        Aspose.Pdf.LogicalStructure.ParagraphElement paragraph = firstTdElement.FindElements<Aspose.Pdf.LogicalStructure.ParagraphElement>(true)[0];

        // Move Span Element into Paragraph
        spanElement.ChangeParentElement(paragraph);

        // Save PDF document
        document1.Save(dataDir + "TH_out.pdf");
    }

    // Check PDF/UA Compliance for out document
    using (var document2 = new Aspose.Pdf.Document(dataDir + "TH_out.pdf"))
    {
        bool isPdfUaCompliance = document2.Validate(dataDir + "TH_out.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
        Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void TagImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document1 = new Aspose.Pdf.Document(dataDir + "TH.pdf");

    // Gets tagged content and root structure element
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document1.TaggedContent;
    Aspose.Pdf.LogicalStructure.StructureElement rootElement = taggedContent.RootElement;

    // Set title for tagged PDF document
    taggedContent.SetTitle("Document with images");

    foreach (Aspose.Pdf.LogicalStructure.FigureElement figureElement in rootElement.FindElements<Aspose.Pdf.LogicalStructure.FigureElement>(true))
    {
        // Set AlternativeText for Figure
        figureElement.AlternativeText = "Figure alternative text (technique 2)";

        // Create and Set BBox Attribute
        var bboxAttribute = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.BBox);
        bboxAttribute.SetRectangleValue(new Aspose.Pdf.Rectangle(0.0, 0.0, 100.0, 100.0));

        Aspose.Pdf.LogicalStructure.StructureAttributes figureLayoutAttributes = figureElement.Attributes.GetAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);
        figureLayoutAttributes.SetAttribute(bboxAttribute);
    }

    // Move Span Element into Paragraph (find wrong span and paragraph in first TD)
    Aspose.Pdf.LogicalStructure.TableElement tableElement = rootElement.FindElements<Aspose.Pdf.LogicalStructure.TableElement>(true)[0];
    Aspose.Pdf.LogicalStructure.SpanElement spanElement = tableElement.FindElements<Aspose.Pdf.LogicalStructure.SpanElement>(true)[0];
    Aspose.Pdf.LogicalStructure.TableTDElement firstTdElement = tableElement.FindElements<Aspose.Pdf.LogicalStructure.TableTDElement>(true)[0];
    Aspose.Pdf.LogicalStructure.ParagraphElement paragraph = firstTdElement.FindElements<Aspose.Pdf.LogicalStructure.ParagraphElement>(true)[0];

    // Move Span Element into Paragraph
    spanElement.ChangeParentElement(paragraph);

    // Save PDF document
    document1.Save(dataDir + "TH_out.pdf");

    // Check PDF/UA Compliance for out document
    using var document2 = new Aspose.Pdf.Document(dataDir + "TH_out.pdf");

    bool isPdfUaCompliance = document2.Validate(dataDir + "TH_out.pdf", Aspose.Pdf.PdfFormat.PDF_UA_1);
    Console.WriteLine(String.Format("PDF/UA compliance: {0}", isPdfUaCompliance));
}
```
{{< /tab >}}
{{< /tabs >}}

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