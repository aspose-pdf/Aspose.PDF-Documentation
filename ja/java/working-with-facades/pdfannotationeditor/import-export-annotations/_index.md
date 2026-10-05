---
title: Java を使用した注釈のインポートとエクスポート
linktitle: 注釈のインポートとエクスポート
type: docs
weight: 80
url: /ja/java/pdfannotationeditor-class/import-export-annotations/
description: Java を使用して、ある PDF ドキュメントから別の PDF ドキュメントへ注釈をコピーする方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java でドキュメント間の PDF 注釈を転送する
Abstract: この記事では、ソース PDF から注釈をコピーし、Java を使用して新しい PDF ドキュメントにエクスポートする方法を説明します。ワークフローは、ソースファイルを読み込み、宛先ドキュメントを作成し、ページを追加し、最初のソースページから注釈をコピーし、結果を保存します。
---
## PDF を 1 つから別の PDF へ注釈のコピー

1. ソースPDFを開き、ターゲットページを持つ新しい宛先ドキュメントを作成してください。
2. 最初のソースページの注釈を列挙し、それぞれを宛先ページに追加します。
3. コピーされた注釈を永続化するために、宛先ドキュメントを保存してください。

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
