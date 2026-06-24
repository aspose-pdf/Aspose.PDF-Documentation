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
Interactive annotations in this section focus on link and button-based workflows that respond to user actions inside a PDF viewer.

## Add a link annotation

Use this example when you need to place a clickable link over text found on the page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Locate the target text fragment and create a [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) over its rectangle.
1. Assign a [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) and save the updated document.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Get link annotations

This example scans the page annotation collection and reports the location of each link annotation.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterate through the annotations on the target page.
1. Filter annotations by [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` and print their rectangles.

```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## Delete link annotations

Use this approach when existing link annotations should be removed from the page.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Collect annotations whose type is [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link`.
1. Delete the collected annotations and save the output file.

```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Add a line annotation

This example creates an interactive line annotation with arrow styles, border settings, and a popup note.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create a [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) with start and end points.
1. Configure its appearance and popup annotation, then save the document.

```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));

        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Add navigation buttons

Use this example when the PDF should include previous-page and next-page buttons for interactive navigation.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and make sure the document has the required pages.
1. Create [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) controls with predefined navigation actions.
1. Add the buttons to the form collection and save the updated document.

```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Add a print button

This example creates a button that triggers the print command when the user clicks it.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and add a page.
1. Create a [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) and assign the print predefined action.
1. Configure the button border and background, add it to the form, and save the document.

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```
