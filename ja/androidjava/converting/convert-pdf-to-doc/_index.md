---
title: PDF を DOC に変換
linktitle: PDF を DOC に変換
type: docs
weight: 70
url: /ja/androidjava/convert-pdf-to-doc/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java を使用して、PDF ファイルを簡単かつ完全に制御しながら DOC 形式に変換します。Microsoft Word の Doc ファイルを PDF に変換する方法の詳細をご確認ください。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

最も人気のある機能の一つは PDF から Microsoft Word DOC への変換で、コンテンツを簡単に操作できるようにします。Aspose.PDF for Android via Java を使用すると、PDF ファイルを DOC に変換できます。

**Aspose.PDF for Android via Java** は、ゼロから PDF ドキュメントを作成でき、既存の PDF ドキュメントの更新、編集、操作に優れたツールキットです。重要な機能のひとつは、ページや PDF 全体を画像に変換できることです。もうひとつの人気機能は PDF から Microsoft Word DOC への変換で、コンテンツを簡単に操作できます。（ほとんどのユーザーは PDF ドキュメントを編集できませんが、Microsoft Word では表、テキスト、画像を簡単に扱えます。）

シンプルで分かりやすくするために、Aspose.PDF for Android via Java は、ソース PDF ファイルを DOC ファイルに変換するための 2 行コードを提供しています。

{{% alert color="primary" %}}

オンラインでお試しください。Aspose.PDF 変換の品質を確認し、結果をオンラインでこのリンクから表示できます。 [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

次のコードスニペットは、PDFファイルをDOC形式に変換するプロセスを示しています。

```java
 public void convertPDFtoDOC() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Save the file into MS document format
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


