---
title: Поворот страниц PDF в Java
linktitle: Вращение страниц PDF
type: docs
weight: 110
url: /java/rotate-pages/
description: Узнайте, как поворачивать страницы PDF и изменять ориентацию страниц в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Поворот страниц PDF с помощью Java
Abstract: В этой статье объясняется, как вращать страницы PDF с помощью Aspose.PDF для Java. В примере перебираются все страницы документа, применяется поворот на 90 градусов и сохраняется обновленный PDF-файл.
---
Используйте API поворота страниц, когда вам нужно изменить ориентацию одной или нескольких страниц.

## Поворот всех страниц на 90 градусов

Используйте этот пример, когда каждую страницу документа необходимо повернуть по часовой стрелке.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите все объекты [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и установите значение поворота.
1. Сохраните обновленный PDF-файл.

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
