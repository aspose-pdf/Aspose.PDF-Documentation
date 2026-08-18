---
title: Изменение АкроФормы
linktitle: Изменение АкроФормы
type: docs
weight: 45
url: /java/modifying-form/
description: Изменяйте поля AcroForm в документах PDF с помощью Aspose.PDF для Java, включая очистку текста, установку ограничений, стилизацию полей и удаление полей.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Изменение и настройка полей формы PDF с помощью Java
Abstract: В этой статье объясняется, как изменить содержимое AcroForm с помощью Aspose.PDF для Java. Он охватывает удаление текста из ресурсов формы «Пишущая машинка», установку и чтение ограничений длины текстовых полей, изменение внешнего вида шрифта поля формы и удаление определенных полей по имени.
---
Обслуживание форм часто включает в себя как редактирование на уровне полей, так и очистку ресурсов страницы, связанных с формой.

## Очистить текст во встроенных ресурсах формы

Используйте этот пример, когда содержимое формы «Пишущая машинка» необходимо очистить, не удаляя сами объекты формы.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Просмотрите ресурсы форм страницы и найдите формы пишущей машинки.
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

1. Создайте фасад [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) и привяжите исходный PDF-файл.
1. Установите максимальную длину целевого поля.
1. Сохраните обновленный документ.

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

Используйте этот пример, когда вам нужно проверить текущую максимальную длину текстового поля.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к целевому полю из коллекции форм.
1. Считайте ограничение из [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) и выведите его.

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

## Изменение шрифта поля формы

Используйте этот пример, когда существующее текстовое поле должно использовать другой шрифт или внешний вид.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к целевому элементу [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) и установите новый внешний вид по умолчанию.
1. Сохраните обновленный PDF-файл.

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

## Удаление поля формы по имени

Используйте этот пример, когда определенное поле необходимо удалить из AcroForm.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Delete the target field from the form by its name.
1. Сохраните обновленный документ.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
