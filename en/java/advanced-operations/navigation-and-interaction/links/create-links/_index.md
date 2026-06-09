---
title: Create PDF Links in Java
linktitle: Create Links
type: docs
weight: 10
url: /java/create-links/
description: Learn how to create internal, external, and remote PDF links in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create link annotations in PDF files with Java
Abstract: This article shows how to create link annotations using Aspose.PDF for Java. It covers launch actions, remote document navigation, in-document page navigation, and URI-based web links by attaching actions to LinkAnnotation objects.
---
Aspose.PDF for Java uses `LinkAnnotation` together with an action object to define link behavior.

## Create a page navigation link

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create the [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Set the annotation properties required by the example, including the [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rectangle/), [Border](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/border/), and [Color](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/color/).
1. Create the required [GoToAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/gotoaction/) and assign it to the target [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/).
1. Add the annotation to the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
