---
title: PDF 파일 메타데이터
type: docs
weight: 20
url: /ko/cpp/pdf-file-metadata/
---

## PDF 파일 정보 가져오기/설정하기

PDF 파일의 파일별 정보를 얻으려면 먼저 Document 클래스의 **get_Info()** 메서드를 호출해야 합니다. DocumentInfo 객체가 검색되면 개별 속성의 값을 얻을 수 있습니다. 또한, DocumentInfo 클래스의 해당 메서드를 사용하여 속성을 설정할 수도 있습니다. 다음 코드 스니펫은 Aspose.PDF for C++를 사용하여 PDF 파일 정보를 가져오고 설정하는 방법을 보여줍니다:

{{% alert color="primary" %}}

**Application** 및 **Producer** 필드에 대한 값을 설정할 수 없으며, Aspose Ltd. 및 Aspose.PDF for C++ x.x.x가 이러한 필드에 표시될 것임을 유의하십시오.

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // 문서 정보 가져오기
    auto docInfo = pdfDocument->get_Info();
    // 문서 정보 표시
    Console::WriteLine(u"Author: {0}", docInfo->get_Author());
    Console::WriteLine(u"Creation Date: {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Keywords: {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Modify Date: {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Subject: {0}", docInfo->get_Subject());
    Console::WriteLine(u"Title: {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // 문서 정보 지정
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"PDF Information");
    docInfo->set_Title (u"Setting PDF Document Information");

    // 출력 문서 저장
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```

## PDF 파일에서 XMP 메타데이터 가져오기/설정하기

Aspose.PDF for C++를 사용하면 PDF 파일의 XMP 메타데이터에 접근하고 설정할 수 있습니다. PDF 파일의 메타데이터를 가져오거나 설정하려면 다음과 같이 하십시오:

1. Document 객체를 생성하고 입력 PDF 파일을 엽니다.
1. 각각의 메소드를 사용하여 파일의 메타데이터를 가져오거나 설정합니다.

다음 코드 스니펫은 PDF 파일에서 메타데이터를 가져오거나 설정하는 방법을 보여줍니다.

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // 속성 가져오기
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // 속성 설정
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // 문서 저장
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // xmlns 접두사가 제거됨
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // 문서 저장
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```