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
TechArticle: true 
AlternativeHeadline: Popular New Features in Aspose.PDF for Python via .NET
Abstract: The article outlines the new features introduced in various versions of Aspose.PDF for Python. Introduced the ability to save PDFs to HTML without including raster images, validate PDF signatures using a Certificate Authority server, and cross-platform PDF signature validation using SHA-3 hashing algorithms. Features include converting annotation documents to PDF/X-1 using a custom ICC profile and handling font issues in PDF to PNG conversions. Improvements were also made to text stamp annotations to adjust font size automatically. New options for setting the hashing algorithm for Pkcs7Detached signatures and font encoding strategies during PDF to HTML conversion were introduced.
---

## What's new in Aspose.PDF 25.1

An option to save PDF to HTML by skipping all raster images.

```python

    import aspose.pdf as ap

    def save_pdf_to_html_without_images(input_pdf_path: str, output_html_path: str):
        doc = ap.Document(input_pdf_path)
        html_save_options = ap.HtmlSaveOptions()
        html_save_options.explicit_list_of_saved_pages = [1]
        html_save_options.fixed_layout = True
        html_save_options.font_saving_mode = ap.HtmlSaveOptions.FontSavingModes.ALWAYS_SAVE_AS_WOFF
        html_save_options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
        html_save_options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.DONT_SAVE
        doc.save(output_html_path, html_save_options)
```

Possibility to validate a PDF signature using a Certificate Authority (CA) Server:

```python

    import aspose.pdf as ap

    def verify_signature_with_options(input_pdf_path: str):
        document = ap.Document(input_pdf_path)
        pdf_sign = ap.facades.PdfFileSignature(document)
        for sign_name in pdf_sign.get_sign_names(True):
            options = ap.security.ValidationOptions()
            options.validation_mode = ap.security.ValidationMode.STRICT
            options.validation_method = ap.security.ValidationMethod.AUTO
            options.request_timeout = 20000
            validation_results = []
            verified = pdf_sign.verify_signature(sign_name, options, validation_results)
            print(validation_results[0].status)
            print(validation_results[0].message)
```

Cross-platform PDF signature validation using SHA-3 hashing algorithms:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing


    def sign_with_sha3(input_pdf_path: str, cert: str, password: str, output_pdf_path: str):
        document = ap.Document(input_pdf_path)
        pdf_sign = ap.facades.PdfFileSignature(document)
        pkcs = ap.forms.PKCS7Detached(cert, password, ap.DigestHashAlgorithm.SHA_3_256) # // ap.DigestHashAlgorithm.SHA_3_384, ap.DigestHashAlgorithm.SHA_3_512
        pdf_sign.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
        pdf_sign.save(output_pdf_path)


    def verify(signed_pdf_file: str):
        document = ap.Document(signed_pdf_file)
        signature = ap.facades.PdfFileSignature(document)
        sig_names = signature.get_sign_names(True)
        for sig_name in sig_names:
            is_valid = signature.verify_signature(sig_name)
```

## What's new in Aspose.PDF 24.12

The following snippet shows how to convert the annotation document to PDF/X-1 using the annotation FOGRA39 ICC profile:

```python

    import aspose.pdf as ap

    def convert_pdf_to_pdf_x_1_using_custom_icc_profile(input_pdf_path: str, output_pdf_path: str):
        document = ap.Document(input_pdf_path)
        options = ap.PdfFormatConversionOptions(ap.PdfFormat.PDF_X_1A, ap.ConvertErrorAction.DELETE)
        options.icc_profile_file_name = "Coated_Fogra39L_VIGC_300.icc"
        options.output_intent = ap.OutputIntent("FOGRA39")
        document.convert(options)
        document.save(output_pdf_path)
