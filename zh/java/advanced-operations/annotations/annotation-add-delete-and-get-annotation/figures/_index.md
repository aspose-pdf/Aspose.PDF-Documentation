---
title: PDF 图形注释
linktitle: 图形注释
type: docs
weight: 30
url: /zh/java/figures-annotation/
description: 本文描述了如何使用 Aspose.PDF for Java 在 PDF 文档中添加、获取和删除图形注释
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 添加方形或圆形注释

方形和圆形注释分别在页面上显示矩形或椭圆。打开时，它们会显示一个包含相关注释文本的弹出窗口。方形注释类似于圆形注释（Aspose.Pdf.Annotations.CircleAnnotation 类的实例），除了形状不同。

创建方形和圆形注释的步骤：

1. 加载 PDF 文件 - new [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. 创建新的 [Circle Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/circleannotation) 并设置圆形参数（新矩形、标题、颜色、内部颜色、不透明度）。
1. 创建一个新的 [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation)。
1. 接下来我们需要创建 [Square Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/SquareAnnotation)。
1. 设置相同的正方形参数（新矩形、标题、颜色、内部颜色、不透明度）。
1. 之后我们需要将方形和圆形注释添加到页面中。

以下代码片段向您展示如何在 PDF 页面中添加圆形注释。

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleCircleAnnotation {

    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddCircleAnnotation() {
        try {
            // 加载 PDF 文件
            Document document = new com.aspose.pdf.Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // 创建多边形注释
            CircleAnnotation circleAnnotation = new CircleAnnotation(page, new Rectangle(270, 160, 483, 383));
            circleAnnotation.setTitle("John Smith");
            circleAnnotation.setColor(Color.getRed());
            circleAnnotation.setInteriorColor(Color.getMistyRose());
            circleAnnotation.setOpacity(0.5);
            circleAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 316, 1021, 459)));

            // 创建方形注释
            SquareAnnotation squareAnnotation = new SquareAnnotation(page, new Rectangle(67, 317, 261, 459));
            squareAnnotation.setTitle("John Smith");
            squareAnnotation.setColor(Color.getBlue());
            squareAnnotation.setInteriorColor(Color.getBlueViolet());
            squareAnnotation.setOpacity(0.25);
            squareAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // 将注释添加到页面
            page.getAnnotations().add(circleAnnotation);
            page.getAnnotations().add(squareAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


作为一个例子，我们将看到在 PDF 文档中添加方形和圆形注释的结果：

![圆形和方形注释演示](circle_demo.png)

## 获取圆形注释

请尝试使用以下代码片段从 PDF 文档中获取圆形注释。

```java
public static void GetCircleAnnotation() {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // 使用 AnnotationSelector 过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new CircleAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> caretAnnotations = annotationSelector.getSelected();

        // 打印结果
        for (Annotation ca : caretAnnotations) {
            System.out.println(ca.getRect());
        }
    }
```

## 删除圆形注释

以下代码片段展示了如何从 PDF 文件中删除圆形注释。

```java
public static void DeleteCircleAnnotation() {
        // 加载PDF文件
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // 使用AnnotationSelector过滤注释
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

## 添加多边形和折线注释

折线工具允许您在文档上创建任意边数的形状和轮廓。

**多边形注释** 在页面上表示多边形。它们可以具有任意数量的顶点，并通过直线连接。

**折线注释** 也类似于多边形，唯一的区别是第一个和最后一个顶点没有隐式连接。

步骤，我们创建多边形和折线注释：

1. 加载PDF文件 - 新的 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)。
1. 创建新的 [Polygon Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/PolygonAnnotation) 并设置多边形参数（新矩形、新点、标题、颜色、内部颜色和不透明度）。
1. 创建一个新的 [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PopupAnnotation)。
1. 接下来，创建一个 [PolyLine Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PolylineAnnotation) 并重复所有操作。
1. 之后我们可以将注释添加到页面。

以下代码片段展示了如何向PDF文件添加多边形和折线注释：

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExamplePolygonAnnotation {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddPolynnotation() {
        try {
            // 加载PDF文件
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // 创建多边形注释
            PolygonAnnotation polygonAnnotation = new PolygonAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(274, 381), new Point(555, 381), new Point(555, 304), new Point(570, 304),
                            new Point(570, 195), new Point(274, 195) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getBlue());
            polygonAnnotation.setInteriorColor(Color.getBlueViolet());
            polygonAnnotation.setOpacity(0.25);
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // 创建折线注释
            PolylineAnnotation polylineAnnotation = new PolylineAnnotation(page, new Rectangle(270, 193, 571, 383),
                    new Point[] { new Point(545, 150), new Point(545, 190), new Point(667, 190), new Point(667, 110),
                            new Point(626, 111) });

            polygonAnnotation.setTitle("John Smith");
            polygonAnnotation.setColor(Color.getRed());
            polygonAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 196, 1021, 338)));

            // 将注释添加到页面
            page.getAnnotations().add(polygonAnnotation);
            page.getAnnotations().add(polylineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## 获取多边形和折线注释

请尝试使用以下代码片段在 PDF 文档中获取多边形和折线注释。

```java
    public static void GetPolyAnnotation() {
        // 加载 PDF 文件
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

## 删除多边形和折线注释

以下代码片段显示如何从 PDF 文件中删除多边形和折线注释。

```java
        public static void DeletePolyAnnotation() {
        // 加载 PDF 文件
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


## 如何在现有 PDF 文件中添加线条注释

线条注释的目的是在页面上显示一条直线。打开时，会显示一个包含相关注释文本的弹出窗口。此功能具有线条注释特有的附加条目。这些条目以字母的形式加密，例如，LL、BS、IC 等。

此外，线条注释可以包括一个标题，通过将 Cap 设置为 `true` 来指定。

下一个功能允许将标题应用于具有引导偏移的线条注释的效果。此外，这种类型的注释允许您定义线条结束样式。

创建线条注释的步骤：

1. 加载 PDF 文件 - new [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)。
2. 创建新的 [Line Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation) 并设置线条参数（新建矩形，新建点，标题，颜色，宽度，起始样式和结束样式）。

1. 创建一个新的 [PopupAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PopupAnnotation)。
1. 然后我们可以将注释添加到页面

以下代码片段显示了如何将线注释添加到PDF文件：

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleLineAnnotation {

    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddLineAnnotation() {
        try {
            // 加载PDF文件
            Document document = new Document(_dataDir + "appartments.pdf");
            Page page = document.getPages().get_Item(1);

            // 创建线注释
            LineAnnotation lineAnnotation = new LineAnnotation(page, new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443));

            lineAnnotation.setTitle("John Smith");
            lineAnnotation.setColor(Color.getRed());
            lineAnnotation.setWidth(3);
            lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
            lineAnnotation.setEndingStyle(LineEnding.OpenArrow);
            lineAnnotation.setPopup(new PopupAnnotation(page, new Rectangle(842, 124, 1021, 266)));

            // 将注释添加到页面
            page.getAnnotations().add(lineAnnotation);
            document.save(_dataDir + "appartments_mod.pdf");
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
        }
    }
```


## 获取线注释

请尝试使用以下代码片段在 PDF 文档中获取线注释。

```java
    public static void GetLineAnnotation() {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // 使用 AnnotationSelector 过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // 打印结果
        for (Annotation la : lineAnnotations) {
            LineAnnotation l = (LineAnnotation) la;
            System.out.println("[" + l.getStarting().getX() + "," + l.getStarting().getY() + "]" + "["
                    + l.getEnding().getX() + "," + l.getEnding().getY() + "]");
        }
    }
```

## 删除线注释

以下代码片段显示了如何从 PDF 文件中删除线条注释。

```java
   public static void DeleteLineAnnotation() {
        // 加载 PDF 文件
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // 使用 AnnotationSelector 筛选注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new LineAnnotation(page, Rectangle.getTrivial(), Point.getTrivial(), Point.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> lineAnnotations = annotationSelector.getSelected();

        // 打印结果
        for (Annotation la : lineAnnotations) {
            page.getAnnotations().delete(la);
        }
        document.save(_dataDir + "appartments_del.pdf");
    }
}
```

## 如何向 PDF 文件添加墨迹注释

墨迹注释代表由一个或多个不相交路径组成的自由手写“涂鸦”。
 当打开时，它将显示一个包含相关注释文本的弹出窗口。

[InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation) 表示由一个或多个不相连的点组成的手绘涂鸦。请尝试使用以下代码片段在 PDF 文档中添加 InkAnnotation。

```java
package com.aspose.pdf.examples;

import java.util.*;
import com.aspose.pdf.*;

public class ExampleInkAnnotation {

    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";


    public static void AddInkAnnotation() {
        try {
            // 加载 PDF 文件
            Document document = new com.aspose.pdf.Document(_dataDir + "Appartments.pdf");
            Page page = document.getPages().get_Item(1);
            Rectangle arect = new Rectangle(320.086,189.286,384.75,228.927);
            List<Point[]> inkList = new ArrayList<Point[]>();
            // 来自鼠标或其他指示设备的数据
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

            // 将数据转换为点
            Point[] arrpt = new Point[ppts.length/2];
            for (int i = 0, j=0; i < arrpt.length; i++, j+=2) {
                arrpt[i] = new Point(ppts[j],ppts[j+1]);
            }
            inkList.add(arrpt);

            InkAnnotation ia = new InkAnnotation(page, arect, inkList);
            ia.setTitle("Aspose 用户");
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

## 从PDF获取InkAnnotation

您可以使用以下代码片段获取[InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation)：

```java
public static void GetInkAnnotation() {
        // 加载PDF文件
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // 使用AnnotationSelector过滤注释
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new InkAnnotation(page, Rectangle.getTrivial(), null));
        page.accept(annotationSelector);
        List<Annotation> inkAnnotations = annotationSelector.getSelected();

        // 打印结果
        for (Annotation ia : inkAnnotations) {
            System.out.println(ia.getRect());
        }
    }
```

## 删除InkAnnotation

Aspose.PDF for Java允许您从PDF文件中删除[InkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/InkAnnotation)。

```java
public static void DeleteInkAnnotation() {
        // 加载PDF文件
        Document document = new Document(_dataDir + "appartments_mod.pdf");

        // 使用AnnotationSelector过滤注释
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