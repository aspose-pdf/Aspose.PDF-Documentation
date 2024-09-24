---
title: Edit PDF File Tags
linktitle: Edit Tags
type: docs
weight: 70
url: /net/edit-pdf-file-tags/
description: This article explains how to edit tags in the PDF documents using Aspose.PDF for .NET library.
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Tagged PDFs are designed to ensure accessibility by marking each element—such as text, images, and links—with tags that define their purpose and role in the document. When editing these PDFs, it's crucial to preserve these tags to maintain compliance with accessibility standards like WCAG.

Tools like Aspose.PDF for .NET offer robust functionality for handling tagged content, but care must be taken to uphold the document’s structure and accessibility. By methodically adding alt text to images or formatting paragraphs, tagged PDFs remain accessible and user-friendly.

Since the 24.7 release, as part of the editing tagged PDF, were added methods on **Aspose.Pdf.LogicalStructure.Element**:

- Tag (add tags to specific operators like images, text, and links)
- InsertChild
- RemoveChild
- ClearChilds

These methods allow you to edit pdf file tags, for example:

```cs

    var document = new Document(input);
    var page = document.Pages[1];
    // The marked content operator on page for the image.
    BDC imageBdc = null;
    // The marked content operator on page for the text.
    BDC text1BDC = null;
    // The marked content operator on page for the link1.
    BDC link1Bdc = null;
    // The marked content operator on page for the link2.
    BDC link2Bdc = null;
    // The marked content operator on page for the Hello text.
    BDC helloBdc = null;
    // Find the marked content operators for the elements on the page.
    for (int i = 1; i <= page.Contents.Count; i++)
    {
        Operator op = page.Contents[i];
        BDC bdc = op as BDC;
        if (bdc != null)
        {
            // The text operator with marked content id = 0 was found.
            if (bdc.Properties.MCID == 0)
            {
                helloBdc = bdc;
            }
        }

        Do doXobj = op as Do;
        if (doXobj != null)
        {
            // Wrap the image XObject with makred content operator.
            imageBdc = new BDC(PdfConsts.Figure);
            page.Contents.Insert(i - 2, imageBdc);
            i++;
            page.Contents.Insert(i + 1, new EMC());
            i++;
        }

        TextShowOperator tx = op as TextShowOperator;
        if (tx != null)
        {
            // Wrap the text operator on page with makred content operator.
            if (tx.Text.Contains("efter Ukendt forfatter er licenseret under"))
            {
                text1BDC = new BDC(PdfConsts.P);
                page.Contents.Insert(i - 1, text1BDC);
                i++;
                page.Contents.Insert(i + 1, new EMC());
                i++;
            }
            // Wrap the text operator on page with makred content operator.
            if (tx.Text.Contains("CC"))
            {
                link1Bdc = new BDC(PdfConsts.Link);
                page.Contents.Insert(i - 1, link1Bdc);
                i++;
                page.Contents.Insert(i + 1, new EMC());
                i++;
            }
            // Wrap the text operator on page with makred content operator.
            if (tx.Text.Contains("Dette billede"))
            {
                link2Bdc = new BDC(PdfConsts.Link);
                page.Contents.Insert(i - 1, link2Bdc);
                i++;
                page.Contents.Insert(i + 1, new EMC());
                i++;
            }
        }
    }

    var tagged = document.TaggedContent;

    // Find exist struct element in document.
    var helloParagraph = tagged.RootElement.ChildElements[1];

    // Clear the subtree of an existing structure tree element.
    helloParagraph.ClearChilds();

    // Tag paragraph struct element to text on page.
    var helloMCR = helloParagraph.Tag(helloBdc);

    // Get the struct element attributes.
    var helloAttrs = helloMCR.ParentStructureElement.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

    // Fill the paragraph struct element spaceAfter attribute.
    var helloSpaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    helloSpaceAfter.SetNumberValue(30.625);
    helloAttrs.SetAttribute(helloSpaceAfter);

    // Create a figure element and place it to root element in second position.
    var figure = tagged.CreateFigureElement();
    tagged.RootElement.InsertChild(figure, 2);

    // Set an alternative text for the figure.
    figure.AlternativeText = "A fly.";

    // Tag figure struct element to image element on page.
    var figureMCR = figure.Tag(imageBdc);

    // Get the figure struct element attributes.
    var figureAttrs = figureMCR.ParentStructureElement.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

    // Fill the figure struct element spaceAfter attribute.
    var figureSpaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    figureSpaceAfter.SetNumberValue(3.625);
    figureAttrs.SetAttribute(figureSpaceAfter);

    // Fill the figure struct element BBox attribute.
    var figureBBox = new StructureAttribute(AttributeKey.BBox);
    figureBBox.SetArrayNumberValue(new double?[] { 71.9971, 375.839, 523.299, 714.345 });
    figureAttrs.SetAttribute(figureBBox);

    // Fill the figure struct element placement attribute.
    var figurePlacement = new StructureAttribute(AttributeKey.Placement);
    figurePlacement.SetNameValue(AttributeName.Placement_Block);
    figureAttrs.SetAttribute(figurePlacement);

    // Find exist struct element in document.
    var p2 = (StructureElement)tagged.RootElement.ChildElements[3];
    
    // Clear the subtree of an existing structure tree element.
    p2.ClearChilds();

    // Create the span struct element.
    var span1 = tagged.CreateSpanElement();

    // Get the span1 struct element attributes.
    var span1Attrs = span1.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

    // Fill the span1 struct element textDecorationType attribute.
    var span1TextDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    span1TextDecorationType.SetNameValue(AttributeName.TextDecorationType_Underline);
    span1Attrs.SetAttribute(span1TextDecorationType);

    // Fill the span1 struct element textDecorationThickness attribute.
    var span1TextDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    span1TextDecorationThickness.SetNumberValue(0);
    span1Attrs.SetAttribute(span1TextDecorationThickness);

    // Fill the span1 struct element textDecorationColor attribute.
    var span1TextDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    span1TextDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
    span1Attrs.SetAttribute(span1TextDecorationColor);

    // Append the span element to the paragraph element in the struct tree.
    p2.AppendChild(span1);

    // Tag paragraph struct element to text element on page.
    var text1MCR = p2.Tag(text1BDC);

    // Get the mcr struct element attributes.
    var text1Attrs = text1MCR.ParentStructureElement.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

    // Fill the text1 MCR struct element textAlign attribute.
    var text1TextAlign = new StructureAttribute(AttributeKey.TextAlign);
    text1TextAlign.SetNameValue(AttributeName.TextAlign_Center);
    text1Attrs.SetAttribute(text1TextAlign);

    // Create the span struct element.
    var span2 = tagged.CreateSpanElement();

    // Get the span2 struct element attributes.
    var span2Attrs = span2.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

    // Fill the span2 struct element textDecorationType attribute.
    var textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.SetNameValue(AttributeName.TextDecorationType_Underline);
    span2Attrs.SetAttribute(textDecorationType);

    // Fill the span2 struct element textDecorationThickness attribute.
    var textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.SetNumberValue(0);
    span2Attrs.SetAttribute(textDecorationThickness);

    // Fill the span2 struct element textDecorationColor attribute.
    var textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
    span2Attrs.SetAttribute(textDecorationColor);
    
    // Append the span struct element to the struct element tree.
    p2.AppendChild(span2);

    // Create the link struct element.
    var link2 = tagged.CreateLinkElement();
    // Set an id attribute of struct element.
    link2.SetId(Guid.NewGuid().ToString());
    // Append the link struct element to the struct element tree.
    span2.AppendChild(link2);
    // Tag link struct element to the page annotation element.
    link2.Tag(page.Annotations[1]);
    // Tag link struct element to text element on page.
    link2.Tag(link2Bdc);

    // Create the link struct element.
    var link1 = tagged.CreateLinkElement();
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

    // Save document
    document.Save(output);

```