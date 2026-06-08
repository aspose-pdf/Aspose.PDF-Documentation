---
title: Python으로 PDF의 텍스트 교체
linktitle: PDF의 텍스트 교체
type: docs
weight: 40
url: /ko/python-net/replace-text-in-pdf/
description: Python을 사용하여 PDF 파일의 텍스트를 교체하는 방법을 배우세요. 여기에는 페이지 전체에 걸친 텍스트 교체, 페이지 영역에 한정된 변경, 정규식을 사용한 교체, 그리고 텍스트 제거가 포함됩니다.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일의 텍스트를 교체하고 제거하세요.
Abstract: 이 문서에서는 Aspose.PDF for Python via .NET을 사용하여 PDF 문서의 텍스트를 교체하는 방법을 보여줍니다. 여기서는 모든 페이지에서의 텍스트 교체, 페이지 영역 교체, 정규식 매칭, Font 교체, 텍스트 레이아웃 조정, 그리고 표시되거나 숨겨진 텍스트 제거에 대해 다룹니다.
---

이 페이지에서는 **Python을 사용하여 PDF의 텍스트를 교체하는 방법**을 Aspose.PDF for Python via .NET을 사용하여 보여줍니다.

텍스트 값을 업데이트해야 하거나 원치 않는 콘텐츠를 제거하거나 특정 페이지 영역의 텍스트를 교체하거나 여러 PDF 페이지에 걸쳐 텍스트 교체 규칙을 적용해야 할 때 이 예제를 사용하십시오.

## Python으로 PDF의 텍스트 교체

