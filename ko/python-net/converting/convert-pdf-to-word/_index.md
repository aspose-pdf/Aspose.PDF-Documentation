---
title: 파이썬에서 PDF를 워드로 변환
linktitle: PDF를 워드로 변환
type: docs
weight: 10
url: /ko/python-net/convert-pdf-to-word/
lastmod: "2026-06-10"
description: Python에서 PDF를 Word로 변환하는 방법을 알아보세요. PDF를 DOC로, PDF를 DOCX로, PDF를 DOCX로 변환하고, Aspose.PDF 기반의 고급 레이아웃 인식을 할 수 있습니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 파이썬에서 PDF를 DOC와 DOCX로 변환
Abstract: 이 문서에서는.NET을 통해 Python용 Aspose.PDF 를 사용하여 PDF 파일을 마이크로소프트 워드 형식으로 변환하는 방법을 보여줍니다.PDF 콘텐츠에서 편집 가능한 Word 문서를 만들기 위한 PDF를 DOC로, PDF에서 DOC로, PDF를 DOCX로, 그리고 고급 레이아웃 인식 옵션에 대해 설명합니다.
---

이 페이지에서는**Python에서 PDF를 Word로 변환하는 방법**을 보여줍니다.수정, 재사용 또는 사무용 문서 워크플로우를 위해 PDF 파일에서 편집 가능한 DOC 또는 DOCX 출력이 필요한 경우 이 예제를 사용하십시오.

## 파이썬에서 PDF를 DOC로 변환

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC로 변환하여 콘텐츠를 더 쉽게 관리할 수 있다는 것입니다.**.NET을 통한 파이썬용 Aspose.pdf**를 사용하면 PDF 파일을 DOC뿐만 아니라 DOCX 형식으로도 쉽고 효율적으로 변환할 수 있습니다.

텍스트를 수정하거나, Office 워크플로우에서 콘텐츠를 재사용하거나, PDF 콘텐츠를 편집 가능한 DOC 또는 DOCX 문서로 이동해야 하는 경우 Word 변환을 사용하십시오.

더 [문서 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 클래스는 PDF 파일을 DOC 형식으로 변환하는 프로세스를 개선하는 다양한 속성을 제공합니다.이러한 속성 중에서 모드를 사용하면 PDF 내용의 인식 모드를 지정할 수 있습니다.RecognitionMode 열거에 있는 모든 값을 이 속성에 지정할 수 있습니다.각 값에는 특정한 이점과 제한 사항이 있습니다.

단계: 파이썬에서 PDF를 DOC로 변환

1. PDF를 'AP.Document' 개체에 로드합니다.
1. 'DocSaveOptions' 인스턴스를 생성합니다.
1. 형식 속성을 'DocFormat.DOC '로 설정하여 출력이.doc 형식 (이전 Word 형식) 으로 표시되도록 합니다.
1. 지정된 저장 옵션을 사용하여 PDF를 Word 문서로 저장합니다.
1. 확인 메시지를 인쇄합니다.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**온라인에서 PDF를 DOC로 변환해 보세요**

파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 DOC로”](https://products.aspose.app/pdf/conversion/pdf-to-doc)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![PDF를 DOC로 변환](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 파이썬에서 PDF를 DOCX로 변환

파이썬 API용 Aspose.PDF 를 사용하면.NET을 통해 파이썬을 사용하여 PDF 문서를 읽고 DOCX로 변환할 수 있습니다.DOCX는 Microsoft Word 문서에 사용되는 잘 알려진 형식으로, 구조가 일반 바이너리에서 XML과 바이너리 파일의 조합으로 변경되었습니다.Word 2007 및 하위 버전에서는 Docx 파일을 열 수 있지만 DOC 파일 확장명을 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

다음 파이썬 코드 스니펫은 PDF 파일을 DOCX 형식으로 변환하는 과정을 보여줍니다.

단계: 파이썬에서 PDF를 DOCX로 변환

1. 'AP.Document'를 사용하여 소스 PDF를 로드합니다.
1. 'DocSaveOptions'의 인스턴스를 생성합니다.
1. .docx 파일 (최신 Word 형식) 을 생성하려면 형식 속성을 'DocFormat.doc_x'로 설정합니다.
1. 구성된 저장 옵션을 사용하여 PDF를 DOCX 파일로 저장합니다.
1. 변환 후 확인 메시지를 인쇄합니다.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## 고급 레이아웃 인식 기능을 사용하여 PDF를 DOCX로 변환

고급 인식 설정이 포함된 Python과 Aspose.PDF 를 사용하여 PDF 문서를 DOCX (Word) 파일로 변환합니다.향상된 흐름 모드를 사용하여 문서 구조를 보존하므로 출력을 더 쉽게 편집할 수 있고 원본 레이아웃에 더 가깝게 만들 수 있습니다.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

더 [문서 저장 옵션](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 클래스에는 결과 문서의 형식, 즉 DOC 또는 DOCX를 지정하는 기능을 제공하는 Format이라는 속성이 있습니다.PDF 파일을 DOCX 형식으로 변환하려면 DocSaveOptions.docFormat 열거에서 Docx 값을 전달하십시오.

{{% alert color="warning" %}}
**온라인에서 PDF를 DOCX로 변환해 보세요**

파이썬용 Aspose.PDF 는 온라인 애플리케이션을 제공합니다 [“PDF를 워드로”](https://products.aspose.app/pdf/conversion/pdf-to-docx)여기서 작동하는 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF PDF를 워드 앱으로 변환](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 관련 전환

- [PDF를 엑셀로 변환](/pdf/ko/python-net/convert-pdf-to-excel/) 스프레드시트 기반 내보내기용.
- [PDF를 파워포인트로 변환](/pdf/ko/python-net/convert-pdf-to-powerpoint/) 워드 프로세싱 출력 대신 프레젠테이션 슬라이드가 필요할 때
- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 웹 퍼블리싱 및 브라우저 기반 콘텐츠 워크플로우용
