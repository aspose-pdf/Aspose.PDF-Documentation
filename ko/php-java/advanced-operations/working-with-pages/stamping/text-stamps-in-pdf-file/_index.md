---
title: PDF에 텍스트 스탬프 프로그래밍 방식으로 추가
linktitle: PDF 파일의 텍스트 스탬프
type: docs
weight: 20
url: /ko/php-java/text-stamps-in-the-pdf-file/
description: PHP로 TextStamp 클래스를 사용하여 PDF 파일에 텍스트 스탬프를 추가합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Java로 텍스트 스탬프 추가

Aspose.PDF for PHP via Java는 PDF 파일에 텍스트 스탬프를 추가하기 위해 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 클래스를 제공합니다.
 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 클래스는 도장 객체에 대한 글꼴 크기, 글꼴 스타일, 글꼴 색상 등을 지정하기 위한 필요한 메서드를 제공합니다. 텍스트 도장을 추가하려면 먼저 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체와 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 객체를 필요한 메서드를 사용하여 생성해야 합니다. 그런 다음, [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스의 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 메서드를 호출하여 PDF 문서에 도장을 추가할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 텍스트 도장을 추가하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();
    // 텍스트 도장 생성
    $textStamp = new TextStamp("Sample Stamp");
    // 도장이 배경인지 설정
    $textStamp->setBackground(true);
    // 원점 설정
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // 도장 회전
    $textStamp->setRotate((new Rotation())->On90);    
    // 텍스트 속성 설정
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // 특정 페이지에 도장 추가
    $pages->get_Item(1)->addStamp($textStamp);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```

## TextStamp 객체의 정렬 정의

PDF 문서에 워터마크를 추가하는 것은 자주 요구되는 기능 중 하나이며, Aspose.PDF for PHP via Java는 이미지 및 텍스트 워터마크를 추가하는 기능을 완벽하게 지원합니다. [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 클래스는 PDF 파일에 텍스트 스탬프를 추가하는 기능을 제공합니다. 최근에는 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 객체를 사용할 때 텍스트의 정렬을 지정하는 기능을 지원해야 한다는 요구가 있었습니다. 그래서 이 요구를 충족시키기 위해, 우리는 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 클래스에 setTextAlignment(..) 메서드를 도입했습니다. 이 메서드를 사용하면 수평 텍스트 정렬을 지정할 수 있습니다.

다음 코드 스니펫은 기존 PDF 문서를 로드하고 그 위에 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)를 추가하는 예제를 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // 샘플 문자열로 FormattedText 객체 인스턴스화
    $text = new FormattedText("This");

    // FormattedText에 새로운 텍스트 줄 추가
    $text->addNewLineText("is sample");
    $text->addNewLineText("Center Aligned");
    $text->addNewLineText("TextStamp");
    $text->addNewLineText("Object");
    
    // 텍스트 스탬프 생성
    $textStamp = new TextStamp($text);

    // 텍스트 스탬프의 수평 정렬을 중앙 정렬로 지정
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // 텍스트 스탬프의 수직 정렬을 중앙 정렬로 지정
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // TextStamp의 텍스트 수평 정렬을 중앙 정렬로 지정
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // 스탬프 객체의 상단 여백 설정
    $textStamp->setTopMargin(20);
    
    // 특정 페이지에 스탬프 추가
    $pages->get_Item(1)->addStamp($textStamp);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();  
```


## PDF 파일에 스탬프로 채우기 및 스트로크 텍스트

텍스트 추가 및 편집 시나리오에 대한 렌더링 모드 설정을 구현했습니다. 스트로크 텍스트를 렌더링하려면 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) 객체를 생성하고 RenderingMode를 TextRenderingMode.StrokeText로 설정하고 StrokingColor 속성의 색상을 선택하십시오. 나중에 bindTextState() 메서드를 사용하여 스탬프에 TextState를 바인딩하십시오.

다음 코드 스니펫은 채우기 스트로크 텍스트 추가를 보여줍니다:

```php

   // 고급 속성을 전송하기 위한 TextState 객체 생성
    $ts = new TextState();
        
    // 스트로크 색상 설정
    $ts->setStrokingColor((new Color())->getGray());

    // 텍스트 렌더링 모드 설정
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // 입력 PDF 문서 로드
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAID IN FULL",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // TextState 바인딩
    $stamp->bindTextState($ts);
    
    // X, Y 원점 설정
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity (5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation (45.0);
    $stamp->setBackground(false);

    // 스탬프 추가
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```