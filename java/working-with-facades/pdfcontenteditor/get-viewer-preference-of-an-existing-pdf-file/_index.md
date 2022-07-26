---
title: Get Viewer Preference of an existing PDF File
type: docs
weight: 70
url: /java/get-viewer-preference-of-an-existing-pdf-file/
description: This section shows how to work with Aspose.PDF Facades using PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Get Viewer Preference of an existing PDF File

[ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) class represents display modes of PDF files; for example, positioning the document window in the center of the screen, hiding viewer application’s menu bar etc. 

In order to read the settings we use 'getViewerPreference'. This method returns a variable where all settings are saved.

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Change Viewer Preferences
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("CenterWindow");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("Menu bar hided");
        }
```