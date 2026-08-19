---
title: Установить вертикальное выравнивание поля
linktitle: Установить вертикальное выравнивание поля
type: docs
weight: 30
url: /ru/java/set-field-alignment-vertical/
description: Узнайте, как установить вертикальное выравнивание поля PDF-формы в Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Установить вертикальное выравнивание поля PDF-формы в Java
Abstract: В этой статье показано, как привязать существующий PDF, установить вертикальное выравнивание поля и сохранить обновленный документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Установите вертикальное выравнивание поля

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызов `setFieldAlignmentV(...)` для целевого поля и требуемой константы вертикального выравнивания.
3. Сохраните обновлённый документ.

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

