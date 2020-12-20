---
title: Add various backgrounds to PDF document uisng Aspose.PDF for .NET
linktitle: Add backgrounds
type: docs
weight: 60
url: /net/add-backgrounds/
descriptions: You should use the BackgroundArtifact object if you need to add a background image to the PDF file. Check code snippet to resolve this task.
lastmod: "2020-12-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for .NET, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://apireference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Create a new Document object
Document doc = new Document();

// Add a new page to document object
Page page = doc.Pages.Add();

// Create Background Artifact object
BackgroundArtifact background = new BackgroundArtifact();

// Specify the image for backgroundartifact object
background.BackgroundImage = File.OpenRead(dataDir + "aspose-total-for-net.jpg");

// Add backgroundartifact to artifacts collection of page
page.Artifacts.Add(background);

dataDir = dataDir + "ImageAsBackground_out.pdf";
// Save the document
doc.Save(dataDir);
```
