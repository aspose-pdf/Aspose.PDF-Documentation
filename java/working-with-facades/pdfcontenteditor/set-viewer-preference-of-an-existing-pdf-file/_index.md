---
title: Set Viewer Preference of an existing PDF File
type: docs
weight: 60
url: /java/set-viewer-preference-of-an-existing-pdf-file/
description: This section shows how to work with Aspose.PDF Facades using PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Set Viewer Preference of an existing PDF File

[ViewerPreference](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) class represents display modes of PDF files; for example, positioning the document window in the center of the screen, hiding viewer application’s menu bar etc. 

[ChangeViewerPreference](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) method in [PdfContentEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) class allows you to change the viewer preference. In order to do that, you need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) class and bind the input PDF file using [bindPdf](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-) method.

Ater that, you can call [ChangeViewerPreference](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-)  method to set any preference. Finally, you have to save the updated PDF file using Save method. The following code snippet shows you how to change viewer preference in an existing PDF file.

For example, we specify the parameter [CENTER WINDOW](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW) with which we center the window, after remove the top toolbar with [HIDE MENUBAR](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR) and with [PAGE MODE USE NONE](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE) open full-screen mode.

```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Change Viewer Preferences
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```