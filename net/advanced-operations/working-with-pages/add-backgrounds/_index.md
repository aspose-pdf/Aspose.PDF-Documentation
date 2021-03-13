---
title: Add background to PDF with C#
linktitle: Add backgrounds
type: docs
weight: 110
url: /net/add-backgrounds/
descriptions: Add background image to the your PDF file with C#. Use the BackgroundArtifact object.
lastmod: "2020-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for .NET, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://apireference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object with C#.

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
