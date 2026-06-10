---
title: PDF/3-A 호환 PDF 작성 및 파이썬으로 ZugFERD 인보이스 첨부
linktitle: 주그퍼드를 PDF에 첨부하기
type: docs
weight: 10
url: /ko/python-net/attach-zugferd/
description: .NET을 통해 파이썬용 Aspose.PDF 파일에서 ZugFerd를 사용하여 PDF 문서를 생성하는 방법을 알아보세요.
lastmod: "2026-06-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 주그퍼드를 PDF 문서에 첨부하는 방법
Abstract: 이 문서에서는 Aspose.PDF 라이브러리를 사용하여 ZugFERD (전자 인보이스 형식) 를 PDF 문서에 첨부하는 방법에 대한 단계별 가이드를 제공합니다.절차는 필요한 라이브러리를 가져오고 입력 및 출력 파일의 디렉토리 경로를 설정하는 것으로 시작됩니다.여기에는 대상 PDF 파일을 Document 객체에 로드하고 XML 인보이스 메타데이터 파일의 FileSpification 객체를 만드는 작업이 포함됩니다.메타데이터가 제대로 통합되도록 `mime_type` 및 `af_relaship`과 같은 주요 속성이 설정됩니다.그러면 XML 파일이 PDF의 임베디드 파일 컬렉션에 추가되어 효과적으로 메타데이터로 첨부됩니다.이후 PDF 문서는 전자 문서 보관에 적합한 PDF/A-3A 형식으로 변환된 후 ZugFerd가 포함된 최종 PDF를 저장합니다.이 기사는 이러한 단계의 구현을 보여주는 Python 코드 스니펫으로 끝을 맺으며, 문서 관리 개선을 위해 ZugFERD를 PDF와 통합하는 방법을 보여줍니다.
---

## 주그퍼드를 PDF에 첨부하기

ZugFERD를 PDF에 첨부하려면 다음 단계를 따르는 것이 좋습니다.

1. 편의를 위해 Aspose.PDF 라이브러리를 가져오고 ap의 별칭을 지정합니다.
1. 입력 및 출력 PDF 파일이 있는 디렉토리의 경로를 정의합니다.
1. 처리할 PDF 파일의 경로를 정의합니다.
1. path 변수에서 PDF 파일을 로드하고 문서 객체를 만듭니다.
1. 인보이스 메타데이터를 포함하는 XML 파일의 FileSpeification 객체를 생성합니다.경로 변수와 설명 문자열을 사용하여 FileSpeification 객체를 만들 수 있습니다.
1. 설정 `mime_type` 및 `af_relationship` 파일 사양 객체의 속성을 `text/xml` 과 `ALTERNATIVE`, 각각.
1. 문서 객체의 포함된 파일 컬렉션에 FileSpection 객체를 추가합니다.그러면 XML 파일이 PDF 문서에 인보이스 메타데이터 파일로 첨부됩니다.
1. PDF 문서를 PDF/A-3A 형식으로 변환합니다.로그 파일 경로를 사용하십시오. `PdfFormat.PDF_A_3A` 열거, 및 `ConvertErrorAction.DELETE` 문서 객체를 변환하기 위한 열거입니다.
1. 첨부된 ZugFerd와 함께 PDF 문서를 저장합니다.

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
