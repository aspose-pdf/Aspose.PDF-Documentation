---
title: Python에서 Tagged PDF 구조 요소 속성 설정
linktitle: 구조 요소 속성 설정
type: docs
weight: 30
url: /ko/python-net/setting-structure-elements-properties/
description: Aspose.PDF for Python via .NET를 사용하여 Python에서 Tagged PDF 구조 요소 속성을 설정하는 방법을 배우십시오. 여기에는 제목, 언어, 실제 텍스트, 대체 텍스트 및 확장 텍스트가 포함됩니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

구조 요소는 섹션, 헤더, 문단 또는 표와 같이 PDF 문서의 의미 계층 구조를 정의합니다. title, language, alternative_text, actual_text, expansion_text와 같은 속성을 설정함으로써 화면 판독기와 같은 보조 기술을 위해 PDF의 접근성 및 의미를 개선합니다.

다음 코드 조각은 Tagged PDF 문서의 구조 요소 속성을 설정하는 방법을 보여줍니다:

1. 새 태그가 지정된 PDF 문서를 만듭니다.
1. 문서 메타데이터를 설정합니다.
1. 구조 요소를 생성합니다.
1. 접근성 속성을 설정합니다.
1. 태그가 지정된 PDF를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def set_properties(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create Structure Elements
        root_element = tagged_content.root_element

        section_element = tagged_content.create_sect_element()
        root_element.append_child(section_element, True)

        header_element = tagged_content.create_header_element(1)
        section_element.append_child(header_element, True)
        header_element.set_text("The Header")

        header_element.title = "Title"
        header_element.language = "en-US"
        header_element.alternative_text = "Alternative Text"
        header_element.expansion_text = "Expansion Text"
        header_element.actual_text = "Actual Text"

        # Save Tagged PDF Document
        document.save(outfile)
```

## 텍스트 구조 요소 설정

Tagged PDF 문서의 텍스트 구조 요소를 설정하려면, Aspose.PDF가 제공합니다 [단락 요소](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/paragraphelement/) 클래스. 다음 코드 스니펫은 Tagged PDF 문서의 텍스트 구조 요소를 설정하는 방법을 보여줍니다:

```python
import aspose.pdf as ap
import sys
from os import path

def set_text_elements(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Get Root Structure Elements
        root_element = tagged_content.root_element

        paragraph_element = tagged_content.create_paragraph_element()

        # Set Text to Text Structure Element
        paragraph_element.set_text("Paragraph.")
        root_element.append_child(paragraph_element, True)

        # Save Tagged PDF Document
        document.save(outfile)

```

## 텍스트 블록 구조 요소 설정

이 Python 예제는 Aspose.PDF를 사용하여 구조화된 헤더 계층과 단락을 포함하는 Tagged PDF를 생성하며, 문서의 의미론 및 접근성 기능을 향상시킵니다.

1. 새 태그가 지정된 PDF 문서를 만듭니다.
1. 문서 메타데이터를 설정합니다.
1. 루트 구조 요소에 접근합니다.
1. 다중 레벨 헤더 만들기.
1. 루트 구조에 헤더를 추가합니다.
1. 단락 요소를 생성하십시오.
1. 루트 구조에 단락을 추가합니다.
1. 태그가 지정된 PDF를 저장합니다.

다음 코드 스니펫은 Tagged PDF 문서의 텍스트 블록 구조 요소를 설정하는 방법을 보여줍니다:

```python
import aspose.pdf as ap
import sys
from os import path

def set_text_block_elements(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content
        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")
        # Get Root Structure Element
        root_element = tagged_content.root_element
        h1 = tagged_content.create_header_element(1)
        h2 = tagged_content.create_header_element(2)
        h3 = tagged_content.create_header_element(3)
        h4 = tagged_content.create_header_element(4)
        h5 = tagged_content.create_header_element(5)
        h6 = tagged_content.create_header_element(6)
        h1.set_text("H1. Header of Level 1")
        h2.set_text("H2. Header of Level 2")
        h3.set_text("H3. Header of Level 3")
        h4.set_text("H4. Header of Level 4")
        h5.set_text("H5. Header of Level 5")
        h6.set_text("H6. Header of Level 6")
        root_element.append_child(h1, True)
        root_element.append_child(h2, True)
        root_element.append_child(h3, True)
        root_element.append_child(h4, True)
        root_element.append_child(h5, True)
        root_element.append_child(h6, True)
        p = tagged_content.create_paragraph_element()
        p.set_text(
            "P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit."
            " Cras pellentesque libero semper, gravida magna sed, luctus leo. "
            "Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. "
            "Interdum et malesuada fames ac ante ipsum primis in faucibus. "
            "Aliquam lacinia sit amet elit ac consectetur. "
            "Donec cursus condimentum ligula, vitae volutpat sem tristique eget. "
            "Nulla in consectetur massa. Vestibulum vitae lobortis ante. "
            "Nulla ullamcorper pellentesque justo rhoncus accumsan. "
            "Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. "
            "Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, "
            "vitae posuere risus odio id massa. Cras sed venenatis lacus."
        )
        root_element.append_child(p, True)
        # Save Tagged PDF Document
        document.save(outfile)
```

## 인라인 구조 요소 설정

Aspose.PDF for Python via .NET를 사용하여 태그가 지정된 PDF의 헤더와 단락 내에서 인라인 텍스트 요소 (/Span)를 생성합니다.

다음 코드 스니펫은 Tagged PDF 문서의 인라인 구조 요소를 설정하는 방법을 보여줍니다:

```python
import aspose.pdf as ap
import sys
from os import path

def set_inline_elements(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Get Root Structure Element
        root_element = tagged_content.root_element

        header_element_h1 = tagged_content.create_header_element(1)
        header_element_h2 = tagged_content.create_header_element(2)
        header_element_h3 = tagged_content.create_header_element(3)
        header_element_h4 = tagged_content.create_header_element(4)
        header_element_h5 = tagged_content.create_header_element(5)
        header_element_h6 = tagged_content.create_header_element(6)
        root_element.append_child(header_element_h1, True)
        root_element.append_child(header_element_h2, True)
        root_element.append_child(header_element_h3, True)
        root_element.append_child(header_element_h4, True)
        root_element.append_child(header_element_h5, True)
        root_element.append_child(header_element_h6, True)

        span_element_h11 = tagged_content.create_span_element()
        span_element_h11.set_text("H1. ")
        header_element_h1.append_child(span_element_h11, True)
        span_element_h12 = tagged_content.create_span_element()
        span_element_h12.set_text("Level 1 Header")
        header_element_h1.append_child(span_element_h12, True)

        span_element_h21 = tagged_content.create_span_element()
        span_element_h21.set_text("H2. ")
        header_element_h2.append_child(span_element_h21, True)
        span_element_h22 = tagged_content.create_span_element()
        span_element_h22.set_text("Level 2 Header")
        header_element_h2.append_child(span_element_h22, True)

        span_element_h31 = tagged_content.create_span_element()
        span_element_h31.set_text("H3. ")
        header_element_h3.append_child(span_element_h31, True)
        span_element_h32 = tagged_content.create_span_element()
        span_element_h32.set_text("Level 3 Header")
        header_element_h3.append_child(span_element_h32, True)

        span_element_h41 = tagged_content.create_span_element()
        span_element_h41.set_text("H4. ")
        header_element_h4.append_child(span_element_h41, True)
        span_element_h42 = tagged_content.create_span_element()
        span_element_h42.set_text("Level 4 Header")
        header_element_h4.append_child(span_element_h42, True)

        span_element_h51 = tagged_content.create_span_element()
        span_element_h51.set_text("H5. ")
        header_element_h5.append_child(span_element_h51, True)
        span_element_h52 = tagged_content.create_span_element()
        span_element_h52.set_text("Level 5 Header")
        header_element_h5.append_child(span_element_h52, True)

        span_element_h61 = tagged_content.create_span_element()
        span_element_h61.set_text("H6. ")
        header_element_h6.append_child(span_element_h61, True)
        span_element_h62 = tagged_content.create_span_element()
        span_element_h62.set_text("Level 6 Header")
        header_element_h6.append_child(span_element_h62, True)

        paragraph_element = tagged_content.create_paragraph_element()
        paragraph_element.set_text("P. ")
        root_element.append_child(paragraph_element, True)
        span_element_1 = tagged_content.create_span_element()
        span_element_1.set_text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        )
        paragraph_element.append_child(span_element_1, True)
        span_element_2 = tagged_content.create_span_element()
        span_element_2.set_text("Aenean nec lectus ac sem faucibus imperdiet. ")
        paragraph_element.append_child(span_element_2, True)
        span_element_3 = tagged_content.create_span_element()
        span_element_3.set_text("Sed ut erat ac magna ullamcorper hendrerit. ")
        paragraph_element.append_child(span_element_3, True)
        span_element_4 = tagged_content.create_span_element()
        span_element_4.set_text(
            "Cras pellentesque libero semper, gravida magna sed, luctus leo. "
        )
        paragraph_element.append_child(span_element_4, True)
        span_element_5 = tagged_content.create_span_element()
        span_element_5.set_text(
            "Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. "
        )
        paragraph_element.append_child(span_element_5, True)
        span_element_6 = tagged_content.create_span_element()
        span_element_6.set_text(
            "Interdum et malesuada fames ac ante ipsum primis in faucibus. "
        )
        paragraph_element.append_child(span_element_6, True)
        span_element_7 = tagged_content.create_span_element()
        span_element_7.set_text(
            "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. "
        )
        paragraph_element.append_child(span_element_7, True)
        span_element_8 = tagged_content.create_span_element()
        span_element_8.set_text(
            "Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. "
        )
        paragraph_element.append_child(span_element_8, True)
        span_element_9 = tagged_content.create_span_element()
        span_element_9.set_text(
            "Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. "
        )
        paragraph_element.append_child(span_element_9, True)
        span_element_10 = tagged_content.create_span_element()
        span_element_10.set_text(
            "Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus."
        )
        paragraph_element.append_child(span_element_10, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

## 사용자 정의 태그 이름 설정

Aspose.PDF for Python을 사용하여 Tagged PDF의 구조 및 인라인 요소에 대한 사용자 정의 태그 이름을 설정합니다.

다음 코드 스니펫은 사용자 정의 태그 이름을 설정하는 방법을 보여줍니다:

1. 새 태그가 지정된 PDF 문서를 만듭니다.
1. 문서 메타데이터를 설정합니다.
1. 섹션 요소를 생성합니다.
1. 맞춤 태그를 사용하여 단락 요소를 생성합니다.
1. 사용자 지정 태그로 인라인 span 요소를 생성합니다.
1. 태그가 지정된 PDF를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def set_tag_name(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create Logical Structure Elements
        section_element = tagged_content.create_sect_element()
        tagged_content.root_element.append_child(section_element, True)

        paragraph_element1 = tagged_content.create_paragraph_element()
        paragraph_element2 = tagged_content.create_paragraph_element()
        paragraph_element3 = tagged_content.create_paragraph_element()
        paragraph_element4 = tagged_content.create_paragraph_element()

        paragraph_element1.set_text("P1. ")
        paragraph_element2.set_text("P2. ")
        paragraph_element3.set_text("P3. ")
        paragraph_element4.set_text("P4. ")

        paragraph_element1.set_tag("P1")
        paragraph_element2.set_tag("Para")
        paragraph_element3.set_tag("Para")
        paragraph_element4.set_tag("Paragraph")

        section_element.append_child(paragraph_element1, True)
        section_element.append_child(paragraph_element2, True)
        section_element.append_child(paragraph_element3, True)
        section_element.append_child(paragraph_element4, True)

        span_element1 = tagged_content.create_span_element()
        span_element2 = tagged_content.create_span_element()
        span_element3 = tagged_content.create_span_element()
        span_element4 = tagged_content.create_span_element()

        span_element1.set_text("Span 1.")
        span_element2.set_text("Span 2.")
        span_element3.set_text("Span 3.")
        span_element4.set_text("Span 4.")

        span_element1.set_tag("SPAN")
        span_element2.set_tag("Sp")
        span_element3.set_tag("Sp")
        span_element4.set_tag("TheSpan")

        paragraph_element1.append_child(span_element1, True)
        paragraph_element2.append_child(span_element2, True)
        paragraph_element3.append_child(span_element3, True)
        paragraph_element4.append_child(span_element4, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

## 요소에 구조 요소를 추가

**이 기능은 버전 19.4 이상에서 지원됩니다.**

Aspose.PDF for Python via .NET를 사용하여 태그가 지정된 PDF에서 링크 및 이미지 요소를 생성합니다.

다음 코드 스니펫은 Tagged PDF 문서의 텍스트가 포함된 단락에서 구조 요소를 설정하는 방법을 보여줍니다:

```python
import aspose.pdf as ap
import sys
from os import path

def set_elements(imagefile, outfile):
    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        # Setting Title and Nature Language for document
        tagged_content.set_title("Link Elements Example")
        tagged_content.set_language("en-US")

        # Getting Root structure element (Document structure element)
        root_element = tagged_content.root_element

        paragraph_element_1 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_1, True)
        link_element_1 = tagged_content.create_link_element()
        paragraph_element_1.append_child(link_element_1, True)
        link_element_1.hyperlink = ap.WebHyperlink("http://google.com")
        link_element_1.set_text("Google")
        link_element_1.alternate_descriptions = "Link to Google"

        paragraph_element_2 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_2, True)
        link_element_2 = tagged_content.create_link_element()
        paragraph_element_2.append_child(link_element_2, True)
        link_element_2.hyperlink = ap.WebHyperlink("http://google.com")
        span_element_2 = tagged_content.create_span_element()
        span_element_2.set_text("Google")
        link_element_2.append_child(span_element_2, True)
        link_element_2.alternate_descriptions = "Link to Google"

        paragraph_element_3 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_3, True)
        link_element_3 = tagged_content.create_link_element()
        paragraph_element_3.append_child(link_element_3, True)
        link_element_3.hyperlink = ap.WebHyperlink("http://google.com")
        span_element_31 = tagged_content.create_span_element()
        span_element_31.set_text("G")
        span_element_32 = tagged_content.create_span_element()
        span_element_32.set_text("Google")
        link_element_3.append_child(span_element_31, True)
        link_element_3.set_text("-")
        link_element_3.append_child(span_element_32, True)
        link_element_3.alternate_descriptions = "Link to Google"

        paragraph_element_4 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_4, True)
        link_element_4 = tagged_content.create_link_element()
        paragraph_element_4.append_child(link_element_4, True)
        link_element_4.hyperlink = ap.WebHyperlink("http://google.com")
        link_element_4.set_text(
            "The multiline link: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google"
        )
        link_element_4.alternate_descriptions = "Link to Google (multiline)"

        paragraph_element_5 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_5, True)
        link_element_5 = tagged_content.create_link_element()
        paragraph_element_5.append_child(link_element_5, True)
        link_element_5.hyperlink = ap.WebHyperlink("http://google.com")
        figure_element_5 = tagged_content.create_figure_element()
        figure_element_5.set_image(imagefile, 1200)
        figure_element_5.alternative_text = "Google icon"
        link_layout_attributes = link_element_5.attributes.get_attributes(
            ap.logicalstructure.AttributeOwnerStandard.LAYOUT
        )
        placement_attribute = ap.logicalstructure.StructureAttribute(
            ap.logicalstructure.AttributeKey.PLACEMENT
        )
        placement_attribute.set_name_value(
            ap.logicalstructure.AttributeName.PLACEMENT_BLOCK
        )
        link_layout_attributes.set_attribute(placement_attribute)
        link_element_5.append_child(figure_element_5, True)
        link_element_5.alternate_descriptions = "Link to Google"

        # Save Tagged PDF Document
        document.save(outfile)
```

## 링크 구조 요소 설정

Aspose.PDF for Python via .NET API는 또한 링크 구조 요소를 추가할 수 있도록 허용합니다.

다음 코드 스니펫은 Tagged PDF 문서에 링크 구조 요소를 추가하는 방법을 보여줍니다:

```python
import aspose.pdf as ap
import sys
from os import path

def add_link_element(outfile):
    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        # Setting Title and Nature Language for document
        tagged_content.set_title("Text Elements Example")
        tagged_content.set_language("en-US")

        # Getting Root structure element (Document structure element)
        root_element = tagged_content.root_element

        paragraph_element_1 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_1, True)
        span_element_11 = tagged_content.create_span_element()
        span_element_11.set_text("Span_11")
        span_element_12 = tagged_content.create_span_element()
        span_element_12.set_text(" and Span_12.")
        paragraph_element_1.set_text("Paragraph with ")
        paragraph_element_1.append_child(span_element_11, True)
        paragraph_element_1.append_child(span_element_12, True)

        paragraph_element_2 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_2, True)
        span_element_21 = tagged_content.create_span_element()
        span_element_21.set_text("Span_21")
        span_element_22 = tagged_content.create_span_element()
        span_element_22.set_text("Span_22.")
        paragraph_element_2.append_child(span_element_21, True)
        paragraph_element_2.set_text(" and ")
        paragraph_element_2.append_child(span_element_22, True)

        paragraph_element_3 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_3, True)
        span_element_31 = tagged_content.create_span_element()
        span_element_31.set_text("Span_31")
        span_element_32 = tagged_content.create_span_element()
        span_element_32.set_text(" and Span_32")
        paragraph_element_3.append_child(span_element_31, True)
        paragraph_element_3.append_child(span_element_32, True)
        paragraph_element_3.set_text(".")

        paragraph_element_4 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_4, True)
        span_element_41 = tagged_content.create_span_element()
        span_element_411 = tagged_content.create_span_element()
        span_element_411.set_text("Span_411, ")
        span_element_41.set_text("Span_41, ")
        span_element_41.append_child(span_element_411, True)
        span_element_42 = tagged_content.create_span_element()
        span_element_421 = tagged_content.create_span_element()
        span_element_421.set_text("Span 421 and ")
        span_element_42.append_child(span_element_421, True)
        span_element_42.set_text("Span_42")
        paragraph_element_4.append_child(span_element_41, True)
        paragraph_element_4.append_child(span_element_42, True)
        paragraph_element_4.set_text(".")

        # Save Tagged PDF Document
        document.save(outfile)
```

## 노트 구조 요소 설정

Aspose.PDF for Python via .NET API도 추가할 수 있습니다 [노트 요소](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/noteelement/) 태그가 지정된 PDF 문서에서. 다음 코드 조각은 태그가 지정된 PDF 문서에 note 요소를 추가하는 방법을 보여줍니다:

```python
import aspose.pdf as ap
import sys
from os import path

def set_note_element(outfile):
    # Create PDF Document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Sample of Note Elements")
        tagged_content.set_language("en-US")

        # Add Paragraph Element
        paragraph_element = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph_element, True)

        # Add NoteElement
        note_element_1 = tagged_content.create_note_element()
        paragraph_element.append_child(note_element_1, True)
        note_element_1.set_text("Note with auto generate ID. ")

        # Add NoteElement
        note_element_2 = tagged_content.create_note_element()
        paragraph_element.append_child(note_element_2, True)
        note_element_2.set_text("Note with ID = 'note_002'. ")
        note_element_2.set_id("note_002")

        # Add NoteElement
        note_element_3 = tagged_content.create_note_element()
        paragraph_element.append_child(note_element_3, True)
        note_element_3.set_text("Note with ID = 'note_003'. ")
        note_element_3.set_id("note_003")

        # Must throw exception - Aspose.Pdf.Tagged.TaggedException : Structure element with ID='note_002' already exists
        # note_element_3.set_id("note_002")

        # Resultant document does not compliance to PDF/UA If ClearId() used for Note Structure Element
        # note_element_3.clear_id()

        # Save Tagged PDF Document
        document.save(outfile)
```

## 언어 및 제목 설정 방법

Aspose.PDF for Python via .NET API는 PDF/UA 사양에 따라 문서의 언어와 제목을 설정할 수 있습니다. 언어는 전체 문서와 개별 구조 요소 모두에 대해 설정할 수 있습니다. 다음 코드 스니펫은 Tagged PDF Document에서 언어와 제목을 et 하는 방법을 보여줍니다.

1. 새 태그가 지정된 PDF 문서를 만듭니다.
1. 문서 제목과 언어를 설정하십시오.
1. 헤더 요소를 생성합니다.
1. 특정 언어로 단락을 추가합니다.
1. 태그가 지정된 PDF를 저장합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def set_language_and_title(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get TaggedContent
        tagged_content = document.tagged_content

        # Set Title and Language
        tagged_content.set_title("Example Tagged Document")
        tagged_content.set_language("en-US")

        # Header (en-US, inherited from document)
        header_element = tagged_content.create_header_element(1)
        header_element.set_text("Phrase on different languages")
        tagged_content.root_element.append_child(header_element, True)

        # Paragraph (English)
        paragraph_element_en = tagged_content.create_paragraph_element()
        paragraph_element_en.set_text("Hello, World!")
        paragraph_element_en.language = "en-US"
        tagged_content.root_element.append_child(paragraph_element_en, True)

        # Paragraph (German)
        paragraph_element_de = tagged_content.create_paragraph_element()
        paragraph_element_de.set_text("Hallo Welt!")
        paragraph_element_de.language = "de-DE"
        tagged_content.root_element.append_child(paragraph_element_de, True)

        # Paragraph (French)
        paragraph_element_fr = tagged_content.create_paragraph_element()
        paragraph_element_fr.set_text("Bonjour le monde!")
        paragraph_element_fr.language = "fr-FR"
        tagged_content.root_element.append_child(paragraph_element_fr, True)

        # Paragraph (Spanish)
        paragraph_element_sp = tagged_content.create_paragraph_element()
        paragraph_element_sp.set_text("¡Hola Mundo!")
        paragraph_element_sp.language = "es-ES"
        tagged_content.root_element.append_child(paragraph_element_sp, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

## 관련 Tagged PDF 주제

- [Tagged PDF 생성](/pdf/ko/python-net/create-tagged-pdf/) 속성을 업데이트하기 전에 구조 요소를 생성합니다.
- [Tagged PDF에서 태그된 콘텐츠 추출](/pdf/ko/python-net/extract-tagged-content-from-tagged-pdfs/) 기존 구조 노드와 메타데이터를 검사하려면.
- [태그된 PDF에서 테이블 작업](/pdf/ko/python-net/working-with-table-in-tagged-pdfs/) 테이블 구조에 접근성 속성을 적용해야 하는 경우.
