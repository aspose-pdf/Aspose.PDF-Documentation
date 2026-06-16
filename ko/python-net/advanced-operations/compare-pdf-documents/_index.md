---
title: 파이썬에서 PDF 문서 비교하기
linktitle: PDF를 비교하세요
type: docs
weight: 130
url: /ko/python-net/compare-pdf-documents/
description: .NET을 통한 Python용 Aspose.PDF 출력과 병렬 및 그래픽 차이 출력을 사용하여 Python에서 PDF 문서를 비교하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 시각적 차이 출력으로 PDF 페이지와 전체 문서 비교
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF PDF 문서를 비교하는 방법을 설명합니다.특정 페이지 또는 전체 PDF 파일을 나란히 출력하여 비교하는 방법과 그래픽 비교 방법을 사용하여 이미지 기반 또는 PDF 기반 차이 보고서를 생성하는 방법을 알아봅니다.
---

## PDF 문서 비교 방법

PDF 문서로 작업할 때 차이점을 식별하기 위해 두 문서의 내용을 비교해야 하는 경우가 있습니다..NET 라이브러리를 통한 파이썬용 Aspose.PDF 라이브러리는 이러한 목적을 위한 강력한 도구 세트를 제공합니다.이 기사에서는 몇 가지 간단한 코드 스니펫을 사용하여 PDF 문서를 비교하는 방법을 살펴보겠습니다.

페이지 전반의 텍스트 및 레이아웃 변경 사항을 강조 표시하는 PDF 출력을 원하는 경우 병렬 비교를 사용하십시오.시각적 검토 워크플로, 회귀 검사 또는 PDF 비교 보고서를 위한 이미지 기반 차이 탐지가 필요한 경우 그래픽 비교를 사용하십시오.

Aspose.PDF 의 비교 기능을 사용하면 두 PDF 문서를 페이지별로 비교할 수 있습니다.특정 페이지 또는 전체 문서를 비교하도록 선택할 수 있습니다.결과 비교 문서는 차이점을 강조 표시하므로 두 파일 간의 변경 사항을 쉽게 식별할 수 있습니다.

다음은.NET 라이브러리를 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 문서를 비교할 수 있는 방법의 목록입니다.

1. **특정 페이지 비교** - 두 PDF 문서의 첫 페이지를 비교합니다.
1. **전체 문서 비교** - 두 PDF 문서의 전체 내용을 비교합니다.
1. **PDF 문서를 그래픽으로 비교하세요**:

- 변경 사항이 표시된 개별 이미지인 'comparer.get_difference' 방법을 사용하여 PDF를 비교합니다.
- PDF를 'comparer.compare_documents_to_pdf' 메서드 (변경 사항이 표시된 이미지가 있는 PDF 문서) 와 비교하십시오.

## 특정 페이지 비교

첫 번째 코드 스니펫은 SideBisepdfComparer 클래스를 사용하여 두 PDF 문서의 첫 페이지를 비교하는 방법을 보여줍니다.

1. 문서 초기화.
1. 비교를 수행할 함수를 생성합니다.
1. 비교 프로세스:

- 문서1.페이지 [1] 및 문서2.pages [1]: - 비교를 위해 각 문서의 첫 페이지를 지정합니다.참고로 Aspose.PDF 에서는 페이지 인덱싱이 1부터 시작됩니다.
- 병행 비교 옵션 - 이 클래스를 사용하면 비교 동작을 사용자 지정할 수 있습니다.
- additional_change_marks = True - 현재 비교 중인 페이지에 없더라도 다른 페이지에 있을 수 있는 차이점을 강조하여 추가 변경 마커를 표시할 수 있습니다.
- compaison_mode = ComparisonMode.ignoreSpaces - 단어 내의 변경 사항에만 초점을 맞춰 텍스트의 공백을 무시하도록 비교 모드를 설정합니다.

1. 비교 결과는 지정된 data_dir에 ComparingSpecificPages_out.pdf 라는 새 PDF 파일로 저장됩니다.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## 전체 문서 비교

두 번째 코드 스니펫은 범위를 확장하여 두 PDF 문서의 전체 내용을 비교합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

제공된 코드는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 두 PDF 문서를 비교하는 방법을 보여줍니다.SideBisePDFComparer 클래스를 사용하여 페이지별 비교를 수행하여 차이점을 나란히 표시하는 새 PDF를 생성합니다.비교는 SidebySideComparisonOptions를 사용하여 구성됩니다. 여기서 additional_change_marks는 True로 설정되어 현재 페이지뿐만 아니라 다른 페이지의 변경 사항도 강조 표시하고, compaison_mode는 공백 변화를 무시하여 의미 있는 콘텐츠 차이에 초점을 맞추기 위해 IgnoreSpace로 설정됩니다.

