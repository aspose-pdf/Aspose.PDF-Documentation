---
title: Python에서 PDF/3-A 호환 PDF를 생성하고 ZUGFeRD 인보이스 첨부하기
linktitle: ZUGFeRD를 PDF에 첨부
type: docs
weight: 10
url: /ko/python-net/attach-zugferd/
description: 이 문서는 Aspose.PDF 라이브러리를 사용하여 PDF 문서에 ZUGFeRD(전자 청구서를 위한 형식)를 첨부하는 단계별 가이드를 제공합니다. 절차는 필요한 라이브러리를 가져오고 입력 및 출력 파일에 대한 디렉터리 경로를 설정하는 것부터 시작합니다. 대상 PDF 파일을 Document 객체에 로드하고, XML 인보이스 메타데이터 파일에 대한 FileSpecification 객체를 생성합니다. `mime_type`과 `af_relationship`과 같은 핵심 속성을 설정하여 메타데이터가 올바르게 통합되도록 합니다. 그런 다음 XML 파일을 PDF의 임베디드 파일 컬렉션에 추가하여 메타데이터로 첨부합니다. 이후 PDF 문서를 전자 문서 보관에 적합한 PDF/A-3A 형식으로 변환한 뒤, ZUGFeRD가 임베드된 최종 PDF를 저장합니다. 문서는 이러한 단계들을 구현한 Python 코드 스니펫을 제공하며, PDF와 ZUGFeRD의 통합을 통한 문서 관리 향상을 보여줍니다.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF 문서에 ZUGFeRD를 첨부하는 방법
Abstract: 이 기사에서는 Aspose.PDF 라이브러리를 사용하여 PDF 문서에 ZUGFeRD(전자 인보이스 형식)를 첨부하는 방법을 단계별로 안내합니다. 먼저 필요한 라이브러리를 가져오고 입력 및 출력 파일의 디렉터리 경로를 설정합니다. 대상 PDF 파일을 Document 객체에 로드하고, 인보이스 메타데이터 XML 파일에 대한 FileSpecification 객체를 생성합니다. `mime_type` 및 `af_relationship` 속성을 각각 `text/xml`과 `ALTERNATIVE`로 설정하여 메타데이터가 올바르게 통합되도록 합니다. 그런 다음 XML 파일을 PDF의 임베디드 파일 컬렉션에 추가하여 메타데이터 파일로 첨부합니다. 이후 PDF 문서를 전자 문서 보관에 적합한 PDF/A-3A 형식으로 변환하고, 최종적으로 ZUGFeRD가 임베드된 PDF를 저장합니다. 마지막으로 이러한 단계를 구현한 Python 코드 예제가 제공되어 PDF와 ZUGFeRD의 통합을 통한 문서 관리 향상을 시연합니다.
---

## ZUGFeRD를 PDF에 첨부하기

ZUGFeRD를 PDF에 첨부하기 위해 다음 단계들을 권장합니다:

1. Aspose.PDF 라이브러리를 가져오고 편의를 위해 ap라는 별칭을 지정합니다.
1. 입력 및 출력 PDF 파일이 위치한 디렉터리 경로를 정의합니다.
1. 처리할 PDF 파일의 경로를 정의합니다.
1. 경로 변수에서 PDF 파일을 로드하고 Document 객체를 생성합니다.
1. 인보이스 메타데이터를 포함하는 XML 파일에 대한 FileSpecification 객체를 생성합니다. 경로 변수와 설명 문자열을 사용하여 FileSpecification 객체를 만듭니다.
1. FileSpecification 객체의 `mime_type`과 `af_relationship` 속성을 각각 `text/xml`과 `ALTERNATIVE`로 설정합니다.
1. fileSpecification 객체를 document 객체의 임베디드 파일 컬렉션에 추가합니다. 이렇게 하면 XML 파일이 인보이스 메타데이터 파일로 PDF 문서에 첨부됩니다.
1. PDF 문서를 PDF/A-3A 형식으로 변환합니다. 로그 파일 경로와 `PdfFormat.PDF_A_3A` 열거형, `ConvertErrorAction.DELETE` 열거형을 사용하여 document 객체를 변환합니다.
1. 첨부된 ZUGFeRD와 함께 PDF 문서를 저장합니다.

```python
import aspose.pdf as ap

# Define the path to the directory where the input and output PDF files are located
_dataDir = "./"

# Load the PDF file that will be processed
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Create a FileSpecification object for the XML file that contains the invoice metadata
description = "Invoice metadata conforming to ZUGFeRD standard"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Set the MIME type and the AFRelationship properties of the embedded file
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Add the embedded file to the PDF document's embedded files collection
document.embedded_files.add("factur",fileSpecification)

# Convert the PDF document to the PDF/A-3A format
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Save the PDF document with the attached ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```

