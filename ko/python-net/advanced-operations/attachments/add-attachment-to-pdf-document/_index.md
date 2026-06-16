---
title: 파이썬에서 PDF에 첨부 파일 추가
linktitle: PDF 문서에 첨부 파일 추가
type: docs
weight: 10
url: /ko/python-net/add-attachment-to-pdf-document/
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 파이썬에서 PDF 문서에 첨부 파일을 추가하는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python으로 PDF에 첨부 파일을 추가하는 방법
Abstract: 이 문서에서는 Python과 Aspose.PDF 라이브러리를 사용하여 PDF 파일에 첨부 파일을 추가하는 방법에 대한 단계별 가이드를 제공합니다.새 Python 프로젝트를 설정하고, 필요한 Aspose.PDF 패키지를 가져오고, `Document` 객체를 만드는 과정을 자세히 설명합니다.이 문서에서는 원하는 파일과 설명을 포함하는 `FileSpcication` 객체를 만드는 방법과 `add` 메서드를 사용하여 이 객체를 PDF 문서의 `EmbeddedFile Collection`에 추가하는 방법을 설명합니다.'임베디드 파일 컬렉션'은 PDF 내의 모든 첨부 파일을 보관합니다.문서를 열고, 첨부할 파일을 설정하고, 문서의 첨부 파일 컬렉션에 추가하고, 업데이트된 PDF를 저장하는 과정을 보여주는 코드 스니펫이 포함되어 있습니다.
---

첨부 파일에는 다양한 정보가 포함될 수 있으며 파일 형식도 다양할 수 있습니다.이 문서에서는 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다.

지원 소스 파일, 스프레드시트, 이미지 또는 관련 문서를 기본 PDF와 함께 패키지해야 하는 경우 포함된 PDF 첨부 파일을 사용하십시오.

1. 새 Python 프로젝트를 생성합니다.
1. Aspose.PDF 패키지 가져오기
1. 만들기 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 목적.
1. 만들기 [파일 사양](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 추가하려는 파일이 있는 개체 및 파일 설명
1. 추가 [파일 사양](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) 에 대한 반대 [문서](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 사물의 [임베디드 파일 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 컬렉션, 컬렉션 포함 [추가](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) 방법.

더 [임베디드 파일 컬렉션](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) 컬렉션에는 PDF 파일의 모든 첨부 파일이 포함됩니다.다음 코드 스니펫은 PDF 문서에 첨부 파일을 추가하는 방법을 보여줍니다.

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## 관련 첨부 주제

- [파이썬에서 PDF 첨부 파일 작업하기](/pdf/ko/python-net/attachments/)
- [파이썬에서 PDF에서 첨부 파일 제거](/pdf/ko/python-net/removing-attachment-from-an-existing-pdf/)
- [Python에서 PDF 포트폴리오를 만들고 관리할 수 있습니다.](/pdf/ko/python-net/portfolio/)

