---
title: Преобразование различных форматов изображений в PDF 
linktitle: Преобразование изображений в PDF
type: docs
weight: 60
url: /php-java/convert-images-format-to-pdf/
lastmod: "2024-05-20"
description: Эта тема покажет вам, как библиотека Aspose.PDF для PHP позволяет преобразовывать различные форматы изображений в PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF для PHP** позволяет вам преобразовывать различные форматы изображений в PDF файлы. Наша библиотека демонстрирует фрагменты кода для преобразования самых популярных форматов изображений, таких как - BMP, CGM, DMF, JPG, PNG, SVG и TIFF.

## Преобразование BMP в PDF

Преобразование файлов BMP в PDF документ с использованием библиотеки **Aspose.PDF для PHP**.

Изображения <abbr title="Bitmap Image File">BMP</abbr> представляют собой файлы с расширением .BMP, представляющие файлы растровых изображений, которые используются для хранения цифровых растровых изображений. Эти изображения не зависят от графического адаптера и также называются форматом файлов независимых от устройства (DIB).
Вы можете преобразовать BMP в PDF с помощью Aspose.PDF для PHP API.
 Таким образом, вы можете выполнить следующие шаги для преобразования изображений BMP:

1. Создайте новый объект Document
1. Добавьте новую страницу в документ
1. Установите поля страницы в 0 (если необходимо)
1. Создайте новый объект Image и установите входной BMP файл
1. Добавьте изображение на страницу
1. Сохраните документ в выходной PDF файл

Таким образом, следующий фрагмент кода выполняет эти шаги и показывает, как конвертировать BMP в PDF, используя PHP:

```php
// Создайте новый объект Document
$document = new Document();

// Добавьте новую страницу в документ
$page = $document->getPages()->add();

// Установите поля страницы в 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Создайте новый объект Image и установите входной BMP файл
$image = new Image();
$image->setFile($inputFile);

// Добавьте изображение на страницу
$page->getParagraphs()->add($image);

// Сохраните документ в выходной PDF файл
$document->save($outputFile);
```

## Конвертация CGM в PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> — это стандарт ISO, который предоставляет формат файла векторной 2D-графики для хранения и извлечения графической информации. CGM — это формат, не зависящий от устройства. CGM — это векторный графический формат, который поддерживает три различных метода кодирования: двоичный (лучший для скорости чтения программ), символьный (создает наименьший размер файла и позволяет быстрее передавать данные) или кодирование в формате cleartext (позволяет пользователям читать и изменять файл с помощью текстового редактора)

Следующий фрагмент кода показывает, как конвертировать файлы CGM в формат PDF с использованием Aspose.PDF для PHP.

1. Создайте экземпляр [CgmLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) для указания определенных параметров загрузки файла CGM.
1. Создайте экземпляр класса [Document](https://reference.aspose.com/page/java/com.aspose.page/Document) с указанием исходного имени файла и параметров.
1. Сохраните документ с желаемым именем файла.

```php
$options = new CgmLoadOptions();

// Создайте объект Document и загрузите файл CGM, используя указанные параметры
$document = new Document($inputFile, $options);

// Сохраните документ как файл PDF
$document->save($outputFile);
```


## Конвертация DICOM в PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> — это стандарт для обработки, хранения, печати и передачи информации в медицинской визуализации. Он включает в себя определение формата файла и протокол сетевой связи.

Aspsoe.PDF для PHP позволяет конвертировать файлы DICOM в формат PDF, ознакомьтесь со следующим фрагментом кода:

1. Создайте новый объект Document
1. Добавьте новую страницу в документ
1. Установите поля страницы на 0 (если необходимо)
1. Создайте новый объект Image и установите входной файл BMP
1. Установите файл DICOM в качестве исходного файла для изображения
1. Установите тип файла изображения на DICOM
1. Добавьте изображение на страницу
1. Сохраните документ в выходной файл PDF

```php
// Создайте новый объект Document
$document = new Document();

// Добавьте новую страницу в документ
$page = $document->getPages()->add();

// Установите поля страницы на 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Создайте новый объект Image
$image = new Image();

// Установите файл DICOM в качестве исходного файла для изображения
$image->setFile($inputFile);

// Установите тип файла изображения на DICOM
$image->setFileType(ImageFileType::$Dicom);

// Добавьте изображение на страницу
$page->getParagraphs()->add($image);

// Сохраните документ как файл PDF
$document->save($outputFile);
```


{{% alert color="success" %}}
**Попробуйте преобразовать DICOM в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), где вы можете ознакомиться с функциональностью и качеством работы.

