---
title: Using extra types of PDF annotations
linktitle: Extra Annotations
type: docs
weight: 60
url: /java/extra-annotations/
description: Discover how to add extra annotations to PDF documents in Java with Aspose.PDF for more interactive documents.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on adding and managing annotations in PDF with Aspose.PDF for Java
Abstract: This article provides a comprehensive guide on adding and managing various types of annotations in PDF files using Aspose.PDF for Java. It covers the implementation of Caret Annotations, which indicate text insertions, by detailing the steps to create, add, retrieve, and delete these annotations from an existing PDF file. The article includes code snippets demonstrating how to configure Caret Annotations with specific properties such as title, subject, color, and flags. Additionally, it explores the use of StrikeOutAnnotations for text replacements. The document also delves into handling Link Annotations, which serve as hypertext links to other document sections or actions. This section includes instructions on adding, retrieving, and deleting Link Annotations, with examples that illustrate linking to a phone number. Furthermore, the article introduces Redaction Annotations, used to redact specific page regions. It explains how to create and apply these annotations, with examples of modifying the annotation's appearance and flattening the annotation to remove underlying content. The guide concludes
SoftwareApplication: java
---

## How to add Caret Annotation into existing PDF file

Caret Annotation is a symbol that indicates text editing. Caret Annotation is also markup annotation, so the Caret class derives from the Markup class and also provides functions to get or set properties of the Caret Annotation and reset the flow of the Caret Annotation appearance.

Steps with which we create Caret annotation:

1. Load the PDF file - new [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Create new [Caret Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/CaretAnnotation) and set Caret parameters (new Rectangle, title, Subject, Flags, color, width, StartingStyle and EndingStyle). This annotation is used to indicate the insertion of text.
1. Create new [StrikeOutAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/StrikeOutAnnotation) and set parameters (new Rectangle, title, color, new QuadPoints and new points, Subject, InReplyTo,ReplyType).
1. After we can Add annotations to the page.

The following code snippet shows how to add Caret Annotation to a PDF file:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCaretAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCaretAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample.pdf");
        // This annotation is used to indicate the insertion of text
        CaretAnnotation caretAnnotation1 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769));
        caretAnnotation1.setTitle("Aspose User");
        caretAnnotation1.setSubject("Inserted text 1");
        caretAnnotation1.setFlags(AnnotationFlags.Print);
        caretAnnotation1.setColor(Color.getBlue());

        // This annotation is used to indicate the replacement of text
        CaretAnnotation caretAnnotation2 = new CaretAnnotation(
                document.getPages().get_Item(1), new Rectangle(361.246, 727.908, 370.081, 735.107));

        caretAnnotation2.setTitle("Aspose User");
        caretAnnotation2.setFlags(AnnotationFlags.Print);
        caretAnnotation2.setSubject("Inserted text 2");
        caretAnnotation2.setColor(Color.getBlue());

        StrikeOutAnnotation strikeOutAnnotation = new StrikeOutAnnotation(
                document.getPages().get_Item(1), new Rectangle(318.407, 727.826, 368.916, 740.098));

        strikeOutAnnotation.setColor(Color.getBlue());
        strikeOutAnnotation.setQuadPoints(new Point[] { new Point(321.66, 739.416),
                new Point(365.664, 739.416), new Point(321.66, 728.508),
                new Point(365.664, 728.508) });

        strikeOutAnnotation.setSubject("Cross-out");
        strikeOutAnnotation.setInReplyTo(caretAnnotation2);
        strikeOutAnnotation.setReplyType(ReplyType.Group);

        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation1);
        document.getPages().get_Item(1).getAnnotations().add(caretAnnotation2);
        document.getPages().get_Item(1).getAnnotations().add(strikeOutAnnotation);

        document.save(_dataDir + "sample_caret.pdf");

    }
```

## Get Caret Annotation

Please try using the following code snippet to Get Caret Annotation in PDF document

```java
    public static void GetCaretAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## Delete Caret Annotation

The following code snippet shows how Delete Caret Annotation from a PDF file.

```java
public static void DeleteCaretAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample_caret.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CaretAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // delete annotation
        for (Annotation ca : caretAnnotations) {
            document.getPages().get_Item(1).getAnnotations().delete(ca);
        }
        document.save(_dataDir + "sample_caret_del.pdf");
    }
```

A [Link Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) is a hypertext link that leads to a destination elsewhere in the document or to an action to be performed.

## Add Link Annotation

