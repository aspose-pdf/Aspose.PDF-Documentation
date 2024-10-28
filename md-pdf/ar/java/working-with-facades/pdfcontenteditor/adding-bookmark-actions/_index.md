---
title: Adding Bookmark actions to existing PDF file
type: docs
weight: 20
url: /java/adding-bookmark-actions/
description: This section explains how to add Bookmark actions to existing PDF file with Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) class present under com.aspose.pdf.facades package provides the flexibility to add Bookmark actions to a PDF file. You can create a link with the serial actions corresponding to execute a menu item in the PDF viewer. This class also provides the feature to create additional actions for document events. 

The following code example demonstrates how to add a Bookmark zction to a PDF document. If you click on this tab, the desired action is performed. With the help of a Bookmark, clicking on it, we perform the desired action. Then create an [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-), set the parameters of the text, colors, indicate the name of the bookmark, and also indicate the page number. The last action is done with "GoTo", it allows you to go from anywhere to the page we need.

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Bookmark 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // Saves the result PDF to file
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```