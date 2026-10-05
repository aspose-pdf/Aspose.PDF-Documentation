---
title: "PDFにページの挿入"
linktitle: "PDFにページの挿入"
type: docs
weight: 40
url: /ja/java/insert-pages-into-pdf/
description: JavaのPdfFileEditorファサードを使用して、あるPDFから別のPDFへ選択したページを挿入します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用して、別のPDFから選択した位置にページを挿入する
Abstract: Aspose.PDF for Java を使用して PDF にページを挿入する方法を学びます。Java のサンプルでは PdfFileEditor を使用し、2 番目のドキュメントから選択したページをターゲット PDF の指定したページ番号の後に挿入します。
---
## PDFにページの挿入

Java のサンプルは、セカンダリ文書からページ 1 と 2 をターゲット PDF のページ 2 の後に挿入します。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. 対象ドキュメントで挿入位置を選択します。
3. 元ドキュメントからコピーするページ番号を選択してください。
4. 呼び出し `insert` ターゲットファイル、挿入ポイント、ソースファイル、ページ配列、そして出力ファイルを使用して。
5. 更新された PDF を保存してください。

### Javaの例

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
