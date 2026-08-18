---
title: Renomear campos do formulário
linktitle: Renomear campos do formulário
type: docs
weight: 30
url: /java/rename-form-fields/
description: Aprenda como renomear campos de formulário PDF em Java usando a fachada do formulário em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Renomeie campos de formulário em um documento PDF com Java
Abstract: Este artigo mostra como vincular um formulário PDF, renomear campos existentes e salvar o documento atualizado com a fachada Form em Aspose.PDF para Java.
---
Use `FormExamples.renameFormFields(...)` para renomear campos em um formulário PDF interativo.

```java
public static void renameFormFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.renameField("First Name", "NewFirstName");
        form.renameField("Last Name", "NewLastName");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