```

The following sample shows how this can be used in PDF to PNG conversion to avoid text getting turned into blank squares:

```python

    import aspose.pdf as ap

    def pdf_to_png_with_analyzing_fonts(input_pdf_path: str, output_pdf_path: str):
        document = ap.Document(input_pdf_path)
        png_device = ap.devices.PngDevice()
        png_device.rendering_options = ap.RenderingOptions()
        png_device.rendering_options.analyze_fonts = True
        png_device.process(document.pages[1], output_pdf_path) 
```

The following code snippet demonstrates how to add annotation text stamp to annotation PDF file and automatically adjust the font size to fit the stamp rectangle:

```python

    import aspose.pdf as ap

    def auto_set_the_font_size_of_text_stamp(input_pdf_path: str, output_pdf_path: str):
        document = ap.Document(input_pdf_path)
        text = "Stamp example"
        stamp = ap.TextStamp(text)
        stamp.auto_adjust_font_size_to_fit_stamp_rectangle = True
        stamp.auto_adjust_font_size_precision = 0.01
        stamp.word_wrap_mode = ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
        stamp.scale = False
        stamp.width = 400
        stamp.height = 200
        document.pages[1].add_stamp(stamp)
        document.save(output_pdf_path)
```

The following code snippet demonstrates how to add an annotation text stamp to an annotation PDF file and automatically adjust the font size to fit the page size:

```python

    import aspose.pdf as ap

    def auto_set_the_font_size_of_text_stamp_to_fit_page(input_pdf_path: str, output_pdf_path: str):
        document = ap.Document(input_pdf_path)
        text = "Stamp example"
        stamp = ap.TextStamp(text)
        stamp.auto_adjust_font_size_to_fit_stamp_rectangle = True
        stamp.auto_adjust_font_size_precision = 0.01
        stamp.word_wrap_mode = ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
        stamp.scale = False
        document.pages[1].add_stamp(stamp)
        document.save(output_pdf_path)
```

## What's new in Aspose.PDF 24.11

The following code snippet demonstrates the setting of the hashing algorithm for Pkcs7Detached:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    def sign_with_manual_digest_hash_algorithm(cert: str, password: str, input_pdf_path: str, out_pdf_signed_path: str):
        document = ap.Document(input_pdf_path)
        signature = ap.facades.PdfFileSignature(document)
        pkcs = ap.forms.PKCS7Detached(cert, password,  ap.DigestHashAlgorithm.SHA512)
        signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
        signature.save(out_pdf_signed_path)
        document.save(out_pdf_signed_path)
```

FontEncodingStrategy property. The following sample demonstrates the new option using:

```python

    import aspose.pdf as ap

    def convert_pdf_to_html_using_cmap(input_pdf_path: str, output_html_path: str):
        document = ap.Document(input_pdf_path)
        options = ap.HtmlSaveOptions()
        options.font_encoding_strategy = ap.HtmlSaveOptions.FontEncodingRules.DECREASE_TO_UNICODE_PRIORITY_LEVEL
        document.save(output_html_path, options)
```

## What's new in Aspose.PDF 24.10

You can use your usual code to sign documents with ECDSA and to verify signatures:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing


    def sign(cert: str, input_pdf_path: str, signed_pdf_path: str):
        document = ap.Document(input_pdf_path)
        signature = ap.facades.PdfFileSignature(document)
        pkcs = ap.forms.PKCS7Detached(cert, "12345")
        signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
        signature.save(signed_pdf_path)
        
    def verify(signed_pdf_path: str):
        document = ap.Document(signed_pdf_path)
        signature = ap.facades.PdfFileSignature(document)
        sig_names = signature.get_sign_names(True)
        for sig_name in sig_names:
            is_valid = signature.verify_signature(sig_name)
