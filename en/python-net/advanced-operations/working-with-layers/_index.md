---
title: Work with PDF Layers using Python
linktitle: Work with PDF layers
type: docs
weight: 50
url: /python-net/working-with-pdf-layers/
description: Learn how to add, lock, extract, flatten, and merge PDF layers in Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manage PDF layers with Python
Abstract: This article explains how to work with PDF layers (Optional Content Groups) by using Aspose.PDF for Python via .NET. Learn how to add layers, lock layer visibility, extract layer content, flatten layered content, and merge layers into one.
---

PDF layers, also called Optional Content Groups (OCGs), let you organize content into separate visual groups that can be shown or hidden in compatible PDF viewers. In Aspose.PDF, layer operations are built around the [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API.

With Aspose.PDF for Python via .NET, you can:

- Add multiple layers to a page.
- Lock and unlock layers to control visibility behavior.
- Extract layers into separate files or streams.
- Flatten layered content into the page.
- Merge multiple layers into one layer.

## Add Layers to a PDF

This example creates a PDF with three layers. It uses a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), adds a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), and appends [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) objects to that page.

1. Create a new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) and add a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Create and add the red layer.
1. Create and add the green layer.
1. Create and add the blue layer.
1. Save the PDF document.

The resulting PDF will contain three separate layers: a red line, a green line, and a blue line. Each can be toggled on or off in PDF readers that support layered content.

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
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
    print(f"Layers added successfully. File saved at {outfile}")
```

## Lock a PDF Layer

This example opens a PDF, locks a specific layer on the first page, and saves the updated file.

Locking a layer prevents users from changing that layer's visibility state in supported PDF viewers. Layers are accessed from a page and managed through the page's layer collection.

Available methods and property:

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) locks the layer.
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) unlocks the layer.
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) returns the current lock state.

1. Open the PDF document.
1. Access the first page of the PDF.
1. Check if the page has layers.
1. Get the first layer and lock it.
1. Save the updated PDF.

If the PDF contains layers, the first layer will be locked, ensuring its visibility state cannot be changed by the user. If no layers are found, a message is printed instead.

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
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

## Extract PDF Layer Elements

This example uses the Aspose.PDF for Python via .NET library to extract individual layers from the first page of a PDF document and save each layer as a separate PDF file by using [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

To create a new PDF from a layer, the following code snippet can be used:

1. Load the PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Access layers on page 1 through [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Check whether layers exist.
1. Iterate through layers and save each one.

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
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

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## Flatten a Layered PDF

This script uses Aspose.PDF for Python via .NET to flatten all layers on the first page of a PDF document. Flattening merges the visual content of each layer into one unified layer, making it easier to print, share, or archive without losing visual fidelity or layer-specific data. The operation is performed with [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. Load the PDF document.
1. Access layers on page 1.
1. Check whether layers exist.
1. Flatten each layer with `layer.flatten(True)`.
1. Save the modified document.

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
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

## Merge All Layers in a PDF into One

This code snippet uses Aspose.PDF to merge all layers on the first page of a PDF into one unified layer with a custom name by using [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. Load the PDF document.
1. Access page 1 and retrieve its layers.
1. Check whether layers exist.
1. Define a new layer name.
1. Merge the layers into one.
1. Save the document.

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
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

## Related Layer Topics

- [Work with PDF pages in Python](/pdf/python-net/working-with-pages/)
- [Work with tables in PDF using Python](/pdf/python-net/working-with-tables/)
- [Add PDF pages in Python](/pdf/python-net/add-pages/)
