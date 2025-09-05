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

## What's new in Aspose.PDF 25.5

The 'extract_certificate' method extracts digital certificates from signatures embedded in a PDF document.

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

The 'create_ordered_list' method generates a tagged PDF document with a structured numbered list, including nested sublists.

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

This example verifies a digital signature in a PDF document using a public key certificate.

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

Next feature converts a dynamic XFA (XML Forms Architecture) PDF form into a standard AcroForm PDF.

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

This code snippet converts a PDF document to XPS format while replacing missing or unavailable fonts with a specified default font.

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

This version converts an existing PDF document into PDF/A-1b format.

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

## What's new in Aspose.PDF 25.3

From 25.3 Aspose.PDF for Python via .NET library supports verifying whether the digital signatures in a PDF document have been compromised.

```python

    import aspose.pdf as ap

    def check(self, infile):

        path_infile = self.data_dir + infile

        # Open PDF document
        with ap.Document(path_infile) as document:
            # Create the compromise detector instance
            detector = ap.SignaturesCompromiseDetector(document)
            results = []
            #  Check for compromise
            if detector.check(results):
                print("No signature compromise detected")
                return
            # Get information about compromised signatures
            result = results[0]
            if result.has_compromised_signatures:
                print(f"Count of compromised signatures: {result.COMPROMISED_SIGNATURES.length}")
                for signature_name in result.COMPROMISED_SIGNATURES:
                    print(f"Signature name: {signature_name.FULL_NAME}")
            # Get info about signatures coverage
            print(result.signatures_coverage)

```

Also supports adjusting the Table position in PDF.

```python

    import aspose.pdf as ap

    def adjust_table_position(self, outfile, outlogfile):

    path_outfile = self.data_dir + outfile
    path_outlogfile = self.data_dir + outlogfile

    # Create PDF document
    with ap.Document() as document:
        # Create tagged content
        tagged_content = document.tagged_content
        tagged_content.set_title("Example table cell style")
        tagged_content.set_language("en-US")
        # Get root structure element
        root_element = tagged_content.root_element
        # Create table structure element
        table_element = tagged_content.create_table_element()
        root_element.append_child(table_element, True)
        # Create position settings
        position_settings = ap.tagged.PositionSettings()
        position_settings.horizontal_alignment = ap.HorizontalAlignment.NONE
        margin_info = ap.MarginInfo()
        margin_info.left = 20
        margin_info.right = 0
        margin_info.top = 0
        margin_info.bottom = 0
        position_settings.margin = margin_info
        position_settings.vertical_alignment = ap.VerticalAlignment.NONE
        position_settings.is_first_paragraph_in_column = False
        position_settings.is_kept_with_next = False
        position_settings.is_in_new_page = False
        position_settings.is_in_line_paragraph = False
        # Adjust table position
        table_element.adjust_position(position_settings)
        table_t_head_element = table_element.create_t_head()
        table_t_body_element = table_element.create_t_body()
        table_t_foot_element = table_element.create_t_foot()
        row_count = 4
        col_count = 4
        head_tr_element = table_t_head_element.create_tr()
        head_tr_element.alternative_text = "Head Row"
        for col_index in range(col_count):
            th_element = head_tr_element.create_th()
            th_element.set_text(f"Head {col_index}")
            th_element.background_color = ap.Color.green_yellow
            th_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)
            th_element.is_no_border = True
            th_element.margin = ap.MarginInfo(16.0, 2.0, 8.0, 2.0)
            th_element.alignment = ap.HorizontalAlignment.RIGHT
        for row_index in range(row_count):
            tr_element = table_t_body_element.create_tr()
            tr_element.alternative_text = f"Row {row_index}"
            for col_index in range(col_count):
                col_span = 1
                row_span = 1
                if col_index == 1 and row_index == 1:
                    col_span = 2
                    row_span = 2
                elif col_index == 2 and (row_index == 1 or row_index == 2):
                    continue
                elif row_index == 2 and (col_index == 1 or col_index == 2):
                    continue
                td_element = tr_element.create_td()
                td_element.set_text(f"Cell [{row_index}, {col_index}]")
                td_element.background_color = ap.Color.yellow
                td_element.border = ap.BorderInfo(ap.BorderSide.ALL, 4.0, ap.Color.gray)
                td_element.is_no_border = False
                td_element.margin = ap.MarginInfo(8.0, 2.0, 8.0, 2.0)
                td_element.alignment = ap.HorizontalAlignment.CENTER
                cell_text_state = ap.text.TextState()
                cell_text_state.foreground_color = ap.Color.dark_blue
                cell_text_state.font_size = 7.5
                cell_text_state.font_style = ap.text.FontStyles.BOLD
                cell_text_state.font = ap.text.FontRepository.find_font("Arial")
                td_element.default_cell_text_state = cell_text_state
                td_element.is_word_wrapped = True
                td_element.vertical_alignment = ap.VerticalAlignment.CENTER
                td_element.col_span = col_span
                td_element.row_span = row_span
        foot_tr_element = table_t_foot_element.create_tr()
        foot_tr_element.alternative_text = "Foot Row"

        for col_index in range(col_count):
            td_element = foot_tr_element.create_td()
            td_element.set_text(f"Foot {col_index}")
        # Save Tagged PDF Document
        document.save(path_outfile)
    # Check PDF/UA compliance
    with ap.Document(path_outfile) as document:
        # Create tagged content
        is_pdf_ua_compliance = document.validate(path_outlogfile, ap.PdfFormat.PDF_UA_1)
        print(f"PDF/UA compliance: {is_pdf_ua_compliance}")
```

