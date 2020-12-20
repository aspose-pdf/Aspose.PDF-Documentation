---
title: Add Links to PDF programmatically using Aspose.PDF for .NET
linktitle: Links
type: docs
weight: 10
url: /net/links/
description: Add links to PDF programmatically. This guide is about how to add an internal page link in PDF or insert an external website hyperlink to PDF in C# language.
lastmod: "2020-12-18"
---

## Create, Update and Extract

By adding a link to an application into a document, it is possible to link to applications from a document. This is useful when you want readers to take a certain action at a specific point in a tutorial, for example, or to create a feature-rich document. To create an application link:

1. [Create a Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Get the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) you want to add link to.
1. Create a [LinkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object using the Page and [Rectangle](https://apireference.aspose.com/pdf/net/aspose.pdf/rectangle) objects.
1. Set the link attributes using the [LinkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object.
1. Also, set the to [LaunchAction](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction) object’s Action property.
1. When creating the [LaunchAction](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/launchaction) object, specify the application you want to launch.
1. Add the link to the Page object’s [Annotations](https://apireference.aspose.com/pdf/net/aspose.pdf/page/properties/annotations) property.
1. Finally, save the updated PDF using the Document object’s [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method.

The following code snippet shows how to create a link to an application in a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Open document
Document document = new Document( dataDir + "CreateApplicationLink.pdf");

// Create link
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new LaunchAction(document, dataDir + "CreateApplicationLink.pdf");
page.Annotations.Add(link);

dataDir = dataDir + "CreateApplicationLink_out.pdf";
// Save updated document
document.Save(dataDir);
```

### Create PDF Document Link in a PDF File

Aspose.PDF for .NET allows you to add a link to an external PDF file so that you can link several documents together. To create a PDF document link:

1. First, create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Then, get the particular [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) you want to add the link to.
1. Create a [LinkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object using the Page and [Rectangle](https://apireference.aspose.com/pdf/net/aspose.pdf/rectangle) objects.
1. Set the link attributes using the [LinkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object.
1. Set the Action property to the [GoToRemoteAction](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/gotoremoteaction) object.
1. While creating the GoToRemoteAction object, specify the PDF file that should launch, as well as the page number it should open on.
1. Add the link to the Page object’s Annotations collection.
1. Save the updated PDF using the Document object’s [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method.

The following code snippet shows how to create PDF document link in a PDF file.

 ```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Open document
Document document = new Document(dataDir+ "CreateDocumentLink.pdf");
// Create link
Page page = document.Pages[1];
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
link.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
link.Action = new GoToRemoteAction(dataDir + "RemoveOpenAction.pdf", 1);
page.Annotations.Add(link);
dataDir = dataDir + "CreateDocumentLink_out.pdf";
// Save updated document
document.Save(dataDir);
```

## Update Links in a PDF File

As discussed in Add Hyperlink in a PDF File, the [LinkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) class makes it possible to add links in a PDF file. There’s also a similar class used to get existing links from inside PDF files. Use this if you need to update an existing link. To update an existing link:

1. Load a PDF file.
1. Go to a specific page in the PDF file.
1. Specify the link destination using the [GoToAction](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) object’s Destination property.
1. The destination page is specified using the [XYZExplicitDestination](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) constructor.

### Set Link Target to a Page in the Same Document

The following code snippet shows you how to update a link in a PDF file and set its target to the second page of the document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Load the PDF file
Document doc = new Document(dataDir + "UpdateLinks.pdf");
// Get the first link annotation from first page of document
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Modification link: change link destination
GoToAction goToAction = (GoToAction)linkAnnot.Action;
// Specify the destination for link object
// The first parameter is document object, second is destination page number.
// The 5ht argument is zoom factor when displaying the respective page. When using 2, the page will be displayed in 200% zoom
goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);
dataDir = dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf";
// Save the document with updated link
doc.Save(dataDir);
```

### Set Link Destination to a Web Address

To update the hyperlink so that it points to a web address, instantiate the [GoToURIAction](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) object and pass it to the LinkAnnotation’s Action property. The following code snippet shows how to update a link in a PDF file and set its target to a web address.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Load the PDF file
Document doc = new Document(dataDir + "UpdateLinks.pdf");

// Get the first link annotation from first page of document
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Modification link: change link action and set target as web address
linkAnnot.Action = new GoToURIAction("www.aspose.com");

dataDir = dataDir + "SetDestinationLink_out.pdf";
// Save the document with updated link
doc.Save(dataDir);
```

### Set Link Target to Another PDF File

The following code snippet shows how to update a link in a PDF file and set its target to another PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Load the PDF file
Document document = new Document(dataDir + "UpdateLinks.pdf");

LinkAnnotation linkAnnot = (LinkAnnotation)document.Pages[1].Annotations[1];

GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.Action;
// Next line update destination, do not update file
goToR.Destination = new XYZExplicitDestination(2, 0, 0, 1.5);
// Next line update file
goToR.File = new FileSpecification(dataDir +  "input.pdf");

dataDir = dataDir + "SetTargetLink_out.pdf";
// Save the document with updated link
document.Save(dataDir);
```

### Update LinkAnnotation Text Color

The link annotation does not contain text. Instead, the text is placed in the contents of the page under the annotation. Therefore, to change the color of the text, replace the color of the page text instead of trying change color of the annotation. The following code snippet shows how to update the color of link annotation in a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Load the PDF file
Document doc = new Document(dataDir + "UpdateLinks.pdf");
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    if (annotation is LinkAnnotation)
    {
        // Search the text under the annotation
        TextFragmentAbsorber ta = new TextFragmentAbsorber();
        Rectangle rect = annotation.Rect;
        rect.LLX -= 10;
        rect.LLY -= 10;
        rect.URX += 10;
        rect.URY += 10;
        ta.TextSearchOptions = new TextSearchOptions(rect);
        ta.Visit(doc.Pages[1]);
        // Change color of the text.
        foreach (TextFragment tf in ta.TextFragments)
        {
            tf.TextState.ForegroundColor = Color.Red;
        }
    }

}
dataDir = dataDir + "UpdateLinkTextColor_out.pdf";
// Save the document with updated link
doc.Save(dataDir);
```

## Extract Links from the PDF File

Links are represented as annotations in a PDF file, so to extract links, extract all the [LinkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) objects.

1. Create a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Get the [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) you want to extract links from.
1. Use the [AnnotationSelector](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) class to extract all the [LinkAnnotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) objects from the specified page.
1. Pass the [AnnotationSelector](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) object to the Page object’s Accept method.
1. Get all the selected link annotations into an IList object using the [AnnotationSelector](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) object’s Selected property.

The following code snippet shows you how to extract links from a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Open document
Document document = new Document(dataDir+ "ExtractLinks.pdf");
// Extract actions
Page page = document.Pages[1];
AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));
page.Accept(selector);
IList<Annotation> list = selector.Selected;
Annotation annotation = (Annotation)list[0];
dataDir = dataDir + "ExtractLinks_out.pdf";
// Save updated document
document.Save(dataDir);
```
