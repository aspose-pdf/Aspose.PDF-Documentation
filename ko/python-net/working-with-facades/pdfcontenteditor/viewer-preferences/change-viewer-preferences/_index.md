---
title: PDF 뷰어 기본 설정 변경
linktitle: PDF 뷰어 기본 설정 변경
type: docs
weight: 10
url: /ko/python-net/change-viewer-preferences/
description: 이 모듈은 Python용 Aspose.PDF 를 사용하여 PDF 문서의 뷰어 설정을 조정하는 방법을 보여줍니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF 뷰어 경험을 사용자 정의하세요
Abstract: 뷰어 기본 설정을 프로그래밍 방식으로 수정하여 PDF 문서를 열 때 표시되는 방식을 제어할 수 있습니다.이 기능을 사용하면 사용자 인터페이스와 레이아웃을 조정하여 일관된 보기 환경을 보장할 수 있습니다.
---

PDF 파일에는 페이지 레이아웃, 도구 모음 가시성 및 창 동작과 같은 측면을 제어하는 내장 뷰어 기본 설정이 있습니다.이 스크립트를 사용하여 다음을 수행할 수 있습니다.

- PDF의 현재 뷰어 기본 설정을 검사합니다.
- 레이아웃 옵션을 수정합니다 (예: 단일 페이지, 1열, 2열).
- 도구 모음, 메뉴 막대 또는 제목 표시와 같은 UI 요소를 전환합니다.
- 제어된 보기 환경을 위해 업데이트된 기본 설정을 사용하여 PDF를 저장합니다.

1. 뷰어 환경설정 플래그를 정의합니다.
1. 현재 뷰어 환경설정 가져오기.
1. 기본 설정 수정.
1. 업데이트된 기본 설정 적용.
1. PDF를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import sys
from enum import IntFlag
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Define ViewerPreference flags
class ViewerPreference(IntFlag):
    HIDE_TOOLBAR = 1
    HIDE_MENUBAR = 2
    HIDE_WINDOW_UI = 4
    FIT_WINDOW = 8
    CENTER_WINDOW = 16
    DISPLAY_DOC_TITLE = 32
    NON_FULL_SCREEN_PAGE_MODE_USE_NONE = 64
    NON_FULL_SCREEN_PAGE_MODE_USE_OUTLINES = 128
    NON_FULL_SCREEN_PAGE_MODE_USE_THUMBS = 256
    NON_FULL_SCREEN_PAGE_MODE_USE_OC = 512
    DIRECTION_L2R = 1024
    DISPLAY_DOC_TITLE_IN_TITLE_BAR = 2048
    PAGE_LAYOUT_SINGLE_PAGE = 4096
    PAGE_LAYOUT_ONE_COLUMN = 8192
    PAGE_LAYOUT_TWO_COLUMN_LEFT = 16384
    PAGE_LAYOUT_TWO_COLUMN_RIGHT = 32768
    PAGE_LAYOUT_TWO_PAGE_LEFT = 65536
    PAGE_LAYOUT_TWO_PAGE_RIGHT = 131072


def change_viewer_preferences(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    # Get current viewer preference and toggle single-page layout
    current_preference = ViewerPreference(content_editor.get_viewer_preference())
    updated_preference = current_preference | ViewerPreference.PAGE_LAYOUT_SINGLE_PAGE
    content_editor.change_viewer_preference(int(updated_preference))

    # Save updated document
    content_editor.save(outfile)
```
