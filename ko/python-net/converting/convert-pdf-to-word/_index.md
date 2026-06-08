---
title: Python에서 PDF를 Word로 변환
linktitle: PDF를 Word로 변환
type: docs
weight: 10
url: /ko/python-net/convert-pdf-to-word/
lastmod: "2026-04-14"
description: Python에서 PDF를 Word로 변환하는 방법을 배우세요. 여기에는 PDF를 DOC로, PDF를 DOCX로 변환하고 Aspose.PDF를 사용한 고급 레이아웃 인식이 포함됩니다.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python에서 PDF를 DOC 및 DOCX로 변환
Abstract: 이 문서에서는 Aspose.PDF for Python via .NET을 사용하여 PDF 파일을 Microsoft Word 형식으로 변환하는 방법을 보여줍니다. PDF를 DOC, PDF를 DOCX로 변환하고, PDF 콘텐츠에서 편집 가능한 Word 문서를 만들기 위한 고급 레이아웃 인식 옵션을 다룹니다.
---

이 페이지에서는 **Python에서 PDF를 Word로 변환하는 방법**을 보여줍니다. PDF 파일에서 편집 가능한 DOC 또는 DOCX 출력을 필요로 할 때, 수정, 재사용 또는 사무 문서 작업 흐름에 이 예제를 사용하십시오.

## Python에서 PDF를 DOC로 변환

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC로 변환하는 것으로, 콘텐츠 관리를 보다 쉽게 만들어 줍니다. **Aspose.PDF for Python via .NET**을 사용하면 PDF 파일을 DOC뿐만 아니라 DOCX 형식으로도 쉽고 효율적으로 변환할 수 있습니다.

텍스트를 수정하거나, 사무 워크플로우에서 콘텐츠를 재사용하거나, PDF 콘텐츠를 편집 가능한 DOC 또는 DOCX 문서로 이동해야 할 때 Word 변환을 사용하십시오.

그 [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 클래스는 PDF 파일을 DOC 형식으로 변환하는 과정을 향상시키는 다양한 속성을 제공합니다. 이러한 속성 중 Mode는 PDF 콘텐츠에 대한 인식 모드를 지정할 수 있게 해줍니다. 이 속성에는 RecognitionMode 열거형의 任意 값을 지정할 수 있습니다. 각 값은 고유한 이점과 제한 사항을 가지고 있습니다:

단계: Python에서 PDF를 DOC로 변환

1. PDF를 ’ap.Document’ 객체에 로드합니다.
1. ’DocSaveOptions’ 인스턴스를 생성합니다.
1. 출력이 .doc 형식(이전 Word 형식)으로 나오도록 하려면 format 속성을 ’DocFormat.DOC’로 설정합니다.
1. 지정된 저장 옵션을 사용하여 PDF를 Word 문서로 저장합니다.
1. 확인 메시지를 출력합니다.

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

Aspose.PDF for Python이 온라인 애플리케이션을 제공합니다 [\"PDF를 DOC로\"](https://products.aspose.app/pdf/conversion/pdf-to-doc), 여기서 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![PDF를 DOC로 변환](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Python에서 PDF를 DOCX로 변환

Aspose.PDF for Python API는 Python via .NET을 사용하여 PDF 문서를 DOCX로 읽고 변환할 수 있습니다. DOCX는 Microsoft Word 문서의 잘 알려진 형식으로, 구조가 순수 바이너리에서 XML과 바이너리 파일의 조합으로 변경되었습니다. Docx 파일은 Word 2007 및 그 이후 버전에서 열 수 있지만, DOC 파일 확장자를 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

다음 Python 코드 조각은 PDF 파일을 DOCX 형식으로 변환하는 과정을 보여줍니다.

단계: Python에서 PDF를 DOCX로 변환

1. 'ap.Document'를 사용하여 원본 PDF를 로드합니다.
1. 'DocSaveOptions'의 인스턴스를 생성합니다.
1. 형식 속성을 'DocFormat.DOC_X'로 설정하여 .docx 파일(최신 Word 형식)을 생성합니다.
1. 구성된 저장 옵션을 사용하여 PDF를 DOCX 파일로 저장합니다.
1. 변환 후 확인 메시지를 출력합니다.

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

## 고급 레이아웃 인식을 사용하여 PDF를 DOCX로 변환

Python과 Aspose.PDF를 사용하여 PDF 문서를 DOCX(Word) 파일로 변환합니다. 고급 인식 설정을 적용하며, 향상된 흐름 모드를 사용해 문서 구조를 유지하여 출력물이 더 편집 가능하고 원본 레이아웃에 가깝게 만듭니다.

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

그 [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) class는 Format이라는 속성을 가지고 있으며, 이는 결과 문서의 형식(DOC 또는 DOCX)을 지정할 수 있는 기능을 제공합니다. PDF 파일을 DOCX 형식으로 변환하려면 DocSaveOptions.DocFormat 열거형에서 Docx 값을 전달하십시오.

{{% alert color="warning" %}}
**PDF를 DOCX로 온라인 변환해 보세요**

Aspose.PDF for Python이 온라인 애플리케이션을 제공합니다 ["PDF를 Word로"](https://products.aspose.app/pdf/conversion/pdf-to-docx), 여기서 기능과 품질이 어떻게 작동하는지 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF to Word 앱](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 관련 변환

- [PDF를 Excel로 변환](/pdf/ko/python-net/convert-pdf-to-excel/) 스프레드시트 중심의 내보내기를 위해.
- [PDF를 PowerPoint로 변환](/pdf/ko/python-net/convert-pdf-to-powerpoint/) 워드 프로세싱 출력 대신 프레젠테이션 슬라이드가 필요할 때.
- [PDF를 HTML로 변환](/pdf/ko/python-net/convert-pdf-to-html/) 웹 게시 및 브라우저 기반 콘텐츠 워크플로를 위해.
