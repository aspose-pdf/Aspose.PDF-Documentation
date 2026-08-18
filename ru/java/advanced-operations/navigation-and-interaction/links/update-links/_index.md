---
title: Обновить PDF-ссылки в Java
linktitle: Обновить ссылки
type: docs
weight: 20
url: /java/update-links/
description: Узнайте, как обновить внешний вид и места назначения ссылок PDF в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обновление внешнего вида аннотаций ссылок и веб-адресов в файлах PDF с помощью Java
Abstract: В этой статье показано, как обновить существующие аннотации ссылок с помощью Aspose.PDF для Java. В примерах показано изменение цвета текста, покрытого ссылкой, обновление цвета аннотации ссылки и замена целевого URI для веб-ссылок.
---
Существующие ссылки можно редактировать, найдя аннотацию ссылки на странице и обновив ее внешний вид или действие.

## Обновите цвет связанного текста

Используйте этот пример, когда необходимо перекрасить текстовую область, покрытую аннотацией ссылки.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите аннотации ссылок и постройте прямоугольник текстового поиска из каждой области аннотаций.
1. Перекрасьте совпавшие фрагменты текста и сохраните документ.

```java
public static void linkAnnotationUpdateTextColor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX() - 2);
                rect.setLLY(rect.getLLY() - 2);
                rect.setURX(rect.getURX() + 2);
                rect.setURY(rect.getURY() + 2);
                absorber.setTextSearchOptions(new TextSearchOptions(rect));
                absorber.visit(document.getPages().get_Item(1));
                for (TextFragment textFragment : absorber.getTextFragments()) {
                    textFragment.getTextState().setForegroundColor(Color.getRed());
                }
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Обновите цвет рамки ссылки

Используйте этот пример, когда необходимо изменить видимый цвет существующих аннотаций ссылок.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Просмотрите аннотации страниц и отфильтруйте объекты [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/).
1. Обновите цвет аннотации ссылки и сохраните документ.

```java
public static void linkAnnotationUpdateBorder(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                linkAnnotation.setColor(Color.getRed());
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Обновите место назначения веб-ссылки

Используйте этот пример, когда существующая веб-ссылка должна указывать на новый URI.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите аннотации ссылок, действие которых — [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Замените URI и сохраните обновленный документ.

```java
public static void linkAnnotationUpdateWebDestination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    action.setURI("https://www.aspose.com");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
