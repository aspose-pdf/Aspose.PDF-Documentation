---
title: Основы Aspose.PDF DOM API
linktitle: Основы DOM API
type: docs
weight: 10
url: /androidjava/basics-of-dom-api/
description: Aspose.PDF для Android через Java также использует идею DOM для представления структуры PDF-документа в терминах объектов. Здесь вы можете прочитать описание этой структуры.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Введение в DOM API

Document Object Model (DOM) — это форма представления структурированных документов в виде объектно-ориентированной модели. DOM является официальным стандартом World Wide Web Consortium (W3C) для представления структурированных документов таким образом, чтобы быть независимым от платформы и языка.

Проще говоря, DOM — это дерево объектов, представляющих структуру некоторого документа.
 Aspose.PDF для Android через Java также использует идею DOM для представления структуры PDF-документа в терминах объектов. Однако аспекты DOM (такие как его элементы) управляются в рамках синтаксиса используемого языка программирования. Публичный интерфейс DOM определен в его интерфейсе прикладного программирования (API).

### Введение в PDF-документ

Portable Document Format (PDF) — это открытый стандарт для обмена документами. PDF-документ представляет собой комбинацию текстовых и двоичных данных. Если вы откроете его в текстовом редакторе, вы увидите необработанные объекты, которые определяют структуру и содержимое документа.

Логическая структура PDF-файла является иерархической и определяет последовательность, в которой приложение просмотра отображает страницы документа и их содержимое. PDF состоит из четырех компонентов: объекты, структура файла, структура документа и потоки содержимого.

### Структура PDF-документа

Поскольку структура PDF-файла является иерархической, Aspose.PDF для Java также получает доступ к элементам аналогичным образом. Следующая иерархия показывает, как PDF-документ логически структурирован и как Aspose.PDF для Java DOM API его строит.

![Структура PDF-документа](https://docs.aspose.com/pdf/java/images/structure.png)

### Доступ к элементам PDF-документа

Объект Document находится на корневом уровне объектной модели. Aspose.PDF для Android через Java DOM API позволяет создать объект Document, а затем получить доступ ко всем остальным объектам в иерархии. Вы можете либо получить доступ к любой из коллекций, таких как Pages, либо к отдельному элементу, такому как Page и т.д. DOM API предоставляет единую точку входа и выхода для управления PDF-документом, как показано ниже:

- Открыть PDF-документ
- Получить доступ к структуре PDF-документа в стиле DOM
- Обновить данные в PDF-документе
- Проверить PDF-документ
- Экспортировать PDF-документ в различные форматы
- Наконец, сохранить обновленный PDF-документ

## Как использовать новый Aspose.PDF для Android через Java API

Эта тема объяснит новый Aspose.PDF для Android через Java API и поможет вам быстро и легко начать работу. Please note that the details regarding the use of the particular features are not the part of this article.

Aspose.PDF для Android через Java состоит из двух частей:

- Aspose.PDF для Android через Java DOM API
- Aspose.PDF.Facades

Вы найдете подробности каждой из этих областей ниже.

### Aspose.PDF для Android через Java DOM API

Новый Aspose.PDF для Android через Java DOM API соответствует структуре PDF-документа, что помогает вам работать с PDF-документами не только на уровне файла и документа, но и на уровне объектов. Мы предоставили разработчикам больше гибкости для доступа ко всем элементам и объектам PDF-документа. Используя классы Aspose.PDF DOM API, вы можете получить программный доступ к элементам документа и форматированию. Этот новый DOM API состоит из различных пространств имен, как указано ниже:

### com.aspose.pdf

Это пространство имен предоставляет класс Document, который позволяет открывать и сохранять PDF-документ. The License класс также является частью этого пространства имен. Оно также предоставляет классы, связанные со страницами PDF, вложениями и закладками, такие как com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection и com.aspose.pdf.OutlineCollection и т.д.

#### com.aspose.pdf.text

Это пространство имен предоставляет классы, которые помогают работать с текстом и его различными аспектами, например com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment и com.aspose.pdf.TextSegmentCollection и т.д.

#### com.aspose.pdf.TextOptions

Это пространство имен предоставляет классы, которые позволяют устанавливать различные параметры для поиска, редактирования или замены текста, например com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions и com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

Этот пространство имен содержит классы, которые помогают работать с интерактивными функциями PDF-документа, например, работа с документом и другие действия. Это пространство имен содержит такие классы, как com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction и com.aspose.pdf.GoToURIAction и т.д.

#### com.aspose.pdf.Annotation

Аннотации являются частью интерактивных функций PDF-документа. Мы выделили пространство имен для аннотаций. Это пространство имен содержит классы, которые помогают работать с аннотациями, например, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation и com.aspose.pdf.LinkAnnotation и т.д.

#### com.aspose.pdf.Form

Это пространство имен содержит классы, которые помогают работать с PDF-формами и полями форм, например, com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField и com.aspose.pdf.OptionCollection и т.д.

#### com.aspose.pdf.devices 

Мы можем выполнять различные операции с PDF-документами, такие как преобразование PDF-документа в различные форматы изображений.
 Однако такие операции не относятся к объекту Document, и мы не можем расширить класс Document для таких операций. Вот почему мы ввели концепцию устройства в новом API DOM.

##### com.aspose.pdf.facades

Ранее для Aspose.PDF for Java вам был нужен Aspose.PDF.Kit for Java для работы с существующими PDF-файлами. Чтобы выполнить старый код Aspose.PDF.Kit, можно использовать пространство имен com.aspose.pdf.facades.