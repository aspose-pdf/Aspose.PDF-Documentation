---
title: Python에서 PDF에 이미지 스탬프 추가
linktitle: PDF 파일의 이미지 스탬프
type: docs
weight: 10
url: /ko/python-net/image-stamps-in-pdf-page/
description: Python에서 PDF 페이지에 이미지 스탬프를 추가하는 방법을 알아보세요.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 이미지 스탬프를 추가하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 라이브러리를 사용하여 PDF 파일에 이미지 스탬프를 추가하는 방법에 대한 포괄적인 가이드를 제공합니다.높이, 너비, 불투명도 및 회전과 같은 속성을 포함하여 이미지 기반 스탬프를 사용자 지정할 수 있는 `ImageStamp` 클래스의 사용에 대해 자세히 설명합니다.이 프로세스에는 원하는 속성을 가진 `Document` 객체와 `ImageStamp` 객체를 만든 다음 `add_stamp () `메서드를 사용하여 PDF의 특정 페이지에 스탬프를 추가하는 작업이 포함됩니다.이 문서에는 PDF에 이미지 스탬프를 적용하고 이미지 품질을 백분율로 조정하는 `quality` 속성을 사용하여 품질을 제어하는 방법을 보여주는 Python 코드 스니펫이 포함되어 있습니다.또한 이 문서에서는 `FloatingBox` 클래스를 사용하여 플로팅 박스에서 이미지 스탬프를 배경으로 사용하는 방법을 설명하고, 이를 구현하는 방법을 보여주는 또 다른 코드 예제를 제공합니다.이 안내서는 Aspose.PDF 를 사용하여 이미지 스탬프로 PDF를 개선하려는 개발자에게 유용한 리소스가 됩니다.
---

## PDF 파일에 이미지 스탬프 추가

사용할 수 있습니다 [이미지 스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) PDF 파일에 이미지 스탬프를 추가하는 클래스입니다. [이미지 스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스는 높이, 너비, 불투명도 등과 같은 이미지 기반 스탬프를 만드는 데 필요한 속성을 제공합니다.스탬프를 배치하고, 크기를 조정하고, 회전하고, 부분적으로 투명하게 만들어 워터마크, 브랜딩 또는 주석을 추가할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 이미지 스탬프를 추가하는 방법을 보여줍니다.

1. 'AP.Document () '를 사용하여 PDF를 로드합니다.
1. '이미지스탬프 () '로 이미지 스탬프를 만드세요.
1. 스탬프 속성을 구성합니다.
1. 대상 페이지에 스탬프를 추가합니다.
1. 수정한 PDF를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## 스탬프 추가 시 이미지 품질 제어

이미지를 스탬프 오브젝트로 추가할 때 이미지 품질을 제어할 수 있습니다. [품질](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) 의 재산 [이미지 스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스는 이러한 목적으로 사용됩니다.이미지의 품질을 백분율로 나타냅니다 (유효한 값은 0.. 100).
품질 속성을 설정하면 이미지 해상도를 줄여 PDF 크기를 최적화하거나 선명도를 위해 더 높은 충실도를 유지할 수 있습니다.

1. PDF 문서를 엽니다.
1. 이미지 스탬프 만들기
1. 이미지 품질을 설정합니다.
1. 대상 페이지에 스탬프를 추가합니다.
1. 수정한 PDF를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## 플로팅 박스의 배경으로 이미지 스탬프

만들기 [플로팅 박스](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) PDF에서 이미지를 배경으로 적용합니다.또한 텍스트를 추가하고, 테두리, 배경색을 설정하고, 페이지에 상자를 정확하게 배치하는 방법도 보여줍니다.이는 콜아웃, 배너 또는 이미지 위에 텍스트가 있는 강조 표시된 섹션 등 시각적으로 풍부한 PDF 콘텐츠를 만드는 데 유용합니다.

1. PDF 문서를 열거나 생성합니다.
1. '플로팅박스' 객체를 생성합니다.
1. 상자에 텍스트 내용을 추가합니다.
1. 상자 테두리와 배경색을 설정합니다.
1. 배경 이미지를 추가합니다.
1. 페이지에 플로팅 박스를 추가합니다.
1. PDF 문서를 저장합니다.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```

## 관련 스탬핑 주제

- [파이썬으로 PDF 페이지에 스탬프 찍기](/pdf/ko/python-net/stamping/)
- [Python에서 PDF에 페이지 스탬프 추가](/pdf/ko/python-net/page-stamps-in-the-pdf-file/)
- [Python에서 PDF에 텍스트 스탬프 추가](/pdf/ko/python-net/text-stamps-in-the-pdf-file/)
- [파이썬에서 PDF에 페이지 번호 추가](/pdf/ko/python-net/add-page-number/)