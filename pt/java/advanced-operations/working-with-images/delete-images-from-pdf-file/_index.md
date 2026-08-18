---
title: Excluir imagens do arquivo PDF usando Java
linktitle: Excluir imagens
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: Aprenda como excluir imagens incorporadas de arquivos PDF em Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Exclua imagens incorporadas de arquivos PDF com Java
Abstract: Este artigo mostra como excluir imagens de documentos PDF usando Aspose.PDF para Java. O exemplo remove um recurso de imagem da primeira página pelo seu índice na coleção de imagens da página e depois salva o documento modificado.
---
Use a coleção de recursos de imagem de página quando precisar remover imagens incorporadas de uma página PDF.

## Excluir uma imagem incorporada por índice

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acesse os recursos de imagem na [página] de destino (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Exclua a imagem de destino da coleção de recursos de página por seu índice.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
