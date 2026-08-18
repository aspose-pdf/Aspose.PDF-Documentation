---
title: Verificações de integridade de assinatura
linktitle: Verificações de integridade de assinatura
type: docs
weight: 70
url: /java/signature-integrity-checks/
description: Aprenda como validar a cobertura e integridade da assinatura em Java com a fachada PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Valide a cobertura e integridade da assinatura PDF em Java
Abstract: Aprenda como inspecionar a integridade da assinatura com Aspose.PDF para Java. O conjunto de exemplos Java atual usa `verifySignature` para validar a assinatura selecionada e `coversWholeDocument` para determinar se a assinatura protege todo o PDF.
---
## Verifique a integridade da assinatura

Este artigo mapeia o mesmo fluxo de trabalho de verificação exposto por `PdfFileSignatureExamples.java`.

### Passos

1. Vincule o PDF assinado com `PdfFileSignature`.
2. Selecione um nome de assinatura do documento.
3. Chame `verifySignature` para validar o conteúdo da assinatura.
4. Ligue para `coversWholeDocument` para confirmar a cobertura de todo o documento.
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
