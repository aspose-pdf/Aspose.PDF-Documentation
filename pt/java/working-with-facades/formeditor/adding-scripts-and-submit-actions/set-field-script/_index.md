---
title: Definir script de campo
linktitle: Definir script de campo
type: docs
weight: 20
url: /java/set-field-script/
description: Aprenda como atribuir ou atualizar uma ação JavaScript em um campo de formulário PDF em Java usando a fachada FormEditor em Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Defina uma ação JavaScript em um campo de formulário PDF em Java
Abstract: Este artigo mostra como vincular um PDF existente, adicionar um script inicial, substituí-lo por um script atualizado e salvar o documento modificado usando a fachada FormEditor em Aspose.PDF para Java.
---
## Defina um script de campo

1. Vincule o PDF de origem à fachada `FormEditor`.
2. Adicione uma ação JavaScript inicial ao campo.
3. Substitua-o pelo texto do script atualizado.
4. Salve o documento atualizado.

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
