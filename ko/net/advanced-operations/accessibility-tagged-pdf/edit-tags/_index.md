---
title: PDF 파일 태그 편집
linktitle: 태그 편집
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/edit-pdf-file-tags/
description: 이 문서에서는 Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서의 태그를 편집하는 방법을 설명합니다.
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Edit PDF File Tags",
    "alternativeHeadline": "Programmatically edit PDF file tags using Aspose.PDF",
    "abstract": "Aspose.PDF for .NET은 이제 태그가 있는 PDF 요소에 대한 세밀한 제어를 제공합니다. 새로운 메서드를 통해 개발자는 PDF 논리 구조 내에서 태그를 직접 추가, 제거 및 수정할 수 있어 접근성 준수를 보장합니다. 이는 태그가 있는 PDF를 조작하는 라이브러리 기능을 향상시키면서 접근성 기능을 유지합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Edit PDF File Tags, Aspose.PDF for .NET, Tagged PDFs, Accessibility, WCAG,  PDF Tag Editing,  Aspose.Pdf.LogicalStructure.Element,  Add PDF Tags, Edit PDF Tags",
    "wordcount": "1075",
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
    "url": "/net/edit-pdf-file-tags/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/edit-pdf-file-tags/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

태그가 있는 PDF는 각 요소(텍스트, 이미지 및 링크 등)에 태그를 지정하여 접근성을 보장하도록 설계되었습니다. 이러한 PDF를 편집할 때는 접근성 표준(WCAG 등)을 준수하기 위해 이러한 태그를 유지하는 것이 중요합니다.

Aspose.PDF for .NET과 같은 도구는 태그가 있는 콘텐츠를 처리하기 위한 강력한 기능을 제공하지만, 문서의 구조와 접근성을 유지하는 데 주의해야 합니다. 이미지를 위한 대체 텍스트를 체계적으로 추가하거나 단락을 형식화함으로써 태그가 있는 PDF는 접근 가능하고 사용자 친화적으로 유지됩니다.

24.7 릴리스 이후, 태그가 있는 PDF 편집의 일환으로 **Aspose.Pdf.LogicalStructure.Element**에 메서드가 추가되었습니다:

- 태그(이미지, 텍스트 및 링크와 같은 특정 연산자에 태그 추가).
- InsertChild.
- RemoveChild.
- ClearChilds.

