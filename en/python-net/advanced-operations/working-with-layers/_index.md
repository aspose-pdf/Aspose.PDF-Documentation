---
title: Working with PDF layers using Python
linktitle: Working with PDF layers
type: docs
weight: 50
url: /python-net/work-with-pdf-layers/
description: This article explains how to lock a PDF layer, extract PDF layer elements, flatten a layered PDF, and merge all layers inside a PDF into one.
lastmod: "2025-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to manage, lock, extract, flatten, and merge PDF layers in Python
Abstract: This article explains how to work with PDF layers in Python using Aspose.PDF for .NET, including locking layers, extracting layer elements, flattening layered PDFs, and merging layers.
---

PDF layers allow a document to contain multiple sets of content that can be selectively shown or hidden. Each layer may include text, images, or graphics, and users can toggle them on or off as needed. Layers are especially useful in complex documents where content must be organized or separated. The examples below use the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) and [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) APIs and manipulate [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) objects via the page's `layers` collection.

## Lock a PDF layer

With Aspose.PDF for Python via .NET you can open a PDF (see [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)), lock a specific [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) on the first [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), and save the document with the changes.

Available methods and property on the [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) object:

 - `layer.lock()` – Locks the layer. (see [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
 - `layer.unlock()` – Unlocks the layer. (see [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
 - `layer.locked` – Returns the current lock state. (see [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties))

1. Open the PDF document (see [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Retrieve the first page using the document's [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) collection (see [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).
1. Select the [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) to lock from `page.layers`.
1. Call `layer.lock()` to prevent users from toggling the layer’s visibility.
1. Save the updated document using [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Extract PDF layer elements

Aspose.PDF allows you to extract each [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) from a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) and save it as a separate PDF file.

To create a new PDF from a layer, the following code snippet can be used (the `layers` collection is accessed via `Page.layers`):

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

You can also save layers into a stream:

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## Flatten a layered PDF

Flattening makes a [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) permanent on the page, removing its toggle functionality.

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

The `cleanup_content_stream` parameter controls whether optional content group markers (OCG markers) are removed. Setting it to `False` speeds up flattening. See the [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) method for details.

## Merge All Layers inside the PDF into one

You can merge all layers (or specific ones) into a single new [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) (the merge API is on the [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) object).

Methods on the [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) object:

 - `page.merge_layers(new_layer_name)` — merge all layers into a new layer name (see [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).
 - `page.merge_layers(new_layer_name, new_optional_content_group_id)` — merge using a custom optional content group ID (see [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```