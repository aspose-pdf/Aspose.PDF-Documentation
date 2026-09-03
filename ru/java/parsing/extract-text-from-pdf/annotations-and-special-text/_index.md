---
title: Аннотации и специальный текст с использованием Java
linktitle: Аннотации и специальный текст
type: docs
weight: 40
url: /ru/java/annotation-and-special-text/
description: Узнайте, как извлекать текст из аннотаций штампа, выделенного текста, а также содержимого верхнего и нижнего индекса в PDF‑документах с помощью Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Извлеките выделенный текст

Перебрать аннотации страниц и прочитать помечённый текст `HighlightAnnotation`.

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляре.
1. Итерируйте через [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) объекты на целевом [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Проверьте, является ли каждая аннотация [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) перед приведением её к типу класса аннотации.
1. Прочитайте помеченный текст из каждой аннотации выделения и выведите его в консоль.

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

## Извлеките текст из аннотаций штампа

Прочтите поток обычного отображения из аннотации штампа и передайте его дальше `TextAbsorber`.

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляре.
1. Итерируйте через [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) объекты на целевом [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Отфильтруйте аннотации, тип которых `Stamp`.
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) и запросить запись normal appearance entry из словаря appearance аннотации штампа.
1. Посетите appearance [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) и вывести извлечённый текст.

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

## Извлеките сведения о надстрочном и подстрочном тексте

Использовать `TextFragmentAbsorber` когда вам нужны как извлечённый текст, так и флаги верхнего или нижнего индекса для каждого фрагмента.

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляре.
1. Создайте [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) для анализа текста на уровне фрагментов.
1. Посетите цель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и собрать его [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) объекты.
1. Итерируйте эти фрагменты и считывать текст вместе с флагами надстрочного и нижстрочного `fragment.getTextState()`.
1. Запишите извлечённые детали в выходной файл.

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


