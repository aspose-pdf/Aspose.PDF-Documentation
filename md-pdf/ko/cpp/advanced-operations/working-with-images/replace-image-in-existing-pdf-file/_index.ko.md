---
title: 기존 PDF 파일에서 이미지 교체 C++ 사용
linktitle: 이미지 교체
type: docs
weight: 70
url: /cpp/replace-image-in-existing-pdf-file/
description: 이 섹션에서는 ++ 라이브러리를 사용하여 기존 PDF 파일에서 이미지를 교체하는 방법을 설명합니다.
lastmod: "2021-12-18"
---

Images 컬렉션의 Replace 메서드를 사용하면 기존 PDF 파일의 이미지를 교체할 수 있습니다.

Images 컬렉션은 페이지의 Resources 컬렉션에서 찾을 수 있습니다. 이미지를 교체하려면:

1. Document 객체를 사용하여 PDF 파일을 엽니다.
2. 특정 이미지를 교체하고, Document 객체의 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 PDF 파일에서 이미지를 교체하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceImage() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"input.pdf");
    // Replace a particular image
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Replace(1, System::IO::File::OpenRead(u"lovely.jpg"));
    // Save updated PDF file
    document->Save(_dataDir + u"output.pdf");
}
```