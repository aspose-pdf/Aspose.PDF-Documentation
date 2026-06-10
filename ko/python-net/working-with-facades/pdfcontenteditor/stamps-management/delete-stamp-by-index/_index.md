---
title: 색인별 스탬프 삭제
type: docs
weight: 50
url: /ko/python-net/delete-stamp-by-index/
description: 이 예제에서는 2페이지에 두 개의 러버 스탬프를 만듭니다.그런 다음 색인을 지정하여 스탬프를 삭제할 수 있습니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 PDFContentEditor를 사용하여 PDF에서 색인별로 러버 스탬프 삭제하기
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 색인을 사용하여 PDF에서 러버 스탬프 주석을 삭제하는 방법을 보여줍니다.스탬프를 여러 개 추가한 다음 페이지에서의 순서에 따라 스탬프 중 하나를 삭제하는 방법을 보여 줍니다.
---

페이지에 여러 개의 러버 스탬프가 있는 경우 색인을 사용하여 특정 스탬프를 삭제할 수 있습니다.delete_stamp () 메서드를 사용하면 순서에 따라 주석을 제거할 수 있습니다. 이는 스탬프 ID를 추적하지는 못하지만 순서를 알고 있을 때 유용합니다.

1. 만들기 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) 예.
1. 입력 PDF 문서를 바인딩합니다.
1. bind_pdf (파일 내) 를 사용하여 입력 PDF 파일을 PDF 콘텐츠 편집기 인스턴스에 바인딩합니다.
1. 페이지 2와 3에서 인덱스 1이 있는 스탬프를 제거하려면 'delete_stamp (1, [2, 3]) '를 호출합니다.
1. save (outfile) 를 사용하여 수정된 PDF 문서를 출력 파일에 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```
