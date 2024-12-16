---
title: Основы Aspose.PDF DOM API
linktitle: Основы DOM API
type: docs
weight: 120
url: /ru/cpp/basics-of-dom-api/
description: Aspose.PDF для C++ также использует идею DOM для представления структуры PDF-документа в виде объектов. Здесь вы можете прочитать описание этой структуры.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Введение в DOM API

Document Object Model (DOM) — это форма представления структурированных документов в виде объектно-ориентированной модели. DOM является официальным стандартом World Wide Web Consortium (W3C) для представления структурированных документов в платформенно и языково-нейтральной форме.

Проще говоря, DOM — это дерево объектов, представляющее структуру некоторого документа. Aspose.PDF для C++ также использует идею DOM для представления структуры PDF-документа в терминах объектов. Однако аспекты DOM (такие как его элементы) манипулируются в рамках синтаксиса используемого языка программирования. Публичный интерфейс DOM определяется в его интерфейсе программирования приложений (API).

### Введение в PDF-документ

Portable Document Format (PDF) — это открытый стандарт для обмена документами. PDF-документ представляет собой комбинацию текстовых и бинарных данных. Если открыть его в текстовом редакторе, можно увидеть необработанные объекты, которые определяют структуру и содержимое документа.

Логическая структура PDF-файла является иерархической и определяет последовательность, в которой приложение просмотра выводит страницы документа и их содержимое. PDF состоит из четырех компонентов: объектов, структуры файла, структуры документа и потоков содержимого.

### Структура PDF-документа

Поскольку структура PDF-файла является иерархической, Aspose.PDF для C++ также получает доступ к элементам таким же образом. Следующая иерархия показывает, как PDF-документ логически структурирован и как Aspose.PDF для C++ DOM API его конструирует.

![Структура PDF-документа](../images/structure.png)

### Доступ к элементам PDF-документа

Объект Document находится на корневом уровне объектной модели. Aspose.PDF для C++ DOM API позволяет создать объект Document и затем получить доступ ко всем другим объектам в иерархии. Вы можете получить доступ либо к любой из коллекций, таких как Pages, либо к отдельному элементу, например, Page и т. д. DOM API предоставляет единую точку входа и выхода для манипулирования PDF-документом, как показано ниже:

- Открыть PDF-документ
- Получить доступ к структуре PDF-документа в стиле DOM
- Обновить данные в PDF-документе
- Проверить PDF-документ
- Экспортировать PDF-документ в различные форматы
- Наконец, сохранить обновленный PDF-документ

## Как использовать новый Aspose.PDF для C++ API

Эта тема объяснит новый Aspose.PDF для C++ API и поможет вам быстро и легко начать работу. Пожалуйста, обратите внимание, что подробности использования конкретных функций не являются частью этой статьи.

Aspose.PDF для C++ состоит из двух частей:

- Aspose.PDF для C++ DOM API
- Aspose.PDF.Facades

Ниже вы найдете подробности каждой из этих областей.

### Aspose.PDF для C++ DOM API

Aspose.PDF для C++ DOM API соответствует структуре PDF документа, что помогает вам работать с PDF документами не только на уровне файлов и документов, но и на уровне объектов. Мы предоставили разработчикам больше гибкости для доступа ко всем элементам и объектам PDF документа. Используя классы Aspose.PDF DOM API, вы можете получить программный доступ к элементам документа и форматированию. Этот новый DOM API состоит из различных пространств имен, как указано ниже:

### Aspose::Pdf Namespace Reference

Это пространство имен предоставляет класс Document, который позволяет открывать и сохранять PDF документ.

#### Aspose::Pdf::Text Namespace Reference

Это пространство имен предоставляет классы, которые помогают работать с текстом и его различными аспектами, например, Font, FontCollection, FontRepository, FontSource, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment и TextSegmentCollection и т.д.
#### Aspose::Pdf::Collections Namespace Reference

