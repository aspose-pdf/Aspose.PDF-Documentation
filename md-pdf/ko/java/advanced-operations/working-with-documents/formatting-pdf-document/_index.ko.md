---
title: PDF 문서 서식 
linktitle: PDF 문서 서식
type: docs
weight: 20
url: /java/formatting-pdf-document/
description: Aspose.PDF for Java를 사용하여 PDF 문서의 서식을 지정합니다. 다음 코드 스니펫을 사용하여 작업을 해결하십시오.
lastmod: "2021-06-05"
---

## 문서 창 및 페이지 표시 속성 가져오기

이 주제는 문서 창, 뷰어 애플리케이션의 속성을 가져오는 방법과 페이지가 표시되는 방법을 이해하는 데 도움이 됩니다.

이러한 다양한 속성을 설정하려면 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF 파일을 엽니다. 이제 다음과 같은 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 메서드를 얻을 수 있습니다.

- [IsCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – 화면에 문서 창을 중앙에 배치합니다. 기본값: false.
- [SetDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – 읽기 순서.
 이것은 페이지가 나란히 표시될 때 어떻게 배열되는지를 결정합니다. 기본값: 왼쪽에서 오른쪽으로.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – 문서 창 제목 표시줄에 문서 제목을 표시합니다. 기본값: false (제목이 표시됨).
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-) – 문서 창의 메뉴 바를 숨기거나 표시합니다. 기본값: false (메뉴 바가 표시됨).
- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-) – 문서 창의 툴바를 숨기거나 표시합니다. 기본값: false (툴바가 표시됨).
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-) – 스크롤 바와 같은 문서 창 요소를 숨기거나 표시합니다. 기본값: false (UI 요소가 표시됨).

- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-) – 문서가 전체 페이지 모드로 표시되지 않을 때 문서가 표시되는 방식.- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-) – 페이지 레이아웃.
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-) – 문서를 처음 열 때 어떻게 표시할지를 설정합니다. 옵션에는 썸네일 보기, 전체 화면, 첨부 파일 패널 표시가 있습니다.

