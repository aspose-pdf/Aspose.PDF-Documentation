---
title: Python에서 PDF를 Microsoft Word 문서로 변환
linktitle: PDF를 Word 2003/2019로 변환
type: docs
weight: 10
url: /ko/python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: Aspose.PDF for Python via .NET을 사용하여 PDF를 Microsoft Word 형식으로 변환하는 Python 코드를 작성하고 PDF를 DOC(DOCX)로 변환하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 개요

이 문서에서는 **Python을 사용하여 PDF를 Microsoft Word 문서로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **DOC**
- [Python PDF를 DOC로](#python-pdf-to-doc)
- [Python PDF를 DOC로 변환](#python-pdf-to-doc)
- [Python PDF 파일을 DOC로 변환하는 방법](#python-pdf-to-doc)

_형식_: **DOCX**
- [Python PDF를 DOCX로](#python-pdf-to-docx)
- [Python PDF를 DOCX로 변환](#python-pdf-to-docx)
- [Python PDF 파일을 DOCX로 변환하는 방법](#python-pdf-to-docx)

_형식_: **Word**
- [Python PDF를 Word로](#python-pdf-to-docx)
- [Python PDF를 Word로 변환](#python-pdf-to-doc)

- [Python PDF 파일을 Word로 변환하는 방법](#python-pdf-to-docx)

## Python PDF to DOC 및 DOCX 변환

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC로 변환하여 콘텐츠 관리를 용이하게 하는 것입니다. **Aspose.PDF for Python**을 사용하면 PDF 파일을 DOC뿐만 아니라 DOCX 형식으로도 쉽게 변환할 수 있습니다.

## PDF를 DOC(Word 97-2003) 파일로 변환

PDF 파일을 DOC 형식으로 쉽게 변환하고 완벽한 제어를 할 수 있습니다. Aspose.PDF for Python은 유연하며 다양한 변환을 지원합니다. 예를 들어, PDF 문서의 페이지를 이미지로 변환하는 것은 매우 인기 있는 기능입니다.

많은 고객들이 요청한 변환 중 하나는 PDF를 DOC로 변환하는 것입니다: PDF 파일을 Microsoft Word 문서로 변환하는 것입니다. 고객들은 PDF 파일을 쉽게 편집할 수 없기 때문에 Word 문서로 변환하기를 원합니다. 일부 회사들은 사용자가 PDF로 시작된 파일에서 텍스트, 표 및 이미지를 조작할 수 있기를 원합니다.

간단하고 이해하기 쉬운 전통을 이어가기 위해, Aspose.PDF for Python은 두 줄의 코드로 원본 PDF 파일을 DOC 파일로 변환할 수 있도록 합니다.
 이 기능을 구현하기 위해 SaveFormat이라는 열거형을 도입했으며, .Doc 값을 사용하여 소스 파일을 Microsoft Word 형식으로 저장할 수 있습니다.

다음 Python 코드 스니펫은 PDF 파일을 DOC 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-pdf-to-doc"><strong>단계: Python에서 PDF를 DOC로 변환</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하여 [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) 형식으로 저장합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # PDF 문서 열기
    document = ap.Document(input_pdf)
    # 파일을 MS Word 문서 형식으로 저장
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### DocSaveOptions 클래스 사용

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 클래스는 PDF 파일을 DOC 형식으로 변환하는 과정을 개선하는 다양한 속성을 제공합니다. 이 속성들 중에서 Mode는 PDF 콘텐츠에 대한 인식 모드를 지정할 수 있게 해줍니다. 이 속성에 대해 RecognitionMode 열거형에서 임의의 값을 지정할 수 있습니다. 이러한 값 각각에는 특정한 이점과 제한이 있습니다:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # 인식 모드를 Flow로 설정
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # 수평 근접성을 2.5로 설정
    save_options.relative_horizontal_proximity = 2.5
    # 변환 과정에서 글머리 기호를 인식하도록 설정
    save_options.recognize_bullets = True

    # 파일을 MS Word 문서 형식으로 저장
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**PDF를 DOC로 온라인 변환 시도하기**

Aspose.PDF for Python은 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)라는 무료 온라인 응용 프로그램을 제공하여, 당신이 기능과 품질을 조사해 볼 수 있습니다.
[![Convert PDF to DOC](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOCX로 변환

Aspose.PDF for Python API를 사용하면 Python via .NET을 통해 PDF 문서를 DOCX로 읽고 변환할 수 있습니다. DOCX는 Microsoft Word 문서의 잘 알려진 형식으로, 구조가 일반 바이너리에서 XML과 바이너리 파일의 조합으로 변경되었습니다. Docx 파일은 Word 2007 및 이후 버전에서 열 수 있지만 DOC 파일 확장자를 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

다음 Python 코드 스니펫은 PDF 파일을 DOCX 형식으로 변환하는 과정을 보여줍니다.

<a name="csharp-pdf-to-docx"><strong>단계: Python에서 PDF를 DOCX로 변환</strong></a>

1. 소스 PDF 문서를 사용하여 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.

2. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 메서드를 호출하여 [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) 형식으로 저장합니다.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # PDF 문서 열기
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # 인식 모드를 Flow로 설정
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # 수평 근접성을 2.5로 설정
    save_options.relative_horizontal_proximity = 2.5
    # 변환 과정에서 불릿을 인식하도록 값 활성화
    save_options.recognize_bullets = True

    # 파일을 MS Word 문서 형식으로 저장
    document.save(output_pdf, save_options)
```

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) 클래스에는 결과 문서의 형식을 DOC 또는 DOCX로 지정할 수 있는 Format이라는 속성이 있습니다.
 PDF 파일을 DOCX 형식으로 변환하려면 DocSaveOptions.DocFormat 열거형에서 Docx 값을 전달하십시오.

{{% alert color="warning" %}}
**PDF를 DOCX로 온라인 변환 시도하기**

Aspose.PDF for Python은 무료 온라인 응용 프로그램 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)를 제공합니다. 이곳에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF PDF를 Word로 변환하는 무료 앱](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 관련 항목 

이 문서에는 다음 주제도 포함되어 있습니다. 코드는 위와 동일합니다.

_형식_: **Word**
- [Python PDF to Word 코드](#python-pdf-to-docx)
- [Python PDF to Word API](#python-pdf-to-docx)
- [Python PDF를 Word로 프로그래밍 방식으로 변환](#python-pdf-to-docx)
- [Python PDF to Word 라이브러리](#python-pdf-to-docx)
- [Python PDF를 Word로 저장](#python-pdf-to-docx)
- [Python PDF에서 Word 생성](#python-pdf-to-docx)
- [Python PDF에서 Word 만들기](#python-pdf-to-docx)

- [Python PDF to Word 변환기](#python-pdf-to-docx)
_Format_: **DOC**
- [Python PDF to DOC Code](#python-pdf-to-doc)
- [Python PDF to DOC API](#python-pdf-to-doc)
- [Python PDF to DOC Programmatically](#python-pdf-to-doc)
- [Python PDF to DOC Library](#python-pdf-to-doc)
- [Python Save PDF as DOC](#python-pdf-to-doc)
- [Python Generate DOC from PDF](#python-pdf-to-doc)
- [Python Create DOC from PDF](#python-pdf-to-doc)
- [Python PDF to DOC Converter](#python-pdf-to-doc)

_형식_: **DOCX**
- [Python PDF를 DOCX 코드로 변환](#python-pdf-to-docx)
- [Python PDF를 DOCX API로 변환](#python-pdf-to-docx)
- [Python PDF를 DOCX로 프로그래밍 방식으로 변환](#python-pdf-to-docx)
- [Python PDF를 DOCX 라이브러리로 변환](#python-pdf-to-docx)
- [Python PDF를 DOCX로 저장](#python-pdf-to-docx)
- [Python PDF에서 DOCX 생성](#python-pdf-to-docx)
- [Python PDF에서 DOCX 만들기](#python-pdf-to-docx)
- [Python PDF를 DOCX 변환기로 변환](#python-pdf-to-docx)