```

Sometimes, it is necessary to crop an image before inserting it into a PDF. We have added an overloaded version of the AddImage() method to support adding cropped images:

```python

    import aspose.pdf as ap
    import io

    def add_cropped_image_to_pdf(image_file_path: str, result_pdf_path: str):
        document = ap.Document()
        img_stream = io.FileIO(image_file_path, "r")
        image_rect = ap.Rectangle(17.62, 65.25, 602.62, 767.25, True)
        w = image_rect.width / 2
        h = image_rect.height / 2
        bbox = ap.Rectangle(image_rect.llx, image_rect.lly, image_rect.llx + w, image_rect.lly + h, True)
        page = document.pages.add()
        page.add_image(img_stream, image_rect, bbox, True)
        document.save(result_pdf_path)
```

## What's new in Aspose.PDF 24.9

Now, it is possible to extract PDF document layer elements and save them into new PDF streams. Layers (also known as Optional Content Groups or OCGs) are used in PDF documents for various purposes, primarily to manage and control the visibility of content within the document. This functionality is particularly useful in design, engineering, and publishing. Examples include blueprint aspects, complex diagram components, and language versions of the same content.

```python

    import aspose.pdf as ap

    def extract_pdf_layer(input_pdf_path: str, output_pdf_path: str):
        input_document = ap.Document(input_pdf_path)
        input_page = input_document.pages[1]
        layers = input_page.layers
        for layer in layers:
            extracted_layer_pdf_name = output_pdf_path + layer.id + ".pdf"
            with open(extracted_layer_pdf_name, "wb") as stream:
                layer.save(stream)
```            

The following code snippet demonstrates the graphic comparison of two PDF documents and saves an image with the differences into the resultant PDF document:

```python

    import aspose.pdf as ap

    def compare_pdf_with_compare_documents_to_pdf_method(first_document_path: str, second_document_path: str, comparison_result_pdf_path: str):
        first_document = ap.Document(first_document_path)
        second_document = ap.Document(second_document_path)
        comparer = ap.comparison.graphicalcomparison.GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.red
        comparer.resolution = ap.devices.Resolution(300)
        comparer.compare_documents_to_pdf(first_document, second_document, comparison_result_pdf_path)
```

To convert HEIC images to PDF user should add the reference to the FileFormat.HEIC NuGet package and use the following code snippet:

```python

    import aspose.pdf as ap
    import io

    dev convert_heic_to_pdf(input_pdf_path: str, result_pdf_path: str, width: int, height: int, pixel_format: ap.BitmapInfo.PixelFormat):
        document = ap.Document()
        page = document.pages.add()
        aspose_image = ap.Image()

        pixels = io.FileIO(input_pdf_path).read()
        aspose_image.bitmap_info = ap.BitmapInfo(pixels, width, height, pixel_format)
        page.page_info.width = width
        page.page_info.height = height
        page.page_info.margin.bottom = 0
        page.page_info.margin.top = 0
        page.page_info.margin.right = 0
        page.page_info.margin.left = 0
        page.paragraphs.add(aspose_image)
        document.save(result_pdf_path)
```

## What's new in Aspose.PDF 24.8

The following code snippet demonstrates how to convert a document into PDF/A-4 format when the input document is an earlier PDF version than 2.0.

```python

    import aspose.pdf as ap

    def convert_pdf_to_pdf_a4(input_pdf_path: str, conversion_log_path: str, result_pdf_path: str):
        document = ap.Document(input_pdf_path) 
        document.convert(io.BytesIO(), ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
        document.convert(conversion_log_path , ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
        document.save(result_pdf_path) 
```

Since 24.8 we introduced a method for flattening transparent content in PDF documents:

```python

    import aspose.pdf as ap

    def flatten_transparency(input_pdf_path: str, result_pdf_path: str):
        document = ap.Document(input_pdf_path) 
        document.flatten_transparency()
        document.save(result_pdf_path) 
```

## What's new in Aspose.PDF 24.7

The first code snippet demonstrates how to compare the first pages of two PDF documents.

```python

    import aspose.pdf as ap

    def comparing_specific_pages_side_by_side(input_pdf_path1: str, input_pdf_path2: str, result_pdf_path: str)
        document1 = ap.Document(input_pdf_path1)
        document2 = ap.Document(input_pdf_path2)
        options = ap.comparison.SideBySideComparisonOptions()
        options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES
        options.additional_change_marks = True
        ap.comparison.SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], result_pdf_path, options)
