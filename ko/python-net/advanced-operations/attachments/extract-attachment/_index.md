---
title: PDF에서 첨부 파일 추출
linktitle: 첨부 파일 추출
type: docs
weight: 50
url: /ko/python-net/extract-attachment/
description: Python과 Aspose.PDF 를 사용하여 PDF 첨부 파일을 사용하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Python에서 PDF 첨부 파일 관리를 위한 전체 가이드: 포함된 파일 추가, 추출 및 처리"
Abstract: PDF 첨부 파일은 지원 문서, 보고서, 이미지 및 기타 리소스를 PDF 파일 내에 직접 저장하는 데 널리 사용됩니다.이 문서에서는 Aspose.PDF 를 사용하여 Python으로 PDF 첨부 파일을 처리하는 방법에 대한 전체 개요를 제공합니다.외부 파일을 기존 PDF에 포함하고, 특정 또는 모든 첨부 파일을 추출하고, 파일 크기 및 타임스탬프와 같은 메타데이터를 검사하고, FileAttachment 주석으로 저장된 파일을 복구하는 방법을 설명합니다.각 예제는 첨부 워크플로를 자동화하고, 문서 이동성을 개선하고, 파일 관리를 간소화하는 실용적인 기술을 보여줍니다.엔터프라이즈 문서 시스템을 구축하든 사용자 지정 자동화 스크립트를 구축하든 개발자는 이러한 방법을 사용하여 PDF 문서 내에 포함된 파일을 효율적으로 관리할 수 있습니다.
---

## PDF에서 특정 첨부 파일 추출

Python과 Aspose.PDF 를 사용하여 PDF 문서에서 하나의 임베디드 파일을 추출합니다.첨부 파일을 이름으로 검색하고 내용을 검색한 다음 별도의 파일로 저장합니다.이는 보고서, 로그 또는 PDF에 저장된 지원 파일과 같은 포함된 문서에 액세스할 때 유용합니다.

1. '추출_단일_첨부 () '함수를 정의합니다.
1. PDF 문서를 엽니다.
1. 첨부 파일을 검색합니다.
1. 첨부 파일 콘텐츠 추출.

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## 첨부 파일의 메타데이터 표시

이 도우미 함수는 파일 사양 개체의 메타데이터 정보를 인쇄합니다.일반적으로 Aspose.PDF 를 사용하여 PDF에 포함된 첨부 파일 작업을 할 때 사용되므로 개발자가 체크섬, 만든 날짜, 수정 날짜, 파일 크기 등의 세부 정보를 검사할 수 있습니다.

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## 모든 PDF 첨부 파일 추출 및 검사

이 코드 스니펫은 Python과 Aspose.PDF 를 사용하여 PDF 문서에서 모든 임베디드 파일을 추출하는 방법을 보여줍니다.각 첨부 파일을 지정된 폴더에 저장할 뿐만 아니라 파일 이름, 설명, MIME 유형, 체크섬, 타임스탬프와 같은 세부 메타데이터도 인쇄합니다.이는 PDF 파일에 포함된 내용을 감사, 내보내기 또는 처리하는 데 유용합니다.

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## PDF 첨부 주석에서 파일 추출

Python과 Aspose.PDF 를 사용하여 PDF의 파일첨부 주석에서 포함된 파일을 추출합니다.첫 페이지에서 첫 번째 첨부 파일 주석을 검색하고, 포함된 파일을 검색하고, 선택한 출력 디렉토리에 저장합니다.이는 PDF에 표준 내장 파일 컬렉션 대신 클릭 가능한 첨부 파일 아이콘이 포함되어 있는 경우에 유용합니다.

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```