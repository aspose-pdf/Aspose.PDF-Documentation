---
title: PDF 문서 만들기
linktitle: PDF 만들기
type: docs
weight: 10
url: /cpp/create-pdf-document/
description: 이 글은 C++용 Aspose.PDF를 사용하여 PDF 문서를 만들고 형식화하는 방법을 설명합니다.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

우리는 항상 C++ 프로젝트에서 PDF 문서를 생성하고 보다 정확하고 효율적으로 작업할 수 있는 방법을 찾고 있습니다. 라이브러리에서 사용하기 쉬운 기능을 통해 C++에서 PDF를 생성하려고 시도하는 시간 소모적인 세부 사항에 더 적은 시간을 투자하고 더 많은 작업을 추적할 수 있습니다.

## C++를 사용하여 PDF 생성

Aspose.PDF for C++ API를 사용하면 C++를 사용하여 PDF 파일을 생성하고 읽을 수 있습니다. 이 API는 WinForms를 비롯한 다양한 C++ 응용 프로그램에서 사용할 수 있습니다. 이 글에서는 C++ 응용 프로그램에서 PDF 파일을 쉽게 생성하고 읽을 수 있도록 Aspose.PDF for C++ API를 사용하는 방법을 보여드리겠습니다.

### 간단한 PDF 파일 생성 방법

C++를 사용하여 PDF 파일을 생성하려면 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스의 객체를 생성합니다.
1. Document 객체의 'Pages' 컬렉션에 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 객체를 추가합니다.
1. 페이지의 [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) 컬렉션에 [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)를 추가합니다.
1. 결과 PDF 문서를 저장합니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // 경로 이름에 대한 문자열.
    String _dataDir("C:\\Samples\\");

    // 파일 이름에 대한 문자열.
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // 새 페이지에 텍스트 추가
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // 업데이트된 PDF 저장
    document->Save(_dataDir + outputFileName);
}
```
## 검색 가능한 PDF 문서 만들기

Aspose.PDF for C++를 사용하면 처음부터 PDF를 만들고 기존 PDF를 조작할 수 있습니다. PDF에 텍스트 요소를 추가할 때 결과 PDF는 검색 가능합니다. 그러나 텍스트가 포함된 이미지를 PDF 파일로 변환하면 PDF 내의 콘텐츠는 검색할 수 없습니다. 그러나 해결 방법으로, 결과 파일에 OCR을 사용하여 검색 가능하게 만들 수 있습니다. 따라서 먼저 시스템에 Tesseract-OCR을 설치해야 하며, tesseract 콘솔 응용 프로그램을 사용할 수 있습니다.

다음은 이 요구 사항을 달성하기 위한 전체 코드입니다:

```cpp
void CreateSearchableDocument() {
    // 경로 이름에 대한 문자열입니다.
    String _dataDir("C:\\Samples\\");
    // 파일 이름에 대한 문자열입니다.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();

    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;
}
```