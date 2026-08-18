---
title: Аннотации и специальный текст с использованием Java
linktitle: Аннотации и специальный текст
type: docs
weight: 40
url: /java/annotation-and-special-text/
description: Узнайте, как извлечь текст из примечаний к штампам, выделенного текста и содержимого надстрочных или подстрочных индексов в документах PDF с помощью Aspose.PDF для Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Извлеките выделенный текст

Просматривайте аннотации страниц и читайте отмеченный текст из `HighlightAnnotation`.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Выполните итерацию по объектам [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) на целевой [Странице](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Проверьте, является ли каждая аннотация [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/), прежде чем приводить ее к типизированному классу аннотаций.
1. Прочтите выделенный текст из каждой выделенной аннотации и распечатайте его на консоли.

```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## Извлечение текста из аннотаций штампов

Считайте поток нормального внешнего вида из аннотации штампа и передайте его через `TextAbsorber`.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Выполните итерацию по объектам [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) на целевой [Странице](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Отфильтруйте аннотации по типу `Stamp`.
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) и запросите запись обычного внешнего вида из словаря внешнего вида аннотации штампа.
1. Посетите внешний вид [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) и распечатайте извлеченный текст.

```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## Извлечение деталей текста надстрочного и нижнего индекса

Используйте `TextFragmentAbsorber`, когда вам нужен как извлеченный текст, так и флаги надстрочного или подстрочного индекса в каждом фрагменте.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) для анализа текста на уровне фрагментов.
1. Посетите целевую [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и соберите ее объекты [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Переберите эти фрагменты и прочитайте текст вместе с флагами верхнего и нижнего индекса из `fragment.getTextState()`.
1. Запишите извлеченные данные в выходной файл.

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
