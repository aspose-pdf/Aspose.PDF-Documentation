---
title: 문서 권한 가져오기
linktitle: 문서 권한 가져오기
type: docs
weight: 10
url: /ko/python-net/get-document-privileges/
description: Python용 Aspose.PDF 를 사용하여 프로그래밍 방식으로 PDF 문서의 권한을 확인하는 방법을 알아봅니다.이 자습서에서는 PDFFileInfo 클래스를 사용하여 인쇄, 복사 또는 권한 수정과 같은 문서의 보안 설정을 읽는 방법을 보여줍니다.
lastmod: "2026-06-10"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬용 Aspose.PDF 를 사용하여 PDF 문서 권한 가져오기
Abstract: PDF 문서에는 양식 인쇄, 복사, 수정 또는 채우기와 같은 작업을 제한하는 보안 제한이 있을 수 있습니다.개발자는 프로그래밍 방식으로 이러한 권한에 액세스하여 PDF에서 허용되는 작업을 결정할 수 있습니다.이 안내서는 PDFFileInfo 클래스를 사용하여 PDF의 문서 권한을 검색하고 Python으로 표시하는 방법을 보여줍니다.
---

PDF 권한은 사용자가 문서로 수행할 수 있는 작업과 수행할 수 없는 작업을 제어합니다.공통 권한에는 다음이 포함됩니다.

- 문서 인쇄하기
- 콘텐츠 복사
- 주석 또는 컨텐츠 수정
- 양식 필드 채우기
- 스크린 리더 사용
- 문서 조립 또는 병합

Python용 Aspose.PDF 를 사용하면 다음을 사용하여 프로그래밍 방식으로 이러한 설정을 검사할 수 있습니다. [PDF 파일 정보](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) 수업.이는 자동화된 워크플로우에서 여러 PDF로 작업하거나, 규정 준수를 확인하거나, 응용 프로그램에서 문서 처리를 제어할 때 특히 유용합니다.

1. PDF 파일을 로드합니다.
1. 해당 문서 권한을 검색합니다.
1. 문서에 허용된 작업을 표시합니다.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
