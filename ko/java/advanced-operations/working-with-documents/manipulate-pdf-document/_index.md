---
title: PDF 문서 조작
linktitle: PDF 문서 조작
type: docs
weight: 30
url: /ko/java/manipulate-pdf-document/
description: 이 문서는 PDF A 표준에 대한 PDF 문서 유효성 검사, 목차 작업, PDF 만료 날짜 설정 및 PDF 파일 생성 진행 상태 결정에 대한 정보를 포함하고 있습니다.
lastmod: "2021-06-05"
---

## PDF A 표준을 위한 PDF 문서 유효성 검사 (A 1A 및 A 1B)

PDF/A-1a 또는 PDF/A-1b 호환성을 위한 PDF 문서의 유효성을 검사하려면, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) 메서드를 사용하십시오. 이 메서드는 결과가 저장될 파일의 이름과 필요한 유효성 검사 유형인 [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) 열거형: PDF_A_1A 또는 PDF_A_1B를 지정할 수 있습니다.

출력 XML 형식은 사용자 지정 Aspose 형식입니다.
 XML에는 Problem이라는 이름을 가진 태그들이 모여 있으며, 각 태그에는 특정 문제에 대한 세부 정보가 포함되어 있습니다. Problem 태그의 ObjectID 속성은 이 문제가 관련된 특정 객체의 ID를 나타냅니다. Clause 속성은 PDF 사양의 해당 규칙을 나타냅니다.

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // PDF/A-1a 검증
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // 업데이트된 PDF 파일 저장
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## TOC 작업하기

### 기존 PDF에 TOC 추가

aspose.pdf 패키지의 ListSection 클래스는 PDF 문서를 처음부터 생성할 때 목차를 생성할 수 있게 해줍니다. 목차의 요소인 제목을 추가하려면 [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 클래스를 사용하십시오.

기존 PDF 파일에 TOC를 추가하려면 com.aspose.pdf 패키지의 [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) 클래스를 사용하십시오. com.aspose.pdf 패키지는 새로운 PDF 파일을 생성하고 기존 PDF 파일을 조작할 수 있습니다. 기존 PDF에 목차를 추가하려면 com.aspose.pdf 패키지를 사용합니다.

다음 코드 스니펫은 기존 PDF 파일 내에 목차를 생성하는 방법을 보여줍니다.

```java
public static void AddTOCtoExistingPDF() {
    // 기존 PDF 파일 로드
    Document document = new Document(_dataDir + "sample.pdf");

    // PDF 파일의 첫 번째 페이지에 접근
    Page tocPage = document.getPages().insert(1);

    // 목차 정보를 나타내는 객체 생성
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // 목차 제목 설정
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // 목차 요소로 사용될 문자열 객체 생성
    String[] titles = new String[4];
    titles[0] = "First page";
    titles[1] = "Second page";
    titles[2] = "Third page";
    titles[3] = "Fourth page";
    for (int i = 0; i < 4; i++) {
      // Heading 객체 생성
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // Heading 객체의 목적지 페이지 지정
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // 목적지 페이지
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // 목적지 좌표
      segment2.setText(titles[i]);

      // 목차가 포함된 페이지에 heading 추가
      tocPage.getParagraphs().add(heading2);
    }
    // 업데이트된 문서 저장
    document.save("TOC_Output_Java.pdf");
  }
```
### 서로 다른 TOC 레벨에 대해 다른 TabLeaderType 설정

Aspose.PDF는 또한 서로 다른 TOC 레벨에 대해 다른 TabLeaderType을 설정할 수 있습니다. 다음과 같이 FormatArray의 LineDash 속성을 TabLeaderType 열거형의 적절한 값으로 설정해야 합니다.

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // 리더 유형 설정

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("목차");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // Pdf 문서의 섹션 컬렉션에 목록 섹션 추가

    tocPage.setTocInfo(tocInfo);

    // 각 레벨의 왼쪽 여백과 텍스트 포맷 설정을 통해 네 레벨 목록의 형식 정의

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // Pdf 문서에 섹션 생성
    Page page = document.getPages().add();

    // 섹션에 네 개의 머리글 추가
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("샘플 머리글" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // 목차에 머리글 추가.
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // PDF 저장
    document.save(outFile);
  }
```

### TOC에서 페이지 번호 숨기기

TOC에서 제목과 함께 페이지 번호를 표시하고 싶지 않은 경우, [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) 클래스의 [IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) 속성을 false로 사용할 수 있습니다. 다음 코드 스니펫을 확인하여 목차에서 페이지 번호를 숨기는 방법을 확인하세요:

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // Pdf 문서의 섹션 컬렉션에 목록 섹션 추가
    tocPage.setTocInfo(tocInfo);

    // 각 수준의 왼쪽 여백 및 텍스트 형식 설정을 설정하여 4개 수준 목록의 형식 정의

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // 섹션에 4개의 제목 추가
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("this is heading of level " + Level);
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```


### TOC 추가 시 페이지 번호 사용자 정의

PDF 문서에 TOC를 추가할 때 TOC의 페이지 번호를 사용자 정의하는 것이 일반적입니다. 예를 들어, P1, P2, P3 등과 같이 페이지 번호 앞에 접두사를 추가해야 할 수도 있습니다. 이러한 경우, Aspose.PDF for Java는 TocInfo 클래스의 PageNumbersPrefix 속성을 제공하여 다음 코드 샘플과 같이 페이지 번호를 사용자 정의할 수 있습니다.

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // 기존 PDF 파일 로드
    Document doc = new Document(inFile);
    // PDF 파일의 첫 번째 페이지에 접근
    Page tocPage = doc.getPages().insert(1);
    // TOC 정보를 나타내는 객체 생성
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // TOC 제목 설정
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // Heading 객체 생성
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // Heading 객체의 대상 페이지 지정
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // 대상 페이지
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // 대상 좌표
      segment2.setText("Page " + i);
      // TOC가 포함된 페이지에 Heading 추가
      tocPage.getParagraphs().add(heading2);
    }

    // 업데이트된 문서 저장
    doc.save(outFile);
  }