[![Aspose.PDF Конвертация DICOM в PDF с использованием бесплатного приложения](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Конвертация EMF в PDF

Формат расширенного метафайла (<abbr title="Формат расширенного метафайла">EMF</abbr>) хранит графические изображения независимо от устройства. Метафайлы EMF состоят из записей переменной длины в хронологическом порядке, которые могут воспроизводить сохраненное изображение после разбора на любом выходном устройстве.

У нас есть несколько подходов для конвертации EMF в PDF.

## Использование класса Image

PDF-документ состоит из страниц, и каждая страница содержит один или несколько объектов параграфов. Параграф может быть текстом, изображением, таблицей, плавающим блоком, графиком, заголовком, полем формы или вложением.

Чтобы преобразовать файл изображения в формат PDF, заключите его в параграф.

Возможно преобразовать изображения, находящиеся на физическом расположении на локальном жестком диске, по веб-адресу или в экземпляре Stream.

Чтобы добавить изображение:

1. Создайте объект класса com.aspose.pdf.Image.
1. Добавьте изображение в коллекцию [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) экземпляра страницы.
1. Укажите путь или источник изображения.
    - Если изображение находится в определенном месте на жестком диске, укажите местоположение пути с помощью метода [Image.setFile(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).
    - Если изображение помещено в FileInputStream, передайте объект, содержащий изображение, в метод [Image.setImageStream(…)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Image).

Следующий фрагмент кода показывает, как загрузить объект изображения, установить поля страницы, разместить изображение на странице и сохранить результат в PDF.

```php
$inputFile = "sample.emf";

// Создать новый объект Document
$document = new Document();

// Добавить новую страницу в документ
$page = $document->getPages()->add();

// Установить поля страницы в 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Создать новый объект Image и установить входной файл
$image = new Image();
$image->setFile($inputFile);

// Добавить изображение на страницу
$page->getParagraphs()->add($image);

// Сохранить документ как PDF файл
$document->save($outputFile);
```


## Конвертация JPG в PDF

Не нужно задумываться о том, как конвертировать JPG в PDF, потому что библиотека Apose.PDF для PHP имеет лучшее решение.

Вы можете очень легко конвертировать изображения JPG в PDF с помощью Aspose.PDF для PHP, выполнив следующие шаги:

1. Инициализируйте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Добавьте новую страницу в документ
1. Установите поля страницы в 0
1. Создайте новый объект Image и установите входной файл
1. Сохраните выходной PDF

Приведенный ниже фрагмент кода показывает, как конвертировать изображение JPG в PDF с использованием PHP:

```php
$inputFile = "sample.jpg";

// Создайте новый объект Document
$document = new Document();

// Добавьте новую страницу в документ
$page = $document->getPages()->add();

// Установите поля страницы в 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Создайте новый объект Image и установите входной файл
$image = new Image();
$image->setFile($inputFile);

// Добавьте изображение на страницу
$page->getParagraphs()->add($image);

// Сохраните документ как PDF файл
$document->save($outputFile);
```


{{% alert color="success" %}}
**Попробуйте преобразовать JPG в PDF онлайн**

Aspose представляет вашему вниманию бесплатное онлайн-приложение ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конвертация JPG в PDF с использованием бесплатного приложения](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Преобразование PNG в PDF

**Aspose.PDF для PHP** поддерживает функцию преобразования изображений PNG в формат PDF. Ознакомьтесь с следующим фрагментом кода для выполнения вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу растрового формата файлов изображений, который использует без потерь сжатие, что делает его популярным среди пользователей.

Вы можете преобразовать PNG в изображение PDF, используя следующие шаги:

1. Инициализируйте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Добавьте новую страницу в документ
1. Установите поля страницы в 0
1. Создайте новый объект Image и установите входной файл
1. Сохраните выходной PDF

Кроме того, приведенный ниже фрагмент кода показывает, как преобразовать PNG в PDF в ваших PHP приложениях:

```php
$inputFile = "sample.png";

// Создать новый объект Document
$document = new Document();

// Добавить новую страницу в документ
$page = $document->getPages()->add();

// Установить отступы страницы на 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Создать новый объект Image и установить входной файл
$image = new Image();
$image->setFile($inputFile);

// Добавить изображение на страницу
$page->getParagraphs()->add($image);

// Сохранить документ как PDF файл
$document->save($outputFile);
```

{{% alert color="success" %}}
**Попробуйте преобразовать PNG в PDF онлайн**

Aspose предлагает вам онлайн бесплатное приложение ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Преобразование PNG в PDF с использованием бесплатного приложения](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)

{{% /alert %}}

## Convert SVG to PDF

Scalable Vector Graphics (SVG) — это семейство спецификаций формата файлов на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

Изображения SVG и их поведение определяются в текстовых файлах XML. Это означает, что их можно искать, индексировать, скриптовать и, при необходимости, сжимать. Как XML-файлы, изображения SVG можно создавать и редактировать с помощью любого текстового редактора, но чаще всего их удобнее создавать с помощью программ для рисования, таких как Inkscape.

## How to convert SVG file to PDF format

Чтобы конвертировать файлы SVG в PDF, используйте класс с именем [SvgLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions), который используется для инициализации объекта [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions).
 Позже этот объект передается как аргумент во время инициализации объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) и помогает механизму рендеринга PDF определить входной формат исходного документа.

Следующий фрагмент кода демонстрирует процесс конвертации файла SVG в формат PDF.

```php
// Создать новый объект SvgLoadOptions
$loadOption = new SvgLoadOptions();

// Создать новый объект Document и загрузить файл SVG
$document = new Document($inputFile, $loadOption);

// Сохранить документ как файл PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Попробуйте конвертировать формат SVG в PDF онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), где вы можете попробовать изучить функциональность и качество работы.

[![Конвертация Aspose.PDF SVG в PDF с бесплатным приложением](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Конвертация TIFF в PDF

**Aspose.PDF для PHP** поддерживает формат файла, будь то однофреймовое или многофреймовое изображение <abbr title="Tag Image File Format">TIFF</abbr>. Это означает, что вы можете преобразовать изображение TIFF в PDF в своих Java-приложениях.

TIFF или TIF, Tagged Image File Format, представляет собой растровые изображения, предназначенные для использования на различных устройствах, которые соответствуют этому стандарту файлового формата. Изображение TIFF может содержать несколько кадров с различными изображениями. Формат файла Aspose.PDF также поддерживается, будь то однофреймовое или многофреймовое изображение TIFF. Таким образом, вы можете преобразовать изображение TIFF в PDF в своих Java-приложениях. Поэтому мы рассмотрим пример преобразования многостраничного изображения TIFF в многостраничный PDF-документ с помощью следующих шагов:

1. Создайте новый объект Document
1. Добавьте новую страницу в документ
1. Установите поля страницы равными 0
1. Создайте новый объект Image
1. Установите путь к файлу входного изображения TIFF
1. Добавьте изображение на страницу
1. Сохраните документ в виде PDF-файла

Более того, следующий фрагмент кода показывает, как преобразовать многостраничное или многофреймовое изображение TIFF в PDF:

```php
// Создать новый объект Document
$document = new Document();

// Добавить новую страницу в документ
$page = $document->getPages()->add();

// Установить поля страницы в 0
$page->getPageInfo()->getMargin()->setBottom(0);
$page->getPageInfo()->getMargin()->setTop(0);
$page->getPageInfo()->getMargin()->setRight(0);
$page->getPageInfo()->getMargin()->setLeft(0);

// Создать новый объект Image
$image = new Image();

// Установить путь к входному TIFF изображению
$image->setFile($inputFile);

// Добавить изображение на страницу
$page->getParagraphs()->add($image);

// Сохранить документ как PDF файл
$document->save($outputFile);
```