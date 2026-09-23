---
title: Управление верхними и нижними колонтитулами PDF с помощью Java
linktitle: Управление верхними и нижними колонтитулами PDF
type: docs
weight: 70
url: /ru/java/artifacts-header-footer/
description: Узнайте, как добавлять и удалять артефакты верхних и нижних колонтитулов в PDF‑документах с использованием Aspose.PDF for Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить, настроить и удалить верхние и нижние колонтитулы PDF с помощью Java
Abstract: В этой статье объясняется, как управлять артефактами верхнего и нижнего колонтитулов в PDF‑документах с использованием Aspose.PDF for Java. Описывается создание переиспользуемых объектов `HeaderArtifact` и `FooterArtifact` с пользовательским состоянием текста и выравниванием, их добавление на страницу и удаление существующих артефактов верхнего и нижнего колонтитулов.
---
Артефакты верхнего и нижнего колонтитулов являются элементами пагинации, не являющимися содержимым, обычно используемыми для повторяющихся меток, идентификаторов страниц и оформления макета.

## Создание артефакта верхнего колонтитула

Используйте этот вспомогательный элемент, когда вам нужен переиспользуемый артефакт верхнего колонтитула с постоянным стилем текста и выравниванием.

1. Создайте [HeaderArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/headerartifact/).
1. Установите его текст, настройки шрифта и цвет переднего плана.
1. Настройте выравнивание по горизонтали и верните артефакт.

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

Этот вспомогательный метод создаёт переиспользуемый артефакт нижнего колонтитула с тем же шаблоном стилизации, что и артефакт верхнего колонтитула.

1. Создайте [FooterArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/footerartifact/).
1. Установите его текст, состояние текста и цвет переднего плана.
1. Настройте выравнивание и верните артефакт.

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

Используйте этот пример, когда страница должна отображать переиспользуемый артефакт верхнего колонтитула.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте артефакт верхнего колонтитула с помощью вспомогательного метода.
1. Добавьте артефакт на страницу и сохраните выходной файл.

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
1. Добавьте артефакт на страницу и сохраните выходной файл.

```java
public static void addFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FooterArtifact footer = createFooterArtifact("Sample Footer");
        document.getPages().get_Item(1).getArtifacts().add(footer);
        document.save(outputFile.toString());
    }
}
```

## Удаление артефактов верхнего и нижнего колонтитулов

Используйте этот подход, когда существующие артефакты верхнего и нижнего колонтитулов должны быть удалены со страницы.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите коллекцию артефактов страницы в обратном порядке.
1. Удалите артефакты пагинации, подтип которых — верхний колонтитул или нижний колонтитул, затем сохраните документ.

```java
public static void deleteHeaderFooterArtifact(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = document.getPages().get_Item(1).getArtifacts().size(); i >= 1; i--) {
            Artifact artifact = document.getPages().get_Item(1).getArtifacts().get_Item(i);
            if (artifact.getType() == Artifact.ArtifactType.Pagination
                    && (artifact.getSubtype() == Artifact.ArtifactSubtype.Header
                    || artifact.getSubtype() == Artifact.ArtifactSubtype.Footer)) {
                document.getPages().get_Item(1).getArtifacts().delete(artifact);
            }
        }

        document.save(outputFile.toString());
    }
}
```


