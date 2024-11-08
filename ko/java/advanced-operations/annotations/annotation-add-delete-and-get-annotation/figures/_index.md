---
title: PDF 도형 주석
linktitle: 도형 주석
type: docs
weight: 30
url: /ko/java/figures-annotation/
description: 이 문서는 Java용 Aspose.PDF를 사용하여 PDF 문서에 도형 주석을 추가하고, 가져오고, 삭제하는 방법을 설명합니다.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 사각형 또는 원 주석 추가

사각형 및 원 주석은 각각 페이지에 사각형 또는 타원을 표시합니다. 열릴 때 관련 메모의 텍스트가 포함된 팝업 창을 표시합니다. 사각형 주석은 모양을 제외하고 원 주석(Aspose.Pdf.Annotations.CircleAnnotation 클래스의 인스턴스)과 유사합니다.

사각형 및 원 주석을 생성하는 단계:

1. PDF 파일 로드 - 새로운 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. 새로운 [Circle Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/circleannotation)을 생성하고 Circle 매개변수(새 Rectangle, 제목, 색상, InteriorColor, 불투명도)를 설정합니다.
1. 새로운 [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation)을 생성합니다.
1. 다음으로 [Square Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquareAnnotation)을 생성해야 합니다.
1. 동일한 Square 매개변수(새 Rectangle, 제목, 색상, InteriorColor, 불투명도)를 설정합니다.
1. 그런 다음 페이지에 Square 및 Circle Annotation을 추가해야 합니다.

