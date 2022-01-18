---
title: Set Viewer Preference of PDF 
type: docs
weight: 60
url: /net/set-viewer-preference-of-an-existing-pdf-file/
description: This section shows how to set viewer preference of an existing PDF file using PdfContentEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Set Viewer Preference of an existing PDF File

[ViewerPreference](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) class represents display modes of PDF files; for example, positioning the document window in the center of the screen, hiding viewer application’s menu bar etc. 

[ChangeViewerPreference](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) method in [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class allows you to change the viewer preference. In order to do that, you need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and bind the input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index) method. 

Ater that, you can call [ChangeViewerPreference](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference)  method to set any preference. Finally, you have to save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method. The following code snippet shows you how to change viewer preference in an existing PDF file.

For example, we specify the parameter [CenterWindow](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) with which we center the window, after remove the top toolbar with [HideMenubar](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) and with [PageModeUseNone](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) open full-screen mode.

```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Change Viewer Preferences
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // Saves the result PDF to file
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```