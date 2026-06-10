---
title: Python에서 PDF 파일 메타데이터로 작업하기
linktitle: PDF 파일 메타데이터
type: docs
weight: 200
url: /ko/python-net/pdf-file-metadata/
description: Aspose.PDF 파일을 사용하여 Python에서 PDF 파일 메타데이터 및 XMP 속성을 추출, 업데이트 및 관리하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF 문서 정보와 XMP 메타데이터를 가져오고 설정합니다.
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF PDF 메타데이터를 사용하는 방법을 설명합니다.작성자, 제목, 키워드와 같은 문서 정보를 읽고, 파일 속성을 업데이트하고, XMP 메타데이터 필드를 설정하고, Python에서 PDF 파일의 사용자 지정 메타데이터 접두사를 등록하는 방법을 알아봅니다.
---

문서 속성을 검사하거나, 검색 또는 카탈로그 작성을 위해 PDF 파일 정보를 업데이트하거나, Python에서 프로그래밍 방식으로 XMP 메타데이터를 관리해야 할 때 이 가이드를 사용하십시오.

## PDF 파일 정보 가져오기

이 코드 스니펫은 Python용 Aspose.PDF 파일을.NET을 통해 PDF 문서에서 메타데이터를 추출하는 방법을 보여줍니다.Document 객체의 info 속성에 액세스하여 작성자, 생성일, 키워드, 수정일, 주제, 제목과 같은 주요 정보를 검색합니다.이 기능은 문서 카탈로그 작성, 검색 최적화 또는 문서 속성 검증이 필요한 응용 프로그램에 필수적입니다.

1. 문서 클래스를 사용하여 PDF 파일 열기
1. info 속성을 통해 문서의 메타데이터를 검색합니다.
1. 메타데이터 정보를 표시합니다.원하는 메타데이터 필드를 출력합니다.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## PDF 파일 정보 설정

.NET을 통한 Python용 Aspose.PDF 를 사용하면 PDF에 대한 파일별 정보, 작성자, 작성 날짜, 주제 및 제목과 같은 정보를 설정할 수 있습니다.이 정보를 설정하려면:

1. 문서 클래스를 사용하여 PDF 파일을 엽니다.
1. 만들기 [문서 정보](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) 객체를 생성하고 원하는 메타데이터 속성을 설정합니다.
1. 저장 방법을 사용하여 변경 사항을 새 PDF 파일에 저장합니다.

다음 코드 스니펫은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## PDF 파일에 XMP 메타데이터 설정

이 코드 스니펫은 .NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 문서에서 XMP 메타데이터를 프로그래밍 방식으로 설정하거나 업데이트하는 방법을 보여줍니다.XMP:CreateDate, XMP:Nickname 및 사용자 정의 필드와 같은 속성을 수정하여 표준화된 메타데이터를 PDF 파일에 포함할 수 있습니다.이 방법은 문서 구성을 개선하고, 검색을 용이하게 하고, 필수 정보를 파일에 직접 포함시키는 데 특히 유용합니다.

Aspose.PDF 를 사용하면 PDF 파일에 메타데이터를 설정할 수 있습니다.메타데이터를 설정하려면:

1. 를 사용하여 PDF 파일을 엽니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 수업.
1. 특정 키에 값을 할당하여 XMP 메타데이터를 수정합니다.
1. 업데이트된 PDF 문서를 저장합니다.

다음 코드 스니펫은 PDF 파일에서 메타데이터를 설정하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## 접두사가 있는 메타데이터 삽입

일부 개발자는 접두사를 사용하여 새 메타데이터 네임스페이스를 만들어야 합니다.다음 코드 스니펫은 접두사를 사용하여 메타데이터를 삽입하는 방법을 보여줍니다.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## 관련 주제

- [파이썬에서의 고급 PDF 작업](/pdf/ko/python-net/advanced-operations/)
- [파이썬에서 PDF 문서로 작업하기](/pdf/ko/python-net/working-with-documents/)
- [파이썬에서 PDF 첨부 파일 작업하기](/pdf/ko/python-net/attachments/)
- [파이썬에서 PDF 문서 비교하기](/pdf/ko/python-net/compare-pdf-documents/)
