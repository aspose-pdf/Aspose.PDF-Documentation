---
title: PDF を PowerPoint に変換
linktitle: PDF を PowerPoint に変換
type: docs
weight: 110
url: /ja/androidjava/convert-pdf-to-powerpoint/
description: Aspose.PDF は PDF を PowerPoint フォーマットに変換できます。1 つの方法として、スライドを画像として PDF を PPTX に変換することが可能です。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.Slides という API があり、PPT/PPTX プレゼンテーションの作成および操作機能を提供します。この API は PPT/PPTX ファイルを PDF フォーマットに変換する機能も提供します。Aspose.PDF for Java では、PDF ドキュメントを PPTX フォーマットに変換する機能を導入しました。この変換では、PDF ファイルの個々のページが PPTX ファイルの個別のスライドに変換されます。

{{% alert color="primary" %}}

オンラインで試す。Aspose.PDF の変換品質を確認し、結果をオンラインでこのリンクで表示できます [products.aspose.app/pdf/conversion/pdf-to-pptx](https://products.aspose.app/pdf/conversion/pdf-to-pptx)

{{% /alert %}}

PDF から PPTX への変換中、テキストは画像としてレンダリングされる代わりに、選択/更新できるテキストとしてレンダリングされます。PDF ファイルを PPTX 形式に変換するために、Aspose.PDF は PptxSaveOptions というクラスを提供していることに注意してください。このクラスのオブジェクトは [PptxSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PptxSaveOptions) クラスは第2引数として渡されます [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..) メソッド。

PDF を PowerPoint 形式に変換するタスクを解決するための次のコードスニペットを確認してください：

```java
 public void convertPDFtoPowerPoint() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        PptxSaveOptions pptxSaveOptions = new PptxSaveOptions();


        // Save the output in PPTX
        File xlsFileName = new File(fileStorage, "PDF-to-Powerpoint.pptx");
        try {
            // Save the file into PPTX format
            document.save(xlsFileName.toString(), pptxSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