A Link is a rectangular area that can be placed anywhere on the page. Each link has a corresponding PDF action associated with it. This action is performed when the user clicks in the area of this link.

The following code snippet shows how to add Link Annotation to a PDF file using a phone number example:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLinkAnnotation {

    // The path to the documents directory.

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLinkAnnotation() {
        try {
            // Load the PDF file
            Document document = new Document(_dataDir + "SimpleResume.pdf");
            Page page = document.getPages().get_Item(1);

            // Create TextFragmentAbsorber object to find a phone number
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // Accept the absorber for the 1st page only
            page.accept(textFragmentAbsorber);

            TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

            // Create Link Annotation and set the action to call a phone number
            LinkAnnotation linkAnnotation = new LinkAnnotation(page, phoneNumberFragment.getRectangle());
            linkAnnotation.setAction(new GoToURIAction("callto:678-555-0103"));

            // Add annotation to page
            page.getAnnotations().add(linkAnnotation);
            document.save(_dataDir + "SimpleResume_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```

## Get Link Annotation

Please try using the following code snippet to Get LinkAnnotation from PDF document.

```java
    public static void GetLinkAnnotations() {

        // Load the PDF file
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        // print results
        for (Annotation la : linkAnnotations) {

            LinkAnnotation l = (LinkAnnotation) la;

            // Print the URL of each Link Annotation
            System.out.println("URI: " + ((GoToURIAction) l.getAction()).getURI());

            TextAbsorber absorber = new TextAbsorber();
            absorber.getTextSearchOptions().setLimitToPageBounds(true);
            absorber.getTextSearchOptions().setRectangle(l.getRect());
            page.accept(absorber);

            String extractedText = absorber.getText();

            // Print the text associated with hyperlink
            System.out.println(extractedText);
        }
    }
```

## Delete Link Annotation

The following code snippet shows how to Delete Link Annotation from PDF file. For this we need to find and and remove all link annotations on the 1st page. After this we will save document with removed annotation.

```java
    public static void DeleteLinkAnnotations() {
        // Load the PDF file
        Document document = new Document(_dataDir + "SimpleResume_mod.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> linkAnnotations = annotationSelector.getSelected();

        for (Annotation la : linkAnnotations)
            page.getAnnotations().delete(la);

        // Save document with removed annotation
        document.save(_dataDir + "SimpleResume_del.pdf");
    }
```

## Redact certain page region with Redaction Annotation using Aspose.PDF for Java

Aspose.PDF for Java supports the feature to add as well as manipulate Annotations in an existing PDF file. Recently some of our customers posted a required to redact (remove text, image, etc elements from) a certain page region of PDF document. In order to fulfill this requirement, a class named RedactionAnnotation is provided, which can be used to redact certain page regions or it can be used to manipulate existing RedactionAnnotations and redact them (i.e. flatten annotation and remove the text under it).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleRedactAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RedactionAnnotation() {

        // Open document
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        // Create RedactionAnnotation instance for specific page region
        RedactionAnnotation annot = new RedactionAnnotation(page, new Rectangle(200, 500, 300, 600));
        annot.setFillColor(Color.getGreen());
        annot.setBorderColor(Color.getYellow());
        annot.setColor(Color.getBlue());

        // Text to be printed on redact annotation
        annot.setOverlayText("REDACTED");
        annot.setTextAlignment(HorizontalAlignment.Center);

        // Repat Overlay text over redact Annotation
        annot.setRepeat(true);

        // Add annotation to annotations collection of first page
        page.getAnnotations().add(annot);

        // Flattens annotation and redacts page contents (i.e. removes text and image
        // Under redacted annotation)
        annot.redact();
        document.save(_dataDir + "RedactPage_out.pdf");
    }
```

## Facades approach

Aspose.PDF.Facades namespace also has a class named [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) which provides the feature to manipulate existing Annotations inside PDF file. This class contains a method named [RedactArea(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Redaction#getredactArea-com.aspose.pdf.Page-com.aspose.pdf.Rectangle-java.awt.Color-) which provides the capability to remove certain page regions.

```java
    public static void RedactionAnnotationFacades(){
        PdfAnnotationEditor editor = new PdfAnnotationEditor();

        editor.bindPdf(_dataDir + "sample.pdf");

        // Redact certain page region
        editor.redactArea(1, new Rectangle(100, 100, 20, 70), java.awt.Color.white);
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.save( _dataDir + "FacadesApproach_out.pdf");
    }
```
