---
title: Copiar Campo Externo
linktitle: Copiar Campo Externo
type: docs
weight: 80
url: /pt/java/copy-outer-field/
description: Aprenda como copiar um campo de formulário de um documento PDF para outro em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Copiar um campo de formulário PDF entre documentos em Java
Abstract: Este artigo mostra como criar um PDF de destino, vinculá-lo à fachada FormEditor, copiar um campo de outro documento e salvar o resultado usando o Aspose.PDF for Java.
---
## Copiar um campo de outro PDF

1. Crie um PDF de destino com pelo menos uma página.
2. Vincule o PDF de destino ao `FormEditor` fachada.
3. Chamar `copyOuterField(...)` com o caminho do documento de origem, nome do campo, página de destino e coordenadas.
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
