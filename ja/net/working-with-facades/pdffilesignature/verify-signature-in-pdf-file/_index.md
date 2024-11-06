---
title: PDFファイルの署名を検証する
type: docs
weight: 30
url: ja/net/verify-signature-in-pdf/
description: このセクションでは、PdfFileSignatureクラスを使用してPDFファイルの署名を検証する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルが署名でサインされているかどうかを検証する

[特定の署名](/pdf/net/working-with-signature-in-a-pdf-file/)を使用してPDFファイルがサインされているかどうかを検証するには、[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)クラスのVerifySignedメソッドを使用します。このメソッドは署名名を必要とし、その署名名を使用してPDFがサインされている場合はtrueを返します。また、どの署名でサインされているかを検証せずに[PDFがサインされている](/pdf/net/working-with-signature-in-a-pdf-file/)ことを確認することも可能です。

### 指定された署名でPDFがサインされていることを確認する

次のコードスニペットは、指定された署名を使用してPDFがサインされているかどうかを確認する方法を示しています。

```csharp
public static void IsPdfSigned()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.ContainsSignature())
                Console.WriteLine("Document Signed");
            pdfSign.Close();
        }
```


### PDFが署名されていることの確認

ファイルが署名されているかどうかを署名名を提供せずに判断するには、次のコードを使用します。

```csharp
 public static void IsPdfSignedWithGivenSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySigned("Signature1"))
            {
                Console.WriteLine("PDF Signed");
            }
            //if (pdfSign.VerifySigned("Signature2"))
            //{
            //    Console.WriteLine("PDF Signed");
            //}
        }
```

## 署名が有効かどうかの確認

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) クラスの [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) メソッドを使用すると、特定の署名を検証できます。 この方法は、入力として署名名を必要とし、署名が有効である場合にtrueを返します。次のコードスニペットは、署名を検証する方法を示しています。

```csharp
public static void IsPdfSignatureValid()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySignature("Signature1"))
            {
                Console.WriteLine("署名が確認されました");
            }
        }
```