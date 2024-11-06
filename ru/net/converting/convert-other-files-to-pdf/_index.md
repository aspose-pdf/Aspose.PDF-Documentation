---
title: Конвертация других форматов файлов в PDF в .NET
linktitle: Конвертация других форматов файлов в PDF
type: docs
weight: 80
url: ru/net/convert-other-files-to-pdf/
lastmod: "2021-11-01"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать другие форматы файлов, такие как EPUB, MD, PCL, XPS, PS, XML и LaTeX в документ PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Обзор

Эта статья объясняет, как **конвертировать различные другие типы форматов файлов в PDF с использованием C#**. Она охватывает следующие темы.

Следующий пример кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Формат_: **EPUB**
- [C# EPUB в PDF](#csharp-convert-epub-to-pdf)
- [C# Конвертировать EPUB в PDF](#csharp-convert-epub-to-pdf)
- [C# Как конвертировать файл EPUB в PDF](#csharp-convert-epub-to-pdf)

_Формат_: **Markdown**
- [C# Markdown в PDF](#csharp-convert-markdown-to-pdf)
- [C# Конвертировать Markdown в PDF](#csharp-convert-markdown-to-pdf)
- [C# Как конвертировать файл Markdown в PDF](#csharp-convert-markdown-to-pdf)
- [C# Как конвертировать файл Markdown в PDF](#csharp-convert-markdown-to-pdf)

_Формат_: **MD**
- [C# MD в PDF](#csharp-convert-md-to-pdf)
- [C# Конвертировать MD в PDF](#csharp-convert-md-to-pdf)
- [C# Как конвертировать файл MD в PDF](#csharp-convert-md-to-pdf)

_Формат_: **PCL**
- [C# PCL в PDF](#csharp-convert-pcl-to-pdf)
- [C# Конвертировать PCL в PDF](#csharp-convert-pcl-to-pdf)
- [C# Как конвертировать файл PCL в PDF](#csharp-convert-pcl-to-pdf)

_Формат_: **Text**
- [C# Text в PDF](#csharp-convert-text-to-pdf)
- [C# Конвертировать Text в PDF](#csharp-convert-text-to-pdf)
- [C# Как конвертировать файл Text в PDF](#csharp-convert-text-to-pdf)

_Формат_: **TXT**
- [C# TXT в PDF](#csharp-convert-txt-to-pdf)
- [C# Конвертировать TXT в PDF](#csharp-convert-txt-to-pdf)
- [C# Как конвертировать файл TXT в PDF](#csharp-convert-txt-to-pdf)

_Формат_: **Plain Text**
- [C# Обычный текст в PDF](#csharp-convert-plain-text-to-pdf)
- [C# Конвертировать обычный текст в PDF](#csharp-convert-plain-text-to-pdf)
- [C# Как конвертировать файл обычного текста в PDF](#csharp-convert-plain-text-to-pdf)
- [C# Как конвертировать текстовый файл в PDF](#csharp-convert-plain-text-to-pdf)

_Формат_: **Преформатированный TXT**
- [C# Преформатированный текст в PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# Конвертировать преформатированный текст в PDF](#csharp-convert-pre-formatted-txt-to-pdf)
- [C# Как конвертировать файл преформатированного текста в PDF](#csharp-convert-pre-formatted-txt-to-pdf)

_Формат_: **Пре Текст**
- [C# Пре Текст в PDF](#csharp-convert-pre-text-to-pdf)
- [C# Конвертировать Пре Текст в PDF](#csharp-convert-pre-text-to-pdf)
- [C# Как конвертировать файл Пре Текст в PDF](#csharp-convert-pre-text-to-pdf)

_Формат_: **XPS**
- [C# XPS в PDF](#csharp-convert-xps-to-pdf)
- [C# Конвертировать XPS в PDF](#csharp-convert-xps-to-pdf)
- [C# Как конвертировать файл XPS в PDF](#csharp-convert-xps-to-pdf)

## Конвертация EPUB в PDF

**Aspose.PDF для .NET** позволяет легко конвертировать файлы EPUB в формат PDF.

<abbr title="электронная публикация">EPUB</abbr> (сокращение от электронная публикация) является свободным и открытым стандартом электронных книг от Международного форума по цифровым публикациям (IDPF).
<abbr title="электронная публикация">EPUB</abbr> (сокращение от электронная публикация) является свободным и открытым стандартом электронных книг от Международного форума цифровых публикаций (IDPF).

EPUB также поддерживает контент с фиксированным макетом. Формат предназначен как единый формат, который издатели и конвертационные компании могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook. Версия EPUB 3 также поддерживается Книжной промышленной исследовательской группой (BISG), ведущей ассоциацией книжной торговли для стандартизации лучших практик, исследований, информации и событий для упаковки содержимого.

{{% alert color="success" %}}
**Попробуйте конвертировать EPUB в PDF онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн приложение ["EPUB в PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация EPUB в PDF с помощью бесплатного приложения](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>Шаги:</em> Конвертирование EPUB в PDF на C#</strong></a>
<a name="csharp-convert-epub-to-pdf" id="csharp-convert-epub-to-pdf"><strong><em>Шаги:</em> Конвертация EPUB в PDF на C#</strong></a>

1. Создайте экземпляр класса [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions).
2. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с указанием исходного имени файла и опций.
3. Сохраните документ с желаемым именем файла.

Следующий фрагмент кода показывает, как конвертировать файлы EPUB в формат PDF на C#.

```csharp
public static void ConvertEPUBtoPDF()
{
    EpubLoadOptions option = new EpubLoadOptions();
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```

Вы также можете установить размер страницы для конвертации. Чтобы определить новый размер страницы, используйте объект `SizeF` и передайте его в конструктор [EpubLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/epubloadoptions/constructors/main).

```csharp
public static void ConvertEPUBtoPDFAdv()
{
    EpubLoadOptions option = new EpubLoadOptions(new SizeF(1190, 1684));
    Document pdfDocument= new Document(_dataDir + "WebAssembly.epub", option);
    pdfDocument.Save(_dataDir + "epub_test.pdf");
}
```
## Конвертирование Markdown в PDF

**Эта функция поддерживается начиная с версии 19.6 или выше.**

{{% alert color="success" %}}
**Попробуйте конвертировать Markdown в PDF онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн приложение ["Markdown в PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация Markdown в PDF с помощью бесплатного приложения](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF для .NET предоставляет функциональность создания PDF документа на основе входного файла данных [Markdown](https://daringfireball.net/projects/markdown/syntax). Для конвертации Markdown в PDF необходимо инициализировать [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с использованием [MdLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions).

Следующий фрагмент кода показывает, как использовать эту функциональность с библиотекой Aspose.PDF:

<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>Шаги:</em> Конвертация Markdown в PDF на C#</strong></a> |
<a name="csharp-convert-markdown-to-pdf" id="csharp-convert-markdown-to-pdf"><strong><em>Шаги:</em> Конвертация Markdown в PDF на C#</strong></a> |
<a name="csharp-convert-md-to-pdf" id="csharp-convert-md-to-pdf"><strong><em>Шаги:</em> Конвертация MD в PDF на C#</strong></a>

1. Создайте экземпляр класса [MdLoadOptions ](https://reference.aspose.com/pdf/net/aspose.pdf/mdloadoptions/).
2. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с указанием исходного имени файла и опций.
3. Сохраните документ с желаемым именем файла.

```csharp
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Открыть документ Markdown
Document pdfDocument= new Document(dataDir + "sample.md", new MdLoadOptions());
// Сохранить документ в формате PDF
pdfDocument.Save(dataDir + "MarkdownToPDF.pdf");
```

## Конвертация PCL в PDF

<abbr title="Printer Command Language">PCL</abbr> (язык команд принтера) — это разработанный Hewlett-Packard язык принтера, предназначенный для доступа к стандартным функциям принтера.
<abbr title="Язык команд принтера">PCL</abbr> (Язык команд принтера) — это язык принтеров Hewlett-Packard, разработанный для доступа к стандартным функциям принтера.

{{% alert color="success" %}}
**Попробуйте конвертировать PCL в PDF онлайн**

Aspose.PDF для .NET предлагает вам бесплатное онлайн-приложение ["PCL в PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), где вы можете исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF PCL в PDF с помощью бесплатного приложения](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**В настоящее время поддерживаются только PCL5 и более старые версии**

<table>
    <thead>
        <tr>
            <th>
                Наборы команд
            </th>
            <th>
                Поддержка
            </th>
            <th>
                Исключения
            </th>
            <th>
                Описание
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                Команды управления заданиями

        <tr>
            <td>
                Команды управления заданиями
            </td>
            <td>
                +
            </td>
            <td>
                Режим двусторонней печати
            </td>
            <td>
                Управление процессом печати: количество копий, приемный лоток, односторонняя/двусторонняя печать, смещения слева и сверху и т.д.
            </td>
        </tr>
        <tr>
            <td>
                Команды управления страницами
            </td>
            <td>
                +
            </td>
            <td>
                Команда пропуска перфорации
            </td>
            <td>
                Указание размера страницы, полей, ориентации страницы, межстрочных и межсимвольных расстояний и т.д.
            </td>
        </tr>
        <tr>
            <td>
                Команды позиционирования курсора
            </td>
            <td>
                +
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Указание позиции курсора и, следовательно, начала текста, растровых или векторных изображений и деталей.
            </td>
        </tr>
```

<tr>
    <td>
        Укажите позицию курсора и, следовательно, исходные позиции текста, растровых или векторных изображений и деталей.
    </td>
</tr>
<tr>
    <td>
        Команды выбора шрифта
    </td>
    <td>
        +
    </td>
    <td>
        <ol>
            <li>Команда печати прозрачных данных.</li>
            <li>Встроенные программные шрифты. В текущей версии вместо создания программного шрифта наша библиотека выбирает
                подходящий шрифт из существующих "жестких" шрифтов TrueType, установленных на целевой машине. <br/>
                Подходящесть определяется по соотношению ширины и высоты.<br/>
                Эта функция работает только для шрифтов Bitmap и TrueType и не
                гарантирует, что текст, напечатанный с использованием программного шрифта, будет соответствовать тому, что в исходном файле.<br/>
                Поскольку коды символов в программном шрифте могут не совпадать с умолчательными.
            </li>
            <li>Пользовательские наборы символов.</li>
        </ol>
    </td>
</tr>
```

<tr>
    <td>
        <li>Пользовательские наборы символов.</li>
    </ol>
    </td>
    <td>
        Разрешить загрузку мягких (встроенных) шрифтов из файла PCL и управление ими в памяти.
    </td>
</tr>
<tr>
    <td>
        Команды растровой графики
    </td>
    <td>
        +
    </td>
    <td>
        Только черно-белые
    </td>
    <td>
        Разрешить загрузку растровых изображений из файла PCL в память, указать параметры растра, <br
            > такие как ширина, высота, тип сжатия, разрешение и т.д.
    </td>
</tr>
<tr>
    <td>
        Команды работы с цветом
    </td>
    <td>
        +
    </td>
    <td>
        &nbsp;
    </td>
    <td>
        Разрешить раскраску для всех печатаемых объектов.
    </td>
</tr>
<tr>
    <td>
        Команды модели печати
```

Команды печати модели
+
Разрешить заполнение текста, растровых изображений и прямоугольных областей растровыми предопределенными и пользовательскими узорами, указать режим прозрачности для узоров и исходного растрового изображения. Предопределенные узоры включают штриховку, крестообразную штриховку и теневые узоры.

Команды заполнения прямоугольной области
+
Разрешить создание и заполнение прямоугольных областей узорами.

Команды векторной графики HP-GL/2
+
Команда векторной графики с экранированием (SV), Команда режима прозрачности (TR), Команда прозрачных данных (TD), RO
```

Команды Screened Vector Command (SV), Transparency Mode Command (TR), Transparent Data Command (TD), RO
(Rotate Coordinate System), Scalable or Bitmap Fonts Command (SB), Character Slant Command (SL) и
Extra Space (ES) не реализованы, а команды DV (Define Variable Text Path) реализованы в
бета-версии.
</td>
<td>
Разрешить загрузку векторных изображений HP-GL/2 из файла PCL в память. Векторное изображение имеет начало в нижнем
левом углу печатаемой области, может быть масштабировано, перемещено, повернуто и обрезано. <br>
Векторное изображение может содержать текст, как метки, и геометрические фигуры, такие
как прямоугольник, круг, эллипс, линия, дуга, кривая Безье и сложные фигуры, составленные из простых. <br> Закрытые фигуры, включая буквы меток, могут быть заполнены
сплошной заливкой или векторным узором. <br> Узор может быть
штриховкой, крестообразной штриховкой, теневой заливкой, растровой пользовательской, PCL штриховкой или крестообразной штриховкой и PCL
```

     штриховка, крест-накрест, штриховка, растровый пользовательский, штриховка PCL или крест-накрест и пользовательский PCL.
    Узоры PCL представляют собой растр. Метки могут быть индивидуально вращены, масштабированы и направлены в
    четыре стороны: вверх, вниз, влево и вправо. Направления влево и вправо включают расположение букв одна за другой.
    Направления вверх и вниз включают расположение букв одна под другой.
</td>
</tr>
<tr>
    <td>
        Макросы
    </td>
    <td>
        ―
    </td>
    <td>
        &nbsp;
    </td>
    <td>
        Позволяют загружать последовательность команд PCL в память и использовать эту последовательность много раз, например,
        для печати заголовка страницы или установки одного форматирования для набора страниц.
    </td>
</tr>
<tr>
    <td>
        Текст Unicode
    </td>
    <td>
        ―
    </td>
```

            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Разрешить печать символов, не относящихся к ASCII. Не реализовано из-за отсутствия образцовых файлов с <br> текстом Unicode
            </td>
        </tr>
        <tr>
            <td>
                PCL6 (PCL-XL)
            </td>
            <td>
                &nbsp;
            </td>
            <td>
                Реализовано только в бета-версии из-за недостатка тестовых файлов. Встроенные шрифты также не поддерживаются.<br> Расширение JetReady не поддерживается, поскольку невозможно получить спецификацию JetReady.
            </td>
            <td>
                Бинарный формат файла.
            </td>
        </tr>
    </tbody>
</table>

### Конвертация PCL файла в формат PDF

Для конвертации из PCL в PDF, Aspose.PDF использует класс [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions), который используется для инициализации объекта LoadOptions.
```
Для конвертации из PCL в PDF, Aspose.PDF использует класс [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions), который используется для инициализации объекта LoadOptions.

Следующий фрагмент кода показывает процесс конвертации файла PCL в формат PDF.

<a name="csharp-convert-pcl-to-pdf" id="csharp-convert-pcl-to-pdf"><strong><em>Шаги:</em> Конвертация PCL в PDF на C#</strong></a>

1. Создайте экземпляр класса [PclLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions/).
2. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) с указанием исходного имени файла и опций.
3. Сохраните документ с желаемым именем файла.

```csharp
public static void ConvertPCLtoPDF()
{
    PclLoadOptions options = new PclLoadOptions();
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

Также вы можете отслеживать обнаружение ошибок в процессе конвертации.
Вы также можете отслеживать обнаружение ошибок в процессе конвертации.

```csharp
public static void ConvertPCLtoPDFAvdanced()
{
    PclLoadOptions options = new PclLoadOptions { SupressErrors = true };
    Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
    if (options.Exceptions!=null)
        foreach (var ex in options.Exceptions)
        {
            Console.WriteLine(ex.Message);
        }
    pdfDocument.Save(_dataDir + "pcl_test.pdf");
}
```

### Известные проблемы

1. Исходное положение текстовых строк и изображений может незначительно отличаться от исходного файла PCL, если направление печати не равно 0°. То же относится к векторным изображениям, если система координат векторного графика повернута (предшествует команда RO).
1. Исходное положение меток на векторных изображениях может отличаться от исходного файла PCL, если на метки влияет последовательность команд: Исходное положение метки (LO), Определение переменного текстового пути (DV), Абсолютное направление (DI) или Относительное направление (DR).
1. Если обработанный файл PCL содержит шрифты Intellifont или Universal, будет выброшено исключение, поскольку шрифты Intellifont и Universal не поддерживаются.
1. Если обработанный файл PCL содержит команды макросов, результат обработки сильно отличается от исходного файла, поскольку команды макросов не поддерживаются.

## Конвертация текста в PDF

**Aspose.PDF для .NET** поддерживает функцию конвертации обычного текста и предварительно отформатированного текстового файла в формат PDF.

Конвертация текста в PDF означает добавление фрагментов текста на страницу PDF. Что касается текстовых файлов, мы имеем дело с 2 типами текста: предварительная форматирование (например, 25 строк по 80 символов в каждой) и неформатированный текст (обычный текст). В зависимости от наших потребностей, мы можем контролировать это добавление самостоятельно или доверить его алгоритмам библиотеки.

{{% alert color="success" %}}
**Попробуйте конвертировать TEXT в PDF онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), где вы можете изучить функциональность и качество его работы.
Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["Текст в PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), где вы можете изучить функциональность и качество его работы.

[![Преобразование Aspose.PDF текста в PDF с помощью бесплатного приложения](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Преобразование обычного текстового файла в PDF

В случае с обычным текстовым файлом мы можем использовать следующую технику:

<a name="csharp-convert-text-to-pdf" id="csharp-convert-text-to-pdf"><strong><em>Шаги:</em> Преобразование текста в PDF на C#</strong></a> |
<a name="csharp-convert-txt-to-pdf" id="csharp-convert-txt-to-pdf"><strong><em>Шаги:</em> Преобразование TXT в PDF на C#</strong></a> |
<a name="csharp-convert-plain-text-to-pdf" id="csharp-convert-plain-text-to-pdf"><strong><em>Шаги:</em> Преобразование простого текста в PDF на C#</strong></a>

1. Используйте _TextReader_ для чтения всего текста;
2.
2.
3. Создайте новый объект [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment/) и передайте объект _TextReader_ в его конструктор;
4. Добавьте объект _TextFragment_ как параграф в коллекцию _Paragraphs_. Если объем текста превышает размер страницы, алгоритм библиотеки автоматически добавляет дополнительные страницы;
5. Используйте метод **Save** класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/);

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Чтение исходного текстового файла
TextReader tr = new StreamReader(dataDir + "log.txt");

// Создание экземпляра объекта Document с помощью вызова его пустого конструктора
Document pdfDocument= new Document();

// Добавление новой страницы в коллекцию Pages документа
Page page = pdfDocument.Pages.Add();

// Создание экземпляра TextFragment и передача текста из объекта reader в его конструктор в качестве аргумента
TextFragment text = new TextFragment(tr.ReadToEnd());

// Добавление нового текстового параграфа в коллекцию параграфов и передача объекта TextFragment
page.Paragraphs.Add(text);

// Сохранение результирующего PDF-файла
pdfDocument.Save(dataDir + "TexttoPDF_out.pdf");
```
### Конвертация предварительно отформатированного текстового файла в PDF

Конвертация предварительно отформатированного текста похожа на обработку обычного текста, но требует выполнения дополнительных действий, таких как настройка полей, выбор типа и размера шрифта. Очевидно, что шрифт должен быть моноширинным (например, Courier New).

Следуйте этим шагам для конвертации предварительно отформатированного текста в PDF с помощью C#:

<a name="csharp-convert-pre-text-to-pdf" id="csharp-convert-pre-text-to-pdf"><strong><em>Шаги:</em> Конвертация предварительно отформатированного текста в PDF на C#</strong></a> |
<a name="csharp-convert-pre-formatted-txt-to-pdf" id="csharp-convert-pre-formatted-txt-to-pdf"><strong><em>Шаги:</em> Конвертация предварительно отформатированного TXT в PDF на C#</strong></a>

1. Прочитайте весь текст как массив строк;
2. Создайте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) и добавьте новую страницу в коллекцию [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/pages/);
В данном случае алгоритм библиотеки также добавляет дополнительные страницы, но мы можем контролировать этот процесс самостоятельно.
Следующий пример показывает, как конвертировать предварительно отформатированный текстовый файл (80x25) в PDF-документ формата A4.

```csharp
public static void ConvertPreFormattedTextToPdf()
{
    // Читаем текстовый файл как массив строк
    var lines = System.IO.File.ReadAllLines(_dataDir + "rfc822.txt");

    // Создаем объект Document, вызвав его пустой конструктор
    Document pdfDocument= new Document();

    // Добавляем новую страницу в коллекцию Pages документа
    Page page = pdfDocument.Pages.Add();

    // Устанавливаем левый и правый отступы для лучшего представления
    page.PageInfo.Margin.Left = 20;
    page.PageInfo.Margin.Right = 10;
    page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
    page.PageInfo.DefaultTextState.FontSize = 12;

    foreach (var line in lines)
    {
        // проверяем, содержит ли строка символ "разрыв формы"
        // см. https://en.wikipedia.org/wiki/Page_break
        if (line.StartsWith("\x0c"))
        {
            page = pdfDocument.Pages.Add();
            page.PageInfo.Margin.Left = 20;
            page.PageInfo.Margin.Right = 10;
            page.PageInfo.DefaultTextState.Font = FontRepository.FindFont("Courier New");
            page.PageInfo.DefaultTextState.FontSize = 12;
        }
        else
        {
            // Создаем экземпляр TextFragment и
            // передаем строку в его
            // конструктор в качестве аргумента
            TextFragment text = new TextFragment(line);

            // Добавляем новый текстовый параграф в коллекцию параграфов и передаем объект TextFragment
            page.Paragraphs.Add(text);
        }
    }

    // Сохраняем результирующий PDF-файл
    pdfDocument.Save(_dataDir + "TexttoPDF_out.pdf");
}
```
## Преобразование XPS в PDF

**Aspose.PDF для .NET** поддерживает функцию конвертации файлов <abbr title="XML Paper Specification">XPS</abbr> в формат PDF. Ознакомьтесь с этой статьей, чтобы решить свои задачи.

Тип файла XPS в первую очередь связан с XML Paper Specification от корпорации Microsoft. XML Paper Specification (XPS), ранее известная под кодовым названием Metro и включающая маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в ее операционную систему Windows.

{{% alert color="primary" %}}

Формат файла представляет собой по сути архивированный XML-файл, который в основном используется для распространения и хранения. Его очень трудно редактировать, и он в основном реализован Microsoft.

{{% /alert %}}

Для преобразования XPS в PDF с помощью Aspose.PDF для .NET мы ввели класс с названием [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions), который используется для инициализации объекта [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions).
Для конвертации XPS в PDF с помощью Aspose.PDF для .NET, мы представили класс под названием [XpsLoadOption](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions), который используется для инициализации объекта [LoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions).

{{% alert color="primary" %}}

В обеих системах, XP и Windows 7, вы должны найти предустановленный XPS принтер, если посмотрите в Панель управления, а затем Принтеры. Для создания этих файлов вы можете использовать этот принтер в качестве устройства вывода. В Windows 7 файлы должны открываться с помощью двойного щелчка в XPS просмотрщике. Также вы можете скачать XPS просмотрщик с сайта Microsoft.

{{% /alert %}}

Следующий пример кода показывает процесс конвертации файла XPS в формат PDF на языке C#.

<a name="csharp-convert-xps-to-pdf" id="csharp-convert-xps-to-pdf"><strong><em>Шаги:</em> Конвертация XPS в PDF на C#</strong></a>

1. Создайте экземпляр класса [XpsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xpsloadoptions/).
2.
3. Сохраните документ в формате PDF с желаемым именем файла.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Создайте объект LoadOption с использованием опции загрузки XPS
Aspose.Pdf.LoadOptions options = new XpsLoadOptions();

// Создайте объект документа
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options);

// Сохраните полученный документ PDF
document.Save(dataDir + "XPSToPDF_out.pdf");
```

{{% alert color="success" %}}
**Попробуйте конвертировать формат XPS в PDF онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["XPS в PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация XPS в PDF с помощью бесплатного приложения](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}
## Конвертация PostScript в PDF

**Aspose.PDF для .NET** поддерживает возможность конвертации файлов PostScript в формат PDF. Одной из особенностей Aspose.PDF является возможность установки набора папок шрифтов, которые будут использоваться во время конвертации.

Для конвертации файла PostScript в формат PDF, Aspose.PDF для .NET предлагает класс [PsLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/psloadoptions), который используется для инициализации объекта LoadOptions. Позже этот объект может быть передан в конструктор объекта Document, что поможет движку рендеринга PDF определить формат исходного документа.

Следующий фрагмент кода может быть использован для конвертации файла PostScript в формат PDF с помощью Aspose.PDF для .NET:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string _dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Создание нового экземпляра PsLoadOptions
PsLoadOptions options = new PsLoadOptions();
// Открытие .ps документа с созданными параметрами загрузки
Document pdfDocument = new Document(_dataDir + "input.ps", options);
// Сохранение документа
pdfDocument.Save(dataDir + "PSToPDF.pdf");
```
Кроме того, вы можете задать набор папок со шрифтами, которые будут использоваться во время конвертации:

```csharp
public static void ConvertPostscriptToPDFAvdanced()
{
    PsLoadOptions options = new PsLoadOptions
    {
        FontsFolders = new [] { @"c:\tmp\fonts1", @"c:\tmp\fonts2"}
    };
    Document pdfDocument = new Document(_dataDir + "input.ps", options);
    pdfDocument.Save(_dataDir + "ps_test.pdf");
}
```

## Конвертация XML в PDF

Формат XML используется для хранения структурированных данных. Существует несколько способов конвертации XML в PDF в Aspose.PDF:

1. Преобразуйте любые данные XML в HTML с помощью XSLT и конвертируйте HTML в PDF, как описано ниже
1. Создайте XML-документ с использованием схемы XSD Aspose.PDF
1. Используйте XML-документ на основе стандарта XSL-FO

{{% alert color="success" %}}
**Попробуйте конвертировать XML в PDF онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["XML в PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), где вы можете изучить функциональность и качество его работы.
Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["XML в PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), где вы можете изучить функциональность и качество его работы.

[![Преобразование Aspose.PDF XML в PDF с помощью бесплатного приложения](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}


## Преобразование XSL-FO в PDF

Преобразование файлов XSL-FO в PDF можно реализовать с использованием традиционной техники Aspose.PDF - создайте объект [Document](https://reference.aspose.com/page/net/aspose.page/document) с [XslFoLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/xslfoloadoptions). Но иногда вы можете столкнуться с некорректной структурой файла. В этом случае конвертер XSL-FO позволяет настроить стратегию обработки ошибок. Вы можете выбрать `ThrowExceptionImmediately`, `TryIgnore` или `InvokeCustomHandler`.

```csharp
public static void Convert_XSLFO_to_PDF()
{
    // Создайте объект XslFoLoadOption
    var options = new XslFoLoadOptions(".\\samples\\employees.xslt");
    // Установите стратегию обработки ошибок
    options.ParsingErrorsHandlingType = XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately;
    // Создайте объект Document
    var pdfDocument = new Aspose.Pdf.Document(".\\samples\\employees.xml", options);
    pdfDocument.Save(_dataDir + "data_xml.pdf");
}
```
## Преобразование LaTeX/TeX в PDF

Формат файла LaTeX - это текстовый файл с разметкой в производном LaTeX из семейства языков TeX, и LaTeX является производным форматом системы TeX. LaTeX (ˈleɪtɛk/lay-tek или lah-tek) - это система подготовки документов и язык разметки документов. Он широко используется для коммуникации и публикации научных документов во многих областях, включая математику, физику и информатику. Также он играет важную роль в подготовке и публикации книг и статей, содержащих сложные многоязычные материалы, такие как санскрит и арабский, включая критические издания. LaTeX использует программу вёрстки TeX для форматирования своего вывода и сам написан на макроязыке TeX.

{{% alert color="success" %}}
**Попробуйте преобразовать LaTeX/TeX в PDF онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["LaTex в PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование LaTeX/TeX в PDF с помощью бесплатного приложения](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Aspose.PDF для .NET поддерживает функционал конвертации файлов TeX в формат PDF. Для реализации этой задачи пространство имен Aspose.Pdf содержит класс под названием [LatexLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexloadoptions), который предоставляет возможности загрузки файлов LaTex и вывода результатов в формате PDF с использованием [класса Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
Следующий фрагмент кода демонстрирует процесс конвертации файла LaTex в формат PDF на языке C#.

```csharp
public static void ConvertTeXtoPDF()
{
    // Создаем объект опций загрузки Latex
    TeXLoadOptions options = new TeXLoadOptions();
    // Создаем объект документа
    Aspose.Pdf.Document pdfDocument= new Aspose.Pdf.Document(_dataDir + "samplefile.tex", options);
    // Сохраняем результат в файл PDF
    pdfDocument.Save(_dataDir + "TeXToPDF_out.pdf");
}
```
