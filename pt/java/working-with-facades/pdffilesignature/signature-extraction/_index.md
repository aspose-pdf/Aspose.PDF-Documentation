---
title: Extração de assinatura
linktitle: Extração de assinatura
type: docs
weight: 50
url: /pt/java/signature-extraction/
description: Aprenda como extrair o certificado de assinatura de um PDF assinado em Java com PdfFileSignature.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair um certificado de assinatura de PDF em Java
Abstract: Aprenda como extrair o certificado associado a uma assinatura de PDF usando Aspose.PDF for Java. O conjunto atual de exemplos em Java inclui a extração do certificado para um fluxo de saída, mas não inclui um exemplo separado de extração de imagem da assinatura.
---
## Extrair certificado de assinatura

Use este Workflow quando precisar salvar o certificado associado a uma assinatura existente.

### Etapas

1. Crie uma instância de `PdfFileSignature` e associe o PDF assinado.
2. Selecione o nome da assinatura para inspecionar.
3. Chame `extractCertificate` para abrir o fluxo do certificado.
4. Copie os bytes do certificado para um arquivo de saída.
5. Feche os recursos do fluxo e o objeto fachada.

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

O atual `PdfFileSignatureExamples.java` A classe não inclui um exemplo Java dedicado para extrair uma imagem de assinatura renderizada.
