---
title: PDF를 PDF/A 형식으로 변환
linktitle: PDF를 PDF/A 형식으로 변환
type: docs
weight: 100
url: ko/cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: 이 주제는 Aspose.PDF가 PDF 파일을 PDF/A 호환 PDF 파일로 변환할 수 있는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++**를 사용하면 PDF 파일을 <abbr title="Portable Document Format / A">PDF/A</abbr> 호환 PDF 파일로 변환할 수 있습니다. 이를 수행하기 전에 파일을 검증해야 합니다. 이 주제에서는 그 방법을 설명합니다.

{{% alert color="primary" %}}

PDF/A 적합성을 검증하기 위해 Adobe Preflight을 따르고 있음을 유의하십시오. 시장의 모든 도구는 PDF/A 적합성에 대한 자체 "표현"을 가지고 있습니다. 참조용으로 PDF/A 검증 도구에 관한 이 기사를 확인하십시오. 우리는 Aspose.PDF가 PDF 파일을 생성하는 방식을 검증하기 위해 Adobe 제품을 선택했습니다. 왜냐하면 Adobe가 PDF와 관련된 모든 것의 중심에 있기 때문입니다.

{{% /alert %}}

파일을 변환하려면 Document 클래스의 Convert 메서드를 사용하십시오. PDF를 PDF/A 준수 파일로 변환하기 전에 Validate 메서드를 사용하여 PDF를 검증하세요. 검증 결과는 XML 파일에 저장되며, 이 결과는 Convert 메서드에도 전달됩니다. ConvertErrorAction 열거형을 사용하여 변환할 수 없는 요소에 대한 작업을 지정할 수도 있습니다.

## PDF 파일을 PDF/A-1b로 변환하기

다음 코드는 PDF 파일을 PDF/A-1b 준수 PDF로 변환하는 방법을 보여줍니다.

```cpp
void ConverttoPDFA_1b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 로그 파일 이름을 위한 문자열
    String logfilename("log.xml");
    // 출력 파일 이름을 위한 문자열
    String outfilename("PDFToPDFA_out.pdf");

    // 문서 열기
    auto document = new Document(_dataDir + infilename);

    // PDF/A 준수 문서로 변환
    // 변환 과정에서 검증도 수행됩니다
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

    // 출력 문서 저장
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
문서의 유효성 검사만 수행하려면 다음 코드 줄을 사용하십시오:

```cpp
void ConverttoPDFA_1b_Validation()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 로그 파일 이름을 위한 문자열
    String logfilename("log.xml");

    // 문서 열기
    auto document = new Document(_dataDir + infilename);

    // PDF/A 호환 문서로 변환
    // 변환 과정에서 유효성 검사도 수행됩니다
    document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF 파일을 PDF/A-3b로 변환

Aspose.PDF for C++는 또한 PDF 파일을 PDF/A-3b 형식으로 변환하는 기능을 지원합니다.

```cpp
void ConverttoPDFA_3b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 로그 파일 이름을 위한 문자열
    String logfilename("log.xml");
    // 출력 파일 이름을 위한 문자열
    String outfilename("PDFToPDFA3b_out.pdf");

    // 문서 열기
    auto document = new Document(_dataDir + infilename);

    // PDF/A 호환 문서로 변환
    // 변환 과정에서 유효성 검사도 수행됩니다
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

    // 출력 문서 저장
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF 파일을 PDF/A-2u로 변환

Aspose.PDF for C++는 PDF 파일을 PDF/A-2u 형식으로 변환하는 기능을 지원합니다.

```cpp
void ConverttoPDFA_2u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로명에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일명에 대한 문자열
     String infilename("sample.pdf");
    // 로그 파일명에 대한 문자열
    String logfilename("log.xml");
    // 출력 파일명에 대한 문자열
    String outfilename("PDFToPDFA3b_out.pdf");

    // 문서 열기
    auto document = new Document(_dataDir + infilename);

    // PDF/A 호환 문서로 변환
    // 변환 과정에서 유효성 검사도 수행됩니다
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // 출력 문서 저장
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF 파일을 PDF/A-3u로 변환

