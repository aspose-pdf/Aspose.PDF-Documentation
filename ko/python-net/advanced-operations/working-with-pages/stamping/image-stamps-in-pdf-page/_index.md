---
title: Python을 사용한 PDF에 이미지 스탬프 추가
linktitle: PDF 파일의 이미지 스탬프
type: docs
weight: 10
url: /ko/python-net/image-stamps-in-pdf-page/
description: Aspose.PDF for Python 라이브러리의 ImageStamp 클래스를 사용하여 PDF 문서에 이미지 스탬프를 추가합니다.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에 이미지 스탬프를 추가하는 방법
Abstract: 이 문서는 Aspose.PDF for Python 라이브러리를 사용하여 PDF 파일에 이미지 스탬프를 추가하는 포괄적인 가이드를 제공합니다. `ImageStamp` 클래스를 사용하여 높이, 너비, 불투명도, 회전 등 이미지 기반 스탬프의 속성을 커스터마이징하는 방법을 자세히 설명합니다. `Document` 객체와 원하는 속성을 가진 `ImageStamp` 객체를 생성한 뒤, `add_stamp()` 메서드를 이용해 특정 페이지에 스탬프를 추가하는 과정을 다룹니다. 또한, `quality` 속성을 사용하여 이미지 품질을 퍼센트 단위로 조정하는 Python 코드 예제가 포함되어 있습니다. 추가로 `FloatingBox` 클래스를 활용해 이미지 스탬프를 배경으로 사용하는 방법과 구현 예제도 제공됩니다. 이 가이드는 Aspose.PDF를 이용해 이미지 스탬프로 PDF를 향상시키고자 하는 개발자에게 유용한 자료가 됩니다.
---

## PDF 파일에 이미지 스탬프 추가

PDF 파일에 이미지 스탬프를 추가하려면 [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스를 사용할 수 있습니다. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스는 높이, 너비, 불투명도 등 이미지 기반 스탬프를 만들기 위한 필요한 속성을 제공합니다. 스탬프는 위치를 지정하고, 크기를 조정하고, 회전시키며 부분 투명하게 만들 수 있어 워터마크, 브랜딩 또는 주석으로 활용할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 이미지 스탬프를 추가하는 방법을 보여줍니다.

1. 'ap.Document()'를 사용하여 PDF를 로드합니다.
1. 'ImageStamp()'로 이미지 스탬프를 생성합니다.
1. 스탬프 속성을 설정합니다.
1. 스탬프를 대상 페이지에 추가합니다.
1. 수정된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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

이미지를 스탬프 객체로 추가할 때 이미지 품질을 제어할 수 있습니다. [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) 클래스의 [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) 속성이 이를 위해 사용됩니다. 이 속성은 이미지 품질을 퍼센트(0~100)로 나타냅니다.
quality 속성을 설정함으로써 이미지 해상도를 낮춰 PDF 크기를 최적화하거나, 높은 선명도를 유지할 수 있습니다.

1. PDF 문서를 엽니다.
1. 이미지 스탬프를 생성합니다.
1. 이미지 품질을 설정합니다.
1. 스탬프를 대상 페이지에 추가합니다.
1. 수정된 PDF를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_stamp_image_control_image_quality(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## 플로팅 박스 배경으로 이미지 스탬프 사용

[FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/)를 PDF에 생성하고 이미지를 배경으로 적용합니다. 또한 텍스트를 추가하고, 테두리와 배경 색을 설정하며, 박스를 페이지에 정확히 배치하는 방법을 보여줍니다. 이는 이미지 위에 텍스트가 있는 콜아웃, 배너, 강조 섹션 등 시각적으로 풍부한 PDF 콘텐츠를 만들 때 유용합니다.

1. PDF 문서를 열거나 새로 만듭니다.
1. 'FloatingBox' 객체를 생성합니다.
1. 박스에 텍스트 콘텐츠를 추가합니다.
1. 박스 테두리와 배경 색을 설정합니다.
1. 배경 이미지를 추가합니다.
1. 페이지에 FloatingBox를 추가합니다.
1. PDF 문서를 저장합니다.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):

    document = ap.Document(infile)
    # Add page to PDF document
    page = document.pages.add()
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


