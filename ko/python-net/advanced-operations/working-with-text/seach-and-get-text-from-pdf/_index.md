---
title: 파이썬에서 PDF 텍스트 검색 및 추출
linktitle: 검색 및 텍스트 가져오기
type: docs
weight: 60
url: /ko/python-net/search-and-get-text-from-pdf/
description: Python에서 PDF 문서에서 텍스트를 검색, 검사 및 추출하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 텍스트 검색 및 추출된 조각 검사
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서에서 텍스트를 검색하고 추출하는 방법을 설명합니다.영역 기반 추출, 페이지별 검색, 구문 매칭, 텍스트 위치 및 글꼴 속성 검사 등 'TextAbsorber'와 'TextFragmentAbsorber'에 대해 다룹니다.
---

## PDF에서 텍스트 검색

를 사용하여 PDF 문서의 정의된 사각형 영역에서 텍스트를 검색하고 추출합니다. `TextAbsorber` 수업.형식이 지정되지 않은 깔끔한 출력을 위해 순수 텍스트 서식 지정 모드를 사용하는데, 이는 머리글, 바닥글 또는 표 영역과 같은 구조화된 영역에서 콘텐츠를 추출하는 데 유용합니다.결합하여 `TextExtractionOptions` 과 `TextSearchOptions` 직사각형 구속조건을 사용하여 문자를 추출하는 위치와 방법을 제어할 수 있습니다.

PDF 텍스트 내용을 감사하거나, 분석을 위해 텍스트를 추출하거나, 일치하는 텍스트 조각의 위치 및 형식을 검사해야 할 때 이 페이지를 사용하십시오.

1. 'AP.Document'를 사용하여 PDF 파일을 로드합니다.
1. 텍스트 추출 옵션을 구성합니다.
1. 사각형 제약 조건을 사용하여 검색 영역을 정의합니다.
1. 텍스트 흡수기 만들기 및 구성
1. 문서의 모든 페이지를 처리합니다.
1. 추출된 텍스트 검색 및 표시

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## 특정 PDF 페이지에서 텍스트 검색

Aspose.PDF TextAbsorber를 사용하여 PDF의 특정 페이지 및 영역에서 텍스트를 검색하고 추출할 수 있습니다.문서의 2페이지를 대상으로 하며 정의된 사각형 영역 내에 있는 텍스트만 추출합니다.
텍스트 추출 옵션 (서식 제어용) 과 TextSearchOptions (영역 제한용) 를 결합하여 페이지별 정확한 텍스트 추출을 효율적으로 수행할 수 있습니다.

1. PDF 문서를 로드합니다.
1. 텍스트 추출 옵션을 설정합니다.
1. 텍스트 추출을 페이지의 특정 사각형 영역으로 제한합니다.
1. 텍스트 흡수기 만들기 및 구성
1. 특정 페이지를 처리합니다.
1. 추출된 텍스트 검색 및 표시

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## PDF에서 상세한 텍스트 조각 속성 분석 및 추출

원시 텍스트를 추출하는 TextAbsorber와 달리 TextFragmentAbsorber는 위치, 글꼴 특성, 색상, 임베딩 세부 정보 등 각 텍스트 조각에 대한 자세한 저수준 정보를 제공합니다.

1. PDF 문서를 로드합니다.
1. 텍스트 조각 흡수기를 초기화합니다.
1. 문서의 모든 페이지를 처리합니다.
1. 추출한 텍스트 조각을 반복합니다.
1. 기본 텍스트 정보를 인쇄합니다.
1. 글꼴 및 서식 세부 정보를 인쇄합니다.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## 단일 PDF 페이지에서 특정 텍스트 문구 검색

TextFragmentAbsorber를 사용하여 PDF 문서의 페이지 내에서 특정 텍스트 구문을 검색합니다.전체 문서를 검색하는 것과 달리 이 방법은 검색을 한 페이지로만 제한하므로 머리글, 바닥글 또는 특정 콘텐츠 섹션과 같은 대상 영역에서 텍스트의 존재 여부와 위치를 보다 효율적으로 확인할 수 있습니다.

1. PDF 문서를 로드합니다.
1. 검색 구문을 사용하여 텍스트 프래그먼트 업소버를 초기화합니다.
1. 특정 페이지에 업소버를 적용합니다.
1. 찾은 조각을 반복하세요.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 누적 결과를 사용한 페이지별 텍스트 순차 검색

Aspose.PDF TextFragmentAbsorber를 사용하여 PDF 문서의 여러 페이지에서 텍스트를 점진적으로 검색합니다.
단일 페이지 또는 문서 전체 검색과 달리 이 방법을 사용하면 페이지를 순차적으로 처리하고 결과를 점진적으로 수집하며 페이지별 컨텍스트를 사용하여 텍스트 조각을 분석할 수 있습니다.이 방법은 대형 문서나 점진적 처리 워크플로우에 적합합니다.

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber를 초기화하고 검색 구문을 설정합니다.
1. 프로세스 첫 페이지.1페이지만 검색하세요.텍스트, 페이지 번호 및 위치를 인쇄합니다.명확성을 위해 분리된 페이지별 결과를 제공합니다.
1. 다음 페이지를 순차적으로 처리합니다.2페이지로 이동하고 필요에 따라 문서의 나머지 부분을 계속 진행하십시오.'absorber.visit () '을 사용하면 방문한 모든 페이지의 결과가 누적됩니다.텍스트와 위치를 모두 보여 주는 누적 검색 결과를 인쇄합니다.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## 사각형 영역 내에서 대상 구문 검색

