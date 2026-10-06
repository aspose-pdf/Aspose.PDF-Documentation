---
title: "Java でのデジタル署名の追加または PDF へのデジタル署名"
linktitle: "PDF へのデジタル署名"
type: docs
weight: 10
url: /ja/java/digitally-sign-pdf-file/
description: "Aspose.PDF を使用して、Java で PDF 文書にデジタル署名および認証を行う方法を学習してください。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ファイルへのデジタル署名"
Abstract: "このガイドでは、Aspose.PDF for Java を使用して PDF ドキュメントにデジタル署名を行う方法を説明します。証明書オブジェクトによる署名、基本的な証明書パラメーターによる署名、および DocMDP 署名による文書認証と、署名後の変更を制御する方法をカバーしています。"
---
Aspose.PDF for Java は、`PdfFileSignature` を通じて複数の署名フローをサポートしています。

## 証明書オブジェクトの使用して PDF への署名

1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを作成し、ソース PDF ドキュメントをバインドしてください。
1. [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) 署名オブジェクトを作成し、署名オプションを構成してください。
1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) を使用して PDF ドキュメントに署名を適用してください。
1. 更新された PDF ドキュメントを保存してください。

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

このアプローチでは、まず `PKCS7` 署名オブジェクトを構築し、次にページ 1 に適用します。

## 基本的な証明書パラメータで PDF に署名

1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを作成し、ソース PDF ドキュメントをバインドしてください。
1. 署名サンプルで必要とされる証明書パラメータを構成してください。
1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) を使用して PDF ドキュメントに署名を適用してください。
1. 更新された PDF ドキュメントを保存してください。

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

## DocMDP で PDF の認証

認証レベルの制限が必要な場合は、文書の変更検出および防止署名を使用してください。

1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを作成し、ソース PDF ドキュメントをバインドしてください。
1. [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) オブジェクトを作成し、[DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/) 署名オプションを構成してください。
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
