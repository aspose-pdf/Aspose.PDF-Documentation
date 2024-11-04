---
title: 페이지 속성 가져오기 및 설정
type: docs
weight: 30
url: /java/get-and-set-page-properties/
description: 이 주제는 Aspose.PDF for Java를 사용하여 PDF 파일에서 숫자를 가져오고, 페이지 속성을 가져오고, 페이지 색상을 결정하는 방법을 설명합니다.
lastmod: "2021-06-05"
---

Aspose.PDF for Java를 사용하면 Java 애플리케이션에서 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다. 이 섹션에서는 PDF 파일에서 페이지 수를 가져오고, PDF 페이지 속성 정보(예: 색상)를 가져오고, 페이지 속성을 설정하는 방법을 보여줍니다.

## PDF 파일의 페이지 수 가져오기

문서를 작업할 때 종종 몇 페이지인지 알고 싶어합니다. Aspose.PDF를 사용하면 이 작업은 두 줄의 코드로 가능합니다.

PDF 파일의 페이지 수를 가져오려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF 파일을 엽니다.

1. 그런 다음 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) 컬렉션의 Count 속성(문서 객체에서 사용)을 사용하여 문서의 총 페이지 수를 가져옵니다.

다음 코드 스니펫은 PDF 파일의 페이지 수를 얻는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleGetAndSetPageProperties {
    // 문서 디렉터리 경로.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GetNumberOfPagesInaPDFFile() {

        // 문서 열기
        Document pdfDocument = new Document(_dataDir + "GetNumberofPages.pdf");

        // 페이지 수 가져오기
        System.out.println("Page Count : " + pdfDocument.getPages().size());
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDocument.save(_dataDir);

    }
```

### 문서를 저장하지 않고 페이지 수 가져오기

PDF 파일이 저장되고 모든 요소가 실제로 PDF 파일 안에 배치되지 않는 한 특정 문서에 대한 페이지 수를 얻을 수 없습니다 (모든 요소가 수용될 페이지 수를 확신할 수 없기 때문입니다).
 그러나 Aspose.PDF for Java 10.1.0 릴리스부터 파일을 저장하지 않고 PDF 문서의 페이지 수를 얻을 수 있는 기능을 제공하는 [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--)라는 메서드를 도입했습니다. 따라서 페이지 수 정보를 실시간으로 얻을 수 있습니다. 이 요구 사항을 충족하기 위해 다음 코드 스니펫을 사용해 보십시오.

```java
public static void GetPageCountWithoutSavingTheDocument() {

        // 전체 예제 및 데이터 파일은 다음을 참조하십시오.
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        // Document 인스턴스 생성
        Document doc = new Document();
        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = doc.getPages().add();
        // 300개의 TextFragment 인스턴스를 추가하기 위한 루프 생성
        for (int i = 0; i < 300; i++)
            // PDF의 첫 번째 페이지의 단락 컬렉션에 TextFragment 추가
            page.getParagraphs().add(new TextFragment("페이지 수 테스트"));
        // 페이지 수 정보를 얻기 위해 단락 처리
        doc.processParagraphs();
        System.out.println("PDF의 페이지 수 = " + doc.getPages().size());
    }
