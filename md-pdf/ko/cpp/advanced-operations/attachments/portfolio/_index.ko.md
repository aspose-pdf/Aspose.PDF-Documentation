---
title: PDF 포트폴리오 작업
linktitle: 포트폴리오
type: docs
weight: 40
url: /cpp/portfolio/
description: Aspose.PDF for C++를 사용하여 PDF 포트폴리오를 만듭니다. Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 만들어야 합니다.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 포트폴리오 생성 방법

Aspose.PDF는 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스를 사용하여 PDF 포트폴리오 문서를 생성할 수 있습니다. [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) 클래스를 사용하여 파일을 가져온 후 Document.Collection 객체에 파일을 추가합니다. 파일이 추가되면 Document 클래스의 Save 메서드를 사용하여 포트폴리오 문서를 저장합니다.

다음 예제는 Microsoft Excel 파일, Word 문서 및 이미지 파일을 사용하여 PDF 포트폴리오를 생성합니다.

아래 코드는 다음 포트폴리오를 생성합니다.

### Aspose.PDF로 생성된 PDF 포트폴리오

![A PDF Portfolio created with Aspose.PDF for C++](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // 문서 객체 인스턴스화
    auto pdfDocument = MakeObject<Document>();

    // 문서 컬렉션 객체 인스턴스화
    pdfDocument->set_Collection(MakeObject<Collection>());

    // 포트폴리오에 추가할 파일 가져오기
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // 파일 설명 제공
    excel->set_Description(u"엑셀 파일");
    word->set_Description(u"워드 파일");
    image->set_Description(u"이미지 파일");

    // 문서 컬렉션에 파일 추가
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // 포트폴리오 문서 저장
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```

## PDF 포트폴리오에서 파일 추출

PDF 포트폴리오는 다양한 소스(예: PDF, Word, Excel, JPEG 파일)의 콘텐츠를 하나의 통합된 컨테이너로 결합할 수 있게 합니다. 원본 파일은 개별적인 정체성을 유지하면서도 PDF 포트폴리오 파일로 조립됩니다. 사용자는 각 구성 요소 파일을 다른 구성 요소 파일과 독립적으로 열고, 읽고, 편집하고, 형식을 지정할 수 있습니다.

Aspose.PDF는 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스를 사용하여 PDF 포트폴리오 문서를 생성하는 기능을 제공합니다. 또한 PDF 포트폴리오에서 파일을 추출하는 기능도 제공합니다.

다음 코드 스니펫은 PDF 포트폴리오에서 파일을 추출하는 단계를 보여줍니다.

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // 내장 파일의 컬렉션 가져오기
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // 포트폴리오의 개별 파일을 반복
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // 추출된 파일을 일부 위치에 저장
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // 스트림 객체 닫기
    fileStream->Close();
    }
}
```

![PDF 포트폴리오에서 파일 추출](working-with-pdf-portfolio_2.jpg)

## PDF 포트폴리오에서 파일 제거

PDF 포트폴리오에서 파일을 삭제/제거하려면 다음 코드 라인을 사용해 보세요.

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // 소스 PDF 포트폴리오 로드
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```