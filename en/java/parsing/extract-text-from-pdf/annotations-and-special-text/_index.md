---
title: Annotations and Special Text using Java
linktitle: Annotations and Special Text
type: docs
weight: 40
url: /java/annotation-and-special-text/
description: Learn how to extract text from stamp annotations, highlighted text, and superscript or subscript content in PDF documents using Aspose.PDF for Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Extract highlighted text

Iterate through page annotations and read marked text from `HighlightAnnotation`.

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) objects on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Check whether each annotation is a [HighlightAnnotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/highlightannotation/) before casting it to the typed annotation class.
1. Read the marked text from each highlight annotation and print it to the console.

```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## Extract text from stamp annotations

Read the normal appearance stream from a stamp annotation and pass it through `TextAbsorber`.

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Iterate through the [Annotation](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/annotation/) objects on the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Filter the annotations to those whose type is `Stamp`.
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textabsorber/) and request the normal appearance entry from the stamp annotation appearance dictionary.
1. Visit the appearance [XForm](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/xform/) and print the extracted text.

```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## Extract superscript and subscript text details

Use `TextFragmentAbsorber` when you need both the extracted text and the superscript or subscript flags on each fragment.

1. Open the source PDF in a [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) instance.
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragmentabsorber/) for fragment-level text analysis.
1. Visit the target [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) and collect its [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) objects.
1. Iterate through those fragments and read the text together with the superscript and subscript flags from `fragment.getTextState()`.
1. Write the extracted details to the output file.

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