## What's new in Aspose.PDF 25.2

From 25.2 Aspose.PDF for Python via .NET library supports PDF to PDF/X conversion.

```python

    import aspose.pdf as ap

    def convert_pdf_to_pdf_x(self, infile, infile_icc, outfile):

    path_infile = self.data_dir + infile
    path_infile_icc = self.data_dir + infile_icc
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        #  Set up the desired PDF/X format with PdfFormatConversionOptions
        options = ap.PdfFormatConversionOptions(ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE)
        # Provide the name of the external ICC profile file (optional)
        options.icc_profile_file_name = path_infile_icc
        # Provide an output condition identifier and other necessary OutputIntent properties (optional)
        options.output_intent = ap.OutputIntent("FOGRA39")
        # Convert to PDF/X compliant document
        document.convert(options)
        # Save PDF document
        document.save(path_outfile)
```

How to get information about Digital Signatures of PDF?

```python

    import aspose.pdf as ap

    def verify(self, infile):

    path_infile = self.data_dir + infile

    # Open the document
    with ap.Document(path_infile) as document:
        #  Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Get a list of signature names in the document
            signature_names = signature.get_signature_names(True)
            # Loop through all signature names to verify each one
            for signature_name in signature_names:
                # Verify that the signature with the given name is valid
                if signature.verify_signature(signature_name) is False:
                    raise Exception('Not verified')

```

With this version it is now possible to create a TextBoxField with multiple widget annotations.

```python

    import aspose.pdf as ap

    def add_text_box_field_to_pdf(self, outfile):

    path_outfile = self.data_dir + outfile

    # Create PDF document
    with ap.Document() as document:
        # Add a new page in the created document
        page = document.pages.add()
        # Defining an array with rectangle data for widget annotations.
        # The number of elements in the array determines the number of widget annotations to add.
        rects = [ap.Rectangle(10, 600, 110, 620, True), ap.Rectangle(10, 630, 110, 650, True),
                    ap.Rectangle(10, 660, 110, 680, True)]
        # Defining an array with DefaultAppearance used to specify how widget annotations are displayed in the added field.
        default_appearances = [ap.annotations.DefaultAppearance("Arial", 10, drawing.Color.dark_blue),
                                ap.annotations.DefaultAppearance("Helvetica", 12, drawing.Color.dark_green),
                                ap.annotations.DefaultAppearance(ap.text.FontRepository.find_font("TimesNewRoman"),
                                                                14, drawing.Color.dark_magenta)]
        # Create a field
        text_box_field = ap.forms.TextBoxField(page, rects)
        # Setting the appearances of widget annotations
        i = 0
        for wa in text_box_field:
            wa.default_appearance = default_appearances[i]
            i += 1
        text_box_field.value = "Text"
        # Add field to the document
        document.form.add(text_box_field)
        # Save PDF document
        document.save(path_outfile)
```

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