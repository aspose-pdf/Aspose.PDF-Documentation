---
title: Extract Images from PDF File using Python
linktitle: Extract Images
type: docs
weight: 30
url: /python-net/extract-images-from-pdf-file/
description: This section shows how to extract images from PDF file using Python library.
lastmod: "2025-09-27"
TechArticle: true 
AlternativeHeadline: Extract images from PDF with Python
Abstract: This article discusses the process of extracting images from PDF files using Aspose.PDF for Python. It highlights the utility of separating images for purposes such as management, archiving, analysis, or sharing. The article explains that images within a PDF are stored in each page's resources collection, specifically within the XImage collection. To extract an image, users can access a particular page and retrieve the image using its index from the Images collection. The XImage object returned by the index provides a `save()` method to save the extracted image. A code snippet is provided to demonstrate the steps required to open a PDF document, extract a specific image from the second page using its index, and save it to a file.
---

Do you need to separate images from your PDF files? For simplified management, archiving, analysis, or sharing images of your documents, use **Aspose.PDF for Python** and extract images from PDF files.

1. Load the PDF document with 'ap.Document()'.
1. Access the desired page of the document (document.pages[1]).
1. Select the image from the page resources (for example, resources.images[1]).
1. Create an output stream (FileIO) for the target file.
1. Save the extracted image using 'xImage.save(output_image)'.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## Extract Images from Specific Region in PDF

This method extracts images located within a specified rectangular region on a PDF page and saves them as separate files.

1. Load the PDF document using 'ap.Document'.
1. Create an 'ImagePlacementAbsorber' to collect all images on the first page.
1. Call 'document.pages[1].accept(absorber)' to analyze image placements.
1. Iterate through all images in 'absorber.image_placements':
    - Get the image bounding box (llx, lly, urx, ury).
    - Check if both corners of the image rectangle fall inside the target rectangle (rectangle.contains()).
    - If true, save the image to a file using FileIO, replacing 'index' in the filename with a sequential number.
1. Increment the index for each saved image.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## Extract Image Information from PDF

The example below demonstrates how to analyze images embedded in a PDF page and calculate their effective resolution.

1. Open the PDF with 'ap.Document'.
1. Track graphics state while reading page content.
1. Handle operators:
    - 'GSave'/'GRestore' - push/pop matrix.
    - 'ConcatenateMatrix' - update transform.
    - 'Do' - if it’s an image, get size & apply transform.
1. Calculate effective DPI.
1. Print image name, scaled size, and DPI.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```