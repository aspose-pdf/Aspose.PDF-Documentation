---
title: Add Screen Annotation
type: docs
weight: 140
url: /net/add-screen-annotation/
---

# Add SWF File Annotation to PDF Document

Annotations in a PDF document are contained in a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object’s Annotations collection. This collection contains all annotations for that individual page only: every page has its own Annotations collection. To add an annotation to a particular page, add it to that page’s Annotations collection using the Add method. Use the [ScreenAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) class in the Aspose.PDF.InteractiveFeatures.Annotations namespace to include SWF files as annotations in a PDF document instead. A screen annotation specifies a region of a page upon which media clips may be played.

ScreenAnnotation takes three arguments:

1. The page you are adding the annotation to,
1. A Rectangle object which defines the area in the PDF where the annotation will be displayed, and
1. The path to the SWF multimedia file.

To add an SWF file as an annotation:

1. First, create an instance of ScreenAnnotation.
1. Then add it to the page’s Annotations collection using the Add method.
The following code snippet shows you how to add SWF annotation in a PDF page.
```
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open the PDF document
Document doc = new Document(dataDir + "AddSwfFileAsAnnotation.pdf");
            
// Get reference of the page to which you need to add the annotation
Page page = doc.Pages[1];
            
// Create ScreenAnnotation object with .swf multimedia file as an argument
ScreenAnnotation annotation = new ScreenAnnotation(page, new Aspose.Pdf.Rectangle(0, 400, 600, 700), dataDir + "input.swf");
           
// Add the annotation to annotations collection of page
page.Annotations.Add(annotation);

dataDir = dataDir + "AddSwfFileAsAnnotation_out.pdf";
// Save the update PDF document with annotation
doc.Save(dataDir);
```