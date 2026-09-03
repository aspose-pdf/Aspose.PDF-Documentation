---
title: Удалить формы из PDF в Java
linktitle: Удалить формы
type: docs
weight: 70
url: /ru/java/remove-form/
description: Удалить объекты форм со страниц PDF, используя Aspose.PDF for Java, включая полную очистку и целенаправленное удаление.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить ресурсы форм со страниц PDF с помощью Java
Abstract: В этой статье объясняется, как удалить ресурсы форм из PDF‑документов с использованием Aspose.PDF for Java. Описывается очистка всех форм на странице и удаление только выбранных ресурсов формы Typewriter после фильтрации коллекции форм страницы.
---
Эти примеры удаляют ресурсы форм со страницы, а не просто изменяют значения полей.

## Удалите все ресурсы формы со страницы

Используйте этот пример, когда каждый ресурс формы на выбранной странице должен быть удалён в одной операции.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Доступ к [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) для целевой страницы.
1. Очистите коллекцию и сохраните обновлённый документ.

```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## Удалите конкретные ресурсы Form

Используйте этот пример, когда должны быть удалены только выбранные ресурсы Form, такие как формы Typewriter.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Доступ к [XFormCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) для целевой страницы.
1. Фильтруйте [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) ресурсы, которые вы хотите удалить, и удалить их из коллекции.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```


