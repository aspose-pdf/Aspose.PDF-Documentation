---
title: Work with PDF layers using C#
linktitle: Work with PDF layers
type: docs
weight: 80
url: /net/work-with-pdf-layers/
description: The next task explains how to lock a PDF layer, extract PDF layer elements, flatten a layered PDF, and merge all layers inside PDF into one.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDF layers allow a PDF document to contain different sets of content that can be selectively viewed or hidden. Each layer in a PDF may include text, images, or graphics, and users can toggle these layers on or off, depending on their needs. Layers are often used in complex documents where different content needs to be organized or separated.

## Lock a PDF layer

With Aspose.PDF for .NET you can open a PDF, lock a specific layer on the first page, and save the document with the changes.

Since the 24.5 release, this feature has been implemented. 

There are two new methods and one property was added:

- Layer.Lock(); -  Locks the layer.
- Layer.Unlock(); - Unlocks the layer.
- Layer.Locked; - Property, indicating the layer locked state.

```cs
var document = new Document(input);
var page = document.Pages[1];
var layer = page.Layers[0];

layer.Lock();

document.Save(output);
```

## Extract PDF layer elements

The Aspose.PDF for .NET library allows extracts of each layer from the first page and saves each layer to a separate file.

To create a new PDF from a layer, the following code snippet can be used:

```cs
var document = new Document(inputPath);
var layers = document.Pages[1].Layers;

foreach (var layer in layers)
{
    layer.Save(outputPath);
}
```

The 24.9 release has resulted in an update to this feature.

It is possible to extract PDF layer elements and save them into a new PDF file stream:

```cs
var document = new Document(inputPath);
var layers = document.Pages[1].Layers;

foreach (var layer in layers)
{
    Layer.Save(Stream outputStream);
}
```

## Flatten a layered PDF

Aspose.PDF for .NET library opens a PDF, iterates through each layer on the first page, and flattens each layer, making it permanent on the page.

```cs
var document = new Document(input);
var page = document.Pages[1];

foreach (var layer in page.Layers)
{
    layer.Flatten(true);
}
```

The 'Layer.Flatten(bool cleanupContentStream)' method accepts the boolean parameter that specifies whether to remove optional content group markers from the content stream. Setting the cleanupContentStream parameter to false speeds up the process of flattening.

## Merge All Layers inside the PDF into one

The Aspose.PDF for .NET library allows merges either all PDF layers or a specific layer on the first page into a new layer and saves the updated document.

Two methods were added to merge all layers on the page:

- void MergeLayers(string newLayerName).
- void MergeLayers(string newLayerName, string newOptionalContentGroupId).

The second parameter allows renaming the optional content group marker. The default value is "oc1" (/OC /oc1 BDC).

```cs
var document = new Document(input);
var page = document.Pages[1];

page.MergeLayers("NewLayerName");

// Or page.MergeLayers("NewLayerName", "OC1");

document.Save(output);
```