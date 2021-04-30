---
title: PDF Link Annotation 
linktitle: Link Annotation
type: docs
weight: 20
url: /java/link-annotation/
description: Aspose.PDF for Java allows you to Add, Get, and Delete Link Annotation from your PDF document.
lastmod: "2021-02-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

A [Link Annotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) is a hypertext link that leads to a destination elsewhere in the document or to an action to be performed.

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
}
```