```

The second code snippet expands the scope to compare the entire content of two PDF documents.

```python

    import aspose.pdf as ap

    def comparing_entire_documents_side_by_side(input_pdf_path1: str, input_pdf_path2: str, result_pdf_path: str):
        document1 = ap.Document(input_pdf_path1)
        document2 = ap.Document(input_pdf_path2)
        options = ap.comparison.SideBySideComparisonOptions()
        options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES
        options.additional_change_marks = True
        ap.comparison.SideBySidePdfComparer.compare(document1, document2, result_pdf_path, options)
```

## What's new in Aspose.PDF 24.6

The next code snippet works with a PDF document and its tagged content, utilizing an Aspose.PDF library to process it:

```python

    import aspose.pdf as ap

    def create_an_accessible_document(input_pdf_path: str, result_pdf_path: str):
        document = ap.Document(input_pdf_path)
        content = document.tagged_content
        span = content.create_span_element()
        content.root_element.append_child(span, True)
        for op in document.pages[1].contents:
                if is_assignable(op, ap.operators.BDC):
                    bdc = cast(ap.operators.BDC, op)
                    if bdc is not None:
                        span.tag(bdc)
        document.save(result_pdf_path)
```

## What's new in Aspose.PDF 24.5

Lock a PDF layer:

```python

    import aspose.pdf as ap

    def lock_layer_in_pdf(input_pdf_path: str, result_pdf_path: str):
        document = ap.Document(input_pdf_path)
        page = document.pages[1]
        layer = page.layers[0]
        layer.lock()
        document.save(result_pdf_path)
```

Extract PDF layer elements:

```python

    import aspose.pdf as ap

    def extract_pdf_layer(input_pdf_path: str, result_pdf_path: str):
        document = ap.Document(input_pdf_path)
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(result_pdf_path)
```

Flatten a layered PDF:

```python

    import aspose.pdf as ap

    def flatten_pdf_layers(input_pdf_path: str, result_pdf_path: str):
        document = ap.Document(input_pdf_path)
        page = document.pages[1]
        for layer in page.layers:
            layer.flatten(True)
        document.save(result_pdf_path)
```

Merge All Layers inside the PDF into one:

```python

    import aspose.pdf as ap

    def merge_pdf_layers(input_pdf_path: str, result_pdf_path: str):
        document = ap.Document(input_pdf_path)
        page = document.pages[1]
        page.merge_layers("NewLayerName")
        # Or page.merge_layers("NewLayerName", "OC1")
        document.save(result_pdf_path)
```

## What's new in Aspose.PDF 24.4

This release supports applying a clipping mask to images:

```python

    import aspose.pdf as ap
    import io

    def add_stencil_masks_to_images(input_pdf_path: str, input_mask1_path: str, input_mask2_path: str, result_pdf_path: str):
        document = ap.Document(input_pdf_path)
        fs1 = io.FileIO(input_mask1_path, "r")
        fs2 = io.FileIO(input_mask2_path, "r")
        document.pages[1].resources.images[1].add_stencil_mask(fs1)
        document.pages[1].resources.images[2].add_stencil_mask(fs2)
        document.save(result_pdf_path)
``` 

Beginning with Aspose.PDF 24.4 this preference can be switched on and off using the Document.PickTrayByPdfSize property or the PdfContentEditor facade:

```python

    import aspose.pdf as ap

    def pick_tray_by_pdf_size(result_pdf_path: str):
        document = ap.Document()
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello world!"))
        document.pick_tray_by_pdf_size = True
        document.save(result_pdf_path)
