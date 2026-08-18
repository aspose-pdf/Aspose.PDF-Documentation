---
title: Girar páginas PDF em Java
linktitle: Girando páginas PDF
type: docs
weight: 110
url: /java/rotate-pages/
description: Aprenda como girar páginas PDF e alterar a orientação da página em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gire páginas PDF com Java
Abstract: Este artigo explica como girar páginas PDF usando Aspose.PDF para Java. O exemplo percorre todas as páginas de um documento, aplica uma rotação de 90 graus e salva o PDF atualizado.
---
Use a API de rotação de página quando precisar alterar a orientação em uma ou mais páginas.

## Girar todas as páginas em 90 graus

Use este exemplo quando cada página do documento precisar ser girada no sentido horário.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Itere todos os objetos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) e defina o valor de rotação.
1. Salve o PDF atualizado.

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```
