---
title: Преобразование PDF в документы Microsoft Word на Java
linktitle: Преобразование PDF в Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Преобразование PDF файла в формат DOC и DOCX с легкостью и полным контролем с помощью Aspose.PDF для Java. Узнайте больше о том, как настроить преобразование PDF в документы Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Обзор

Эта статья объясняет, как преобразовать PDF в Word, используя Java. Код очень простой, просто загрузите PDF в класс Document и сохраните его в выходном формате Microsoft Word DOC или DOCX. Она охватывает следующие темы

- [Java PDF в Word](#convert-pdf-to-doc)
- [Java PDF в DOC](#convert-pdf-to-doc)
- [Java PDF в DOCX](#convert-pdf-to-docx)
- [Java Преобразование PDF в Word](#convert-pdf-to-docx)
- [Java Преобразование PDF в DOC](#convert-pdf-to-doc)
- [Java Преобразование PDF в DOCX](#convert-pdf-to-docx)
- [Java Как преобразовать PDF файл в Word DOC](#convert-pdf-to-doc) или [Word DOCX](#convert-pdf-to-docx)

- [Java Библиотека PDF в Word, API или код для сохранения, генерации или создания документов Word программно из PDF](#convert-pdf-to-docx)

## Convert PDF to DOC

Одной из самых популярных функций является преобразование PDF в Microsoft Word DOC, что позволяет легко манипулировать содержимым. Aspose.PDF for Java позволяет конвертировать файлы PDF в DOC.

**Aspose.PDF for Java** может создавать PDF-документы с нуля и является отличным инструментарием для обновления, редактирования и манипуляции существующими PDF-документами. Важной функцией является возможность преобразования страниц и целых PDF-документов в изображения. Еще одна популярная функция — это преобразование PDF в Microsoft Word DOC, что делает содержимое легким для манипуляции. (Большинство пользователей не могут редактировать PDF-документы, но могут легко работать с таблицами, текстом и изображениями в Microsoft Word.)

Чтобы сделать процесс простым и понятным, Aspose.PDF for Java предоставляет код из двух строк для преобразования исходного PDF-файла в файл DOC.

Следующий фрагмент кода на Java демонстрирует процесс преобразования файла PDF в формат DOC.

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/page/java/com.aspose.page/document) с исходным документом PDF.
2. Сохраните его в формате **SaveFormat.Doc**, вызвав метод **Document.save()**.

```java
public static void convertPDFtoWord() {
    // Открыть исходный PDF-документ
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Сохранить файл в формате MS документа
    document.save(DATA_DIR + "PDFToDOC_out.doc", SaveFormat.Doc);
    document.close();
}
```

## Использование класса DocSaveOptions

Класс [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) предоставляет множество свойств, которые улучшают процесс преобразования PDF-файлов в формат DOC. Среди этих свойств, Mode позволяет указать режим распознавания содержимого PDF. Вы можете указать любое значение из перечисления RecognitionMode для этого свойства. Каждое из этих значений имеет свои преимущества и ограничения:

- Режим [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) быстрый и хорош для сохранения оригинального вида PDF-файла, но редактируемость полученного документа может быть ограничена.
 Каждый визуально сгруппированный блок текста в оригинальном PDF преобразуется в текстовое поле в выходном документе. Это достигает максимального сходства с оригиналом, поэтому выходной документ выглядит хорошо, но он состоит полностью из текстовых полей, и это может затруднить редактирование в Microsoft Word.

- Поток — это режим полного распознавания, где движок выполняет группировку и многоуровневый анализ для восстановления оригинального документа в соответствии с намерениями автора, создавая при этом легко редактируемый документ. Ограничение заключается в том, что выходной документ может выглядеть иначе, чем оригинал.

- Свойство RelativeHorizontalProximity может использоваться для управления относительной близостью между текстовыми элементами, что означает, что расстояние нормируется по размеру шрифта. Более крупные шрифты могут иметь большие расстояния между слогами и все равно считаться единым целым. Оно указывается в процентах от размера шрифта, например, 1 = 100%. Это означает, что два символа размером 12pt, которые расположены на расстоянии 12pt друг от друга, считаются близкими.

- RecognitionBullets используется для включения распознавания маркеров во время конверсии.
```java
public static void convertPDFtoWordDocAdvanced() {
    Path pdfFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.pdf");
    Path docFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.doc");
    Document document = new Document(pdfFile.toString());
    DocSaveOptions saveOptions = new DocSaveOptions();

    // Укажите выходной формат как DOC
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    // Установите режим распознавания как Flow
    saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);

    // Установите горизонтальную близость как 2.5
    saveOptions.setRelativeHorizontalProximity(2.5f);

    // Включите значение для распознавания маркеров во время процесса конвертации
    saveOptions.setRecognizeBullets(true);

    document.save(docFile.toString(), saveOptions);
    document.close();
}
```

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в DOC онлайн**

Aspose.PDF для Java представляет вам бесплатное онлайн-приложение ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попробовать исследовать функциональность и качество его работы.

[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Преобразовать PDF в DOCX

Перечисление DocFormat также предоставляет возможность выбрать DOCX в качестве выходного формата для документов Word. Чтобы отобразить исходный PDF-файл в формате DOCX, используйте указанный ниже фрагмент кода.

## Как преобразовать PDF в DOCX

Следующий фрагмент кода на Java показывает процесс преобразования PDF-файла в формат DOCX.

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/page/java/com.aspose.page/document) с исходным PDF-документом.
2. Сохраните его в формате **SaveFormat.DocX**, вызвав метод **Document.save()**.

```java
public static void convertPDFtoWord_DOCX_Format() {
    // Открыть исходный PDF-документ
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Сохранить результирующий DOC-файл
    document.save(DATA_DIR + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    document.close();
}
```

Класс [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) имеет свойство с именем Format, которое предоставляет возможность указать формат результирующего документа, то есть DOC или DOCX.
 Для того чтобы конвертировать PDF файл в формат DOCX, пожалуйста, передайте значение Docx из перечисления DocSaveOptions.DocFormat.

Пожалуйста, посмотрите на следующий фрагмент кода, который предоставляет возможность конвертировать PDF файл в формат DOCX с помощью Java.

```java
public static void convertPDFtoWord_Advanced_DOCX_Format() {
    // Открыть исходный PDF документ
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");

    // Создать объект DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions();
    // Указать выходной формат как DOCX
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    // Установить другие параметры DocSaveOptions
    // ....

    // Сохранить документ в формате docx
    document.save("ConvertToDOCX_out.docx", saveOptions);
    document.close();
}
```

{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF for Java предлагает вам бесплатное онлайн-приложение ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попробовать исследовать функциональность и качество работы.
[![Aspose.PDF Конвертация PDF в DOCX Бесплатное Приложение](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}