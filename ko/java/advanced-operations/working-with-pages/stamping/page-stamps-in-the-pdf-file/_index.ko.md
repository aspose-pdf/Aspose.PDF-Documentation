---
title: PDF에 페이지 스탬프 추가
linktitle: PDF 파일의 페이지 스탬프
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: Java로 PdfPageStamp 클래스를 사용하여 PDF 파일에 페이지 스탬프 추가.
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Java로 페이지 스탬프 추가

[PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp)는 그래픽, 텍스트, 테이블을 포함하는 복합 스탬프를 적용해야 할 때 사용할 수 있습니다. 다음 예제는 Adobe InDesign, Illustrator, Microsoft Word를 사용할 때와 같이 문구류를 만드는 데 스탬프를 사용하는 방법을 보여줍니다. 입력 문서가 있으며 파란색과 자주색 두 종류의 테두리를 적용하고 싶다고 가정합니다.

```java
public static void AddPageStamp()
{
    String inputFileName = "sample-4pages.pdf";
    String outputFileName = "AddPageStamp_out.pdf";
    String pageStampFileName = "PageStamp.pdf";
    Document document = new Document(_dataDir + inputFileName);

    PdfPageStamp bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1);
    bluePageStamp.setHeight(800);
    bluePageStamp.setBackground(true);

    PdfPageStamp plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2);
    plumPageStamp.setHeight(800);
    plumPageStamp.setBackground(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.getPages().get_Item(i).addStamp(bluePageStamp);
        else
            document.getPages().get_Item(i).addStamp(plumPageStamp);
    }

    document.save(_dataDir + outputFileName);
}
```