---
title: Working with Artifacts in Python via .NET
linktitle: Working with Artifacts
type: docs
weight: 170
url: /net/artifacts/
description: Aspose.PDF for Python via .NET allows you to add a background image to PDF pages, and get each watermark using Artifact class.
lastmod: "2025-05-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Artifacts in PDF are graphics objects or other elements that are not part of the actual content of the document. They are usually used for decoration, layout, or background purposes. Examples of artifacts include page headers, footers, separators, or images that do not convey any meaning.

The purpose of artifacts in PDF is to allow the distinction between content and non-content elements. This is important for accessibility, as screen readers and other assistive technologies can ignore artifacts and focus on the relevant content. Artifacts can also improve the performance and quality of PDF documents, as they can be omitted from printing, searching, or copying.

To create an element as an artifact in PDF, you need to use the [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) class.
It contains following useful properties:

**custom_type** - Gets name of artifact type. May be used if artifact type is non standard.
**custom_subtype** - Gets name of artifact subtype. May be used if artifact subtype is not standard subtype.
**typ** - Gets artifact type.
**subtype** - Gets artifact subtype. If artifact has non-standard subtype, name of the subtype may be read via CustomSubtype.
**contents** - Gets collection of artifact internal operators.
**form** - Gets XForm of the artifact (if XForm is used).
**rectangle** - Gets rectangle of the artifact.
**position** - Gets or sets artifact position. If this property is specified, then margins and alignments are ignored.
**right_margin** - Right margin of artifact.If position is specified explicitly (in Position property) this value is ignored.
**left_margin** - Left margin of artifact.If position is specified explicitly (in Position property) this value is ignored.
**top_margin** - Top margin of artifact. If position is specified explicitly (in Position property) this value is ignored.
**bottom_margin** - Bottom margin of artifact.If position is specified explicitly (in Position property) this value is ignored.
**artifact_horizontal_alignment** - Horizontal alignment of artifact. If position is specified explicitly (in Position property) this value is ignored.
**artifact_vertical_alignment** - Vertical alignment of artifact. If position is specified explicitly (in Position property) this value is ignored.
**rotation** - Gets or sets artifact rotation angle.
**text** - Gets text of the artifact.
**image** - Gets image of the artifact (if presents).
**opacity** - Gets or sets opacity of the artifact. Possible values are in range 0..1.
**lines** - Lines of multiline text artifact.
**text_state** - Text state for artifact text.
**is_background** - If true Artifact is placed behind page contents.

The following classes may also be useful for work with artifacts:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)

## Working with Existing Watermarks

A watermark created with Adobe Acrobat is called an artifact (as described in 14.8.2.2 Real Content and Artifacts of the PDF specification).

In order to get all Watermarks on a particular page, the [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) class has the 'artifacts' property.

