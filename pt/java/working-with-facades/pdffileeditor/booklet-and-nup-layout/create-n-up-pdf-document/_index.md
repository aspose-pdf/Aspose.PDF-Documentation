---
title: Criar documento PDF N-Up
linktitle: Criar documento PDF N-Up
type: docs
weight: 10
url: /java/create-n-up-pdf-document/
description: Crie um layout PDF 2x2 N-Up em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gere um layout PDF N-Up a partir de um documento existente em Java
Abstract: Aprenda como criar um documento PDF N-Up com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor para colocar quatro páginas de origem em cada planilha de saída e também mostra uma variante de retorno booleano para verificação de falhas.
---
## Crie um documento PDF N-Up

O exemplo Java usa `PdfFileEditor.makeNUp` para construir um layout 2x2 a partir de um PDF existente.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Chame `makeNUp` com o arquivo de entrada, o arquivo de saída e o número de colunas e linhas.
3. Salve o documento gerado.
4. Se você deseja uma verificação explícita de sucesso, chame a variante de retorno booleano e manipule um resultado `false`.

### Exemplo Java

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
