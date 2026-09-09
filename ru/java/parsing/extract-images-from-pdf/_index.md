---
title: Извлечение изображений из PDF с помощью Java
linktitle: Извлечение изображений из PDF
type: docs
weight: 20
url: /ru/java/extract-images-from-the-pdf-file/
description: Узнайте, как извлекать встроенные изображения из PDF‑файлов с помощью Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь изображения из PDF с помощью Java
Abstract: В этой статье объясняется, как извлекать встроенные изображения из PDF‑документа с помощью Aspose.PDF for Java. Описывается, как открыть исходный PDF, получить доступ к изображению из коллекции ресурсов страницы и сохранить извлечённый XImage во внешний файл.
---
Извлекайте изображения со страниц PDF, когда необходимо повторно использовать встроенную графику, проверять ресурсы документа или экспортировать изображения для последующей обработки.

1. Откройте исходный PDF в [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр и откройте поток вывода для извлечённого файла изображения.
1. Получите целевой [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) из документа и получить к нему доступ `Resources.Images` коллекция.
1. Получите требуемый [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) объект из этой коллекции изображений по индексу.
1. Вызовите `image.save(outputImage)` записать извлечённые байты изображения в целевой поток.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```


