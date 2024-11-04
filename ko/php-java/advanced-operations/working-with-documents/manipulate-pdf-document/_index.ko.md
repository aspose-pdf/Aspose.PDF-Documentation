---
title: PDF 문서 조작
linktitle: PDF 문서 조작
type: docs
weight: 30
url: /php-java/manipulate-pdf-document/
description: 이 문서에는 PDF A 표준에 대한 PDF 문서 검증 방법, 목차 작업 방법, PDF 만료 날짜 설정 방법 및 PDF 파일 생성 진행 상황 확인 방법에 대한 정보가 포함되어 있습니다.
lastmod: "2024-06-05"
---

## PDF A 표준 (A 1A 및 A 1B)에 대한 PDF 문서 검증

PDF/A-1a 또는 PDF/A-1b 호환성을 위해 PDF 문서를 검증하려면 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 [validate(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#validate-java.lang.String-com.aspose.pdf.PdfFormat-) 메서드를 사용하세요. 이 메서드는 결과가 저장될 파일의 이름과 필요한 검증 유형 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) 열거형: PDF_A_1A 또는 PDF_A_1B를 지정할 수 있도록 합니다.

출력 XML 형식은 사용자 지정 Aspose 형식입니다.
 XML에는 Problem이라는 이름을 가진 태그 모음이 포함되어 있습니다. 각 태그는 특정 문제의 세부 정보를 포함하고 있습니다. Problem 태그의 ObjectID 속성은 이 문제가 관련된 특정 객체의 ID를 나타냅니다. Clause 속성은 PDF 사양의 해당 규칙을 나타냅니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // PDF를 PDF/A-1a로 검증
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## 목차 작업

### 기존 PDF에 목차 추가

기존 PDF 파일에 목차를 추가하려면 com.aspose.pdf 패키지의 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 클래스를 사용하세요. com.aspose.pdf 패키지는 새 PDF 파일을 생성하고 기존 PDF 파일을 조작할 수 있습니다. 기존 PDF에 목차를 추가하려면 com.aspose.pdf 패키지를 사용하십시오.

이 PHP 코드 스니펫은 Aspose.PDF를 사용하여 기존 PDF 문서에 목차(Table of Contents, TOC)를 추가합니다:

```php
    // 문서 열기
    $document = new Document($inputFile);

    // PDF 파일의 첫 번째 페이지에 접근
    $tocPage = $document->getPages()->insert(1);

    // 목차 정보를 나타내는 객체 생성
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // 목차의 제목 설정
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // 목차 요소로 사용될 문자열 객체 생성
    $titles = ["First page", "Second page", "Third page", "Fourth page"];

    for ($i = 0; $i < 4; $i++) {
        // Heading 객체 생성
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Heading 객체의 대상 페이지 지정
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // 대상 페이지
        $heading2->setTop($page->getRect()->getHeight());

        // 대상 좌표
        $segment2->setText($titles[$i]);

        // 목차를 포함하는 페이지에 제목 추가
        $tocPage->getParagraphs()->add($heading2);
    }
    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

### 서로 다른 TOC 레벨에 대해 다른 TabLeaderType 설정

Aspose.PDF는 또한 서로 다른 TOC 레벨에 대해 다른 TabLeaderType을 설정할 수 있습니다. 다음과 같이 FormatArray의 LineDash 속성을 TabLeaderType 열거형의 적절한 값으로 설정해야 합니다.

```php
    // 문서 열기
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // LeaderType 설정
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("목차");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // PDF 문서의 섹션 컬렉션에 목록 섹션 추가
    $tocPage->setTocInfo($tocInfo);

    // 각 레벨의 왼쪽 여백 및 텍스트 형식 설정을 통해 네 가지 레벨 목록의 형식을 정의
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // PDF 문서에 섹션 생성
    $page = $document->getPages()->add();

    // 섹션에 네 개의 제목 추가
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("샘플 제목" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // 목차에 제목 추가.
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```


### 목차에서 페이지 번호 숨기기

목차에 제목과 함께 페이지 번호를 표시하지 않으려는 경우, [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) 클래스의 [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/#setShowPageNumbers-boolean-) 속성을 false로 설정하면 됩니다. 목차에서 페이지 번호를 숨기기 위한 다음 코드 스니펫을 확인하십시오:

```php
    // 문서 열기
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // 목차 정보를 나타내는 객체 생성
    $tocInfo = new TocInfo();

    $title = new TextFragment("목차");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // 목차의 제목 설정
    $tocInfo->setTitle($title);

    // Pdf 문서의 섹션 컬렉션에 리스트 섹션 추가
    $tocPage->setTocInfo($tocInfo);

    // 왼쪽 여백 및 각 레벨의 텍스트 형식 설정을 통해 네 레벨 목록의 형식 정의

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // 섹션에 네 개의 제목 추가
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("이것은 레벨 " + $Level + "의 제목입니다");
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```


### TOC 추가 시 페이지 번호 사용자 정의

PDF 문서에 TOC를 추가할 때 페이지 번호를 사용자 정의하는 것이 일반적입니다. 예를 들어, 페이지 번호 앞에 P1, P2, P3 등과 같은 접두사를 추가해야 할 수 있습니다. 이러한 경우, Aspose.PDF for PHP via Java는 TocInfo 클래스의 PageNumbersPrefix 속성을 제공하여 다음 코드 샘플에서 보여주는 대로 페이지 번호를 사용자 정의할 수 있습니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // PDF 파일의 첫 번째 페이지에 접근
    $tocPage = $document->getPages()->insert(1);

    // TOC 정보를 나타내는 객체 생성
    $tocInfo = new TocInfo();

    $title = new TextFragment("Table Of Contents");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // TOC 제목 설정
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // TOC 요소로 사용될 문자열 객체 생성
    $titles = ["First page", "Second page", "Third page", "Fourth page"];

    for ($i = 0; $i < 4; $i++) {
        // Heading 객체 생성
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Heading 객체의 대상 페이지 지정
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // 대상 페이지
        $heading2->setTop($page->getRect()->getHeight());

        // 대상 좌표
        $segment2->setText($titles[$i]);

        // TOC가 포함된 페이지에 heading 추가
        $tocPage->getParagraphs()->add($heading2);
    }
    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```


## PDF 파일에 레이어 추가

레이어는 PDF 문서에서 다양한 방식으로 사용할 수 있습니다. 여러 언어로 된 파일을 배포하려는 경우 각 언어의 텍스트가 다른 레이어에 나타나도록 하고, 배경 디자인은 별도의 레이어에 나타나도록 할 수 있습니다. 또는 애니메이션이 별도의 레이어에 나타나는 문서를 생성할 수도 있습니다. 예를 들어 파일에 사용권 계약을 추가하고, 사용자가 계약 조건에 동의하기 전까지 내용을 보지 못하게 할 수 있습니다.

Aspose.PDF for PHP via Java는 PDF 파일에 레이어를 추가하는 것을 지원합니다.

PDF 파일의 레이어를 작업하려면 다음의 API 멤버를 사용하십시오.

[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) 클래스는 레이어를 나타내며 다음과 같은 속성을 포함합니다:

- **Name** – 레이어의 이름.
- **Id** – 레이어의 ID.
- **Contents** – 레이어 연산자의 목록.

한번 [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) 객체가 정의되면, [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 객체의 Layers 컬렉션에 이를 추가하십시오.
 PDF 문서에 레이어를 추가하는 방법을 보여주는 코드입니다.

```php
    // 문서 열기
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "빨간 선");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "녹색 선");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "파란 선");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```

## PDF 만료 설정

PDF 만료 기능은 PDF 파일의 유효 기간을 설정합니다. 특정 날짜에 누군가가 접근하려고 하면, 파일이 만료되었으며 새 파일이 필요하다는 설명과 함께 팝업이 표시됩니다.

Aspose.PDF는 PDF 파일을 생성하고 편집할 때 만료를 설정할 수 있게 합니다.

아래의 코드 스니펫은 PDF 파일의 만료 날짜를 설정하는 방법을 보여줍니다. JavaScript를 사용해야 하며, 제3자 구성 요소(예: OwnerGuard)로 저장된 파일은 해당 유틸리티 없이는 다른 워크스테이션에서 볼 수 없습니다.

PDF 파일은 만료 날짜가 있는 기존 파일을 사용하여 PDF OwnerGuard로 생성할 수 있습니다. 그러나 새 파일은 PDF OwnerGuard가 설치된 워크스테이션에서만 열 수 있습니다. PDF OwnerGuard가 없는 워크스테이션에서는 ExpirationFeatureError가 발생합니다. 예를 들어, PDF 리더는 OwnerGuard가 설치되어 있으면 파일을 열 수 있지만, Adobe Acrobat은 오류를 반환합니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```