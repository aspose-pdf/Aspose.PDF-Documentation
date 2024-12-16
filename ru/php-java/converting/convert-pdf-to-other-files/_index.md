---
title: Конвертировать PDF файл в другие форматы
linktitle: Конвертировать PDF в другие форматы
type: docs
weight: 90
url: /ru/php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать PDF файл в другие форматы файлов.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Конвертировать PDF в EPUB

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF для PHP представляет вам бесплатное онлайн приложение ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в EPUB с помощью бесплатного приложения](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (сокращение от электронная публикация) — это бесплатный и открытый стандарт электронных книг от Международного форума цифровых публикаций (IDPF).
 Файлы имеют расширение .epub. EPUB предназначен для содержимого с возможностью переноса, что означает, что EPUB-ридер может оптимизировать текст для конкретного устройства отображения. EPUB также поддерживает содержимое с фиксированной версткой. Формат предназначен как единый формат, который издатели и конверсионные компании могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

Aspose.PDF для PHP поддерживает функцию конвертации документов PDF в формат EPUB. Aspose.PDF для PHP имеет класс под названием [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions), который может быть использован в качестве второго аргумента к методу [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-), чтобы создать файл EPUB. Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования.

```php
// Создайте новый экземпляр класса Document и загрузите входной PDF файл
$document = new Document($inputFile);

// Создайте новый экземпляр класса EpubSaveOptions
$saveOption = new EpubSaveOptions();

// Сохраните документ в формате EPUB, используя указанные параметры сохранения
$document->save($outputFile, $saveOption);
```

## Convert PDF to LaTeX/TeX

**Aspose.PDF for PHP** поддерживает преобразование PDF в LaTeX/TeX. Формат файла LaTeX — это текстовый формат файла со специальной разметкой, используемый в системе подготовки документов на основе TeX для высококачественной вёрстки.

Чтобы преобразовать PDF-файлы в TeX, Aspose.PDF имеет класс [LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions), который предоставляет метод `setOutDirectoryPath` для сохранения временных изображений в процессе конверсии.

Следующий фрагмент кода показывает процесс преобразования PDF-файлов в формат TEX с использованием Java.

```php
// Создайте новый объект Document и загрузите входной PDF-файл
$document = new Document($inputFile);

// Создайте новый объект LaTeXSaveOptions
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// Сохраните документ как LaTeX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в LaTeX/TeX онлайн**

Aspose.PDF for PHP предлагает вам бесплатное онлайн-приложение ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в LaTeX/TeX с помощью бесплатного приложения](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Конвертировать PDF в Текст

**Aspose.PDF для PHP** поддерживает преобразование всего PDF документа и отдельной страницы в текстовый файл.

### Конвертировать весь PDF документ в текстовый файл

Вы можете конвертировать PDF документ в TXT файл, используя метод Visit класса [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

Следующий фрагмент кода объясняет, как извлечь текст со всех страниц.

```php
// Загрузить PDF документ
$document = new Document($inputFile);

// Создать объект TextAbsorber для извлечения текста из документа
$textAbsorber = new TextAbsorber();

// Извлечь текст из документа
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// Сохранить извлеченный текст в выходной файл
file_put_contents($outputFile, $content);

// Получить размер файла выходного файла
$fileSize = filesize($outputFile);
```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в текст онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Конвертация страницы PDF в текстовый файл

Вы можете конвертировать PDF-документ в TXT-файл с помощью Aspose.PDF для PHP. Вам следует использовать метод Visit класса [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) для выполнения этой задачи.

Следующий фрагмент кода объясняет, как извлечь текст из конкретных страниц.

```php
// Загрузить PDF-документ
$document = new Document($inputFile);

// Создать объект TextAbsorber для извлечения текста из документа
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // Сохранить извлеченный текст в выходной файл
    file_put_contents($outputFile, $content);
}
```


## Convert PDF to XPS

**Aspose.PDF для PHP** предоставляет возможность конвертировать PDF файлы в формат <abbr title="XML Paper Specification">XPS</abbr>. Давайте попробуем использовать представленный фрагмент кода для конвертирования PDF файлов в формат XPS с помощью Java.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XPS онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF PDF в XPS с бесплатным приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Тип файла XPS в первую очередь ассоциируется с XML Paper Specification от Microsoft Corporation. XML Paper Specification (XPS), ранее известный под кодовым названием Metro и охватывающий маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Для конвертации PDF файлов в XPS, Aspose.PDF имеет класс [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions), который используется в качестве второго аргумента в конструкторе Document.save(..) для генерации XPS файла.
 Следующий фрагмент кода показывает процесс преобразования PDF файлов в формат XPS.

```php
// Создать новый объект Document и загрузить входной PDF файл
$document = new Document($inputFile);

// Создать новый объект XpsSaveOptions
$saveOption = new XpsSaveOptions();

// Сохранить документ как XPS, используя указанные параметры сохранения
$document->save($outputFile, $saveOption);
```