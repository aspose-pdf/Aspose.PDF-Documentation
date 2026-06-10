---
title: 스트림에서 파일 첨부 주석 추가
type: docs
weight: 40
url: /ko/python-net/add-file-attachment-annotation-from-stream/
description: 이 예제에서는 PDF를 로드하고 외부 파일을 메모리 스트림으로 읽고 첫 페이지에 첨부 파일 주석을 추가하고 수정된 문서를 저장합니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python의 스트림에서 PDF에 파일 첨부 주석 추가
Abstract: 이 예제에서는 Facades API를 통해 Python용 Aspose.PDF 파일 스트림을 사용하여 PDF에 파일 첨부 주석을 만드는 방법을 보여줍니다.주석 위치를 지정하고, 설명을 설정하고, 불투명도 값을 포함하고, 수정된 문서를 저장하는 방법을 보여줍니다.
---

파일 첨부 주석을 사용하면 파일을 PDF 페이지 내에 대화형 아이콘으로 포함할 수 있습니다.스트림 기반 접근 방식을 사용하면 실제 파일 경로에 의존하지 않고도 파일을 동적으로 첨부할 수 있습니다.또한 이 방법을 사용하면 불투명도를 비롯한 주석의 모양을 사용자 지정할 수 있습니다.

1. PDF 컨텐트 편집기 객체를 만듭니다.
1. 입력 PDF를 바인딩합니다.
1. 첨부 파일을 스트림으로 읽습니다.
1. 첨부 파일 주석을 추가합니다.
1. 업데이트된 문서를 저장합니다.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_file_attachment_annotation_from_stream(infile, attachment_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)

    with open(attachment_file, "rb") as source_stream:
        attachment_stream = BytesIO(source_stream.read())

    # Create file attachment annotation using stream+opacity overload
    content_editor.create_file_attachment(
        apd.Rectangle(130, 520, 20, 20),
        "Attachment annotation from stream",
        attachment_stream,
        path.basename(attachment_file),
        1,
        "Tag",
        0.75,
    )
    # Save updated document
    content_editor.save(outfile)
```
