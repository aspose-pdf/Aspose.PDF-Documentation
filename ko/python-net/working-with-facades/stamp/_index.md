---
title: 스탬프 클래스
type: docs
weight: 150
url: /ko/python-net/stamp-class/
description: Stamp 클래스를 사용하여 Python에서 PDF 문서에 이미지, PDF 및 텍스트 기반 스탬프를 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

.NET을 통한 파이썬용 Aspose.PDF 는 다음을 제공합니다. [스탬프](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) PDF 페이지에 재사용 가능한 시각적 콘텐츠를 배치하기 위한 클래스입니다.스탬프는 텍스트, 이미지 또는 다른 PDF의 페이지를 기반으로 할 수 있으며 위치 지정, 회전, 스타일 지정 및 특정 페이지로 제한할 수 있습니다.

이 문서에서는 몇 가지 일반적인 스탬프 워크플로를 보여줍니다.

1. 텍스트 기반 스탬프를 위한 재사용 가능한 텍스트 리소스를 만드세요.
1. 이미지 및 PDF 페이지 스탬프를 추가합니다.
1. 스타일이 적용된 텍스트 스탬프를 추가합니다.
1. 스탬프를 선택한 페이지로 제한합니다.
1. 배경 이미지 스탬프를 구성합니다.

이 예제에서는 두 개의 도우미 함수를 사용합니다. 하나는 텍스트 기반 스탬프의 서식이 지정된 텍스트를 만들고 다른 하나는 `TextState` 텍스트 스탬프의 스타일을 지정하는 데 사용되는 개체입니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## 이미지 스탬프 추가

용도 `bind_image()` 스탬프에 로고, 배지 또는 아이콘과 같은 이미지를 표시해야 하는 경우이미지를 바인딩한 후 문서에 추가하기 전에 스탬프 ID와 출처를 설정할 수 있습니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## PDF 페이지를 스탬프로 추가

용도 `bind_pdf()` 다른 PDF 파일의 페이지를 스탬프 내용으로 사용하려는 경우이는 승인, 템플릿 또는 별도의 문서에 저장된 미리 작성된 시각적 요소와 같은 오버레이에 유용합니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 텍스트 상태가 포함된 텍스트 스탬프 추가

용도 `bind_logo()` 와 함께 `bind_text_state()` 사용자 지정 글꼴 스타일을 사용하여 텍스트 기반 스탬프를 만들려는 경우이 방법은 승인 표시, 레이블 및 워크플로별 주석에 유용합니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 특정 페이지에 스탬프 추가

스탬프가 모든 페이지에 나타나지 않도록 하려면 대상 페이지 번호를 에 할당하십시오. `pages` 재산.이 예에서는 첫 페이지에만 이미지 스탬프를 추가합니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 배경 이미지 스탬프 추가

이미지가 페이지 콘텐츠 뒤에 표시되어야 하는 경우 배경 스탬프를 사용합니다.스탬프 불투명도, 회전, 품질, 크기 및 위치를 제어하여 워터마크 스타일 효과를 만들 수도 있습니다.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## 관련 파사드 주제

- [파이썬에서 PDF 파사드 작업하기](/pdf/ko/python-net/working-with-facades/)
- [PDF 파일 스탬프로 머리글, 바닥글, 스탬프 추가](/pdf/ko/python-net/pdffilestamp-class/)
- [Python에서 PDF 파일에 페이지 스탬프 추가](/pdf/ko/python-net/add-stamp/)
