---
title: 파이썬에서 HTML을 PDF로 변환
linktitle: HTML을 PDF 파일로 변환
type: docs
weight: 40
url: /ko/python-net/convert-html-to-pdf/
lastmod: "2026-06-10"
description: .NET을 통해 파이썬용 Aspose.PDF 를 사용하여 파이썬에서 HTML과 MHTML을 PDF로 변환하는 방법을 알아보세요. 여기에는 CSS 미디어 설정, 포함된 글꼴, 태그가 지정된 PDF 출력 등이 포함됩니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Aspose.PDF 파일을 사용하여 파이썬에서 HTML을 PDF로 변환하는 방법
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 HTML 및 MHTML 파일을 PDF로 변환하는 방법을 설명합니다.기본 HTML-PDF 워크플로를 다루며 미디어 유형, CSS 페이지 규칙 우선 순위, 포함된 글꼴, 단일 페이지 출력, 액세스 가능한 태그가 지정된 PDF의 논리적 구조 생성을 사용하여 렌더링을 제어하는 방법을 보여줍니다.
---

## 파이썬 HTML을 PDF로 변환

**.NET을 통한 파이썬용 Aspose.pdf**를 사용하면 유연한 렌더링 옵션을 사용하여 기존 HTML 문서를 PDF로 변환할 수 있습니다.레이아웃, 스타일, 접근성 및 보관 요구 사항에 맞게 출력이 생성되는 방식을 미세 조정할 수 있습니다.

## HTML을 PDF로 변환

다음 Python 예제는 HTML 문서를 PDF로 변환하는 기본 워크플로를 보여줍니다.

1. 의 인스턴스 생성 [HTML 로드 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 수업.
1. a 초기화 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 소스 HTML 파일이 있는 객체입니다.
1. 호출하여 출력 PDF 문서 저장 `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## 관련 전환

- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 기존 PDF 파일을 웹에서 바로 출력해야 하는 경우
- [다른 파일 형식을 PDF로 변환](/pdf/ko/python-net/convert-other-files-to-pdf/) EPUB, XPS, 텍스트 및 포스트스크립트 변환 워크플로우에 적합합니다.
- [이미지를 PDF로 변환](/pdf/ko/python-net/convert-images-format-to-pdf/) 소스 콘텐츠가 HTML 마크업이 아닌 이미지 기반인 경우

{{% alert color="success" %}}
**온라인에서 HTML을 PDF로 변환해 보세요**

Aspose는 온라인 신청서를 제공합니다 [“HTML을 PDF로”](https://products.aspose.app/html/en/conversion/html-to-pdf)여기서 변환 품질 및 출력을 테스트할 수 있습니다.

[![Aspose.PDF 앱을 사용하여 HTML을 PDF로 변환](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## 미디어 유형을 사용하여 HTML을 PDF로 변환

이 예제에서는 특정 렌더링 옵션을 사용하여 HTML 파일을 PDF로 변환하는 방법을 보여줍니다.

1. 의 인스턴스 생성 [HTML 로드 옵션 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 수업.
1. 세트 `html_media_type` 화면 또는 인쇄 레이아웃용 CSS 규칙 적용 (예: `HtmlMediaType.SCREEN` 또는 `HtmlMediaType.PRINT`.
1. HTML을 에 로드합니다. `ap.Document` 로드 옵션 사용
1. 문서를 PDF로 저장합니다.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## CSS의 우선 순위 지정하기 `@page` HTML을 PDF로 변환하는 동안의 규칙

일부 문서 사용 [그 `@page` 규칙](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) 페이지 레이아웃용.이러한 스타일이 다른 설정과 충돌하는 경우 다음을 사용하여 우선 순위를 제어할 수 있습니다. `is_priority_css_page_rule`.

1. 의 인스턴스 생성 [HTML 로드 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) 수업.
1. 세트 `is_priority_css_page_rule = False` 다른 스타일이 우선하도록 `@page` 규칙.
1. HTML을 에 로드합니다. `ap.Document` 구성된 옵션과 함께.
1. 문서를 PDF로 저장합니다.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## 글꼴이 포함된 HTML을 PDF로 변환

이 예제에서는 글꼴을 포함하는 동안 HTML 파일을 PDF로 변환하는 방법을 보여줍니다.원본 타이포그래피를 보존하기 위해 출력 PDF가 필요한 경우 다음을 설정하십시오. `is_embed_fonts` 에 `True`.

1. 작성 `HtmlLoadOptions()` HTML에서 PDF로의 변환을 구성합니다.
1. 세트 `is_embed_fonts = True` HTML에 사용된 글꼴을 PDF에 직접 포함시킬 수 있습니다.
1. HTML을 에 로드합니다. `ap.Document` 다음과 같은 옵션이 있습니다.
1. 문서를 PDF로 저장합니다.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## 단일 PDF 페이지에 HTML 콘텐츠 렌더링

이 예제는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 HTML 파일을 단일 페이지 PDF로 변환하는 방법을 보여줍니다.다음을 사용하십시오. `is_render_to_single_page` 전체 HTML 콘텐츠를 하나의 연속 페이지에 렌더링하려는 경우의 속성입니다.

1. 의 인스턴스 생성 `HtmlLoadOptions()` 변환 프로세스를 구성합니다.
1. 활성화 `is_render_to_single_page` 전체 HTML 콘텐츠를 한 페이지에 렌더링합니다.
1. 구성된 옵션이 있는 문서를 에 로드합니다. `ap.Document`.
1. 결과를 PDF 파일로 저장합니다.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## HTML 태그에서 논리적 구조 만들기

태그가 있는 PDF라고도 하는 논리적 구조는 제목, 단락 및 목록과 같은 원본 HTML의 의미론적 계층 구조를 유지합니다.따라서 결과 PDF를 보다 쉽게 액세스하고 검색할 수 있으며 구조화된 문서 워크플로우에 적합합니다.

변환 중에 논리적 구조를 활성화하면 HTML DOM이 시각적 콘텐츠로만 렌더링되지 않고 PDF 태그 트리에 매핑됩니다.

접근성 요구 사항을 충족하려면 PDF에 읽기 순서를 정의하고, 화면 판독기에 대체 텍스트를 제공하고, 내용의 계층 구조를 유지하는 논리적 구조 요소가 포함되어야 합니다.

> 출력 PDF의 논리적 구조 품질은 원본 HTML 마크업의 품질에 직접적으로 좌우됩니다.HTML의 구조가 잘못되거나 유효하지 않으면 변환된 PDF의 태그가 불완전하거나 부정확할 수 있습니다.

1. HTMLLoadOptions 인스턴스를 생성하여 HTML이 변환되는 방식을 제어합니다.
1. PDF에 구조화된 요소가 포함되도록 시맨틱 태깅을 활성화합니다.
1. 구성된 옵션을 사용하여 HTML 파일을 엽니다.
1. 구조화된 PDF를 저장합니다.

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## MHTML을 PDF로 변환

이 예제에서는 Python용 Aspose.PDF 파일을 사용하여 특정 페이지 크기의 .NET을 통해 MHT 또는 MHTML 파일을 PDF 문서로 변환하는 방법을 보여줍니다.

1. 의 인스턴스 생성 `ap.MhtLoadOptions()` MHTML 파일 처리를 구성합니다.
1. 페이지 크기와 같은 다양한 매개 변수를 설정합니다.
1. 입력 파일과 구성된 로드 옵션을 사용하여 문서를 초기화합니다.
1. 결과 문서를 PDF로 저장합니다.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
