---
title: Javaによるシェイプ注釈
linktitle: シェイプ注釈
type: docs
weight: 40
url: /ja/java/pdfannotationeditor-class/shape-annotations/
description: Javaを使用してPDFドキュメントに四角形、円、多角形、折れ線の注釈を追加、検査、削除する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Javaで幾何学的PDF注釈を扱う
Abstract: この記事では、Javaを使用してPDFドキュメント内の幾何学的注釈を作成、検査、削除する方法を説明します。四角形、円、多角形、折れ線の注釈に加えて、色、透明度、ポップアップ、ポイント設定についても取り上げています。
---
## シェイプ注釈の追加

1. 入力 PDF を開き、シェイプ注釈を含むページと矩形を選択してください。
2. 必要なシェイプ注釈を作成し、必要に応じてタイトル、色、不透明度、ポイントを設定してください。
3. 注釈をページに追加し、変更された PDF を保存してください。

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1), new Rectangle(60, 600, 250, 450, true));
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
