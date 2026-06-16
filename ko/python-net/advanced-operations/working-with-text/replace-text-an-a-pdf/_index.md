---
title: PDF의 텍스트를 파이썬으로 바꾸기
linktitle: PDF에서 텍스트 바꾸기
type: docs
weight: 40
url: /ko/python-net/replace-text-in-pdf/
description: 페이지 간 텍스트 바꾸기, 페이지 영역 변경 제한, 정규식 사용, 텍스트 제거 등 PDF 파일의 텍스트를 Python으로 바꾸는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF 파일의 텍스트 바꾸기 및 제거
Abstract: 이 문서에서는.NET을 통해 PDF 문서의 텍스트를 Python용 Aspose.PDF 로 바꾸는 방법을 보여줍니다.전체 페이지의 텍스트 바꾸기, 페이지 영역 바꾸기, 정규식 일치, 글꼴 바꾸기, 텍스트 레이아웃 조정, 보이거나 숨겨진 텍스트 제거에 대해 다룹니다.
---

이 페이지에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여**PDF의 텍스트를 파이썬으로 대체**하는 방법을 보여줍니다.

텍스트 값을 업데이트하거나, 불필요한 내용을 제거하거나, 특정 페이지 영역의 텍스트를 바꾸거나, 여러 PDF 페이지에 텍스트 대체 규칙을 적용해야 할 때 이러한 예를 사용하십시오.

## PDF의 텍스트를 파이썬으로 바꾸기

### PDF 문서의 모든 페이지에서 텍스트 바꾸기

{{% alert color="primary" %}}

