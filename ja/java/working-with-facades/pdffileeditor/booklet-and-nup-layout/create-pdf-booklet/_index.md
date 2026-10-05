---
title: "PDFブックレットの作成"
linktitle: "PDFブックレットの作成"
type: docs
weight: 20
url: /ja/java/create-pdf-booklet/
description: Javaで既存のドキュメントから、PdfFileEditorファサードを使用してブックレット用のPDFを作成します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFドキュメントからブックレット出力を生成する
Abstract: Aspose.PDF for Javaを使用してPDFブックレットを作成する方法を学びます。このJava例ではPdfFileEditorを使用してページをブックレット印刷用に並び替え、さらに単純な成功確認のためのブール値を返すバリアントも含まれています。
---
## PDFブックレットの作成

使用 `PdfFileEditor.makeBooklet` 既存のPDFのページをブックレット順に再配置する。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. 呼び出し `makeBooklet` ソースPDFおよび出力ファイルとともに。
3. ブックレット文書を保存してください。
4. 戻りステータスを確認したい場合は、ブール値を返すバリアントを使用し、失敗した結果を処理します。

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
