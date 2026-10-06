---
title: Criar documento PDF N-Up
linktitle: Criar documento PDF N-Up
type: docs
weight: 10
url: /pt/java/create-n-up-pdf-document/
description: Criar um layout PDF N-Up 2x2 em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerar um layout PDF N-Up a partir de um documento existente em Java
Abstract: Aprenda como criar um documento PDF N-Up com Aspose.PDF for Java. O exemplo Java usa PdfFileEditor para colocar quatro páginas de origem em cada folha de saída e também mostra uma variante que retorna booleano para verificação de falhas.
---
## Criar um documento PDF N-Up

O exemplo Java usa `PdfFileEditor.makeNUp` para construir um layout 2x2 a partir de um PDF existente.

### Etapas

1. Criar um `PdfFileEditor` instância.
2. Chamar `makeNUp` com o arquivo de entrada, arquivo de saída e o número de colunas e linhas.
3. Salve o documento gerado.
4. Se você quiser verificação explícita de sucesso, chame a variante que retorna booleano e trate um `false` resultado.

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
