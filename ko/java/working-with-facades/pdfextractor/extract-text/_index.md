---
title: PDF에서 이미지 추출하기 (facades)
type: docs
weight: 30
url: ko/java/extract-images/
description: 이 섹션에서는 PdfExtractor 클래스를 사용하여 Aspose.PDF Facades로 이미지를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) 클래스는 PDF 파일에서 이미지를 추출할 수 있도록 합니다.
 먼저, [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) 클래스의 객체를 생성하고 bindPdf 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) 메서드를 호출하여 모든 이미지를 메모리로 추출합니다. 이미지가 추출되면, hasNextImage 및 getNextImage 메서드를 사용하여 해당 이미지를 얻을 수 있습니다. while 루프를 사용하여 추출된 모든 이미지를 반복해야 합니다. 이미지를 디스크에 저장하려면 파일 경로를 인수로 받는 getNextImage 메서드의 오버로드를 호출할 수 있습니다. 다음 코드 스니펫은 전체 PDF에서 이미지를 파일로 추출하는 방법을 보여줍니다.

```java   
public static void ExtractImages()
 {
    //추출기를 생성하고 문서에 바인딩
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    //추출기 실행
    extractor.extractImage();
    int imageNumber = 1;
    //추출된 이미지 컬렉션을 반복
    while (extractor.hasNextImage())
    {
        //컬렉션에서 이미지를 가져와 파일에 저장
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++),ImageType.getPng());
    }
}
```