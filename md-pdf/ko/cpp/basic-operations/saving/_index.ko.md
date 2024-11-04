---
title: C++를 사용하여 PDF 문서 저장
linktitle: 저장
type: docs
weight: 30
url: /cpp/save-pdf-document/
description: Aspose.PDF for C++ 라이브러리를 사용하여 PDF 파일을 저장하는 방법을 배우세요.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 파일 시스템에 PDF 문서 저장

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스의 Save 메서드를 사용하여 생성되거나 조작된 PDF 문서를 파일 시스템에 저장할 수 있습니다.

```cpp
void SaveDocument()
{
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);
    // 일부 조작 수행, 예: 새로운 빈 페이지 추가
    document->get_Pages()->Add();
    document->Save(_dataDir + modifiedFileName);
}
```

## 스트림에 PDF 문서 저장

Save 메서드의 오버로드를 사용하여 생성되거나 조작된 PDF 문서를 스트림에 저장할 수도 있습니다.

```cpp
void SaveDocumentStream()
{
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);

    // 일부 조작 수행, 예: 새로운 빈 페이지 추가
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
    document->Save(fileStream);
}
```

## PDF/A 또는 PDF/X 형식으로 저장

PDF/A는 전자 문서의 보관 및 장기 보존을 위해 사용되는 휴대용 문서 형식(PDF)의 ISO 표준화 버전입니다. PDF/A는 폰트 연결(폰트 임베딩과 반대) 및 암호화와 같은 장기 보관에 적합하지 않은 기능을 금지한다는 점에서 PDF와 다릅니다. PDF/A 뷰어에 대한 ISO 요구 사항에는 색상 관리 지침, 임베디드 폰트 지원 및 임베디드 주석을 읽기 위한 사용자 인터페이스가 포함됩니다.

PDF/X는 PDF ISO 표준의 하위 집합입니다. PDF/X의 목적은 그래픽 교환을 용이하게 하는 것이며, 따라서 표준 PDF 파일에는 적용되지 않는 일련의 인쇄 관련 요구 사항이 있습니다.

두 경우 모두, [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options)를 사용하여 문서를 준비하는 동안 저장 방법을 사용하여 문서를 저장합니다.

```cpp
void SaveDocumentAsPDFx()
{
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\");

    // 파일 이름에 대한 문자열
    String infilename("SimpleResume.pdf");
    String outfilename("SimpleResume_A3U.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
    try
    {
        document->Convert(options);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what();
    }

    document->Save(_dataDir + outfilename);
}
```