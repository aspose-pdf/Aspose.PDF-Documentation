---
title: PDFファイルの署名を確認する
type: docs
weight: 30
url: ja/java/verify-signature-in-pdf/
description: このセクションでは、PdfFileSignatureクラスを使用してPDFファイル内の署名を操作する方法を説明します。
lastmod: "2021-06-05"
draft: false
---

## PDFファイルが署名されているかどうかを確認する

[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature)クラスのVerifySignedメソッドを使用して、PDFファイルが署名されているかどうかを確認します。このメソッドは署名名を必要とし、その署名名を使用してPDFが署名されている場合にtrueを返します。どの署名で署名されているかを確認せずに、[PDFが署名されている](/pdf/java/working-with-signature-in-a-pdf-file/)ことを確認することも可能です。

### 指定された署名でPDFが署名されていることを確認する

以下のコードスニペットは、指定された署名を使用してPDFが署名されているかどうかを確認する方法を示しています。

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Document Signed");

        pdfSign.close();
    }
```


### PDFが署名されていることの確認

署名名を指定せずにファイルが署名されているかを判断するには、次のコードを使用します。

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF Signed");
        }
    }
```

## 署名が有効であるかの確認

[VerifySignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) メソッドは、特定の署名を検証することを可能にします。このメソッドは署名名を入力として必要とし、署名が有効であればtrueを返します。以下のコードスニペットは、署名を検証する方法を示しています。

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("Signature Verified");
        }
    }
```