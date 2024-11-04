---
title: PDFファイルから添付ファイルを抽出する
type: docs
weight: 10
url: /java/extract-attachments/
description: このセクションでは、PdfExtractorクラスを使用してPDFから添付ファイルを抽出する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

[com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame)の抽出機能の主なカテゴリーの一つが、添付ファイルの抽出です。
 このカテゴリは、添付ファイルを抽出するだけでなく、添付ファイルに関連する情報を提供するメソッドも提供します。つまり、[GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) と [GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) メソッドはそれぞれ添付ファイル情報と添付ファイル名を提供します。添付ファイルを抽出して取得するために、[ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) と [GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--) メソッドを使用します。

次のコードスニペットは、PdfExtractor メソッドの使用方法を示しています：

```java
public static void ExtractAttachments() {
    PdfExtractor pdfExtractor = new PdfExtractor();
    pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

    // 添付ファイルを抽出
    pdfExtractor.extractAttachment();

    // 添付ファイル名を取得
    if (pdfExtractor.getAttachNames().size() > 0) {
        System.out.println("抽出して保存中...");
        // 抽出された添付ファイルを取得
        pdfExtractor.getAttachment(_dataDir);
    }
}
```