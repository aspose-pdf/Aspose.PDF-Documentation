---
title: PDF/3-A 준수 PDF 생성 및 ZUGFeRD 인보이스를 Python에 첨부
linktitle: PDF에 ZUGFeRD 첨부
type: docs
weight: 10
url: /python-net/attach-zugferd/
description: Aspose.PDF for Python via .NET에서 ZUGFeRD가 포함된 PDF 문서를 생성하는 방법을 알아봅니다.
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF에 ZUGFeRD 첨부

PDF에 ZUGFeRD를 첨부하기 위해 다음 단계를 따르는 것을 권장합니다:

1. Aspose.PDF 라이브러리를 가져오고 편의를 위해 ap라는 별칭을 부여합니다.
1. 입력 및 출력 PDF 파일이 위치한 디렉토리의 경로를 정의합니다.
1. 처리할 PDF 파일의 경로를 정의합니다.
1. 경로 변수에서 PDF 파일을 로드하고 문서 객체를 생성합니다.
1. 인보이스 메타데이터가 포함된 XML 파일을 위한 FileSpecification 객체를 생성합니다. 경로 변수와 설명 문자열을 사용하여 FileSpecification 객체를 생성합니다.

1. FileSpecification 객체의 `mime_type` 및 `af_relationship` 속성을 각각 `text/xml` 및 `ALTERNATIVE`로 설정합니다.
1. fileSpecification 객체를 문서 객체의 내장 파일 컬렉션에 추가합니다. 이렇게 하면 XML 파일이 PDF 문서에 송장 메타데이터 파일로 첨부됩니다.
1. PDF 문서를 PDF/A-3A 형식으로 변환합니다. 문서 객체를 변환하기 위해 로그 파일 경로, `PdfFormat.PDF_A_3A` 열거형 및 `ConvertErrorAction.DELETE` 열거형을 사용합니다.
1. 첨부된 ZUGFeRD와 함께 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap

# 입력 및 출력 PDF 파일이 있는 디렉토리의 경로를 정의합니다
_dataDir = "./"

# 처리할 PDF 파일을 로드합니다
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# ZUGFeRD 표준에 부합하는 송장 메타데이터를 포함하는 XML 파일에 대한 FileSpecification 객체를 생성합니다
description = "ZUGFeRD 표준에 부합하는 송장 메타데이터"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# 내장 파일의 MIME 유형 및 AFRelationship 속성을 설정합니다
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# PDF 문서의 내장 파일 컬렉션에 내장 파일을 추가합니다
document.embedded_files.add("factur",fileSpecification)

# PDF 문서를 PDF/A-3A 형식으로 변환합니다
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# 첨부된 ZUGFeRD와 함께 PDF 문서를 저장합니다
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```