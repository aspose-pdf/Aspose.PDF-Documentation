---
title: Working with Actions 
linktitle: Actions
type: docs
weight: 20
url: /java/actions/
description: This section explains how to add actions to the document and form fields programmatically with Java. Learn how to Add, Create, and Get Hyperlink in a PDF File.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract: The article provides a comprehensive guide on handling hyperlinks within PDF documents using Aspose.PDF for Java. It describes methods to embed hyperlinks to both external URLs and internal pages within a PDF document. The process involves using the `Document`, `Page`, `LinkAnnotation`, and `GoToURIAction` classes to create and manage links. The article includes detailed code snippets for adding hyperlinks, extracting hyperlink destinations (URLs), retrieving hyperlink text, and removing document open actions. Additionally, it explains how to set a specific page to open when viewing a PDF document, utilizing the `XYZExplicitDestination` class. Each section is supported by practical Java code examples, illustrating the implementation of these features. Overall, the article serves as a technical resource for developers looking to manipulate PDF hyperlink functionalities programmatically.
---

A PDF file can contain embedded file attachments and it is often necessary to Hyperlink to these documents. You may direct readers from the main PDF document to a PDF attachment by creating a link in the parent document that points to the attachment.

## Add Hyperlink in PDF File

It is possible to add hyperlinks to PDF files, either to allow readers to navigate to another part of the PDF, or to external content.

In order to add web hyperlinks to PDF documents:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) Class object.
1. Get the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) Class you want to add the link to.
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) object using the Page and [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) objects. The rectangle object is used to specify the location on the page where the link should be added.
1. Set the getAction method to the [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToURIAction) object which specifies the location of the remote URI.
1. To display a hyperlink text, add a text string on a location similar to where the [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) object is placed.
1. To add a free text:

- Instantiate an [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) object. It also accepts Page and Rectangle objects as argument, so it is possible to provide same values as specified against the LinkAnnotation constructor.
- Using the [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) object's Contents property, specify the string that should be displayed in the output PDF.
- Optionally, set the border width of both the [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) and FreeTextAnnotation objects to 0 so that they do not appear in the PDF document.
- Once the [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) and [FreeTextAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/FreeTextAnnotation) objects have been defined, add these links to the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) object's Annotations collection.
- Finally, save the updated PDF using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's Save method.

The following code snippet shows you how to add a hyperlink to a PDF file.

```java
package com.aspose.pdf.examples;

import java.util.List;

import com.aspose.pdf.*;

public class ExampleActions {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Actions/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Actions";
        return _dataDir;
    }

    public static void AddHyperlinkInPDFFile() {
        // Open document
        Document document = new Document(GetDataDir() + "AddHyperlink.pdf");
        // Create link
        Page page = document.getPages().get_Item(1);
        // Create Link annotation object
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 100, 300, 300));
        // Create border object for LinkAnnotation
        Border border = new Border(link);
        // Set the border width value as 0
        border.setWidth(0);
        // Set the border for LinkAnnotation
        link.setBorder(border);
        // Specify the link type as remote URI
        link.setAction(new GoToURIAction("www.aspose.com"));
        // Add link annotation to annotations collection of first page of PDF file
        page.getAnnotations().add(link);

        // Create Free Text annotation
        FreeTextAnnotation textAnnotation = new FreeTextAnnotation(page, new Rectangle(100, 100, 300, 300),
                new DefaultAppearance(FontRepository.findFont("TimesNewRoman"), 10, java.awt.Color.BLUE));

        // String to be added as Free text
        textAnnotation.setContents("Link to Aspose website");
        // Set the border for Free Text Annotation
        textAnnotation.setBorder(border);
        // Add FreeText annotation to annotations collection of first page of Document
        page.getAnnotations().add(textAnnotation);

        // Save updated document
        document.save(_dataDir + "AddHyperlink_out.pdf");

    }
```

## Create Hyperlink to pages in same PDF

Aspose.PDF for Java provides a great feature to PDF creation as well as its manipulation. It also offers the feature to add links to PDF pages and a link can either direct to pages in another PDF file, a web URL, link to launch an Application or even link to pages in same PDF file.

In order to add the local hyperlink, we need to create a TextFragment so that link can be associated with the TextFragment. The [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) class has a method named [getHyperlink](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#getHyperlink--) which is used to associate LocalHyperlink instance. The following code snippet shows the steps to accomplish this requirement.

```java
public static void CreateHyperlinkToPagesInSamePDF() {
        // Create Document instance
        Document document = new Document();

        // Add page to pages collection of PDF file
        Page page = document.getPages().add();

        // Create Text Fragment instance
        TextFragment text = new TextFragment("link page number test to page 2");

        // Create local hyperlink instance
        LocalHyperlink link = new LocalHyperlink();

        // Set target page for link instance
        link.setTargetPageNumber(2);

        // Set TextFragment hyperlink
        text.setHyperlink(link);

        // Add text to paragraphs collection of Page
        page.getParagraphs().add(text);

        // Create new TextFragment instance
        text = new TextFragment("link page number test to page 1");

        // TextFragment should be added over new page
        text.setInNewPage(true);

        // Create another local hyperlink instance
        link = new LocalHyperlink();

        // Set Target page for second hyperlink
        link.setTargetPageNumber(1);

        // Set link for second TextFragment
        text.setHyperlink(link);

        // Add text to paragraphs collection of page object
        page.getParagraphs().add(text);

        // Save updated document
        document.save(GetDataDir() + "CreateLocalHyperlink_out.pdf");
    }
```

## Get PDF Hyperlink Destination (URL)

Links are represented as annotations in a PDF file and they can be added, updated or deleted. Aspose.PDF for Java also supports getting the destination (URL) of the hyperlink in PDF file.

To get a link's URL:

1. Create a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object.
1. Get the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) you want to extract links from.
1. Use the [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) class to extract all the [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation)) objects from the specified page.
1. Pass the [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) object to the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) object's Accept method.
1. Get all the selected link annotations into an IList object using the [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector) object's Selected property.
1. Finally, extract the LinkAnnotation Action as GoToURIAction.

