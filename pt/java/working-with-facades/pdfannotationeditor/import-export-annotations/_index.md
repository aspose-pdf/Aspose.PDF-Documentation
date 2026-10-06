---
title: Importar e exportar anotações usando Java
linktitle: Importar e exportar anotações
type: docs
weight: 80
url: /pt/java/pdfannotationeditor-class/import-export-annotations/
description: Aprenda como copiar anotações de um documento PDF para outro documento PDF usando Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Transferir anotações PDF entre documentos em Java
Abstract: Este artigo explica como copiar anotações de um PDF de origem e exportá‑las para um novo documento PDF usando Java. O fluxo de trabalho carrega o arquivo de origem, cria o documento de destino, adiciona uma página, copia as anotações da primeira página de origem e salva o resultado.
---
## Copiar anotações de um PDF para outro

1. Abra o PDF de origem e crie um novo documento de destino com uma página de destino.
2. Enumere as anotações na primeira página de origem e adicione cada uma à página de destino.
3. Salve o documento de destino para preservar as anotações copiadas.

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
