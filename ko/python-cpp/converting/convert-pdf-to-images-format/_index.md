---
title: 파이썬에서 PDF를 다양한 이미지 형식으로 변환하기
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /ko/python-cpp/convert-pdf-to-images-format/
lastmod: "2023-06-23"
description: 이 주제는 Aspose.PDF for Python을 사용하여 PDF를 TIFF, BMP, EMF, JPEG, PNG, GIF, SVG 등 다양한 이미지 형식으로 몇 줄의 코드로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 개요

이 글은 파이썬을 사용하여 PDF를 다양한 이미지 형식으로 변환하는 방법을 설명합니다. 다음 주제를 다룹니다.

## 파이썬에서 PDF를 이미지로 변환하기

### 파이썬에서 PDF를 PNG로 변환하기

1. Aspose.PDF 라이브러리에 대한 파이썬 래퍼를 제공하는 AsposePdfPython 모듈을 가져옵니다.
1. 파일 이름을 인수로 받아 Document 객체를 반환하는 `document_open` 함수를 사용하여 PDF 문서를 엽니다.
1. Document 객체를 인수로 받아 PageCollection 객체를 반환하는 `document_get_pages` 함수를 사용하여 문서의 페이지를 가져옵니다.

1. `page_collection_get_page` 함수를 사용하여 문서의 원하는 페이지를 가져옵니다. 이 함수는 PageCollection 객체와 인덱스를 인수로 받아 Page 객체를 반환합니다.
1. 인수가 없는 `png_device_create` 함수를 사용하여 PngDevice 객체를 생성합니다. 이 객체는 기본 매개변수로 PDF 페이지를 PNG 이미지로 변환할 수 있습니다.
1. `png_device_save_page_to_file` 함수를 사용하여 문서의 원하는 페이지를 PNG 이미지로 저장합니다. 이 함수는 PngDevice 객체, Page 객체 및 파일 이름을 인수로 받습니다.
1. 객체를 인수로 받아 그 리소스를 해제하는 `close_handle` 함수를 사용하여 PngDevice 및 Document 객체의 핸들을 닫습니다.

```python

from AsposePdfPython import *

doc = document_open("blank_pdf_document.pdf")
pages = document_get_pages(doc)
page = page_collection_get_page(pages,1)

pngDevice = png_device_create()
png_device_save_page_to_file(pngDevice,page,"test.png")

```

### Python PDF를 JPEG로 변환하기

1. `document_open` 함수를 사용하여 PDF 문서를 열고, 파일 이름을 인수로 받아 Document 객체를 반환합니다.
1. `document_get_pages` 함수를 사용하여 문서의 페이지를 가져오고, Document 객체를 인수로 받아 PageCollection 객체를 반환합니다.
1. `page_collection_get_page` 함수를 사용하여 문서의 원하는 페이지를 가져오고, PageCollection 객체와 인덱스를 인수로 받아 Page 객체를 반환합니다.
1. `resolution_create` 함수를 사용하여 Resolution 객체를 생성하고, 인치당 점(DPI) 단위의 해상도 값을 인수로 받습니다.
1. `jpeg_device_create_from_width_height_resolution` 함수를 사용하여 JpegDevice 객체를 생성하고, 너비, 높이 및 해상도 값을 인수로 받습니다. 이 객체는 지정된 매개변수로 PDF 페이지를 JPEG 이미지로 변환할 수 있습니다.

1. `jpeg_device_save_page_to_file` 함수를 사용하여 문서의 원하는 페이지를 JPEG 이미지로 저장합니다. 이 함수는 JpegDevice 객체, Page 객체, 파일 이름을 인수로 받습니다.
2. `close_handle` 함수를 사용하여 JpegDevice 및 Document 객체의 핸들을 닫습니다. 이 함수는 객체를 인수로 받아서 자원을 해제합니다.

```python

    from AsposePdfPython import *

    doc = document_open("blank_pdf_document.pdf")
    pages = document_get_pages(doc)
    page = page_collection_get_page(pages,1)

    res = resolution_create(300)
    jpegDevice = jpeg_device_create_from_width_height_resolution(1239,1754,res)
    jpeg_device_save_page_to_file(jpegDevice,page,"test.jpeg")
```