다음 코드 스니펫은 PDF 페이지에 Circle Annotation을 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCircleAnnotation {

    // 문서 디렉토리의 경로입니다.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCircleAnnotation() {
        try {
            // PDF 파일을 로드합니다.
            Document document = new com.aspose.pdf.Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // 다각형 주석을 생성합니다.
            CircleAnnotation circleAnnotation = new CircleAnnotation(page, new Rectangle(270, 160, 483, 383));
            circleAnnotation.setTitle("John Smith");
            circleAnnotation.setColor(Color.getRed());
            circleAnnotation.setInteriorColor(Color.getMistyRose());
            circleAnnotation.setOpacity(0.5);
            circleAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 316, 1021, 459)));

            // 사각형 주석을 생성합니다.
            SquareAnnotation squareAnnotation = new SquareAnnotation(page, new Rectangle(67, 317, 261, 459));
            squareAnnotation.setTitle("John Smith");
            squareAnnotation.setColor(Color.getBlue());
            squareAnnotation.setInteriorColor(Color.getBlueViolet());
            squareAnnotation.setOpacity(0.25);
            squareAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // 페이지에 주석을 추가합니다.
            page.getAnnotations().add(circleAnnotation);
            page.getAnnotations().add(squareAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


예를 들어, PDF 문서에 사각형 및 원 주석을 추가한 결과는 다음과 같습니다:

![원 및 사각형 주석 데모](circle_demo.png)

## 원 주석 가져오기

다음 코드 스니펫을 사용하여 PDF 문서에서 원 주석을 가져와 보십시오.

```java
public static void GetCircleAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // 결과 출력
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## 원 주석 삭제

다음 코드 스니펫은 PDF 파일에서 원 주석을 삭제하는 방법을 보여줍니다.

```java
public static void DeleteCircleAnnotation() {
        // PDF 파일 불러오기
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> circleAnnotations = annotationSelector.getSelected();

        for (Annotation ca : circleAnnotations) {
            page.getAnnotations().delete(ca);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
```

## 다각형 및 폴리라인 주석 추가

폴리라인 도구를 사용하면 문서에 임의의 개수의 변을 가진 도형과 윤곽선을 만들 수 있습니다.

**다각형 주석**은 페이지에 다각형을 나타냅니다. 직선으로 연결된 임의의 개수의 꼭짓점을 가질 수 있습니다.

**폴리라인 주석** 또한 다각형과 유사하지만, 유일한 차이점은 첫 번째와 마지막 꼭짓점이 암묵적으로 연결되지 않는다는 것입니다.

Steps with which we create Polygon and Polyline annotations:

1. PDF 파일을 로드합니다 - new [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. 새로운 [Polygon Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/PolygonAnnotation)을 만들고 Polygon 매개변수 (new Rectangle, new Points, title, color, InteriorColor 및 Opacity)를 설정합니다.
1. 새로운 [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PopupAnnotation)을 만듭니다.
1. 다음으로, [PolyLine Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PolylineAnnotation)을 만들고 모든 작업을 반복합니다.
1. 그런 다음 페이지에 주석을 추가할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 Polygon 및 Polyline 주석을 추가하는 방법을 보여줍니다:

```java
 package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExamplePolygonAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddPolynnotation() {
        try {
            // PDF 파일 로드
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // Polygon Annotation 생성
            PolygonAnnotation polygonAnnotation = new PolygonAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(274, 381), new Point(555, 381), new Point(555, 304), new Point(570, 304),
                            new Point(570, 195), new Point(274, 195) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getBlue());
            polygonAnnotation.setInteriorColor(Color.getBlueViolet());
            polygonAnnotation.setOpacity(0.25);
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // PoliLine Annotation 생성
            PolylineAnnotation polylineAnnotation = new PolylineAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(545, 150), new Point(545, 190), new Point(667, 190), new Point(667, 110),
                            new Point(626, 111) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getRed());
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // 페이지에 주석 추가
            page.getAnnotations().add(polygonAnnotation);
            page.getAnnotations().add(polylineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## 다각형 및 폴리라인 주석 가져오기

PDF 문서에서 다각형 및 폴리라인 주석을 가져오려면 다음 코드 스니펫을 사용해 보세요.

```java
    public static void GetPolyAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "Appartments_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector = new AnnotationSelector(
                new PolylineAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> polyAnnotations = annotationSelector.getSelected();

        for (Annotation pa : polyAnnotations) {
            System.out.printf("[%s]", pa.getRect());
        }
    }
```

## 다각형 및 폴리라인 주석 삭제

다음 코드 스니펫은 PDF 파일에서 다각형 및 폴리라인 주석을 삭제하는 방법을 보여줍니다.

```java
        public static void DeletePolyAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "Appartments_mod.pdf");
        Page page = document.getPages().get_Item(1);

        AnnotationSelector annotationSelector = new AnnotationSelector(
                new PolylineAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> polyAnnotations = annotationSelector.getSelected();

        for (Annotation pa : polyAnnotations) {
            page.getAnnotations().delete(pa);
        }

        document.save(_dataDir + "Appartments_del.pdf");
    }
```


## 기존 PDF 파일에 선 주석 추가하는 방법

선 주석(Line Annotation)의 목적은 페이지에 단일 직선을 표시하는 것입니다. 열리면 관련 메모의 텍스트를 포함하는 팝업 창이 표시됩니다. 이 기능은 선 주석에 특정한 추가 항목을 포함합니다. 이러한 항목은 LL, BS, IC 등과 같은 문자 형식으로 암호화됩니다.

또한, 선 주석에는 Cap을 `true`로 설정하여 주석에 캡션을 포함할 수 있습니다.

다음 기능은 리더 오프셋이 있는 선 주석에 캡션을 적용하는 효과를 허용합니다.
또한 이러한 유형의 주석은 선 끝 스타일을 정의할 수 있도록 합니다.

선 주석을 생성하는 단계:

1. PDF 파일 불러오기 - 새로운 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. 새로운 [Line Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation)을 만들고 선 매개변수(새 Rectangle, 새 Point, 제목, 색상, 너비, StartingStyle 및 EndingStyle)를 설정합니다.

1. 새 [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation)을 생성합니다.
1. 그런 다음 페이지에 주석을 추가할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 라인 주석을 추가하는 방법을 보여줍니다:

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLineAnnotation {

    // 문서 디렉토리 경로입니다.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLineAnnotation() {
        try {
            // PDF 파일을 로드합니다
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // 라인 주석을 생성합니다
            LineAnnotation lineAnnotation = new LineAnnotation(page, new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443));

            lineAnnotation.setTitle("John Smith");
            lineAnnotation.setColor(Color.getRed());
            lineAnnotation.setWidth(3);
            lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
            lineAnnotation.setEndingStyle(LineEnding.OpenArrow);
            lineAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 124, 1021, 266)));

            // 페이지에 주석을 추가합니다
            page.getAnnotations().add(lineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## 선 주석 가져오기

PDF 문서에서 선 주석을 가져오려면 다음 코드 스니펫을 사용해 보세요.

```java
    public static void GetLineAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // 결과 출력
        for (Annotation la : lineAnnotations) {
            LineAnnotation l = (LineAnnotation) la;
            System.out.println("[" + l.getStarting().getX() + "," + l.getStarting().getY() + "]" + "["
                    + l.getEnding().getX() + "," + l.getEnding().getY() + "]");
        }
    }
```

## 선 주석 삭제하기

다음 코드는 PDF 파일에서 선 주석을 삭제하는 방법을 보여줍니다.

```java
   public static void DeleteLineAnnotation() {
        // PDF 파일 로드
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // 결과 출력
        for (Annotation la : lineAnnotations) {
            page.getAnnotations().delete(la);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
}
```

## PDF 파일에 잉크 주석 추가하는 방법

잉크 주석은 하나 이상의 분리된 경로로 구성된 자유형 "낙서"를 나타냅니다.
 열면 관련 메모의 텍스트가 포함된 팝업 창이 표시됩니다.

[InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation)은 하나 이상의 분리된 점으로 구성된 자유롭게 그린 낙서를 나타냅니다. PDF 문서에 InkAnnotation을 추가하려면 다음 코드 스니펫을 사용해 보세요.

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleInkAnnotation {

    // 문서 디렉토리 경로.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";


    public static void AddInkAnnotation() {
        try {
            // PDF 파일 로드
            Document document = new com.aspose.pdf.Document(_dataDir + "Appartments.pdf");
            Page page = document.getPages().get_Item(1);
            Rectangle arect = new Rectangle(320.086,189.286,384.75,228.927);
            List<Point[]> inkList = new ArrayList<Point[]>();
            //마우스 또는 다른 포인팅 장치로부터 수신된 ppt 데이터
            double ppts[] = { 328.002, 222.017, 328.648, 222.017, 329.294, 222.017, 329.617, 222.34, 330.91, 222.663,
                    331.556, 222.663, 332.203, 222.986, 333.495, 223.633, 334.141, 223.956, 334.788, 224.279, 335.434,
                    224.602, 336.08, 224.602, 336.727, 224.925, 337.373, 225.248, 337.696, 225.248, 338.342, 225.572,
                    338.989, 225.895, 341.897, 225.895, 343.513, 226.218, 346.098, 226.218, 348.683, 226.541, 350.622,
                    226.541, 352.238, 226.541, 353.208, 226.541, 353.854, 226.541, 355.146, 226.541, 356.439, 226.541,
                    357.732, 226.541, 358.378, 226.541, 359.024, 226.541, 360.64, 226.541, 361.286, 226.541, 361.933,
                    226.541, 362.256, 226.541, 362.902, 226.541, 363.548, 226.541, 363.872, 226.541, 363.872, 226.218,
                    365.164, 226.218, 365.487, 226.218, 365.811, 226.218, 367.103, 226.218, 367.749, 226.218, 368.719,
                    226.218, 370.012, 226.218, 370.981, 226.218, 371.627, 226.218, 372.597, 225.895, 372.92, 225.895,
                    373.243, 225.895, 373.243, 225.572, 373.566, 225.572, 374.213, 225.248, 374.536, 225.248, 375.182,
                    224.602, 375.182, 224.279, 375.828, 223.956, 376.475, 223.31, 377.121, 222.986, 377.767, 222.986,
                    378.414, 222.017, 379.383, 221.371, 379.706, 220.724, 380.029, 219.432, 380.676, 219.109, 380.676,
                    218.462, 381.645, 217.493, 381.968, 217.17, 381.968, 216.523, 382.291, 215.554, 382.615, 215.231,
                    382.615, 214.261, 382.938, 213.292, 382.938, 212.645, 382.938, 211.999, 382.938, 211.353, 382.938,
                    210.707, 382.938, 209.737, 382.938, 208.768, 382.938, 208.444, 382.615, 207.475, 382.615, 206.829,
                    382.291, 206.505, 382.291, 205.859, 381.968, 204.89, 381.968, 204.243, 381.645, 203.92, 380.999,
                    203.274, 380.999, 202.951, 380.676, 202.305, 380.353, 201.658, 380.029, 201.335, 380.029, 200.689,
                    380.029, 200.366, 379.383, 199.719, 379.06, 199.719, 378.737, 199.073, 377.767, 198.103, 377.121,
                    197.780, 376.475, 197.457, 375.505, 196.488, 374.859, 196.165, 374.536, 195.841, 372.92, 195.195,
                    371.951, 194.549, 370.658, 194.226, 368.719, 193.902, 367.426, 193.256, 366.457, 193.256, 363.872,
                    192.933, 362.902, 192.933, 361.61, 192.61, 359.024, 192.61, 357.409, 192.61, 356.439, 192.61,
                    353.531, 192.61, 352.561, 192.61, 350.945, 192.61, 349.007, 192.933, 348.36, 193.256, 347.391,
                    193.256, 346.098, 193.902, 345.452, 193.902, 344.806, 193.902, 343.513, 193.902, 342.867, 193.902,
                    342.220, 193.902, 341.574, 193.902, 341.251, 194.226, 340.928, 194.226, 340.928, 194.549, 340.605,
                    194.549, 340.605, 194.872, 339.635, 195.195, 339.635, 195.518, 338.989, 195.518, 338.989, 195.841,
                    338.666, 196.165, 338.019, 196.811, 338.019, 197.134, 337.373, 197.457, 336.404, 198.427, 335.757,
                    198.427, 335.434, 198.75, 334.141, 199.719, 333.818, 199.719, 333.818, 200.042, 332.849, 200.366,
                    332.203, 200.366, 331.556, 201.335, 330.91, 201.981, 330.587, 202.305, 330.264, 202.305, 329.294,
                    202.628, 328.971, 202.951, 328.002, 203.274, 328.002, 203.597, 327.355, 204.243, 326.709, 204.567,
                    326.386, 204.89, 326.063, 205.536, 325.416, 205.859, 325.093, 205.859, 324.447, 205.859, 324.124,
                    206.182, 324.124, 206.505, 323.477, 206.829, 323.477, 207.152, 323.477, 207.798, 322.831, 207.798,
                    322.831, 208.121, 322.831, 208.444, 322.508, 208.444, 322.508, 209.091, 322.185, 209.414, 322.185,
                    209.737, 322.185, 210.383, 322.185, 211.03, 322.185, 211.353, 322.185, 211.676, 322.185, 212.322,
                    323.154, 213.292, 323.154, 213.938, 324.447, 214.584, 325.093, 215.877, 325.416, 216.2, 325.416,
                    216.846, 325.739, 217.17, 326.063, 217.493, 326.386, 218.139, 326.709, 218.139, 326.709, 218.462,
                    327.032, 219.109, 327.032, 219.432, 327.032, 219.755, 327.355, 220.078, 327.355, 220.401, 327.678,
                    221.371, 328.002, 221.371, 328.002, 222.017, 328.325, 222.663, 328.648, 222.663, 328.971, 222.986,
                    329.294, 223.31, 329.617, 223.956, 329.617, 224.279 };

            //데이터를 포인트로 변환
            Point[] arrpt = new Point[ppts.length/2];
            for (int i = 0, j=0; i < arrpt.length; i++, j+=2) {
                arrpt[i] = new Point(ppts[j],ppts[j+1]);
            }
            inkList.add(arrpt);

            InkAnnotation ia = new InkAnnotation(page, arect, inkList);
            ia.setTitle("Aspose User");
            ia.setColor(Color.getRed());
            ia.setCapStyle(CapStyle.Rounded);

            Border border = new Border(ia);
            border.setWidth(3);
            ia.setOpacity(0.75);

            page.getAnnotations().add(ia);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```

## PDF에서 InkAnnotation 가져오기

다음 코드 스니펫을 사용하여 [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation)을 가져올 수 있습니다:

```java
public static void GetInkAnnotation() {
        // PDF 파일 불러오기
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> inkAnnotations = annotationSelector.getSelected();

        // 결과 출력
        for (Annotation ia : inkAnnotations) {
            System.out.println(ia.getRect());
        }
    }
```

## InkAnnotation 삭제

Aspose.PDF for Java를 사용하여 PDF 파일에서 [InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation)을 삭제할 수 있습니다.

```java
public static void DeleteInkAnnotation() {
        // PDF 파일 불러오기
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // AnnotationSelector를 사용하여 주석 필터링
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> InkAnnotations = annotationSelector.getSelected();

        for (Annotation ca : InkAnnotations) {
            page.getAnnotations().delete(ca);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
```