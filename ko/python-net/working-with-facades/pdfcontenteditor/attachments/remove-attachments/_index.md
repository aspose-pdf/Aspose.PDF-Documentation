---
title: 첨부 파일 제거
linktitle: 첨부 파일 제거
type: docs
weight: 50
url: /ko/python-net/remove-attachments/
description: 이 예제에서는 입력 PDF를 바인딩하고, 모든 첨부 파일을 삭제하고, 포함된 파일 없이 수정된 PDF를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 모든 첨부 파일 제거
Abstract: 이 예제는 Python용 Aspose.PDF 를 사용하여 Facades API를 통해 PDF 문서에서 모든 첨부 파일을 제거하는 방법을 보여줍니다.PDF를 바인딩하고, 포함된 첨부 파일을 삭제하고, 업데이트된 문서를 저장하는 방법을 보여줍니다.
---

PDF에는 문서, 이미지 또는 기타 파일과 같은 첨부 파일이 포함될 수 있습니다.보안, 개인 정보 보호 또는 배포 목적으로 모든 첨부 파일을 PDF에서 정리해야 하는 시나리오가 있습니다.사용 [PDF 콘텐츠 편집기](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)문서에 포함된 모든 첨부 파일을 프로그래밍 방식으로 제거할 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다. 
1. 입력 PDF를 바인딩합니다.
1. 모든 첨부 파일을 삭제합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def remove_attachments(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Remove all attachments from document
    content_editor.delete_attachments()
    # Save updated document
    content_editor.save(outfile)
```
