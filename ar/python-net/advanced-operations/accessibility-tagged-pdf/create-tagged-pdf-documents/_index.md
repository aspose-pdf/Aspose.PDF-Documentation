---
title: إنشاء PDF معلم باستخدام بايثون
linktitle: إنشاء PDF معلم
type: docs
weight: 10
url: /ar/python-net/create-tagged-pdf/
description: تشرح هذه المقالة كيفية إنشاء عناصر الهيكل لمستند PDF معلم برمجياً باستخدام Aspose.PDF لبايثون عبر .NET.
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

إنشاء PDF معلم يعني إضافة (أو إنشاء) عناصر معينة إلى المستند ستمكّن المستند من التحقق وفقًا لمتطلبات PDF/UA. تُسمى هذه العناصر غالبًا عناصر الهيكل.

## إنشاء PDF معلم (سيناريو بسيط)

من أجل إنشاء عناصر الهيكل في مستند PDF معلم، توفر Aspose.PDF طرقًا لإنشاء عناصر الهيكل باستخدام واجهة [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) . يُنشئ هذا المثال مستند PDF معلم — PDF به بنية معنوية، مما يجعله أكثر قابلية للوصول ومتوافقًا مع معايير مثل PDF/UA.
يوضح مقتطف الشيفرة التالي كيفية إنشاء PDF معلم يحتوي على عنصرين: رأس وفقرة.

```python

    import aspose.pdf as ap

    # Create PDF Document
    document = ap.Document()

    # Get Content for working with TaggedPdf
    tagged_content = document.tagged_content
    root_element = tagged_content.root_element

    # Set Title and Language for Document
    tagged_content.set_title("Tagged Pdf Document")
    tagged_content.set_language("en-US")
    main_header = tagged_content.create_header_element()
    main_header.set_text("Main Header")
    paragraph_element = tagged_content.create_paragraph_element()
    paragraph_element.set_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
                                "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
                                "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
                                "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
                                "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
                                "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
                                "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
                                "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
                                "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.")
    root_element.append_child(main_header, True)
    root_element.append_child(paragraph_element, True)

    # Save Tagged PDF Document
    document.save(path_outfile)
```

```python

    import aspose.pdf as ap

    # Create PDF Document
    document = ap.Document()

    # Get Content for working with TaggedPdf
    tagged_content = document.tagged_content
    root_element = tagged_content.root_element

    # Set Title and Language for Document
    tagged_content.set_title("Tagged Pdf Document")
    tagged_content.set_language("en-US")

    # Create Header Level 1
    header1 = tagged_content.create_header_element(1)
    header1.set_text("Header Level 1")

    # Create Paragraph with Quotes
    paragraph_with_quotes = tagged_content.create_paragraph_element()
    paragraph_with_quotes.structure_text_state.font = ap.text.FontRepository.find_font("Calibri")
    position_settings = ap.tagged.PositionSettings()
    position_settings.margin = ap.MarginInfo(10, 5, 10, 5)
    paragraph_with_quotes.adjust_position(position_settings)

    # Create Span Element
    span_element1 = tagged_content.create_span_element()
    span_element1.set_text(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. "
        "Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, "
        "luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada "
        "fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus "
        "condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae "
        "lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non "
        "lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit.")

    # Create Quote Element
    quote_element = tagged_content.create_quote_element()
    quote_element.set_text(
        "Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.")
    quote_element.structure_text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC

    # Create Another Span Element
    span_element2 = tagged_content.create_span_element()
    span_element2.set_text(" Sed non consectetur elit.")

    # Append Children to Paragraph
    paragraph_with_quotes.append_child(span_element1, True)
    paragraph_with_quotes.append_child(quote_element, True)
    paragraph_with_quotes.append_child(span_element2, True)

    # Append Header and Paragraph to Root Element
    root_element.append_child(header1, True)
    root_element.append_child(paragraph_with_quotes, True)

    # Save Tagged PDF Document
    document.save(path_outfile)
```

سوف نحصل على المستند التالي بعد الإنشاء:

![مستند PDF معلم مع عنصرين - رأس وفقرة](taggedpdf-01.png)

## تنسيق بنية النص

PDFs المعلمة هي مستندات مُنظمة توفر ميزات الوصول والمعنى الدلالي للمحتوى.

