---
title: 例外制御 PDF ファイル
type: docs
weight: 30
url: ja/net/control-exception/
description: このトピックでは、PdfFileSecurity クラスを使用して PDF ファイルの例外を制御する方法について説明します。
lastmod: "2021-06-05"
draft: false
---

[PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) クラスを使用すると、例外を制御できます。これを行うには、[AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) プロパティを false または true に設定する必要があります。操作を false に設定した場合、[DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) の結果は、パスワードの正確さに応じて true または false を返します。

```csharp
   public static void ControlExceptionPDFFile()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = false;
            // PDF ドキュメントを復号化する
            if (!fileSecurity.DecryptFile("IncorrectPassword"))
            {
                Console.WriteLine("何か問題があります...");
                Console.WriteLine($"最後の例外: {fileSecurity.LastException.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```

If you set [AllowExceptions](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) プロパティを true に設定すると、try-catch 演算子を使用して操作の結果を取得できます。

```csharp
public static void ControlExceptionPDFFile2()
        {
            PdfFileSecurity fileSecurity = new PdfFileSecurity();
            fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
            fileSecurity.AllowExceptions = true;
            try
            {
                // PDF ドキュメントを復号化する
                fileSecurity.DecryptFile("IncorrectPassword");
            }
            catch (Exception ex)
            {
                Console.WriteLine("何か問題が発生しました...");
                Console.WriteLine($"Exception: {ex.Message}");
            }
            fileSecurity.Save(_dataDir + "sample_decrtypted.pdf");
        }
```