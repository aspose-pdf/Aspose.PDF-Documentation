---
title: PDF에서 단락 추출
linktitle: 단락 추출
type: docs
weight: 20
url: /php-java/extract-paragraph-from-pdf/
description: 이 문서는 Aspose.PDF의 특별한 도구인 ParagraphAbsorber를 사용하여 PDF 문서에서 텍스트를 추출하는 방법을 설명합니다.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서에서 단락 형태로 텍스트 추출

우리는 특정 텍스트("평문" 또는 "정규 표현식" 사용)를 단일 페이지나 전체 문서에서 검색하여 PDF 문서에서 텍스트를 얻거나, 단일 페이지, 페이지 범위 또는 전체 문서의 전체 텍스트를 얻을 수 있습니다. 그러나 경우에 따라 PDF 문서에서 단락을 추출하거나 단락 형태로 텍스트를 추출해야 할 수도 있습니다. 우리는 PDF 문서 페이지의 텍스트에서 섹션과 단락을 검색하는 기능을 구현했습니다. 우리는 PDF 문서에서 단락을 추출하는 데 사용할 수 있는 ParagraphAbsorber 클래스를 도입했습니다(마치 TextFragmentAbsorber 및 TextAbsorber 처럼).

### 단락 컬렉션을 반복하고 그들의 텍스트 얻기

```php

// 기존 PDF 파일 열기
$document = new Document($inputFile);
// ParagraphAbsorber 인스턴스화
$absorber = new ParagraphAbsorber();
$absorber->visit($document);
$responseData = "";

foreach ($absorber->getPageMarkups() as $markup) {
    $i = 1;

    foreach ($markup->getSections() as $section) {
        $j = 1;

        foreach ($section->getParagraphs() as $paragraph) {
            $paragraphText = "\r\n";

            foreach ($paragraph->getLines() as $line) {
                foreach ($line as $fragment) {
                    $paragraphText = $paragraphText . $fragment->getText();
                }
                $paragraphText = $paragraphText . "\r\n";
            }
            $paragraphText = $paragraphText . "\r\n";

            $responseData = $responseData . "섹션 " . $i++ . "의 문단 " . $j++ . " 페이지에서" . ":" . markup->getNumber();
            $responseData = $responseData . $paragraphText;
            $j++;
        }
        $i++;
    }
}

// 추출된 텍스트를 출력 파일에 저장
file_put_contents($outputFile, $responseData);
```