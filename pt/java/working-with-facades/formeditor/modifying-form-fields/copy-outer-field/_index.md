---
title: Copiar campo externo
linktitle: Copiar campo externo
type: docs
weight: 80
url: /java/copy-outer-field/
description: Aprenda como copiar um campo de formulário de um documento PDF para outro em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Copie um campo de formulário PDF entre documentos em Java
Abstract: Este artigo mostra como criar um PDF de destino, vinculá-lo à fachada do FormEditor, copiar um campo de outro documento e salvar o resultado usando Aspose.PDF para Java.
---
## Copiar um campo de outro PDF

1. Crie um PDF de destino com pelo menos uma página.
2. Vincule o PDF de destino à fachada `FormEditor`.
3. Chame `copyOuterField(...)` com o caminho do documento de origem, nome do campo, página de destino e coordenadas.
4. Salve o documento de destino atualizado.

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
