---
title: PDF 문서 포맷팅 
linktitle: PDF 문서 포맷팅
type: docs
weight: 20
url: /php-java/formatting-pdf-document/
description: PHP를 통해 Java로 Aspose.PDF를 사용하여 PDF 문서를 포맷합니다. 작업을 해결하기 위해 다음 코드 스니펫을 사용하십시오.
lastmod: "2024-06-05"
---

## 문서 창 및 페이지 표시 속성 가져오기

이 주제는 문서 창, 뷰어 애플리케이션의 속성을 얻고 페이지가 어떻게 표시되는지 이해하는 데 도움이 됩니다.

이러한 다양한 속성을 설정하려면 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF 파일을 엽니다. 이제 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 메서드를 얻을 수 있습니다. 예를 들어

- [isCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – 문서 창을 화면 중앙에 배치합니다. 기본값: false.
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – 읽기 순서.
 이것은 페이지가 나란히 표시될 때 레이아웃되는 방식을 결정합니다. 기본값: 왼쪽에서 오른쪽으로.

- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – 문서 창 제목 표시줄에 문서 제목을 표시합니다. 기본값: false (제목이 표시됨).
- [isHideMenubar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideMenubar--) – 문서가 활성화될 때 메뉴 바를 숨길지 여부를 지정하는 플래그를 가져옵니다.
- [isHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideToolBar--) – 문서가 활성화될 때 도구 모음을 숨길지 여부를 지정하는 플래그를 가져옵니다.
- [isHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideWindowUI--) – 문서가 활성화될 때 사용자 인터페이스 요소를 숨길지 여부를 지정하는 플래그를 가져옵니다.

- [getNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getNonFullScreenPageMode--) – 전체 화면 모드를 종료할 때 문서를 표시하는 방법을 지정하는 페이지 모드를 가져옵니다.- [getPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageLayout--) – 페이지 레이아웃.
- [getPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageMode--) – 문서를 열 때 어떻게 표시되어야 하는지 지정하는 페이지 모드를 가져옵니다.

다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 속성을 가져오는 방법을 보여줍니다.

```php  

    // 문서 열기
    $document = new Document($inputFile);

    // 다양한 문서 속성 가져오기
    // 문서 창의 위치 - 기본값: false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // 주된 읽기 순서; 페이지의 위치를 결정
    // 나란히 표시될 때 - 기본값: L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // 창의 제목 표시줄에 문서 제목을 표시할지 여부.
    // false인 경우, 제목 표시줄에 PDF 파일 이름이 표시됨 - 기본값: false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // 첫 표시 페이지의 크기에 맞춰 문서 창의 크기를 조정할지 여부 - 기본값: false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // 뷰어 응용 프로그램의 메뉴 막대를 숨길지 여부 - 기본값: false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // 뷰어 응용 프로그램의 도구 막대를 숨길지 여부 - 기본값: false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // 스크롤 막대 같은 UI 요소를 숨기고
    // 페이지 내용만 표시할지 여부 - 기본값: false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // 문서의 페이지 모드. 전체 화면 모드를 종료할 때 문서를 표시하는 방법.
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // 페이지 레이아웃, 즉 단일 페이지, 한 열
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // 문서를 열 때 어떻게 표시해야 하는지.
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
```


## 문서 창 및 페이지 표시 속성 설정

이 주제는 문서 창, 뷰어 애플리케이션 및 페이지 표시의 속성을 설정하는 방법을 설명합니다.

이러한 다양한 속성을 설정하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF 파일을 엽니다.
1. Document 객체의 속성을 설정합니다.
1. Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

사용 가능한 메서드는 다음과 같습니다:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 속성을 설정하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    // 다양한 문서 속성 설정
    // 문서 창의 위치를 지정 - 기본값: false
    $document->setCenterWindow(true);
    // 주로 사용되는 읽기 순서; 페이지의 위치를 결정
    // 나란히 표시될 때 - 기본값: L2R
    $document->setDirection(Direction::$R2L);
    // 창의 제목 표시줄에 문서 제목을 표시할지 여부를 지정
    // false인 경우, 제목 표시줄에 PDF 파일 이름이 표시됩니다 - 기본값: false
    $document->setDisplayDocTitle(true);
    // 첫 번째로 표시된 페이지의 크기에 맞게
    // 문서 창의 크기를 조정할지 여부를 지정 - 기본값: false
    $document->setFitWindow(true);
    // 뷰어 애플리케이션의 메뉴 바를 숨길지 여부를 지정 - 기본값:
    // false
    $document->setHideMenubar(true);
    // 뷰어 애플리케이션의 도구 모음을 숨길지 여부를 지정 - 기본값:
    // false
    $document->setHideToolBar(true);
    // 스크롤 바와 같은 UI 요소를 숨기고
    // 페이지 콘텐츠만 표시할지 여부를 지정 - 기본값: false
    $document->setHideWindowUI(true);
    // 문서의 페이지 모드. 전체 화면 모드를 종료할 때
    // 문서를 어떻게 표시할지 지정합니다.
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // 페이지 레이아웃 지정, 예: 단일 페이지, 한 열
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // 문서를 열 때 어떻게 표시할지 지정
    // 예: 썸네일 표시, 전체 화면, 첨부 파일 패널 표시
    $document->setPageMode(PageMode::$UseThumbs);
    // 업데이트된 PDF 파일 저장
    $document->save($outputFile);
    $document->close();

```


## 기존 PDF 파일에 글꼴 포함시키기

PDF 리더는 문서가 표시되는 플랫폼에 관계없이 동일한 방식으로 문서를 표시할 수 있도록 [14개의 기본 글꼴](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts)을 지원합니다. PDF에 기본 글꼴 이외의 글꼴이 포함된 경우, 글꼴 대체를 피하기 위해 글꼴을 포함시킵니다.

Aspose.PDF for PHP via Java는 기존 PDF 문서에서 글꼴 포함을 지원합니다. 전체 글꼴이나 부분 집합을 포함시킬 수 있습니다. 글꼴을 포함시키려면 다음과 같이 하십시오:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 기존 PDF 파일을 엽니다.
1. [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) 클래스를 사용하여 글꼴을 포함시킵니다.
   1. setEmbedded(true) 메소드는 전체 글꼴을 포함시킵니다.
   1. [isSubset(true) 메소드](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/#isSubset--)는 글꼴의 부분 집합을 포함시킵니다.

글꼴 부분 집합은 사용된 문자만을 포함하여, 짧은 문장이나 슬로건에 글꼴이 사용될 때 유용합니다. 예를 들어, 기업 로고에 사용되는 글꼴이 본문 텍스트에는 사용되지 않는 경우입니다.
 파일 크기를 줄이기 위해 부분 집합을 사용합니다.

그러나 본문 텍스트에 사용자 정의 글꼴이 사용된 경우 전체 글꼴을 포함합니다.

다음 코드 스니펫은 PDF 파일에 글꼴을 포함하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    $pages = $document->getPages();
    for ($i = 1; $i <= $pages->size(); $i++) {
      $page = $pages->get_Item($i);
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        for ($fontIndex = 1; $fontIndex <= $fonts->size(); $fontIndex++) {
          $pageFont = $fonts->get_Item($fontIndex);
          // 글꼴이 이미 포함되어 있는지 확인
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // 양식 객체 확인
      for ($formIndex = 0; $formIndex < -$forms->size(); $formIndex++) {
        $formFonts = $forms->get_Item($formIndex)->getResources()->getFonts();
        if (!is_null($formFonts)) {
          for ($fontIndex = 1; $fontIndex <= $formFonts->size(); $fontIndex++) {
            $pageFont = $formFonts->get_Item($fontIndex);
            // 글꼴이 이미 포함되어 있는지 확인
            if (!$pageFont->isEmbedded())
              $pageFont->setEmbedded(true);
          }
        }
      }
      $responseData = "Ok";
    }

    // 업데이트된 PDF 파일 저장
    $document->save($outputFile);
    $document->close();
```

## PDF 생성 시 폰트 임베딩

Adobe Reader에서 지원하는 14개의 기본 폰트 외에 다른 폰트를 사용해야 하는 경우, PDF 파일을 생성할 때 폰트 설명을 임베딩해야 합니다. 폰트 정보가 임베딩되지 않으면 Adobe Reader는 시스템에 설치되어 있는 경우 운영 체제에서 이를 가져오거나 PDF의 폰트 설명에 따라 대체 폰트를 구성합니다. 임베딩된 폰트는 호스트 머신에 설치되어 있어야 합니다. 즉, 다음 코드의 경우 'Univers Condensed' 폰트가 시스템에 설치되어 있습니다.

[Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) 클래스의 setEmbedded 속성을 사용하여 PDF 파일에 폰트 정보를 임베딩합니다. 이 속성의 값을 'true'로 설정하면 전체 폰트 파일이 PDF에 임베딩되며, PDF 파일 크기가 증가할 수 있습니다. 다음은 폰트 정보를 PDF에 임베딩하는 데 사용할 수 있는 코드 스니펫입니다.

```php

    // 빈 생성자를 호출하여 PDF 객체 인스턴스 생성
    $document = new Document();

    // Pdf 객체에 섹션 생성
    $page = $document->getPages()->add();
    $fragment = new TextFragment("");
    $segment = new TextSegment("이것은 사용자 정의 폰트를 사용하는 샘플 텍스트입니다.");

    $fontRepository = new FontRepository();

    $ts = new TextState();
    $ts->setFont($fontRepository->findFont("Univers Condensed"));
    $ts->getFont()->setEmbedded(true);
    $segment->setTextState($ts);
    $fragment->getSegments()->add($segment);
    $page->getParagraphs()->add($fragment);

    // 업데이트된 PDF 파일 저장
    $document->save($outputFile);
    $document->close();
```


## PDF 저장 시 기본 글꼴 이름 설정

PDF 문서에 문서 자체와 장치에 없는 글꼴이 포함되어 있을 경우, API는 이러한 글꼴을 기본 글꼴로 대체합니다. 글꼴이 사용 가능한 경우(장치에 설치되어 있거나 문서에 포함되어 있는 경우), 출력 PDF는 동일한 글꼴을 가져야 하며 기본 글꼴로 대체되지 않아야 합니다. 기본 글꼴의 값은 글꼴 이름(글꼴 파일 경로가 아님)을 포함해야 합니다. 우리는 문서를 PDF로 저장할 때 기본 글꼴 이름을 설정하는 기능을 구현했습니다. 다음 코드 스니펫을 사용하여 기본 글꼴을 설정할 수 있습니다:

```php

    // 기존 PDF 문서 로드
    $document = new Document($inputFile);
    $newName = "Arial";

    // PDF 형식의 저장 옵션 초기화
    $ops = new PdfSaveOptions();

    // 기본 글꼴 이름 설정
    $ops->setDefaultFontName($newName);

    // PDF 파일 저장
    $document->save($outputFile, $ops);
    // 업데이트된 PDF 파일 저장
    $document->close();
```

## PDF 문서에서 모든 글꼴 가져오기

PDF 문서에서 모든 글꼴을 가져오려는 경우, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스에서 제공하는 **Document.getFontUtilities().getAllFonts()** 메서드를 사용할 수 있습니다.
 다음 코드 스니펫을 확인하여 기존 PDF 문서에서 모든 글꼴을 가져오십시오:

```php

    // 기존 PDF 문서 로드
    $document = new Document($inputFile);

    // 문서에서 모든 글꼴 가져오기
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // 업데이트된 PDF 파일 저장
    $document->close();
```

## PDF 파일의 확대/축소 계수 가져오기/설정

때때로 PDF 문서의 확대/축소 계수를 설정하거나 가져와야 할 때가 있습니다. Aspose.PDF를 사용하여 이 요구 사항을 쉽게 달성할 수 있습니다.

[GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) 객체는 PDF 파일과 연결된 확대/축소 값을 가져올 수 있도록 합니다. 마찬가지로, 파일의 확대/축소 계수를 설정하는 데 사용할 수 있습니다.

```php

    // 기존 PDF 문서 로드
    $document = new Document($inputFile);

    // GoToAction 객체 생성
    $action = $document->getOpenAction();

    // PDF 파일의 확대/축소 계수 가져오기
    $responseData = $action->getDestination()->getZoom();

    // 업데이트된 PDF 파일 저장
    $document->close();  
```

다음 코드 스니펫은 PDF 파일의 확대 비율을 얻는 방법을 보여줍니다.

```php

    // 기존 PDF 문서 로드
    $document = new Document($inputFile);
    $zoom = 0.5;
    // 문서의 확대 비율 설정
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // 페이지 너비에 맞추기 위한 동작 설정
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // 페이지 높이에 맞추기 위한 동작 설정
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination( $page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // 업데이트된 PDF 파일 저장
    $document->save($outputFile);
    $document->close();  
```