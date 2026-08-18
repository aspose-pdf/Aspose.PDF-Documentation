---
title: Verificação de assinatura
linktitle: Verificação de assinatura
type: docs
weight: 90
url: /java/signature-verification/
description: Aprenda como verificar assinaturas de PDF em Java com a fachada PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verifique assinaturas de PDF em Java
Abstract: Aprenda como verificar uma assinatura PDF com Aspose.PDF para Java. O exemplo Java seleciona a primeira assinatura disponível, valida a assinatura e verifica se ela cobre todo o documento.
---
## Verifique a assinatura do PDF

Use este fluxo de trabalho quando precisar de uma validação rápida em um PDF assinado existente.

### Passos

1. Crie uma instância `PdfFileSignature` e vincule o PDF assinado.
2. Selecione o nome da assinatura que você deseja inspecionar.
3. Ligue para `verifySignature` para validar a assinatura.
4. Ligue para `coversWholeDocument` para verificar a cobertura.
5. Feche o objeto de fachada.

### Exemplo Java

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
