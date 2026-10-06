---
title: Adicionar margens às páginas PDF
linktitle: Adicionar margens às páginas PDF
type: docs
weight: 10
url: /pt/java/add-margins-to-pdf-pages/
description: Adicionar margens às páginas PDF selecionadas em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar margens a páginas específicas em um documento PDF com Java
Abstract: Saiba como adicionar margens a páginas selecionadas com Aspose.PDF for Java. O exemplo em Java usa PdfFileEditor para direcionar números de página individuais e aplicar valores iguais de margem superior, inferior, esquerda e direita.
---
## Adicionar margens às páginas PDF

O exemplo em Java adiciona margens de 36 pontos às páginas 1 e 3 do documento de origem.

### Etapas

1. Crie uma instância de `PdfFileEditor`.
2. Selecione os números de página que devem receber novas margens.
3. Chame `addMargins` com o arquivo de entrada, arquivo de saída, lista de páginas e valores de margem.
4. Salve o PDF atualizado.

### Exemplo Java

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
