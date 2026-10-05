---
title: "PDF のページの削除"
linktitle: "PDF のページの削除"
type: docs
weight: 20
url: /ja/java/delete-pages-from-pdf/
description: Java で PdfFileEditor ファサードを使用して PDF から選択したページを削除する。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF ドキュメントから特定のページを削除する
Abstract: Aspose.PDF for Java を使用して PDF のページを削除する方法を学びます。Java のサンプルでは PdfFileEditor を使用して指定されたページ番号のセットを削除し、残りのページを新しいドキュメントとして保存します。
---
## PDF からページの削除

Java のサンプルは、ソース ドキュメントからページ 2 とページ 4 を削除します。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. 削除するページ番号の配列を作成してください。
3. 呼び出す `delete` 入力ファイル、ページ配列、および出力ファイルとともに。
4. 結果の PDF を保存してください。

### Java の例

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
