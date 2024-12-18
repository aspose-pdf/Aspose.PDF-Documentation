---
title: PDFをDOCに変換 
linktitle: PDFをDOCに変換
type: docs
weight: 70
url: /ja/androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: Aspose.PDF for Android via Javaを使用して、簡単かつ完全にコントロールしてPDFファイルをDOC形式に変換します。Microsoft Word DocファイルをPDFに変換する方法について詳しく学びます。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

最も人気のある機能の1つはPDFからMicrosoft Word DOCへの変換であり、コンテンツの操作が簡単になります。Aspose.PDF for Android via Javaを使用すると、PDFファイルをDOCに変換できます。

**Aspose.PDF for Android via Java**は、ゼロからPDFドキュメントを作成でき、既存のPDFドキュメントを更新、編集、操作するための優れたツールキットです。
 重要な機能は、ページやPDFドキュメント全体を画像に変換する能力です。もう一つの人気のある機能は、PDFをMicrosoft Word DOCに変換することで、コンテンツを簡単に操作できるようにします。（ほとんどのユーザーはPDFドキュメントを編集できませんが、Microsoft Word内で表、テキスト、画像の操作は簡単に行えます。）

物事をシンプルで理解しやすくするために、Aspose.PDF for Android via Javaは、ソースPDFファイルをDOCファイルに変換するための2行のコードを提供します。

{{% alert color="primary" %}}

オンラインで試してみてください。Aspose.PDFの変換品質を確認し、結果をオンラインで表示できます。このリンクで確認してください [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

次のコードスニペットは、PDFファイルをDOC形式に変換するプロセスを示しています。

```java
public void convertPDFtoDOC() {
    // ソースPDFドキュメントを開く
    try {
        document = new Document(inputStream);
    } catch (Exception e) {
        resultMessage.setText(e.getMessage());
        return;
    }
    File docFileName = new File(fileStorage, "PDF-to-Word.doc");

    try {
        // ファイルをMSドキュメント形式で保存
        document.save(docFileName.toString(), SaveFormat.Doc);
    }
    catch (Exception e) {
        resultMessage.setText(e.getMessage());
        return;
    }
    resultMessage.setText(R.string.success_message);
}
```