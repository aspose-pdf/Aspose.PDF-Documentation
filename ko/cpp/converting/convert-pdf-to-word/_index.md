---
title: C++에서 PDF를 Microsoft Word 문서로 변환
linktitle: PDF를 Word로 변환
type: docs
weight: 10
url: ko/cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Aspose.PDF for C++ 라이브러리를 사용하면 C++로 PDF를 Word 형식으로 쉽게 변환하고 완전한 제어가 가능합니다. 이 형식에는 DOC 및 DOCX가 포함됩니다. PDF를 Microsoft Word 문서로 변환하는 방법을 더 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 개요

이 문서에서는 C++를 사용하여 PDF를 Microsoft Word 문서로 변환하는 방법을 설명합니다. 다음 주제를 다룹니다.

_형식_: **DOC**
- [C++ PDF를 DOC로](#cpp-pdf-to-doc)
- [C++ PDF를 DOC로 변환](#cpp-pdf-to-doc)
- [C++ PDF 파일을 DOC로 변환하는 방법](#cpp-pdf-to-doc)

_형식_: **DOCX**
- [C++ PDF를 DOCX로](#cpp-pdf-to-docx)
- [C++ PDF를 DOCX로 변환](#cpp-pdf-to-docx)
- [C++ PDF 파일을 DOCX로 변환하는 방법](#cpp-pdf-to-docx)

_형식_: **Microsoft Word DOC 형식**
- [C++ PDF를 Word로](#cpp-pdf-to-word-doc)
- [C++ PDF를 Word로 변환](#cpp-pdf-to-word-doc)

- [C++ PDF 파일을 Word로 변환하는 방법](#cpp-pdf-to-word-doc)

_Format_: **Microsoft Word DOCX 형식**
- [C++ PDF를 Word로](#cpp-pdf-to-word-docx)
- [C++ PDF를 워드로 변환](#cpp-pdf-to-word-docx)
- [C++ PDF 파일을 워드로 변환하는 방법](#cpp-pdf-to-word-docx)

이 문서에서 다루는 기타 주제
- [참조](#see-also)

## C++ PDF를 Word로 변환

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC로 변환하여 콘텐츠를 쉽게 조작할 수 있게 하는 것입니다. Aspose.PDF for C++를 사용하면 PDF 파일을 DOC로 변환할 수 있습니다.

## PDF를 DOC (Word 97-2003) 파일로 변환

PDF 파일을 DOC 형식으로 쉽게 변환하고 완벽하게 제어할 수 있습니다. Aspose.PDF for C++는 유연하며 다양한 변환을 지원합니다. 예를 들어 PDF 문서의 페이지를 이미지로 변환하는 것은 매우 인기 있는 기능입니다.

많은 고객들이 요청한 변환 중 하나는 PDF를 DOC로 변환하는 것으로, PDF 파일을 Microsoft Word 문서로 변환하는 것입니다. 고객들은 PDF 파일은 쉽게 편집할 수 없고 Word 문서는 할 수 있기 때문에 이를 원합니다. 일부 회사는 사용자가 PDF로 시작한 파일의 텍스트, 표 및 이미지를 조작할 수 있기를 원합니다.

간단하고 이해하기 쉽게 만드는 전통을 이어가며, Aspose.PDF for C++는 두 줄의 코드로 소스 PDF 파일을 DOC 파일로 변환할 수 있게 합니다. 이 기능을 수행하기 위해 SaveFormat이라는 열거형을 도입했으며, 그 값 .Doc는 소스 파일을 Microsoft Word 형식으로 저장할 수 있게 합니다.

다음 C++ 코드 스니펫은 PDF 파일을 DOC 형식으로 변환하는 과정을 보여줍니다.

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>단계: C++에서 PDF를 DOC로 변환</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>단계: C++에서 PDF를 Microsoft Word DOC 형식으로 변환</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 인스턴스를 생성합니다.
2. 문서를 **SaveFormat::Doc** 형식으로 저장하려면 **Document->Save()** 메서드를 호출하세요.

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // 파일을 MS 문서 형식으로 저장합니다.
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

다음 코드 스니펫은 PDF 파일을 DOC 고급 버전으로 변환하는 과정을 보여줍니다:

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // 인식 모드를 Flow로 설정합니다.
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // 수평 근접성을 2.5로 설정합니다.
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // 변환 과정에서 글머리 기호를 인식하도록 값을 활성화합니다.
    saveOptions->set_RecognizeBullets(true);

    try {
        // 파일을 MS 문서 형식으로 저장합니다.
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**PDF를 DOC로 온라인 변환 시도**

Aspose.PDF for C++는 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)라는 무료 온라인 애플리케이션을 제공하여 기능과 품질을 조사해볼 수 있습니다.

[![Convert PDF to DOC](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOCX로 변환

Aspose.PDF for C++ API를 사용하면 C++ 언어를 사용하여 PDF 문서를 DOCX로 읽고 변환할 수 있습니다. DOCX는 Microsoft Word 문서의 잘 알려진 형식으로, 구조가 평문 바이너리에서 XML 및 바이너리 파일의 조합으로 변경되었습니다. Docx 파일은 Word 2007 및 이후 버전에서 열 수 있지만 DOC 파일 확장자를 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

다음 C++ 코드 스니펫은 PDF 파일을 DOCX 형식으로 변환하는 과정을 보여줍니다.


<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>단계: C++에서 PDF를 DOCX로 변환</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>단계: C++에서 PDF를 Microsoft Word DOCX 형식으로 변환</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 인스턴스를 생성합니다.
2. **Document->Save()** 메서드를 호출하여 **SaveFormat::DocX** 형식으로 저장합니다.

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // 파일을 MS 문서 형식으로 저장
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

[`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) 클래스는 결과 문서의 형식을 DOC 또는 DOCX로 지정할 수 있는 Format이라는 속성을 가지고 있습니다. PDF 파일을 DOCX 형식으로 변환하려면 DocSaveOptions.DocFormat 열거형에서 Docx 값을 전달하십시오.

다음 코드 스니펫은 C++로 PDF 파일을 DOCX 형식으로 변환할 수 있는 기능을 제공합니다.

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // 다른 DocSaveOptions 매개변수 설정
    // ...

    // 파일을 MS 문서 형식으로 저장

    try {
        // 파일을 MS 문서 형식으로 저장
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="warning" %}}
**PDF를 DOCX로 온라인으로 변환 시도**

Aspose.PDF for C++는 ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)라는 무료 온라인 애플리케이션을 제공하며, 이곳에서 기능과 작동 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to Word Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 관련 항목

이 문서에는 또한 다음 주제가 포함됩니다. 코드는 위와 동일합니다.

_형식_: **Microsoft Word DOC 형식**
- [C++ PDF to Word Code](#cpp-pdf-to-word-doc)
- [C++ PDF to Word API](#cpp-pdf-to-word-doc)
- [C++ PDF to Word Programmatically](#cpp-pdf-to-word-doc)
- [C++ PDF to Word Library](#cpp-pdf-to-word-doc)
- [C++ Save PDF as Word](#cpp-pdf-to-word-doc)
- [C++ Generate Word from PDF](#cpp-pdf-to-word-doc)
- [C++ Create Word from PDF](#cpp-pdf-to-word-doc)
- [C++ PDF to Word Converter](#cpp-pdf-to-word-doc)

_형식_: **Microsoft Word DOCX 형식**

- [C++ PDF to Word Code](#cpp-pdf-to-word-docx)
```
- [C++ PDF to Word API](#cpp-pdf-to-word-docx)
- [C++ PDF to Word Programmatically](#cpp-pdf-to-word-docx)
- [C++ PDF to Word Library](#cpp-pdf-to-word-docx)
- [C++ Save PDF as Word](#cpp-pdf-to-word-docx)
- [C++ Generate Word from PDF](#cpp-pdf-to-word-docx)
- [C++ Create Word from PDF](#cpp-pdf-to-word-docx)
- [C++ PDF to Word Converter](#cpp-pdf-to-word-docx)

_포맷_: **DOC**
- [C++ PDF to DOC Code](#cpp-pdf-to-doc)
- [C++ PDF to DOC API](#cpp-pdf-to-doc)
- [C++ PDF to DOC Programmatically](#cpp-pdf-to-doc)
- [C++ PDF to DOC Library](#cpp-pdf-to-doc)
- [C++ Save PDF as DOC](#cpp-pdf-to-doc)
- [C++ Generate DOC from PDF](#cpp-pdf-to-doc)
- [C++ Create DOC from PDF](#cpp-pdf-to-doc)
- [C++ PDF to DOC Converter](#cpp-pdf-to-doc)

_포맷_: **DOC**
- [C++ PDF to DOCX Code](#cpp-pdf-to-docx)
- [C++ PDF to DOCX API](#cpp-pdf-to-docx)
- [C++ PDF to DOCX Programmatically](#cpp-pdf-to-docx)
- [C++ PDF to DOCX Library](#cpp-pdf-to-docx)
- [C++ Save PDF as DOCX](#cpp-pdf-to-docx)

- [C++ Generate DOCX from PDF](#cpp-pdf-to-docx)
```
- [C++ PDF에서 DOCX 생성](#cpp-pdf-to-docx)  
- [C++ PDF에서 DOCX 변환기](#cpp-pdf-to-docx)