---
title: Java を使用したセキュリティアノテーション
linktitle: セキュリティアノテーション
type: docs
weight: 60
url: /ja/java/pdfannotationeditor-class/security-annotations/
description: Java を使用して PDF ファイル内のテキストを削除対象としてマークし、削除アノテーションを適用し、検出された画像配置矩形に基づいて選択した領域を削除する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java でセキュリティアノテーションを使用して機密 PDF コンテンツを削除する
Abstract: この記事では、Java を使用して PDF 文書で削除アノテーションを操作する方法を説明します。マッチしたテキストを削除アノテーションでマークし、削除を永続的に適用し、検出された画像配置矩形に基づいて選択した領域を削除する方法を取り上げています。
---
## 削除対象としてテキストをマークする

1. PDF をロードし、すべてのページで削除すべきテキストを検索してください。
2. 作成 `RedactionAnnotation` 一致したテキストフラグメントごとに外観を設定してください。
3. 削除アノテーションを各ページに追加し、ドキュメントを保存してください。

```java
public static void markTextRedaction(Path inputFile, Path outputFile, String searchTerm) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(searchTerm);
        TextSearchOptions textSearchOptions = new TextSearchOptions(true);
        textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
        document.getPages().accept(textFragmentAbsorber);

        for (TextFragment textFragment : textFragmentAbsorber.getTextFragments()) {
            Page page = textFragment.getPage();
            Rectangle annotationRectangle = textFragment.getRectangle();
            RedactionAnnotation annotation = new RedactionAnnotation(page, annotationRectangle);
            annotation.setFillColor(Color.getGray());
            annotation.setBorderColor(Color.getRed());
            annotation.setColor(Color.getWhite());
            annotation.setOverlayText("REDACTED");
            annotation.setTextAlignment(HorizontalAlignment.Center);
            annotation.setRepeat(true);
            page.getAnnotations().add(annotation, true);
        }

        document.save(outputFile.toString());
    }
}
```
