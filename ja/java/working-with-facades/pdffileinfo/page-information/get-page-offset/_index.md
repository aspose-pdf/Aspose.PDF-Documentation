---
title: "ページオフセットの取得"
linktitle: "ページオフセットの取得"
type: docs
weight: 20
url: /ja/java/get-page-offset/
description: Java の PdfFileInfo ファサードを使用して、ページの X および Y オフセットを検査する方法を学びます。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ページオフセットの取得"
Abstract: Aspose.PDF for Java を使用してページオフセットを取得する方法を学びます。Java のサンプルでは PdfFileInfo を使用してページ 1 の X および Y オフセットを読み取り、ポイント値をインチに変換してレイアウト分析を容易にします。
---
## ページオフセットの取得

PDF の原点に対してページコンテンツがどのように配置されているかを理解する必要がある場合に、このワークフローを使用してください。

### 手順

1. 入力 PDF の `PdfFileInfo` オブジェクトを作成してください。
2. `getPageXOffset` および `getPageYOffset` を対象ページに対して呼び出してください。
3. ポイント値をインチに変換するには、`72.0` で割ってください。
4. 変換された値を使用するか、出力してください。
5. `PdfFileInfo` インスタンスを閉じてください。

### Java の例

```java
public static void getPageOffsets(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Page X Offset: " + (pdfInfo.getPageXOffset(1) / 72.0) + " inches");
    System.out.println("Page Y Offset: " + (pdfInfo.getPageYOffset(1) / 72.0) + " inches");
    pdfInfo.close();
}
```
