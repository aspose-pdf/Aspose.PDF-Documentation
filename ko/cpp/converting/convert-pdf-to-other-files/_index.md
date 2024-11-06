---
title: PDF 파일을 다른 형식으로 변환 
linktitle: PDF를 다른 형식으로 변환 
type: docs
weight: 90
url: ko/cpp/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF가 PDF 파일을 다른 파일 형식으로 변환할 수 있는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF를 EPUB로 변환

{{% alert color="success" %}}
**PDF를 EPUB로 온라인 변환 시도**

Aspose.PDF for C++는 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)라는 무료 온라인 응용 프로그램을 제공하며, 여기에서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> (Electronic Publication의 약자)는 국제 디지털 출판 포럼(IDPF)에서 제공하는 무료 및 오픈 전자책 표준입니다. 파일 확장자는 .epub입니다.
EPUB는 가변적인 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 최적화된 텍스트를 제공할 수 있다는 것을 의미합니다. EPUB은 고정 레이아웃 콘텐츠도 지원합니다. 이 형식은 출판사와 변환 회사에서 내부적으로 사용할 수 있는 단일 형식으로 의도되었으며, 배포 및 판매를 위해서도 사용됩니다. 이는 Open eBook 표준을 대체합니다.

Aspose.PDF for C++는 PDF 문서를 EPUB 형식으로 변환하는 기능도 지원합니다. Aspose.PDF for C++에는 `EpubSaveOptions`라는 클래스가 있으며, 이를 [`Document.Save(..)`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 메서드의 두 번째 인수로 사용할 수 있어 EPUB 파일을 생성할 수 있습니다. C++로 이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용해 보십시오.

```cpp
void ConvertPDFtoEPUB()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 출력 파일 이름을 위한 문자열
    String outfilename("PDFToEPUB_out.epub");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // PDF 파일을 EPUB 형식으로 저장
    document->Save(_dataDir + outfilename, SaveFormat::Epub);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## PDF를 LaTeX/TeX로 변환

**Aspose.PDF for C++**는 PDF를 LaTeX/TeX로 변환하는 것을 지원합니다. LaTeX 파일 형식은 특별한 마크업이 포함된 텍스트 파일 형식이며, 고품질 조판을 위한 TeX 기반 문서 준비 시스템에서 사용됩니다.

PDF 파일을 TeX로 변환하기 위해, Aspose.PDF는 변환 과정에서 임시 이미지를 저장하기 위한 OutDirectoryPath 속성을 제공하는 클래스 [LaTeXSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.la_te_x_save_options)를 가지고 있습니다.

다음 코드 스니펫은 C++로 PDF 파일을 TEX 형식으로 변환하는 과정을 보여줍니다.

```cpp
void ConvertPDFtoLaTeX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 출력 파일 이름을 위한 문자열
    String outfilename("PDFToTeX_out.tex");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // LaTex 저장 옵션 인스턴스화
    auto saveOptions = MakeObject<LaTeXSaveOptions>();

    // 저장 옵션 객체를 위한 출력 디렉토리 경로 설정
    saveOptions->set_OutDirectoryPath(_dataDir);

    // PDF 파일을 LaTex 형식으로 저장
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**PDF를 LaTeX/TeX로 온라인 변환 시도**

Aspose.PDF for C++는 온라인 무료 애플리케이션 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF 변환 PDF를 LaTeX/TeX로 무료 앱으로 변환](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## PDF를 텍스트로 변환

**Aspose.PDF for C++**는 전체 PDF 문서와 단일 페이지를 텍스트 파일로 변환하는 것을 지원합니다.

### 전체 PDF 문서를 텍스트 파일로 변환

[TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/) 클래스를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다.

다음 코드 스니펫은 모든 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```cpp
void ConvertPDFDocToTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 출력 파일 이름을 위한 문자열
    String outfilename("input_Text_Extracted_out.txt");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();
    ta->Visit(document);
    // 추출된 텍스트를 텍스트 파일에 저장
    System::IO::File::WriteAllText(_dataDir + outfilename, ta->get_Text());
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### PDF 페이지를 텍스트 파일로 변환하기

Aspose.PDF for C++를 사용하여 PDF 문서를 TXT 파일로 변환할 수 있습니다. 이 작업을 해결하려면 [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/) 클래스를 사용해야 합니다.

다음 코드 조각은 특정 페이지에서 텍스트를 추출하는 방법을 설명합니다.

```cpp
void ConvertPDFPagestoTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample-4pages.pdf");
    // 출력 파일 이름을 위한 문자열
    String outfilename("sample-4pages_out.txt");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();

    auto pages = { 1, 3, 4 };
    try {
    for (auto page : pages)
    {
    ta->Visit(document->get_Pages()->idx_get(page));
    }
    // 추출된 텍스트를 텍스트 파일에 저장
    auto text = ta->get_Text();
    System::IO::File::WriteAllText(_dataDir + outfilename, text);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**PDF를 텍스트로 온라인으로 변환해 보세요**

Aspose.PDF for C++는 온라인 무료 애플리케이션 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)을 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![무료 앱으로 Aspose.PDF 변환 PDF를 텍스트로](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF를 XPS로 변환

**Aspose.PDF for C++**는 PDF 파일을 <abbr title="XML Paper Specification">XPS</abbr> 형식으로 변환할 수 있는 기능을 제공합니다. C++로 PDF 파일을 XPS 형식으로 변환하기 위해 제시된 코드 스니펫을 사용해 보세요.

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 관련이 있습니다. XML Paper Specification (XPS)은 이전에 Metro라는 코드명이 붙었으며 차세대 인쇄 경로(NGPP) 마케팅 개념을 포함하며, 문서 생성 및 보기를 Windows 운영 체제에 통합하려는 Microsoft의 이니셔티브입니다.

PDF 파일을 XPS로 변환하기 위해 Aspose.PDF는 XPS 파일을 생성하기 위해 [Document.Save(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 메서드의 두 번째 인수로 사용되는 클래스 [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xps_save_options)를 가지고 있습니다.

다음 코드 스니펫은 PDF 파일을 XPS 형식으로 변환하는 과정을 보여줍니다.

```cpp
void ConvertPDFtoXPS()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 출력 파일 이름을 위한 문자열
    String outfilename("PDFToXPS_out.xps");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // LaTex 저장 옵션 인스턴스화
    auto saveOptions = MakeObject<XpsSaveOptions>();

    // PDF 파일을 XPS 형식으로 저장
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**온라인에서 PDF를 SVG로 변환해보세요**

Aspose.PDF for C++는 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)라는 온라인 무료 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.


[![무료 앱으로 Aspose.PDF 변환 PDF to SVG](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}
