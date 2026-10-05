---
title: Java を使用した透かし注釈
linktitle: 透かし注釈
type: docs
weight: 70
url: /ja/java/watermark-annotations/
description: "Aspose.PDF for Java を使用して、PDF ドキュメント内の透かし注釈の追加、確認、削除を行う方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ファイル内の透かし注釈の操作"
Abstract: "このドキュメントでは、Aspose.PDF for Java を使用して PDF 文書内の透かし注釈の作成、確認、削除を行う方法を説明します。カスタムテキストステートと不透明度を持つテキスト透かし注釈の追加、既存の透かし注釈領域の読み取り、透かし注釈の削除について取り上げています。"
---
透かし注釈を使用すると、ページ上に再利用可能なオーバーレイコンテンツを配置しながら、アノテーションコレクションを通じて管理できます。

## 透かし注釈の追加

カスタムフォント設定と不透明度を持つテキスト透かし注釈が必要な場合に、この例をご使用ください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/watermarkannotation/) を作成し、ページに追加してください。
1. [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/)、透かしテキスト、不透明度を設定し、ドキュメントを保存してください。

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                page,
                new Rectangle(100, 100, 400, 200, true));

        page.getAnnotations().add(watermarkAnnotation);

        TextState textState = new TextState();
        textState.setForegroundColor(Color.getBlue());
        textState.setFontSize(25);
        textState.setFont(FontRepository.findFont("Arial"));

        watermarkAnnotation.setOpacity(0.5);
        watermarkAnnotation.setTextAndState(new String[]{"HELLO", "Line 1", "Line 2"}, textState);

        document.save(outputFile.toString());
    }
}
```

## 透かしアノテーションの取得

この例では、アノテーションコレクションをスキャンし、各透かしアノテーションの矩形を出力します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象ページのアノテーションを反復処理してください。
1. [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` でアノテーションをフィルタリングし、それらの矩形を出力してください。

```java
public static void watermarkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                System.out.println(a.getRect());
            }
        }
    }
}
```

## 透かしアノテーションの削除

既存の透かしアノテーションをドキュメントから削除する必要がある場合に、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Watermark` のアノテーションを収集してください。
1. 収集したアノテーションを削除し、出力ファイルを保存してください。

```java
public static void watermarkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation a : document.getPages().get_Item(1).getAnnotations()) {
            if (a.getAnnotationType() == AnnotationType.Watermark) {
                toDelete.add(a);
            }
        }
        for (Annotation a : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(a);
        }
        document.save(outputFile.toString());
    }
}
```

## 関連する注釈トピック

- [インタラクティブアノテーション](/pdf/ja/java/interactive-annotations/)
- [マークアップアノテーション](/pdf/ja/java/markup-annotations/)
- [セキュリティアノテーション](/pdf/ja/java/security-annotations/)
- [シェイプアノテーション](/pdf/ja/java/shape-annotations/)
- [テキスト注釈](/pdf/ja/java/text-based-annotations/)
- [注釈のインポートとエクスポート](/pdf/ja/java/import-export-annotations/)
