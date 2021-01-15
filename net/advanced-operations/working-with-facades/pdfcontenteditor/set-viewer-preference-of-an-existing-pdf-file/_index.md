---
title: Set Viewer Preference of an existing PDF File
type: docs
weight: 70
url: /net/set-viewer-preference-of-an-existing-pdf-file/
description: This section shows how to work with Aspose.PDF Facades using PdfContentEditor Class.
lastmod: "2021-01-15"
draft: false
---

## Set Viewer Preference of an existing PDF File

[ViewerPreference](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) class represents display modes of PDF files; for example, positioning the document window in the center of the screen, hiding viewer application’s menu bar etc. [ChangeViewerPreference](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) method in [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class allows you to change the viewer preference. In order to do that, you need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and bind the input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index) method. Ater that, you can call [ChangeViewerPreference](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference)  method to set any preference. Finally, you have to save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method. The following code snippet shows you how to change viewer preference in an existing PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();
// Open document
PdfContentEditor contentEditor = new PdfContentEditor();
contentEditor.BindPdf(dataDir + "SetViewerPreference.pdf");

// Change Viewer Preferences
contentEditor.ChangeViewerPreference(ViewerPreference.CenterWindow);
contentEditor.ChangeViewerPreference(ViewerPreference.HideMenubar);
contentEditor.ChangeViewerPreference(ViewerPreference.PageModeUseNone);

// Save output PDF file
contentEditor.Save(dataDir+ "SetViewerPreference_out.pdf");
```