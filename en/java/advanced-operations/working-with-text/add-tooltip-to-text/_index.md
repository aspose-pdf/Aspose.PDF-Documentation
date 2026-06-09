---
title: Add Tooltips to PDF Text in Java
linktitle: PDF Tooltip
type: docs
weight: 20
url: /java/pdf-tooltip/
description: Learn how to add tooltips to text fragments in PDF documents in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add interactive tooltips to PDF text fragments using Java
Abstract: This article shows how to add interactive help to PDF text using Aspose.PDF for Java. It covers attaching tooltip text to invisible button fields placed over matched text fragments and creating a hidden text field that appears when the pointer enters a trigger area.
---
## Add tooltips to searched text

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) with the target [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/).
1. Save the initial PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and reopen it.
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragmentabsorber/) and search for the target text.
1. Create a [ButtonField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/buttonfield/) for each matched fragment and add it to the document form.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void addToolTipToSearchedText(Path outputFile) {
    Document document = new Document();
    document.getPages().add().getParagraphs()
            .add(new TextFragment("Move the mouse cursor here to display a tooltip"));
    document.save(outputFile.toString());
    document.close();

    document = new Document(outputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber(
            "Move the mouse cursor here to display a tooltip");
    document.getPages().accept(absorber);

    for (TextFragment fragment : absorber.getTextFragments()) {
        ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
        field.setAlternateName("Tooltip for text.");
        document.getForm().add(field);
    }

    document.save(outputFile.toString());
    document.close();
}
```
