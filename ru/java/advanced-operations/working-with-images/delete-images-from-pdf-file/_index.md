---
title: Удалить изображения из PDF-файла с помощью Java
linktitle: Удалить изображения
type: docs
weight: 20
url: /ru/java/delete-images-from-pdf-file/
description: Узнайте, как удалить встроенные изображения из PDF‑файлов на Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Удалить встроенные изображения из PDF‑файлов с Java
Abstract: В этой статье показано, как удалять изображения из PDF‑документов с использованием Aspose.PDF for Java. Пример удаляет ресурс изображения с первой страницы по его индексу в коллекции изображений страницы, а затем сохраняет изменённый документ.
---
Используйте коллекцию ресурсов изображений страницы, когда необходимо удалить встроенные изображения со страницы PDF.

## Удалите встроенное изображение по индексу

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к ресурсам изображений в целевом файле [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Удалите целевое изображение из коллекции ресурсов страницы по его индексу.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```

