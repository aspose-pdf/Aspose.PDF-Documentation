---
title: Java を使用した透かしアノテーション
linktitle: 透かしアノテーション
type: docs
weight: 70
url: /ja/java/pdfannotationeditor-class/watermark-annotations/
description: "Java を使用して PDF ドキュメントに透かしアノテーションを追加・検査・削除する方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ファイルの透かしアノテーションの操作"
Abstract: "この記事では、Java を使用して PDF ドキュメント内の透かしアノテーションを作成・検査・削除する方法を説明します。カスタムのテキスト状態と不透明度を持つテキスト透かしアノテーションの追加、既存の透かしアノテーション領域の読み取り、透かしアノテーションの削除について扱います。"
---
## 透かしアノテーションの追加

1. 入力 PDF を開き、透かし注釈を配置する矩形を定義してください。
2. 作成する `WatermarkAnnotation` をページに追加し、透かしテキストの状態と不透明度を設定してください。
3. 透かしテキスト行を適用し、変更された PDF を保存してください。

```java
public static void watermarkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        WatermarkAnnotation watermarkAnnotation = new WatermarkAnnotation(
                document.getPages().get_Item(1), new Rectangle(100, 0, 400, 100, true));

        document.getPages().get_Item(1).getAnnotations().add(watermarkAnnotation);

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
