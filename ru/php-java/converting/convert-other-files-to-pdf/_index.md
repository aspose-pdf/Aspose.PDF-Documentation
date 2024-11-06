---
title: Преобразование различных форматов файлов в PDF 
linktitle: Преобразование других форматов файлов в PDF 
type: docs
weight: 80
url: ru/php-java/convert-other-files-to-pdf/
lastmod: "2024-05-20"
description: Эта тема показывает, как Aspose.PDF позволяет преобразовывать другие форматы файлов в PDF документ.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Преобразование EPUB в PDF

**Aspose.PDF for PHP** позволяет легко преобразовать файлы EPUB в формат PDF.

<abbr title="electronic publication">EPUB</abbr> — это бесплатный и открытый стандарт электронной книги от Международного форума цифровых публикаций (IDPF). Файлы имеют расширение .epub. EPUB разработан для контента с возможностью перенастройки, что означает, что EPUB-ридер может оптимизировать текст для конкретного устройства отображения.

Для того чтобы преобразовать файлы EPUB в формат PDF, Aspose.PDF for PHP имеет класс под названием [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions), который используется для загрузки исходного файла EPUB.
 После этого объект передается в качестве аргумента для инициализации объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), поскольку это помогает механизму рендеринга PDF определить формат входного документа.

Следующий фрагмент кода показывает процесс преобразования файла EPUB в формат PDF.

1. Создайте EPUB [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/).
2. Инициализируйте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
3. Сохраните выходной PDF документ.

```php
// Создайте новый экземпляр EpubLoadOptions
$loadOption = new EpubLoadOptions();

// Создайте новый объект Document и загрузите файл EPUB
$document = new Document($inputFile, $loadOption);

// Сохраните документ как PDF файл
$document->save($outputFile);
```

{{% alert color="success" %}}
**Попробуйте конвертировать EPUB в PDF онлайн**

