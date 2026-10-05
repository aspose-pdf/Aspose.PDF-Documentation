---
title: Java を使用した注釈のインポートとエクスポート
linktitle: 注釈のインポートとエクスポート
type: docs
weight: 80
url: /ja/java/import-export-annotations/
description: Aspose.PDF for Java を使用して、ある PDF ドキュメントから別の PDF ドキュメントへ注釈をコピーする方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF 注釈をドキュメント間で転送します。
Abstract: この記事では、Aspose.PDF for Java を使用して、ソース PDF から注釈をコピーし、それらを新しい PDF ドキュメントにエクスポートする方法を説明します。ワークフローは、ソースファイルを読み込み、宛先ドキュメントを作成し、ページを追加し、最初のソースページから注釈をコピーし、結果を保存します。
---
## 注釈をある PDF から別の PDF にコピーする

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 宛先へ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 各項目を追加 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 対象へ [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 読み取るまたは反復処理する [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 対象ページの項目。
1. 更新された PDF を保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 列挙する [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 最初のソースページの項目を取得し、各項目を宛先ページに追加します。

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
