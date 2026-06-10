---
title: 파이썬에서 PDF를 HTML로 변환
linktitle: PDF를 HTML 형식으로 변환
type: docs
weight: 50
url: /ko/python-net/convert-pdf-to-html/
lastmod: "2026-06-10"
description: 다중 페이지 출력, 외부 이미지, SVG 처리 및 계층화된 HTML 렌더링을 포함하여.NET을 통해 파이썬에서 PDF를 HTML로 변환하는 방법을 알아봅니다. Aspose.PDF
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 파이썬에서 PDF를 HTML로 변환하는 방법
Abstract: 이 문서에서는 파이썬을 사용하여 PDF 파일을 HTML로 변환하는 방법에 대한 포괄적인 가이드를 제공합니다. 특히.NET 라이브러리를 통한 파이썬용 Aspose.PDF 라이브러리를 통해 말이죠.이 문서에서는 소스 PDF에서 '문서' 객체를 만드는 방법을 강조하고 문서를 HTML 형식으로 저장하기 위한 'HTMLSaveOptions'를 활용하여 프로그래밍 방식으로 이러한 변환을 수행하는 데 필요한 단계를 간략하게 설명합니다.이 문서에는 변환 과정을 보여주는 간결한 Python 코드 스니펫이 포함되어 있습니다.또한 사용자가 변환의 기능과 품질을 탐색할 수 있도록 하는 온라인 도구인 Aspose.PDF “PDF to HTML” 애플리케이션을 소개합니다.이 문서는 다양한 관련 주제를 다루도록 구성되어 있으므로 PDF에서 HTML로의 변환에 Python을 사용하는 방법을 철저히 이해할 수 있습니다.
---

## PDF를 HTML로 변환

**.NET을 통한 파이썬용 Aspose.pdf**는 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하기 위한 많은 기능을 제공합니다.이 문서에서는 PDF 파일을 다음과 같이 변환하는 방법에 대해 설명합니다. <abbr title="HyperText Markup Language">HTML</abbr>.Python 코드 몇 줄만 사용하여 PDF를 HTML로 변환할 수 있습니다.웹 사이트를 만들거나 온라인 포럼에 콘텐츠를 추가하려면 PDF를 HTML로 변환해야 할 수 있습니다.PDF를 HTML로 변환하는 한 가지 방법은 프로그래밍 방식으로 Python을 사용하는 것입니다.

{{% alert color="success" %}}
**온라인에서 PDF를 HTML로 변환해 보세요**