Aspose.PDF for C++는 PDF 파일을 PDF/A-3u 형식으로 변환하는 기능을 지원합니다.

```cpp
void ConverttoPDFA_3u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 로그 파일 이름을 위한 문자열
    String logfilename("log.xml");
    // 입력 파일 이름을 위한 문자열
    String outfilename("PDFToPDFA3b_out.pdf");

    // 문서 열기
    auto document = new Document(_dataDir + infilename);

    // PDF/A 호환 문서로 변환
    // 변환 과정 중에 유효성 검사도 수행됩니다
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // 출력 문서 저장
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF/A 파일에 첨부 파일 추가

PDF/A 호환 형식에 파일을 첨부해야 하는 경우 Aspose.PDF.PdfFormat 열거형에서 PDF_A_3A 값을 사용하는 것을 권장합니다.

PDF/A_3a는 PDF/A 호환 파일에 첨부 파일로 어떤 파일 형식이든 첨부할 수 있는 기능을 제공하는 형식입니다.

```cpp
void ConverttoPDFA_AddAttachment()
{
    std::clog << __func__ << ": 시작" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 로그 파일 이름을 위한 문자열
    String logfilename("log.xml");
    // 입력 파일 이름을 위한 문자열
    String outfilename("PDFToPDFA3b_out.pdf");

    // 문서 열기
    auto document = new Document(_dataDir + infilename);

    // 첨부 파일로 추가할 새 파일 설정
    auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("큰 이미지 파일"));
    // 문서의 첨부 파일 컬렉션에 첨부 파일 추가
    document->get_EmbeddedFiles()->Add(fileSpecification);

    // PDF/A 호환 문서로 변환
    // 변환 과정 중에 검증도 수행됩니다
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

    // 출력 문서 저장
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": 완료" << std::endl;
}
```

## 누락된 글꼴을 대체 글꼴로 교체

PDFA 표준에 따르면, 글꼴은 PDFA 문서에 포함되어야 합니다. 그러나 글꼴이 소스 문서에 포함되어 있지 않거나 컴퓨터에 존재하지 않는 경우 PDFA는 유효성 검사를 통과하지 못합니다. 이 경우, 우리는 컴퓨터에 있는 일부 대체 글꼴로 누락된 글꼴을 대체해야 합니다. PDF를 PDFA로 변환하는 동안 SimpleFontSubsituation 메서드를 사용하여 누락된 글꼴을 대체할 수 있습니다.

```cpp
void ConverttoPDFA_ReplaceFont()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.pdf");
    // 로그 파일 이름을 위한 문자열
    String logfilename("log.xml");
    // 출력 파일 이름을 위한 문자열
    String outfilename("PDFToPDFA3b_out.pdf");

    // 문서 열기
    auto document = new Document(_dataDir + infilename);

    System::SharedPtr<Aspose::Pdf::Text::Font> originalFont;
    try
    {
        originalFont = FontRepository::FindFont(String("AgencyFB"));
    }
    catch (Exception)
    {
        // 대상 컴퓨터에서 글꼴이 누락됨
        auto substitutions = FontRepository::get_Substitutions();
        auto substitution = MakeObject<SimpleFontSubstitution>(String("AgencyFB"), String("Helvetica"));
        substitutions->Add(substitution);
    }

    // PDF/A 준수 문서로 변환
    try {
        // 변환 과정에서 유효성 검사도 수행됩니다.
        document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

        // 출력 문서 저장
        document->Save(_dataDir + outfilename);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```


{{% alert color="primary" %}}
**PDF를 PDF/A로 온라인 변환 시도하기**

Aspose.PDF for C++는 온라인 무료 애플리케이션 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)를 제공합니다. 여기서 기능성과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}
```