```

```python

    import aspose.pdf as ap

    def pick_tray_by_pdf_size_facade(input_pdf_path: str, result_pdf_path: str):
        content_editor = ap.facades.PdfContentEditor()
        content_editor.bind_pdf(input_pdf_path)
        # Set the flag to choose a paper tray using the PDF page size
        content_editor.change_viewer_preference(ap.facades.ViewerPreference.PICK_TRAY_BY_PDF_SIZE)
        content_editor.save(result_pdf_path)
```

## What's new in Aspose.PDF 24.1

Since 24.1 release possible to import FDF format annotations to PDF:

```python

    import aspose.pdf as ap

    def import_fdf_by_form(input_pdf_path: str, template_path: str, result_pdf_path: str):
        form = ap.facades.Form(template_path)
        fdf_input_stream = io.FileIO(input_pdf_path, 'r')
        form.import_fdf(fdf_input_stream)
        form.save(result_pdf_path)    
```

## What's new in Aspose.PDF 23.12

From Aspose.PDF 23.12, support was added to the new conversion features:

- Implement PDF to Markdown conversion

```python

    import aspose.pdf as ap

    input_pdf_path = DIR_INPUT + "input.pdf"
    markdown_output_file_path = DIR_OUTPUT + "output_md_file.md"

    doc = ap.Document(input_pdf_path)
    save_options = ap.pdftomarkdown.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    doc.save(markdown_output_file_path, save_options)
```

- Implement OFD to PDF conversion

```python

    import aspose.pdf as ap

    input_path = DIR_INPUT + "input.ofd"
    output_path = DIR_OUTPUT + "output.pdf"
    document = ap.Document(input_path, ap.OfdLoadOptions())
    document.save(output_path)
```

Support for Python 3.6 has been discontinued.

## What's new in Aspose.PDF 23.11

Since 23.11 possible to remove the hidden text. The following code snippet can be used:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    text_absorber = ap.text.TextFragmentAbsorber()
    # This option can be used to prevent other text fragments from moving after hidden text replacement.
    text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
    document.pages.accept(text_absorber)

    for fragment in text_absorber.text_fragments:
        if fragment.text_state.invisible:
            fragment.text = ''

    document.save(output_file)
```    

## What's new in Aspose.PDF 23.8

Since the 23.8 version supports to add Incremental Updates detection.

The function for detecting Incremental Updates in a PDF document has been added. This function returns 'true' if a document was saved with incremental updates; otherwise, it returns 'false'.

```python

    import aspose.pdf as ap

    doc = ap.Document(file_path)
    updated = doc.has_incremental_update()
    print(updated)
```

Also, 23.8 supports the ways to work with nested checkbox fields. Many fillable PDF forms have checkbox fields that act as radio groups:

- Create multi-value checkbox field:

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    checkbox = ap.forms.CheckboxField(page, ap.Rectangle(50, 50, 70, 70, True))
    # Set the first checkbox group option value
    checkbox.export_value = "option 1"
    # Add new option right under existing ones
    checkbox.add_option("option 2")
    # Add new option at the given rectangle
    checkbox.add_option("option 3", ap.Rectangle(100, 100, 120, 120, True))
    document.form.add(checkbox)
    # Select the added checkbox
    checkbox.value = "option 2"
    document.save(DIR_OUTPUT + "checkbox_group.pdf")
```

- Get and set value of a multi-value checkbox:

```python

    import aspose.pdf as ap

    doc = ap.Document("example.pdf")
    form = doc.form
    checkbox = cast(ap.forms.CheckboxField, form.fields[0])

    # Allowed values may be retrieved from the AllowedStates collection
    # Set the checkbox value using Value property
    checkbox.value = checkbox.allowed_states[0]
    checkbox_value = checkbox.value  # the previously set value, e.g. "option 1"
    # The value should be any element of AllowedStates
    checkbox.value = "option 2"
    checkbox_value = checkbox.value  # option 2
    # Uncheck boxes by either setting Value to "Off" or setting Checked to false
    checkbox.value = "Off"
    # or, alternately:
    # checkbox.checked = False
    checkbox_value = checkbox.value  # Off
