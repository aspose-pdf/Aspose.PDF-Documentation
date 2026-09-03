---
title: Извлечение PDF‑ссылок в Java
linktitle: Извлечь ссылки
type: docs
weight: 30
url: /ru/java/extract-links/
description: Узнайте, как извлекать аннотации ссылок и гиперссылки из PDF‑документов на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлеките аннотации ссылок и URI‑цели из PDF‑файлов с помощью Java
Abstract: В этой статье объясняется, как извлекать аннотации ссылок из PDF‑документов с использованием Aspose.PDF for Java. Показано, как перечислять аннотации ссылок на странице, считывать их индекс страницы и прямоугольник, а также извлекать URI‑цели из экземпляров GoToURIAction.
---
Вы можете проверять ссылки PDF, перебирая аннотации страниц и отфильтровывая `AnnotationType.Link`.

## Извлеките аннотации ссылок

Используйте этот пример, когда вам нужна информация о местоположении и странице для аннотаций ссылок на странице.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Итерируйте аннотации страницы и отфильтруйте аннотации ссылок.
1. Прочитайте индекс страницы и прямоугольник для каждой подходящей ссылки.

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

## Извлеките назначения гиперссылок

Используйте этот пример, когда нужно прочитать целевые URI из аннотаций веб-ссылок.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найти [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) объекты, действие которых является [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Выведите индекс страницы и целевой URI для каждой гиперссылки.

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


