---
title: "Java での PDF の署名情報の抽出"
linktitle: "署名から詳細の抽出"
type: docs
weight: 20
url: /ja/java/extract-image-and-signature-information/
description: Java で PDF ファイルから証明書とデジタル署名の詳細を抽出する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での 署名された PDF から署名の詳細と証明書データの抽出"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントのデジタル署名を検査する方法を説明します。署名者の詳細を読み取る方法、署名を検証する方法、署名が文書全体をカバーしているか確認する方法、埋め込まれた署名証明書を抽出する方法、既存の署名を削除する方法を学びます。
---
使用 `PdfFileSignature` で、PDF ドキュメントに既に存在する署名を検査し、管理します。

## 署名情報を読み取る

1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを作成し、ソース PDF ドキュメントをバインドしてください。
1. ドキュメント署名名にアクセスし、サンプルで必要とされる署名検査フローを構成してください。
1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードから署名情報を読み取り、検証してください。
1. 返された値を読み取るか、次の処理ステップに進んでください。

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## 署名の検証

1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを作成し、ソース PDF ドキュメントをバインドしてください。
1. ドキュメント署名名にアクセスし、例で要求される検証フローを構成してください。
1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードから署名情報を読み取り、検証してください。

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: "
                + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: "
                + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## 署名証明書の抽出

1. [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードを作成し、ソース PDF ドキュメントをバインドしてください。
1. 証明書抽出に必要なドキュメント署名名にアクセスしてください。
1. 抽出された出力を書き込むか、[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) ファサードから返された値を検査してください。

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```
