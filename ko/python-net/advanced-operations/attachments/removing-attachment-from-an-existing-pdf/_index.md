---
title: 파이썬에서 PDF에서 첨부 파일 제거
linktitle: 기존 PDF에서 첨부 파일 제거
type: docs
weight: 30
url: /ko/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF 는 PDF 문서에서 첨부 파일을 제거할 수 있습니다.파이썬용 Aspose.PDF 파일을.NET 라이브러리를 통해 파이썬 PDF API를 사용하여 PDF 파일에서 첨부 파일을 제거하세요.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python을 사용하여 PDF에서 첨부 파일을 삭제하는 방법
Abstract: 이 문서에서는 Python용 Aspose.PDF 를 사용하여 PDF 파일에서 첨부 파일을 제거하는 방법에 대해 설명합니다.PDF 문서의 첨부 파일은 '문서' 객체의 'EmbeddedFiles' 컬렉션에 저장됩니다.PDF에서 모든 첨부 파일을 삭제하려면 `EmbeddedFiles` 컬렉션에서 `delete () `메서드를 호출한 다음 `Document` 객체의 `save ()` 메서드를 사용하여 업데이트된 문서를 저장할 수 있습니다.문서 열기, 첨부 파일 삭제, 수정된 파일 저장 단계를 보여주는 코드 스니펫이 이 프로세스를 보여 줍니다.
---

파이썬용 Aspose.PDF 는 PDF 파일에서 첨부 파일을 제거할 수 있습니다.PDF 문서의 첨부 파일은 문서 객체에 보관됩니다. [임베디드 파일](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 컬렉션.

이 워크플로는 오래된 내장 파일을 정리하거나, 패키지 크기를 줄이거나, 원본 자료를 첨부하지 않고 재배포할 PDF를 준비해야 할 때 유용합니다.

PDF 파일과 관련된 모든 첨부 파일을 삭제하려면:

1. 전화해 [임베디드 파일](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 컬렉션의 [삭제 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 방법.
1. 를 사용하여 업데이트된 파일을 저장합니다. [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 사물의 [저장 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 방법.

다음 코드 스니펫은 PDF 문서에서 첨부 파일을 제거하는 방법을 보여줍니다.

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## 이름별로 특정 첨부 파일 제거

첨부 파일 하나만 제거하고 다른 첨부 파일은 유지해야 하는 경우 를 사용하십시오. [키를 기준으로 삭제 ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) 메서드를 입력하고 첨부 파일 이름을 전달합니다.

특정 첨부 파일을 삭제하려면:

1. 원본 PDF 파일을 엽니다.
1. 전화 `document.embedded_files.delete_by_key(attachment_name)`.
1. 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 이름을 기준으로 첨부 파일 하나를 제거합니다.

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## 관련 첨부 주제

- [파이썬에서 PDF 첨부 파일 작업하기](/pdf/ko/python-net/attachments/)
- [파이썬에서 PDF에 첨부 파일 추가](/pdf/ko/python-net/add-attachment-to-pdf-document/)
- [Python에서 PDF 포트폴리오를 만들고 관리할 수 있습니다.](/pdf/ko/python-net/portfolio/)

