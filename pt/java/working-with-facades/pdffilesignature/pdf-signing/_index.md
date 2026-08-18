---
title: Assinar documentos PDF
linktitle: Assinar documentos PDF
type: docs
weight: 10
url: /java/pdf-signing/
description: Aprenda como assinar documentos PDF em Java com a fachada PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assine documentos PDF com assinaturas digitais em Java
Abstract: Aprenda como assinar documentos PDF com Aspose.PDF para Java. O conjunto de exemplos Java abrange a assinatura com um caminho de certificado e senha configurados e a assinatura com um objeto de assinatura PKCS7 explícito que inclui metadados de assinatura, como motivo, informações de contato, localização e autoridade.
---
## Assine documentos PDF

Use `PdfFileSignature` quando precisar aplicar uma assinatura digital visível a um PDF.

### Passos

1. Crie uma instância `PdfFileSignature` e vincule o PDF de origem.
2. Carregue o certificado por meio de `setCertificate` ou criando um objeto `PKCS7`.
3. Chame `sign` com a página de destino, configurações de visibilidade, retângulo de assinatura e dados de assinatura.
4. Salve o PDF assinado e feche o objeto fachada.

### Exemplos Java

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
