---
title: Украсить поле
linktitle: Украсить поле
type: docs
weight: 10
url: /java/decorate-field/
description: Узнайте, как украсить поле PDF-формы цветами и выравниванием в Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Украсьте поле формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, настроить FormFieldFacade с цветами и выравниванием, украсить поле и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Украсьте поле

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Настройте `FormFieldFacade` с необходимыми цветами и выравниванием.
3. Передайте фасад редактору и позвоните `decorateField(...)`.
4. Сохраните обновленный документ.

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