```

- Update checkbox state on user click:

```python

    import aspose.pdf as ap
    from aspose.pycore import cast

    input_file = DIR_INPUT + "input.pdf"
    document = ap.Document(input_file)
    point = ap.Point(62,462)  # for example, the coordinates of a mouse click
    # Option 1: look through the annotations on the page
    page = document.pages[5]
    for annotation in page.annotations:
        if(annotation.rect.contains(point)):
            widget = cast(ap.annotations.WidgetAnnotation, annotation)
            checkbox = cast(ap.forms.CheckboxField, widget.parent)
            if(annotation.active_state == "Off"):
                checkbox.value = widget.get_checked_state_name()
            else:
                checkbox.value = "Off"
        break
    # Option 2: look through the fields in the AcroForm
    for widget in document.form:
        field = cast(ap.forms.Field, widget)
        if(field == None):
            continue
        checkBoxFound = False
        for annotation in field:
            if(annotation.rect.contains(point)):
                checkBoxFound = True
                if(annotation.active_state=="Off"):
                    annotation.parent.value = annotation.get_checked_state_name()
                else:
                    annotation.parent.value = "Off"
            if(checkBoxFound):
                break
```

## What's new in Aspose.PDF 23.7

Since the 23.7 version supports to add the shape extraction:

```python

    import aspose.pdf as ap

    input1_file = DIR_INPUT + "input_1.pdf"
    input2_file = DIR_INPUT + "input_2.pdf"

    source = ap.Document(input1_file)
    dest = ap.Document(input2_file)

    graphic_absorber = ap.vector.GraphicsAbsorber()
    graphic_absorber.visit(source.pages[1])
    area = ap.Rectangle(90, 250, 300, 400, True)
    dest.pages[1].add_graphics(graphic_absorber.elements, area)
```

Also supports the ability to detect Overflow when adding text:

```python

    import aspose.pdf as ap

    output_file = DIR_OUTPUT + "output.pdf"
    doc = ap.Document()
    paragraph_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan."
    fragment = ap.text.TextFragment(paragraph_content)
    rectangle = ap.Rectangle(100, 600, 500, 700, False)
    paragraph = ap.text.TextParagraph()
    paragraph.vertical_alignment = ap.VerticalAlignment.TOP
    paragraph.formatting_options.wrap_mode = ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.rectangle = rectangle
    is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    while is_fit_rectangle == False:
        fragment.text_state.font_size -= 0.5
        is_fit_rectangle = fragment.text_state.is_fit_rectangle(paragraph_content, rectangle)

    paragraph.append_line(fragment)
    builder = ap.text.TextBuilder(doc.pages.add())
    builder.append_paragraph(paragraph)
    doc.save(output_file)
```

## What's new in Aspose.PDF 23.6

Support the ability to set the title of the HTML, Epub page:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_html = DIR_OUTPUT + "output_title.html"
    options = ap.HtmlSaveOptions()
    options.fixed_layout = True
    options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    options.parts_embedding_mode = ap.HtmlSaveOptions.PartsEmbeddingModes.EMBED_ALL_INTO_HTML
    options.title = "NEW PAGE & TITILE"  # <-- this added

    document = ap.Document(input_pdf)
    document.save(output_html, options)
```

## What's new in Aspose.PDF 23.5

Since the 23.5 version supports to add RedactionAnnotation FontSize option. Use the next code snippet to solve this task:

