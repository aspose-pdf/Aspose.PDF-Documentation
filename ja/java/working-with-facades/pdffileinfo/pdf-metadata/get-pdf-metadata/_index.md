---
title: "PDF メタデータの取得"
linktitle: "PDF メタデータの取得"
type: docs
weight: 20
url: /ja/java/get-pdf-metadata/
description: PdfFileInfo ファサードを使用して Java で PDF メタデータを読み取る方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java を使用した PDF メタデータの取得。
Abstract: Aspose.PDF for Java を使用して PDF メタデータを取得する方法を学びます。Java のサンプルでは、件名、タイトル、キーワード、作成者、作成日、変更日などの標準フィールドに加えて、ファイルステータスフラグやカスタムメタデータエントリ `Reviewer` を読み取ります。
---
## PDF メタデータの取得

このサンプルは、標準的な文書情報、ファイルステータスフラグ、およびカスタムメタデータキーを読み取ります。

### 手順

1. 作成 `PdfFileInfo` ソース PDF 用のオブジェクト。
2. subject、title、keywords、creator などの標準メタデータフィールドを読み取ります。
3. ファイルが有効か、暗号化されているか、パスワードで保護されているか、ポートフォリオかなどのファイル状態フラグを確認します。
4. カスタムメタデータの値を読み取る `getMetaInfo`。
5. 閉じる `PdfFileInfo` インスタンス。

### Javaの例

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```
