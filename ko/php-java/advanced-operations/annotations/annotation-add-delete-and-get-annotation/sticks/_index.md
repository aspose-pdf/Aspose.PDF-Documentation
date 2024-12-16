---
title: PDF 스티키 주석
linktitle: 스티키 주석
type: docs
weight: 50
url: /ko/php-java/sticky-annotations/
description: 이 주제는 스티키 주석에 대한 것으로, 예시로 텍스트에 워터마크 주석을 보여줍니다. 페이지에 그래픽을 나타내는 데 사용됩니다. 이 작업을 해결하기 위한 코드 스니펫을 확인하세요.
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 워터마크 주석 추가

워터마크 주석은 인쇄된 페이지의 크기에 관계없이 페이지에 고정된 크기와 위치로 인쇄되어야 하는 그래픽을 나타내는 데 사용됩니다.

[WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation)을 사용하여 PDF 페이지의 특정 위치에 워터마크 텍스트를 추가할 수 있습니다. 워터마크의 불투명도는 opacity 속성을 사용하여 제어할 수 있습니다.

워터마크 주석을 추가하기 위한 다음 코드 스니펫을 확인하세요.

```php

    // 문서 열기
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // 특정 페이지 가져오기
    $page = $document->getPages()->get_Item(1);
    
    // 주석 생성
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    // 주석을 페이지의 주석 컬렉션에 추가
    $page->getAnnotations()->add($wa);

    // 글꼴 설정을 위한 TextState 생성
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    // 주석 텍스트의 불투명도 수준 설정
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "Watermark", "Demo"];
    // 주석에 텍스트 추가
    $wa->setTextAndState($watermarkStrings, $ts);

    // 결과 PDF 문서 저장
    $document->save($outputFile);
    $document->close();
```