---
title: Update PDF Links in Java
linktitle: Update Links
type: docs
weight: 20
url: /java/update-links/
description: Learn how to update PDF link appearance and destinations in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Update link annotation appearance and web destinations in PDF files with Java
Abstract: This article shows how to update existing link annotations using Aspose.PDF for Java. The examples demonstrate changing the color of text covered by a link, updating the link annotation color, and replacing the target URI for web links.
---
Existing links can be edited by finding the link annotation on a page and updating either its appearance or its action.

## Update the text color under a link

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragmentabsorber/) and search for the target text.
1. Configure the [TextSearchOptions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textsearchoptions/) required by the example.
1. Set the required [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) formatting options, including [Color](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/color/).
1. Read or iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) items on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void linkAnnotationUpdateTextColor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX() - 2);
                rect.setLLY(rect.getLLY() - 2);
                rect.setURX(rect.getURX() + 2);
                rect.setURY(rect.getURY() + 2);
                absorber.setTextSearchOptions(new TextSearchOptions(rect));
                absorber.visit(document.getPages().get_Item(1));
                for (TextFragment textFragment : absorber.getTextFragments()) {
                    textFragment.getTextState().setForegroundColor(Color.getRed());
                }
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Update the link annotation color

`linkAnnotationUpdateBorder` iterates through link annotations and calls `linkAnnotation.setColor(Color.getRed())`.

## Update the web destination

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Read or iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) items on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Find the [LinkAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/linkannotation/) and update its [GoToURIAction](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/gotouriaction/).
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void linkAnnotationUpdateWebDestination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    action.setURI("https://www.aspose.com");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
