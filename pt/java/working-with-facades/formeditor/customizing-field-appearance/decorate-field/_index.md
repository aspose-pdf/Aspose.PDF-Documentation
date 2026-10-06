---
title: Decorar campo
linktitle: Decorar campo
type: docs
weight: 10
url: /pt/java/decorate-field/
description: Aprenda como decorar um campo de formulário PDF com cores e alinhamento em Java usando a fachada FormEditor no Aspose.PDF.
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Decorar um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, configurar um FormFieldFacade com cores e alinhamento, decorar um campo e salvar o documento atualizado usando a fachada FormEditor no Aspose.PDF for Java.
---
## Decorar um campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Configure um `FormFieldFacade` com as cores e alinhamento necessários.
3. Passe a fachada para o editor e chame `decorateField(...)`.
4. Salve o documento atualizado.

```java
public static void decorateField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        FormFieldFacade facade = new FormFieldFacade();
        facade.setBackgroundColor(Color.RED);
        facade.setTextColor(Color.BLUE);
        facade.setBorderColor(Color.GREEN);
        facade.setAlignment(FormFieldFacade.ALIGN_CENTER);
        editor.setFacade(facade);
        editor.decorateField("First Name");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
