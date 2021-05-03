---
title: Update Links in PDF using Aspose.PDF for Java
linktitle: Update Links
type: docs
weight: 20
url: /java/update-links/
description: Update links in PDF programmatically. This guide is about how to update links in PDF in Java language. 
lastmod: "2021-04-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Update Links in PDF File

As discussed in Add Hyperlink in a PDF File, the [LinkAnnotation](https://apireference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) class makes it possible to add links in a PDF file. There’s also a similar class used to get existing links from inside PDF files. Use this if you need to update an existing link. To update an existing link:

1. Load a PDF file.
1. Go to a specific page in the PDF file.
1. Specify the link destination using the [GoToAction](https://apireference.aspose.com/pdf/java/com.aspose.pdf/gotoaction) object’s Destination property.
1. The destination page is specified using the [XYZExplicitDestination](https://apireference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) constructor.

### Set Link Target to a Page in the Same Document

The following code snippet shows you how to update a link in a PDF file and set its target to the second page of the document.

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // Load the PDF file
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // Get the first link annotation from first page of document
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Modification link: change link destination
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // Specify the destination for link object
        // Represents explicit destination that displays the page with the coordinates (left, top) positioned at the upper-left corner of 
        // the window and the contents of the page magnified by the factor zoom.
        // The 1st parameter is destination page number. 
        // The 2nd is left coordinate
        // The 3nd is top coordinate
        // The 4th argument is zoom factor when displaying the respective page. Using 2 means page will be displayed in 200% zoom
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // Save the document with updated link
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### Set Link Destination to a Web Address

To update the hyperlink so that it points to a web address, instantiate the [GoToURIAction](https://apireference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction) object and pass it to the LinkAnnotation’s Action property. The following code snippet shows how to update a link in a PDF file and set its target to a web address.

```java
    public static void SetLinkDestinationToWebAddress() {        
        // Load the PDF file
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // Get the first link annotation from first page of document
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // Modification link: change link action and set target as web address
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // Save the document with updated link
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### Set Link Target to Another PDF File

The following code snippet shows how to update a link in a PDF file and set its target to another PDF file.

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // Load the PDF file
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // Next line update destination, do not update file
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // Next line update file
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // Save the document with updated link
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### Update LinkAnnotation Text Color

The link annotation does not contain text. Instead, the text is placed in the contents of the page under the annotation. Therefore, to change the color of the text, replace the color of the page text instead of trying change color of the annotation. The following code snippet shows how to update the color of link annotation in a PDF file.

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // Load the PDF file
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // Search the text under the annotation
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // Change color of the text.
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // Save the document with updated link
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```
