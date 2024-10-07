---
title: PDFファイル情報を設定する
type: docs
weight: 40
url: /net/set-pdf-file-information/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイル情報を設定する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) クラスを使用すると、PDFファイルの特定の情報を設定することができます。[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) クラスのオブジェクトを作成し、著者、タイトル、キーワード、作成者などの異なるファイル特定のプロパティを設定する必要があります。最後に、[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo) オブジェクトの [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) メソッドを使用して更新されたPDFファイルを保存します。

次のコードスニペットは、PDFファイル情報を設定する方法を示しています。

```csharp
 public static void SetPdfInfo()
        {
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf")
            {
                // Set PDF information
                Author = "Aspose",
                Title = "Hello World!",
                Keywords = "Peace and Development",
                Creator = "Aspose"
            };
            // Save updated file
            fileInfo.SaveNewInfo(_dataDir + "SetFileInfo_out.pdf");
        }
```

## メタ情報を設定する

[SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) メソッドを使用すると、任意の情報を追加できます。私たちの例では、フィールドを追加しました。次のコードスニペットを確認してください：

```csharp
 public static void SetMetaInfo()
        {
            // PdfFileInfo オブジェクトのインスタンスを作成
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "sample.pdf");

            // 新しい顧客属性をメタ情報として設定
            fInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

            // 更新されたファイルを保存
            fInfo.SaveNewInfo(_dataDir + "SetMetaInfo_out.pdf");
```