이러한 메서드를 사용하면 PDF 파일 태그를 편집할 수 있습니다. 예를 들어:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EditTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "EditTags.pdf"))
    {
        // Get first page 
        var page = document.Pages[1];
        // The marked content operator on page for the image.
        Aspose.Pdf.Operators.BDC imageBdc = null;
        // The marked content operator on page for the text.
        Aspose.Pdf.Operators.BDC text1BDC = null;
        // The marked content operator on page for the link1.
        Aspose.Pdf.Operators.BDC link1Bdc = null;
        // The marked content operator on page for the link2.
        Aspose.Pdf.Operators.BDC link2Bdc = null;
        // The marked content operator on page for the Hello text.
        Aspose.Pdf.Operators.BDC helloBdc = null;
        // Find the marked content operators for the elements on the page.
        for (int i = 1; i <= page.Contents.Count; i++)
        {
            Aspose.Pdf.Operator op = page.Contents[i];
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                // The text operator with marked content id = 0 was found.
                if (bdc.Properties.MCID == 0)
                {
                    helloBdc = bdc;
                }
            }

            var doXobj = op as Aspose.Pdf.Operators.Do;
            if (doXobj != null)
            {
                // Wrap the image XObject with makred content operator.
                imageBdc = new Aspose.Pdf.Operators.BDC("Figure");
                page.Contents.Insert(i - 2, imageBdc);
                i++;
                page.Contents.Insert(i + 1, new Aspose.Pdf.Operators.EMC());
                i++;
            }

            var tx = op as Aspose.Pdf.Operators.TextShowOperator;
            if (tx != null)
            {
                // Wrap the text operator on page with makred content operator.
                if (tx.Text.Contains("efter Ukendt forfatter er licenseret under"))
                {
                    text1BDC = new Aspose.Pdf.Operators.BDC("P");
                    page.Contents.Insert(i - 1, text1BDC);
                    i++;
                    page.Contents.Insert(i + 1, new Aspose.Pdf.Operators.EMC());
                    i++;
                }
                // Wrap the text operator on page with makred content operator.
                if (tx.Text.Contains("CC"))
                {
                    link1Bdc = new Aspose.Pdf.Operators.BDC("Link");
                    page.Contents.Insert(i - 1, link1Bdc);
                    i++;
                    page.Contents.Insert(i + 1, new Aspose.Pdf.Operators.EMC());
                    i++;
                }
                // Wrap the text operator on page with makred content operator.
                if (tx.Text.Contains("Dette billede"))
                {
                    link2Bdc = new Aspose.Pdf.Operators.BDC("Link");
                    page.Contents.Insert(i - 1, link2Bdc);
                    i++;
                    page.Contents.Insert(i + 1, new Aspose.Pdf.Operators.EMC());
                    i++;
                }
            }
        }

        Aspose.Pdf.Tagged.ITaggedContent tagged = document.TaggedContent;

        // Find exist struct element in document.
        Aspose.Pdf.LogicalStructure.Element helloParagraph = tagged.RootElement.ChildElements[1];

        // Clear the subtree of an existing structure tree element.
        helloParagraph.ClearChilds();

        // Tag paragraph struct element to text on page.
        Aspose.Pdf.LogicalStructure.MCRElement helloMCR = helloParagraph.Tag(helloBdc);

        // Get the struct element attributes.
        Aspose.Pdf.LogicalStructure.StructureAttributes helloAttrs = helloMCR.ParentStructureElement.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

        // Fill the paragraph struct element spaceAfter attribute.
        var helloSpaceAfter = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.SpaceAfter);
        helloSpaceAfter.SetNumberValue(30.625);
        helloAttrs.SetAttribute(helloSpaceAfter);

        // Create a figure element and place it to root element in second position.
        Aspose.Pdf.LogicalStructure.FigureElement figure = tagged.CreateFigureElement();
        tagged.RootElement.InsertChild(figure, 2);

        // Set an alternative text for the figure.
        figure.AlternativeText = "A fly.";

        // Tag figure struct element to image element on page.
        Aspose.Pdf.LogicalStructure.MCRElement figureMCR = figure.Tag(imageBdc);

        // Get the figure struct element attributes.
        Aspose.Pdf.LogicalStructure.StructureAttributes figureAttrs = figureMCR.ParentStructureElement.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

        // Fill the figure struct element spaceAfter attribute.
        var figureSpaceAfter = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.SpaceAfter);
        figureSpaceAfter.SetNumberValue(3.625);
        figureAttrs.SetAttribute(figureSpaceAfter);

        // Fill the figure struct element BBox attribute.
        var figureBBox = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.BBox);
        figureBBox.SetArrayNumberValue(new double?[] { 71.9971, 375.839, 523.299, 714.345 });
        figureAttrs.SetAttribute(figureBBox);

        // Fill the figure struct element placement attribute.
        var figurePlacement = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.Placement);
        figurePlacement.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.Placement_Block);
        figureAttrs.SetAttribute(figurePlacement);

        // Find exist struct element in document.
        Aspose.Pdf.LogicalStructure.Element p2 = (Aspose.Pdf.LogicalStructure.StructureElement)tagged.RootElement.ChildElements[3];

        // Clear the subtree of an existing structure tree element.
        p2.ClearChilds();

        // Create the span struct element.
        Aspose.Pdf.LogicalStructure.SpanElement span1 = tagged.CreateSpanElement();

        // Get the span1 struct element attributes.
        Aspose.Pdf.LogicalStructure.StructureAttributes span1Attrs = span1.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

        // Fill the span1 struct element textDecorationType attribute.
        var span1TextDecorationType = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationType);
        span1TextDecorationType.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.TextDecorationType_Underline);
        span1Attrs.SetAttribute(span1TextDecorationType);

        // Fill the span1 struct element textDecorationThickness attribute.
        var span1TextDecorationThickness = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationThickness);
        span1TextDecorationThickness.SetNumberValue(0);
        span1Attrs.SetAttribute(span1TextDecorationThickness);

        // Fill the span1 struct element textDecorationColor attribute.
        var span1TextDecorationColor = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationColor);
        span1TextDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
        span1Attrs.SetAttribute(span1TextDecorationColor);

        // Append the span element to the paragraph element in the struct tree.
        p2.AppendChild(span1);

        // Tag paragraph struct element to text element on page.
        Aspose.Pdf.LogicalStructure.MCRElement text1MCR = p2.Tag(text1BDC);

        // Get the mcr struct element attributes.
        Aspose.Pdf.LogicalStructure.StructureAttributes text1Attrs = text1MCR.ParentStructureElement.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

        // Fill the text1 MCR struct element textAlign attribute.
        var text1TextAlign = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextAlign);
        text1TextAlign.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.TextAlign_Center);
        text1Attrs.SetAttribute(text1TextAlign);

        // Create the span struct element.
        Aspose.Pdf.LogicalStructure.SpanElement span2 = tagged.CreateSpanElement();

        // Get the span2 struct element attributes.
        Aspose.Pdf.LogicalStructure.StructureAttributes span2Attrs = span2.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

        // Fill the span2 struct element textDecorationType attribute.
        var textDecorationType = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationType);
        textDecorationType.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.TextDecorationType_Underline);
        span2Attrs.SetAttribute(textDecorationType);

        // Fill the span2 struct element textDecorationThickness attribute.
        var textDecorationThickness = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationThickness);
        textDecorationThickness.SetNumberValue(0);
        span2Attrs.SetAttribute(textDecorationThickness);

        // Fill the span2 struct element textDecorationColor attribute.
        var textDecorationColor = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationColor);
        textDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
        span2Attrs.SetAttribute(textDecorationColor);

        // Append the span struct element to the struct element tree.
        p2.AppendChild(span2);

        // Create the link struct element.
        Aspose.Pdf.LogicalStructure.LinkElement link2 = tagged.CreateLinkElement();
        // Set an id attribute of struct element.
        link2.SetId(Guid.NewGuid().ToString());
        // Append the link struct element to the struct element tree.
        span2.AppendChild(link2);
        // Tag link struct element to the page annotation element.
        link2.Tag(page.Annotations[1]);
        // Tag link struct element to text element on page.
        link2.Tag(link2Bdc);

        // Create the link struct element.
        Aspose.Pdf.LogicalStructure.LinkElement link1 = tagged.CreateLinkElement();
        // Set an id attribute of struct element.
        link1.SetId(Guid.NewGuid().ToString());
        // Append the link struct element to the struct element tree.
        span1.AppendChild(link1);
        // Tag link struct element to the page annotation element.
        link1.Tag(page.Annotations[2]);
        // Tag link struct element to text element on page.
        link1.Tag(link1Bdc);

        // Remove the struct element at index 0 from the struct tree.
        tagged.RootElement.RemoveChild(0);

        // Save PDF document
        document.Save(dataDir + "EditTags_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EditTags()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "EditTags.pdf");

    // Get first page
    var page = document.Pages[1];
    // The marked content operator on page for the image.
    Aspose.Pdf.Operators.BDC imageBdc = null;
    // The marked content operator on page for the text.
    Aspose.Pdf.Operators.BDC text1BDC = null;
    // The marked content operator on page for the link1.
    Aspose.Pdf.Operators.BDC link1Bdc = null;
    // The marked content operator on page for the link2.
    Aspose.Pdf.Operators.BDC link2Bdc = null;
    // The marked content operator on page for the Hello text.
    Aspose.Pdf.Operators.BDC helloBdc = null;
    // Find the marked content operators for the elements on the page.
    for (int i = 1; i <= page.Contents.Count; i++)
    {
        Aspose.Pdf.Operator op = page.Contents[i];
        var bdc = op as Aspose.Pdf.Operators.BDC;
        if (bdc != null)
        {
            // The text operator with marked content id = 0 was found.
            if (bdc.Properties.MCID == 0)
            {
                helloBdc = bdc;
            }
        }

        var doXobj = op as Aspose.Pdf.Operators.Do;
        if (doXobj != null)
        {
            // Wrap the image XObject with makred content operator.
            imageBdc = new Aspose.Pdf.Operators.BDC("Figure");
            page.Contents.Insert(i - 2, imageBdc);
            i++;
            page.Contents.Insert(i + 1, new Aspose.Pdf.Operators.EMC());
            i++;
        }

        var tx = op as Aspose.Pdf.Operators.TextShowOperator;
        if (tx != null)
        {
            // Wrap the text operator on page with makred content operator.
            if (tx.Text.Contains("efter Ukendt forfatter er licenseret under"))
            {
                text1BDC = new Aspose.Pdf.Operators.BDC("P");
                page.Contents.Insert(i - 1, text1BDC);
                i++;
                page.Contents.Insert(i + 1, new Aspose.Pdf.Operators.EMC());
                i++;
            }
            // Wrap the text operator on page with makred content operator.
            if (tx.Text.Contains("CC"))
            {
                link1Bdc = new Aspose.Pdf.Operators.BDC("Link");
                page.Contents.Insert(i - 1, link1Bdc);
                i++;
                page.Contents.Insert(i + 1, new Aspose.Pdf.Operators.EMC());
                i++;
            }
            // Wrap the text operator on page with makred content operator.
            if (tx.Text.Contains("Dette billede"))
            {
                link2Bdc = new Aspose.Pdf.Operators.BDC("Link");
                page.Contents.Insert(i - 1, link2Bdc);
                i++;
                page.Contents.Insert(i + 1, new Aspose.Pdf.Operators.EMC());
                i++;
            }
        }
    }

    Aspose.Pdf.Tagged.ITaggedContent tagged = document.TaggedContent;

    // Find exist struct element in document.
    Aspose.Pdf.LogicalStructure.Element helloParagraph = tagged.RootElement.ChildElements[1];

    // Clear the subtree of an existing structure tree element.
    helloParagraph.ClearChilds();

    // Tag paragraph struct element to text on page.
    Aspose.Pdf.LogicalStructure.MCRElement helloMCR = helloParagraph.Tag(helloBdc);

    // Get the struct element attributes.
    Aspose.Pdf.LogicalStructure.StructureAttributes helloAttrs = helloMCR.ParentStructureElement.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

    // Fill the paragraph struct element spaceAfter attribute.
    var helloSpaceAfter = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.SpaceAfter);
    helloSpaceAfter.SetNumberValue(30.625);
    helloAttrs.SetAttribute(helloSpaceAfter);

    // Create a figure element and place it to root element in second position.
    Aspose.Pdf.LogicalStructure.FigureElement figure = tagged.CreateFigureElement();
    tagged.RootElement.InsertChild(figure, 2);

    // Set an alternative text for the figure.
    figure.AlternativeText = "A fly.";

    // Tag figure struct element to image element on page.
    Aspose.Pdf.LogicalStructure.MCRElement figureMCR = figure.Tag(imageBdc);

    // Get the figure struct element attributes.
    Aspose.Pdf.LogicalStructure.StructureAttributes figureAttrs = figureMCR.ParentStructureElement.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

    // Fill the figure struct element spaceAfter attribute.
    var figureSpaceAfter = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.SpaceAfter);
    figureSpaceAfter.SetNumberValue(3.625);
    figureAttrs.SetAttribute(figureSpaceAfter);

    // Fill the figure struct element BBox attribute.
    var figureBBox = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.BBox);
    figureBBox.SetArrayNumberValue(new double?[] { 71.9971, 375.839, 523.299, 714.345 });
    figureAttrs.SetAttribute(figureBBox);

    // Fill the figure struct element placement attribute.
    var figurePlacement = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.Placement);
    figurePlacement.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.Placement_Block);
    figureAttrs.SetAttribute(figurePlacement);

    // Find exist struct element in document.
    Aspose.Pdf.LogicalStructure.Element p2 = (Aspose.Pdf.LogicalStructure.StructureElement)tagged.RootElement.ChildElements[3];

    // Clear the subtree of an existing structure tree element.
    p2.ClearChilds();

    // Create the span struct element.
    Aspose.Pdf.LogicalStructure.SpanElement span1 = tagged.CreateSpanElement();

    // Get the span1 struct element attributes.
    Aspose.Pdf.LogicalStructure.StructureAttributes span1Attrs = span1.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

    // Fill the span1 struct element textDecorationType attribute.
    var span1TextDecorationType = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationType);
    span1TextDecorationType.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.TextDecorationType_Underline);
    span1Attrs.SetAttribute(span1TextDecorationType);

    // Fill the span1 struct element textDecorationThickness attribute.
    var span1TextDecorationThickness = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationThickness);
    span1TextDecorationThickness.SetNumberValue(0);
    span1Attrs.SetAttribute(span1TextDecorationThickness);

    // Fill the span1 struct element textDecorationColor attribute.
    var span1TextDecorationColor = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationColor);
    span1TextDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
    span1Attrs.SetAttribute(span1TextDecorationColor);

    // Append the span element to the paragraph element in the struct tree.
    p2.AppendChild(span1);

    // Tag paragraph struct element to text element on page.
    Aspose.Pdf.LogicalStructure.MCRElement text1MCR = p2.Tag(text1BDC);

    // Get the mcr struct element attributes.
    Aspose.Pdf.LogicalStructure.StructureAttributes text1Attrs = text1MCR.ParentStructureElement.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

    // Fill the text1 MCR struct element textAlign attribute.
    var text1TextAlign = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextAlign);
    text1TextAlign.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.TextAlign_Center);
    text1Attrs.SetAttribute(text1TextAlign);

    // Create the span struct element.
    Aspose.Pdf.LogicalStructure.SpanElement span2 = tagged.CreateSpanElement();

    // Get the span2 struct element attributes.
    Aspose.Pdf.LogicalStructure.StructureAttributes span2Attrs = span2.Attributes.CreateAttributes(Aspose.Pdf.LogicalStructure.AttributeOwnerStandard.Layout);

    // Fill the span2 struct element textDecorationType attribute.
    var textDecorationType = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationType);
    textDecorationType.SetNameValue(Aspose.Pdf.LogicalStructure.AttributeName.TextDecorationType_Underline);
    span2Attrs.SetAttribute(textDecorationType);

    // Fill the span2 struct element textDecorationThickness attribute.
    var textDecorationThickness = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationThickness);
    textDecorationThickness.SetNumberValue(0);
    span2Attrs.SetAttribute(textDecorationThickness);

    // Fill the span2 struct element textDecorationColor attribute.
    var textDecorationColor = new Aspose.Pdf.LogicalStructure.StructureAttribute(Aspose.Pdf.LogicalStructure.AttributeKey.TextDecorationColor);
    textDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
    span2Attrs.SetAttribute(textDecorationColor);

    // Append the span struct element to the struct element tree.
    p2.AppendChild(span2);

    // Create the link struct element.
    Aspose.Pdf.LogicalStructure.LinkElement link2 = tagged.CreateLinkElement();
    // Set an id attribute of struct element.
    link2.SetId(Guid.NewGuid().ToString());
    // Append the link struct element to the struct element tree.
    span2.AppendChild(link2);
    // Tag link struct element to the page annotation element.
    link2.Tag(page.Annotations[1]);
    // Tag link struct element to text element on page.
    link2.Tag(link2Bdc);

    // Create the link struct element.
    Aspose.Pdf.LogicalStructure.LinkElement link1 = tagged.CreateLinkElement();
    // Set an id attribute of struct element.
    link1.SetId(Guid.NewGuid().ToString());
    // Append the link struct element to the struct element tree.
    span1.AppendChild(link1);
    // Tag link struct element to the page annotation element.
    link1.Tag(page.Annotations[2]);
    // Tag link struct element to text element on page.
    link1.Tag(link1Bdc);

    // Remove the struct element at index 0 from the struct tree.
    tagged.RootElement.RemoveChild(0);

    // Save PDF document
    document.Save(dataDir + "EditTags_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}