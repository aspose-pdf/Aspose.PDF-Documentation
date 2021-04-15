---
title: Create Links in PDF file with C#
linktitle: Create Links
type: docs
weight: 10
url: /net/create-links/
description: This section explains how to create links in your PDF document with C#. 
lastmod: "2021-03-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Create Links

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