### PDF 문서의 모든 페이지에서 텍스트 교체

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 온라인에서 텍스트 검색 및 교체를 시도할 수 있습니다. [편집 앱](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

텍스트 교체는 기존 PDF 문서의 내용을 업데이트하거나 수정할 때 흔히 필요한 작업입니다 — 예를 들어, 제품 이름을 변경하거나, 오타를 수정하거나, 여러 페이지에 걸쳐 용어를 업데이트하는 경우가 있습니다.

Aspose.PDF for Python via .NET은 프로그래밍 방식으로 텍스트를 검색하고 교체하는 강력하고 효율적인 방법을 제공합니다. [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 클래스.

이 예제는 특정 구문(이 경우는 "Black cat")의 모든 발생을 찾아 전체 PDF 문서에서 새로운 구문("White dog")으로 교체하는 방법을 보여줍니다.

1. 검색 및 교체 구문을 지정하십시오. 찾으려는 텍스트와 교체하려는 텍스트를 설정하십시오.
1. PDF 문서를 로드합니다.
1. 텍스트 흡수기를 생성합니다. TextFragmentAbsorber는 검색 구문으로 초기화됩니다. 이는 문서에서 해당 구문의 모든 인스턴스를 스캔합니다.
1. Absorber를 모든 페이지에 적용합니다. 이것은 모든 페이지를 순회하면서 해당 구문과 일치하는 텍스트 조각을 수집합니다.
1. 각 발견된 조각을 교체하십시오. "Black cat"의 모든 경우를 "White dog"로 바꾸어야 합니다.
1. 업데이트된 PDF를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### 특정 페이지 영역의 텍스트 교체

때때로 전체 문서를 검색하는 대신 PDF 페이지의 특정 영역 내에서만 텍스트를 교체해야 할 수도 있습니다 — 예를 들어, 알려진 위치에 있는 헤더, 푸터 또는 표 셀을 업데이트하는 경우.

Aspose.PDF for Python via .NET 라이브러리는 이 기능을 활용하여 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 지역 기반 텍스트 검색과 함께.

이 예제는 특정 페이지의 정의된 사각형 영역 내에서 대상 구문의 모든 발생을 찾아 교체하는 방법을 보여줍니다.

1. 검색 및 교체 구문을 지정하십시오.
1. PDF 문서를 로드합니다.
1. 검색을 위한 Text Absorber를 생성합니다. 원하는 텍스트를 찾기 위해 TextFragmentAbsorber를 초기화합니다.
1. 검색 영역을 제한합니다. 사각형은 페이지에서 x 및 y 좌표의 제한을 지정합니다.
1. Absorber를 특정 페이지에 적용합니다. 이는 지정된 영역 내에서 검색을 수행하고 일치하는 텍스트 조각을 수집합니다.
1. 찾은 텍스트를 교체합니다. 정의된 영역에서 'doc'가 나타나는 모든 경우는 'DOC'로 바뀝니다.
1. 업데이트된 PDF를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### 폰트 크기를 변경하지 않고 텍스트 크기 조정 및 이동

PDF에서 텍스트를 교체할 때, 때때로 글꼴 크기를 수정하지 않고 새 텍스트를 특정 영역에 맞추거나 재배치하고 싶을 수 있습니다.
Aspose.PDF for Python via .NET은 원래 글꼴 크기를 유지하면서 텍스트 레이아웃과 간격을 조정하는 옵션을 제공합니다.

1. PDF 문서를 로드합니다.
1. 페이지의 모든 텍스트 조각을 'TextFragmentAbsorber'를 사용하여 수집합니다.
1. 수정할 프래그먼트를 선택하십시오.
1. 텍스트 사각형을 이동하고 크기를 조정하십시오.
1. 텍스트 간격 조정. 수정된 사각형 내에 텍스트가 들어가도록 간격 조정을 활성화합니다.
1. 조각 텍스트를 교체하십시오.
1. 업데이트된 PDF를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### PDF에서 단락을 크기 조정하고 이동하기

PDF를 다룰 때, 때때로 페이지 레이아웃에 시각적으로 맞게 유지하면서 단락을 교체하거나 확장해야 할 필요가 있습니다. Aspose.PDF를 사용하면 단락의 경계 사각형 크기를 조정하고 새로운 텍스트에 맞게 간격을 맞출 수 있으며, 폰트 크기를 변경하지 않습니다.

1. PDF 문서를 로드합니다.
1. 페이지의 모든 텍스트 조각을 수집하려면 'TextFragmentAbsorber'를 사용하십시오.
1. 수정할 프래그먼트를 선택하십시오.
1. 단락의 크기를 조정하고 이동합니다. 페이지의 미디어 박스를 사용하여 경계를 결정하고 사각형을 조정합니다.
1. 간격 조정. 이는 글자 크기를 변경하는 대신 단어/글자 사이의 간격을 수정합니다.
1. 조각 텍스트를 교체하십시오.
1. 수정된 PDF를 저장하세요.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### 텍스트 교체 및 자동으로 폰트를 확장하여 대상 영역을 채우기

PDF의 텍스트를 교체하면서 자동으로 글꼴 크기를 조정하고 확장하여 특정 사각형 영역을 채웁니다. Aspose.PDF for Python via .NET 라이브러리를 사용하여 코드는 글꼴 크기와 간격을 동적으로 조정해 새로운 텍스트 내용이 정의된 경계 상자에 완벽하게 맞도록 합니다 — 수동으로 글꼴을 계산할 필요 없이.

1. PDF를 로드합니다.
1. 텍스트 조각 캡처.
1. 특정 조각을 선택하십시오.
1. 대상 사각형 정의.
1. 텍스트 조정 옵션을 활성화합니다.
1. 텍스트를 교체합니다.
1. 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### 텍스트를 교체하고 사각형에 맞추기

PDF 문서의 텍스트를 교체하면서, 필요할 경우 자동으로 글꼴 크기를 줄여 새로운 내용이 원래 텍스트의 사각형 영역에 맞도록 합니다.

Aspose.PDF for Python via .NET 라이브러리를 사용하여, 이 함수는 텍스트 레이아웃과 글꼴 크기를 동적으로 조정하여 문서 구조를 보존하면서 오버플로우를 방지합니다.

1. 첫 페이지에서 모든 텍스트 프래그먼트를 추출하기 위해 TextFragmentAbsorber 객체를 생성합니다.
1. 특정 텍스트 조각에 접근합니다.
1. 교체 영역을 설정합니다.
1. 텍스트 조정 옵션을 구성합니다. 두 가지 주요 교체 옵션을 설정합니다:
    - 글꼴 크기 조정 - 'SHRINK_TO_FIT'은 새로운 텍스트가 너무 길 경우 자동으로 글꼴 크기를 줄입니다.
    - 간격 조정 - 'ADJUST_SPACE_WIDTH'는 간격을 비례적으로 유지합니다.
1. 텍스트를 교체하십시오.
1. 수정된 PDF를 저장하세요.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### 플레이스홀더 텍스트를 자동으로 교체하고 PDF 레이아웃을 재배열

PDF 내부의 자리표시자 텍스트(예: 템플릿이나 양식)를 이름이나 회사 정보와 같은 실제 데이터로 교체합니다.
새 텍스트에 맞게 페이지 레이아웃을 자동으로 조정하면서 사용자 지정 서식(글꼴, 색상, 크기)을 적용합니다.

1. PDF를 가져와 로드합니다.
1. 플레이스홀더에 대한 Text Absorber를 생성합니다.
1. 흡수기를 모든 페이지에 적용합니다.
1. 찾은 텍스트 조각을 반복합니다.
1. 맞춤 텍스트 서식 적용.
1. 업데이트된 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### 정규 표현식을 기반으로 텍스트 교체

PDF 문서 작업 시 특정 문구 대신 패턴에 따라 나타나는 텍스트를 교체해야 할 수 있습니다 — 예를 들어 전화번호, 코드 또는 날짜와 같은 형식입니다.

Aspose.PDF for Python via .NET은 TextFragmentAbsorber 클래스를 사용하여 정규식(regex)으로 이러한 교체를 수행할 수 있습니다.

이 예제는 텍스트 패턴(이 경우 ####-#### 형식에 맞는 모든 텍스트, 예: 1234-5678)을 찾아서 형식이 지정된 문자열 'ABC1-2XZY'로 교체하는 방법을 보여줍니다. 또한 교체된 텍스트의 글꼴, 색상 및 크기를 사용자 지정하는 방법도 표시합니다.

다음 코드 스니펫은 정규 표현식을 기반으로 텍스트를 교체하는 방법을 보여줍니다.

1. PDF 문서를 로드합니다.
1. 정규식 기반 Text Absorber를 생성합니다. 정규식 패턴을 사용하여 TextFragmentAbsorber를 초기화합니다.
1. 정규식 모드를 활성화합니다. 'True' 매개변수는 정규식 검색 모드를 활성화합니다.
1. Absorber를 페이지에 적용합니다. 이는 정의된 정규식 패턴과 일치하는 모든 텍스트 조각을 페이지에서 스캔합니다.
1. 각 매치를 새 텍스트로 교체하고 맞춤 스타일을 적용합니다.
1. 수정된 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## 글꼴을 교체하거나 사용되지 않는 글꼴을 제거합니다

### 기존 PDF 파일에서 글꼴을 교체

때때로 PDF 전체에 걸쳐 글꼴을 표준화하거나 업데이트해야 할 때가 있습니다 — 예를 들어, 오래되거나 독점적인 글꼴을 더 접근하기 쉬운 글꼴로 교체하는 경우입니다. Aspose.PDF for Python via .NET 라이브러리를 사용하면 글꼴을 프로그래밍 방식으로 감지하고 교체할 수 있어 일관된 타이포그래피와 문서 호환성을 보장합니다.

이 예제는 PDF 문서 전체에서 특정 글꼴(예: 'Arial-BoldMT')의 모든 인스턴스를 다른 글꼴(예: 'Verdana')로 교체하는 방법을 보여줍니다.

다음 코드 스니펫은 PDF 문서 내의 글꼴을 교체하는 방법을 보여줍니다:

1. PDF 문서를 엽니다.
1. TextFragmentAbsorber를 초기화합니다.
1. Absorber를 사용하여 문서의 모든 페이지에서 텍스트 조각을 추출합니다.
1. 폰트를 식별하고 교체합니다. 스크립트는 fragment의 현재 폰트가 'Arial-BoldMT'인지 확인합니다. 참이면, FontRepository.find_font() 메서드를 사용하여 'Verdana' 폰트로 교체합니다.
1. 수정된 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### 사용되지 않는 Font 제거

시간이 지남에 따라 PDF 문서는 사용되지 않거나 내장된 글꼴이 누적되어 파일 크기가 늘어나고 처리 속도가 느려질 수 있습니다. 이러한 사용되지 않은 글꼴은 텍스트 편집이나 교체 후에도 특히 대형 또는 복잡한 PDF 작업 시에도 남아 있는 경우가 많습니다.

Aspose.PDF for Python via .NET 라이브러리는 TextEditOptions 클래스를 사용하여 이러한 중복 글꼴을 제거하는 효율적인 방법을 제공합니다. 이는 문서를 최적화할 뿐만 아니라 실제로 보이는 텍스트에 적용된 글꼴만을 사용하도록 보장합니다.

'remove_unused_fonts()' 메서드는 중복된 글꼴 데이터를 제거하여 PDF 파일을 최적화하는 간단하지만 강력한 방법입니다.

이 예제는 다음을 보여줍니다:

- 사용되지 않은 글꼴을 찾기 위해 PDF를 스캔합니다.
- 안전하게 제거하십시오.
- 활성 텍스트 조각을 일관된 글꼴(예: Times New Roman)로 재할당합니다.

1. PDF 문서를 엽니다.
1. 텍스트 편집 옵션을 구성합니다. 이는 엔진에게 현재 화면에 표시된 텍스트에서 사용되지 않은 모든 임베디드 글꼴을 제거하도록 지시합니다.
1. 옵션과 함께 Text Absorber를 생성합니다. TextFragmentAbsorber는 편집을 위해 문서에서 텍스트 조각을 추출합니다.
1. 표준 글꼴을 다시 할당합니다. 흡수기가 모든 조각을 수집한 후, 이를 반복하면서 일관된 글꼴을 적용합니다.
1. 정리된 PDF를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## 모든 텍스트 제거

### PDF에서 텍스트 제거

PDF 파일에서 모든 텍스트 내용을 제거하되 이미지, 도형 및 레이아웃 구조는 그대로 유지합니다.
TextFragmentAbsorber를 사용하면, 코드는 전체 문서를 효율적으로 스캔하고 각 페이지에서 발견되는 모든 텍스트 조각을 삭제합니다.

1. PDF 문서를 로드합니다.
1. PDF에서 텍스트 조각을 감지하고 처리하기 위해 TextFragmentAbsorber 객체가 생성됩니다.
1. 모든 텍스트 내용을 제거합니다. 메서드 ‘absorber.remove_all_text()’는 로드된 문서에서 모든 텍스트 요소를 제거하고, 텍스트가 아닌 구성 요소는 untouched 상태로 남깁니다.
1. 업데이트된 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### 특정 페이지의 모든 텍스트 제거

Aspose.PDF의 TextFragmentAbsorber 클래스를 사용하여 PDF 문서의 단일 페이지에서 모든 텍스트를 제거합니다.
전체 문서 삭제와 달리, 이 방법은 페이지 수준의 텍스트 정리를 수행하여 선택된 페이지의 텍스트만 삭제하고 다른 모든 페이지는 그대로 둡니다.

1. PDF 파일을 로드합니다.
1. TextFragmentAbsorber 인스턴스를 생성합니다.
1. 첫 페이지의 모든 텍스트를 제거하십시오.
1. 수정된 PDF를 저장하세요.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### PDF 페이지의 특정 영역에서 모든 텍스트를 제거합니다

Aspose.PDF의 TextFragmentAbsorber를 사용하여 페이지의 특정 직사각형 영역에서 모든 텍스트를 제거합니다.
전체 페이지를 지우는 대신, 이 메서드는 대상 텍스트 제거를 수행하여 페이지의 어떤 부분이 영향을 받는지 정확하게 제어할 수 있습니다.

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber를 생성합니다.
1. 대상 영역(사각형)을 정의합니다.
1. 지정된 영역에서 텍스트를 제거합니다.
1. 문서의 나머지를 보존하십시오.
1. 수정된 PDF를 저장하세요.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### PDF 문서에서 모든 숨겨진 Text를 제거합니다

Aspose.PDF의 TextFragmentAbsorber를 사용하여 페이지의 특정 직사각형 영역에서 모든 텍스트를 제거합니다.
전체 페이지를 지우는 대신, 이 메서드는 대상 텍스트 제거를 수행하여 페이지의 어떤 부분이 영향을 받는지 정확하게 제어할 수 있습니다.

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber를 생성합니다.
1. 대상 영역(사각형)을 정의합니다.
1. 지정된 영역에서 텍스트를 제거합니다.
1. 문서의 나머지를 보존하십시오.
1. 수정된 PDF를 저장하세요.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## 관련 텍스트 주제

- [Python을 사용하여 PDF에서 텍스트 작업](/pdf/ko/python-net/working-with-text/)
- [PDF에 텍스트 추가](/pdf/ko/python-net/add-text-to-pdf-file/)
- [Python에서 PDF 텍스트를 검색하고 추출하기](/pdf/ko/python-net/search-and-get-text-from-pdf/)
- [Python에서 PDF 텍스트 서식 지정](/pdf/ko/python-net/text-formatting-inside-pdf/)