ينشئ المثال مستند PDF بميزات الوصول باستخدام بنية محتوى معلمة. يوضح كيفية إنشاء عنصر فقرة مع تنسيق مخصص وبيانات تعريفية صحيحة للمستند.

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        paragraph_element = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph_element, True)

        paragraph_element.structure_text_state.font_size = 18.0
        paragraph_element.structure_text_state.foreground_color = ap.Color.red
        paragraph_element.structure_text_state.font_style = ap.text.FontStyles.ITALIC

        paragraph_element.set_text("Red italic text.")

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## توضيح عناصر الهيكل

PDFs المعلمة ضرورية للامتثال لمتطلبات الوصول وتوفر محتوى مُنظم يمكن قراءته بشكل صحيح بواسطة القارئات الشاشة وغيرها من التقنيات المساعدة. يُظهر مقتطف الشيفرة التالي كيفية إنشاء مستند PDF معلم مع صورة مدمجة:

1. إنشاء PDF معلم مع صورة.
1. تكوين المستند.
1. إنشاء وتكوين الشكل.
1. ضبط التوضع.
1. حفظ المستند.

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")
        figure1 = tagged_content.create_figure_element()
        tagged_content.root_element.append_child(figure1, True)
        figure1.alternative_text = "Figure One"
        figure1.title = "Image 1"
        figure1.set_tag("Fig1")
        figure1.set_image(path_imagefile, 300)
        # Adjust position
        position_settings = ap.tagged.PositionSettings()
        margin_info = ap.MarginInfo()
        margin_info.left = 50
        margin_info.top = 20
        position_settings.margin = margin_info
        figure1.adjust_position(position_settings)

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## التحقق من صحة PDF المعلم

توفر Aspose.PDF لبايثون عبر .NET القدرة على التحقق من صحة مستند PDF/UA معلم. تُحقق طريقة 'validate_tagged_pdf' من صحة مستندات PDF وفقًا لمعيار PDF/UA-1، وهو جزء من مواصفة ISO 14289 للمستندات PDF القابلة للوصول. يضمن ذلك أن تكون ملفات PDF قابلة للوصول للمستخدمين ذوي الإعاقة والتقنيات المساعدة.

- بنية المستند. وضع علامات دلالية صحيحة وبنية منطقية.
- النص البديل. نص بديل للصور والعناصر غير النصية.
- ترتيب القراءة. تسلسل منطقي للقارئات الشاشة.
- اللون والتباين. نسب تباين كافية.
- النماذج. حقول ونصوص نماذج قابلة للوصول.
- التنقل. إشارات مرجعية وبنية تنقل صحيحة.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        is_valid = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
```

## تعديل موقع بنية النص

يوضح مقتطف الشيفرة التالي كيفية تعديل موضع بنية النص في مستند PDF المعلم:

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create paragraph
        paragraph = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph, True)
        paragraph.set_text("Text.")

        # Adjust position
        position_settings = ap.tagged.PositionSettings()
        margin_info = ap.MarginInfo()
        margin_info.left = 300
        margin_info.top = 20
        margin_info.right = 0
        margin_info.bottom = 0
        position_settings.margin = margin_info
        position_settings.horizontal_alignment = ap.HorizontalAlignment.NONE
        position_settings.vertical_alignment = ap.VerticalAlignment.NONE
        position_settings.is_first_paragraph_in_column = False
        position_settings.is_kept_with_next = False
        position_settings.is_in_new_page = False
        position_settings.is_in_line_paragraph = False
        paragraph.adjust_position(position_settings)

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## إنشاء PDF معلم تلقائيًا مع تحويل PDF/UA-1

تمكن Aspose.PDF من إنشاء وسوم بنية منطقية أساسية تلقائيًا عند تحويل مستند إلى PDF/UA-1. يمكن للمستخدمين بعد ذلك تحسين هذه البنية المنطقية الأساسية يدويًا، مما يوفر رؤى إضافية حول محتوى المستند.

يحول مقتطف الشيفرة مستند PDF موجود إلى صيغة PDF/UA-1، وهو معيار ISO (ISO 14289-1) يضمن أن تكون مستندات PDF قابلة للوصول للمستخدمين ذوي الإعاقة. تشمل عملية التحويل وضع علامات تلقائيًا على عناصر المستند لإنشاء بنية منطقية.

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document(path_infile) as document:
        # Create conversion options
        options = ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_UA_1, ap.ConvertErrorAction.DELETE)
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
