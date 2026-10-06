---
title: Remover Campo
linktitle: Remover Campo
type: docs
weight: 40
url: /pt/java/remove-field/
description: Saiba como remover um campo de formulário existente de um documento PDF em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Excluir um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, remover um campo especificado e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF for Java.
---
## Remover um campo

1. Vincule o PDF de origem ao `FormEditor` fachada.
2. Chamar `removeField(...)` para o nome do campo de destino.
3. Salve o documento atualizado.

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