The following code snippet shows how to get all watermarks on the first page of a PDF file:

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Get the watermarks from the first page artifacts
        watermarks = [
            artifact for artifact in document.pages[0].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION and
                artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        # Iterate through the found watermark artifacts and print details
        for watermark_item in watermarks:
            print(f"{watermark_item.text} {watermark_item.rectangle}")
```

## Working with Backgrounds as Artifacts

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for Python via .NET, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object.

```python

    import aspose.pdf as ap

    # Open PDF document
    with Document(path_infile) as pdf_document:
        # Create a new BackgroundArtifact and set the background image
        background_artifact = ap.BackgroundArtifact()
        background_artifact.background_image = open(path_imagefile, 'rb')

        # Add the background image to the first page's artifacts
        pdf_document.pages[1].artifacts.add(background_artifact)

        # Save PDF document with the added background
        pdf_document.save(path_outfile)
```

If you want, for some reason, to use a solid color background, please change the previous code in the following manner:

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a new BackgroundArtifact and set the background color
        background_artifact = ap.BackgroundArtifact()
        background_artifact.background_color = ap.Color.dark_khaki

        # Add the background color to the first page's artifacts
        document.pages[1].artifacts.add(background_artifact)

        # Save PDF document
        document.save(path_outfile)
```

## Counting Artifacts of a Particular Type

To calculate the total count of artifacts of a particular type (for example, the total number of watermarks), use the following code:

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Get pagination artifacts from the first page
        pagination_artifacts = [artifact for artifact in document.pages[1].artifacts
                                if artifact.type == ap.Artifact.ArtifactType.PAGINATION]

        # Count and display the number of each artifact type
        print("Watermarks: {}".format(
            sum(1 for artifact in pagination_artifacts
                if artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK)))
        print("Backgrounds: {}".format(
            sum(1 for artifact in pagination_artifacts
                if artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND)))
        print("Headers: {}".format(
            sum(1 for artifact in pagination_artifacts
                if artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER)))
        print("Footers: {}".format(
            sum(1 for artifact in pagination_artifacts
                if artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER)))
```

## Adding Bates Numbering Artifact

This example illustrates how to programmatically add Bates numbering to a PDF document using Aspose.PDF for Python via .NET. By configuring the BatesNArtifact with desired settings and applying it to the document's pages, you can automate the process of adding standardized identifiers to each page.

To add a Bates numbering artifact to a document, call the `AddBatesNumbering(BatesNArtifact)` extension method on the `PageCollection`, passing the `BatesNArtifact` object as a parameter:

```python

    import aspose.pdf as ap

    # Create or open PDF document
    with ap.Document() as document:
        # Add 10 pages
        for page_index in range(10):
            document.pages.add()

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(ap.BatesNArtifact(
            # These properties are set to their default values, as if they were not specified
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        ))

        # Save PDF document
        document.save(path_outfile)
```

Or, you can pass a collection of `PaginationArtifacts`:

```python

    import aspose.pdf as ap

    # Create or open PDF document
    with ap.Document() as document:
        # Add 10 pages
        for page_index in range(10):
            document.pages.add()

        # Add Bates numbering to all pages
        document.pages.add_pagination([
            ap.BatesNArtifact(
                # These properties are set to their default values, as if they were not specified
                start_page=1,
                end_page=0,
                subset=ap.Subset.ALL,
                number_of_digits=6,
                start_number=1,
                prefix="",
                suffix="",
                artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
                artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
                right_margin=72,
                left_margin=72,
                top_margin=36,
                bottom_margin=36
            )
        ])

        # Save PDF document
        document.save(path_outfile)
```

Add a Bates numbering artifact using an action delegate:

```python

    import aspose.pdf as ap

    # Create or open PDF document
    with ap.Document() as document:
        # Add 10 pages
        for page_index in range(10):
            document.pages.add()

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(lambda bates_numbering: (
            # These properties are set to their default values, as if they were not specified
            setattr(bates_numbering, 'start_page', 1),
            setattr(bates_numbering, 'end_page', 0),
            setattr(bates_numbering, 'subset', Subset.All),
            setattr(bates_numbering, 'number_of_digits', 6),
            setattr(bates_numbering, 'start_number', 1),
            setattr(bates_numbering, 'prefix', ""),
            setattr(bates_numbering, 'suffix', ""),
            setattr(bates_numbering, 'artifact_vertical_alignment', ap.VerticalAlignment.BOTTOM),
            setattr(bates_numbering, 'artifact_horizontal_alignment', ap.HorizontalAlignment.RIGHT),
            setattr(bates_numbering, 'right_margin', 72),
            setattr(bates_numbering, 'left_margin', 72),
            setattr(bates_numbering, 'top_margin', 36),
            setattr(bates_numbering, 'bottom_margin', 36),
            setattr(bates_numbering.text_state, 'font_size', 10)
        ))

        # Save PDF document
        document.save(path_outfile)
```

To delete Bates numbering, use the following code:

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Delete Bates numbering from all pages

        document.pages.delete_bates_numbering()

        # Save PDF document
        document.save(path_outfile)
```