---
title: PDF 파일에 텍스트 추가
linktitle: PDF 파일에 텍스트 추가
type: docs
weight: 10
url: ko/php-java/add-text-to-pdf-file/
description: 이 문서는 Aspose.PDF에서 텍스트 작업의 다양한 측면을 설명합니다. PDF에 텍스트를 추가하거나 HTML 조각을 추가하거나 사용자 지정 OTF 글꼴을 사용하는 방법을 알아보십시오.
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

기존 PDF 파일에 텍스트를 추가하려면:

1. Document 객체를 사용하여 입력 PDF를 엽니다.
1. 텍스트를 추가하려는 특정 페이지를 가져옵니다.
1. "Aspose.PDF"라는 내용의 텍스트 조각을 생성합니다.
1. 페이지에서 텍스트 조각의 위치를 설정합니다.
1. 텍스트 조각의 텍스트 속성을 설정합니다.
1. 페이지에 대한 TextBuilder 객체를 생성합니다.
1. PDF 페이지에 텍스트 조각을 추가합니다.
4. 결과 PDF 문서를 출력 파일로 저장합니다.

## 텍스트 추가

다음 코드 스니펫은 기존 PDF 파일에 텍스트를 추가하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    // 특정 페이지 가져오기
    $page = $document->getPages()->add();
    
    // 텍스트 조각 생성
    $textFragment = new TextFragment("Aspose.PDF");
    $textFragment->setPosition(new Position(80, 700));

    // 텍스트 속성 설정
    $fontRepository = new FontRepository();
    
    $colors = new Color();
    $textFragment->getTextState()->setFont($fontRepository->findFont("Verdana"));
    $textFragment->getTextState()->setFontSize(14);
    $textFragment->getTextState()->setForegroundColor($colors->getBlue());
    $textFragment->getTextState()->setBackgroundColor($colors->getLightGray());

    // TextBuilder 객체 생성
    $textBuilder = new TextBuilder($page);
    // PDF 페이지에 텍스트 조각 추가
    $textBuilder->appendText($textFragment);

    // 결과 PDF 문서 저장.    
    $document->save($outputFile);
    $document->close();
```