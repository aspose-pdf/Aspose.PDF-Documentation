---
title: Удалить изображения из PDF-файла с помощью Java
linktitle: Удалить изображения
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: Узнайте, как удалить встроенные изображения из файлов PDF в Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Удаление встроенных изображений из файлов PDF с помощью Java
Abstract: В этой статье показано, как удалить изображения из PDF-документов с помощью Aspose.PDF для Java. В примере ресурс изображения удаляется с первой страницы по его индексу в коллекции изображений страниц, а затем сохраняется измененный документ.
---
Используйте коллекцию ресурсов изображений страниц, когда вам нужно удалить встроенные изображения со страницы PDF.

## Удалите встроенное изображение по индексу

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к ресурсам изображений на целевой [Странице](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Удалите целевое изображение из коллекции ресурсов страницы по его индексу.
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
