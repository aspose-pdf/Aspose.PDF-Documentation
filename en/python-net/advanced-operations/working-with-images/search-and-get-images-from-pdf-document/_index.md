---
title: Get and Search Images in PDF
linktitle: Get and Search Images
type: docs
weight: 40
url: /python-net/search-and-get-images-from-pdf-document/
description: Learn how to search and get images from the PDF document in Python using Aspose.PDF.
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: Searching and Extracting Images from PDF 
Abstract: The Aspose.PDF for Python via .NET library offers robust capabilities for searching and extracting images from PDF documents. Utilizing the 'ImagePlacementAbsorber' class, developers can efficiently locate and access images embedded across all pages of a PDF.
---

## Inspect Image Placement Properties in a PDF Page

This example demonstrates how to analyze and display properties of all images on a specific PDF page using Aspose.PDF for Python via .NET.

1. Create an 'ImagePlacementAbsorber' to collect all images on the page.
1. Call 'document.pages[1].accept(absorber)' to analyze image placements on the first page.
1. Iterate through 'absorber.image_placements' and display key properties of each image:
    - Width and Height (points).
    - Lower-left X (LLX) and Lower-left Y (LLY) coordinates.
    - Horizontal (X) and Vertical (Y) resolution (DPI).

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## Extract and Count Image Types in a PDF

This function analyzes all images on the first page of a PDF and counts how many are grayscale and RGB images.

1. Create an 'ImagePlacementAbsorber' to collect all images on the page.
1. Initialize counters for grayscale and RGB images.
1. Call 'document.pages[1].accept(absorber)' to analyze image placements.
1. Print the total number of images found.
1. Iterate through each image in 'absorber.image_placements':
    - Get the image color type using 'image_placement.image.get_color_type()'.
    - Increment the corresponding counter (grayscaled or rgb).
    - Print a message for each image indicating whether it is grayscale or RGB.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1
```    

## Extract Detailed Image Information from a PDF

This function analyzes all images on the first page of a PDF and calculates their scaled dimensions and effective resolution based on the page’s graphics transformations.

1. Load PDF and initialize variables
1. Collect image resources
1. Process page content operators:
    - 'GSave' - push the current CTM onto the stack.
    - 'GRestore' - pop the last CTM from the stack.
    - 'ConcatenateMatrix' - update the current CTM by multiplying with the operator’s matrix.
1. Print image name, scaled dimensions, and calculated resolution.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path


    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    # Collect image names from page resources
    image_names = list(document.pages[1].resources.images.names)

    # Push identity matrix to stack
    graphics_state.append(Matrix23(1, 0, 0, 1, 0, 0))

    # Process operators on first page
    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(graphics_state[-1])

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = Matrix23(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1] = graphics_state[-1] * cm
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = graphics_state[-1]
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                # Calculate scaled dimensions
                scaled_width = math.sqrt(last_ctm.a**2 + last_ctm.b**2)
                scaled_height = math.sqrt(last_ctm.c**2 + last_ctm.d**2)

                # Original dimensions
                original_width = image.width
                original_height = image.height

                # Compute resolution
                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                # Output info
                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## Extract Alternative Text from Images in a PDF

This function retrieves alternative text (alt text) from all images on the first page of a PDF, useful for accessibility and PDF/UA compliance checks.

1. Load the PDF document using 'ap.Document()'.
1. Create an 'ImagePlacementAbsorber' to collect all images on the page.
1. Accept the absorber on the first page (page.accept(absorber)).
1. Iterate through each image in 'absorber.image_placements':
    - Print the name of the image in the page’s resource collection (get_name_in_collection()).
    - Retrieve the alternative text using 'get_alternative_text(page)'.
    - Print the first line of the alt text.

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```    