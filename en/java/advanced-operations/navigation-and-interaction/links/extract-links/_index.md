---
title: Extract PDF Links in Java
linktitle: Extract Links
type: docs
weight: 30
url: /java/extract-links/
description: Learn how to extract link annotations and hyperlinks from PDF documents in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract link annotations and URI targets from PDF files with Java
Abstract: This article explains how to extract link annotations from PDF documents using Aspose.PDF for Java. It shows how to enumerate link annotations on a page, read their page index and rectangle, and extract URI targets from GoToURIAction instances.
---
You can inspect PDF links by iterating over page annotations and filtering for `AnnotationType.Link`.

## Extract link annotations

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Read or iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) items on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Filter for [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) items whose [AnnotationType](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotationtype/) is `Link`.
1. Write the extracted output or inspect the returned values.

```java
public static void extractLinkAnnotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                System.out.println("Page: " + linkAnnotation.getPageIndex()
                        + ", location: " + linkAnnotation.getRect());
            }
        }
    }
}
```

## Extract hyperlink targets

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Read or iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) items on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Filter for [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) items and inspect their [GoToURIAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/gotouriaction/).
1. Write the extracted output or inspect the returned values.

```java
public static void extractHyperlinks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    System.out.println("Page " + linkAnnotation.getPageIndex() + ", URI:" + action.getURI());
                }
            }
        }
    }
}
```
