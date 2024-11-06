---
title: C++에서 PDF를 Microsoft PowerPoint로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: ko/cpp/convert-pdf-to-powerpoint/
description: Aspose.PDF는 C++를 사용하여 PDF를 PowerPoint 형식으로 변환할 수 있게 해줍니다. 슬라이드를 이미지로 하여 PDF를 PPTX로 변환할 수 있습니다.
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 개요

이 문서에서는 **C++를 사용하여 PDF를 PowerPoint 형식으로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **PPTX**
- [C++ PDF에서 PPTX로](#cpp-pdf-to-pptx)
- [C++ PDF를 PPTX로 변환](#cpp-pdf-to-pptx)
- [C++ PDF 파일을 PPTX로 변환하는 방법](#cpp-pdf-to-pptx)

_형식_: **Microsoft PowerPoint PPTX 형식**
- [C++ PDF에서 PowerPoint로](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint로 변환](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF 파일을 PowerPoint로 변환하는 방법](#cpp-pdf-to-powerpoint-pptx)

이 문서에서 다루는 기타 주제.
- [참조](#see-also)

## C++ PDF에서 PowerPoint 변환

**Aspose.PDF for C++**를 사용하면 PDF에서 PPTX로 변환하는 진행 상황을 추적할 수 있습니다.

PDF를 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>로 변환하는 동안, 텍스트는 선택/업데이트할 수 있는 텍스트로 렌더링됩니다. PDF 파일을 PPTX 형식으로 변환하려면, Aspose.PDF는 [`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options)라는 클래스를 제공합니다. PptxSaveOptions 클래스의 객체는 [`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 메소드의 두 번째 인수로 전달됩니다. 다음 코드 스니펫은 PDF 파일을 PPTX 형식으로 변환하는 과정을 보여줍니다.

## Aspose.PDF for C++를 사용한 PDF에서 PPTX로의 간단한 변환

PDF를 PPTX로 변환하기 위해, Aspose.PDF for C++는 다음의 코드 단계를 사용할 것을 권장합니다.

<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>단계: C++에서 PDF를 PPTX로 변환</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>단계: C++에서 PDF를 PowerPoint PPTX 형식으로 변환</strong></a>

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스의 인스턴스를 생성합니다.
2. [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) 클래스의 인스턴스를 생성합니다.
3. **Document** 객체의 **Save** 메서드를 사용하여 _PDF를 PPTX로 저장합니다_.

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // 문서를 엽니다
    auto document = MakeObject<Document>(_dataDir + infilename);

    // PPTX 형식으로 출력 저장
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 슬라이드를 이미지로 PDF를 PPTX로 변환

선택 가능한 텍스트 대신 이미지로 검색 가능한 PDF를 PPTX로 변환해야 하는 경우, Aspose.PDF는 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) 클래스를 통해 이러한 기능을 제공합니다. 이 작업을 수행하려면 [PptxSaveOptios](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) 클래스의 [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) 속성을 'true'로 설정합니다. 다음 코드 샘플에 나와 있습니다.

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // PPTX 형식으로 출력 저장
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PPTX 변환의 진행 상세 정보

Aspose.PDF for C++를 사용하면 PDF에서 PPTX로의 변환 진행 상황을 추적할 수 있습니다. [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) 클래스는 변환의 진행 상황을 추적하기 위해 사용자 지정 메서드에 지정할 수 있는 [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) 속성을 제공합니다. 다음 코드 샘플에 나와 있습니다.

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //사용자 지정 진행 상황 핸들러 지정
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // PPTX 형식으로 출력 저장
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
다음은 진행 상황 변환을 표시하기 위한 사용자 정의 메서드입니다.

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 변환 진행률 : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 결과 페이지의 " << eventInfo->Value << " / " << eventInfo->MaxValue << " 레이아웃 생성됨." << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 결과 페이지의 " << eventInfo->Value << " / " << eventInfo->MaxValue << " 내보내짐." << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 소스 페이지 " << eventInfo->Value << " / " << eventInfo->MaxValue << " 분석됨." << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**PDF를 PowerPoint로 온라인 변환 시도**

Aspose.PDF for C++는 온라인 무료 애플리케이션 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)를 제공하여 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## 관련 항목

이 문서에서는 다음 주제도 다룹니다. 코드는 위와 동일합니다.

_형식_: **PowerPoint**
- [C++ PDF를 PowerPoint 코드로 변환](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint API로 변환](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint로 프로그래밍 방식으로 변환](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint 라이브러리로 변환](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint로 저장](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF에서 PowerPoint 생성](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF에서 PowerPoint 만들기](#cpp-pdf-to-powerpoint-pptx)

- [C++ PDF를 PowerPoint 변환기로 변환](#cpp-pdf-to-powerpoint-pptx)

_Format_: **Microsoft PowerPoint PPTX format**
- [C++ PDF를 PowerPoint PPTX로 변환 코드](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint PPTX로 변환 API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint PPTX로 프로그래밍 방식으로 변환](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint PPTX로 변환 라이브러리](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint PPTX로 저장](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF에서 PowerPoint PPTX 생성](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF에서 PowerPoint PPTX 만들기](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF를 PowerPoint PPTX로 변환기](#cpp-pdf-to-powerpoint-pptx)

_Format_: **PPTX**
- [C++ PDF를 PPTX로 변환 코드](#cpp-pdf-to-pptx)
- [C++ PDF를 PPTX로 변환 API](#cpp-pdf-to-pptx)
- [C++ PDF를 PPTX로 프로그래밍 방식으로 변환](#cpp-pdf-to-pptx)
- [C++ PDF를 PPTX로 변환 라이브러리](#cpp-pdf-to-pptx)
- [C++ PDF를 PPTX로 저장](#cpp-pdf-to-pptx)
- [C++ PDF에서 PPTX 생성](#cpp-pdf-to-pptx)
- [C++ PDF에서 PPTX 만들기](#cpp-pdf-to-pptx)
- [C++ PDF를 PPTX로 변환기](#cpp-pdf-to-pptx)