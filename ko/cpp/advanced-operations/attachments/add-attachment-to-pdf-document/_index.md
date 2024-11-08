---
title: PDF 문서에 첨부 파일 추가
linktitle: PDF 문서에 첨부 파일 추가
type: docs
weight: 10
url: /ko/cpp/add-attachment-to-pdf-document/
description: 이 페이지는 Aspose.PDF for C++ 라이브러리를 사용하여 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

첨부 파일은 다양한 정보를 포함할 수 있으며 다양한 파일 유형이 될 수 있습니다. 이 문서에서는 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다.

1. 새 C++ 프로젝트를 만듭니다.
1. Aspose.PDF DLL에 대한 참조를 추가합니다.
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 만듭니다.
1. 추가할 파일과 파일 설명을 포함한 [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) 객체를 만듭니다.
1. [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) 객체를 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) 컬렉션에 컬렉션의 Add 메서드를 사용하여 추가합니다.

[EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) 컬렉션에는 PDF 파일의 모든 첨부 파일이 포함되어 있습니다. 다음 코드 스니펫은 PDF 문서에 첨부 파일을 추가하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{

String _dataDir("C:\\Samples\\");


// 문서 열기

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");


// 첨부 파일로 추가될 새 파일 설정

auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"샘플 텍스트 파일");


// 문서의 첨부 파일 컬렉션에 첨부 파일 추가

pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);


// 새로운 출력 저장

pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```