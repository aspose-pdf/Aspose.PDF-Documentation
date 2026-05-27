---
title: Interactive Annotations using Java
linktitle: Interactive Annotations
type: docs
weight: 60
url: /java/interactive-annotations/
description: Learn how to add, inspect, and delete link annotations in PDF documents using Aspose.PDF for Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Work with interactive PDF annotations in Java.
Abstract: This article explains how to work with interactive link annotations in PDF files using Aspose.PDF for Java. It covers locating text, creating a link annotation over the matched text area, reading existing link annotations, and deleting them.
---
## Add a link annotation

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

The same example class also includes `linkGet` and `linkDelete` methods that enumerate or remove annotations where `AnnotationType` is `Link`.
