---
title: Working with PDF layers using Python
linktitle: Working with PDF layers
type: docs
weight: 50
url: /python-net/work-with-pdf-layers/
description: The next task explains how to lock a PDF layer, extract PDF layer elements, flatten a layered PDF, and merge all layers inside PDF into one.
lastmod: "2025-11-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract:       
---

PDF layers allow a document to contain multiple sets of content that can be selectively shown or hidden. Each layer may include text, images, or graphics, and users can toggle them on or off as needed. Layers are especially useful in complex documents where content must be organized or separated.

## Lock a PDF layer

With Aspose.PDF for Python via .NET you can open a PDF, lock a specific layer on the first page, and save the document with the changes.

Available methods and property:

 - layer.lock() – Locks the layer.
 - layer.unlock() – Unlocks the layer.
 - layer.locked – Returns the current lock state.

1. Open the PDF document.
1. Retrieve the first page with 'document.pages'.
1. Select the layer to lock.
1. Call 'layer.lock()' to prevent users from toggling the layer’s visibility.
1. Save the updated document.

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

Aspose.PDF allows you to extract each layer from a page and save it as a separate PDF file.

To create a new PDF from a layer, the following code snippet can be used:

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

You can also save layers into a stream:

```python

import aspose.pdf as ap

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## Flatten a layered PDF

Flattening makes a layer permanent on the page, removing its toggle functionality.

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

The 'cleanup_content_stream' parameter controls whether optional content group markers are removed. Setting it to 'False' speeds up flattening.

## Merge All Layers inside the PDF into one

You can merge all layers (or specific ones) into a single new layer.

Methods:

 - page.merge_layers(new_layer_name)
 - page.merge_layers(new_layer_name, new_optional_content_group_id)

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