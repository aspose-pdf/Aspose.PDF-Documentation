---
title: Преобразование HTML в PDF файл на Java
linktitle: Преобразование HTML в PDF файл
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет преобразовывать форматы HTML и MHTML в PDF файл.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Обзор

Эта статья объясняет, как преобразовывать HTML в PDF с использованием Java. Код очень простой, просто загрузите HTML в класс Document и сохраните его как выходной PDF. Преобразование MHTML в PDF на Java также похоже. Она охватывает следующие темы

- [Java HTML в PDF](#convert-html-to-pdf)
- [Java MHTML в PDF](#convert-mhtml-to-pdf)
- [Java Преобразование HTML в PDF](#convert-html-to-pdf)
- [Java Преобразование MHTML в PDF](#convert-mhtml-to-pdf)
- [Java PDF из HTML](#convert-html-to-pdf)
- [Java PDF из MHTML](#convert-mhtml-to-pdf)
- [Java HTML в PDF Конвертер - Как Преобразовать Веб-страницу в PDF](#convert-html-to-pdf)

- [Java HTML в PDF Библиотека, API или Код для Визуализации, Сохранения, Генерации или Создания PDF Программно из HTML](#convert-html-to-pdf)

## Java HTML to PDF Converter Library

**Aspose.PDF for Java** — это API для работы с PDF, которое позволяет беспрепятственно конвертировать любые существующие HTML-документы в PDF. Процесс конвертации HTML в PDF можно гибко настроить.

## Convert HTML to PDF

Следующий пример кода на Java показывает, как конвертировать HTML-документ в PDF.

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Инициализируйте объект [Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Сохраните выходной PDF-документ, вызвав метод **Document.save(String)**.

```java
// Открыть исходный PDF-документ
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Создать экземпляр объекта HTML SaveOptions
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Сохранить документ
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**Попробуйте конвертировать HTML в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация HTML в PDF с использованием бесплатного приложения](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Расширенная конвертация из HTML в PDF

Движок конвертации HTML имеет несколько опций, которые позволяют нам контролировать процесс конвертации.

### Поддержка медиа-запросов

1. Создайте HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Установите режим печати или экрана.
1. Инициализируйте [объект Document](<https://reference.aspose.com/page/java/com.aspose.page/document>).
1. Сохраните выходной PDF-документ.

Медиа-запросы - это популярная техника для предоставления адаптированного стиля для разных устройств. Мы можем установить тип устройства с помощью свойства [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```java
// Создайте HTML LoadOptions
HtmlLoadOptions options = new HtmlLoadOptions();

// Установите режим печати или экрана
options.setHtmlMediaType(HtmlMediaType.Print);

// Инициализируйте объект документа
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// Сохраните выходной PDF-документ
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```


### Включение (отключение) встраивания шрифтов

1. Добавьте новый Html [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Включите/отключите встраивание шрифтов.
1. Сохраните новый документ.

HTML страницы часто используют шрифты (например, шрифты из локальной папки, Google Fonts и т.д.). Мы также можем контролировать встраивание шрифтов в документ, используя свойство [IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--).

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// Включение/отключение встраивания шрифтов
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### Управление загрузкой внешних ресурсов

Движок конвертации предоставляет механизм, который позволяет контролировать загрузку определенных ресурсов, связанных с HTML-документом.

Класс [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) имеет свойство [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-), с помощью которого мы можем определить поведение загрузчика ресурсов.

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // Создание чистого шаблона ресурса для замены:
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // Возвращаем пустой массив байт в случае сервера i.imgur.com
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // Обработка ресурсов с помощью загрузчика ресурсов по умолчанию
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## Конвертировать MHTML в PDF

{{% alert color="success" %}}
**Попробуйте конвертировать MHTML в PDF онлайн**


Aspose.PDF for Java представляет вашему вниманию бесплатное онлайн-приложение ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конвертация MHTML в PDF с использованием бесплатного приложения](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>, сокращенно от MIME HTML, это формат архива веб-страниц, используемый для объединения ресурсов, которые обычно представлены внешними ссылками (таких как изображения, Flash-анимации, апплеты Java и аудиофайлы), с HTML-кодом в один файл. Содержимое MHTML-файла кодируется так, как если бы это было HTML-сообщение электронной почты, используя MIME-тип multipart/related.

Следующий фрагмент кода показывает, как конвертировать файлы MHTML в формат PDF с использованием Java:

```java
// Создайте экземпляр MhtLoadOptions, чтобы указать параметры загрузки для
// MHTML файла.
MhtLoadOptions options = new MhtLoadOptions();

// Установите путь к MHTML файлу.
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// Загрузите MHTML файл в объект Document.
Document document = new Document(mhtmlFileName, options);

// Сохраните документ как PDF файл.
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// Закройте документ.
document.close();
```