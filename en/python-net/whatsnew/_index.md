---
title: What's new
linktitle: What's new
type: docs
weight: 10
url: /python-net/whatsnew/
description: In this page introduces the most popular new features in Aspose.PDF for Python via .NET that have been introduced in recent releases.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2025-02-24"
TechArticle: false 
---

## What's new in Aspose.PDF 25.9

The 25.9 release introduces improved accessibility, enhanced compliance support, and new API capabilities for working with tagged images and document standards. 

1. Convert PDFs to PDF/E-1 format.
1. Add tagged images from memory streams.

### Convert PDF to PDF/E-1 Format

In the 25.9 version of the Aspose.PDF for Python library, PDF/E-1 format conversion is available. You can find more information about this format on the [(File Formats Docs)[https://docs.fileformat.com/pdf/e/]. 

```python

import aspose.pdf as ap

def convert_pdf_to_pdf_e(self, infile, outfile):
    """PDF/E-1 Standard Support: Added the capability to convert PDF files to the PDF/E-1 format and to validate
        the output files for compliance with the standard."""

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Set up the PDF/E-1 format with PdfFormatConversionOptions
        options = ap.PdfFormatConversionOptions(ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE)
        # Convert to PDF/E-1 compliant document
        document.convert(options)
        # Save PDF document
        document.save(path_outfile)
```

### Add Tagged Images from a Stream

Add Tagged Images from a Stream in PDF. 25.9 version supports enhanced accessibility in PDF documents by adding an image from a memory stream and tagging it with alternative text.

```python

import io
import aspose.pdf as ap

def add_tagged_image_from_stream(self, image_file, outfile):
    """Enhanced Accessibility for Tagged Images: possible to add alternative text to images loaded from a memory stream."""

    path_image = self.data_dir + image_file
    path_outfile = self.data_dir + outfile

    # Create the PDF document
    with ap.Document() as document:

        page = document.pages.add()
        # Tag the document for accessibility
        tagged_content = document.tagged_content
        tagged_content.set_title("Tagged Image from Stream")
        tagged_content.set_language("en-US")
        # Add an image from a stream to the page
        image_stream = io.FileIO(path_image, "r")
        page.add_image(image_stream, ap.Rectangle(100, 600, 300, 800, True), None, True)
        # Get the added image and set its alternative text
        img = page.resources.images[1]
        img.try_set_alternative_text("Aspose Logo", page)
        # Save the document
        document.save(path_outfile)
```

## What's new in Aspose.PDF 25.8

This update adds more flexibility in layout and document security management.

1. Create tagged tables of contents (TOC).
1. Resize PDF pages with content scaling.
1. Apply dashed borders to tables.

### Create Tagged Table of Contents (TOC)

Automatically generate accessible tables of contents (TOC) in tagged PDFs. Creating a fully accessible Table of Contents (TOC) in a PDF allows readers to navigate the document efficiently and ensures PDF/UA-1 compliance for accessibility.

```python

import aspose.pdf as ap

def create_pdf_with_toc_page(self, outfile):
    """
    Supports generating fully accessible Tagged Table of Contents (TOC) pages with proper navigation to
    corresponding sections, ensuring PDF/UA-1 compliance.
    """

    path_outfile = self.data_dir + outfile

    # Create the PDF document
    with ap.Document() as document:
        # Get tagged content for the PDF structure
        content = document.tagged_content
        root_element = content.root_element
        content.set_language("en-US")
        # Add the table of contents (TOC) page
        toc_page = document.pages.add()
        toc_page.toc_info = ap.TocInfo()
        # Create a TOC structure element
        toc_element = content.create_toc_element()
        # Add the TOC element to the document structure tree
        root_element.append_child(toc_element, True)
        # Add a content page
        document.pages.add()
        # Create a header element and set its text
        header = content.create_header_element(1)
        header.set_text("1. Header")
        # Add the header to the document structure
        root_element.append_child(header, True)
        # Create a TOC item (TOCI) element
        toci = content.create_toci_element()
        # Add the TOCI element to the TOC element
        toc_element.append_child(toci, True)
        # Add an entry to the TOC page and link it to the TOCI element
        header.add_entry_to_toc_page(toc_page, toci)
        # Add a logical reference to the header within the TOCI element
        toci.add_ref(header)
        # Save PDF document
        document.save(path_outfile)
```

### Resize Pages with Content Scaling

Resize PDF pages while preserving layout and proportionally scaling content. When working with PDFs, you may need to resize pages or scale content to fit new dimensions.

```python

import aspose.pdf as ap

def resize_page(self, document, page_number, target_width, target_height, width, height, outfile):
    """
    Resize and scale page content using PdfFileEditor.ResizeContents.

    A high-level helper that scales and/or resizes the rendered content streams of one or more pages
    without performing a full content reflow. Use this to make existing page contents larger or smaller,
    fit content into a different page box, or uniformly scale content for printing or display.

    Parameters (recommended)
    ------------------------
    pdf_editor : Aspose.Pdf.Facades.PdfFileEditor
        The PdfFileEditor instance that exposes the ResizeContents API.
    page_numbers : int | Iterable[int] | slice, optional
        Page index (1-based) or collection of page indices to process. If omitted or None, all pages
        in the document are processed.
    scale : float, optional
        Uniform scale factor to apply to content (e.g., 0.5 reduces content to 50%). Mutually exclusive
        with target_width/target_height unless keep_aspect_ratio is explicitly handled.
    target_width : float, optional
        Desired content width in PDF points (1 point = 1/72 inch). When provided, content will be scaled
        to match this width (subject to keep_aspect_ratio and fit_mode).
    target_height : float, optional
        Desired content height in PDF points.
    keep_aspect_ratio : bool, default True
        If True, preserve the original aspect ratio when scaling to a target width or height.
    fit_mode : {'fit', 'fill', 'stretch'}, default 'fit'
        'fit'   — scale so content fits entirely inside the target box, preserving aspect ratio;
        'fill'  — scale so the target box is completely covered (may crop content);
        'stretch' — scale independently in X and Y (may distort).
    margins : tuple(float, float, float, float), optional
        (left, top, right, bottom) margins in points to preserve inside the target box.
    preserve_annotations : bool, default True
        When True, attempt to preserve annotations/forms/interactive elements; some annotations may
        require special handling after scaling.
    preserve_transparency : bool, default True
        Preserve transparency settings of page contents where possible.

    Returns
    -------
    bool
        True if the operation completed successfully. Some implementations operate in-place and may
        return a status rather than a new document object.

    Raises
    ------
    ValueError
        If parameters are invalid (e.g., scale <= 0 or both scale and conflicting target dimensions).
    IOError
        If input/output streams cannot be read or written.
    PdfProcessingError
        If the PDF content streams cannot be interpreted or transformed by the editor.

    Notes
    -----
    - All size and margin values are in PDF points (1/72 inch). Convert from inches or millimeters
      before calling if necessary.
    - This API scales content streams and their transform matrices; it does not reflow text or rebuild
      page layout. Text encoded as vectors will scale; text drawn by layout engines may not reflow.
    - Complex page objects such as XObjects, forms, and annotations may require additional post-processing.
    - For raster-output use-cases (images/screenshots), consider exporting to an image at a target DPI
      instead of scaling content streams.
    - When targeting printing, compute target page size in points from the physical paper size and DPI.

    Example (conceptual)
    --------------------
    # Scale pages 1-3 to 50%:
    editor = PdfFileEditor(input_stream, output_stream)
    editor.ResizeContents(page_numbers=[1,2,3], scale=0.5)
    editor.Save()

    # Fit page content into a letter-sized box while preserving aspect ratio:
    editor.ResizeContents(page_numbers=None, target_width=612, target_height=792, fit_mode='fit')

    See also
    --------
    PdfFileEditor.ResizeContents : Low-level API that performs content scaling and transform adjustments.
    """

    path_outfile = self.data_dir + outfile

    margin_width = (target_width - width) / 2
    margin_height = (target_height - height) / 2

    # Set the parameters
    param = ap.facades.PdfFileEditor.ContentsResizeParameters.page_resize(width, height)
    param.top_margin = ap.facades.PdfFileEditor.ContentsResizeValue.units(margin_height)
    param.bottom_margin = ap.facades.PdfFileEditor.ContentsResizeValue.units(margin_height)
    param.left_margin = ap.facades.PdfFileEditor.ContentsResizeValue.units(margin_width)
    param.right_margin = ap.facades.PdfFileEditor.ContentsResizeValue.units(margin_width)
    param.change_media_box = True

    # Do resize
    ap.facades.PdfFileEditor().resize_contents(document, [page_number], param)

    document.save(path_outfile)
```

### Apply Dashed Borders to Tables

Add tables with custom border styles using dashed lines. This example demonstrates how to apply custom border styles—such as dashed or dotted lines—to tables in a PDF document using Aspose.PDF for Python via .NET.

```python

import aspose.pdf as ap

def create_table_with_dashed_border(self, outfile):
    """Support style  for table borders, allowing you to set dashed, dotted, or custom border styles for tables."""

    path_outfile = self.data_dir + outfile

    # Create the PDF document
    with ap.Document() as document:

        page = document.pages.add()
        table = ap.Table()
        graph_info = ap.GraphInfo()
        graph_info.dash_array = [10, 10]
        graph_info.dash_phase = 5
        graph_info.line_width = 3
        table.border = ap.BorderInfo(ap.BorderSide.BOX, graph_info)
        row = table.rows.add()
        row.cells.add("Dashed border cell")

        page.paragraphs.add(table)

        document.save(path_outfile)
```

## What's new in Aspose.PDF 25.7

The 25.7 release focuses on better annotation support, text fitting, and digital signature management.

1. Fit text inside shapes.
1. Encrypt PDFs using a public certificate.
1. Add cloud and polygon annotations.

### Encrypt PDFs with a Public Certificate

Secure your PDFs with encryption based on public certificates. Public certificate encryption allows PDFs to be encrypted for specific recipients, ensuring that only holders of the corresponding private keys can open and read the document.

```python

import aspose.pdf as ap

def pub_sec_encryption(self, outfile, pub_cert, crypto_algorithm):
    """Support for public certificate encryption, allowing PDFs to be encrypted so that only specified certificate
        holders can open the document."""

    # The path to the recipient certificate
    path_outfile = self.data_dir + outfile
    path_cert = self.data_dir + pub_cert

    # Create the PDF document
    with ap.Document() as document:
        # Add an info
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"

        # Add a page and add some text
        page = document.pages.add()
        text = ap.text.TextFragment("Hello World!")
        page.paragraphs.add(text)

        # Load certificate
        with open(path_cert, "rb") as f:
            cert_data = f.read()

        # Encrypt the PDF document
        document.encrypt(ap.Permissions.PRINT_DOCUMENT, crypto_algorithm, [cert_data])

        # Save the PDF document. A private key certificate must be installed in the storage to open the document
        # by Adobe Acrobat.
        document.save(path_outfile)
```

### Fit Text Within a Rectangle

Automatically scale text to fit inside a defined rectangle. When updating or expanding text in a PDF, it may exceed the original paragraph bounds.

```python

import re
import aspose.pdf as ap

def fit_text_into_rectangle(self, infile, outfile):
    """New functionality to fit expanded text content within the bounds of a paragraph’s original rectangle,
        adjusting font size and spacing automatically."""

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Extract the paragraph text (or provide the specific text you want to replace)
        text_absorber = ap.text.TextAbsorber()
        text_absorber.visit(document)
        paragraph_text = text_absorber.text
        paragraph_text = paragraph_text.replace("\n", " ")

        # Search for the text fragment
        searchable_content = re.sub(" ", r"\\s+", paragraph_text)
        text_fragment_absorber = ap.text.TextFragmentAbsorber(searchable_content, ap.text.TextSearchOptions(True))
        document.pages.accept(text_fragment_absorber)
        text_fragment = text_fragment_absorber.text_fragments[1]
        # Use the text fragment’s rectangle as the target replacement area
        text_fragment.replace_options.rectangle = text_fragment.rectangle
        # Enable font size reduction to fit the text within the specified area
        text_fragment.replace_options.font_size_adjustment_action = ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        # Optionally adjust spacing to justify the text width
        text_fragment.replace_options.replace_adjustment_action = ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        # Duplicate the paragraph content and assign it to the text fragment
        text_fragment.text = paragraph_text + " " + paragraph_text
        # Save PDF document
        document.save(path_outfile)
```

### Add Cloud Polygon Annotations

Enhance PDF review workflows with cloud or polygon-style annotations. Polygon annotations allow you to highlight or emphasize specific areas in a PDF using geometric shapes.

```python

import aspose.pdf as ap

def add_cloud_polygon_annotation(self, outfile):
    """The ability to apply “Cloudy” border effects to polygon annotations for enhanced visual appearance."""

    path_outfile = self.data_dir + outfile

    # Create the PDF document
    with ap.Document() as document:

        page = document.pages.add()
        # Add Cloud Polygon (rectangle)
        left = 100.0
        top = 270.0
        right = 420.0
        bottom = 80.0
        cloud_polygon = ap.annotations.PolygonAnnotation(page,ap.Rectangle(left, top, right, bottom, True),
                                                            [ap.Point(left, top),ap.Point(right, top),
                                                            ap.Point(right, bottom), ap.Point(left, bottom)])
        cloud_polygon.color = ap.Color.blue
        border = ap.annotations.Border(cloud_polygon)
        border.width = 3
        border.effect = ap.annotations.BorderEffect.CLOUDY
        cloud_polygon.border = border
        page.annotations.append(cloud_polygon)
        # Add another Cloud Polygon
        cloud_polygon = ap.annotations.PolygonAnnotation(page, ap.Rectangle(400, 400, 580, 600, True),
                                                            [ap.Point(400, 450), ap.Point(450, 300),
                                                            ap.Point(520, 300), ap.Point(580, 500),
                                                            ap.Point(500, 600)])
        cloud_polygon.color = ap.Color.dark_green
        cloud_polygon.interior_color = ap.Color.aqua
        border = ap.annotations.Border(cloud_polygon)
        border.width = 3
        border.effect = ap.annotations.BorderEffect.CLOUDY
        cloud_polygon.border = border
        page.annotations.append(cloud_polygon)
        # Save PDF document
        document.save(path_outfile)
```

## What's new in Aspose.PDF 25.6

The main features of this release:

1. Image Alt Text Support.
1. License Info Access.
1. Styled Free Text Annotations.
1. Customizable Digital Signature Appearance.

### Image Alt Text Support

Set and retrieve alternative text for images to improve accessibility for screen readers.

```python

import aspose.pdf as ap

def get_set_alternative_text_for_image(self, infile, outfile):
    """To get and set the alternative text for images"""

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Alternative text to be given to the image
        alt_text = "Alternative text for image"
        # Image for which alternative text will be set and get
        x_image = document.pages[1].resources.images[1]
        # Try to set alternative text for an image
        result = x_image.try_set_alternative_text(alt_text, document.pages[1])
        # If set is successful, then get the alternative text for the image
        if (result):
            alt_texts = x_image.get_alternative_text(document.pages[1])
        # Save PDF document
        document.save(path_outfile)
```

### License Info Access

Retrieve detailed license metadata (licensed user, expiry date) via LicenseInfo.

```python

import aspose.pdf as ap

def get_license_info_example(self, infile):
    """A new way to access license information programmatically through the LicenseInfo property of the License class"""

    path_infile = self.data_dir + infile

    # Initialize license object
    lic = ap.License()
    # Set license
    lic.set_license(path_infile)
    # Get license info.
    lic_license_info = lic.license_info
    print(lic_license_info.licensed_to)
    print(lic_license_info.subscription_expiry)
```

### Styled Free Text Annotations

Use SetTextStyle to apply styles like bold, italic, underline, or clear existing formatting to annotation text.

```python

import aspose.pdf as ap

def add_free_annotation_and_set_styles(self, outfile):
    """Extended formatting capabilities for annotation text through the SetTextStyle method family of the
        FreeTextAnnotation class"""

    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document() as document:
        # Add new page
        page = document.pages.add()
        # Instantiate DefaultAppearance object
        default_appearance = ap.annotations.DefaultAppearance("Arial", 16, drawing.Color.blue)
        # Create annotation
        free_text = ap.annotations.FreeTextAnnotation(page, ap.Rectangle(20, 600, 400, 650, True), default_appearance)
        # Specify the contents of annotation
        free_text.contents = "Text of FreeTextAnnotation with different styles"
        # Add annotation to annotations collection of page
        page.annotations.append(free_text)
        # Set styles for annotation text
        free_text.set_text_style(0, 4, ap.annotations.RichTextFontStyles.ITALIC)
        free_text.set_text_style(8, 26, ap.annotations.RichTextFontStyles.UNDERLINE | ap.annotations.RichTextFontStyles.BOLD)
        free_text.set_text_style(27, 86, ap.annotations.RichTextFontStyles.BOLD)
        free_text.set_text_style(42, 45, ap.annotations.RichTextFontStyles.CLEAR_EXISTING | ap.annotations.RichTextFontStyles.UNDERLINE)
        # Save PDF document
        document.save(path_outfile)
```

### Customizable Digital Signature Appearance

Add images, change fonts, and layer signature graphics over background content for better branding or design consistency.

```python

import aspose.pdf as ap

def customization_features_for_digital_sign(self, infile, outfile, image_file, pfx_file):
    """Enhanced digital signature appearance allowing signature images to appear over background text."""

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_image = self.data_dir + image_file
    path_pfx = self.data_dir + pfx_file

    with ap.facades.PdfFileSignature() as pdf_file_signature:
        # Bind PDF document
        pdf_file_signature.bind_pdf(path_infile)
        # Create a rectangle for signature location
        rect = drawing.Rectangle(10, 10, 300, 50)
        # Create any of the three signature types
        signature = ap.forms.PKCS7Detached(path_pfx, "12345")
        # Create signature appearance
        signature_custom_appearance = ap.forms.SignatureCustomAppearance()
        signature_custom_appearance.font_size = 6
        signature_custom_appearance.font_family_name = "Times New Roman"
        signature_custom_appearance.digital_signed_label = "Signed by:"
        signature_custom_appearance.is_foreground_image = True
        # Set signature appearance
        signature.custom_appearance = signature_custom_appearance
        # Set signature appearance
        pdf_file_signature.signature_appearance = path_image
        pdf_file_signature.sign(1, True, rect, signature)
        #  Save PDF document
        pdf_file_signature.save(path_outfile)
```

## What's new in Aspose.PDF 25.5

The latest Aspose.PDF update introduces several powerful enhancements that improve document accessibility, compatibility, and security. Developers can now extract digital certificates directly from signed PDF files, enabling advanced verification and compliance checks.

1. Extract Certificates from PDF Signatures.
1. Create Structured Ordered Lists in Tagged PDFs.
1. Verify Signatures with Public Key Certificates.
1. Convert Dynamic XFA Forms to AcroForm PDFs.
1. Font Replacement in PDF - XPS Conversion.

### Extract Certificates from PDF Signatures

Retrieve embedded certificates using 'extract_certificate()'.

```python

import aspose.pdf as ap

def extract_certificate(self, infile):
    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            # Get signature names
            signature_names = signature.get_signature_names(True)
            for signature_name in signature_names:
                # Extract certificate
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print(certificate[0] is not None)
```

### Create Structured Ordered Lists in Tagged PDFs

Generate accessible numbered lists (with nested items) inside tagged documents.

```python

import aspose.pdf as ap

def create_ordered_list(self, outfile):

    path_outfile = self.data_dir + outfile

    # Create or open PDF document
    with ap.Document() as document:
    content = document.tagged_content
    root_element = content.root_element
    content.set_language("en-US")
    root_list = content.create_list_element()
    span_for_lbl_1 = content.create_span_element()
    span_for_lbl_1.set_text("1. ")
    position_settings = ap.tagged.PositionSettings()
    position_settings.is_in_line_paragraph = True
    span_for_lbl_1.adjust_position(position_settings)
    span_for_body_1 = content.create_span_element()
    span_for_body_1.set_text("bread")
    span_for_body_1.adjust_position(position_settings)
    lbl_1 = content.create_list_lbl_element()
    lbl_1.append_child(span_for_body_1, True)
    l_body_1 = content.create_list_l_body_element()
    l_body_1.append_child(span_for_lbl_1, True)
    li_1 = content.create_list_li_element()
    li_1.append_child(lbl_1, True)
    li_1.append_child(l_body_1, True)
    root_list.append_child(li_1, True)
    span_for_lbl_2 = content.create_span_element()
    span_for_lbl_2.set_text("2. ")
    span_for_body_2 = content.create_span_element()
    span_for_body_2.set_text("milk")
    span_for_body_2.adjust_position(position_settings)
    lbl_2 = content.create_list_lbl_element()
    lbl_2.append_child(span_for_lbl_2, True)
    l_body_2 = content.create_list_l_body_element()
    l_body_2.append_child(span_for_body_2, True)
    li_2 = content.create_list_li_element()
    li_2.append_child(lbl_2, True)
    li_2.append_child(l_body_2, True)
    root_list.append_child(li_2, True)
    nested_list_depth_1 = content.create_list_element()
    span_for_lbl_3_1 = content.create_span_element()
    span_for_lbl_3_1.set_text("3.1. ")
    position_settings_lbl_3_1 = ap.tagged.PositionSettings()
    position_settings_lbl_3_1.is_in_line_paragraph = False
    margin_info = ap.MarginInfo()
    margin_info.left = 50
    position_settings_lbl_3_1.margin = margin_info
    span_for_lbl_3_1.adjust_position(position_settings_lbl_3_1)
    span_for_body_3_1 = content.create_span_element()
    span_for_body_3_1.set_text("apples")
    span_for_body_3_1.adjust_position(position_settings)
    lbl_3_1 = content.create_list_lbl_element()
    lbl_3_1.append_child(span_for_lbl_3_1, True)
    l_body_3_1 = content.create_list_l_body_element()
    l_body_3_1.append_child(span_for_body_3_1, True)
    li_3_1 = content.create_list_li_element()
    li_3_1.append_child(lbl_3_1, True)
    li_3_1.append_child(l_body_3_1, True)
    nested_list_depth_1.append_child(li_3_1, True)
    span_for_lbl_3_2 = content.create_span_element()
    span_for_lbl_3_2.set_text("3.2. ")
    span_for_lbl_3_2.adjust_position(position_settings_lbl_3_1)
    span_for_body_3_2 = content.create_span_element()
    span_for_body_3_2.set_text("banana")
    span_for_body_3_2.adjust_position(position_settings)
    lbl_3_2 = content.create_list_lbl_element()
    lbl_3_2.append_child(span_for_lbl_3_2, True)
    l_body_3_2 = content.create_list_l_body_element()
    l_body_3_2.append_child(span_for_body_3_2, True)
    li_3_2 = content.create_list_li_element()
    li_3_2.append_child(lbl_3_2, True)
    li_3_2.append_child(l_body_3_2, True)
    nested_list_depth_1.append_child(li_3_2, True)
    span_for_lbl_3 = content.create_span_element()
    span_for_lbl_3.set_text("3. ")
    span_for_body_3 = content.create_span_element()
    span_for_body_3.set_text("fruits")
    span_for_body_3.adjust_position(position_settings)
    lbl_3 = content.create_list_lbl_element()
    lbl_3.append_child(span_for_lbl_3, True)
    l_body_3 = content.create_list_l_body_element()
    l_body_3.append_child(span_for_body_3, True)
    li_3 = content.create_list_li_element()
    li_3.append_child(lbl_3, True)
    li_3.append_child(l_body_3, True)
    l_body_3.append_child(nested_list_depth_1, True)
    root_list.append_child(li_3, True)
    root_element.append_child(root_list, True)
    # Save Tagged PDF Document
    document.save(path_outfile)
```

### Verify Signatures with Public Key Certificates

Validate digital signatures using external public key certs.

```python

import aspose.pdf as ap

def verify_with_public_key_certificate1(self, certificate, infile):
    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

### Convert Dynamic XFA Forms to AcroForm PDFs

Standardize XFA forms with 'ignore_needs_rendering'.

```python

import aspose.pdf as ap

def convert_xfa_form_with_ignore_needs_rendering(self, infile, outfile):
    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```

### Font Replacement in PDF - XPS Conversion

Substitute missing fonts with a default fallback (e.g., “Courier New”).

```python

import aspose.pdf as ap

def replace_font_when_converting_pdf_to_xps(self, infile, outfile):
    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Create XpsSaveOptions instance
    xps_save_options = ap.XpsSaveOptions()
    # use_embedded_true_type_fonts option specifies whether to use embedded TrueType fonts
    xps_save_options.use_embedded_true_type_fonts = False
    # The specified default font will be used if the embedded font name cannot be found in the system
    xps_save_options.default_font = "Courier New"
    # Open PDF document
    doc = ap.Document(path_infile)
    # Save the resultant XPS
    doc.save(path_outfile, xps_save_options)
```

## What's new in Aspose.PDF 25.4

### Auto-Tagging During PDF/A Conversion

Convert PDFs to PDF/A-1b with automatic logical structure creation for improved accessibility.

```python

import aspose.pdf as ap

def convert_to_pdfa_with_automatic_tagging(self, infile, outfile, outlogfile):
    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_outlogfile = self.data_dir + outlogfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create conversion options
        options = ap.PdfFormatConversionOptions(path_outlogfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
        # Create auto-tagging settings
        # aspose.pdf.AutoTaggingSettings.default may be used to set the same settings as given below
        auto_tagging_settings = ap.AutoTaggingSettings()
        # Enable auto-tagging during the conversion process
        auto_tagging_settings.enable_auto_tagging = True
        # Use the heading recognition strategy that's optimal for the given document structure
        auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO
        # Assign auto-tagging settings to be used during the conversion process
        options.auto_tagging_settings = auto_tagging_settings
        # During the conversion, the document logical structure will be automatically created
        document.convert(options)
        # Save PDF document
        document.save(path_outfile)
```

