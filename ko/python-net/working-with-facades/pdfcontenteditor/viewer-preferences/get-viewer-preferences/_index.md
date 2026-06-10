---
title: PDF 뷰어 기본 설정 가져오기
type: docs
weight: 20
url: /ko/python-net/get-viewer-preferences/
description: Python용 Aspose.PDF 파일을 사용하여 프로그래밍 방식으로 PDF 뷰어 기본 설정을 읽고 수정하는 방법
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 Aspose.PDF 파일을 사용하여 PDF 뷰어 환경 설정 관리
Abstract: 이 안내서는 Python용 Aspose.PDF 를 사용하여 프로그래밍 방식으로 PDF 뷰어 기본 설정을 읽고 수정하는 방법을 보여줍니다.뷰어 기본 설정은 외곽선으로 열기, 도구 모음 숨기기, 단일 페이지 레이아웃 사용 등 PDF 뷰어에서 PDF를 열 때 PDF가 표시되는 방식을 제어합니다.
---

Aspose.PDF 는 PDF 뷰어 기본 설정에 액세스하고 업데이트할 수 있는 도구를 제공합니다.이러한 기본 설정은 PDF 리더에서 PDF 문서의 초기 레이아웃 및 표시 동작을 정의합니다.여기에는 개요 보기 활성화, 메뉴 막대 숨기기 또는 페이지 레이아웃 모드 지정과 같은 옵션이 포함됩니다.PDFContentEditor를 사용하여 기존 환경 설정을 검색하고, 특정 플래그를 확인하고, 필요에 따라 업데이트할 수 있습니다.

1. 뷰어 환경설정 플래그를 정의합니다.
1. 초기화 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 그리고 PDF를 바인딩하세요.
1. 현재 뷰어 환경설정 가져오기.
1. 특정 플래그를 확인하십시오.
1. 현재 환경설정을 표시합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_viewer_preferences(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Read current viewer preference flags
    viewer_preference = ViewerPreference(content_editor.get_viewer_preference())
    if viewer_preference & ViewerPreference.PAGE_MODE_USE_OUTLINES:
        print("PageModeUseOutlines is enabled")
    print(f"Current viewer preference: {viewer_preference}")
```
