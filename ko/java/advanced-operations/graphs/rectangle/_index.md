---
title: PDF 파일에 사각형 객체 추가
linktitle: 사각형 추가
type: docs
weight: 50
url: /ko/java/add-rectangle/
description: 이 문서에서는 Aspose.PDF for Java를 사용하여 PDF에 사각형 객체를 생성하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 사각형 객체 추가

Aspose.PDF for Java는 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 또한 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) 객체를 추가할 수 있는 기능도 제공하며, 특정 색상으로 사각형 객체를 채우거나, Z-Order를 제어하거나, 그라디언트 색상 채우기 등을 추가할 수 있습니다.

먼저 사각형 객체를 생성할 수 있는 가능성을 살펴보겠습니다.

다음 단계를 따르세요:

1. 새 PDF [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)를 생성합니다.

1. PDF 파일의 페이지 컬렉션에 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)를 추가합니다.

1. 페이지 인스턴스의 단락 컬렉션에 [텍스트 조각](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) 추가

1. [그래프](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) 인스턴스 생성

1. [그리기 객체](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)의 테두리 설정

1. 사각형 인스턴스 생성

1. 그래프 객체의 도형 컬렉션에 [사각형](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) 객체 추가

1. 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가

1. 페이지 인스턴스의 단락 컬렉션에 [텍스트 조각](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) 추가

1. 그리고 PDF 파일 저장

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Point;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.drawing.*;

public class WorkingWithGraphs {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ExampleRectangle() {

        // 새 PDF 문서 생성
        Document pdfDocument = new Document();

        // 페이지를 PDF 파일의 페이지 컬렉션에 추가
        Page page = pdfDocument.getPages().add();

        // 페이지 인스턴스의 단락 컬렉션에 텍스트 조각 추가
        page.getParagraphs().add(new TextFragment("텍스트 그래프 객체 전"));

        // 그래프 인스턴스 생성
        Graph graph = new Graph(400, 200);

        // 그리기 객체의 테두리 설정
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getRed());
        graph.setBorder(borderInfo);

        // 사각형 인스턴스 생성
        Rectangle rect = new Rectangle(10, 10, 380, 180);

        // 그래프 객체의 도형 컬렉션에 사각형 객체 추가
        graph.getShapes().add(rect);

        // 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가
        page.getParagraphs().add(graph);

        // 페이지 인스턴스의 단락 컬렉션에 텍스트 조각 추가
        page.getParagraphs().add(new TextFragment("텍스트 그래프 객체 후"));

        // PDF 파일 저장
        pdfDocument.save(_dataDir + "CreateRectangle_out.pdf");
    }
```


![Create Rectangle](create_rectangle.png)

## 채워진 직사각형 객체 생성

Aspose.PDF for Java는 특정 색상으로 직사각형 객체를 채우는 기능도 제공합니다.

다음 코드 스니펫은 색상으로 채워진 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 객체를 추가하는 방법을 보여줍니다.

```java
   public static void ExampleRectangleFilledSolidColor() {

        Document pdfDocument = new Document();

        // PDF 파일의 페이지 컬렉션에 페이지 추가
        Page page = pdfDocument.getPages().add();
        // Graph 인스턴스 생성
        Graph graph = new Graph(100, 400);

        // 페이지 인스턴스의 단락 컬렉션에 그래프 객체 추가
        page.getParagraphs().add(graph);

        // Rectangle 인스턴스 생성
        Rectangle rect = new Rectangle(100, 100, 200, 120);

        // Graph 객체에 채우기 색상 지정
        rect.getGraphInfo().setFillColor(Color.getRed());

        // Graph 객체의 도형 컬렉션에 직사각형 객체 추가
        graph.getShapes().add(rect);

        // PDF 파일 저장
        pdfDocument.save(_dataDir + "CreateFilledRectangle_out.pdf");
    }
