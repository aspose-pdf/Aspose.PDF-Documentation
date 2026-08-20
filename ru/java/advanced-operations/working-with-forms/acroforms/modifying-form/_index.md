---
title: Изменение AcroForm
linktitle: Изменение AcroForm
type: docs
weight: 45
url: /ru/java/modifying-form/
description: Изменяйте поля AcroForm в PDF-документах с помощью Aspose.PDF for Java, включая очистку текста, установку ограничений, стилизацию полей и удаление полей.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Изменяйте и настраивайте поля PDF-форм с помощью Java
Abstract: В этой статье объясняется, как изменить содержимое AcroForm с использованием Aspose.PDF for Java. Она охватывает очистку текста из ресурсов формы Typewriter, установку и чтение ограничений длины текстовых полей, изменение внешнего вида Font поля формы, а также удаление определенных полей по имени.
---
Обслуживание форм зачастую включает как правки на уровне полей, так и очистку ресурсов страниц, связанных с формами.

## Очистить текст во встроенных ресурсах формы

Используйте этот пример, когда содержимое формы Typewriter должно быть опустошено без удаления самих объектов формы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Итеративно проходите ресурсы форм страниц и находите формы Typewriter.
1. Очистите поглощённые фрагменты текста и сохраните документ.

```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Установите ограничение длины текстового поля

Используйте этот пример, когда текстовое поле должно принимать только ограниченное количество символов.

1. Создайте [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) оболочка и привязка исходного PDF.
1. Установите максимальную длину для целевого поля.
1. Сохраните обновлённый документ.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Получите ограничение длины текстового поля

Используйте этот пример, когда нужно проверить текущую максимальную длину текстового поля.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите целевое поле из коллекции формы.
1. Прочитайте ограничение из [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) и вывести его.

```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## Изменить шрифт поля Form

Используйте этот пример, когда существующее текстовое поле должно использовать другой шрифт или внешний вид.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к цели [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) и установить новое значение по умолчанию внешнего вида.
1. Сохраните обновлённый PDF.

```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```

## Удалите поле формы по имени

Используйте этот пример, когда конкретное поле должно быть удалено из AcroForm.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите целевое поле из формы по его имени.
1. Сохраните обновлённый документ.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```


