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
from io import FileIO
import aspose.pdf as ap
import sys
from os import path

def add_layers(outfile):
    """
    Add three colored line layers (red, green, blue) to a new PDF document.

    Args:
        outfile (str): The filename for the output PDF file

    Returns:
        None

    Example:
        >>> add_layers("output.pdf")

    Note:
        Creates a PDF with three layers containing horizontal lines:
        - "Red Line" at y=700
        - "Green Line" at y=750
        - "Blue Line" at y=800
    """
    path_outfile = path.join(outfile)

    try:
        document = ap.Document()
        page = document.pages.add()

        # Red layer
        layer = ap.Layer("oc1", "Red Line")
        layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
        layer.contents.append(ap.operators.MoveTo(500, 700))
        layer.contents.append(ap.operators.LineTo(400, 700))
        layer.contents.append(ap.operators.Stroke())
        page.layers.append(layer)

        # Green layer
        layer = ap.Layer("oc2", "Green Line")
        layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
        layer.contents.append(ap.operators.MoveTo(500, 750))
        layer.contents.append(ap.operators.LineTo(400, 750))
        layer.contents.append(ap.operators.Stroke())
        page.layers.append(layer)

        # Blue layer
        layer = ap.Layer("oc3", "Blue Line")
        layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
        layer.contents.append(ap.operators.MoveTo(500, 800))
        layer.contents.append(ap.operators.LineTo(400, 800))
        layer.contents.append(ap.operators.Stroke())
        page.layers.append(layer)

        document.save(outfile)
        print(f"\nLayers added successfully to PDF file.\nFile saved at {path_outfile}")
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
from io import FileIO
import aspose.pdf as ap
import sys
from os import path

def lock_layer(infile, outfile):
    """
    Lock the first layer of the first page in a document.

    Args:
        infile (str): The name of the input file
        outfile (str): The name of the output file

    Returns:
        None

    Example:
        >>> lock_layer("input.pdf", "locked_output.pdf")

    Note:
        If no layers are found, prints a message and returns without saving.
    """

    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## Extract PDF layer elements

This example uses the Aspose.PDF for Python via .NET library to extract individual layers from the first page of a PDF document and save each layer as a separate PDF file.

To create a new PDF from a layer, the following code snippet can be used:

1. Load the PDF Document. The input PDF is loaded into an Aspose.PDF.Document object.
1. Access Layers on Page 1. The script retrieves all layers from the first page using document.pages[1].layers.
1. Check for Layers. If no layers are found, a message is printed and the function exits.
1. Iterate and Save Each Layer.

```python
from io import FileIO
import aspose.pdf as ap
import sys
from os import path

def extract_layers(infile, outfile):
    """
    Extract all layers from the first page and save each as a separate file.

    Args:
        infile (str): The name of the input PDF file
        outfile (str): The base name for output files (index will be appended)

    Returns:
        None

    Example:
        >>> extract_layers("input.pdf", "layer_output.pdf")
        # Creates layer_output1.pdf, layer_output2.pdf, etc.

    Note:
        Only extracts layers from the first page of the input PDF.
    """
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

It is possible to extract PDF layer elements and save them into a new PDF file stream:

```python
from io import FileIO
import aspose.pdf as ap
import sys
from os import path

def extract_layers_stream(infile, outfile):
    """
    Extract the first layer from the first page and save it to a stream.

    Args:
        infile (str): The name of the input file
        outfile (str): The name of the output file

    Returns:
        None

    Example:
        >>> extract_layers_stream("input.pdf", "layer.pdf")

    Note:
        If no layers are found on the first page, prints a message and returns.
        The extracted layer is saved as a binary stream.
    """

    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## Flatten a layered PDF

This script uses Aspose.PDF for Python via .NET to flatten all layers on the first page of a PDF document. Flattening merges the visual content of each layer into one unified layer, making it easier to print, share, or archive without losing visual fidelity or layer-specific data.

1. Load the PDF Document. The input PDF is loaded into an Aspose.PDF.Document object.
1. Access Layers on Page 1. The script retrieves all layers from the first page using document.pages[1].layers.
1. Check for Layer Presence. If no layers are found, a message is printed and the function exits.
1. Flatten Each Layer. Each layer is flattened using layer.flatten(True), which merges its content into the page.
1. Save the Modified Document.

```python
from io import FileIO
import aspose.pdf as ap
import sys
from os import path

def flatten_layers(infile, outfile):
    """
    Flatten all layers of the first page in a document.

    Args:
        infile (str): The name of the input file
        outfile (str): The name of the output file

    Returns:
        None

    Example:
        >>> flatten_layers("input.pdf", "flattened.pdf")

    Note:
        Flattening makes all layers permanent and non-toggleable.
    """

    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
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
from io import FileIO
import aspose.pdf as ap
import sys
from os import path

def merge_layers(infile, outfile):
    """
    Merge all layers of the first page into a single layer.

    Args:
        infile (str): The name of the input file
        outfile (str): The name of the output file

    Returns:
        None

    Example:
        >>> merge_layers("input.pdf", "merged.pdf")

    Note:
        All layers are combined into a new layer named "LayerNew".
    """

    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```