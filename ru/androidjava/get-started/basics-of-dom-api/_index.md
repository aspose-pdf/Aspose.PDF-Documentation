---
title: Основы Aspose.PDF DOM API
linktitle: Основы DOM API
type: docs
weight: 10
url: /ru/androidjava/basics-of-dom-api/
description: Aspose.PDF для Android через Java также использует концепцию DOM для представления структуры PDF‑документа в виде объектов. Здесь вы можете прочитать описание этой структуры.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Введение в DOM API

Document Object Model (DOM) — это форма представления структурированных документов в виде объектно‑ориентированной модели. DOM является официальным стандартом World Wide Web Consortium (W3C) для представления структурированных документов независимо от платформы и языка.

Проще говоря, DOM — это дерево объектов, представляющих структуру какого‑то документа. Aspose.PDF для Android через Java также использует концепцию DOM для представления структуры PDF‑документа в виде объектов. Однако аспекты DOM (например, его Elements) манипулируются в синтаксисе используемого языка программирования. Публичный интерфейс DOM задаётся его программным интерфейсом приложений (API).

### Введение в PDF‑документ

Portable Document Format (PDF) — это открытый стандарт для обмена документами. PDF‑документ представляет собой комбинацию текста и бинарных данных. Если открыть его в текстовом редакторе, вы увидите необработанные объекты, определяющие структуру и содержание документа.

Логическая структура PDF‑файла иерархична и определяет порядок, в котором приложение‑просмотрщик отрисовывает страницы документа и их содержимое. PDF состоит из четырёх компонентов: объектов, структуры файла, структуры документа и потоков содержимого.

### Структура PDF‑документа

Поскольку структура PDF‑файла иерархична, Aspose.PDF for Java также обращается к элементам тем же способом. Ниже представлена иерархия, показывающая, как логически структурирован PDF‑документ и как Aspose.PDF for Java DOM API его конструирует.

![Структура PDF‑документа](https://docs.aspose.com/pdf/java/images/structure.png)

### Доступ к элементам PDF‑документа

Объект Document находится на корневом уровне объектной модели. API DOM для Aspose.PDF for Android через Java позволяет создать объект Document, а затем получить доступ ко всем остальным объектам иерархии. Вы можете обращаться как к коллекциям, например Pages, так и к отдельным элементам, например Page и т.д. API DOM предоставляет единые точки входа и выхода для манипулирования PDF‑документом, как показано ниже:

- Откройте PDF‑документ
- Получите доступ к структуре PDF‑документа в стиле DOM
- Обновите данные в PDF‑документе
- Проверьте PDF‑документ
- Экспортировать PDF‑документ в различные форматы
- Наконец, сохраните обновлённый PDF‑документ

## Как использовать новый Aspose.PDF для Android через Java API

В этой статье будет объяснено новое Aspose.PDF для Android через Java API и дано руководство по быстрому и простому началу работы. Обратите внимание, что детали использования конкретных функций не являются частью этой статьи.

Aspose.PDF для Android через Java состоит из двух частей:

- Aspose.PDF для Android через Java DOM API
- Aspose.PDF.Facades 

Ниже вы найдете детали каждой из этих областей.

### Aspose.PDF для Android через Java DOM API

Новый Aspose.PDF for Android via Java DOM API соответствует структуре PDF‑документа, что помогает работать с PDF‑документами не только на уровне файлов и документов, но и на уровне объектов. Мы предоставили разработчикам большую гибкость доступа ко всем элементам и объектам PDF‑документа. Используя классы Aspose.PDF DOM API, вы можете получить программный доступ к элементам документа и его форматированию. Этот новый DOM API состоит из различных пространств имён, указанных ниже:

### com.aspose.pdf

Это пространство имён предоставляет класс Document, который позволяет открывать и сохранять PDF‑документ. Класс License также является частью этого пространства имён. Оно также предоставляет классы, связанные со страницами PDF, вложениями и закладками, такие как com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection и com.aspose.pdf.OutlineCollection и т.д.

#### com.aspose.pdf.text

Это пространство имён предоставляет классы, которые помогают работать с текстом и его различными аспектами, например com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment и com.aspose.pdf.TextSegmentCollection и т.д.

#### com.aspose.pdf.TextOptions

Это пространство имён предоставляет классы, которые позволяют задавать различные параметры для поиска, редактирования или замены текста, например com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions и com.aspose.pdf.TextSearchOptions.

#### com.aspose.pdf.PdfAction

Это пространство имён содержит классы, которые помогают работать с интерактивными функциями PDF‑документа, например работать с документом и другими действиями. В этом пространстве имён находятся классы, такие как com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction и com.aspose.pdf.GoToURIAction и т.д.

#### com.aspose.pdf.Annotation

Аннотации являются частью интерактивных возможностей PDF‑документа. Мы выделили отдельное пространство имён для анноtaций. Это пространство имён содержит классы, которые помогают работать с аннотациями, например, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation и com.aspose.pdf.LinkAnnotation и т.д.

#### com.aspose.pdf.Form

Это пространство имён содержит классы, которые помогают работать с PDF‑формами и полями форм, например com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField и com.aspose.pdf.OptionCollection и т.д.

#### com.aspose.pdf.devices 

Мы можем выполнять различные операции с PDF‑документами, такие как преобразование PDF‑документа в различные форматы изображений. Однако такие операции не относятся к объекту Document, и мы не можем расширять класс Document для этих операций. Поэтому мы ввели понятие Device в новом API DOM.

##### com.aspose.pdf.facades

До появления Aspose.PDF for Java t.o.o вам нужно было использовать Aspose.PDF.Kit for Java для работы с существующими PDF‑файлами. Чтобы выполнить старый код Aspose.PDF.Kit, можно использовать пространство имен com.aspose.pdf.facades.


