---
title: PHP에서 문서 창 및 페이지 표시 속성 가져오기
type: docs
weight: 30
url: /ko/java/get-document-window-and-page-display-properties-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 문서 창 및 페이지 표시 속성 가져오기

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서의 문서 창 및 페이지 표시 속성을 가져오려면, **GetDocumentWindow** 클래스를 호출합니다.

PHP 코드

```php

# PDF 문서를 엽니다.
$doc = new Document($dataDir . "input1.pdf");

# 다양한 문서 속성 가져오기
# 문서 창의 위치 - 기본값: false
print "CenterWindow :- " . $doc->getCenterWindow() . PHP_EOL;

# 주요 읽기 순서; 나란히 표시될 때 페이지의 위치 결정 - 기본값: L2R
print "Direction :- " . $doc->getDirection() . PHP_EOL;

# 창의 제목 표시줄에 문서 제목을 표시할지 여부.
# false이면 제목 표시줄에 PDF 파일 이름이 표시됨 - 기본값: false
print "DisplayDocTitle :- " . $doc->getDisplayDocTitle() . PHP_EOL;

# 문서의 창 크기를 첫 번째로 표시된 페이지의 크기에 맞추어
# 조정할지 여부 - 기본값: false
print "FitWindow :- " . $doc->getFitWindow() . PHP_EOL;

# 뷰어 응용 프로그램의 메뉴 표시줄을 숨길지 여부 - 기본값: false
print "HideMenuBar :-" . $doc->getHideMenubar() . PHP_EOL;

# 뷰어 응용 프로그램의 도구 모음을 숨길지 여부 - 기본값: false
print "HideToolBar :-" . $doc->getHideToolBar() . PHP_EOL;

# 스크롤 바와 같은 UI 요소를 숨기고
# 페이지 내용만 표시할지 여부 - 기본값: false
print "HideWindowUI :-" . $doc->getHideWindowUI() . PHP_EOL;

# 문서의 페이지 모드. 전체 화면 모드에서 나올 때 문서를 표시하는 방법.
print "NonFullScreenPageMode :-" . $doc->getNonFullScreenPageMode() . PHP_EOL;

# 페이지 레이아웃 즉, 단일 페이지, 한 열
print "PageLayout :-" . $doc->getPageLayout() . PHP_EOL;

# 문서를 열 때 어떻게 표시할지.
print "pageMode :-" . $doc->getPageMode() . PHP_EOL;
```


**실행 코드 다운로드**

다음의 소셜 코딩 사이트 중 하나에서 **문서 창 및 페이지 표시 속성 가져오기 (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetDocumentWindow.php)