---
title: Interactive Annotations using Java
linktitle: Interactive Annotations
type: docs
weight: 60
url: /java/interactive-annotations/
description: Learn how to add, inspect, and delete link annotations in PDF documents using Aspose.PDF for Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Work with interactive PDF annotations in Java.
Abstract: This article explains how to work with interactive link annotations in PDF files using Aspose.PDF for Java. It covers locating text, creating a link annotation over the matched text area, reading existing link annotations, and deleting them.
---
## Add a link annotation

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragmentabsorber/) and search for the target text.
1. Create the [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) and configure its [GoToURIAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/gotouriaction/).
1. Add the [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) to the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Add the annotation to the page and save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

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

## Related annotation topics

- [Markup Annotations](/pdf/java/markup-annotations/)
- [Security Annotations](/pdf/java/security-annotations/)
- [Shape Annotations](/pdf/java/shape-annotations/)
- [Text Annotations](/pdf/java/text-based-annotations/)
- [Watermark Annotations](/pdf/java/watermark-annotations/)
- [Import and Export Annotations](/pdf/java/import-export-annotations/)
