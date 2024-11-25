---
title: Get Viewer Preference of PDF File
type: docs
weight: 70
url: /net/get-viewer-preference-of-an-existing-pdf-file/
description: This section shows how to get viewer preference of an existing PDF file using PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Get Viewer Preference of an existing PDF File

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) class represents display modes of PDF files; for example, positioning the document window in the center of the screen, hiding viewer application's menu bar etc. 

In order to read the settings we use [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference) class. This method returns a variable where all settings are saved.

```csharp
public static void GetViewerPreference()
{
    var document = new Document(dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
    PdfContentEditor editor = new PdfContentEditor(document);

    // Change Viewer Preferences
    var preferences = editor.GetViewerPreference();
    if ((preferences & ViewerPreference.CenterWindow) != 0)
    {
        Console.WriteLine("CenterWindow");
    }

    if ((preferences & ViewerPreference.HideMenubar) != 0)
    {
        Console.WriteLine("Menu bar hided");
    }

    if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
    {
        Console.WriteLine("Page Mode Full Screen");
    }
}
```