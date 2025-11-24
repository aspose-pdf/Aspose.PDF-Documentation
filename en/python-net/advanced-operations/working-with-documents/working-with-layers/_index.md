---
title: Work with PDF layers using Python
linktitle: Work with PDF layers
type: docs
weight: 50
url: /python-net/working-with-pdf-layers/
description: The next task explains how to lock a PDF layer, extract PDF layer elements, flatten a layered PDF, and merge all layers inside PDF into one.
lastmod: "2025-11-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manipulate the PDF Layers
Abstract: This guide provides a comprehensive overview of how to manage and manipulate PDF layers using the Aspose.PDF for Python via .NET library. PDF layers—also known as Optional Content Groups (OCGs)—enable the organization of content into separate visual components that can be toggled on or off.  
---

PDF layers are a powerful way to organize and present content flexibly inside a single PDF file, allowing users to show or hide different parts depending on their needs.

With **Aspose.PDF for Python via .NET**, you can:

 - Lock/Unlock layers to control visibility.
 - Extract layers into separate files or streams.
 - Flatten layers to make them permanent.
 - Merge layers into a single unified layer.

## Add layers to PDF

This example shows how to create and add multiple layers  to a PDF document using Aspose.PDF for Python via .NET. Each layer contains separate graphical content, such as colored lines, which can be turned on or off in PDF viewers that support layers.

1. Create a new PDF document and add a page.
1. Create and add the red layer.
1. Create and add the green layer.
1. Create and add the blue layer.
1. Save the PDF document.

The resulting PDF will contain three separate layers: a red line, a green line, and a blue line. Each can be toggled on or off in PDF readers that support layered content.

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## Lock a PDF layer

With Aspose.PDF for Python via .NET you can open a PDF, lock a specific layer on the first page, and save the document with the changes.

This example shows how to lock a layer (Optional Content Group, OCG) in a PDF document using Aspose.PDF for Python via .NET. Locking prevents users from changing the visibility of the layer in a PDF viewer, ensuring that the content remains always visible (or hidden) as defined by the document.

Available methods and property:

 - layer.lock() – Locks the layer.
 - layer.unlock() – Unlocks the layer.
 - layer.locked – Returns the current lock state.

1. Open the PDF document.
1. Access the first page of the PDF.
1. Check if the page has layers.
1. Get the first layer and lock it.
1. Save the updated PDF.

If the PDF contains layers, the first layer will be locked, ensuring its visibility state cannot be changed by the user. If no layers are found, a message is printed instead.

```python

import aspose.pdf as ap
from os import path

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

This example uses the Aspose.PDF for Python via .NET library to extract individual layers from the first page of a PDF document and save each layer as a separate PDF file.

To create a new PDF from a layer, the following code snippet can be used:

1. Load the PDF Document. The input PDF is loaded into an Aspose.PDF.Document object.
1. Access Layers on Page 1. The script retrieves all layers from the first page using document.pages[1].layers.
1. Check for Layers. If no layers are found, a message is printed and the function exits.
1. Iterate and Save Each Layer.

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

It is possible to extract PDF layer elements and save them into a new PDF file stream:

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## Flatten a layered PDF

This script uses Aspose.PDF for Python via .NET to flatten all layers on the first page of a PDF document. Flattening merges the visual content of each layer into one unified layer, making it easier to print, share, or archive without losing visual fidelity or layer-specific data.

1. Load the PDF Document. The input PDF is loaded into an Aspose.PDF.Document object.
1. Access Layers on Page 1. The script retrieves all layers from the first page using document.pages[1].layers.
1. Check for Layer Presence. If no layers are found, a message is printed and the function exits.
1. Flatten Each Layer. Each layer is flattened using layer.flatten(True), which merges its content into the page.
1. Save the Modified Document.

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## Merge All Layers inside the PDF into one

This code snippet uses Aspose.PDF to merge all layers on the first page of a PDF into one unified layer with a custom name.

1. Load the PDF Document. The PDF is loaded into an Aspose.PDF.Document object.
1. Access Page and Its Layers. The first page is selected, and its layers are retrieved.
1. Check for Layers. If no layers exist, a message is printed and the process exits.
1. Define New Layer Name. A new layer name ("LayerNew") is specified for the merged result.
1. Merge Layers. If an optional content group ID is provided, it's used in the merge. Otherwise, layers are merged using just the new name.
1. Save the Document

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```