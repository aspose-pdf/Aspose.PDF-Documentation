---
title: Создать ссылки PDF в Java
linktitle: Создать ссылки
type: docs
weight: 10
url: /ru/java/create-links/
description: Узнайте, как создавать внутренние, внешние и удалённые ссылки PDF в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создавайте аннотации ссылок в PDF‑файлах с помощью Java
Abstract: В этой статье показано, как создавать аннотации ссылок с использованием Aspose.PDF for Java. Рассматриваются действия запуска, навигация к удалённому документу, навигация по страницам внутри документа и веб‑ссылки на основе URI, путем привязки действий к объектам LinkAnnotation.
---
Aspose.PDF for Java использует `LinkAnnotation` вместе с объектом действия для определения поведения ссылки.

## Создайте ссылку с действием запуска

Используйте этот пример, когда аннотация ссылки должна запускать внешний файл или цель.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и выберите целевую страницу.
1. Создайте [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) и настройте его границу и цвет.
1. Назначьте [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) и сохранить документ.

```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Создайте удалённую ссылку перехода

Используйте этот пример, когда ссылка должна открывать страницу в другом PDF‑документе.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) на целевой странице.
1. Назначьте [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) и сохранить файл вывода.

```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Создайте внутреннюю ссылку перехода

Используйте этот пример, когда ссылка должна переходить на другую страницу внутри того же PDF‑документа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) и настройте его внешний вид.
1. Назначьте [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) на страницу назначения и сохранить документ.

```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## Создайте URI‑ссылку

Используйте этот пример, когда ссылка должна открывать веб-ресурс через действие URI.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) на странице.
1. Назначьте [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) и сохранить файл вывода.

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```


