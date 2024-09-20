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

    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;
    for (int i = 1; i <= page.Contents.Count; i++)
    {
        Operator op = page.Contents[i];
        BDC bdc = op as BDC;
        if (bdc != null)
        {
            if (bdc.Properties.MCID == 0)
            {
                helloBdc = bdc;
            }
        }

        Do doXobj = op as Do;
        if (doXobj != null)
        {
            imageBdc = new BDC("Figure");
            page.Contents.Insert(i - 2, imageBdc);
            i++;
            page.Contents.Insert(i + 1, new EMC());
            i++;
        }

        TextShowOperator tx = op as TextShowOperator;
        if (tx != null)
        {
            if (tx.Text.Contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.Contents.Insert(i - 1, pBdc);
                i++;
                page.Contents.Insert(i + 1, new EMC());
                i++;
            }
            if (tx.Text.Contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.Contents.Insert(i - 1, link1Bdc);
                i++;
                page.Contents.Insert(i + 1, new EMC());
                i++;
            }
            if (tx.Text.Contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.Contents.Insert(i - 1, link2Bdc);
                i++;
                page.Contents.Insert(i + 1, new EMC());
                i++;
            }
        }
    }

    var tagged = document.TaggedContent;
    {
        var p = tagged.RootElement.ChildElements[1];
        p.ClearChilds();
        var mcr = p.Tag(helloBdc);
        var attrs = ((StructureElement)mcr.ParentElement).Attributes.CreateAttributes(AttributeOwnerStandard.Layout);
        var attr = new StructureAttribute(AttributeKey.SpaceAfter);
        attr.SetNumberValue(30.625);
        attrs.SetAttribute(attr);
    }

    {
        var figure = tagged.CreateFigureElement();
        tagged.RootElement.InsertChild(figure, 2);
        figure.AlternativeText = "A fly.";
        var mcr = figure.Tag(imageBdc);

        var attrs = ((StructureElement)mcr.ParentElement).Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

        var spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
        spaceAfter.SetNumberValue(3.625);
        attrs.SetAttribute(spaceAfter);

        var bbox = new StructureAttribute(AttributeKey.BBox);
        bbox.SetArrayNumberValue(new double?[] { 71.9971, 375.839, 523.299, 714.345 });
        attrs.SetAttribute(bbox);

        var placement = new StructureAttribute(AttributeKey.Placement);
        placement.SetNameValue(AttributeName.Placement_Block);
        attrs.SetAttribute(placement);
    }

    var p2 = (StructureElement)tagged.RootElement.ChildElements[3];
    p2.ClearChilds();

    var span1 = tagged.CreateSpanElement();
    {
        var attrs = span1.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

        var textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
        textDecorationType.SetNameValue(AttributeName.TextDecorationType_Underline);
        attrs.SetAttribute(textDecorationType);

        var textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
        textDecorationThickness.SetNumberValue(0);
        attrs.SetAttribute(textDecorationThickness);

        var textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
        textDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
        attrs.SetAttribute(textDecorationColor);
    }
    p2.AppendChild(span1);

    {
        var mcr = p2.Tag(pBdc);
        var attrs = ((StructureElement)mcr.ParentElement).Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

        var textAlign = new StructureAttribute(AttributeKey.TextAlign);
        textAlign.SetNameValue(AttributeName.TextAlign_Center);
        attrs.SetAttribute(textAlign);

        var spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
        spaceAfter.SetNumberValue(21.75);
        attrs.SetAttribute(spaceAfter);
    }

    var span2 = tagged.CreateSpanElement();
    {
        var attrs = span2.Attributes.CreateAttributes(AttributeOwnerStandard.Layout);

        var textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
        textDecorationType.SetNameValue(AttributeName.TextDecorationType_Underline);
        attrs.SetAttribute(textDecorationType);

        var textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
        textDecorationThickness.SetNumberValue(0);
        attrs.SetAttribute(textDecorationThickness);

        var textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
        textDecorationColor.SetArrayNumberValue(new double?[] { 0.0196075, 0.384308, 0.756866 });
        attrs.SetAttribute(textDecorationColor);
    }
    p2.AppendChild(span2);

    var link2 = tagged.CreateLinkElement();
    link2.SetId(Guid.NewGuid().ToString());
    span2.AppendChild(link2);
    link2.Tag(page.Annotations[1]);
    link2.Tag(link2Bdc);

    var link1 = tagged.CreateLinkElement();
    link1.SetId(Guid.NewGuid().ToString());
    span1.AppendChild(link1);
    link1.Tag(page.Annotations[2]);
    link1.Tag(link1Bdc);

    tagged.RootElement.RemoveChild(0);

    document.Save(output);

```