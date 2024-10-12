---
title: PDF에 페이지 스탬프 추가
linktitle: PDF 파일의 페이지 스탬프
type: docs
weight: 30
url: /cpp/page-stamps-in-the-pdf-file/
description: C++의 PdfPageStamp 클래스를 사용하여 PDF 파일에 페이지 스탬프 추가.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## C++로 페이지 스탬프 추가

[PdfPageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_page_stamp)는 그래픽, 텍스트, 테이블을 포함하는 복합 스탬프를 적용해야 할 때 사용될 수 있습니다. 다음 예제는 Adobe InDesign, Illustrator, Microsoft Word를 사용하는 것처럼 문구류를 생성하기 위해 스탬프를 사용하는 방법을 보여줍니다. 입력 문서가 있고 파란색과 자주색 색상의 두 가지 테두리를 적용하고 싶다고 가정합니다.

```cpp
void AddPageStamp()
{
    String _dataDir("C:\\Samples\\");

    String inputFileName ("sample-4pages.pdf");
    String outputFileName ("AddPageStamp_out.pdf");
    String pageStampFileName ("PageStamp.pdf");
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto bluePageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 1);
    bluePageStamp->set_Height(800);
    bluePageStamp->set_Background(true);

    auto plumPageStamp = MakeObject<PdfPageStamp>(_dataDir + pageStampFileName, 2);
    plumPageStamp->set_Height(800);
    plumPageStamp->set_Background(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document->get_Pages()->idx_get(i)->AddStamp(bluePageStamp);
        else
            document->get_Pages()->idx_get(i)->AddStamp(plumPageStamp);
    }

    document->Save(_dataDir + outputFileName);
}
```