```

## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 여백상자, 자르기 상자 및 트림 상자와 같은 여러 속성이 있습니다. Aspose.PDF를 사용하면 이러한 속성에 액세스할 수 있습니다.

### **페이지 속성 이해하기: Artbox, BleedBox, CropBox, MediaBox, TrimBox 및 Rect 속성의 차이점**

- **미디어 상자**: 미디어 상자는 가장 큰 페이지 상자입니다. 이는 PostScript 또는 PDF로 문서를 인쇄할 때 선택된 페이지 크기(A4, A5, US Letter 등)에 해당합니다. 즉, 미디어 상자는 PDF 문서가 표시되거나 인쇄되는 미디어의 물리적 크기를 결정합니다.
- **블리드 상자**: 문서에 블리드가 있는 경우 PDF에도 블리드 상자가 포함됩니다.
 블리드는 페이지의 가장자리를 넘어 확장되는 색상(또는 아트워크)의 양입니다. 문서가 인쇄되고 크기에 맞춰 잘릴 때(“트림”) 잉크가 페이지의 가장자리까지 도달하도록 하기 위해 사용됩니다. 페이지가 잘못 잘리더라도 - 트림 마크에서 약간 벗어나 잘리더라도 - 페이지에 흰 가장자리가 나타나지 않습니다.

- **트림 박스**: 트림 박스는 인쇄 및 트림 후 문서의 최종 크기를 나타냅니다.
- **아트 박스**: 아트 박스는 문서의 페이지 실제 내용 주위에 그려진 박스입니다. 이 페이지 박스는 다른 애플리케이션에서 PDF 문서를 가져올 때 사용됩니다.
- **크롭 박스**: 크롭 박스는 Adobe Acrobat에서 PDF 문서가 표시되는 "페이지" 크기입니다. 일반 보기에서는 Adobe Acrobat에서 크롭 박스의 콘텐츠만 표시됩니다. 이러한 속성에 대한 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **페이지.Rect**: MediaBox와 DropBox의 교차점(일반적으로 보이는 사각형)입니다. 아래 그림은 이러한 속성을 설명합니다.

자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

### 페이지 속성 접근하기

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스는 특정 PDF 페이지와 관련된 모든 속성을 제공합니다. PDF 파일의 모든 페이지는 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PageCollection) 컬렉션에 포함되어 있습니다.

여기에서 인덱스를 사용하여 개별 Page 객체에 접근하거나, foreach 루프를 사용하여 컬렉션을 반복하면서 모든 페이지를 가져올 수 있습니다. 개별 페이지에 접근하면 해당 페이지의 속성을 얻을 수 있습니다. 다음 코드 스니펫은 페이지 속성을 가져오는 방법을 보여줍니다.

```java
    public static void AccessingPageProperties() {

        Document pdfDocument = new Document("input.pdf");

        // 페이지 컬렉션 가져오기
        PageCollection pageCollection = pdfDocument.getPages();

        // 특정 페이지 가져오기
        Page pdfPage = pageCollection.get_Item(1);

        // 페이지 속성 가져오기
        System.out.printf("\n ArtBox : Height = " + pdfPage.getArtBox().getHeight() + ", Width = "
                + pdfPage.getArtBox().getWidth() + ", LLX = " + pdfPage.getArtBox().getLLX() + ", LLY = "
                + pdfPage.getArtBox().getLLY() + ", URX = " + pdfPage.getArtBox().getURX() + ", URY = "
                + pdfPage.getArtBox().getURY());
        System.out.printf("\n BleedBox : Height = " + pdfPage.getBleedBox().getHeight() + ", Width = "
                + pdfPage.getBleedBox().getWidth() + ", LLX = " + pdfPage.getBleedBox().getLLX() + ", LLY = "
                + pdfPage.getBleedBox().getLLY() + ", URX = " + pdfPage.getBleedBox().getURX() + ", URY = "
                + pdfPage.getBleedBox().getURY());
        System.out.printf("\n CropBox : Height = " + pdfPage.getCropBox().getHeight() + ", Width = "
                + pdfPage.getCropBox().getWidth() + ", LLX = " + pdfPage.getCropBox().getLLX() + ", LLY = "
                + pdfPage.getCropBox().getLLY() + ", URX = " + pdfPage.getCropBox().getURX() + ", URY = "
                + pdfPage.getCropBox().getURY());
        System.out.printf("\n MediaBox : Height = " + pdfPage.getMediaBox().getHeight() + ", Width = "
                + pdfPage.getMediaBox().getWidth() + ", LLX = " + pdfPage.getMediaBox().getLLX() + ", LLY = "
                + pdfPage.getMediaBox().getLLY() + ", URX = " + pdfPage.getMediaBox().getURX() + ", URY = "
                + pdfPage.getMediaBox().getURY());
        System.out.printf("\n TrimBox : Height = " + pdfPage.getTrimBox().getHeight() + ", Width = "
                + pdfPage.getTrimBox().getWidth() + ", LLX = " + pdfPage.getTrimBox().getLLX() + ", LLY = "
                + pdfPage.getTrimBox().getLLY() + ", URX = " + pdfPage.getTrimBox().getURX() + ", URY = "
                + pdfPage.getTrimBox().getURY());
        System.out.printf(
                "\n Rect : Height = " + pdfPage.getRect().getHeight() + ", Width = " + pdfPage.getRect().getWidth()
                        + ", LLX = " + pdfPage.getRect().getLLX() + ", LLY = " + pdfPage.getRect().getLLY() + ", URX = "
                        + pdfPage.getRect().getURX() + ", URY = " + pdfPage.getRect().getURY());
        System.out.printf("\n Page Number :- " + pdfPage.getNumber());
        System.out.printf("\n Rotate :-" + pdfPage.getRotate());
    }
```

## 페이지 색상 결정

[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스는 PDF 문서의 특정 페이지와 관련된 속성을 제공하며, 페이지가 사용하는 색상 유형 - RGB, 흑백, 그레이스케일 또는 정의되지 않음 - 을 포함합니다.

모든 PDF 파일의 페이지는 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 컬렉션에 포함되어 있습니다. [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) 속성은 페이지의 요소 색상을 지정합니다. 특정 PDF 페이지의 색상 정보를 가져오거나 결정하려면 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 클래스 객체의 [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) 속성을 사용하십시오.

다음 코드 스니펫은 PDF 파일의 개별 페이지를 반복하여 색상 정보를 얻는 방법을 보여줍니다.

```java
    public static void DeterminePageColor () {

        Document pdfDocument = new Document("input.pdf");
        // PDF 파일의 모든 페이지를 반복합니다.
        for (int pageCount = 1; pageCount <= pdfDocument.getPages().size(); pageCount++) {
            // 특정 PDF 페이지의 색상 유형 정보를 가져옵니다.
            int pageColorType = pdfDocument.getPages().get_Item(pageCount).getColorType();
            switch (pageColorType) {
            case 2:
                System.out.println("페이지 # -" + pageCount + " 는 흑백입니다..");
                break;
            case 1:
                System.out.println("페이지 # -" + pageCount + " 는 그레이스케일입니다...");
                break;
            case 0:
                System.out.println("페이지 # -" + pageCount + " 는 RGB입니다..");
                break;
            case 3:
                System.out.println("페이지 # -" + pageCount + " 색상이 정의되지 않았습니다..");
                break;
            }
        }
    }
}
```