---
title: Adding Bookmarks to PDF file
type: docs
weight: 20
url: /net/how-to-create-nested-bookmarks/
description: This section explains how to create Nested Bookmarks with PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---

Bookmarks give you the option to keep track/link to specific page inside the PDF document. [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) class in [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) provides a feature which allows you to create your own bookmark in a sophisticated yet intuitive way within an existing PDF file, at a given page or all pages.

## Implementation details

Other than the creation of simple bookmarks, sometimes you have a requirement to create a bookmark in the form of chapters where you nest the individual bookmarks inside of the chapter bookmarks so that when you click on the + sign for a chapter you would see the pages inside when the bookmarks expands, as shown in the picture below .
 
```csharp
public static void AddBookmarksAction()
{
    var document = new Document(dataDir + "Sample.pdf");
    PdfContentEditor editor = new PdfContentEditor(document);
    editor.CreateBookmarksAction("Bookmark 1", System.Drawing.Color.Green, true, false, string.Empty, "GoTo", "2");

    // Saves the result PDF to file
    editor.Save(dataDir + "PdfContentEditorDemo_Bookmark.pdf");
}
```
