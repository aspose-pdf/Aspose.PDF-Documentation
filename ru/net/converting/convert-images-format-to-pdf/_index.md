---
title: Конвертация различных форматов изображений в PDF в .NET
linktitle: Конвертация изображений в PDF
type: docs
weight: 60
url: /ru/net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: Конвертация различных форматов изображений, таких как BMP, CGM, JPEG, DICOM, PNG, TIFF, EMF и SVG в PDF с использованием C# .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Обзор

В этой статье объясняется, как конвертировать различные форматы изображений в PDF с использованием C#. Она охватывает следующие темы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

_Формат_: **BMP**
- [C# BMP в PDF](#csharp-bmp-to-pdf)
- [C# Конвертация BMP в PDF](#csharp-bmp-to-pdf)
- [C# Как конвертировать изображение BMP в PDF](#csharp-bmp-to-pdf)

_Формат_: **CGM**
- [C# CGM в PDF](#csharp-cgm-to-pdf)
- [C# Конвертация CGM в PDF](#csharp-cgm-to-pdf)
- [C# Как конвертировать изображение CGM в PDF](#csharp-cgm-to-pdf)

_Формат_: **DICOM**
- [C# DICOM в PDF](#csharp-dicom-to-pdf)
- [C# Конвертация DICOM в PDF](#csharp-dicom-to-pdf)
- [C# Как конвертировать изображение DICOM в PDF](#csharp-dicom-to-pdf)
- [C# Как конвертировать изображение DICOM в PDF](#csharp-dicom-to-pdf)

_Формат_: **EMF**
- [C# EMF в PDF](#csharp-emf-to-pdf)
- [C# Конвертировать EMF в PDF](#csharp-emf-to-pdf)
- [C# Как конвертировать изображение EMF в PDF](#csharp-emf-to-pdf)

_Формат_: **GIF**
- [C# GIF в PDF](#csharp-gif-to-pdf)
- [C# Конвертировать GIF в PDF](#csharp-gif-to-pdf)
- [C# Как конвертировать изображение GIF в PDF](#csharp-gif-to-pdf)

_Формат_: **JPG**
- [C# JPG в PDF](#csharp-jpg-to-pdf)
- [C# Конвертировать JPG в PDF](#csharp-jpg-to-pdf)
- [C# Как конвертировать изображение JPG в PDF](#csharp-jpg-to-pdf)

_Формат_: **PNG**
- [C# PNG в PDF](#csharp-png-to-pdf)
- [C# Конвертировать PNG в PDF](#csharp-png-to-pdf)
- [C# Как конвертировать изображение PNG в PDF](#csharp-png-to-pdf)

_Формат_: **SVG**
- [C# SVG в PDF](#csharp-svg-to-pdf)
- [C# Конвертировать SVG в PDF](#csharp-svg-to-pdf)
- [C# Как конвертировать изображение SVG в PDF](#csharp-svg-to-pdf)

_Формат_: **TIFF**
- [C# TIFF в PDF](#csharp-tiff-to-pdf)
- [C# Конвертировать TIFF в PDF](#csharp-tiff-to-pdf)
- [C# Как конвертировать изображение TIFF в PDF](#csharp-tiff-to-pdf)
- [C# Как конвертировать изображение TIFF в PDF](#csharp-tiff-to-pdf)

Другие темы, рассматриваемые в этой статье
- [Смотрите также](#see-also)


## C# Конвертация изображений в PDF

**Aspose.PDF для .NET** позволяет конвертировать различные форматы изображений в файлы PDF. Наша библиотека демонстрирует фрагменты кода для конвертации самых популярных форматов изображений, таких как - BMP, CGM, DICOM, EMF, JPG, PNG, SVG и TIFF.

## Конвертация BMP в PDF

Конвертируйте файлы BMP в документ PDF с помощью библиотеки **Aspose.PDF для .NET**.

<abbr title="Bitmap Image File">BMP</abbr> изображения — это файлы с расширением .BMP, представляющие собой файлы формата Bitmap Image, используемые для хранения растровых цифровых изображений. Эти изображения не зависят от графического адаптера и также называются форматом файла независимого от устройства растра (DIB).
Вы можете конвертировать BMP в PDF файлы с помощью API Aspose.PDF для .NET. Следовательно, вы можете следовать следующим шагам для конвертации изображений BMP:

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>Шаги: Конвертация BMP в PDF на C#</strong></a>

1.
1.
2. Загрузите входное изображение **BMP**.
3. В конце сохраните выходной файл PDF.

Таким образом, следующий фрагмент кода следует этим шагам и показывает, как конвертировать BMP в PDF с использованием C#:

```csharp
//Инициализация пустого PDF документа
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Загрузка образца файла изображения BMP
    image.File = dataDir + "Sample.bmp";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Сохранение выходного документа PDF
    pdfDocument.Save(dataDir + "BMPtoPDF.pdf");
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать BMP в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация BMP в PDF с использованием бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Конвертация CGM в PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> — это расширение файла для формата метафайла компьютерной графики, который обычно используется в приложениях компьютерного проектирования (CAD) и графики презентаций.
<abbr title="Формат метафайла компьютерной графики">CGM</abbr> - это расширение файла для формата метафайла компьютерной графики, обычно используемого в приложениях CAD (компьютерное проектирование) и презентационной графике.

Ознакомьтесь со следующим фрагментом кода для конвертации файлов CGM в формат PDF.

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>Шаги: Конвертация CGM в PDF на C#</strong></a>

1. Создайте экземпляр класса [CgmLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/cgmloadoptions).
2. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) с указанием исходного имени файла и опций.
3. Сохраните документ с желаемым именем файла.

```csharp
public static void ConvertCGMtoPDF()
{
    CgmLoadOptions option = new CgmLoadOptions();
    Document pdfDocument= new Document(_dataDir+"corvette.cgm", option);
    pdfDocument.Save(_dataDir+"CGMtoPDF.pdf");
}
```

## Конвертация DICOM в PDF

<abbr title="Цифровая визуализация и коммуникации в медицине">DICOM</abbr> является стандартом медицинской индустрии для создания, хранения, передачи и визуализации цифровых медицинских изображений и документов обследуемых пациентов.
Формат <abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> является стандартом медицинской индустрии для создания, хранения, передачи и визуализации цифровых медицинских изображений и документов обследуемых пациентов.

**Aspsoe.PDF для .NET** позволяет конвертировать изображения DICOM и SVG, но по техническим причинам для добавления изображений необходимо указать тип файла, который будет добавлен в PDF:

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>Шаги: Конвертация DICOM в PDF на C#</strong></a>

1. Создайте объект класса Image.
2. Добавьте изображение в коллекцию Paragraphs страницы.
3. Укажите свойство [FileType](https://reference.aspose.com/pdf/net/aspose.pdf/image/properties/filetype).
4. Укажите путь к файлу или источник.
    - Если изображение находится в месте на жестком диске, укажите местоположение пути с помощью свойства Image.File.
    - Если изображение размещено в MemoryStream, передайте объект, содержащий изображение, в свойство Image.ImageStream.

Следующий фрагмент кода показывает, как конвертировать файлы DICOM в формат PDF с помощью Aspose.PDF.
Следующий фрагмент кода показывает, как конвертировать файлы DICOM в формат PDF с помощью Aspose.PDF.

```csharp
private const string _dataDir = "..\\..\\..\\..\\Samples";
// Конвертация изображений DICOM в PDF с использованием класса Image
public static void ConvertDICOMtoPDF()
{
    // Создание объекта документа
    Document pdfDocument = new Document();

    // Добавление страницы в коллекцию страниц документа
    Page page = pdfDocument.Pages.Add();

    Image image = new Image
    {
        FileType = ImageFileType.Dicom,
        File = System.IO.Path.Combine(_dataDir,"bmode.dcm")
    };
    pdfDocument.Pages[1].Paragraphs.Add(image);
    // Сохранение результата в формате PDF
    pdfDocument.Save(System.IO.Path.Combine(_dataDir,"PDFWithDicomImage_out.pdf"));
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать DICOM в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["DICOM в PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), где вы можете изучить функциональность и качество его работы.
{{% /alert %}}

[![Конвертация DICOM в PDF с помощью бесплатного приложения Aspose.PDF](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
## Конвертация EMF в PDF

<abbr title="Формат улучшенного метафайла">EMF</abbr>EMF хранит графические изображения независимо от устройства. Метафайлы EMF состоят из записей переменной длины в хронологическом порядке, которые могут воспроизводить сохраненное изображение на любом выходном устройстве. Кроме того, вы можете конвертировать EMF в изображение PDF, используя следующие шаги:

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>Шаги: Конвертация EMF в PDF на C#</strong></a>

1. Сначала инициализируйте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Загрузите файл изображения **EMF**.
3. Добавьте загруженное изображение EMF на страницу.
4. Сохраните документ PDF.

Более того, следующий фрагмент кода показывает, как конвертировать EMF в PDF с C# в вашем коде .NET:

```csharp
// Инициализация нового документа PDF
var doc = new Document();

// Укажите путь к входному файлу изображения EMF
var imageFile = dataDir + "drawing.emf";
var page = doc.Pages.Add();
string file = imageFile;
FileStream filestream = new FileStream(file, FileMode.Open, FileAccess.Read);
BinaryReader reader = new BinaryReader(filestream);
long numBytes = new FileInfo(file).Length;
byte[] bytearray = reader.ReadBytes((int)numBytes);
Stream stream = new MemoryStream(bytearray);
var b = new Bitmap(stream);

// Укажите свойства размера страницы
page.PageInfo.Margin.Bottom = 0;
page.PageInfo.Margin.Top = 0;
page.PageInfo.Margin.Left = 0;
page.PageInfo.Margin.Right = 0;
page.PageInfo.Width = b.Width;
page.PageInfo.Height = b.Height;
var image = new Aspose.Pdf.Image();
image.File = imageFile;
page.Paragraphs.Add(image);

// Сохраните выходной документ PDF
doc.Save(dataDir + "EMFtoPDF.pdf");
```
{{% alert color="success" %}}
**Попробуйте конвертировать EMF в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["EMF в PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), где вы можете оценить функциональность и качество его работы.

[![Конвертация Aspose.PDF из EMF в PDF с помощью бесплатного приложения](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Конвертировать GIF в PDF

Конвертируйте файлы GIF в документ PDF с помощью библиотеки **Aspose.PDF для .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> позволяет хранить сжатые данные без потери качества в формате не более 256 цветов. Аппаратно-независимый формат GIF был разработан в 1987 году (GIF87a) компанией CompuServe для передачи растровых изображений по сетям.
Вы можете конвертировать GIF в файлы PDF с помощью API Aspose.PDF для .NET. Следуйте следующим шагам для конвертации изображений GIF:

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>Шаги: Конвертация GIF в PDF на C#</strong></a>

1.
1.
2. Загрузите входное изображение **GIF**.
3. Наконец, сохраните выходной файл PDF.

Таким образом, следующий фрагмент кода следует этим шагам и показывает, как конвертировать BMP в PDF с использованием C#:

```csharp
//Инициализация пустого PDF документа
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Загрузка образца файла изображения GIF
    image.File = dataDir + "Sample.gif";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Сохранение выходного PDF документа
    pdfDocument.Save(dataDir + "GIFtoPDF.pdf");
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать GIF в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация GIF в PDF с использованием бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Конвертировать JPG в PDF

Не нужно задумываться о том, как конвертировать JPG в PDF, потому что библиотека **Apose.PDF для .NET** имеет лучшее решение.
Не нужно задумываться о том, как конвертировать JPG в PDF, потому что библиотека **Apose.PDF для .NET** имеет лучшее решение.

Вы можете очень легко конвертировать изображения JPG в PDF с Aspose.PDF для .NET, следуя шагам:

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>Шаги: Конвертация JPG в PDF на C#</strong></a>

1. Инициализируйте объект класса [Document](https://reference.aspose.com/page/net/aspose.page/document).
2. Добавьте новую страницу в документ PDF.
3. Загрузите **JPG** изображение и добавьте в параграф.
4. Сохраните итоговый PDF.

Приведенный ниже фрагмент кода показывает, как конвертировать изображение JPG в PDF используя C#:

```csharp
// Загрузите входной файл JPG
String path = dataDir + "Aspose.jpg";

// Инициализируйте новый документ PDF
Document doc = new Document();

// Добавьте пустую страницу в пустой документ
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Добавьте изображение на страницу
page.Paragraphs.Add(image);

// Сохраните итоговый файл PDF
doc.Save(dataDir + "ImagetoPDF.pdf");
```

Затем вы можете увидеть, как конвертировать изображение в PDF с **такой же высотой и шириной страницы**.
Тогда вы можете увидеть, как преобразовать изображение в PDF с **той же высотой и шириной страницы**.

1. Загрузите входной файл изображения
1. Получите высоту и ширину изображения
1. Установите высоту, ширину и поля страницы
1. Сохраните выходной файл PDF

Следующий фрагмент кода показывает, как преобразовать изображение в PDF с той же высотой и шириной страницы с использованием C#:

```csharp
// Загрузите входной JPG файл изображения
String path = dataDir + "Aspose.jpg";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);

// Прочитайте высоту входного изображения
int h = srcImage.Height;

// Прочитайте ширину входного изображения
int w = srcImage.Width;

// Инициализируйте новый документ PDF
Document doc = new Document();

// Добавьте пустую страницу
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Установите размеры страницы и поля
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Сохраните выходной файл PDF
doc.Save(dataDir + "ImagetoPDF_HeightWidth.pdf");
```
{{% alert color="success" %}}
**Попробуйте конвертировать JPG в PDF онлайн**

Aspose представляет вам бесплатное онлайн приложение ["JPG в PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация JPG в PDF с помощью бесплатного приложения](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Конвертация PNG в PDF

**Aspose.PDF для .NET** поддерживает функцию конвертации изображений PNG в формат PDF. Ознакомьтесь с приведенным ниже фрагментом кода для выполнения вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу растрового формата файла изображения, который использует безубыточное сжатие, что делает его популярным среди пользователей.

Вы можете конвертировать изображение PNG в PDF, следуя приведенным ниже шагам:

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>Шаги: Конвертация PNG в PDF на C#</strong></a>

1. Загрузите входное изображение **PNG**.
2. Прочитайте значения высоты и ширины.
3.
3.
4. Установите размеры страницы.
5. Сохраните выходной файл.

Кроме того, приведенный ниже фрагмент кода показывает, как конвертировать PNG в PDF с использованием C# в ваших .NET приложениях:

```csharp
// Загрузите входной файл PNG
String path = dataDir + "Aspose.png";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);
int h = srcImage.Height;
int w = srcImage.Width;

// Инициализируйте новый документ
Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// Установите размеры страницы
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// Сохраните выходной PDF
doc.Save(dataDir + "ImagetoPDF.pdf");
```

{{% alert color="success" %}}
**Попробуйте конвертировать PNG в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["PNG в PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), где вы можете изучить функциональность и качество его работы.

Aspose представляет вам бесплатное онлайн-приложение ["PNG в PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), где вы можете изучить функциональность и качество его работы.

[![Конвертация Aspose.PDF PNG в PDF с использованием бесплатного приложения](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Конвертация SVG в PDF

**Aspose.PDF для .NET** объясняет, как конвертировать изображения SVG в формат PDF и как получить размеры исходного файла <abbr title="Масштабируемая векторная графика">SVG</abbr>.

Масштабируемая векторная графика (SVG) — это семейство спецификаций XML-базированного формата файла для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

Изображения SVG и их поведение определяются в текстовых файлах XML.
SVG изображения и их поведение определены в текстовых файлах XML.

{{% alert color="success" %}}
**Попробуйте конвертировать формат SVG в PDF онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн приложение ["SVG в PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), где вы можете исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF SVG в PDF с помощью бесплатного приложения](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Для конвертации файлов SVG в PDF используйте класс под названием [SvgLoadOptions](https://reference.aspose.com/net/pdf/aspose.pdf/svgloadoptions), который используется для инициализации объекта [`LoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions). Затем этот объект передается в качестве аргумента при инициализации объекта Document и помогает движку рендеринга PDF определить формат исходного документа.

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>Шаги: Конвертация SVG в PDF на C#</strong></a>

1.
1.
2. Создайте экземпляр класса [`Document`](https://reference.aspose.com/pdf/net/aspose.pdf/document) с указанием имени исходного файла и опций.
3. Сохраните документ с желаемым именем файла.

Следующий фрагмент кода показывает процесс конвертации SVG файла в формат PDF с использованием Aspose.PDF для .NET.

```csharp
public static void ConvertSVGtoPDF()
{
    SvgLoadOptions option = new SvgLoadOptions();
    Document pdfDocument= new Document(_dataDir + "car.svg", option);
    pdfDocument.Save(_dataDir + "svgtest.pdf");
}
```

## Получение размеров SVG

Также возможно получить размеры исходного файла SVG. Эта информация может быть полезной, если мы хотим, чтобы SVG полностью покрывал страницу выходного PDF. Свойство AdjustPageSize класса ScgLoadOption удовлетворяет этому требованию. Значение этого свойства по умолчанию - false. Если значение установлено в true, выходной PDF будет иметь те же размеры (размеры), что и исходный SVG.

Следующий фрагмент кода показывает процесс получения размеров исходного файла SVG и создания файла PDF.
Следующий фрагмент кода показывает процесс получения размеров исходного файла SVG и генерации файла PDF.

```csharp
public static void ConvertSVGtoPDF_Advanced()
{
    // Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Путь к директории с документами.
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var loadopt = new SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    var svgDoc = new Document(dataDir + "GetSVGDimensions.svg", loadopt);
    svgDoc.Pages[1].PageInfo.Margin.Top = 0;
    svgDoc.Pages[1].PageInfo.Margin.Left = 0;
    svgDoc.Pages[1].PageInfo.Margin.Bottom = 0;
    svgDoc.Pages[1].PageInfo.Margin.Right = 0;
    svgDoc.Save(dataDir + "GetSVGDimensions_out.pdf");
}
```

### Поддерживаемые возможности SVG

<table>
    <thead>
        <tr>
            <th>
                <p>Тег SVG</p>
            </th>
            <th>
                <p>Пример использования</p>
            </th>
        </tr>
    </thead>
    <tbody>

<tbody>
    <tr>
        <td>
            <p>круг</p>
        </td>
        <td>
            <code><pre>&lt;circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt;</pre></code>
        </td>
    </tr>
    <tr>
        <td>
            <p>определения</p>
        </td>
        <td>
            <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
                stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
                cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
                &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
                x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
                x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
                x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
        </td>
    </tr>
</tbody>
```

         </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Ссылочные символьные данные&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
text-anchor="middle" &gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Маскированный текст&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;/text&gt;&nbsp; <br
    class="atl-forced-newline"> &lt;use xlink:href="#Text" fill="blue"&nbsp; /&gt;</p>
</td>
</tr>
<tr>
<td>
    <p>эллипс&nbsp;</p>
</td>
<td>
    <p>&lt;ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="red" /&gt;</p>
</td>
</tr>
<tr>
<td>
    <p>g&nbsp;</p>
</td>
<td>
    <p>&lt;g fill="none" stroke="dimgray" stroke-width="1.5" &gt;&nbsp; <br>
        &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7"
        y1="-7" x2="-3" y2="-3"/&gt;&nbsp; <br> &nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
```

<tr>
    <td>
        <p>изображение</p>
    </td>
    <td>
        <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"
            /&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>линия</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
    </td>
</tr>
```

<tr>
    <td>
        <p>линия</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>путь</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>стиль</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>многоугольник</p>
    </td>
    <td>
        <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
            /&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>полилиния</p>
```

<tr>
    <td>
        <p>полилиния</p>
    </td>
    <td>
        <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
            -3,1 -3,-5"/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>прямоугольник&nbsp;</p>
    </td>
    <td>
        <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>svg</p>
    </td>
    <td>
        <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>текст</p>
    </td>
    <td>
        <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
            y="30" pointer-events="none"&gt;Название карты&lt;/text&gt;</p>
    </td>
</tr>
```
## Конвертация TIFF в PDF

**Aspose.PDF** поддерживает формат файла, будь то однокадровое или многокадровое изображение <abbr title="Tag Image File Format">TIFF</abbr>. Это означает, что вы можете конвертировать изображение TIFF в PDF в ваших .NET приложениях.

TIFF или TIF, формат файла с тегированными изображениями, представляет растровые изображения, предназначенные для использования на различных устройствах, соответствующих этому стандарту формата файла.
TIFF или TIF, формат файла с тегами изображения, представляет собой растровые изображения, предназначенные для использования на различных устройствах, соответствующих этому стандарту формата файла.

Вы можете конвертировать TIFF в PDF так же, как и другие растровые форматы графики:

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>Шаги: Конвертация TIFF в PDF на C#</strong></a>

1. Создайте новый объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) и добавьте страницу.
2. Загрузите входное изображение **TIFF**.
3. Сохраните документ PDF.

```csharp
Инициализация пустого документа PDF
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // Загрузка образца файла изображения Tiff
    image.File = dataDir + "sample.tiff";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // Сохранение результирующего документа PDF
    pdfDocument.Save(dataDir + "TIFFtoPDF.pdf");
}
```

В случае, если вам нужно конвертировать многостраничное изображение TIFF в многостраничный документ PDF и управлять некоторыми параметрами, например,
Если вам нужно конвертировать многостраничное изображение TIFF в многостраничный документ PDF и управлять некоторыми параметрами, например:

1. Создайте экземпляр класса Document
1. Загрузите входное изображение TIFF
1. Получите FrameDimension кадров
1. Добавьте новую страницу для каждого кадра
1. Наконец, сохраните изображения на страницах PDF

Следующий фрагмент кода показывает, как конвертировать многостраничное или многофреймовое изображение TIFF в PDF с использованием C#:

```csharp
public static void TiffToPDF2()
{
    // Инициализация нового Document
    Document pdf = new Document();

    // Загрузка изображения TIFF в поток
    Bitmap bitmap = new Bitmap(File.OpenRead(_dataDir+"multipage.tif"));
    // Конвертация многостраничного или многофреймового TIFF в PDF
    FrameDimension dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
    int frameCount = bitmap.GetFrameCount(dimension);

    // Итерация по каждому кадру
    for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
    {
        Page page = pdf.Pages.Add();

        bitmap.SelectActiveFrame(dimension, frameIdx);

        MemoryStream currentImage = new MemoryStream();
        bitmap.Save(currentImage, ImageFormat.Tiff);

        Aspose.Pdf.Image imageht = new Aspose.Pdf.Image
        {
            ImageStream = currentImage,
            // Применение других опций
            //ImageScale = 0.5
        };
        page.Paragraphs.Add(imageht);
    }

    // Сохранение выходного файла PDF
    pdf.Save(_dataDir + "TifftoPDF.pdf");
}
```
## Применимо к

|**Платформа**|**Поддерживается**|**Комментарии**|
| :- | :- |:- |
|Windows .NET Framework|2.0-4.6| |
|Windows .NET Core |2.0-3.1| |
|.NET 5 Windows| |
|Linux .NET Core|2.0-3.1 | |
|.NET 5 Linux | |

## Смотрите также

Эта статья также охватывает следующие темы. Коды такие же, как указано выше.

_Формат_: **BMP**
- [C# BMP в PDF код](#csharp-bmp-to-pdf)
- [C# BMP в PDF API](#csharp-bmp-to-pdf)
- [C# BMP в PDF программно](#csharp-bmp-to-pdf)
- [C# BMP в PDF библиотека](#csharp-bmp-to-pdf)
- [C# сохранить BMP как PDF](#csharp-bmp-to-pdf)
- [C# генерировать PDF из BMP](#csharp-bmp-to-pdf)
- [C# создать PDF из BMP](#csharp-bmp-to-pdf)
- [C# BMP в PDF конвертер](#csharp-bmp-to-pdf)

_Формат_: **CGM**
- [C# CGM в PDF код](#csharp-cgm-to-pdf)
- [C# CGM в PDF API](#csharp-cgm-to-pdf)
- [C# CGM в PDF программно](#csharp-cgm-to-pdf)
- [C# CGM в PDF библиотека](#csharp-cgm-to-pdf)
- [C# сохранить CGM как PDF](#csharp-cgm-to-pdf)
- [C# генерировать PDF из CGM](#csharp-cgm-to-pdf)
- [C# создать PDF из CGM](#csharp-cgm-to-pdf)
- [C# CGM в PDF конвертер](#csharp-cgm-to-pdf)
- [C# CGM to PDF Converter](#csharp-cgm-to-pdf)

_Формат_: **DICOM**
- [C# DICOM в PDF код](#csharp-dicom-to-pdf)
- [C# DICOM в PDF API](#csharp-dicom-to-pdf)
- [C# DICOM в PDF программно](#csharp-dicom-to-pdf)
- [C# DICOM в PDF библиотека](#csharp-dicom-to-pdf)
- [C# Сохранить DICOM как PDF](#csharp-dicom-to-pdf)
- [C# Создать PDF из DICOM](#csharp-dicom-to-pdf)
- [C# Создать PDF из DICOM](#csharp-dicom-to-pdf)
- [C# Конвертер DICOM в PDF](#csharp-dicom-to-pdf)

_Формат_: **EMF**
- [C# EMF в PDF код](#csharp-emf-to-pdf)
- [C# EMF в PDF API](#csharp-emf-to-pdf)
- [C# EMF в PDF программно](#csharp-emf-to-pdf)
- [C# EMF в PDF библиотека](#csharp-emf-to-pdf)
- [C# Сохранить EMF как PDF](#csharp-emf-to-pdf)
- [C# Создать PDF из EMF](#csharp-emf-to-pdf)
- [C# Создать PDF из EMF](#csharp-emf-to-pdf)
- [C# Конвертер EMF в PDF](#csharp-emf-to-pdf)
