---
title: "ページ情報の取得"
linktitle: "ページ情報の取得"
type: docs
weight: 10
url: /ja/java/get-page-info/
description: Java で PdfFileInfo ファサードを使用して、ページの幅、高さ、回転を検査する方法を学びます。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Aspose.PDF for Java を使用して PDF ページ情報の取得"
Abstract: Aspose.PDF for Java を使用してページ情報を取得する方法を学びます。Java のサンプルは PdfFileInfo を使用して、ページ 1 の幅、高さ、回転を読み取り、さらに処理を行う前にそのレイアウトを検査できるようにします。
---
## ページ情報の取得

この例では、ページ 1 の主要な幾何学的プロパティを読み取ります。

### 手順

1. 作成 `PdfFileInfo` オブジェクトを、ソース PDF に対して行ってください。
2. 検査したいページに対して、`getPageWidth`、`getPageHeight`、および `getPageRotation` を呼び出してください。
3. 返された値を使用するか、出力してください。
4. `PdfFileInfo` インスタンスを閉じてください。

### Java の例

```java
public static void getPageInformation(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page Width: " + pdfInfo.getPageWidth(1));
    System.out.println("Page Height: " + pdfInfo.getPageHeight(1));
    System.out.println("Page Rotation: " + pdfInfo.getPageRotation(1));
    pdfInfo.close();
}
```
