---
title: Add, Delete and Get Annotation in existing PDF file | Aspose.PDF
linktitle: Add, Delete and Get Annotation in existing PDF file 
type: docs
weight: 10
url: /net/add-annotation-in-existing-pdf-file/
description: This page describes how to add an annotation in an existing PDF file. Also, you may delete all or particular annotations from a page of a PDF file.
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Add, Delete, and Get Annotation are similar for different kinds of annotations. Let take as example a Text Annotation.

## How to add Text Annotation into existing PDF file

A Text Annotation is an annotation attached to a specific location in a PDF document. When closed, the annotation is displayed as an icon; when opened, it should display a pop-up window containing the note text in the font and size chosen by the reader.

Annotations are contained by the [Annotations](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations) collection of a particular Page. This collection contains the annotations for that individual page only; every page has its own Annotations collection.

To add an annotation to a particular page, add it to that page’s Annotations collection with the [Add](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add) method.

1. First, create an annotation that you want to add to the PDF.
1. Then open the input PDF.
1. Add the annotation to the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object’s Annotations collection.

The following code snippet shows you how to add an annotation in a PDF page.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// Create annotation
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "Sample Annotation Title";
textAnnotation.Subject = "Sample Subject";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "Sample contents for the annotation";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// Add annotation in the annotations collection of the page
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// Save output file
pdfDocument.Save(dataDir);
```

## Delete All Annotations from a Page of a PDF File

A [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object’s [AnnotationCollection](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection contains all the annotations for that particular page. To delete all the annotations from a page, call the *Delete* method of the AnnotationCollectoin collection.

The following code snippet shows you how to delete all the annotations from a particular page.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// Delete particular annotation
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

## Delete a Particular Annotation from the PDF File

{{% alert color="primary" %}}

You can check the quality of Aspose.PDF and get the results online at this link:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF allows you to remove a particular Annotation from PDF file. This topic explains how.

To delete a particular annotation from a PDF, call the [AnnotationCollection collection’s Delete method](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). This collection belongs to the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object. The Delete method requires the index of the annotation you want to delete. Then, save the updated PDF file. The following code snippet shows how to delete a particular annotation.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// Delete particular annotation
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// Save updated document
pdfDocument.Save(dataDir);
```

## Get All Annotations from the Page of a PDF Document

Aspose.PDF allows you to get annotations from an entire document, or from a given page. To get all annotations from the page in a PDF document, loop through the [AnnotationCollection](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection of desired page resources. The following code snippet shows you how to get all the annotations of a page.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// Loop through all the annotations
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // Get annotation properties
    Console.WriteLine("Title : {0} ", annotation.Title);
    Console.WriteLine("Subject : {0} ", annotation.Subject);
    Console.WriteLine("Contents : {0} ", annotation.Contents);
}
```

Please note that to get all annotations from the whole PDF, you have to loop through the document’s PageCollection Class collection before navigating through the AnnotationCollection class collection. You can get each annotation of the collection in a base annotation type called MarkupAnnotation Class and then show its properties.

## Get Particular Annotation from a PDF File

Annotations are associated with individual pages and stored in a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object’s [AnnotationCOllection](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) collection. To get a particular annotation, specify its index. This returns an [Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) object which needs to be cast to a particular annotation type, for example [TextAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/textannotation). The following code snippet shows how to get a particular annotation and its properties.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// Get particular annotation
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// Get annotation properties
Console.WriteLine("Title : {0} ", textAnnotation.Title);
Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
```

## Get Resource of Annotation

Aspose.PDF allows you to get a resource of annotation from an entire document, or from a given page. The following code snippet shows you how to get the resource of annotation as [FileSpecification](https://apireference.aspose.com/pdf/net/aspose.pdf/filespecification) object of input PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Open document
Document doc = new Document(dataDir + "AddAnnotation.pdf");
//Create annotation
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// Save Doucument
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// Open document
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

//Get action of the annotation
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

//Get rendition of the rendition action
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

//Media Clip
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
//Data of media are accessible in FileSpecification.Contents
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
```
