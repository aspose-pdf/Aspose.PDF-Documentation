---
title: 첨부 파일 추출 및 저장
linktitle: 첨부 파일 추출 및 저장
type: docs
weight: 20
url: ko/cpp/extract-and-save-an-attachment/
description: Aspose.PDF for C++를 사용하면 PDF 문서에서 모든 첨부 파일을 얻을 수 있습니다. 또한, 문서에서 개별 첨부 파일을 추출할 수 있습니다.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 모든 첨부 파일 가져오기

Aspose.PDF를 사용하면 PDF 문서에서 모든 첨부 파일을 얻을 수 있습니다. 이는 PDF 문서에서 첨부 파일을 별도로 저장하거나 PDF에서 첨부 파일을 제거해야 할 때 유용합니다.

PDF 파일에서 모든 첨부 파일을 얻으려면:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) 컬렉션을 순회합니다. [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) 컬렉션에는 모든 첨부 파일이 포함되어 있습니다. 이 컬렉션의 각 요소는 [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) 객체를 나타냅니다. [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) 컬렉션을 통한 foreach 루프의 각 반복은 [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) 객체를 반환합니다.
1. 객체가 사용 가능해지면 첨부된 파일의 모든 속성이나 파일 자체를 검색합니다.

다음 코드 조각은 PDF 문서에서 모든 첨부 파일을 가져오는 방법을 보여줍니다.

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // 문서 열기
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // 임베디드 파일 컬렉션 가져오기
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // 임베디드 파일 개수 가져오기
 Console::WriteLine(u"Total files : {0}", embeddedFiles->get_Count());

 int count = 1;

 // 컬렉션을 순회하여 모든 첨부 파일 가져오기
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

  // 매개변수 객체가 매개변수를 포함하는지 확인
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"CheckSum: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Creation Date: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Modification Date: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Size: {0}", fileSpecification->get_Params()->get_Size());
  }

  // 첨부 파일을 가져와 파일 또는 스트림에 쓰기
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```
## 개별 첨부 파일 가져오기

개별 첨부 파일을 가져오기 위해서는 Document 인스턴스의 `EmbeddedFiles` 객체에서 첨부 파일의 인덱스를 지정할 수 있습니다. 다음 코드 스니펫을 사용해 보세요.

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // 특정 내장 파일 가져오기
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // 파일 속성 가져오기
    Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

    // 매개변수 객체가 매개변수를 포함하는지 확인
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"CheckSum: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"Creation Date: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"Modification Date: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"Size: {0}",
        fileSpecification->get_Params()->get_Size());
    }

    // 첨부 파일 가져오기 및 파일 또는 스트림에 쓰기
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```