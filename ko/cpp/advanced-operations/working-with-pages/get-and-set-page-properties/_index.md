---
title: 페이지 속성 가져오기 및 설정
type: docs
weight: 20
url: /ko/cpp/get-and-set-page-properties/
description: C++ 라이브러리를 사용하여 PDF 파일에서 페이지 속성을 가져오고 설정할 수 있습니다.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++**를 사용하면 C++ 애플리케이션에서 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다. 이 섹션에서는 PDF 파일의 페이지 수를 가져오는 방법, 색상과 같은 PDF 페이지 속성에 대한 정보를 가져오고 페이지 속성을 설정하며, PDF 파일의 특정 페이지를 가져오는 방법 등을 보여줍니다.

## PDF 파일의 페이지 수 가져오기

문서를 다룰 때, 종종 문서에 몇 페이지가 있는지 알고 싶습니다. Aspose.PDF를 사용하면 두 줄 이상의 코드로 이 작업을 수행할 수 있습니다.

PDF 파일의 페이지 수를 가져오려면:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스를 사용하여 PDF 파일을 엽니다.
1. [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션의 Count 속성(Document 객체에서)을 사용하여 문서의 총 페이지 수를 얻습니다.

다음 코드 스니펫은 PDF 파일의 페이지 수를 얻는 방법을 보여줍니다.

```cpp
void GetNumberOfPages() {
    // 문서 열기
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // 페이지 수 얻기
    std::cout << "Page Count : " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### 문서를 저장하지 않고 페이지 수 얻기

때때로 PDF 파일을 즉석에서 생성할 때 PDF 파일 생성 중에 시스템이나 스트림에 파일을 저장하지 않고 PDF 파일의 페이지 수를 얻어야 할 필요성(목차 생성 등)이 발생할 수 있습니다. 따라서 이러한 요구 사항을 충족하기 위해 Document 클래스에 [ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f) 메서드가 도입되었습니다. 문서를 저장하지 않고 페이지 수를 가져오는 단계를 보여주는 다음 코드 스니펫을 살펴보세요.

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // Document 인스턴스 생성
    auto document = MakeObject<Document>();

    // PDF 파일의 페이지 컬렉션에 페이지 추가
    auto page = document->get_Pages()->Add();
    // 루프 인스턴스 생성
    for (int i = 0; i < 300; i++)
        // 페이지 객체의 단락 컬렉션에 TextFragment 추가
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Pages count test"));
    // 정확한 페이지 수를 얻기 위해 PDF 파일의 단락 처리
    document->ProcessParagraphs();
    // 문서의 페이지 수 출력
    std::cout << "Number of pages in document = " << document->get_Pages()->get_Count();
}
```

## 페이지 속성 가져오기
### 페이지 속성 접근하기

[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 클래스는 특정 PDF 페이지와 관련된 모든 속성을 제공합니다. PDF 파일의 모든 페이지는 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) 컬렉션에 포함되어 있습니다.

그곳에서, 인덱스를 사용하여 개별 페이지 객체에 접근하거나, 컬렉션을 foreach 루프를 사용하여 반복하여 모든 페이지를 얻을 수 있습니다. 개별 페이지에 접근한 후, 우리는 그 속성을 얻을 수 있습니다. 다음 코드 스니펫은 페이지 속성을 얻는 방법을 보여줍니다.

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // 특정 페이지 가져오기
    auto pdfPage = document->get_Pages()->idx_get(1);
    // 페이지 속성 가져오기
    Console::WriteLine(u"ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Page Number : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotate : {0}", pdfPage->get_Rotate());
}
```