Aspose.PDF 파일을 사용하여 온라인으로 텍스트 검색 및 바꾸기를 시도할 수 있습니다. [편집 앱](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

텍스트 교체는 제품 이름 변경, 오타 수정, 여러 페이지의 용어 업데이트 등 기존 PDF 문서의 내용을 업데이트하거나 수정할 때 일반적으로 필요한 요구 사항입니다.

.NET을 통한 Python용 Aspose.PDF 는 프로그래밍 방식으로 텍스트를 검색하고 바꾸는 강력하고 효율적인 방법을 제공합니다. [텍스트 프래그먼트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 수업.

이 예제에서는 전체 PDF 문서에서 나타나는 특정 문구 (이 경우 “Black cat”) 를 모두 찾아 새 문구 (“White dog”) 로 바꾸는 방법을 보여줍니다.

1. 검색 및 대체 문구를 지정합니다.찾으려는 텍스트와 대체하려는 텍스트를 설정합니다.
1. PDF 문서를 로드합니다.
1. 텍스트 흡수기 만들기.텍스트 프래그먼트 업소버는 검색 구문을 사용하여 초기화됩니다.문서에서 해당 구문의 모든 인스턴스를 검색합니다.
1. 모든 페이지에 흡수기를 적용합니다.이렇게 하면 모든 페이지가 반복되고 해당 문구와 일치하는 텍스트 조각이 수집됩니다.
1. 찾은 각 조각을 교체하십시오.“검은 고양이”의 모든 인스턴스를 “흰색 개”로 변경해야 합니다.
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

### 특정 페이지 영역의 텍스트 바꾸기

전체 문서를 검색하는 대신 PDF 페이지의 특정 영역 내에서만 텍스트를 바꿔야 하는 경우가 있습니다 (예: 알려진 위치의 머리글, 바닥글 또는 표 셀 업데이트).

.NET 라이브러리를 통한 파이썬용 Aspose.PDF 라이브러리는 다음을 활용하여 이 기능을 가능하게 합니다. [텍스트 프래그먼트 업소버](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 지역 기반 텍스트 검색과 함께 사용할 수 있습니다.

이 예제에서는 특정 페이지의 정의된 사각형 영역 내에 있는 대상 문구를 모두 찾아 바꾸는 방법을 보여줍니다.

1. 검색 및 대체 문구를 지정합니다.
1. PDF 문서를 로드합니다.
1. 검색을 위한 텍스트 흡수기를 만드세요.TextFragmentAbsorber를 초기화하여 원하는 텍스트를 찾으십시오.
1. 검색 영역을 제한합니다.사각형은 페이지의 x 및 y 좌표 제한을 지정합니다.
1. 특정 페이지에 업소버를 적용합니다.그러면 검색이 수행되고 지정된 영역 내에서 일치하는 텍스트 조각이 수집됩니다.
1. 찾은 텍스트를 바꿉니다.정의된 영역에 'doc'이 나타날 때마다 'DOC'가 됩니다.
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

### 글꼴 크기를 변경하지 않고 텍스트 크기 조정 및 이동

PDF에서 텍스트를 바꿀 때 글꼴 크기를 수정하지 않고 특정 영역에 새 텍스트를 맞추거나 위치를 조정해야 하는 경우가 있습니다.
.NET을 통한 Python용 Aspose.PDF 파일은 원래 글꼴 크기를 그대로 유지하면서 텍스트 레이아웃과 간격을 조정할 수 있는 옵션을 제공합니다.

1. PDF 문서를 로드합니다.
1. 'TextFragmentAbsorber'를 사용하여 페이지의 모든 텍스트 조각을 수집하세요.
1. 수정할 프래그먼트를 선택합니다.
1. 텍스트 사각형을 이동하고 크기를 조정합니다.
1. 텍스트 간격을 조정합니다.수정된 사각형 내에 텍스트가 맞도록 간격 조정을 활성화합니다.
1. 프래그먼트 텍스트를 교체합니다.
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

### PDF에서 단락 크기 조정 및 이동

PDF로 작업할 때 페이지 레이아웃에 맞게 시각적으로 정렬된 상태로 단락을 바꾸거나 확장해야 하는 경우가 있습니다.Aspose.PDF 기능을 사용하면 글꼴 크기를 변경하지 않고도 단락의 테두리 사각형 크기를 조정하고 새 텍스트에 맞게 간격을 조정할 수 있습니다.

1. PDF 문서를 로드합니다.
1. 페이지의 모든 텍스트 조각을 수집하려면 '텍스트 조각 흡수기'를 사용하십시오.
1. 수정할 프래그먼트를 선택합니다.
1. 단락의 크기를 조정하고 이동하십시오.페이지의 미디어 상자를 사용하여 경계를 결정하고 사각형을 조정합니다.
1. 간격을 조정합니다.이렇게 하면 글꼴 크기를 변경하는 대신 단어/글자 사이의 간격이 수정됩니다.
1. 프래그먼트 텍스트를 교체합니다.
1. 수정한 PDF를 저장합니다.

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

### 텍스트 바꾸기 및 대상 영역 채우기에 맞게 글꼴 자동 확장

특정 사각형 영역을 채우도록 글꼴의 크기를 자동으로 조정하고 확장하면서 PDF의 텍스트를 교체할 수 있습니다.이 코드는 Aspose.PDF for Python.NET 라이브러리를 사용하여 수동으로 글꼴을 계산할 필요 없이 새 텍스트 내용이 정의된 경계 상자에 완벽하게 맞도록 글꼴 크기와 간격을 동적으로 조정합니다.

1. PDF를 로드합니다.
1. 텍스트 조각 캡처.
1. 특정 프래그먼트를 선택합니다.
1. 대상 사각형을 정의합니다.
1. 텍스트 조정 옵션을 활성화합니다.
1. 텍스트 바꾸기.
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

### 텍스트 바꾸기 및 사각형에 맞추기

필요한 경우 글꼴 크기를 자동으로 줄여 새 내용이 원본 텍스트의 사각형 영역에 맞도록 하면서 PDF 문서의 텍스트를 교체합니다.

.NET 라이브러리를 통해 Aspose.PDF for Python을 사용하는 이 함수는 오버플로를 방지하면서 문서 구조를 보존하면서 텍스트 레이아웃과 글꼴 크기를 모두 동적으로 조정합니다.

1. TextFragmentAbsorber 객체를 만들어 첫 페이지에서 모든 텍스트 조각을 추출합니다.
1. 특정 텍스트 조각에 액세스하십시오.
1. 교체 영역을 설정합니다.
1. 텍스트 조정 옵션을 구성합니다.두 가지 주요 교체 옵션을 설정합니다.
    - 글꼴 크기 조정 - 'SHRINK_TO_FIT'은 새 텍스트가 너무 길 경우 글꼴 크기를 자동으로 줄입니다.
    - 간격 조정 - 'ADJUST_SPACE_WIDTH'는 간격을 비례적으로 유지합니다.
1. 텍스트를 교체합니다.
1. 수정한 PDF를 저장합니다.

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

### 자동으로 자리표시자 텍스트 바꾸기 및 PDF 레이아웃 재정렬

PDF 내의 자리 표시자 텍스트 (예: 템플릿 또는 양식) 를 이름이나 회사 정보와 같은 실제 데이터로 바꿉니다.
사용자 지정 서식 (글꼴, 색상, 크기) 을 적용하면서 새 텍스트에 맞게 페이지 레이아웃을 자동으로 조정합니다.

1. PDF를 가져오고 로드합니다.
1. 플레이스홀더를 위한 텍스트 흡수기를 만드세요.
1. 모든 페이지에 흡수기를 적용합니다.
1. 찾은 텍스트 조각을 반복해서 살펴보세요.
1. 사용자 지정 텍스트 서식을 적용합니다.
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

### 정규 표현식을 기반으로 텍스트 바꾸기

PDF 문서로 작업할 때 전화번호, 코드 또는 날짜와 같은 형식 등 특정 문구가 아닌 패턴을 따르는 텍스트를 바꿔야 할 수 있습니다.

.NET을 통한 파이썬용 Aspose.PDF 기능을 사용하면 TextFragmentAbsorber 클래스의 정규 표현식 (regex) 을 사용하여 이러한 대체 작업을 수행할 수 있습니다.

이 예제에서는 텍스트 패턴 (이 경우 1234-5678과 같이 ###-## 형식과 일치하는 모든 텍스트) 을 찾아 서식이 지정된 문자열 'ABC1-2XZY'로 바꾸는 방법을 보여 줍니다.또한 대체된 텍스트의 글꼴, 색상 및 크기를 사용자 지정하는 방법도 보여 줍니다.

다음 코드 스니펫은 정규 표현식을 기반으로 텍스트를 바꾸는 방법을 보여줍니다.

1. PDF 문서를 로드합니다.
1. 정규식 기반 텍스트 흡수기 만들기정규 표현식 패턴을 사용하여 TextFragment의 흡수기를 초기화합니다.
1. 정규 표현식 모드를 활성화합니다.'True' 파라미터는 정규 표현식 검색 모드를 활성화합니다.
1. 페이지에 업소버를 적용합니다.이렇게 하면 페이지에서 정의된 정규식 패턴과 일치하는 모든 텍스트 부분이 검색됩니다.
1. 각 일치 항목을 새 텍스트로 바꾸고 사용자 지정 스타일을 적용하세요.
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

## 글꼴 바꾸기 또는 사용하지 않는 글꼴 제거

### 기존 PDF 파일의 글꼴 바꾸기

경우에 따라 PDF 전체의 글꼴을 표준화하거나 업데이트해야 합니다. 예를 들어 오래되거나 독점 글꼴을 접근하기 쉬운 글꼴로 교체해야 합니다..NET 라이브러리를 통한 Python용 Aspose.PDF 라이브러리를 사용하면 프로그래밍 방식으로 글꼴을 검색하고 바꿀 수 있으므로 일관된 타이포그래피와 문서 호환성을 보장할 수 있습니다.

이 예제는 PDF 문서 전체에서 특정 글꼴 (예: 'Arial-Boldmt') 의 모든 인스턴스를 다른 글꼴 (예: 'Verdana') 로 바꾸는 방법을 보여줍니다.

다음 코드 스니펫은 PDF 문서 내에서 글꼴을 바꾸는 방법을 보여줍니다.

1. PDF 문서를 엽니다.
1. 텍스트 조각 흡수기를 초기화합니다.
1. 흡수기를 사용하여 문서의 모든 페이지에서 텍스트 조각을 추출합니다.
1. 글꼴 식별 및 바꾸기.스크립트는 프래그먼트의 현재 글꼴이 'Arial-BoldMt'인지 확인합니다.참인 경우 FontRepository.find_font () 메서드를 사용하여 '베르다나' 글꼴로 대체합니다.
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

### 사용하지 않는 글꼴 제거

시간이 지남에 따라 PDF 문서에는 사용하지 않거나 포함된 글꼴이 누적되어 파일 크기가 커지고 처리 속도가 느려질 수 있습니다.이러한 미사용 글꼴은 특히 크거나 복잡한 PDF로 작업할 때 텍스트를 편집하거나 교체한 후에도 그대로 남아 있는 경우가 많습니다.

.NET을 통한 파이썬용 Aspose.PDF 라이브러리는 TextEditOptions 클래스를 사용하여 이러한 중복 글꼴을 제거하는 효율적인 방법을 제공합니다.이렇게 하면 문서가 최적화될 뿐만 아니라 보이는 텍스트에 실제로 적용된 글꼴만 사용되도록 할 수 있습니다.

'remove_unused_fonts () '메서드는 중복 글꼴 데이터를 제거하여 PDF 파일을 최적화하는 간단하면서도 강력한 방법입니다.

이 예제에서는 다음 방법을 보여줍니다.

- PDF에서 사용하지 않은 글꼴을 스캔합니다.
- 안전하게 제거하십시오.
- 활성 텍스트 부분을 일관된 글꼴로 재할당합니다 (예: Times New Roman).

1. PDF 문서를 엽니다.
1. 텍스트 편집 옵션을 구성합니다.그러면 엔진이 현재 보이는 텍스트에 사용되지 않는 포함된 글꼴을 제거하도록 지시합니다.
1. 옵션을 사용하여 텍스트 흡수기를 만드십시오.텍스트 조각 흡수기는 편집을 위해 문서에서 텍스트 조각을 추출합니다.
1. 표준 글꼴을 재할당합니다.업소버가 모든 조각을 수집한 후에는 이를 반복하여 일관된 글꼴을 적용하세요.
1. 정리한 PDF를 저장합니다.

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

이미지, 도형 및 레이아웃 구조를 그대로 유지하면서 PDF 파일에서 모든 텍스트 내용을 제거합니다.
코드는 TextFragmentAbsorber를 사용하여 전체 문서를 효율적으로 스캔하고 각 페이지에 있는 모든 텍스트 조각을 삭제합니다.

1. PDF 문서를 로드합니다.
1. TextFragmentAbsorber 객체는 PDF에서 텍스트 부분을 감지하고 처리하기 위해 만들어집니다.
1. 모든 텍스트 내용을 제거합니다.'absorber.remove_all_text () '메서드는 로드된 문서에서 모든 텍스트 요소를 제거하여 텍스트가 아닌 구성 요소는 그대로 둡니다.
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

### 특정 페이지에서 모든 텍스트 제거

Aspose.PDF 의 TextFragmentAbsorber 클래스를 사용하여 PDF 문서의 단일 페이지에서 모든 텍스트를 제거합니다.
전체 문서 제거와 달리 이 방법은 페이지 수준의 텍스트 정리를 수행하여 선택한 페이지의 텍스트만 삭제하고 다른 모든 페이지는 그대로 둡니다.

1. PDF 파일을 로드합니다.
1. 텍스트 프래그먼트 업소버 인스턴스를 생성합니다.
1. 첫 페이지에서 모든 텍스트를 제거합니다.
1. 수정한 PDF를 저장합니다.

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

### PDF 페이지의 특정 영역에서 모든 텍스트 제거

Aspose.PDF TextFragmentAbsorber를 사용하여 페이지의 특정 사각형 영역에서 모든 텍스트를 제거합니다.
이 방법은 전체 페이지를 지우는 대신 대상 텍스트 제거를 수행하여 페이지의 어느 부분이 영향을 받는지 정밀하게 제어할 수 있습니다.

1. PDF 문서를 로드합니다.
1. 텍스트 조각 흡수기를 만듭니다.
1. 대상 영역 (직사각형) 을 정의합니다.
1. 지정된 영역에서 텍스트를 제거합니다.
1. 문서의 나머지 부분을 보존하십시오.
1. 수정한 PDF를 저장합니다.

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

### PDF 문서에서 숨겨진 텍스트 모두 제거

Aspose.PDF TextFragmentAbsorber를 사용하여 페이지의 특정 사각형 영역에서 모든 텍스트를 제거합니다.
이 방법은 전체 페이지를 지우는 대신 대상 텍스트 제거를 수행하여 페이지의 어느 부분이 영향을 받는지 정밀하게 제어할 수 있습니다.

1. PDF 문서를 로드합니다.
1. 텍스트 조각 흡수기를 만듭니다.
1. 대상 영역 (직사각형) 을 정의합니다.
1. 지정된 영역에서 텍스트를 제거합니다.
1. 문서의 나머지 부분을 보존하십시오.
1. 수정한 PDF를 저장합니다.

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

- [Python을 사용하여 PDF에서 텍스트 작업하기](/pdf/ko/python-net/working-with-text/)
- [PDF에 텍스트 추가](/pdf/ko/python-net/add-text-to-pdf-file/)
- [파이썬에서 PDF 텍스트 검색 및 추출](/pdf/ko/python-net/search-and-get-text-from-pdf/)
- [파이썬에서 PDF 텍스트 포맷 지정하기](/pdf/ko/python-net/text-formatting-inside-pdf/)