## 그래픽 PDF 비교기를 사용하여 비교

특히 전문적인 환경에서 문서 공동 작업을 할 때 동일한 파일의 여러 버전이 생성되는 경우가 많습니다.
제공된 코드는.NET을 통해 Python용 Aspose.PDF 를 사용하여 두 PDF 문서의 특정 페이지를 시각적으로 비교하는 방법을 보여줍니다.를 사용하여 `GraphicalPdfComparer` 클래스에서는 두 PDF의 첫 페이지 간의 차이점을 강조 표시하고 해당 이미지를 생성하여 이러한 차이점을 나타냅니다.

다음과 같은 클래스 속성을 설정할 수 있습니다.

- 해상도 - 출력 이미지 및 비교 중에 생성된 이미지의 해상도 (DPI 단위).
- 색상 - 변경 마크의 색상입니다.
- 임계값 - 임계값을 백분율로 변경합니다.기본값은 0입니다.0이 아닌 다른 값을 설정하면 중요하지 않은 그래픽 변경을 무시할 수 있습니다.

.NET을 통한 Python용 Aspose.PDF 를 사용하면 문서와 페이지를 비교하고 비교 결과를 PDF 문서 또는 이미지 파일로 출력할 수 있습니다.

더 `GraphicalPdfComparer` class에는 추가 처리에 적합한 형식으로 페이지 이미지 차이를 가져올 수 있는 메서드가 있습니다. `get_difference(document1.pages[1], document2.pages[1])`.

이 메서드는 의 객체를 반환합니다. `images_difference` 유형: 비교 중인 첫 페이지의 이미지와 차이점 배열을 포함합니다.

더 `images_difference` object를 사용하면 원본 이미지에 차이 배열을 적용하여 다른 이미지를 생성하고 비교 중인 두 번째 페이지의 이미지를 가져올 수 있습니다.이 작업을 수행하려면 다음을 사용하십시오. `difference_to_image` 과 `get_destination_image` 방법.

### 차이 가져오기 방법을 사용하여 PDF 비교

제공된 코드는 메서드를 정의합니다. `get_difference` 두 PDF 문서를 비교하고 두 문서 간의 차이점을 시각적으로 표현합니다.

이 메서드는 두 PDF 파일의 첫 페이지를 비교하여 두 개의 PNG 이미지를 생성합니다.

- 한 이미지는 페이지 간의 차이점을 빨간색으로 강조 표시합니다.
- 다른 이미지는 대상 (두 번째) PDF 페이지를 시각적으로 표현한 것입니다.

이 프로세스는 두 문서 버전 간의 변경 사항이나 차이점을 시각적으로 비교하는 데 유용할 수 있습니다.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### 문서와 PDF 비교 방법을 사용하여 PDF 비교

제공된 코드 스니펫은 다음을 사용합니다. `compare_documents_to_pdf` 메서드는 두 문서를 비교하고 비교 결과에 대한 PDF 보고서를 생성합니다.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

이 예제는.NET을 통해 Python용 Aspose.PDF 를 사용하여 두 전체 PDF 문서를 그래픽으로 비교하는 방법을 보여줍니다.를 활용하여 `GraphicalPdfComparer` 클래스를 생성하면 문서 간의 차이점을 시각적으로 강조하는 새 PDF 파일이 생성됩니다.

- 임계값 속성은 3.0으로 설정되어 있습니다. 즉, 이 백분율 미만의 사소한 차이는 비교 중에 무시되고 더 중요한 변경 사항에 초점을 맞춥니다.
- 색상 속성을 ap.Color.blue로 설정하여 차이점을 파란색으로 표시하므로 시각적으로 명확하게 구분할 수 있습니다.
- 해상도 속성을 설정하여 300DPI의 해상도에서 비교를 수행하여 상세하고 명확한 출력을 보장합니다.

더 `compare_documents_to_pdf` 메서드는 두 문서의 모든 페이지를 비교하여 차이점을 시각적으로 강조 표시한 새 PDF 파일인 compareDocumentsToPdf_out.pdf 에 결과를 출력합니다.

## 관련 주제

- [파이썬에서의 고급 PDF 작업](/pdf/ko/python-net/advanced-operations/)
- [파이썬에서 PDF 문서로 작업하기](/pdf/ko/python-net/working-with-documents/)
- [파이썬에서 PDF 페이지 작업하기](/pdf/ko/python-net/working-with-pages/)
- [파이썬에서 PDF 텍스트로 작업하기](/pdf/ko/python-net/working-with-text/)