검색을 단일 페이지의 특정 사각형 영역으로 제한하면서 PDF에서 특정 문구를 검색합니다.
구문 검색과 공간적 제약을 결합하면 전체 페이지나 문서를 스캔하지 않고도 지정된 영역에서 콘텐츠를 정확하게 찾을 수 있습니다.이는 콘텐츠가 예측 가능한 위치에 표시되는 양식, 머리글, 바닥글 또는 구조화된 보고서에 특히 유용합니다.

1. PDF 문서를 로드합니다.
1. 구문 및 사각형 제약 조건을 사용하여 TextFragmentAbsorber 초기화하기
1. 페이지 2에 흡수제를 바릅니다.처리를 2페이지로 제한하여 불필요한 계산을 줄입니다.페이지별로 검색되도록 합니다.
1. 발견된 조각을 반복하고 인쇄하기

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 정규 표현식을 사용하여 PDF에서 텍스트 패턴 검색

정규 표현식을 사용하여 PDF에서 텍스트 패턴을 검색합니다.TextFragmentAbsorber에서 정규식 모드를 활성화하면 숫자, 날짜, 가격, 좌표 또는 사용자 지정 텍스트 형식과 같은 복잡한 패턴을 찾을 수 있습니다.이 함수는 검색을 특정 페이지로 제한하므로 구조화된 데이터를 표적으로 추출하는 데 효과적입니다.

1. PDF 문서를 로드합니다.
1. 정규식 패턴으로 TextFragmentAbsorber를 초기화합니다.
1. 페이지 2에 흡수제를 바릅니다.효율성과 정확성을 위해 검색을 2페이지로 제한합니다.이 페이지의 텍스트만 분석됩니다.
1. 찾은 조각을 반복해서 살펴보세요.일치하는 텍스트 조각과 해당 좌표를 인쇄합니다.추출된 패턴의 정확한 위치 정보를 제공합니다.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## TextFragmentAbsorber를 사용하여 텍스트 일치 항목을 PDF의 하이퍼링크로 변환

PDF에서 특정 텍스트 구문을 검색하고 클릭 가능한 하이퍼링크로 변환할 수 있습니다.정규식 패턴과 함께 TextFragmentAbsorber를 사용하여 대상 단어를 찾고 대화형 링크와 함께 시각적 스타일 (색상 및 밑줄) 을 적용합니다.

1. PDF 문서를 로드합니다.
1. 정규식 패턴으로 TextFragmentAbsorber를 초기화합니다.
1. 페이지 1에 흡수제를 바릅니다.
1. 매치에 스타일 지정 및 하이퍼링크 추가
1. 수정된 PDF를 저장합니다.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## 텍스트 조각 흡수기를 사용하여 PDF에서 스타일이 지정된 텍스트 검색 및 식별

내용이 아닌 서식 속성을 기준으로 PDF에서 텍스트 부분을 검색합니다.TextFragmentAbsorber를 사용하여 굵은 텍스트와 같은 특정 스타일의 텍스트를 식별합니다.

1. PDF 문서를 로드합니다.
1. 텍스트 조각 흡수기를 초기화합니다.
1. 페이지 1에 흡수제를 바릅니다.
1. 서식을 기반으로 텍스트 조각을 검사합니다.글꼴 스타일에 굵은 글꼴이 있는지 확인합니다.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## PDF 페이지의 시각적 텍스트 강조

이 기능은 텍스트 인식과 렌더링을 단일 워크플로우로 결합합니다.텍스트를 추출할 뿐만 아니라 각 페이지의 PNG 이미지에서 색상으로 구분된 사각형의 조각, 세그먼트 및 문자를 강조 표시하여 텍스트를 시각화합니다.

이 예제에서는 다음과 같은 방법으로 PDF에서 고급 텍스트 시각화를 수행합니다.

- 정규 표현식을 사용하여 보이는 모든 텍스트 조각 검색
- 각 PDF 페이지를 고해상도 PNG 이미지로 렌더링
- 텍스트 조각, 텍스트 세그먼트 및 개별 문자 주위에 색상이 지정된 사각형 그리기

1. 출력 이미지 해상도를 설정합니다.각 PDF 페이지는 150DPI PNG 이미지로 변환됩니다.
1. PDF를 열고 텍스트 흡수기를 초기화합니다.
1. 각 페이지를 처리합니다.모든 페이지에 흡수제를 바릅니다.감지된 모든 텍스트 조각과 그 기하학적 위치를 수집하세요.
1. 페이지를 PNG 스트림으로 변환합니다.
1. 그리기를 위한 그래픽스 객체 준비
1. 좌표 변환 적용PDF 좌표를 이미지 픽셀로 변환합니다.
1. 텍스트 요소에 사각형을 그립니다.
1. 결과를 저장합니다.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```

## 관련 텍스트 주제

- [Python을 사용하여 PDF에서 텍스트 작업하기](/pdf/ko/python-net/working-with-text/)
- [파이썬을 통해 PDF의 텍스트 바꾸기](/pdf/ko/python-net/replace-text-in-pdf/)
- [Python에서 PDF 텍스트에 툴팁 추가](/pdf/ko/python-net/pdf-tooltip/)
- [PDF에 텍스트 추가](/pdf/ko/python-net/add-text-to-pdf-file/)