---
title: Обновить ссылки PDF в Java
linktitle: Обновить ссылки
type: docs
weight: 20
url: /ru/java/update-links/
description: Узнайте, как обновить внешний вид и назначения ссылок PDF в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Обновите внешний вид аннотаций ссылок и веб‑назначения в файлах PDF с помощью Java
Abstract: Эта статья показывает, как обновлять существующие аннотации ссылок с помощью Aspose.PDF for Java. Примеры демонстрируют изменение цвета текста, покрытого ссылкой, обновление цвета аннотации ссылки и замену целевого URI для веб‑ссылок.
---
Существующие ссылки можно редактировать, найдя аннотацию ссылки на странице и обновив либо её внешний вид, либо её действие.

## Обновите цвет связанного текста

Используйте этот пример, когда область текста, покрытая аннотацией ссылки, должна быть перекрашена.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите аннотации ссылок и создайте прямоугольник поиска текста из каждой области аннотации.
1. Перекрасьте найденные фрагменты текста и сохраните документ.

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

## Обновите цвет границы ссылки

Используйте этот пример, когда необходимо изменить видимый цвет существующих аннотаций ссылок.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите аннотации страницы и отфильтруйте по [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) объекты.
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

## Обновите назначение веб‑ссылки

Используйте этот пример, когда существующая веб‑ссылка должна указывать на новый URI.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите аннотации ссылок, действие которых является [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/).
1. Замените URI и сохраните обновлённый документ.

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


