---
title: "ドキュメント権限の取得"
linktitle: "ドキュメント権限の取得"
type: docs
weight: 10
url: /ja/java/get-document-privileges/
description: PdfFileInfo ファサードを使用して、Java で PDF ドキュメントの権限を検査する方法を学びます。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Aspose.PDF for Java を使用して PDF ドキュメント権限の取得"
Abstract: "Aspose.PDF for Java を使用してドキュメント権限を取得する方法を学びます。Java の例では、PdfFileInfo オブジェクトを作成し、その DocumentPrivilege 設定を読み取って、印刷、コピー、変更、注釈、フォーム入力、スクリーンリーダー、および組み立てに対する許可フラグを出力します。"
---
## ドキュメント権限の取得

`PdfFileInfo.getDocumentPrivilege()` を使用して、現在の PDF が許可している操作を検査してください。

### 手順

1. 入力 PDF の `PdfFileInfo` オブジェクトを作成してください。
2. `getDocumentPrivilege()` を呼び出して権限セットを取得してください。
3. 返された `DocumentPrivilege` オブジェクトから該当するブールフラグを読み取ってください。
4. 使用が完了したら、`PdfFileInfo` インスタンスを閉じてください。

### Java の例

```java
public static void getDocumentPrivileges(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    DocumentPrivilege privileges = pdfInfo.getDocumentPrivilege();

    System.out.println("Document Privileges:");
    System.out.println("  Can Print: " + privileges.isAllowPrint());
    System.out.println("  Can Degraded Print: " + privileges.isAllowDegradedPrinting());
    System.out.println("  Can Copy: " + privileges.isAllowCopy());
    System.out.println("  Can Modify Contents: " + privileges.isAllowModifyContents());
    System.out.println("  Can Modify Annotations: " + privileges.isAllowModifyAnnotations());
    System.out.println("  Can Fill In: " + privileges.isAllowFillIn());
    System.out.println("  Can Screen Readers: " + privileges.isAllowScreenReaders());
    System.out.println("  Can Assembly: " + privileges.isAllowAssembly());
    pdfInfo.close();
}
```
