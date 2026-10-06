---
title: "PDF ブックレットの作成"
linktitle: "PDF ブックレットの作成"
type: docs
weight: 20
url: /ja/java/create-pdf-booklet/
description: "Java で既存のドキュメントから、PdfFileEditor ファサードを使用してブックレット用の PDF を作成します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ドキュメントからブックレット出力の生成"
Abstract: "Aspose.PDF for Java を使用して PDF ブックレットを作成する方法を学びます。この Java の例では、PdfFileEditor を使用してページをブックレット印刷用に並び替え、さらに単純な成功確認のためのブール値を返すバリアントも含まれています。"
---
## PDF ブックレットの作成

`PdfFileEditor.makeBooklet` を使用して、既存の PDF のページをブックレット順に再配置します。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. `makeBooklet` をソース PDF および出力ファイルとともに呼び出してください。
3. ブックレット文書を保存してください。
4. 戻りステータスを確認したい場合は、ブール値を返すバリアントを使用し、失敗した結果を処理してください。

### Java の例

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```
