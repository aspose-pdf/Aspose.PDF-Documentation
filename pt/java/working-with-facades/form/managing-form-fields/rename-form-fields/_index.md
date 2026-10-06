---
title: Renomear campos de formulário
linktitle: Renomear campos de formulário
type: docs
weight: 30
url: /pt/java/rename-form-fields/
description: Saiba como renomear campos de formulário PDF em Java usando a fachada Form do Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Renomear campos de formulário em um documento PDF com Java
Abstract: Este artigo mostra como vincular um formulário PDF, renomear campos existentes e salvar o documento atualizado usando a fachada Form no Aspose.PDF for Java.
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
