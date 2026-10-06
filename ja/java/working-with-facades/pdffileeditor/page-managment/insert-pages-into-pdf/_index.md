---
title: "PDF へのページの挿入"
linktitle: "PDF へのページの挿入"
type: docs
weight: 40
url: /ja/java/insert-pages-into-pdf/
description: "Java の PdfFileEditor ファサードを使用して、ある PDF から別の PDF へ選択したページを挿入します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して、別の PDF から選択した位置にページの挿入"
Abstract: Aspose.PDF for Java を使用して PDF にページを挿入する方法を学びます。Java のサンプルでは PdfFileEditor を使用し、2 番目のドキュメントから選択したページをターゲット PDF の指定したページ番号の後に挿入します。
---
## PDF へのページの挿入

Java のサンプルは、セカンダリ文書からページ 1 と 2 をターゲット PDF のページ 2 の後に挿入します。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. 対象ドキュメントで挿入位置を選択してください。
3. 元ドキュメントからコピーするページ番号を選択してください。
4. `insert` を、ターゲットファイル、挿入ポイント、ソースファイル、ページ配列、および出力ファイルを引数として呼び出してください。
5. 更新された PDF を保存してください。

### Java の例

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