```


## PDF 파일에 레이어 추가

레이어는 PDF 문서에서 여러 가지 방법으로 사용될 수 있습니다. 다국어 파일을 배포하고자 할 때 각 언어의 텍스트가 다른 레이어에 나타나고 배경 디자인이 별도의 레이어에 나타나기를 원할 수 있습니다. 애니메이션이 별도의 레이어에 나타나는 문서를 생성할 수도 있습니다. 예를 들어, 파일에 라이선스 계약서를 추가하고 사용자가 계약 조건에 동의하기 전까지 내용을 보지 못하게 하고 싶을 때 사용할 수 있습니다.

Aspose.PDF for Java는 PDF 파일에 레이어를 추가하는 것을 지원합니다.

PDF 파일에서 레이어를 작업하려면 다음 API 멤버를 사용하십시오.

[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) 클래스는 레이어를 나타내며 다음과 같은 속성을 포함합니다:

- **Name** – 레이어의 이름.
- **Id** – 레이어의 ID.
- **Contents** – 레이어 연산자의 목록.

[Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) 객체가 정의되면, 이를 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 객체의 Layers 컬렉션에 추가하십시오.
 PDF 문서에 레이어를 추가하는 방법을 보여주는 코드입니다.

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "빨간 선");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "초록 선");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "파란 선");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## PDF 만료 설정

PDF 만료 기능은 PDF 파일이 유효한 기간을 설정합니다. 특정 날짜에 누군가가 접근하려고 하면, 파일이 만료되었고 새 파일이 필요하다는 설명이 포함된 팝업이 표시됩니다.

Aspose.PDF를 사용하면 PDF 파일을 생성하고 편집할 때 만료를 설정할 수 있습니다.

아래 코드 스니펫은 PDF 파일의 만료 날짜를 설정하는 방법을 보여줍니다. JavaScript를 사용해야 하며, 타사 구성 요소(예: OwnerGuard)로 저장된 파일은 해당 유틸리티 없이는 다른 워크스테이션에서 볼 수 없습니다.

PDF 파일은 만료 날짜가 있는 기존 파일을 사용하여 PDF OwnerGuard를 사용하여 생성할 수 있습니다. 그러나 새로운 파일은 PDF OwnerGuard가 설치된 워크스테이션에서만 열 수 있습니다. PDF OwnerGuard가 없는 워크스테이션은 ExpirationFeatureError를 반환합니다. 예를 들어, OwnerGuard가 설치된 경우 PDF Reader는 파일을 열지만 Adobe Acrobat은 오류를 반환합니다.

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```