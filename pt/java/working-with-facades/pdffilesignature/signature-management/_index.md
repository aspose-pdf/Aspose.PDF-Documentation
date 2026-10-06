---
title: Gerenciamento de Assinaturas
linktitle: Gerenciamento de Assinaturas
type: docs
weight: 80
url: /pt/java/signature-management/
description: Saiba como remover uma assinatura PDF existente em Java com a fachada PdfFileSignature.
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover assinaturas PDF em Java
Abstract: Saiba como remover uma assinatura de um PDF assinado com Aspose.PDF for Java. O conjunto atual de exemplos Java cobre a remoção de uma assinatura existente por nome e a gravação do documento atualizado. Ele não inclui um exemplo separado para limpar o campo de assinatura associado.
---
## Remover uma assinatura

Use este fluxo de trabalho quando uma assinatura digital existente precisar ser removida do documento.

### Etapas

1. Criar um `PdfFileSignature` instância e vincular o PDF assinado.
2. Leia a coleção de assinaturas e selecione um nome de assinatura.
3. Chamar `removeSignature` com esse nome.
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

O conjunto atual de exemplos em Java não inclui um método separado para remover o campo de assinatura associado após excluir a assinatura.
