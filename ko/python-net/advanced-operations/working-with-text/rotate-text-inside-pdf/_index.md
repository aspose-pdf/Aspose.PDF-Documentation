---
title: 파이썬에서 PDF 텍스트 회전하기
linktitle: PDF 내에서 텍스트 회전
type: docs
weight: 50
url: /ko/python-net/rotate-text-inside-pdf/
description: Python에서 PDF 문서 내에서 텍스트 조각과 단락을 회전하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 문서의 텍스트 조각과 단락을 회전시키세요
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서의 텍스트를 회전하는 방법을 설명합니다.'TextFragment'에 '회전' 속성을 설정하고, 'TextBuilder'와 'TextParagraph'를 사용하여 회전된 콘텐츠를 만들고, 다양한 레이아웃 시나리오에서 회전된 텍스트를 페이지 단락에 직접 추가하는 방법을 보여줍니다.
---

.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 PDF 문서의 텍스트 조각을 회전시킬 수 있습니다.이 페이지에서는 다음을 사용하여 텍스트의 위치와 회전을 제어하는 방법을 보여줍니다. `TextFragment`, `TextState`, 및 `TextBuilder`.회전 각도를 조정하여 대각선 헤더, 세로 레이블, 회전된 주석과 같은 레이아웃을 만들 수 있습니다.

## PDF에서 텍스트 빌더를 사용하여 텍스트 조각 회전하기

라는 이름의 PDF 파일을 만듭니다. `rotated_fragments.pdf` 가로로 정렬된 세 개의 텍스트 조각 포함:

- 첫 번째 텍스트는 회전되지 않습니다
- 두 번째는 45° 회전합니다.
- 세 번째는 90° 회전합니다.

1. 새 PDF 문서 만들기
1. 회전된 텍스트를 호스트할 새 페이지를 삽입합니다.
1. 첫 번째 텍스트 조각을 만듭니다 (회전 없음).
1. 두 번째 텍스트 조각을 만듭니다 (45° 회전).
1. 세 번째 텍스트 조각을 만듭니다 (90° 회전).
1. 를 사용하여 텍스트 조각 추가 `TextBuilder`.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## PDF의 단락 내에서 개별 텍스트 조각 회전

단락 내에서 개별 텍스트 조각을 회전시킵니다.각각 고유한 회전 각도를 가진 여러 조각 (TextFragment) 을 포함하는 여러 줄 단락 (TextParagment) 을 만드는 방법을 보여줍니다.이 방법은 가로 방향과 대각선 방향의 텍스트 (예: 양식화된 머리글, 다이어그램 또는 주석이 달린 레이블) 를 결합하여 시각적으로 풍부한 문서를 만드는 데 유용합니다.

라는 이름의 PDF를 만듭니다. `rotated_paragraph_fragments.pdf` 세 줄의 텍스트가 있는 단락을 포함하며 각 줄은 다르게 회전합니다.

- 첫 번째 선이 45° 회전합니다.
- 두 번째 선은 수평 (0°) 으로 유지됩니다.
- 세 번째 선은 -45° 회전합니다.

1. 새 PDF 문서 만들기
1. 회전된 텍스트가 표시될 빈 페이지를 추가합니다.
1. 만들기 `TextParagraph`.
1. 첫 번째 텍스트 조각을 만들고 구성합니다 (+45° 회전).
1. 두 번째 텍스트 조각을 만듭니다 (회전 없음).
1. 세 번째 텍스트 조각을 만듭니다 (-45° 회전).
1. 단락에 텍스트 조각을 추가합니다.
1. 를 사용하여 페이지에 단락 추가 `TextBuilder`.
1. 문서를 저장합니다.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## PDF의 페이지 단락을 사용하여 텍스트 회전하기

이 단원에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 내에서 텍스트를 회전하는 간단한 방법을 보여줍니다.
저수준 접근 방식과 달리 `TextBuilder` 또는 `TextParagraph`, 이 메서드는 회전된 텍스트 조각을 페이지의 단락 컬렉션에 직접 추가합니다 (`page.paragraphs`).기본적인 텍스트 회전이 필요하지만 정확한 위치 지정이나 단락 구조가 필요하지 않은 경우에 이상적입니다.

라는 파일을 생성합니다 `simple_rotated_text.pdf` 포함:

- 기본 수평 텍스트 조각 0° 회전
- 315° 회전된 프래그먼트
- 270° 회전된 프래그먼트

1. 새 PDF 문서를 초기화합니다.
1. 회전된 텍스트를 배치할 페이지를 만듭니다.
1. 첫 번째 텍스트 조각을 만듭니다 (회전 없음).
1. 두 번째 텍스트 조각을 만듭니다 (315° 회전).
1. 세 번째 텍스트 조각을 만듭니다 (270° 회전).
1. 페이지 단락에 텍스트 조각을 직접 추가합니다.
1. PDF 문서를 저장합니다.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## PDF에서 전체 단락 회전

이 예제는 PDF의 고급 단락 수준 텍스트 회전을 보여줍니다.각 텍스트 부분이 개별적으로 회전되는 조각 수준 회전과 달리 이 방법은 전체 단락을 서로 다른 각도로 통합된 블록으로 회전합니다.
각 단락에는 스타일이 지정된 여러 텍스트 부분이 포함되어 있으며 전체 단락이 특정 각도로 회전되므로 복잡하고 일관된 레이아웃 변환이 가능합니다.
이는 전체 텍스트 섹션의 방향을 다양한 방향으로 지정해야 하는 예술적인 레이아웃, 워터마크 또는 디자인이 많은 PDF에 적합합니다.

를 생성합니다 `rotated_paragraphs.pdf`, 완전히 스타일이 지정되고 회전된 네 개의 단락이 포함되어 있습니다.

- 각각 고유한 각도 (45°, 135°, 225° 및 315°) 로 회전합니다.
- 각 단락에는 색상이 지정된 배경, 밑줄 및 일관된 스타일이 적용된 세 줄의 텍스트가 있습니다.

1. 새 PDF 문서 만들기
1. 회전된 단락을 담을 빈 페이지를 추가합니다.
1. 반복하여 여러 단락을 만들 수 있습니다.
1. 단락을 만들고 배치합니다.
1. 서식을 지정하여 텍스트 조각을 만들 수 있습니다.
1. 텍스트 서식을 적용합니다.
1. 단락에 텍스트 조각을 추가합니다.
1. 를 사용하여 페이지에 단락 추가 `TextBuilder`.
1. 네 회전 모두에 대해 반복합니다.
1. PDF 문서를 저장합니다.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## 관련 텍스트 주제

- [Python을 사용하여 PDF에서 텍스트 작업하기](/pdf/ko/python-net/working-with-text/)
- [PDF에 텍스트 추가](/pdf/ko/python-net/add-text-to-pdf-file/)
- [파이썬에서 PDF 텍스트 포맷 지정하기](/pdf/ko/python-net/text-formatting-inside-pdf/)
- [PDF의 텍스트를 파이썬으로 바꾸기](/pdf/ko/python-net/replace-text-in-pdf/)