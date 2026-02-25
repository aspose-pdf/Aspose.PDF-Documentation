---
title: ما الجديد
linktitle: ما الجديد
type: docs
weight: 10
url: /ar/python-net/whatsnew/
description: في هذه الصفحة يتم تقديم أكثر الميزات الجديدة شيوعًا في Aspose.PDF للغة بايثون عبر .NET التي تم تقديمها في الإصدارات الأخيرة.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
lastmod: "2025-02-24"
TechArticle: false
---

## ما الجديد في Aspose.PDF 25.9

يقدم إصدار 25.9 تحسينًا في إمكانية الوصول، ودعمًا معززًا للامتثال، وقدرات API جديدة للعمل مع الصور المعلمة ومعايير المستندات.

1. تحويل ملفات PDF إلى تنسيق PDF/E-1.
1. إضافة صور معلمة من تدفقات الذاكرة.

### تحويل PDF إلى تنسيق PDF/E-1

في نسخة 25.9 من مكتبة Aspose.PDF للبايثون، يتوفر تحويل إلى تنسيق PDF/E-1. يمكنك العثور على مزيد من المعلومات حول هذا التنسيق في [(مستندات تنسيقات الملفات)[https://docs.fileformat.com/pdf/e/].

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

### إضافة صور معلمة من تدفق

إضافة صور معلمة من تدفق في PDF. تدعم نسخة 25.9 إمكانية وصول محسّنة في مستندات PDF عن طريق إضافة صورة من تدفق الذاكرة وتحديدها بنص بديل.

```python

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

## ما الجديد في Aspose.PDF 25.8

يضيف هذا التحديث مزيدًا من المرونة في التخطيط وإدارة أمان المستندات.

1. إنشاء فهارس محتوى معلمة (TOC).
1. تعديل حجم صفحات PDF مع تحجيم المحتوى.
1. تطبيق حدود متقطعة على الجداول.

### إنشاء فهرس محتوى معلم (TOC)

إنشاء تلقائي لجداول محتوى قابلة للوصول (TOC) في ملفات PDF المعلمة. يتيح إنشاء فهرس محتوى كامل القابلية للوصول في ملف PDF للقراء التنقل في المستند بفعالية ويضمن الامتثال لمعيار PDF/UA-1 لقابلية الوصول.

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

### تعديل حجم الصفحات مع تحجيم المحتوى

تعديل حجم صفحات PDF مع الحفاظ على التخطيط وتحجيم المحتوى بنسب متناسبة. عند العمل مع ملفات PDF، قد تحتاج إلى تعديل حجم الصفحات أو تحجيم المحتوى لتتناسب مع الأبعاد الجديدة.

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
    pdf_editor: Aspose.Pdf.Facades.PdfFileEditor
        The PdfFileEditor instance that exposes the ResizeContents API.
    page_numbers: int | Iterable[int] | slice, optional
        Page index (1-based) or collection of page indices to process. If omitted or None, all pages
        in the document are processed.
    scale: float, optional
        Uniform scale factor to apply to content (e.g., 0.5 reduces content to 50%). Mutually exclusive
        with target_width/target_height unless keep_aspect_ratio is explicitly handled.
    target_width: float, optional
        Desired content width in PDF points (1 point = 1/72 inch). When provided, content will be scaled
        to match this width (subject to keep_aspect_ratio and fit_mode).
    target_height: float, optional
        Desired content height in PDF points.
    keep_aspect_ratio: bool, default True
        If True, preserve the original aspect ratio when scaling to a target width or height.
    fit_mode: {'fit', 'fill', 'stretch'}, default 'fit'
        'fit'   — scale so content fits entirely inside the target box, preserving aspect ratio;
        'fill'  — scale so the target box is completely covered (may crop content);
        'stretch' — scale independently in X and Y (may distort).
    margins: tuple(float, float, float, float), optional
        (left, top, right, bottom) margins in points to preserve inside the target box.
    preserve_annotations: bool, default True
        When True, attempt to preserve annotations/forms/interactive elements; some annotations may
        require special handling after scaling.
    preserve_transparency: bool, default True
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

### تطبيق حدود متقطعة على الجداول

أضف جداول بأنماط حدود مخصصة باستخدام خطوط متقطعة. يوضح هذا المثال كيفية تطبيق أنماط حدود مخصصة—مثل الخطوط المتقطعة أو المنقطة—على الجداول في مستند PDF باستخدام Aspose.PDF للبايثون عبر .NET.

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

## ما الجديد في Aspose.PDF 25.7

يركز إصدار 25.7 على تحسين دعم التعليقات التوضيحية، وتناسب النص، وإدارة التوقيع الرقمي.

1. ضبط النص داخل الأشكال.
1. تشفير ملفات PDF باستخدام شهادة عامة.
1. إضافة تعليقات توضيحية سحابية ومتعددة الأضلاع.

### تشفير ملفات PDF باستخدام شهادة عامة

احمِ ملفات PDF الخاصة بك باستخدام تشفير يعتمد على الشهادات العامة. يتيح تشفير الشهادات العامة تشفير ملفات PDF لمستلمين معينين، مما يضمن أن يتمكن فقط حاملو المفاتيح الخاصة المقابلة من فتح وقراءة المستند.

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

### ضبط النص داخل مستطيل

تحجيم النص تلقائيًا ليتناسب داخل مستطيل محدد. عند تحديث أو توسيع النص في PDF، قد يتجاوز حدود الفقرة الأصلية.

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

### إضافة تعليقات توضيحية سحابية متعددة الأضلاع

عزز سير عمل مراجعة ملفات PDF باستخدام التعليقات التوضيحية السحابية أو على شكل مضلع. تسمح لك تعليقات المضلع بتسليط الضوء أو التأكيد على مناطق معينة في ملف PDF باستخدام الأشكال الهندسية.

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

## ما الجديد في Aspose.PDF 25.6

الميزات الرئيسية لهذا الإصدار:

1. دعم نص بديل للصور.
1. الوصول إلى معلومات الترخيص.
1. تعليقات نصية حرة منسقة.
1. مظهر التوقيع الرقمي القابل للتخصيص.

### دعم نص بديل للصور

قم بتعيين واسترجاع النص البديل للصور لتحسين إمكانية الوصول لقارئات الشاشة.

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

### الوصول إلى معلومات الترخيص

استرجع بيانات الترخيص التفصيلية (المستخدم المرخص، تاريخ الانتهاء) عبر LicenseInfo.

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

### تعليقات نصية حرة منسقة

استخدم SetTextStyle لتطبيق أنماط مثل الغامق، المائل، التسطير، أو لإزالة التنسيق الموجود من نص التعليق.

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

### مظهر التوقيع الرقمي القابل للتخصيص

أضف صورًا، غير الخطوط، وضع رسومات التوقيع فوق المحتوى الخلفي لتحسين العلامة التجارية أو اتساق التصميم.

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

## ما الجديد في Aspose.PDF 25.5

تقديم التحديث الأخير لـ Aspose.PDF عدة تحسينات قوية تُحسّن إمكانية الوصول للمستندات، التوافق، والأمان. يمكن للمطورين الآن استخراج الشهادات الرقمية مباشرةً من ملفات PDF الموقعة، مما يتيح تحققًا متقدمًا وفحوصات الامتثال.

1. استخراج الشهادات من توقيعات PDF.
1. إنشاء قوائم مرتّبة مُنظمة في ملفات PDF الموسومة.
1. التحقق من التوقيعات باستخدام شهادات المفتاح العام.
1. تحويل نماذج XFA الديناميكية إلى ملفات PDF بصيغة AcroForm.
1. استبدال الخطوط في PDF - تحويل XPS.

### استخراج الشهادات من توقيعات PDF

استرجع الشهادات المدمجة باستخدام 'extract_certificate()'.

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

### إنشاء قوائم مرتّبة مُنظمة في ملفات PDF الموسومة

إنشاء قوائم رقمية يمكن الوصول إليها (مع عناصر متداخلة) داخل المستندات الموسومة.

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

### التحقق من التوقيعات باستخدام شهادات المفتاح العام

تحقق من صحة التوقيعات الرقمية باستخدام شهادات المفتاح العام الخارجية.

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

### تحويل نماذج XFA الديناميكية إلى ملفات PDF بصيغة AcroForm

قُم بتوحيد نماذج XFA باستخدام 'ignore_needs_rendering'.

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

### استبدال الخطوط في PDF - تحويل XPS

استبدل الخطوط المفقودة بخط افتراضي احتياطي (مثال: “Courier New”).

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

## ما الجديد في Aspose.PDF 25.4

### وضع العلامات تلقائيًا أثناء تحويل PDF/A

حوّل ملفات PDF إلى PDF/A-1b مع إنشاء بنية منطقية تلقائية لتحسين إمكانية الوصول.

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


