---
title: Python을 사용하여 태그가 달린 PDF 만들기
linktitle: 태그가 달린 PDF 만들기
type: docs
weight: 10
url: /ko/python-net/create-tagged-pdf/
description: 이 문서는 Aspose.PDF for Python via .NET을 사용하여 프로그래밍 방식으로 태그가 달린 PDF 문서의 구조 요소를 만드는 방법을 설명합니다.
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

태그가 달린 PDF를 생성한다는 것은 문서에 특정 요소들을 추가(또는 생성)하여 PDF/UA 요구 사항에 따라 문서를 검증할 수 있게 하는 것을 의미합니다. 이러한 요소들은 흔히 구조 요소(Structure Elements)라고 부릅니다.

## 태그가 달린 PDF 만들기 (간단한 시나리오)

태그가 달린 PDF 문서에 구조 요소를 만들기 위해 Aspose.PDF는 [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) 인터페이스를 사용하여 구조 요소를 생성하는 메서드를 제공합니다. 이 예제는 의미 구조를 가진 PDF, 즉 접근성이 향상되고 PDF/UA와 같은 표준을 준수하는 태그가 달린 PDF 문서를 생성합니다.
다음 코드 스니펫은 헤더와 단락이라는 두 요소를 포함하는 태그가 달린 PDF를 만드는 방법을 보여줍니다.

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

생성 후 다음 문서를 얻을 수 있습니다:

![태그가 달린 PDF 문서, 2 요소 - 헤더 및 단락](taggedpdf-01.png)

## 텍스트 구조 스타일링

태그가 달린 PDF는 접근성 기능과 콘텐츠에 의미적 의미를 제공하는 구조화된 문서입니다.

이 예제는 태그가 달린 콘텐츠 구조를 사용하여 접근성 기능이 포함된 PDF 문서를 생성합니다. 맞춤 스타일과 적절한 문서 메타데이터를 가진 단락 요소를 만드는 방법을 보여줍니다.

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

## 구조 요소 설명

태그가 달린 PDF는 접근성 준수를 위해 필수적이며, 화면 판독기 및 기타 보조 기술이 올바르게 해석할 수 있는 구조화된 콘텐츠를 제공합니다. 다음 코드 스니펫은 삽입된 이미지를 포함하는 태그가 달린 PDF 문서를 만드는 방법을 보여줍니다.

1. 이미지를 포함한 태그가 달린 PDF 만들기.
1. 문서 구성.
1. 그림을 만들고 구성하기.
1. 위치 지정하기.
1. 문서 저장하기.

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

## 태그가 달린 PDF 검증

Aspose.PDF for Python via .NET은 PDF/UA 태그가 달린 PDF 문서를 검증할 수 있는 기능을 제공합니다. 'validate_tagged_pdf' 메서드는 접근성 PDF 문서에 대한 ISO 14289 사양의 일부인 PDF/UA-1 표준에 따라 PDF 문서를 검증합니다. 이를 통해 PDF가 장애가 있는 사용자와 보조 기술에 접근 가능하도록 보장합니다.

- 문서 구조. 적절한 의미 태깅 및 논리적 구조.
- 대체 텍스트. 이미지 및 비텍스트 요소에 대한 Alt 텍스트.
- 읽기 순서. 화면 판독기를 위한 논리적 순서.
- 색상 및 대비. 충분한 대비 비율.
- 양식. 접근 가능한 양식 필드 및 레이블.
- 탐색. 적절한 북마크 및 탐색 구조.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        is_valid = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
```

## 텍스트 구조 위치 조정

다음 코드 스니펫은 태그가 달린 PDF 문서에서 텍스트 구조의 위치를 조정하는 방법을 보여줍니다.

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

## PDF/UA-1 변환으로 태그가 달린 PDF 자동 생성

Aspose.PDF는 문서를 PDF/UA-1로 변환할 때 기본 논리 구조 마크업을 자동으로 생성할 수 있게 합니다. 사용자는 이후 이 기본 논리 구조를 수동으로 개선하여 문서 내용에 대한 추가적인 통찰을 제공할 수 있습니다.

다음 코드 스니펫은 기존 PDF 문서를 PDF/UA-1 형식으로 변환합니다. 이는 장애가 있는 사용자가 접근할 수 있도록 보장하는 ISO 표준(ISO 14289-1)이며, 변환 과정에서 문서 요소를 자동으로 태깅하여 논리 구조를 생성합니다.

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