다음 코드 스니펫은 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 속성을 가져오는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleFormatting {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void GetDocumentWindowAndPageDisplayProperties() {

    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // 다양한 문서 속성 가져오기
    // 문서 창의 위치 - 기본값: false
    System.out.printf("CenterWindow : " + pdfDocument.isCenterWindow());

    // 주요 읽기 방향; 페이지의 위치 결정
    // 나란히 표시될 때 - 기본값: L2R
    System.out.printf("Direction :- " + pdfDocument.getDirection());

    // 창의 제목 표시줄이 문서 제목을 표시할지 여부.
    // false인 경우, 제목 표시줄에 PDF 파일 이름이 표시됩니다 - 기본값: false
    System.out.printf("DisplayDocTitle :- " + pdfDocument.isDisplayDocTitle());

    // 문서의 창 크기를 첫 번째 표시된 페이지의 크기에 맞출지 여부 - 기본값: false
    System.out.printf("FitWindow :- " + pdfDocument.isFitWindow());

    // 뷰어 애플리케이션의 메뉴 바를 숨길지 여부 - 기본값: false
    System.out.printf("HideMenuBar :-" + pdfDocument.isHideMenubar());

    // 뷰어 애플리케이션의 도구 모음을 숨길지 여부 - 기본값: false
    System.out.printf("HideToolBar :-" + pdfDocument.isHideToolBar());

    // 스크롤 바와 같은 UI 요소를 숨기고
    // 페이지 콘텐츠만 표시할지 여부 - 기본값: false
    System.out.printf("HideWindowUI :-" + pdfDocument.isHideWindowUI());

    // 문서의 페이지 모드. 전체 화면 모드를 종료할 때
    // 문서를 어떻게 표시할지.
    System.out.printf("NonFullScreenPageMode :-" + pdfDocument.getNonFullScreenPageMode());

    // 페이지 레이아웃 즉, 단일 페이지, 한 열
    System.out.printf("PageLayout :-" + pdfDocument.getPageLayout());

    // 문서를 열 때 어떻게 표시할지를 설정합니다.
    System.out.printf("pageMode :-" + pdfDocument.getPageMode());

  }

```

## 문서 창 및 페이지 표시 속성 설정

이 주제는 문서 창, 뷰어 애플리케이션 및 페이지 표시 속성을 설정하는 방법을 설명합니다.

이러한 다양한 속성을 설정하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF 파일을 엽니다.
1. Document 객체의 속성을 설정합니다.
1. Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

사용 가능한 속성은 다음과 같습니다:

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

```java
  public static void SetDocumentWindowAndPageDisplayProperties() {

    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    
    // 다양한 문서 속성 설정
    // 문서 창의 위치 지정 - 기본값: false
    pdfDocument.setCenterWindow(true);
    
    // 주로 읽는 방향; 나란히 표시될 때 페이지의 위치 결정 - 기본값: L2R
    pdfDocument.setDirection(com.aspose.pdf.Direction.R2L);
    
    // 창의 제목 표시줄이 문서 제목을 표시할지 여부 지정
    // false인 경우 제목 표시줄은 PDF 파일 이름을 표시 - 기본값: false
    pdfDocument.setDisplayDocTitle(true);
    
    // 문서 창을 첫 번째로 표시된 페이지의 크기에 맞게 조정할지 여부 지정 - 기본값: false
    pdfDocument.setFitWindow(true);
    
    // 뷰어 애플리케이션의 메뉴 바를 숨길지 여부 지정 - 기본값: false
    pdfDocument.setHideMenubar(true);
    
    // 뷰어 애플리케이션의 도구 모음을 숨길지 여부 지정 - 기본값: false
    pdfDocument.setHideToolBar(true);
    
    // 스크롤 바와 같은 UI 요소를 숨기고 페이지 내용만 표시할지 여부 지정 - 기본값: false
    pdfDocument.setHideWindowUI(true);
    
    // 문서의 페이지 모드. 전체 화면 모드 종료 시 문서 표시 방법 지정
    pdfDocument.setNonFullScreenPageMode(com.aspose.pdf.PageMode.UseOC);
    
    // 페이지 레이아웃 지정, 예: 단일 페이지, 한 열
    pdfDocument.setPageLayout(com.aspose.pdf.PageLayout.TwoColumnLeft);
    
    // 문서가 열릴 때 표시 방법 지정, 예: 축소판 보기, 전체 화면, 첨부 파일 패널 보기
    pdfDocument.setPageMode(com.aspose.pdf.PageMode.UseThumbs);
    
    // 업데이트된 PDF 파일 저장
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");

  }
```

## 기존 PDF 파일에 글꼴 포함

PDF 리더는 문서가 표시되는 플랫폼에 관계없이 동일한 방식으로 문서를 표시할 수 있도록 [14개의 기본 글꼴](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts)을 지원합니다. PDF에 기본 글꼴 이외의 글꼴이 포함된 경우 글꼴 대체를 피하기 위해 글꼴을 포함하십시오.

Aspose.PDF for Java는 기존 PDF 문서에서 글꼴 포함을 지원합니다. 전체 글꼴 또는 부분 집합을 포함할 수 있습니다. 글꼴을 포함하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 기존 PDF 파일을 엽니다.
1. [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) 클래스를 사용하여 글꼴을 포함합니다.
   1. setEmbedded(true) 메서드는 전체 글꼴을 포함합니다.
   1. pageFont.isSubset(true) 메서드는 글꼴의 부분 집합을 포함합니다.

글꼴 부분 집합은 사용된 문자만 포함하며, 짧은 문장이나 슬로건에 글꼴이 사용되는 경우에 유용합니다. 예를 들어 로고에 기업 글꼴이 사용되지만 본문 텍스트에는 사용되지 않는 경우입니다.
 서브셋을 사용하면 출력 PDF의 파일 크기가 줄어듭니다.

그러나 본문 텍스트에 사용자 정의 글꼴을 사용하는 경우 전체를 포함시킵니다.

다음 코드 스니펫은 PDF 파일에 글꼴을 포함시키는 방법을 보여줍니다.
```java
public static void EmbeddingFontsInAnExistingPDFFile() {
    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // 모든 페이지를 반복
    for (com.aspose.pdf.Page page : (Iterable<com.aspose.pdf.Page>) pdfDocument.getPages()) {
      if (page.getResources().getFonts() != null) {
        for (com.aspose.pdf.Font pageFont : (Iterable<com.aspose.pdf.Font>) page.getResources().getFonts()) {
          // 글꼴이 이미 포함되어 있는지 확인
          if (!pageFont.isEmbedded())
            pageFont.setEmbedded(true);
        }
      }

      // 폼 객체 확인
      for (com.aspose.pdf.XForm form : (Iterable<com.aspose.pdf.XForm>) page.getResources().getForms()) {
        if (form.getResources().getFonts() != null) {
          for (com.aspose.pdf.Font formFont : (Iterable<com.aspose.pdf.Font>) form.getResources().getFonts()) {
            // 글꼴이 포함되어 있는지 확인
            if (!formFont.isEmbedded())
              formFont.setEmbedded(true);
          }
        }
      }
    }
    // 업데이트된 PDF 파일 저장
    pdfDocument.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## PDF 생성 시 폰트 임베딩

Adobe Reader에서 지원하는 14개의 기본 폰트 외에 다른 폰트를 사용해야 하는 경우, PDF 파일을 생성할 때 폰트 설명을 임베딩해야 합니다. 폰트 정보가 임베딩되지 않은 경우, Adobe Reader는 운영 체제에 설치된 경우 해당 시스템에서 가져오거나 PDF의 폰트 설명에 따라 대체 폰트를 구성합니다. 임베디드 폰트는 호스트 머신에 설치되어 있어야 한다는 점을 유의하세요. 즉, 다음 코드의 경우 ‘Univers Condensed’ 폰트가 시스템에 설치되어 있습니다.

[Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) 클래스의 setEmbedded 속성을 사용하여 PDF 파일에 폰트 정보를 임베딩합니다. 이 속성의 값을 ‘true’로 설정하면 전체 폰트 파일이 PDF에 임베딩되며, 이는 PDF 파일 크기를 증가시킬 수 있습니다. 다음은 PDF에 폰트 정보를 임베딩하는 데 사용할 수 있는 코드 스니펫입니다.

```java
public static void EmbeddingFontsWhileCreatingPDF() {

    // 빈 생성자를 호출하여 PDF 객체를 인스턴스화합니다.
    com.aspose.pdf.Document document = new com.aspose.pdf.Document();

    // Pdf 객체에 섹션을 생성합니다.
    com.aspose.pdf.Page page = document.getPages().add();

    com.aspose.pdf.TextFragment fragment = new com.aspose.pdf.TextFragment("");

    com.aspose.pdf.TextSegment segment = new com.aspose.pdf.TextSegment(" This is a sample text using Custom font.");
    com.aspose.pdf.TextState ts = new com.aspose.pdf.TextState();
    ts.setFont(FontRepository.findFont("Univers Condensed"));
    ts.getFont().setEmbedded(true);
    segment.setTextState(ts);
    fragment.getSegments().add(segment);
    page.getParagraphs().add(fragment);

    // 업데이트된 PDF 파일 저장
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```

## PDF 저장 시 기본 글꼴 이름 설정

PDF 문서에 문서 자체나 장치에 사용할 수 없는 글꼴이 포함되어 있을 때, API는 이러한 글꼴을 기본 글꼴로 대체합니다. 글꼴이 사용 가능할 때(장치에 설치되어 있거나 문서에 포함되어 있을 때), 출력 PDF는 동일한 글꼴을 가져야 하며(기본 글꼴로 대체되어서는 안 됩니다). 기본 글꼴의 값은 글꼴 파일의 경로가 아닌 글꼴 이름을 포함해야 합니다. 우리는 문서를 PDF로 저장할 때 기본 글꼴 이름을 설정하는 기능을 구현했습니다. 다음의 코드 스니펫을 사용하여 기본 글꼴을 설정할 수 있습니다:

```java
public static void SetDefaultFontNameWhileSavingPDF() {

    // 기존 PDF 문서 로드
    Document document = new Document("input.pdf");

    String newName = "Arial";

    // PDF 형식의 저장 옵션 초기화
    PdfSaveOptions ops = new PdfSaveOptions();

    // 기본 글꼴 이름 설정
    ops.setDefaultFontName(newName);

    // PDF 파일 저장
    document.save(_dataDir + "output_out.pdf", ops);
  }
```


## PDF 문서에서 모든 글꼴 가져오기

PDF 문서에서 모든 글꼴을 가져오고 싶은 경우, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스에서 제공하는 **Document.getFontUtilities().getAllFonts()** 메서드를 사용할 수 있습니다. 기존 PDF 문서에서 모든 글꼴을 가져오기 위해 다음 코드 스니펫을 확인하십시오:

```java
public static void GetAllFontsFromPDFDocument() {

    // 기존 PDF 문서를 로드합니다.
    Document document = new Document(_dataDir + "sample.pdf");

    // 문서에서 모든 글꼴을 가져옵니다.
    com.aspose.pdf.Font[] fonts = document.getFontUtilities().getAllFonts();
    for (com.aspose.pdf.Font f : fonts) {
      System.out.println(f.getFontName());
    }
  }
```

## PDF 파일의 확대/축소 비율 가져오기/설정하기

때때로 PDF 문서의 확대/축소 비율을 설정하거나 가져오고 싶을 때가 있습니다. Aspose.PDF를 사용하여 이 요구 사항을 쉽게 충족할 수 있습니다.

[GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) 객체는 PDF 파일과 연관된 확대/축소 값을 가져올 수 있도록 해줍니다.
 유사하게, 파일의 줌 팩터를 설정하는 데 사용할 수 있습니다.

```java
  public static void GetSetZoomFactorOfPDFFile() {
    // 기존 PDF 문서 로드
    Document document = new Document(_dataDir + "sample.pdf");
    double zoom = .5;
    // 문서의 줌 팩터 설정
    GoToAction actionzoom = new GoToAction(new XYZExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth(),
        document.getPages().get_Item(1).getMediaBox().getHeight(), zoom));

    // 페이지 너비에 맞추기 줌으로 설정
    GoToAction actionFittoWidth = new GoToAction(new FitHExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getWidth()));

    // 페이지 높이에 맞추기 줌으로 설정
    GoToAction actionFittoHeight = new GoToAction(new FitVExplicitDestination(document.getPages().get_Item(1),
        document.getPages().get_Item(1).getMediaBox().getHeight()));

    document.setOpenAction(actionzoom);
    document.setOpenAction(actionFittoWidth);
    document.setOpenAction(actionFittoHeight);
```

The following code snippet shows how to get the Zoom factor of a PDF file.

```java
    // 새 문서 객체 생성
    Document doc1 = new Document(_dataDir + "Zoomed_actionzoom.pdf");
    // GoToAction 객체 생성
    GoToAction action = (GoToAction) doc1.getOpenAction();
    // PDF 파일의 확대/축소 비율 가져오기
    System.out.println(((XYZExplicitDestination) action.getDestination()).getZoom());

    // 업데이트된 PDF 파일 저장
    document.save(_dataDir + "UpdatedFile_output.pdf");
  }
}
```