파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 HTML로”](https://products.aspose.app/pdf/conversion/pdf-to-html)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 앱을 사용하여 PDF를 HTML로 변환](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

단계: 파이썬에서 PDF를 HTML로 변환

1. 의 인스턴스 생성 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 원본 PDF 문서가 있는 개체입니다.
1. 에 저장 [HTML 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) 전화해서 [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## 관련 전환

- [HTML을 PDF로 변환](/pdf/ko/python-net/convert-html-to-pdf/) 웹-투-문서 워크플로우가 필요할 때
- [PDF를 워드로 변환](/pdf/ko/python-net/convert-pdf-to-word/) 편집 가능한 문서 출력이 HTML보다 더 유용한 경우
- [PDF를 이미지 형식으로 변환](/pdf/ko/python-net/convert-pdf-to-images-format/) 래스터 익스포트 시나리오용

### 지정된 폴더에 이미지를 저장하여 PDF를 HTML로 변환

이 함수는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 PDF 파일을 HTML 형식으로 변환합니다.추출된 모든 이미지는 HTML 파일에 포함되지 않고 지정된 폴더에 저장됩니다.

1. HTML 저장 옵션을 구성합니다.
1. 외부 이미지와 함께 HTML로 저장합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_images(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "images")
    save_options.special_folder_for_all_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF를 여러 페이지 HTML로 변환

이 함수는 PDF 파일을 여러 페이지 HTML로 변환하며, 여기서 각 PDF 페이지는 별도의 HTML 파일로 내보냅니다.이렇게 하면 출력을 더 쉽게 탐색할 수 있고 큰 PDF의 로드 시간이 단축됩니다.

1. 'AP.Document'를 사용하여 소스 PDF를 로드합니다.
1. 'HTML 저장 옵션'을 생성하고 'split_into_pages'를 설정합니다.
1. 페이지를 별도의 파일로 분할한 문서를 HTML로 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_multi_page(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 지정된 폴더에 SVG 이미지를 저장하여 PDF를 HTML로 변환

이 함수는 모든 이미지를 HTML에 직접 포함하는 대신 지정된 폴더에 SVG 파일로 저장하면서 PDF를 HTML 형식으로 변환합니다.

1. 'AP.Document'를 사용하여 소스 PDF를 로드합니다.
1. 'HTMLSaveOptions'를 생성하고 대상 폴더에 '특수_폴더_for_svg_images'를 설정합니다.
1. 문서를 외부 SVG 이미지와 함께 HTML로 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF를 HTML로 변환하고 압축된 SVG 이미지 저장하기

이 스니펫은 PDF를 HTML 형식으로 변환하여 모든 이미지를 지정된 폴더에 SVG 파일로 저장하고 압축하여 파일 크기를 줄입니다.

1. 'AP.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HTML 저장 옵션'을 생성하고:
   - SVG 이미지를 외부에 저장하려면 'Special_folder_for_svg_images'를 설정하십시오.
   - SVG 이미지를 압축하려면 'compress_svg_graphics_if_any'를 활성화하십시오.
1. 문서를 압축된 외부 SVG 이미지와 함께 HTML로 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_compress_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    save_options.compress_svg_graphics_if_any = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 임베디드 래스터 이미지를 제어하여 PDF를 HTML로 변환

이 스니펫은 PDF를 HTML 형식으로 변환하여 래스터 이미지를 PNG 페이지 배경으로 포함합니다.이 방법을 사용하면 HTML 내의 이미지 품질과 페이지 레이아웃이 보존됩니다.

1. 'AP.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HTMLSaveOptions'를 생성하고 '래스터_이미지_저장_모드를 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'로 설정합니다.
1. 문서를 래스터 이미지가 포함된 HTML로 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_PNG_background(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### PDF를 본문 전용 콘텐츠 HTML 페이지로 변환

이 함수는 PDF를 HTML 형식으로 변환하여 추가 'html' 또는 'head' 태그 없이 '본문 전용' 내용을 생성하고 출력을 별도의 페이지로 분할합니다.

1. 'AP.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HTML 저장 옵션'을 생성하고 다음을 구성합니다.
   - 'html_마크업_생성_모드 = WRITE_ONLY_BODY_CONTENT'를 선택하면 '본문' 콘텐츠만 생성됩니다.
   - 'spit_into_pages'를 선택하면 각 PDF 페이지에 대해 별도의 HTML 파일을 만들 수 있습니다.
1. 지정한 옵션을 사용하여 문서를 HTML로 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_body_content(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.html_markup_generation_mode = (
        ap.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    )
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 투명 텍스트 렌더링을 사용하여 PDF를 HTML로 변환

이 함수는 PDF를 HTML 형식으로 변환하여 그림자가 있는 텍스트를 포함한 모든 텍스트를 투명하게 렌더링합니다. 이렇게 하면 출력 HTML에서 유연한 스타일 지정을 허용하면서 시각적 정확도가 유지됩니다.

1. 'AP.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HTML 저장 옵션'을 생성하고 다음을 구성합니다.
    - 'save_transparent t_texts'를 사용하여 일반 텍스트를 투명하게 렌더링합니다.
    - 'save_shadowed_texts_as_transparent t_texts'를 사용하여 그림자가 있는 텍스트를 투명하게 렌더링합니다.
1. 투명 텍스트 렌더링을 사용하여 문서를 HTML로 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_transparent_text_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### 문서 레이어 렌더링을 사용하여 PDF를 HTML로 변환

이 함수는 표시된 내용을 출력 HTML의 개별 레이어로 변환하여 문서 레이어를 보존하면서 PDF를 HTML 형식으로 변환합니다.이를 통해 주석, 배경 및 오버레이와 같은 레이어 요소를 정확하게 렌더링할 수 있습니다.

1. 'AP.Document'를 사용하여 PDF 문서를 로드합니다.
1. 'HTMLSaveOptions'를 생성하고 'Convert_marked_content_to_layers'를 활성화하여 레이어를 보존합니다.
1. 문서를 레이어 내용이 포함된 HTML로 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_document_layers_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