Aspose.PDF for PHP предлагает вам онлайн бесплатное приложение ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), где вы можете исследовать функциональность и качество его работы.
[![Aspose.PDF Конвертация EPUB в PDF с бесплатным приложением](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Конвертация Markdown в PDF

{{% alert color="success" %}}
**Попробуйте конвертировать Markdown в PDF онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), где вы можете исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация Markdown в PDF с бесплатным приложением](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown — это инструмент для конвертации текста в HTML для веб-авторов. Markdown позволяет писать в легкочитаемом и простом текстовом формате, а затем конвертировать его в структурно валидный XHTML (или HTML).

Следующий фрагмент кода показывает, как использовать эту функциональность с Aspose.PDF для PHP:

```php
// Создаем новый экземпляр MdLoadOptions
$loadOption = new MdLoadOptions();

// Создаем новый экземпляр Document и загружаем входной файл Markdown
$document = new Document($inputFile, $loadOption);

// Сохраняем документ как файл PDF
$document->save($outputFile);
```


## Convert PCL to PDF

<abbr title="Printer Command Language">PCL</abbr>  (Printer Command Language) — это язык принтера Hewlett-Packard, разработанный для доступа к стандартным функциям принтера. Уровни PCL с 1 по 5e/5c представляют собой языки, основанные на командах, которые используют управляющие последовательности, обрабатываемые и интерпретируемые в порядке их получения. На уровне потребителя потоки данных PCL генерируются драйвером печати. Вывод PCL также может быть легко сгенерирован пользовательскими приложениями.

{{% alert color="success" %}}
**Попробуйте конвертировать PCL в PDF онлайн**

Aspose.PDF для PHP представляет вам бесплатное онлайн-приложение ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PCL в PDF с бесплатным приложением](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**В настоящее время поддерживаются только PCL5 и более ранние версии.**

|**Наборы команд**|**Поддержка**|**Исключения**|**Описание**|

| :- | :- | :- | :- |
|Команды управления заданиями|+|Режим двусторонней печати|Управление процессом печати: количество копий, выходной лоток, односторонняя/двусторонняя печать, отступы слева и сверху и т.д.|
|Команды управления страницей|+|Команда пропуска перфорации|Указание размера страницы, полей, ориентации страницы, межстрочные и межсимвольные расстояния и т.д.|
|Команды позиционирования курсора|+| |Указание позиции курсора и, следовательно, начала текста, растровых или векторных изображений и деталей.|

|Команды выбора шрифта|+|<p>1. Команда прозрачной печати данных.</p><p>2. Встроенные программные шрифты. В текущей версии вместо создания программного шрифта наша библиотека выбирает подходящий шрифт из существующих "жестких" TrueType шрифтов, установленных на целевой машине. <br>   Пригодность определяется соотношением ширины/высоты. <br>   Эта функция работает только для растровых и TrueType шрифтов и не гарантирует, что текст, напечатанный с программным шрифтом, будет соответствовать тексту в исходном файле. <br>   Поскольку коды символов в программном шрифте могут не совпадать с кодами по умолчанию.</p><p>3. Пользовательские наборы символов.</p>|Позволяет загружать программные (встроенные) шрифты из PCL файла и управлять ими в памяти.|
|Команды растровой графики|+|Только черно-белые|Позволяет загружать растровые изображения из PCL файла в память, указывать параметры растра, <br>такие как ширина, высота, тип сжатия, разрешение и т. д.|
|Команды цвета|+| |Позволяет окрашивать все печатные объекты.|
|Команды печатной модели|+| |Позволяет заполнять текст, растровые изображения и прямоугольные области растровыми предопределенными и пользовательскими шаблонами, указывать режим прозрачности для шаблонов и исходного растрового изображения.|
 <br>Предопределенные шаблоны включают штриховку, перекрестную штриховку и затенение.|
|Команды заполнения прямоугольных областей|+| |Позволяют создавать и заполнять прямоугольные области шаблонами.|
|Команды векторной графики HP-GL/2|+|Команды экранированного вектора (SV), режима прозрачности (TR), прозрачных данных (TD), RO (поворот системы координат), масштабирующие или растровые шрифты (SB), наклон символов (SL) и дополнительное пространство (ES) не реализованы, а команды DV (определение пути переменной текстовой строки) реализованы в бета-версии.|<p>- Позволяют загружать векторные изображения HP-GL/2 из PCL файла в память. Vector image has an origin at the lower-left corner of the printable area, can be scaled, translated, rotated and clipped.

- Векторное изображение имеет начало координат в нижнем левом углу области печати и может быть масштабировано, перемещено, повернуто и обрезано.

- A vector image can contain text, as labels, and geometric figures such as rectangle, circle, ellipse, line, arc, bezier curve and complex figures composed from the simple ones.

- Векторное изображение может содержать текст в виде меток и геометрические фигуры, такие как прямоугольник, круг, эллипс, линия, дуга, кривая Безье и сложные фигуры, составленные из простых.

- Closed figures including letters of labels can be filled with solid fill or vector pattern.

- Замкнутые фигуры, включая буквы меток, могут быть залиты сплошной заливкой или векторным узором.

- The pattern can be hatching, cross-hatch, shading, raster user-defined, PCL hatching or cross-hatch and PCL user-defined. PCL patterns are raster. Labels can be individually rotated, scaled, and directed in four directions: up, down, left and right. Left and Right directions involve one-after-another letter arrangement. Up and Down directions involve one-under-another letter arrangement.

- Узор может быть штриховкой, перекрестной штриховкой, затенением, растровым пользовательским, PCL штриховкой или перекрестной штриховкой и PCL пользовательским. Узоры PCL являются растровыми. Метки могут быть индивидуально повернуты, масштабированы и направлены в четырех направлениях: вверх, вниз, влево и вправо. Направления Влево и Вправо предполагают последовательное расположение букв. Направления Вверх и Вниз предполагают расположение букв друг под другом.

|Macross|―| |Allow loading a sequence of PCL commands into memory and use this sequence many times, for example, to print page header or set one formatting for a set of pages.|

|Macross|―| |Позволяет загружать последовательность команд PCL в память и использовать эту последовательность многократно, например, для печати заголовка страницы или установки одного форматирования для набора страниц.|

|Unicode text|―| |Allow printing non-ASCII characters.|

|Unicode text|―| |Позволяет печатать символы, не относящиеся к ASCII.| Не реализовано из-за отсутствия файлов с образцами <br>Юникод текста|
|PCL6 (PCL-XL)| |Реализовано только в бета-версии из-за отсутствия тестовых файлов. Встроенные шрифты также не поддерживаются. Расширение JetReady не поддерживается, так как невозможно получить спецификацию JetReady.|Двоичный формат файла.|

### Конвертация файла PCL в формат PDF

Для обеспечения конвертации из PCL в PDF, [Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java) имеет класс [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions), который используется для инициализации объекта [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Этот объект затем передаётся в качестве аргумента при инициализации объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) и помогает механизму рендеринга PDF определить формат входного документа.

Следующий фрагмент кода показывает процесс конвертации файла PCL в формат PDF.

```php
// Создайте новый экземпляр PclLoadOptions
$loadOption = new PclLoadOptions();

// Создайте новый экземпляр Document и загрузите файл PCL
$document = new Document($inputFile, $loadOption);

// Сохраните документ как файл PDF
$document->save($outputFile);
```

### Известные проблемы

1. Происхождение текстовых строк и изображений может немного отличаться от таковых в исходном PCL-файле, если направление печати не 0º. То же самое касается векторных изображений, если система координат векторного графика повёрнута (предшествующая команда RO).
2. Происхождение меток на векторных изображениях может отличаться от таковых в исходном PCL-файле, если метки находятся под влиянием последовательности команд: Происхождение метки (LO), Определение пути переменного текста (DV), Абсолютное направление (DI) или Относительное направление (DR).
3. Текст может быть неправильно прочитан, если он должен отображаться с помощью Bitmap или TrueType мягкого (встроенного) шрифта, поскольку в настоящее время эти шрифты поддерживаются только частично (см. исключения в "Таблице поддерживаемых функций"). В этой ситуации текст может быть правильно прочитан только в том случае, если коды символов в мягком шрифте соответствуют стандартным. Стиль прочитанного текста также может отличаться от такового в исходном PCL-файле, так как в заголовке мягкого шрифта не обязательно задавать стиль.

1. Если разобранный PCL файл содержит шрифты Intellifont или Universal soft, будет вызвано исключение, потому что шрифты Intellifont и Universal не поддерживаются.

1. Если разобранный PCL файл содержит макрос-команды, результат разбора будет сильно отличаться от исходного файла, потому что макрос-команды не поддерживаются.

## Конвертация текста в PDF

**Aspose.PDF для PHP** предоставляет возможность конвертировать текстовые файлы в формат PDF. В этой статье мы демонстрируем, как легко и эффективно мы можем конвертировать текстовый файл в PDF, используя Aspose.PDF.

Когда вам нужно конвертировать текстовый файл в PDF, сначала прочтите исходный текстовый файл с помощью некоторого ридера. Мы использовали StringBuilder для чтения содержимого текстового файла. Создайте объект Document и добавьте новую страницу в коллекцию Pages. Создайте новый объект TextFragment и передайте объект StringBuilder в его конструктор. Добавьте новый параграф в коллекцию Paragraphs, используя объект TextFragment и сохраните полученный PDF файл, используя метод Save класса Document.
**Попробуйте конвертировать ТЕКСТ в PDF онлайн**
{{% alert color="success" %}}

Aspose.PDF для PHP представляет вам бесплатное онлайн-приложение ["Текст в PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), где вы можете попробовать изучить функциональность и качество его работы.

[![Конвертация Aspose.PDF ТЕКСТ в PDF с бесплатным приложением](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Преобразование текстового файла в PDF

```php
// Создайте новый объект Document.
$document = new Document();

// Добавьте новую страницу в документ.
$page = $document->getPages()->add();

// Прочитайте содержимое входного текстового файла.
$text = file_get_contents($inputFile);

// Создайте новый объект FontRepository.
$fontRepository = new FontRepository();

// Найдите шрифт "Courier" в репозитории.
$font = $fontRepository->findFont("Courier");

// Создайте новый объект TextFragment с входным текстом.
$textFragment = new TextFragment($text);

// Установите шрифт текстового фрагмента на "Courier".
$textFragment->getTextState()->setFont($font);

// Добавьте текстовый фрагмент на страницу.
$page->getParagraphs()->add($textFragment);

// Сохраните документ в выходной файл.
$document->save($outputFile);
```


## Convert XPS to PDF

**Aspose.PDF for PHP** поддерживает функцию преобразования файлов <abbr title="XML Paper Specification">XPS</abbr> в формат PDF. Ознакомьтесь с этой статьей, чтобы решить ваши задачи.

XPS, XML Paper Specification, — это формат файла Microsoft, используемый для интеграции создания и просмотра документов в Windows. С помощью Aspose.PDF for PHP можно преобразовать файлы XPS в PDF, портативный формат файла от Adobe.

Формат файла в основном представляет собой сжатый XML-файл, который в первую очередь используется для распространения и хранения. Его очень трудно редактировать, и он в основном реализован Microsoft.

Чтобы преобразовать файл XPS в PDF с использованием [Aspose.PDF for PHP](https://products.aspose.com/pdf/php-java), используйте класс [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Это используется для инициализации объекта [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Позже этот объект передается в качестве аргумента при инициализации объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) и помогает движку рендеринга PDF определить формат входного документа.

Следующий фрагмент кода показывает процесс преобразования XPS файла в формат PDF.

```php
// Создайте новый экземпляр класса XpsLoadOptions
$loadOption = new XpsLoadOptions();

// Создайте новый экземпляр класса Document и загрузите XPS файл
$document = new Document($inputFile, $loadOption);

// Сохраните документ как файл PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Попробуйте преобразовать формат XPS в PDF онлайн**

Aspose.PDF for PHP предлагает вам бесплатное онлайн-приложение ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация XPS в PDF с помощью бесплатного приложения](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/){{% /alert %}}

## Конвертация PostScript в PDF

**Aspose.PDF для PHP** поддерживает функции конвертации файлов PostScript в формат PDF. Одна из функций Aspose.PDF заключается в том, что вы можете задать набор папок шрифтов, которые будут использоваться в процессе конвертации.

Для того чтобы конвертировать файл PostScript в формат PDF, Aspose.PDF для PHP предлагает класс [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions), который используется для инициализации объекта LoadOptions. Этот объект затем может быть передан в качестве аргумента в конструктор объекта Document, что поможет PDF Rendering Engine определить формат исходного документа.

Следующий фрагмент кода можно использовать для конвертации файла PostScript в формат PDF:

```php
// Создайте новый объект PsLoadOptions.
$loadOption = new PsLoadOptions();

// Создайте новый объект Document и загрузите входной PS файл.
$document = new Document($inputFile, $loadOption);

// Сохраните документ как файл PDF.
$document->save($outputFile);
```

## Конвертация XML в PDF

Формат XML используется для хранения структурированных данных.
 Существует несколько способов конвертировать <abbr title="Extensible Markup Language">XML</abbr> в PDF в Aspose.PDF.

{{% alert color="success" %}}
**Попробуйте конвертировать XML в PDF онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["XML в PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация XML в PDF с помощью бесплатного приложения](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Рассмотрите вариант использования XML-документа на основе стандарта XSL-FO.

### Конвертация XSL-FO в PDF

Конвертация файлов XSL-FO в PDF может быть реализована с использованием объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) с [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```php
// Установите путь к примерам файлов
$dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
$inputFoFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xslt";
$inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xml";
$outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . 'result-xmlfo-to-pdf.pdf';

// Создайте новый экземпляр класса XslFoLoadOptions и передайте путь к входному файлу XSL-FO
$loadOption = new XslFoLoadOptions($inputFoFile);

// Создайте новый экземпляр класса Document и передайте входной XML-файл и параметры загрузки XSL-FO
$document = new Document($inputFile, $loadOption);

// Сохраните преобразованный PDF-документ по пути выходного файла
$document->save($outputFile);
```

## Convert LaTeX/TeX to PDF

Формат файла LaTeX - это текстовый формат файла с разметкой в производной от TeX семье языков LaTeX, и LaTeX является производным форматом системы TeX. LaTeX (ˈleɪtɛk/ лей-тек или ла-тек) - это система подготовки документов и язык разметки документов. Он широко используется для коммуникации и публикации научных документов в различных областях, включая математику, физику и информатику. Он также играет важную роль в подготовке и публикации книг и статей, содержащих сложные многоязычные материалы, такие как санскрит и арабский, включая критические издания. LaTeX использует программу наборки текста TeX для форматирования своего вывода и сам написан на языке макросов TeX.

**Aspose.PDF для PHP** поддерживает возможность конвертации TeX файлов в формат PDF, и для выполнения этого требования в пакете com.aspose.pdf есть класс с именем [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions), который предоставляет возможности для загрузки файлов LaTeX и рендеринга вывода в формате PDF с использованием класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document).
 Следующий фрагмент кода показывает процесс преобразования файла LaTex в формат PDF.

```php
// Создать новый экземпляр класса LatexLoadOptions
$loadOption = new LatexLoadOptions();

// Создать новый экземпляр класса Document и загрузить файл TeX с использованием TeXLoadOptions
$document = new Document($inputFile, $loadOption);

// Сохранить документ как PDF файл
$document->save($outputFile);
```

{{% alert color="success" %}}
**Попробуйте конвертировать LaTeX/TeX в PDF онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), где вы можете оценить функциональность и качество работы.

[![Aspose.PDF Конвертация LaTeX/TeX в PDF с бесплатным приложением](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}