---
title: Converta PDF/A e PDF/UA em PDF em Java
linktitle: Converta PDF/A e PDF/UA para PDF
type: docs
weight: 120
url: /java/convert-pdf_x-to-pdf/
lastmod: "2026-06-16"
description: Aprenda como remover a conformidade com PDF/A e PDF/UA de arquivos PDF baseados em padrões em Java e salvá-los como documentos PDF padrão.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF/A e PDF/UA em PDF padrão em Java
Abstract: Este artigo explica como remover a conformidade com PDF/A e PDF/UA de documentos PDF baseados em padrões usando Aspose.PDF para Java e, em seguida, salvar o resultado como um arquivo PDF padrão.
---
Aspose.PDF para Java pode converter variantes de PDF compatíveis com os padrões de volta em um documento PDF normal.

## Converter PDF/A em PDF padrão

Use este exemplo quando um documento PDF/A de arquivo precisar ser rebaixado para um PDF padrão.

1. Abra o arquivo PDF/A de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame `removePdfaCompliance()` para separar o perfil de conformidade de arquivamento do documento carregado.
1. Salve o arquivo PDF padrão resultante sem o conjunto de restrições PDF/A.

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## Converter PDF/UA em PDF padrão

Use este exemplo quando um documento PDF/UA acessível precisar ser convertido novamente em um PDF padrão.

1. Abra o arquivo PDF/UA de origem em uma instância [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Chame `removePdfUaCompliance()` para remover o perfil de conformidade de acessibilidade dos metadados do documento e dos requisitos de estrutura.
1. Salve o documento PDF resultante como um arquivo PDF normal.

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
