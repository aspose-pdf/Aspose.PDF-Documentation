---
title: Extract PDF Links in Java
linktitle: Extract Links
type: docs
weight: 30
url: /java/extract-links/
description: Learn how to extract link annotations and hyperlinks from PDF documents in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract link annotations and URI targets from PDF files with Java
Abstract: This article explains how to extract link annotations from PDF documents using Aspose.PDF for Java. It shows how to enumerate link annotations on a page, read their page index and rectangle, and extract URI targets from GoToURIAction instances.
---
You can inspect PDF links by iterating over page annotations and filtering for `AnnotationType.Link`.

## Extract link annotations

Use this example when you need the location and page information for link annotations on a page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Iterate through the page annotations and filter for link annotations.
1. Read the page index and rectangle for each matching link.

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

## Extract hyperlink destinations

Use this example when you need to read the target URIs from web link annotations.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Find [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) objects whose action is a [GoToURIAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/gotouriaction/).
1. Print the page index and URI target for each hyperlink.

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
