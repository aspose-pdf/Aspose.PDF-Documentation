---
title: Python에서 PDF를 Microsoft Word 문서로 변환
linktitle: PDF를 Word 2003/2019로 변환
type: docs
weight: 10
url: ko/python-java/convert-pdf-to-word/
lastmod: "2023-04-06"
description: Aspose.PDF for Python via .NET으로 PDF를 Microsoft Word 형식으로 변환하는 Python 코드를 작성하고 PDF를 DOC(DOCX)로 변환하는 방법을 배우세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 개요

이 문서는 **Python을 사용하여 PDF를 Microsoft Word 문서로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **DOC**
- [Python PDF to DOC](#python-pdf-to-doc)
- [Python Convert PDF to DOC](#python-pdf-to-doc)
- [Python How to convert PDF file to DOC](#python-pdf-to-doc)

_형식_: **DOCX**
- [Python PDF to DOCX](#python-pdf-to-docx)
- [Python Convert PDF to DOCX](#python-pdf-to-docx)
- [Python How to convert PDF file to DOCX](#python-pdf-to-docx)

_형식_: **Word**
- [Python PDF to Word](#python-pdf-to-docx)
- [Python Convert PDF to Word](#python-pdf-to-doc)

- [Python How to convert PDF file to Word](#python-pdf-to-docx)

## Python PDF to DOC 및 DOCX 변환

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC로 변환하는 기능으로, 콘텐츠 관리를 더 쉽게 만들어 줍니다. **Aspose.PDF for Python**은 PDF 파일을 DOC뿐만 아니라 DOCX 형식으로도 쉽고 효율적으로 변환할 수 있습니다.

## PDF를 DOC (Word 97-2003) 파일로 변환

PDF 파일을 DOC 형식으로 쉽게 변환하고 완전한 제어를 할 수 있습니다. Aspose.PDF for Python은 유연하며 다양한 변환을 지원합니다. 예를 들어, PDF 문서의 페이지를 이미지로 변환하는 것은 매우 인기 있는 기능입니다.

많은 고객들이 요청한 변환 중 하나는 PDF에서 DOC로의 변환입니다: PDF 파일을 Microsoft Word 문서로 변환하는 것입니다. 고객들은 PDF 파일은 쉽게 편집할 수 없는 반면, Word 문서는 편집이 가능하기 때문에 이를 원합니다. 일부 회사들은 사용자가 PDF로 시작한 파일에서 텍스트, 표 및 이미지를 조작할 수 있기를 원합니다.

간단하고 이해하기 쉬운 전통을 유지하며, Aspose.PDF for Python은 두 줄의 코드로 원본 PDF 파일을 DOC 파일로 변환할 수 있게 해줍니다.
 이 기능을 구현하기 위해 SaveFormat이라는 열거형을 도입했으며, 그 값 .Doc를 사용하여 소스 파일을 Microsoft Word 형식으로 저장할 수 있습니다.

다음 Python 코드 스니펫은 PDF 파일을 DOC 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-pdf-to-doc"><strong>단계: Python에서 PDF를 DOC로 변환</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 메서드를 호출하여 [SaveFormat.Doc](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) 형식으로 저장합니다.

```python

from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/out.doc"
doc.save(documentOutName, Api.SaveFormat.Doc)
```

### DocSaveOptions 클래스 사용하기

[DocSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/docsaveoptions/) 클래스는 PDF 파일을 DOC 형식으로 변환하는 과정을 개선하는 다양한 속성을 제공합니다. 이 속성들 중에서, Mode는 PDF 콘텐츠에 대한 인식 모드를 지정할 수 있게 해줍니다. 이 속성에 대해 RecognitionMode 열거형의 모든 값을 지정할 수 있습니다. 이러한 값 각각은 특정한 이점과 제한 사항이 있습니다:

```python

from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
# PDF 문서 열기
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Doc
# 인식 모드를 Flow로 설정
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# 수평 근접성을 2.5로 설정
save_options.relative_horizontal_proximity = 2.5
# 변환 과정에서 불렛 인식을 활성화
save_options.recognize_bullets = True

# 파일을 MS Word 문서 형식으로 저장
document.save(output_pdf, save_options)

```

{{% alert color="success" %}}
**PDF를 DOC로 온라인 변환 시도하기**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)을 제공합니다. 여기서 기능과 품질을 조사해 볼 수 있습니다.
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOCX로 변환하기

Aspose.PDF for Python API는 Python을 통해 PDF 문서를 DOCX로 읽고 변환할 수 있게 해줍니다. DOCX는 Microsoft Word 문서의 잘 알려진 형식으로, 구조가 단순한 바이너리에서 XML과 바이너리 파일의 조합으로 변경되었습니다. Docx 파일은 Word 2007 및 이후 버전에서는 열 수 있지만 DOC 파일 확장자를 지원하는 MS Word의 이전 버전에서는 열 수 없습니다.

다음의 Python 코드 스니펫은 PDF 파일을 DOCX 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-pdf-to-docx"><strong>단계: Python에서 PDF를 DOCX로 변환하기</strong></a>

1. 소스 PDF 문서와 함께 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.

2. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 메서드를 호출하여 [SaveFormat.DocX](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) 형식으로 저장합니다.

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.docx"
# PDF 문서 열기
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Docx
# 인식 모드를 Flow로 설정
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# 수평 근접성을 2.5로 설정
save_options.relative_horizontal_proximity = 2.5
# 변환 과정에서 불렛 인식을 활성화
save_options.recognize_bullets = True

# 파일을 MS Word 문서 형식으로 저장
document.save(output_pdf, save_options)
```

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 클래스에는 Format이라는 속성이 있으며, 이 속성은 결과 문서의 형식을 DOC 또는 DOCX로 지정할 수 있는 기능을 제공합니다.
 PDF 파일을 DOCX 형식으로 변환하려면 DocSaveOptions.DocFormat 열거형에서 Docx 값을 전달하세요.

{{% alert color="warning" %}}
**온라인에서 PDF를 DOCX로 변환해 보세요**

Aspose.PDF for Python은 온라인 무료 애플리케이션 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)을 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/java/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 관련 항목 

이 문서에서는 다음 주제도 다룹니다. 코드들은 위와 동일합니다.

_형식_: **Word**
- [Python PDF에서 Word 코드로](#python-pdf-to-docx)
- [Python PDF에서 Word API로](#python-pdf-to-docx)
- [Python PDF에서 프로그래밍 방식으로 Word로](#python-pdf-to-docx)
- [Python PDF에서 Word 라이브러리로](#python-pdf-to-docx)
- [Python PDF를 Word로 저장](#python-pdf-to-docx)
- [Python PDF에서 Word 생성](#python-pdf-to-docx)
- [Python PDF에서 Word 생성](#python-pdf-to-docx)

- [Python PDF에서 Word 변환기](#python-pdf-to-docx)
_Format_: **DOC**
- [Python PDF to DOC Code](#python-pdf-to-doc)
- [Python PDF to DOC API](#python-pdf-to-doc)
- [Python PDF to DOC Programmatically](#python-pdf-to-doc)
- [Python PDF to DOC Library](#python-pdf-to-doc)
- [Python Save PDF as DOC](#python-pdf-to-doc)
- [Python Generate DOC from PDF](#python-pdf-to-doc)
- [Python Create DOC from PDF](#python-pdf-to-doc)
- [Python PDF to DOC Converter](#python-pdf-to-doc)

_포맷_: **DOCX**
- [Python PDF to DOCX Code](#python-pdf-to-docx)
- [Python PDF to DOCX API](#python-pdf-to-docx)
- [Python PDF to DOCX Programmatically](#python-pdf-to-docx)
- [Python PDF to DOCX Library](#python-pdf-to-docx)
- [Python Save PDF as DOCX](#python-pdf-to-docx)
- [Python Generate DOCX from PDF](#python-pdf-to-docx)
- [Python Create DOCX from PDF](#python-pdf-to-docx)
- [Python PDF to DOCX Converter](#python-pdf-to-docx)