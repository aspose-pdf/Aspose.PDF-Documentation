---
title: Поворот страниц PDF в Java
linktitle: Поворот страниц PDF
type: docs
weight: 110
url: /ru/java/rotate-pages/
description: Узнайте, как повернуть страницы PDF и изменить ориентацию страницы в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Повернуть страницы PDF с помощью Java
Abstract: В этой статье объясняется, как повернуть страницы PDF с использованием Aspose.PDF for Java. Пример проходит по всем страницам документа, применяет вращение на 90 градусов и сохраняет обновленный PDF.
---
Используйте API поворота страниц, когда необходимо изменить ориентацию на одной или нескольких страницах.

## Повернуть все страницы на 90 градусов

Используйте этот пример, когда каждая страница документа должна быть повернута по часовой стрелке.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебрать все [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) объекты и установить значение вращения.
1. Сохраните обновленный PDF.

```java
public static void rotatePage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.setRotate(Rotation.on90);
        }
        document.save(outputFile.toString());
    }
}
```

