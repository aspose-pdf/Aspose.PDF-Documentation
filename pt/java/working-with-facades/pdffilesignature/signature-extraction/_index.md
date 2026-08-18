---
title: Extração de assinatura
linktitle: Extração de assinatura
type: docs
weight: 50
url: /java/signature-extraction/
description: Aprenda como extrair o certificado de assinatura de um PDF assinado em Java com PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia um certificado de assinatura de PDF em Java
Abstract: Aprenda como extrair o certificado associado a uma assinatura PDF usando Aspose.PDF para Java. O conjunto de exemplos Java atual inclui extração de certificado para um fluxo de saída, mas não inclui uma amostra separada de extração de imagem de assinatura.
---
## Extrair certificado de assinatura

Use este fluxo de trabalho quando precisar salvar o certificado associado a uma assinatura existente.

### Passos

1. Crie uma instância `PdfFileSignature` e vincule o PDF assinado.
2. Selecione o nome da assinatura a ser inspecionada.
3. Chame `extractCertificate` para abrir o fluxo de certificados.
4. Copie os bytes do certificado para um arquivo de saída.
5. Feche os recursos de fluxo e o objeto de fachada.

### Exemplo Java

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

A classe `PdfFileSignatureExamples.java` atual não inclui uma amostra Java dedicada para extrair uma imagem de assinatura renderizada.
