---
title: Importar e exportar anotações usando Java
linktitle: Importar e exportar anotações
type: docs
weight: 80
url: /pt/java/import-export-annotations/
description: Saiba como copiar anotações de um documento PDF para outro documento PDF usando Aspose.PDF for Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transferir anotações de PDF entre documentos em Java
Abstract: Este artigo explica como copiar anotações de um PDF de origem e exportá‑las para um novo documento PDF usando Aspose.PDF for Java. O fluxo de trabalho carrega o arquivo de origem, cria o documento de destino, adiciona uma página, copia as anotações da primeira página de origem e salva o resultado.
---
## Copiar anotações de um PDF para outro

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) para o destino [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione cada [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) para a página de destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Leia ou itere através do [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) itens na página de destino.
1. Salve o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumerar o [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) itens na primeira página de origem e adicione cada um à página de destino.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
