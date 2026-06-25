---
title: Work with PDF Operators in Java
linktitle: Working with Operators
type: docs
weight: 90
url: /java/working-with-operators/
description: Learn how to use low-level PDF operators in Java for content stream manipulation, image placement, XForm reuse, and graphics cleanup.
lastmod: "2026-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Use low-level PDF operators for content stream control in Java
Abstract: This article explains how to work with low-level PDF operators in Aspose.PDF for Java. Learn how to place images precisely, draw reusable XForm content, and remove graphic operators from PDF pages.
---
## Introduction to the PDF Operators and Their Usage

An operator is a PDF keyword specifying some action that shall be performed, such as painting a graphical shape on the page. An operator keyword is distinguished from a named object by the absence of an initial solidus character (2Fh). Operators are meaningful only inside the content stream.

A content stream is a PDF stream object whose data consists of instructions describing the graphical elements to be painted on a page. More details about PDF operators can be found in the [PDF specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Use this page when you need direct control over a PDF content stream in Java, such as placing an image with explicit matrix math, reusing the same graphic multiple times through an XForm, or deleting low-level drawing instructions from a page.

## Add an image with PDF operators

Use low-level operators when image placement must be controlled precisely at the content-stream level instead of through higher-level layout APIs.

1. Open the source PDF with [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and get the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Add the input image stream to the page resources and keep the returned resource name.
1. Create a [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) that defines the target area and build a [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) from its bounds.
1. Use [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) to preserve the current graphics state, [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) to position the image, [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) to paint it, and [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) to restore the prior state.
1. Save the updated PDF document.

```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## Draw reusable XForm content on a page

Use this approach when the same image or graphic should be rendered more than once without duplicating the resource in the PDF file.

1. Open the source PDF with [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), get the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), and access its [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).
1. Wrap the existing page contents with [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) and [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) so later transformations do not leak into the original content stream.
1. Create an [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) resource, add the image to the form resources, and use [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) plus [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) to draw the image inside the form.
1. Place the same form at multiple page coordinates by adding a translation matrix and executing the form name with the `Do` operator.
1. Restore the graphics state and save the output PDF.

```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## Remove graphics operators from a page

Use this example when a page contains vector drawing operators that should be removed directly from the content stream.

1. Open the source PDF with [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) and get the target [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Iterate through the page content operators and collect instances of [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/), and [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).
1. Delete the collected operators from the page contents and save the updated PDF.

This technique removes the targeted drawing instructions only. If the page also contains related text labels or other non-graphic operators, those items remain in the content stream and may need a separate cleanup pass.

```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## Related Topics

- [Advanced PDF operations in Java](/pdf/java/advanced-operations/)
- [Work with images in PDF using Java](/pdf/java/working-with-images/)
- [Work with PDF pages in Java](/pdf/java/working-with-pages/)
- [Work with Vector Graphics in Java](/pdf/java/working-with-vector-graphics/)