Это пространство имен предоставляет класс AsposeHashDictionary.

#### Aspose::Pdf::CommonData Namespace Reference

#### Aspose::Pdf::Diagnostics Namespace Reference

#### Aspose::Pdf::Drawing Namespace Reference

Это пространство имен предоставляет классы: Curve, Circle, Arc, Rectangle, Graph и т.д., для добавления графических элементов в ваш PDF файл.

#### Aspose::Pdf::Engine Namespace Reference

Это пространство имен предоставляет классы Addressing, Interactive, Security, CommonData, IO, Presentation.

#### Aspose::Pdf::GroupProcessor Namespace Reference

Это пространство имен предоставляет классы: ExtractorFactory - представляет фабрику для создания объектов IPdfTypeExtractor, IDocumentPageTextExtractor, IDocumentTextExtractor, IPdfTypeExtractor классы - представляют интерфейс для взаимодействия с экстрактором.

#### Aspose::Pdf::Interchange Namespace Reference

#### Aspose::Pdf::LogicalStructure Namespace Reference

Это пространство имен предоставляет классы: AnnotationElement, AttributeOwnerStandard, CaptionElement, DocumentElement, FormElement, GroupingElement, ILSTextElement, PrivateElement, WarichuWTElement и т.д.

#### Aspose::Pdf::Operators Namespace Reference

Этот namespace предоставляет классы следующих операторов: BasicSetColorAndPatternOperator, BlockTextOperator, SetCharWidthBoundingBox, SetColorStroke, SetHorizontalTextScaling, SetTextRenderingMode, TextShowOperator и т.д.

#### Aspose::Pdf::Optimization Namespace Reference

Этот namespace предоставляет два класса - ImageCompressionOptions и OptimizationOptions.

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

Этот namespace предоставляет два класса: FontEmbeddingOptions - стандарт PDF/A требует, чтобы все шрифты были встроены в документ. Этот класс включает флаги для случаев, когда невозможно встроить какой-либо шрифт, поскольку этот шрифт отсутствует на целевом ПК. ToUnicodeProcessingRules - Этот класс описывает правила, которые могут быть использованы для решения ошибки Adobe Preflight "Текст не может быть сопоставлен с Unicode".

#### Aspose::Pdf::Sanitization Namespace Reference

Этот namespace предоставляет два класса: Details_SanitizationException и IRecovery.

#### Aspose::Pdf::Tagged Namespace Reference

Этот пространственный имен предоставляет классы Details_TaggedException - представляет исключение для содержимого TaggedPDF документа. ITaggedContent - представляет интерфейс для работы с содержимым TaggedPdf документа и TaggedPdfExceptionCode.

#### Aspose::Pdf::Validation Namespace Reference

#### Aspose::Pdf::XfaConverter Namespace Reference

Этот пространственный имен предоставляет класс XfaParserOptions - класс для обработки инкапсуляции связанных данных.

#### Aspose::Pdf::Annotations Namespace Reference

Аннотации являются частью интерактивных функций PDF документа. Мы выделили пространство имен для аннотаций. Это пространство имен содержит классы, которые помогают работать с аннотациями, например, Annotation, AnnotationCollection, CircleAnnotation и LinkAnnotation и т.д.

#### Aspose::Pdf::Forms Namespace Reference

Это пространство имен содержит классы, которые помогают работать с PDF формами и полями форм, например Form, Field, TextBoxField и OptionCollection и т.д.

#### Aspose::Pdf::Devices Namespace Reference

We can perform various operations on the PDF documents such as converting PDF document to various image formats. However, such operations do not belong to the Document object and we cannot extend the Document class for such operations. That's why we have introduced the concept of the Device in the new DOM API.

##### Aspose::Pdf::Facades Namespace Reference

You can use Aspose.PDF.Facades namespace. This Namespace provides classes AutoFiller - представляет класс для получения данных из базы данных или другого источника данных. Bookmark, Form, Stamp, PdfConverter и другие классы.