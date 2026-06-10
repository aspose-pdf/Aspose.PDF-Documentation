---
title: 모양 스트림으로 러버 스탬프 만들기
type: docs
weight: 30
url: /ko/python-net/create-rubber-stamp-with-appearance-stream/
description: 이 예제에서는 PDF를 로드하고, 모양에 사용할 이미지 파일을 사용하여 1페이지에 고무 스탬프를 만들고, 수정된 문서를 저장합니다.✨
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDFContentEditor를 사용하여 사용자 지정 이미지 모양의 러버 스탬프 만들기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 를 사용하여 PDF에 사용자 지정 이미지 모양으로 러버 스탬프 주석을 만드는 방법을 보여줍니다.이 방법을 사용하면 로고, 도장 또는 서명과 같이 브랜드가 있거나 시각적으로 풍부한 스탬프를 적용할 수 있습니다.
---

외부 이미지 파일을 사용하여 러버 스탬프 주석을 사용자 지정할 수 있습니다.텍스트 기반 스탬프에만 의존하는 대신 시각적 모양 (예: 회사 로고 또는 승인 배지) 을 정의하여 페이지에 배치할 수 있습니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. 스탬프 위치의 직사각형을 정의합니다.
1. 이미지 파일을 스탬프 모양으로 사용합니다.
1. 텍스트 및 색상 설정을 적용합니다.
1. 업데이트된 PDF 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```    
