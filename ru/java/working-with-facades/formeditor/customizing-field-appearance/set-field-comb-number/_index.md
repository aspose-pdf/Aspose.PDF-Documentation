---
title: Установить число ячеек поля
linktitle: Установить число ячеек поля
type: docs
weight: 60
url: /ru/java/set-field-comb-number/
description: Узнайте, как установить число ячеек для поля формы PDF в Java с использованием фасада FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Установить число ячеек для поля формы PDF в Java
Abstract: В этой статье показано, как привязать существующий PDF, установить число ячеек для поля и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF для Java.
---
## Установите число ячеек поля

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызов `setFieldCombNumber(...)` для целевого поля и значения comb.
3. Сохраните обновленный документ.

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

