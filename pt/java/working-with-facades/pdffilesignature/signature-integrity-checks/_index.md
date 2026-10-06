---
title: Verificações de Integridade de assinatura
linktitle: Verificações de Integridade de assinatura
type: docs
weight: 70
url: /pt/java/signature-integrity-checks/
description: Saiba como validar a cobertura e a integridade da assinatura em Java com a fachada PdfFileSignature.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar a cobertura e a integridade da assinatura PDF em Java
Abstract: Saiba como inspecionar a integridade da assinatura com Aspose.PDF for Java. O conjunto de exemplos atual em Java usa `verifySignature` para validar a assinatura selecionada e `coversWholeDocument` para determinar se a assinatura protege todo o PDF.
---
## Verificar integridade da assinatura

Este artigo mapeia para o mesmo fluxo de verificação exposto por `PdfFileSignatureExamples.java`.

### Etapas

1. Vincule o PDF assinado com `PdfFileSignature`.
2. Selecione um nome de assinatura do documento.
3. Chame `verifySignature` para validar o conteúdo da assinatura.
4. Chame `coversWholeDocument` para confirmar a cobertura em todo o documento.
5. Feche o objeto fachada.

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
