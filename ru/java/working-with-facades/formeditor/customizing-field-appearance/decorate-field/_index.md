---
title: Оформить поле
linktitle: Оформить поле
type: docs
weight: 10
url: /ru/java/decorate-field/
description: Узнайте, как оформить поле формы PDF с помощью цветов и выравнивания в Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Оформить поле формы PDF в Java
Abstract: В этой статье показано, как привязать существующий PDF, настроить FormFieldFacade с использованием цветов и выравнивания, оформить поле и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Оформите поле

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Настройте `FormFieldFacade` с требуемыми цветами и выравниванием.
3. Передайте фасад редактору и вызовите `decorateField(...)`.
4. Сохраните обновлённый документ.

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


