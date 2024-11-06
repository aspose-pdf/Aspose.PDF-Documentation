---
title: PDFをPowerPointに変換
linktitle: PDFをPowerPointに変換
type: docs
weight: 110
url: ja/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDFを使用すると、PDFをPowerPoint形式に変換できます。PDFをスライドとして画像としてPPTXに変換する可能性があります。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.SlidesというAPIがあり、PPT/PPTXプレゼンテーションを作成および操作する機能を提供しています。このAPIは、PPT/PPTXファイルをPDF形式に変換する機能も提供しています。Aspose.PDF for Javaでは、PDFドキュメントをPPTX形式に変換する機能を導入しました。この変換中、PDFファイルの各ページがPPTXファイルの個別のスライドに変換されます。

{{% alert color="primary" %}}

オンラインで試すことができます。Aspose.PDFの変換品質を確認し、このリンクで結果をオンラインで見ることができます: [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

PDFからPPTXへの変換中、テキストは画像としてレンダリングされるのではなく、選択/更新可能なテキストとしてレンダリングされます。PDFファイルをPPTX形式に変換するには、Aspose.PDFが提供するクラスであるPptxSaveOptionsを使用する必要があります。[PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions)クラスのオブジェクトは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..)メソッドの第二引数として渡されます。

次のコードスニペットを確認して、PDFからPowerPoint形式への変換タスクを解決してください:

```java
 public void convertPDFtoPowerPoint() {
        // PDFドキュメントを読み込む
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // ExcelSaveオプションオブジェクトをインスタンス化する
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // 出力をPPTXで保存する
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // ファイルをPPTX形式で保存する
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```