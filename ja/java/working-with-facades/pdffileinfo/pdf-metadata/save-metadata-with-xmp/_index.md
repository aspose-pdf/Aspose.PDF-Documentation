---
title: "XMPでメタデータの保存"
linktitle: "XMPでメタデータの保存"
type: docs
weight: 30
url: /ja/java/save-metadata-with-xmp/
description: PdfFileInfo ファサードを使用して、Java で XMP を使用した PDF メタデータの保存方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java を使用して XMP で PDF メタデータを保存する
Abstract: Aspose.PDF for Java を使用して XMP で PDF メタデータを保存する方法を学びます。Java のサンプルは PdfFileInfo でコア メタデータ フィールドを更新し、`saveNewInfoWithXmp()` を使用して書き戻すため、出力ドキュメントは情報を XMP 形式で保存します。
---
## XMPでメタデータの保存

更新されたドキュメント情報を XMP 形式で保存する必要がある場合は、このワークフローを使用します。

### 手順

1. 作成 `PdfFileInfo` ソース PDF 用のオブジェクト。
2. 更新したいメタデータフィールドを設定します（例: subject、title、keywords、creator）。
3. 呼び出す `saveNewInfoWithXmp()` 出力ファイルパスとともに。
4. 閉じる `PdfFileInfo` インスタンス。

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
