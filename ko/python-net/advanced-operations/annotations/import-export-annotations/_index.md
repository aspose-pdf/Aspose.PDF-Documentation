---
title: Python을 사용하여 주석 가져오기 및 내보내기
linktitle: 주석 가져오기 및 내보내기
type: docs
weight: 80
url: /ko/python-net/import-export-annotations/
description: .NET을 통해 Python용 Aspose.PDF 를 사용하여 하나의 PDF에서 주석을 가져오고 새 PDF 문서로 내보내는 방법을 알아봅니다.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 문서 간에 PDF 주석을 전송합니다.
Abstract: 이 문서에서는 .NET을 통해 Python용 Aspose.PDF 를 사용하여 소스 PDF에서 주석을 복사하고 새 PDF 문서로 내보내는 방법을 설명합니다.이 연습에서는 소스 파일 로드, 대상 문서 만들기, 페이지 추가, 첫 페이지의 주석 복사, 결과 저장 등 프로세스를 작은 단계로 나눕니다.
---

이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 기존 PDF에서 주석을 가져오고 새 PDF 문서로 내보내는 방법을 보여줍니다.

이 예제에서는 소스 파일의 첫 페이지에서 주석을 읽고, 새 PDF를 만들고, 빈 페이지를 추가하고, 각 주석을 새 페이지에 복사합니다.이 방법은 주석, 마크업 또는 검토 메모를 별도의 출력 문서로 이동해야 할 때 유용합니다.

## 소스 PDF 불러오기

만들기 `Document` 이미 주석이 포함된 입력 파일의 객체입니다.이 객체를 사용하면 페이지 컬렉션과 각 페이지에 저장된 주석에 액세스할 수 있습니다.

```python
source_document = ap.Document(infile)
```

## 대상 PDF 만들기

다음으로 가져온 주석을 받을 빈 PDF 문서를 만듭니다.이 단계에서 대상 문서에는 페이지가 없습니다.

```python
destination_document = ap.Document()
```

## 내보낸 주석을 위한 페이지 추가

주석은 페이지에 속해야 하므로 복사하기 전에 대상 문서에 새 페이지를 추가하십시오.

```python
page = destination_document.pages.add()
```

## 소스 페이지에서 주석 복사

원본 PDF의 첫 페이지에서 주석 컬렉션을 반복하여 대상 문서의 새 페이지에 각 주석을 추가합니다.

의 두 번째 주장 `page.annotations.add(annot, True)` 기존 개체 참조만 재사용하는 대신 대상 페이지에 주석을 복사하도록 Aspose.PDF 에 지시합니다.

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## 출력 문서 저장

모든 주석을 복사한 후 대상 문서를 저장하여 최종 PDF 파일을 작성합니다.

```python
destination_document.save(outfile)
```

## 전체 예제

다음 코드는 모든 단계를 하나의 재사용 가능한 함수로 결합합니다.

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## 관련 주제

- [인터랙티브 어노테이션](/python-net/interactive-annotations/)
- [마크업 주석](/python-net/markup-annotations/)
- [미디어 어노테이션](/python-net/media-annotations/)
- [보안 주석](/python-net/security-annotations/)
- [셰이프 주석](/python-net/shape-annotations/)
- [텍스트 기반 주석](/python-net/text-based-annotations/)
- [워터마크 주석](/python-net/watermark-annotations/)
