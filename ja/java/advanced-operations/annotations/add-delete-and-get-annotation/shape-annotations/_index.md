---
title: "Java によるシェイプ注釈"
linktitle: シェイプ注釈
type: docs
weight: 20
url: /ja/java/shape-annotations/
description: Aspose.PDF for Java を使用して、PDF ドキュメントにおける四角形、円、ポリゴン、ポリライン アノテーションの追加、検査、削除方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: "Java での 幾何学的な PDF アノテーションの操作"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメント内の幾何学的注釈を作成、検査、削除する方法を説明します。四角形、円、ポリゴン、ポリライン注釈に加えて、色、透過性、ポップアップ、ポイント設定についても取り上げています。
---
このセクションのシェイプ注釈は、正方形、円、ポリゴン、ポリライン、線などの幾何学的注釈タイプをカバーしています。

## 四角形、円形、多角形、ポリラインの注釈の追加

カスタムカラー、透明度、ポップアップデータ、またはポイント配列を使用して幾何学的注釈を配置する必要がある場合は、これらの例をご利用ください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要なシェイプ注釈を作成し、その矩形、ポイント、および視覚的プロパティを設定してください。
1. ページにアノテーションを追加し、更新されたドキュメントを保存してください。

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(60, 600, 250, 450, true));
        squareAnnotation.setTitle("John Smith");
        squareAnnotation.setColor(Color.getBlue());
        squareAnnotation.setInteriorColor(Color.getBlueViolet());
        squareAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(squareAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void circleAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        CircleAnnotation circleAnnotation = new CircleAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(270, 160, 483, 383, true));
        circleAnnotation.setTitle("John Smith");
        circleAnnotation.setColor(Color.getRed());
        circleAnnotation.setInteriorColor(Color.getMistyRose());
        circleAnnotation.setOpacity(0.5);
        circleAnnotation.setPopup(new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 316, 1021, 459, true)));

        document.getPages().get_Item(1).getAnnotations().add(circleAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolygonAnnotation polygonAnnotation = new PolygonAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(200, 300, 400, 400, true),
                new Point[]{
                        new Point(200, 300),
                        new Point(220, 300),
                        new Point(250, 330),
                        new Point(300, 304),
                        new Point(300, 400)
                });
        polygonAnnotation.setTitle("John Smith");
        polygonAnnotation.setColor(Color.getBlue());
        polygonAnnotation.setInteriorColor(Color.getBlueViolet());
        polygonAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(polygonAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polylineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolylineAnnotation polylineAnnotation = new PolylineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(270, 193, 571, 383, true),
                new Point[]{
                        new Point(545, 150),
                        new Point(545, 190),
                        new Point(667, 190),
                        new Point(667, 110),
                        new Point(626, 111)
                });
        polylineAnnotation.setTitle("John Smith");
        polylineAnnotation.setColor(Color.getRed());
        polylineAnnotation.setPopup(new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 196, 1021, 338, true)));

        document.getPages().get_Item(1).getAnnotations().add(polylineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 四角形、円形、多角形、ポリラインのアノテーションの取得

これらの例では、ページ注釈コレクションを検査し、タイプ別に幾何学的注釈の矩形を出力します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページの注釈を反復処理してください。
1. 必要な [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) 値でフィルタリングし、矩形を印刷してください。

```java
public static void squareAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void circleAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Circle) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void polygonAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Polygon) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void polylineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.PolyLine) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## 正方形、円、多角形、およびポリラインの注釈の削除

特定の種類のシェイプ注釈をページから削除する必要がある場合は、これらの例をご利用ください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要なジオメトリタイプのアノテーションを収集してください。
1. 収集されたアノテーションを削除し、出力ファイルを保存してください。

```java
public static void squareAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

```java
public static void circleAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Circle) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Polygon) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

```java
public static void polylineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.PolyLine) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 線注釈の追加

この例では、矢印の端点、枠線の書式設定、およびポップアップノートを備えた線注釈を作成します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) を開始点と終了点を指定して作成してください。
1. 外観を設定し、ポップアップを追加して、ドキュメントを保存してください。

```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));
        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## 線注釈の取得

この例では、線注釈を読み取り、その開始座標と終了座標を出力します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページの注釈を順に処理し、[AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line` を選択してください。
1. 各マッチを [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) にキャストし、その座標を出力してください。

```java
public static void lineAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Line) {
                LineAnnotation la = (LineAnnotation) annotation;
                System.out.printf("[%s,%s]-[%s,%s]%n",
                        la.getStarting().getX(), la.getStarting().getY(),
                        la.getEnding().getX(), la.getEnding().getY());
            }
        }
    }
}
```

## 線注釈の削除

ページからライン注釈を削除する必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. タイプ [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line` の注釈を収集してください。
1. 収集した注釈を削除し、ドキュメントを保存してください。

```java
public static void lineAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Line) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            page.getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## 関連する注釈トピック

- [インタラクティブアノテーション](/pdf/ja/java/interactive-annotations/)
- [マークアップ注釈](/pdf/ja/java/markup-annotations/)
- [セキュリティ注釈](/pdf/ja/java/security-annotations/)
- [テキスト注釈](/pdf/ja/java/text-based-annotations/)
- [透かし注釈](/pdf/ja/java/watermark-annotations/)
- [アノテーションのインポートとエクスポート](/pdf/ja/java/import-export-annotations/)