```python

    import aspose.pdf as ap

    doc = ap.Document(DIR_INPUT + "input.pdf")
    # Create RedactionAnnotation instance for specific page region
    annot = ap.annotations.RedactionAnnotation(doc.pages[1], ap.Rectangle(367, 756.919982910156, 420, 823.919982910156, True))
    annot.fill_color = ap.Color.black
    annot.border_color = ap.Color.yellow
    annot.color = ap.Color.blue
    # Text to be printed on redact annotation
    annot.overlay_text = "(Unknown)"
    annot.text_alignment = ap.HorizontalAlignment.CENTER
    # Repat Overlay text over redact Annotation
    annot.repeat = False
    # New property there !
    annot.font_size = 20
    # Add annotation to annotations collection of first page
    doc.pages[1].annotations.add(annot, False)
    # Flattens annotation and redacts page contents (i.e. removes text and image
    # Under redacted annotation)
    annot.redact()
    out_file = DIR_OUTPUT + "RedactPage_out.pdf"
    doc.save(out_file)
```

Support for Python 3.5 has been discontinued. Support for Python 3.11 has been added.

## What's new in Aspose.PDF 23.3

Version 23.3 introduced support for adding a resolution to an image. Two methods can be used to solve this problem:

```python

    import aspose.pdf as ap

    input_file = DIR_INPUT + "input.jpg"
    table = ap.Table()
    table.column_widths = "600"
    image = ap.Image()
    image.is_apply_resolution = True
    image.file = input_file
    for i in range(0, 2):
        row = table.rows.add()
        cell = row.cells.add()
        cell.paragraphs.add(image)

    page.paragraphs.add(table)
```

The image will be placed with scaled resolution or u can set FixedWidth or FixedHeight properties in combination with IsApplyResolution

## What's new in Aspose.PDF 23.1

Since the 23.1 version supports to creation of PrinterMark annotation.

Printer's marks are graphic symbols or text added to a page to assist production personnel in identifying components of a multiple-plate job and maintaining consistent output during production. Examples commonly used in the printing industry include:

- Registration targets for aligning plates
- Gray ramps and colour bars for measuring colours and ink densities
- Cut marks showing where the output medium is to be trimmed

We will show the example of the option with color bars for measuring colors and ink densities. There is a basic abstract class PrinterMarkAnnotation and from it child ColorBarAnnotation - which already implements these stripes. Let's check the example:

```python

    import aspose.pdf as ap

    out_file = DIR_OUTPUT  + "ColorBarTest.pdf"
    doc = ap.Document()
    page = doc.pages.add()
    page.trim_box = ap.Rectangle(20, 20, 580, 820, True)
    add_annotations(page)
    doc.save(out_file)


def add_annotations(page: ap.Page):
    rect_black = ap.Rectangle(100, 300, 300, 320, True)
    rect_cyan = ap.Rectangle(200, 600, 260, 690, True)
    rect_magenta = ap.Rectangle(10, 650, 140, 670, True)
    color_bar_black = ap.annotations.ColorBarAnnotation(page, rect_black, ap.annotations.ColorsOfCMYK.BLACK)
    color_bar_cyan = ap.annotations.ColorBarAnnotation(page, rect_cyan, ap.annotations.ColorsOfCMYK.CYAN)
    color_ba_magenta = ap.annotations.ColorBarAnnotation(page, rect_magenta, ap.annotations.ColorsOfCMYK.BLACK)
    color_ba_magenta.color_of_cmyk = ap.annotations.ColorsOfCMYK.MAGENTA
    color_bar_yellow = ap.annotations.ColorBarAnnotation(page, ap.Rectangle(400, 250, 450, 700, True), ap.annotations.ColorsOfCMYK.YELLOW)
    page.annotations.add(color_bar_black, False)
    page.annotations.add(color_bar_cyan, False)
    page.annotations.add(color_ba_magenta, False)
    page.annotations.add(color_bar_yellow, False)
```

Also support the vector images extraction. Try using the following code to detect and extract vector graphics:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "input.pdf"
    output_pdf = DIR_OUTPUT + "output.svg"
    doc = ap.Document(input_pdf)
    doc.pages[1].try_save_vector_graphics(output_pdf)
```