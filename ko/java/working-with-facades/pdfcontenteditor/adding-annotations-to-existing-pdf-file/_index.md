---
title: 기존 PDF 파일에 주석 추가
type: docs
weight: 80
url: /ko/java/adding-annotations-to-existing-pdf-file/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 기존 PDF 파일에 주석을 추가하는 방법을 설명합니다.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 기존 PDF 파일에 자유 텍스트 주석 추가 (facades)

자유 텍스트 주석은 페이지에 직접 텍스트를 표시합니다. [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)를 사용하면 기존 PDF 파일에 다양한 유형의 주석을 추가할 수 있습니다. 특정 주석을 추가하기 위해 해당 메소드를 사용할 수 있습니다. 예를 들어, 다음 코드 스니펫에서는 [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) 메소드를 사용하여 FreeText 유형 주석을 추가했습니다.

어떤 유형의 주석도 동일한 방식으로 PDF 파일에 추가할 수 있습니다.
 우선, [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 유형의 객체를 생성하고 bindPdf 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 둘째로, 주석의 영역을 지정하기 위해 Rectangle 객체를 생성해야 합니다. 그 후, [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) 메서드를 호출하여 자유 텍스트 주석을 추가하고, 주석이 위치한 페이지 번호를 지정한 다음, save 메서드를 사용하여 업데이트된 PDF 파일을 저장할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 자유 텍스트 주석을 추가하는 방법을 보여줍니다.

```java
  public static void AddFreeTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createFreeText(rect, "Free Text Demo", 1); // 마지막 매개변수는 페이지 번호입니다
        editor.save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
    }
```

## 기존 PDF 파일에 텍스트 주석 추가 (facades)

이 예제에서도 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 타입의 객체를 생성하고 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 두 번째로, 주석의 영역을 지정하기 위해 Rectangle 객체를 생성해야 합니다. 그 후, [createFreeText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createFreeText-java.awt.Rectangle-java.lang.String-int-) 메서드를 호출하여 FreeText 주석을 추가하고, 주석의 제목과 주석이 위치한 페이지 번호를 생성할 수 있습니다.

```java
 public static void AddTextAnnotation()
    {
        var document = new Document(_dataDir + "sample.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
        tfa.visit(document.getPages().get_Item(1));

        java.awt.Rectangle rect = new  java.awt.Rectangle();
        rect.x = (int)tfa.getTextFragments().get_Item(1).getRectangle().getLLX();
        rect.y = (int)tfa.getTextFragments().get_Item(1).getRectangle().getURY() + 5;
        rect.height = 18;
        rect.width = 100;        

        editor.createText(rect, "Aspose User", "PDF는 현대 문서에 더 적합한 형식입니다", false, "Key", 1);
        editor.save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
    }
```


## 기존 PDF 파일에 선 주석 추가하기 (외관)

우리는 또한 사각형, 선의 시작과 끝의 좌표, 페이지 번호, 주석 프레임의 두께, 스타일 및 색상, 선 대시 유형, 선의 시작 및 끝 유형을 지정합니다.

```java

    public static void AddLineAnnotation()
    {
        var document = new Document(_dataDir + "Appartments.pdf");
        PdfContentEditor editor = new PdfContentEditor(document);
        // 선 주석 생성
        editor.createLine(
            new java.awt.Rectangle(550, 93, 562, 439),
            "Test",
            556, 99, 556, 443, 1, 1,
            java.awt.Color.RED,
            "dash",
            new int[] { 1, 0, 3 },
            new String[] { "Open", "Open" });
        editor.save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
    }
```