---
title: 파이썬에서 PDF/A 및 PDF/UA를 PDF로 변환
linktitle: PDF/A 및 PDF/UA를 PDF로 변환
type: docs
weight: 120
url: /ko/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-06-10"
description: .NET을 통해 파이썬용 Aspose.PDF 파일을 사용하여 파이썬의 PDF 파일에서 PDF/A 및 PDF/UA 규정 준수를 제거하고 표준 PDF 문서로 저장하는 방법을 알아봅니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 파이썬에서 PDF/A와 PDF/UA를 표준 PDF로 변환하는 방법
Abstract: 이 문서에서는.NET을 통해 파이썬용 Aspose.PDF 를 사용하여 표준 기반 PDF 문서에서 PDF/A 및 PDF/UA 규정 준수를 제거하는 방법을 설명합니다.보관 파일이나 접근성이 제한된 파일 대신 표준 PDF가 필요할 수 있는 시나리오를 다루고, 규정 준수 메타데이터 및 제한을 제거한 후 결과를 저장하는 방법을 보여줍니다.
---

PDF/A 또는 PDF/UA와 같은 표준 기반 PDF를 다운스트림 편집, 처리 또는 재배포를 위해 일반 PDF 문서로 다시 변환해야 하는 경우 이 페이지를 사용하십시오.

표준 준수 PDF는 보관, 인쇄 및 접근성 워크플로우에 유용하지만 파일을 다른 시스템이나 파이프라인에 통합하기 전에 해당 규정 준수를 제거해야 하는 경우도 있습니다..NET을 통한 Python용 Aspose.PDF 를 사용하면 프로그래밍 방식으로 이 작업을 수행한 다음 결과를 표준 PDF 파일로 저장할 수 있습니다.

## PDF/A를 PDF로 변환

이 예제에서는 문서를 일반 PDF 파일로 다시 저장할 수 있도록 PDF에서 PDF/A 준수 메타데이터 및 제한을 제거합니다.

1. 'AP.Document'를 사용하여 PDF 문서를 로드합니다.
1. 모든 PDF/A 관련 규정 준수 설정 및 메타데이터를 제거하려면 'remove_pdfa_compliance () '을 호출하십시오.
1. 결과 PDF를 출력 경로에 저장합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)
```

## PDF/UA 규정 준수 제거

이 예제에서는 PDF/UA 관련 규정 준수를 제거하여 문서를 비접근성 관련 워크플로우용 표준 PDF로 저장하는 방법을 보여 줍니다.

1. 'AP.Document () '를 사용하여 PDF 문서를 로드합니다.
1. PDF/A 제한 또는 규정 준수 설정을 제거하려면 'document.remove_pdfa_compliance () '을 호출하십시오.
1. 수정한 PDF를 '경로_아웃파일'에 저장합니다.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFUA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)
```

## 이 워크플로를 사용하는 경우

- PDF/A 또는 PDF/UA 제한이 필요하지 않은 툴체인으로 문서를 보내기 전에 규정 준수 설정을 제거합니다.
- 보관 또는 접근성 메타데이터가 더 이상 필요하지 않을 때 다운스트림 문서 처리를 간소화합니다.
- 입력 PDF를 다른 형식으로 내보내기 전에 표준화합니다.

## 관련 전환

- [PDF를 PDF/A, PDF/E 및 PDF/X로 변환](/pdf/ko/python-net/convert-pdf-to-pdf_x/) 이와 반대되는 워크플로우가 필요하고 표준을 준수하는 PDF를 작성하려는 경우
- [PDF를 워드로 변환](/pdf/ko/python-net/convert-pdf-to-word/) 규정 준수 제약 조건을 제거한 후 편집 가능한 문서 출력용
- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 표준 PDF 파일을 브라우저에 맞게 출력할 수 있습니다.
