---
title: Gerenciamento de assinatura
linktitle: Gerenciamento de assinatura
type: docs
weight: 80
url: /java/signature-management/
description: Aprenda como remover uma assinatura PDF existente em Java com a fachada PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remova assinaturas de PDF em Java
Abstract: Aprenda como remover uma assinatura de um PDF assinado com Aspose.PDF para Java. O conjunto de exemplos Java atual abrange a remoção de uma assinatura existente por nome e o salvamento do documento atualizado. Não inclui uma amostra separada para limpar o campo de assinatura associado.
---
## Remover uma assinatura

Use este fluxo de trabalho quando uma assinatura digital existente precisar ser removida do documento.

### Passos

1. Crie uma instância `PdfFileSignature` e vincule o PDF assinado.
2. Leia a coleção de assinaturas e selecione um nome de assinatura.
3. Ligue para `removeSignature` com esse nome.
4. Salve o arquivo atualizado e feche o objeto fachada.

### Exemplo Java

```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

O conjunto de amostras Java atual não inclui um método separado para remover o campo de assinatura associado após excluir a assinatura.
