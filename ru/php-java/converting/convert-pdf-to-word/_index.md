---
title: Конвертировать PDF в Microsoft Word
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: /ru/php-java/convert-pdf-to-word/
lastmod: "2024-05-20"
description: Конвертируйте PDF файл в формат DOC и DOCX с легкостью и полным контролем с Aspose.PDF для PHP. Узнайте больше о том, как настроить конвертацию PDF в документы Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Обзор

Эта статья объясняет, как конвертировать PDF в Word с использованием PHP. Код очень простой, просто загрузите PDF в класс Document и сохраните его в формате Microsoft Word DOC или DOCX. Она охватывает следующие темы

- [PHP PDF в Word](#convert-pdf-to-doc)
- [PHP PDF в DOC](#convert-pdf-to-doc)
- [PHP PDF в DOCX](#convert-pdf-to-docx)
- [PHP Конвертация PDF в Word](#convert-pdf-to-docx)
- [PHP Конвертация PDF в DOC](#convert-pdf-to-doc)
- [PHP Конвертация PDF в DOCX](#convert-pdf-to-docx)
- [PHP Как конвертировать PDF файл в Word DOC](#convert-pdf-to-doc) или [Word DOCX](#convert-pdf-to-docx)

- [PHP Библиотека, API или код для сохранения, генерации или создания Word документов программным образом из PDF](#convert-pdf-to-docx)

## Конвертация PDF в DOC

Одна из самых популярных функций - это преобразование PDF в Microsoft Word DOC, что делает контент легким для редактирования. Aspose.PDF для PHP позволяет конвертировать PDF файлы в DOC.

**Aspose.PDF для PHP** может создавать PDF документы с нуля и является отличным инструментарием для обновления, редактирования и манипулирования существующими PDF документами. Важной функцией является возможность конвертировать страницы и целые PDF документы в изображения. Еще одна популярная функция - это преобразование PDF в Microsoft Word DOC, что делает контент легким для редактирования. (Большинство пользователей не могут редактировать PDF документы, но могут легко работать с таблицами, текстом и изображениями в Microsoft Word.)

Чтобы сделать процесс простым и понятным, Aspose.PDF для PHP предоставляет код из двух строк для преобразования исходного PDF файла в DOC файл.

Следующий фрагмент кода на Java показывает процесс преобразования PDF файла в формат DOC.

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/page/java/com.aspose.page/document) с исходным PDF документом.

2. Сохраните его в формате **SaveFormat.Doc**, вызвав метод **Document.save()**.

```php
// Загрузите PDF документ
$document = new Document($inputFile);

// Создайте новый объект DocSaveOptions
$saveOption = new DocSaveOptions();

// Установите выходной формат в DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// Сохраните документ как DOC
$document->save($outputFile, $saveOption);
```

## Использование класса DocSaveOptions

[Класс DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) предоставляет многочисленные свойства, которые улучшают процесс преобразования PDF файлов в формат DOC. Среди этих свойств, Mode позволяет вам задать режим распознавания для содержимого PDF. Вы можете задать любое значение из перечисления RecognitionMode для этого свойства. Каждое из этих значений имеет определенные преимущества и ограничения:

- Режим [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) быстрый и хорошо сохраняет оригинальный вид PDF файла, но редактируемость полученного документа может быть ограниченной.
 Каждый визуально сгруппированный блок текста в оригинальном PDF преобразуется в текстовое поле в выходном документе. Это достигает максимального сходства с оригиналом, поэтому выходной документ выглядит хорошо, но он полностью состоит из текстовых полей, что может затруднить редактирование в Microsoft Word.

- Поток — это режим полного распознавания, где движок выполняет группировку и многоуровневый анализ, чтобы восстановить оригинальный документ в соответствии с замыслом автора, создавая легко редактируемый документ. Ограничением является то, что выходной документ может выглядеть иначе, чем оригинал.

- Свойство RelativeHorizontalProximity можно использовать для контроля относительной близости между текстовыми элементами, что означает, что расстояние нормируется по размеру шрифта. Более крупные шрифты могут иметь большие расстояния между слогами и по-прежнему считаться единым целым. Оно указывается как процент от размера шрифта, например, 1 = 100%. Это означает, что два символа размером 12pt, расположенные на расстоянии 12 pt, являются близкими.

- RecognitionBullets используется для включения распознавания маркеров во время конверсии.
```php
// Загрузить PDF документ
$document = new Document($inputFile);

// Создать новый объект DocSaveOptions
$saveOption = new DocSaveOptions();

// Установить режим распознавания на EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// Установить формат вывода на DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// Установить режим распознавания как Flow
saveOptions->setMode(DocSaveOptions_RecognitionMode::$Flow);

// Установить горизонтальную близость как 2.5
saveOptions->setRelativeHorizontalProximity(2.5f);

// Включить распознавание маркеров в процессе конверсии
saveOptions->setRecognizeBullets(true);

// Сохранить документ как DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попробовать исследовать функциональность и качество его работы.


[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Конвертация PDF в DOCX

Перечисление DocFormat также предоставляет возможность выбрать DOCX в качестве выходного формата для документов Word. Чтобы отрендерить исходный PDF-файл в формат DOCX, используйте указанный ниже фрагмент кода.

## Как конвертировать PDF в DOCX

Следующий фрагмент кода на Java демонстрирует процесс конвертации PDF-файла в формат DOCX.

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/page/java/com.aspose.page/document) с исходным PDF-документом.
2. Сохраните его в формате **SaveFormat.DocX**, вызвав метод **Document.save()**.

```php
    // Загрузить PDF-документ
    $document = new Document($inputFile);
    
    // Сохранить документ как DOCX
    $document->save($outputFile, SaveFormat::$DocX);
```

Класс [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) имеет свойство с именем Format, которое предоставляет возможность указать формат результирующего документа, то есть DOC или DOCX.
 Для того чтобы конвертировать PDF файл в формат DOCX, пожалуйста, передайте значение Docx из перечисления DocSaveOptions.DocFormat.

Пожалуйста, обратите внимание на следующий фрагмент кода, который предоставляет возможность конвертировать PDF файл в формат DOCX с помощью Java.

```php
// Загрузить PDF документ
$document = new Document($inputFile);

// Создать новый объект DocSaveOptions
$saveOption = new DocSaveOptions();

// Установить режим распознавания на EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// Установить выходной формат на DOCX
$saveOption->setFormat(DocSaveOptions_DocFormat::$DocX);

// Сохранить документ как DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попробовать изучить функциональность и качество его работы.


[![Aspose.PDF Конвертация PDF в DOCX Бесплатное Приложение](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)
{{% /alert %}}