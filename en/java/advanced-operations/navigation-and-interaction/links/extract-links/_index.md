---
title: Extract PDF Links in Java
linktitle: Extract Links
type: docs
weight: 30
url: /java/extract-links/
description: Learn how to extract link annotations and hyperlinks from PDF documents in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract link annotations and URI targets from PDF files with Java
Abstract: This article explains how to extract link annotations from PDF documents using Aspose.PDF for Java. It shows how to enumerate link annotations on a page, read their page index and rectangle, and extract URI targets from GoToURIAction instances.
---
You can inspect PDF links by iterating over page annotations and filtering for `AnnotationType.Link`.

## Extract link annotations

1. Open the source PDF document used in this example.
2. Run the Aspose.PDF operations required to extract link annotations.
3. Write the extracted output or inspect the returned values.

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

1. Open the source PDF document used in this example.
2. Run the Aspose.PDF operations required to extract hyperlink targets.
3. Write the extracted output or inspect the returned values.

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
