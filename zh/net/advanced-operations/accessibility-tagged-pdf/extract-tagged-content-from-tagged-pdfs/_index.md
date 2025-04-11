---
title: 从PDF中提取标记内容
linktitle: 提取标记内容
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/extract-tagged-content-from-tagged-pdfs/
description: 本文解释了如何使用Aspose.PDF for .NET提取标记内容的PDF文档
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
    "abstract": "Aspose.PDF for .NET中的新提取标记内容功能允许用户使用C#高效提取和操作PDF文档中的标记内容。此功能通过提供对文档结构的无缝访问，增强了PDF的可访问性和合规性，使开发人员能够以编程方式管理标记PDF中的文本、图像和元数据。",
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
    "description": "本文解释了如何使用Aspose.PDF for .NET提取标记内容的PDF文档"
}
</script>

在本文中，您将学习如何使用C#提取标记内容的PDF文档。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库。

## 获取标记PDF内容

为了获取带有标记文本的PDF文档内容，Aspose.PDF提供了[Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document)类的[TaggedContent](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/properties/taggedcontent)属性。

以下代码片段演示了如何获取带有标记文本的PDF文档内容：

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

## 获取根结构

为了获取标记PDF文档的根结构，Aspose.PDF提供了[ITaggedContent](https://reference.aspose.com/pdf/zh/net/aspose.pdf.tagged/itaggedcontent)接口的[StructTreeRootElement](https://reference.aspose.com/pdf/zh/net/aspose.pdf.tagged/itaggedcontent/properties/structtreerootelement)属性和[StructureElement](https://reference.aspose.com/pdf/zh/net/aspose.pdf.logicalstructure/structureelement)。以下代码片段演示了如何获取标记PDF文档的根结构：

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

## 访问子元素

为了访问标记PDF文档的子元素，Aspose.PDF提供了[ElementList](https://reference.aspose.com/pdf/zh/net/aspose.pdf.logicalstructure/elementlist)类。以下代码片段演示了如何访问标记PDF文档的子元素：

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

## 在现有PDF中标记图像

为了在现有PDF文档中标记图像，Aspose.PDF提供了[StructureElement](https://reference.aspose.com/pdf/zh/net/aspose.pdf.logicalstructure/structureelement)类的[FindElements](https://reference.aspose.com/pdf/zh/net/aspose.pdf.logicalstructure/element/methods/findelements/_1)方法。您可以使用[FigureElement](https://reference.aspose.com/pdf/zh/net/aspose.pdf.logicalstructure/figureelement)类的[AlternativeText](https://reference.aspose.com/pdf/zh/net/aspose.pdf.logicalstructure/structureelement/properties/alternativetext)属性为图形添加替代文本。

以下代码片段演示了如何在现有PDF文档中标记图像：

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