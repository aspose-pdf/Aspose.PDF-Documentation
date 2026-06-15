---
title: Create PDF Links in Java
linktitle: Create Links
type: docs
weight: 10
url: /java/create-links/
description: Learn how to create internal, external, and remote PDF links in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create link annotations in PDF files with Java
Abstract: This article shows how to create link annotations using Aspose.PDF for Java. It covers launch actions, remote document navigation, in-document page navigation, and URI-based web links by attaching actions to LinkAnnotation objects.
---
Aspose.PDF for Java uses `LinkAnnotation` together with an action object to define link behavior.

## Create a launch-action link

Use this example when a link annotation should launch an external file or target.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and select the target page.
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) and configure its border and color.
1. Assign a [LaunchAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/launchaction/) and save the document.

```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Create a remote go-to link

Use this example when the link should open a page in another PDF document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) on the target page.
1. Assign a [GoToRemoteAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/gotoremoteaction/) and save the output file.

```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Create an internal go-to link

Use this example when the link should navigate to another page inside the same PDF document.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) and configure its appearance.
1. Assign a [GoToAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/gotoaction/) to the destination page and save the document.

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

## Create a URI link

Use this example when the link should open a web resource through a URI action.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) on the page.
1. Assign a [GoToURIAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/gotouriaction/) and save the output file.

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