The following code snippet shows how to get hyperlink destinations (URL) from a PDF file.

```java
    public static void GetPDFHyperlinkDestination() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Extract actions
        Page page = document.getPages().get_Item(1);
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        List<Annotation> list = selector.getSelected();
        // Iterate through individual item inside list
        if (list.size() == 0)
            System.out.println("No Hyperlinks found..");
        else {
            // Loop through all the bookmarks
            for (Annotation annot : list) {
                LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
                if (la != null) {
                    // Print the destination URL
                    System.out.println("Destination: " + ((GoToURIAction) la.getAction()).getURI());
                }
            }
        } // end else
    }
```

## Get Hyperlink Text

A hyperlink has two parts: the text that shows in the document, and the destination URL. In some cases, it's the text rather than the URL we need.

Text and annotations/actions in a PDF file are represented by different entities. Text on a page is just a set of words and characters, while annotations bring some interactivity such as that inherent in a hyperlink.

To find the URL content, you need to work with both annotation and text. The [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/Annotation) object does not have itself have the text but sits under the text on the page. So to get the text, the Annotation gives the URL's bounds, while the Text object gives the URL contents. Please see the following code snippet.

```java
    public static void GetHyperlinkText() {
        Document document = new Document(GetDataDir() + "Aspose-app-list.pdf");
        // Extract actions
        Page page = document.getPages().get_Item(1);

        for (Annotation annot : page.getAnnotations()) {
            LinkAnnotation la = (annot instanceof LinkAnnotation ? (LinkAnnotation) annot : null);
            if (la != null) {
                // Print the URL of each Link Annotation
                System.out.println("URI: " + ((GoToURIAction) la.getAction()).getURI());
                TextAbsorber absorber = new TextAbsorber();
                absorber.getTextSearchOptions().setLimitToPageBounds(true);
                absorber.getTextSearchOptions().setRectangle(annot.getRect());
                page.accept(absorber);
                String extractedText = absorber.getText();
                // Print the text associated with hyperlink
                System.out.println(extractedText);
            }
        }
    }
```

## Remove Document Open Action from a PDF File

[How to Specify PDF Page when Viewing Document](#how-to-specify-pdf-page-when-viewing-document) explained how to tell a document to open on a different page than the first. When concatenating several documents, and one or more has a GoTo action set, you probably want to remove them. For example, if combining two documents and the second one has a GoTo action that takes you to the second page, the output document will open on the second page of the second document instead of the first page of the combined document. To avoid this behavior, remove the open action command.

To remove an open action:

1. Set the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's [getOpenAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getOpenAction--) method to null.
1. Save the updated PDF using the Document object's Save method.

The following code snippet shows how to remove a document open action from the PDF file.

```java
    public static void RemoveDocumentOpenActionFromPDFFile()
    {
        // Open document
        Document document = new Document(_dataDir + "RemoveOpenAction.pdf");
        // Remove document open action
        document.setOpenAction(null);
        
        // Save updated document
        document.save(GetDataDir()+"RemoveOpenAction_out.pdf");
    }
```

## How to Specify PDF Page when Viewing Document {#how-to-specify-pdf-page-when-viewing-document}

When viewing PDF files in a PDF viewer such as Adobe Reader, the files usually open on the first page. However, it is possible to set the file to open on a different page.

The [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination) class allows you to specify a page in a PDF file that you want to open. When passing the GoToAction object value to the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class getOpenAction method, the document opens at the page specified against the XYZExplicitDestination object. The following code snippet shows how to specify a page as the document open action.

```java
    public static void HowToSpecifyPDFPageWhenViewingDocument()
    {
        // Load the PDF file
        Document document = new Document(GetDataDir()+ "SpecifyPageWhenViewing.pdf");
        // Get the instance of second page of document
        Page page2 = document.getPages().get_Item(2);
        // Create the variable to set the zoom factor of target page
        double zoom = 1;
        // Create GoToAction instance
        GoToAction action = new GoToAction(page2);
        // Go to 2 page
        action.setDestination (new XYZExplicitDestination(page2, 0, page2.getRect().getHeight(), zoom));
        // Set the document open action
        document.setOpenAction (action);
        // Save updated document
        document.save(_dataDir + "goto2page_out.pdf");
    }
}
```
