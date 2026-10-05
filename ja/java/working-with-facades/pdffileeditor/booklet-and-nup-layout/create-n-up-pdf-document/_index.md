---
title: "N-Up PDF ドキュメントの作成"
linktitle: "N-Up PDF ドキュメントの作成"
type: docs
weight: 10
url: /ja/java/create-n-up-pdf-document/
description: Java の PdfFileEditor ファサードを使用して、2x2 N-Up PDF レイアウトを作成します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で既存のドキュメントから N-Up PDF レイアウトを生成する
Abstract: Aspose.PDF for Java を使用して N-Up PDF ドキュメントを作成する方法を学びます。Java のサンプルでは PdfFileEditor を使用し、各出力シートに 4 つの元ページを配置し、失敗確認のためのブール値返却バリアントも示しています。
---
## N-Up PDF ドキュメントの作成

Java のサンプルは使用します `PdfFileEditor.makeNUp` 既存のPDFから2×2レイアウトを作成するために。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. 呼び出す `makeNUp` 入力ファイル、出力ファイル、および列数と行数を使用して。
3. 生成されたドキュメントを保存してください。
4. 明示的な成功チェックが必要な場合は、ブール値を返すバリアントを呼び出し、a を処理してください。 `false` 結果。

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
