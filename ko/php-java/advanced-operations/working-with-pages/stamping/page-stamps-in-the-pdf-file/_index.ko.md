---
title: PDF에 PDF 페이지 스탬프 추가
linktitle: PDF 파일의 페이지 스탬프
type: docs
weight: 30
url: /php-java/page-stamps-in-the-pdf-file/
description: PHP에서 PdfPageStamp 클래스를 사용하여 PDF 파일에 페이지 스탬프 추가.
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 페이지 스탬프 추가

[PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp)는 그래픽, 텍스트, 테이블을 포함하는 복합 스탬프를 적용해야 할 때 사용될 수 있습니다. 다음 예제는 Adobe InDesign, Illustrator, Microsoft Word를 사용하는 것과 같이 문구류를 생성하기 위해 스탬프를 사용하는 방법을 보여줍니다. 입력 문서가 있고 파란색과 자두색 두 가지 테두리를 적용하고 싶다고 가정합니다.

```php

    // 문서 열기
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();  
```