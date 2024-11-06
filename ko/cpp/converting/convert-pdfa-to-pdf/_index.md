---
title: PDF/A를 PDF 형식으로 변환
linktitle: PDF/A를 PDF 형식으로 변환
type: docs
weight: 110
url: ko/cpp/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: 이 주제는 C++ 라이브러리를 사용하여 Aspose.PDF가 PDF/A 파일을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/A 문서를 PDF로 변환하기

PDF/A 문서를 PDF로 변환하는 것은 원본 문서에서 <abbr title="Portable Document Format Archive">PDF/A</abbr> 제한을 제거하는 것을 의미합니다. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스에는 입력/소스 파일에서 PDF 준수 정보를 제거하는 'RemovePdfaCompliance' 메서드가 있습니다. 입력 파일을 [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)한 후에.

```cpp
void ConvertPDFAtoPDF()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);

    // Remove PDF/A compliance information
    document->RemovePdfaCompliance();

    // Save updated document
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```

이 정보는 문서에 변경 사항(예: 페이지 추가)을 가하면 제거됩니다. 다음 예제에서 출력 문서는 페이지 추가 후 PDF/A 준수성을 잃습니다.

```cpp
void ConvertPDFAtoPDFAdvanced()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    // 새로운 (빈) 페이지를 추가하면 PDF/A 준수 정보가 제거됩니다.

    document->get_Pages()->Add();
    // 업데이트된 문서 저장
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```