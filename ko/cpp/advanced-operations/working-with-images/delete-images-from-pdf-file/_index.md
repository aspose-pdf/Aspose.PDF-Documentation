---
title: PDF 파일에서 이미지 삭제하기 C++ 사용
linktitle: 이미지 삭제
type: docs
weight: 20
url: /ko/cpp/delete-images-from-pdf-file/
description: 이 섹션은 Aspose.PDF for C++를 사용하여 PDF 파일에서 이미지를 삭제하는 방법을 설명합니다.
lastmod: "2021-12-18"
---

PDF 파일에서 이미지를 삭제하려면:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 만들고 입력 PDF 파일을 엽니다.
1. Document 객체의 [Pages collection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection)에서 이미지를 포함하는 페이지를 가져옵니다.
1. 이미지는 페이지의 Resources 컬렉션에 있는 Images 컬렉션에 저장됩니다.
1. Images 컬렉션의 Delete 메서드를 사용하여 이미지를 삭제합니다.
1. Document 객체의 Save 메서드를 사용하여 출력 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일에서 이미지를 삭제하는 방법을 보여줍니다.

```cpp
void WorkingWithImages::DeleteImagesFromPDFFile()
{
    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"DeleteImages.pdf");

    // 특정 이미지 삭제
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);

    // 업데이트된 PDF 파일 저장
    document->Save(_dataDir + u"DeleteImages_out.pdf");
}
```