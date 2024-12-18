---
title: Extract Tagged Content from PDF
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /net/extract-tagged-content-from-tagged-pdfs/
description: This article explains how to extract tagged content PDF document using Aspose.PDF for .NET
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
    "abstract": "The new Extract Tagged Content from PDF feature in Aspose.PDF for .NET allows users to efficiently extract and manipulate tagged content from PDF documents using C#. This functionality enhances PDF accessibility and compliance by providing seamless access to the document structure, enabling developers to programmatically manage text, images, and metadata within tagged PDFs",
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
    "description": "This article explains how to extract tagged content PDF document using Aspose.PDF for .NET"
}
</script>

In this article you will learn how to to extract tagged content PDF document using C#.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Getting Tagged PDF Content

In order to get content of PDF Document with Tagged Text, Aspose.PDF offers [TaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/taggedcontent) property of [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class.

Following code snippet shows how to get content of a PDF document with Tagged Text:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetTaggedContent()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create Pdf Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with Tagged PDF
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Work with Tagged PDF content

        // Set Title and Language for Document
        taggedContent.SetTitle("Simple Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        // Save Tagged PDF Document
        document.Save(dataDir + "TaggedPDFContent.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetTaggedContent()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Work with Tagged PDF content

    // Set Title and Language for Document
    taggedContent.SetTitle("Simple Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    // Save Tagged PDF Document
    document.Save(dataDir + "TaggedPDFContent.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Getting Root Structure

In order to get the root structure of Tagged PDF Document, Aspose.PDF offers [StructTreeRootElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement) property of [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) interface and [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). Following code snippet shows how to get the root structure of Tagged PDF Document:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void GetRootStructure()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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

## Accessing Child Elements

In order to access child elements of a Tagged PDF Document, Aspose.PDF offers [ElementList](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/elementlist) class. Following code snippet shows how to access child elements of a Tagged PDF Document:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AccessChildElements()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
        document.Save(dataDir + "AccessChildElements.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void AccessChildElements()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

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
    document.Save(dataDir + "AccessChildElements.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Tagging Images in Existing PDF

In order to tag images in existing PDF document, Aspose.PDF offers [FindElements](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/findelements/_1) method of [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement) class. You can add alternative text for figures using [AlternativeText](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext) property of [FigureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/figureelement) class.

Following code snippet shows how to tag images in existing PDF document:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void TagImages()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    string inFile = dataDir + "TH.pdf";
    string outFile = dataDir + "TH_out.pdf";
    string logFile = dataDir + "TH_out.xml";

    // Open document
    using (var document1 = new Aspose.Pdf.Document(inFile))
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

        // Save document
        document1.Save(outFile);
    }

    // Checking PDF/UA Compliance for out document
    using (var document2 = new Aspose.Pdf.Document(outFile))
    {
        bool isPdfUaCompliance = document2.Validate(logFile, Aspose.Pdf.PdfFormat.PDF_UA_1);
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
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    string inFile = dataDir + "TH.pdf";
    string outFile = dataDir + "TH_out.pdf";
    string logFile = dataDir + "TH_out.xml";

    // Open document
    using var document1 = new Aspose.Pdf.Document(inFile);

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

    // Save document
    document1.Save(outFile);

    // Checking PDF/UA Compliance for out document
    using var document2 = new Aspose.Pdf.Document(outFile);

    bool isPdfUaCompliance = document2.Validate(logFile, Aspose.Pdf.PdfFormat.PDF_UA_1);
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
