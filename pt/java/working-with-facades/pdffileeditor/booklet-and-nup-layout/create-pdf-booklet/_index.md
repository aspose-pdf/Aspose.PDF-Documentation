---
title: Criar livreto PDF
linktitle: Criar livreto PDF
type: docs
weight: 20
url: /pt/java/create-pdf-booklet/
description: Criar um PDF pronto para livreto a partir de um documento existente em Java com a fachada PdfFileEditor.
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerar saída de livreto a partir de um documento PDF em Java
Abstract: Saiba como criar um livreto PDF com Aspose.PDF for Java. O exemplo Java usa PdfFileEditor para reorganizar as páginas para impressão em livreto e também inclui uma variante que retorna um booleano para verificação simples de sucesso.
---
## Criar um livreto PDF

Usar `PdfFileEditor.makeBooklet` reorganizar as páginas de um PDF existente em ordem de livreto.

### Etapas

1. Criar um `PdfFileEditor` instância.
2. Chamada `makeBooklet` com o PDF de origem e o arquivo de saída.
3. Salve o documento do livreto.
4. Se quiser verificar o status de retorno, use a variante que devolve booleano e trate um resultado falho.

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
