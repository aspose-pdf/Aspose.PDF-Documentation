---
title: Work with PDF Layers in Python
linktitle: Working with PDF layers
type: docs
weight: 50
url: /python-net/work-with-pdf-layers/
description: Learn how to lock, extract, flatten, and merge PDF layers in Python using Aspose.PDF for Python via .NET.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to manage, lock, extract, flatten, and merge PDF layers in Python
Abstract: This article explains how to work with PDF layers in Aspose.PDF for Python via .NET. Learn how to lock optional content layers, extract layer content, flatten layered PDFs, and merge layers into a single result in Python workflows.
---

PDF layers (optional content groups) allow a document to contain multiple sets of content that can be shown or hidden. They are useful for maps, technical drawings, and documents that need alternate views.

The examples in this article use [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), and [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) APIs in Aspose.PDF for Python via .NET.

Use this page when you need to:

- Create layers in a PDF.
- Lock or unlock layers.
- Extract layer content.
- Flatten layers for fixed output.
- Merge layers into one.

## Add layers to PDF

This example creates a new PDF and adds three layers (red, green, blue), each with its own line drawing.

```python
import aspose.pdf as ap
from os import path


def add_colored_layers(outfile: str, data_dir: str) -> None:
    path_outfile = path.join(data_dir, outfile)

    document = ap.Document()
    page = document.pages.add()

    def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
        layer = ap.Layer(layer_id, layer_name)
        layer.contents.append(ap.operators.SetRGBColorStroke(*color))
        layer.contents.append(ap.operators.MoveTo(500, y_position))
        layer.contents.append(ap.operators.LineTo(400, y_position))
        layer.contents.append(ap.operators.Stroke())
        page.layers.append(layer)

    add_layer("oc1", "Red Line", (1, 0, 0), 700)
    add_layer("oc2", "Green Line", (0, 1, 0), 750)
    add_layer("oc3", "Blue Line", (0, 0, 1), 800)

    document.save(path_outfile)
```

## Lock a PDF layer

Locking a layer prevents users from changing its visibility in compatible PDF viewers.

Layer members:

- `layer.lock()` - Lock the layer.
- `layer.unlock()` - Unlock the layer.
- `layer.locked` - Check whether the layer is currently locked.

```python
import aspose.pdf as ap


def lock_layer(path_infile: str, path_outfile: str) -> None:
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        if not page.layers:
            return

        layer = page.layers[0]
        layer.lock()
        document.save(path_outfile)
```

## Extract PDF layer elements

You can save each layer from a page to a separate PDF file:

```python
import aspose.pdf as ap


def save_layers(path_infile: str, path_out_prefix: str) -> None:
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for i, layer in enumerate(layers):
            layer.save(f"{path_out_prefix}_layer_{i}.pdf")
```

You can also save layer content into memory streams:

```python
import io
import aspose.pdf as ap


def save_layers_to_stream(path_infile: str):
    with ap.Document(path_infile) as document:
        streams = []
        for layer in document.pages[1].layers:
            stream = io.BytesIO()
            layer.save(stream)
            stream.seek(0)
            streams.append(stream)
        return streams
```

## Flatten a layered PDF

Flattening turns layer content into regular page content and removes layer toggle behavior.

```python
import aspose.pdf as ap


def flatten_layers(path_infile: str, path_outfile: str) -> None:
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

The `cleanup_content_stream` parameter controls whether optional content markers are removed. See [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) for details.

## Merge all PDF layers into one

Use [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) to merge all page layers into one new layer.

```python
import aspose.pdf as ap


def merge_layers(
    path_infile: str,
    path_outfile: str,
    new_layer_name: str,
    optional_group_id: str = None,
) -> None:
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```

## Related Topics

- [Advanced PDF operations in Python](/pdf/python-net/advanced-operations/)
- [Work with PDF documents in Python](/pdf/python-net/working-with-documents/)
- [Work with PDF pages in Python](/pdf/python-net/working-with-pages/)
- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)