---
title: "XMP でのメタデータの保存"
linktitle: "XMP でのメタデータの保存"
type: docs
weight: 30
url: /ja/java/save-metadata-with-xmp/
description: "PdfFileInfo ファサードを使用して、Java で XMP を用いた PDF メタデータの保存方法を学習してください。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Aspose.PDF for Java を使用した XMP での PDF メタデータの保存"
Abstract: "Aspose.PDF for Java を使用して XMP で PDF メタデータを保存する方法を学習してください。この Java のサンプルでは、PdfFileInfo を用いてコアメタデータフィールドを更新し、`saveNewInfoWithXmp()` を使用して書き戻すため、出力ドキュメントは情報を XMP 形式で保存します。"
---
## XMP でのメタデータの保存

更新されたドキュメント情報を XMP 形式で保存する必要がある場合は、このワークフローを使用してください。

### 手順

1. ソース PDF 用の `PdfFileInfo` オブジェクトを作成してください。
2. 更新したいメタデータフィールド（例: subject、title、keywords、creator）を設定してください。
3. `saveNewInfoWithXmp()` を出力ファイルパスとともに呼び出してください。
4. `PdfFileInfo` インスタンスを閉じてください。

### Java の例

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
