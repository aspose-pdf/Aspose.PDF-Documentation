---
title: Excluir Imagens de Arquivo PDF usando Java
linktitle: Excluir Imagens
type: docs
weight: 20
url: /pt/java/delete-images-from-pdf-file/
description: Aprenda como excluir imagens incorporadas de arquivos PDF em Java.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Excluir imagens incorporadas de arquivos PDF com Java
Abstract: Este artigo mostra como excluir imagens de documentos PDF usando Aspose.PDF for Java. O exemplo remove um recurso de imagem da primeira página pelo seu índice na coleção de imagens da página e, em seguida, salva o documento modificado.
---
Use a coleção de recursos de imagem da página quando precisar remover imagens incorporadas de uma página PDF.

## Excluir uma imagem incorporada por índice

1. Abrir o PDF de origem [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acessar os recursos de imagem no destino [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Excluir a imagem de destino da coleção de recursos da página pelo seu índice.
1. Salvar o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
