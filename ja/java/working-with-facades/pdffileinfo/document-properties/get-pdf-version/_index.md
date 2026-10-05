---
title: "PDF バージョンの取得"
linktitle: "PDF バージョンの取得"
type: docs
weight: 20
url: /ja/java/get-pdf-version/
description: "PdfFileInfo ファサードを使用して、Java で PDF ドキュメントのバージョンを取得する方法を学習します。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java を使用した PDF バージョンの取得
Abstract: "Aspose.PDF for Java を使用して PDF バージョンを取得する方法を学習します。Java のサンプルでは、PdfFileInfo オブジェクトを作成し、`getPdfVersion()` でバージョン文字列を読み取り、結果を出力した後、ファイル情報オブジェクトを閉じます。"
---
## PDF バージョンの取得

ファイルの互換性を確認したり、バージョン固有の処理ロジックで文書をルーティングしたりする必要がある場合は、このワークフローを使用してください。

### 手順

1. `PdfFileInfo` オブジェクトを PDF ファイルに対して作成してください。
2. `getPdfVersion()` を呼び出して、報告されたバージョンを取得してください。
3. バージョンの値を使用するか、表示してください。
4. `PdfFileInfo` インスタンスを閉じてください。

### Java の例

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
