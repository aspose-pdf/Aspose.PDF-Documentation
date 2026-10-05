---
title: "PDF バージョンの取得"
linktitle: "PDF バージョンの取得"
type: docs
weight: 20
url: /ja/java/get-pdf-version/
description: PdfFileInfo ファサードを使用して、Java で PDF ドキュメントのバージョンを取得する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java を使用した PDF バージョンの取得
Abstract: Aspose.PDF for Java を使用して PDF バージョンを取得する方法を学びます。Java のサンプルでは PdfFileInfo オブジェクトを作成し、`getPdfVersion()` でバージョン文字列を読み取り、結果を出力し、ファイル情報オブジェクトを閉じます。
---
## PDF バージョンの取得

ファイルの互換性を確認したり、バージョン固有の処理ロジックで文書をルーティングしたりする必要がある場合に、このワークフローを使用してください。

### 手順

1. 作成 `PdfFileInfo` PDFファイルのオブジェクト。
2. 呼び出す `getPdfVersion()` 報告されたバージョンを取得するために。
3. バージョンの値を使用するか、表示してください。
4. 閉じる `PdfFileInfo` インスタンス。

### Java の例

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
