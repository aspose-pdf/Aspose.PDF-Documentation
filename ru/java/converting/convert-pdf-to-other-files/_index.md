---
title: Преобразование PDF файла в другие форматы
linktitle: Преобразование PDF в другие форматы
type: docs
weight: 90
url: /ru/java/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать PDF файл в другие форматы файлов.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Преобразование PDF в EPUB

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF for Java предлагает вам бесплатное онлайн-приложение ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в EPUB с бесплатным приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (сокращение от электронная публикация) - это бесплатный и открытый стандарт электронной книги от Международного форума цифровых публикаций (IDPF).
 Файлы имеют расширение .epub. EPUB предназначен для контента с возможностью переформатирования, что означает, что EPUB-ридер может оптимизировать текст для конкретного устройства отображения. EPUB также поддерживает контент с фиксированной версткой. Формат предназначен как единый формат, который издатели и центры конверсии могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

Aspose.PDF для Java поддерживает функцию преобразования PDF-документов в формат EPUB. Aspose.PDF для Java имеет класс под названием [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions), который может быть использован в качестве второго аргумента метода [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..), чтобы создать файл EPUB. Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования.

```java
// Загрузить PDF документ
Document document = new Document(DATA_DIR + "PDFToEPUB.pdf");
// Создать экземпляр параметров сохранения Epub
EpubSaveOptions options = new EpubSaveOptions();
// Указать макет для содержимого
options.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
// Сохранить ePUB документ
document.save(DATA_DIR + "PDFToEPUB_out.epub", options);
document.close();
```

## Конвертация PDF в LaTeX/TeX

**Aspose.PDF for Java** поддерживает конвертацию PDF в LaTeX/TeX. Формат файла LaTeX - это текстовый формат с специальной разметкой, используемый в системе подготовки документов на базе TeX для высококачественной вёрстки.

Для конвертации PDF файлов в TeX, Aspose.PDF имеет класс [TeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions), который предоставляет метод `setOutDirectoryPath` для сохранения временных изображений в процессе конвертации.

Следующий фрагмент кода показывает процесс конвертации PDF файлов в формат TEX с помощью Java.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX.pdf").toString();
String texDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX_out.tex").toString();

// Создать объект документа
Document document = new Document(documentFileName);

// Создать экземпляр параметров сохранения LaTex
TeXSaveOptions saveOptions = new TeXSaveOptions();

// Указать директорию вывода
String pathToOutputDirectory = DATA_DIR.toString();

// Установить путь директории вывода для объекта параметров сохранения
saveOptions.setOutDirectoryPath(pathToOutputDirectory);

// Сохранить PDF файл в формате LaTex
document.save(texDocumentFileName, saveOptions);
document.close();
```


{{% alert color="success" %}}
**Попробуйте преобразовать PDF в LaTeX/TeX онлайн**

Aspose.PDF для Java предлагает вам бесплатное онлайн-приложение ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в LaTeX/TeX с помощью бесплатного приложения](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Преобразование PDF в текст

**Aspose.PDF для Java** поддерживает преобразование всего PDF-документа и отдельной страницы в текстовый файл.

### Преобразование всего PDF-документа в текстовый файл

Вы можете преобразовать PDF-документ в TXT-файл, используя метод Visit класса [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

Следующий кодовый фрагмент объясняет, как извлечь текст со всех страниц.

```java
// Открыть документ
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Загрузить PDF-документ
Document document = new Document(pdfFileName);
TextAbsorber ta = new TextAbsorber();
ta.visit(document);
// Сохранить извлеченный текст в текстовый файл
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
```


{{% alert color="success" %}}
**Попробуйте преобразовать PDF в текст онлайн**

Aspose.PDF для Java представляет вашему вниманию бесплатное онлайн-приложение ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Преобразование страницы PDF в текстовый файл

Вы можете преобразовать документ PDF в TXT файл с помощью Aspose.PDF для Java. Вам следует использовать метод Visit класса [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) для решения этой задачи.

Следующий фрагмент кода объясняет, как извлечь текст с конкретных страниц.

```java
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Загрузить PDF документ
Document document = new Document(pdfFileName);

TextAbsorber ta = new TextAbsorber();
int[] pages = new int[] { 1, 3, 4 };

for (int page : pages) {
    ta.visit(document.getPages().get_Item(page));
}

// Сохранить извлеченный текст в текстовый файл
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
document.close();
```


## Convert PDF to XPS

**Aspose.PDF for Java** предоставляет возможность конвертировать PDF файлы в формат <abbr title="XML Paper Specification">XPS</abbr>. Давайте попробуем использовать представленный фрагмент кода для конвертации PDF файлов в формат XPS с помощью Java.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XPS онлайн**

Aspose.PDF for Java предлагает вам онлайн бесплатное приложение ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в XPS с помощью бесплатного приложения](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Тип файла XPS в первую очередь ассоциируется с XML Paper Specification от Microsoft Corporation. XML Paper Specification (XPS), ранее известная под кодовым названием Metro и включающая маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Для конвертации PDF файлов в XPS, Aspose.PDF имеет класс [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions), который используется в качестве второго аргумента конструктора Document.save(..) для генерации XPS файла.
 Следующий фрагмент кода показывает процесс преобразования PDF файлов в формат XPS.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(DATA_DIR.toString(), "sample-res-xps.xps").toString();

// Создать объект Document
Document document = new Document(documentFileName);

// Создать экземпляр опций сохранения XPS
XpsSaveOptions saveOptions = new XpsSaveOptions();

// Сохранить вывод в формате XML
document.save(xpsDocumentFileName, saveOptions);
document.close();
```