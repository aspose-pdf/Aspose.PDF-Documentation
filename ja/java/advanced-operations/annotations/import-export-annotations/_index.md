---
title: Java を使用した注釈のインポートとエクスポート
linktitle: 注釈のインポートとエクスポート
type: docs
weight: 80
url: /ja/java/import-export-annotations/
description: Aspose.PDF for Java を使用して、ある PDF ドキュメントから別の PDF ドキュメントへ注釈をコピーする方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF 注釈をドキュメント間で転送"
Abstract: この記事では、Aspose.PDF for Java を使用して、ソース PDF から注釈をコピーし、それらを新しい PDF ドキュメントにエクスポートする方法を説明します。ワークフローは、ソースファイルを読み込み、宛先ドキュメントを作成し、ページを追加し、最初のソースページから注釈をコピーし、結果を保存します。
---
## 注釈のある PDF から別の PDF へのコピー

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 宛先の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) に [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. 対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) に各 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) を追加してください。
1. 対象ページの [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 項目を読み取るか、反復処理してください。
1. 更新した PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を保存してください。
1. 最初のソースページの [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 項目を列挙し、各項目を宛先ページに追加してください。

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