```


사각형에 단색으로 채워진 결과를 보십시오:

![채워진 사각형](fill_rectangle.png)

## 그라데이션 채우기를 사용하여 그리기 추가

Aspose.PDF for Java는 PDF 문서에 그래프 객체를 추가하는 기능을 지원하며 때로는 그래프 객체를 그라데이션 색상으로 채우는 것이 필요합니다. 그래프 객체를 그라데이션 색상으로 채우기 위해, 우리는 다음과 같이 gradientAxialShading 객체와 함께 setPatterColorSpace를 설정해야 합니다.

다음 코드 스니펫은 그라데이션 색상으로 채워진 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 객체를 추가하는 방법을 보여줍니다.

```java
   public static void ExampleRectangleFilledGradient() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        Graph graph = new Graph(300, 300);
        page.getParagraphs().add(graph);
        Rectangle rect = new Rectangle(0, 0, 300, 300);
        graph.getShapes().add(rect);

        // 그래프 객체에 그라데이션 채우기 색상을 지정하고 채우기
        Color gradientFill = new com.aspose.pdf.Color();
        rect.getGraphInfo().setFillColor(gradientFill);

        GradientAxialShading gradientAxialShading = new GradientAxialShading(Color.getRed(), Color.getBlue());

        gradientAxialShading.setStart(new Point(0, 0));
        gradientAxialShading.setEnd(new Point(300, 300));
        gradientFill.setPatternColorSpace(gradientAxialShading);

        // PDF 파일 저장
        pdfDocument.save(_dataDir + "AddDrawingWithGradientFill_out.pdf");
    }
```


![Gradient Rectangle](gradient.png)

## 알파 색상 채널로 사각형 생성

Aspose.PDF for Java는 특정 색상으로 사각형 객체를 채우는 것을 지원합니다. 사각형 객체는 또한 투명한 외관을 주기 위해 알파 색상 채널을 가질 수 있습니다. 다음 코드 조각은 알파 색상 채널을 가진 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 객체를 추가하는 방법을 보여줍니다.

이미지의 픽셀은 색상 값과 함께 불투명도에 대한 정보를 저장할 수 있습니다. 이를 통해 투명 또는 반투명 영역이 있는 이미지를 만들 수 있습니다.

색상을 투명하게 만드는 대신, 각 픽셀은 얼마나 불투명한지에 대한 정보를 저장합니다. 이 불투명도 데이터는 알파 채널이라고 하며, 일반적으로 픽셀의 색상 채널 뒤에 저장됩니다.

우리의 코드 스니펫에서는 [com.aspose.pdf.Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color)의 [fromArgb](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color#fromArgb-int-int-int-) 메서드를 사용했습니다.
 값을 지정해야 합니다. 처음 세 개는 색상 구성 요소로, 0에서 255 범위로 지정되며, 마지막은 0에서 1까지의 소수로 지정된 불투명도 수준(알파 채널)입니다.

```java
    public static void ExampleRectangleAlphaChannelColor() {
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Graph 인스턴스 생성
        Graph graph = new Graph(100, 400);

        // 특정 크기의 사각형 객체 생성
        Rectangle rect1 = new Rectangle(100, 100, 200, 100);
        Color color1 = Color.fromArgb(128, 224, 0, 224);
        rect1.getGraphInfo().setFillColor(color1);
        // Graph 인스턴스의 도형 컬렉션에 사각형 객체 추가
        graph.getShapes().add(rect1);

        // 두 번째 사각형 객체 생성
        Rectangle rect2 = new Rectangle(200, 150, 200, 100);
        Color color2 = Color.fromArgb(64, 0, 224, 224);
        rect2.getGraphInfo().setFillColor(color2);
        graph.getShapes().add(rect2);

        // 페이지 객체의 단락 컬렉션에 그래프 인스턴스 추가
        page.getParagraphs().add(graph);

        // PDF 파일 저장
        pdfDocument.save(_dataDir + "CreateRectangleWithAlphaColor_out.pdf");
    }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## 사각형의 Z-Order 제어

Aspose.PDF for Java는 PDF 문서에 그래프 객체(예: 그래프, 선, 사각형 등)를 추가하는 기능을 지원합니다. 동일한 객체의 인스턴스를 PDF 파일에 여러 개 추가할 때, Z-Order를 지정하여 렌더링을 제어할 수 있습니다. Z-Order는 객체를 서로 겹쳐서 렌더링해야 할 때도 사용됩니다.

다음 코드 스니펫은 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 객체를 서로 겹쳐서 렌더링하는 단계를 보여줍니다.

```java
   public static void Controlling_Z_Order() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // 색상이 빨간색이고 Z-Order가 0이며 특정 치수를 가진 새 사각형 생성
        AddRectangle(page, 50, 40, 60, 40, Color.getRed(), 2);
        // 색상이 파란색이고 Z-Order가 0이며 특정 치수를 가진 새 사각형 생성
        AddRectangle(page, 20, 20, 30, 30, Color.getBlue(), 1);
        // 색상이 초록색이고 Z-Order가 0이며 특정 치수를 가진 새 사각형 생성
        AddRectangle(page, 40, 40, 60, 30, Color.getGreen(), 0);

        // 결과 PDF 파일 저장
        pdfDocument.save(_dataDir + "ControlRectangleZOrder_out.pdf");

    }
```


![Z 순서 제어](control.png)