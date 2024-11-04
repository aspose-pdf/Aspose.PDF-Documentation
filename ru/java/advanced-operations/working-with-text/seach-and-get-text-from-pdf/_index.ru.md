---
title: Поиск и Извлечение Текста со Страниц PDF Документа
linktitle: Поиск и Извлечение Текста
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: Эта статья объясняет, как использовать различные инструменты для поиска и извлечения текста из PDF документов. Мы можем искать с использованием регулярных выражений на определенных или всех страницах.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Поиск и Извлечение Текста со Всех Страниц PDF Документа

TextFragmentAbsorber позволяет найти текст, соответствующий определенной фразе, на всех страницах PDF документа.

Чтобы искать текст во всем документе, вызовите метод accept() коллекции [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 The [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) метод принимает объект TextFragmentAbsorber в качестве параметра, который возвращает коллекцию объектов TextFragment. Пройдитесь по всем фрагментам, чтобы получить их свойства, например, Text, Position, XIndent, YIndent, FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor и т. д.

Следующий фрагмент кода показывает, как выполнить поиск по всему документу и вывести все совпадения в консоль.

```java
// Открыть документ
Document pdfDocument = new Document("input.pdf");

// Создать объект TextAbsorber для поиска всех экземпляров входной поисковой фразы
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Применить абсорбер ко всем страницам
pdfDocument.getPages().accept(textFragmentAbsorber);

// Извлечь фрагменты текста в коллекцию
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Пройтись по фрагментам
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Текст :- " + textFragment.getText());
    System.out.println("Позиция :- " + textFragment.getPosition());
    System.out.println("Отступ по X :- " + textFragment.getPosition().getXIndent());
    System.out.println("Отступ по Y :- " + textFragment.getPosition().getYIndent());
    System.out.println("Шрифт - Имя :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Шрифт - Доступен :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Шрифт - Встроен - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Шрифт - Подмножество :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Размер шрифта :- " + textFragment.getTextState().getFontSize());
    System.out.println("Цвет переднего плана :- " + textFragment.getTextState().getForegroundColor());
}
```

Для поиска текста на определенной странице и получения связанных с ним свойств укажите индекс страницы:

```java
// Применяем абсорбер для первой страницы документа
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Поиск и получение текстовых сегментов со страниц PDF

Для поиска текстовых сегментов на всех страницах в документе получите объекты TextFragment документа.

TextFragmentAbsorber позволяет находить текст, соответствующий определенной фразе, на всех страницах PDF-документа. Чтобы искать текст во всем документе, вызовите метод [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) коллекции [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection). Метод [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) принимает объект TextFragmentAbsorber в качестве параметра, который возвращает коллекцию объектов TextFragment.

{{% alert color="primary" %}}

Когда коллекция TextFragmentCollection была извлечена из документа, пройдитесь по ней, чтобы получить коллекцию TextSegmentCollection каждого объекта TextFragment.
 После этого вы можете получить свойства отдельного объекта TextSegment.
{{% /alert %}}
Следующий фрагмент кода показывает, как искать текстовые сегменты на всех страницах.

```java
// Открыть документ
Document pdfDocument = new Document("input.pdf");

// Создать объект TextAbsorber для поиска всех экземпляров входной фразы
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Принять абсорбер для первой страницы документа
pdfDocument.getPages().accept(textFragmentAbsorber);

// Получить извлеченные текстовые фрагменты в коллекцию
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Перебрать текстовые фрагменты
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // Перебрать текстовые сегменты
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("Текст :- " + textSegment.getText());
        System.out.println("Позиция :- " + textSegment.getPosition());
        System.out.println("XIndent :- " + textSegment.getPosition().getXIndent());
        System.out.println("YIndent :- " + textSegment.getPosition().getYIndent());
        System.out.println("Шрифт - Имя :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("Шрифт - Доступен :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("Шрифт - Встроенный - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("Шрифт - Подмножество :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("Размер шрифта :- " + textSegment.getTextState().getFontSize());
        System.out.println("Цвет переднего плана :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

Чтобы найти определенный текстовый сегмент и получить связанные с ним свойства, укажите индекс страницы для страницы, которую вы хотите искать:

```java
// Примените абсорбер к первой странице документа.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Поиск и извлечение текста со страниц с использованием регулярного выражения

TextFragmentAbsorber помогает искать и извлекать текст со всех страниц в документе, основываясь на регулярном выражении.

Чтобы найти и извлечь текст из документа:

1. Передайте поисковый термин в виде регулярного выражения в конструктор TextFragmentAbsorber.
2. Установите свойство TextSearchOptions объекта TextFragmentAbsorber.
   Это свойство требует объект TextSearchOptions: передайте true в его конструктор при создании нового объекта.
3. Чтобы извлечь совпадающий текст со всех страниц, вызовите метод [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) коллекции [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection).

   TextFragmentAbsorber возвращает TextFragmentCollection, содержащий все фрагменты, соответствующие критериям, указанным в регулярном выражении.

Следующий фрагмент кода показывает, как искать все страницы в документе и получать текст на основе регулярного выражения.

```java
// Открыть документ
Document pdfDocument = new Document("source.pdf");

// Создать объект TextAbsorber для поиска всех экземпляров входной поисковой фразы
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // например, 1999-2000

// Установить опцию поиска текста для указания использования регулярного выражения
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// Применить абсорбер для первой страницы документа
pdfDocument.getPages().accept(textFragmentAbsorber);

// Получить извлеченные фрагменты текста в коллекцию
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Перебрать фрагменты
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Текст :- " + textFragment.getText());
    System.out.println("Позиция :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Шрифт - Название :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Шрифт - Доступен :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Шрифт - Встроен - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Шрифт - Подмножество :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Размер шрифта :- " + textFragment.getTextState().getFontSize());
    System.out.println("Цвет переднего плана :- " + textFragment.getTextState().getForegroundColor());
}
```


Для поиска текста на определенной странице и получения его свойств укажите индекс страницы:

```java
// Применить абсорбер для первой страницы документа.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

Чтобы искать строку в верхнем или нижнем регистре, можно рассмотреть возможность использования регулярного выражения.

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

Пример:

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```