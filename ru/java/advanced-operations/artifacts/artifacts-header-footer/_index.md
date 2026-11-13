---
title: Добавление верхних и нижних колонтитулов в PDF на Java
linktitle: Добавление колонтитулов
type: docs
weight: 70
url: /ru/java/artifacts-header-footer/
description: Создать стилизованные артефакты заголовка и колонтитула и добавить их на страницы PDF в Java.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление верхних и нижних колонтитулов в PDF на Java
Abstract: Создать стилизованные артефакты заголовка и колонтитула и добавить их на страницы PDF в Java.
---
Артефакты заголовка и нижнего колонтитула представляют собой элементы пагинации, не являющиеся содержимым, обычно используемые для повторяющихся меток, идентификаторов страниц и оформления макета.

## Создание артефакта верхнего колонтитула

Используйте этот помощник, когда вам нужен многократно используемый артефакт заголовка с единообразным оформлением текста и выравниванием.

1. Создайте [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Установите его текст, настройки шрифта и цвет переднего плана.
1. Настройте горизонтальное выравнивание.
1. Верните артефакт.

```java
public static HeaderArtifact createHeaderArtifact(String text) {
    HeaderArtifact artifact = new HeaderArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Создание артефакта нижнего колонтитула

Этот помощник создает переиспользуемый артефакт нижнего колонтитула с тем же шаблоном стилей, что и артефакт заголовка.

1. Создайте [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. Установите его текст, состояние текста и цвет переднего плана.
1. Настройте выравнивание.
1. Верните артефакт.

```java
public static FooterArtifact createFooterArtifact(String text) {
    FooterArtifact artifact = new FooterArtifact();
    artifact.setText(text);
    artifact.getTextState().setFontSize(14);
    artifact.getTextState().setFont(FontRepository.findFont("Arial"));
    artifact.getTextState().setForegroundColor(Color.getNavy());
    artifact.setArtifactHorizontalAlignment(HorizontalAlignment.Center);
    return artifact;
}
```

## Добавление артефакта верхнего колонтитула

Используйте этот пример, когда страница должна отображать повторно используемый артефакт заголовка.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте артефакт верхнего колонтитула с помощью вспомогательного метода.
1. Добавьте артефакт на страницу.
1. Сохраните выходной файл.

```java
public static void addHeaderArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HeaderArtifact header = createHeaderArtifact("Sample Header");
        document.getPages().get_Item(1).getArtifacts().add(header);
        document.save(outputFile.toString());
    }
}
```

## Добавление артефакта нижнего колонтитула

Используйте этот пример, когда страница должна отображать артефакт нижнего колонтитула с переиспользуемым форматированием.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте артефакт нижнего колонтитула с помощью вспомогательного метода.
1. Добавьте артефакт на страницу.
1. Сохраните выходной файл.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## См. также

- [Удаление колонтитулов](/pdf/ru/java/remove-headers-footers/)
- [Работа с PDF-артефактами](/pdf/ru/java/artifacts/)
