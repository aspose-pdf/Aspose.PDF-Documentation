---
title: Converter PDF/A e PDF/UA para PDF em Java
linktitle: Converter PDF/A e PDF/UA para PDF
type: docs
weight: 120
url: /pt/java/convert-pdf_x-to-pdf/
lastmod: "2026-10-06"
description: Aprenda como remover a conformidade PDF/A e PDF/UA de arquivos PDF baseados em padrões em Java e salvá-los como documentos PDF padrão.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Converter PDF/A e PDF/UA para PDF padrão em Java
Abstract: Este artigo explica como remover a conformidade PDF/A e PDF/UA de documentos PDF baseados em padrões usando Aspose.PDF for Java, e então salvar o resultado como um arquivo PDF padrão.
---
Aspose.PDF for Java pode converter variantes PDF compatíveis com padrões de volta para um documento PDF normal.

## Converter PDF/A para PDF padrão

Use este exemplo quando um documento PDF/A de arquivamento deve ser rebaixado para um PDF padrão.

1. Abra o arquivo PDF/A de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame `removePdfaCompliance()` desvincular o perfil de conformidade de arquivamento do documento carregado.
1. Salve o arquivo PDF padrão resultante sem a restrição de PDF/A definida.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## Converter PDF/UA para PDF padrão

Use este exemplo quando um documento PDF/UA acessível deve ser convertido de volta para um PDF padrão.

1. Abra o arquivo PDF/UA de origem em uma instância de [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame `removePdfUaCompliance()` remover o perfil de conformidade de acessibilidade dos metadados do documento e dos requisitos de estrutura.
1. Salve o documento PDF resultante como um arquivo PDF normal.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
