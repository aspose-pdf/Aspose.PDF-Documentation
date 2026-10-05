---
title: "N-Up PDF ドキュメントの作成"
linktitle: "N-Up PDF ドキュメントの作成"
type: docs
weight: 10
url: /ja/java/create-n-up-pdf-document/
description: "Java の PdfFileEditor ファサードを使用して、2x2 N-Up PDF レイアウトを作成してください。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での 既存のドキュメントから N-Up PDF レイアウトの生成"
Abstract: "Aspose.PDF for Java を使用して N-Up PDF ドキュメントを作成する方法を学習します。Java のサンプルでは PdfFileEditor を使用し、各出力シートに 4 つの元ページを配置します。また、失敗確認のためのブール値を返すバリアントも示しています。"
---
## N-Up PDF ドキュメントの作成

Java のサンプルでは、`PdfFileEditor.makeNUp` を使用して既存の PDF から 2×2 レイアウトを作成します。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. `makeNUp` を呼び出し、入力ファイル、出力ファイル、および列数と行数を指定してください。
3. 生成されたドキュメントを保存してください。
4. 明示的な成功チェックが必要な場合は、ブール値を返すバリアントを呼び出し、`false` 結果を処理してください。

### Java の例

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
