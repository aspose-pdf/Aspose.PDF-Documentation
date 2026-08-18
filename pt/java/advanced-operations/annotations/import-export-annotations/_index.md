---
title: Importar e exportar anotações usando Java
linktitle: Importar e exportar anotações
type: docs
weight: 80
url: /java/import-export-annotations/
description: Aprenda como copiar anotações de um documento PDF para outro documento PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transfira anotações de PDF entre documentos em Java.
Abstract: Este artigo explica como copiar anotações de um PDF de origem e exportá-las para um novo documento PDF usando Aspose.PDF para Java. O fluxo de trabalho carrega o arquivo de origem, cria o documento de destino, adiciona uma página, copia anotações da primeira página de origem e salva o resultado.
---
## Copie anotações de um PDF para outro

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/ de destino).
1. Adicione cada [Anotação](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) à [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino.
1. Leia ou repita os itens [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) na página de destino.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enumere os itens [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) na primeira página de origem e adicione cada um deles à página de destino.

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
