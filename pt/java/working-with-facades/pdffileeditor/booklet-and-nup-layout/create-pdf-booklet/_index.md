---
title: Criar livreto em PDF
linktitle: Criar livreto em PDF
type: docs
weight: 20
url: /java/create-pdf-booklet/
description: Crie um PDF pronto para livreto a partir de um documento existente em Java com a fachada PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gere saída de livreto a partir de um documento PDF em Java
Abstract: Aprenda como criar um livreto em PDF com Aspose.PDF para Java. O exemplo Java usa PdfFileEditor para reordenar páginas para impressão de livreto e também inclui uma variante de retorno booleano para verificação simples de sucesso.
---
## Crie um livreto em PDF

Use `PdfFileEditor.makeBooklet` para reorganizar as páginas de um PDF existente na ordem do livreto.

### Passos

1. Crie uma instância `PdfFileEditor`.
2. Chame `makeBooklet` com o PDF de origem e o arquivo de saída.
3. Salve o documento do livreto.
4. Se você quiser verificar o status de retorno, use a variante de retorno booleano e lide com um resultado com falha.

### Exemplo Java

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```
