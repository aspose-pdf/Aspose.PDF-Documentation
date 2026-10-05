---
title: Javaでデジタル署名を追加するか、PDFにデジタル署名を行う
linktitle: PDFにデジタル署名する
type: docs
weight: 10
url: /ja/java/digitally-sign-pdf-file/
description: Aspose.PDFを使用して、JavaでPDF文書にデジタル署名と認証を行う方法を学ぶ。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFファイルにデジタル署名する
Abstract: このガイドでは、Aspose.PDF for Java を使用して PDF ドキュメントにデジタル署名を行う方法を説明します。証明書オブジェクトによる署名、基本的な証明書パラメーターによる署名、そして DocMDP 署名で文書を認証し、署名後に許可される変更を制御する方法をカバーしています。
---
Aspose.PDF for Java は、複数の署名フローをサポートしています。 `PdfFileSignature`.

## 証明書オブジェクトを使用して PDF に署名する

1. 作成する [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを使用してソースPDFドキュメントをバインドしてください。
1. 作成する [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) 署名オブジェクトを作成し、署名オプションを構成してください。
1. PDFドキュメントに署名を適用するには [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/)。
1. 更新されたPDFドキュメントを保存してください。

```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

このアプローチは構築します `PKCS7` 署名オブジェクトを最初に作成し、次にページ 1 に適用します。

## 基本的な証明書パラメータで PDF に署名する

1. 作成する [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを使用してソースPDFドキュメントをバインドしてください。
1. 署名サンプルで必要とされる証明書パラメータを構成してください。
1. PDFドキュメントに署名を適用するには [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/)。
1. 更新されたPDFドキュメントを保存してください。

```java
public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

## DocMDPでPDFを認証する

認証レベルの制限が必要な場合は、文書の変更検出および防止署名を使用してください：

1. 作成する [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを使用してソースPDFドキュメントをバインドしてください。
1. 作成する [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) オブジェクトと構成する [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/) 署名オプション。
1. 認証署名を適用し、更新された PDF ドキュメントを保存してください。

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com",
                "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
