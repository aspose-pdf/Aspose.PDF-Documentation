---
title: Извлечение PDF-ссылок в Java
linktitle: Извлечь ссылки
type: docs
weight: 30
url: /java/extract-links/
description: Узнайте, как извлекать аннотации и гиперссылки из PDF-документов на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение аннотаций ссылок и целевых объектов URI из файлов PDF с помощью Java
Abstract: В этой статье объясняется, как извлечь аннотации ссылок из PDF-документов с помощью Aspose.PDF для Java. Он показывает, как перечислять аннотации ссылок на странице, читать их индекс страницы и прямоугольник, а также извлекать целевые URI из экземпляров GoToURIAction.
---
Вы можете проверять ссылки PDF, перебирая аннотации страниц и фильтруя их по `AnnotationType.Link`.

## Извлеките аннотации ссылок

Используйте этот пример, если вам нужна информация о местоположении и странице для аннотаций ссылок на странице.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебирайте аннотации страниц и фильтруйте аннотации ссылок.
1. Прочтите индекс страницы и прямоугольник для каждой соответствующей ссылки.

```java
public static void extractLinkAnnotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                System.out.println("Page: " + linkAnnotation.getPageIndex()
                        + ", location: " + linkAnnotation.getRect());
            }
        }
    }
}
```

## Извлеките места назначения гиперссылок

Используйте этот пример, когда вам нужно прочитать целевые URI из аннотаций веб-ссылок.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите объекты [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/), действием которых является [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Распечатайте индекс страницы и целевой URI для каждой гиперссылки.

```java
public static void extractHyperlinks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    System.out.println("Page " + linkAnnotation.getPageIndex() + ", URI:" + action.getURI());
                }
            }
        }
    }
}
```
