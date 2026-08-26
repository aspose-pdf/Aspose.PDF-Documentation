---
title: Interactive Annotations using Java
linktitle: Interactive Annotations
type: docs
weight: 30
url: /java/pdfannotationeditor-class/interactive-annotations/
description: Learn how to add, inspect, and delete link annotations in PDF documents using Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Work with interactive PDF annotations in Java
Abstract: This article explains how to work with interactive link annotations in PDF files using Java. It covers locating text, creating a link annotation over the matched text area, reading existing link annotations, and deleting them.
---
## Add a link annotation

1. Load the source PDF document and search the first page for the target text.
2. Use the matched text rectangle to create a `LinkAnnotation` and assign the destination URI.
3. Add the annotation to the page and save the updated PDF.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
