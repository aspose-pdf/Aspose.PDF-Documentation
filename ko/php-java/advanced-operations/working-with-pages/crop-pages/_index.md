---
title: PHP를 사용하여 PDF 페이지 자르기
linktitle: 페이지 자르기
type: docs
weight: 80
url: /ko/php-java/crop-pages/
description: Aspose.PDF for PHP via Java를 사용하여 페이지의 너비, 높이, 여백 상자, 자르기 상자 및 재단 상자와 같은 페이지 속성을 가져올 수 있습니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 페이지 속성 가져오기

PDF 파일의 각 페이지는 너비, 높이, 여백 상자, 자르기 상자 및 재단 상자와 같은 여러 속성을 가지고 있습니다. Aspose.PDF for PHP via Java는 이러한 속성에 접근할 수 있도록 합니다.

- **미디어 상자**: 미디어 상자는 가장 큰 페이지 상자입니다. 이는 문서를 PostScript 또는 PDF로 인쇄할 때 선택된 페이지 크기(예: A4, A5, 미국 레터 등)에 해당합니다. 다시 말해, 미디어 상자는 PDF 문서가 표시되거나 인쇄되는 매체의 물리적 크기를 결정합니다.
- **여백 상자**: 문서에 여백이 있는 경우 PDF에도 여백 상자가 있습니다.
 블리드는 페이지 가장자리를 넘어 확장된 색상(또는 작품)의 양입니다. 이는 문서가 인쇄되고 크기에 맞게 잘렸을 때("자름") 잉크가 페이지 가장자리까지 도달하도록 하기 위해 사용됩니다. 페이지가 잘못 잘려 - 자름 표시에서 약간 벗어나 잘린 경우에도 - 페이지에 흰색 가장자리가 나타나지 않습니다.
- **트림 박스**: 트림 박스는 인쇄 및 트림 후 문서의 최종 크기를 나타냅니다.
- **아트 박스**: 아트 박스는 문서의 실제 페이지 내용 주위에 그려진 상자입니다. 이 페이지 박스는 다른 애플리케이션에서 PDF 문서를 가져올 때 사용됩니다.
- **크롭 박스**: 크롭 박스는 Adobe Acrobat에서 PDF 문서가 표시되는 "페이지" 크기입니다. 일반 보기에서는 Adobe Acrobat에서 크롭 박스의 내용만 표시됩니다. 이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **페이지.Rect**: 미디어박스와 드롭박스의 교차점(일반적으로 보이는 직사각형). 아래 그림은 이러한 속성을 설명합니다. 자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

아래 스니펫은 페이지를 자르는 방법을 보여줍니다:

```php

    // 문서 열기
    $document = new Document($inputFile);      

    $page = $document->getPages()->get_Item(1);

    $responseData = $page->getCropBox() . PHP_EOL;
    $responseData = $responseData . $page->getTrimBox() . PHP_EOL;
    $responseData = $responseData . $page->getArtBox() . PHP_EOL;
    $responseData = $responseData . $page->getBleedBox() . PHP_EOL;
    $responseData = $responseData . $page->getMediaBox() . PHP_EOL;

    // 새로운 Box 사각형 생성
    $newBox = new Rectangle(200, 220, 2170, 1520);

    $page->setCropBox($newBox);
    $page->setTrimBox($newBox);
    $page->setArtBox($newBox);
    $page->setBleedBox($newBox);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```

이 예제에서는 [여기](crop_page.pdf)의 샘플 파일을 사용했습니다. 처음에 우리의 페이지는 그림 1과 같이 보입니다.  
![Figure 1. Cropped Page](crop_page.png)

변경 후, 페이지는 그림 2와 같이 보일 것입니다.  
![Figure 2. Cropped Page](crop_page2.png)