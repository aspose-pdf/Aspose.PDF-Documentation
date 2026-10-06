---
title: Verificação de assinatura
linktitle: Verificação de assinatura
type: docs
weight: 90
url: /pt/java/signature-verification/
description: Aprenda como verificar assinaturas PDF em Java com a fachada PdfFileSignature.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verificar assinaturas PDF em Java
Abstract: Aprenda como verificar uma assinatura PDF com Aspose.PDF for Java. O exemplo Java seleciona a primeira assinatura disponível, valida a assinatura e verifica se ela cobre todo o documento.
---
## Verificar assinatura PDF

Use este fluxo de trabalho quando precisar de uma validação rápida em um PDF já assinado.

### Etapas

1. Crie uma instância de `PdfFileSignature` e vincule o PDF assinado.
2. Selecione o nome da assinatura que deseja inspecionar.
3. Chame `verifySignature` para validar a assinatura.
4. Chame `coversWholeDocument` para verificar a cobertura.
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
