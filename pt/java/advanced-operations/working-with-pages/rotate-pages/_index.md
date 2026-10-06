---
title: Rotacionar páginas PDF em Java
linktitle: Rotacionando páginas PDF
type: docs
weight: 110
url: /pt/java/rotate-pages/
description: Aprenda como rotacionar páginas PDF e mudar a orientação da página em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotacione páginas PDF com Java
Abstract: Este artigo explica como rotacionar páginas PDF usando Aspose.PDF for Java. O exemplo percorre todas as páginas de um documento, aplica uma rotação de 90 graus e salva o PDF atualizado.
---
Use a API de rotação de página quando precisar mudar a orientação em uma ou mais páginas.

## Gire todas as páginas em 90 graus

Use este exemplo quando todas as páginas do documento devem ser giradas no sentido horário.

1. Abra o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Iterar por todos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) objetos e definir o valor de rotação.
1. Salvar o PDF atualizado.

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
