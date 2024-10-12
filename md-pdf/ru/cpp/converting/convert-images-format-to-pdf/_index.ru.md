---
title: Преобразование различных форматов изображений в PDF
linktitle: Преобразование изображений в PDF
type: docs
weight: 60
url: /cpp/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Эта тема показывает, как библиотека Aspose.PDF for C++ позволяет конвертировать различные форматы изображений в PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** позволяет конвертировать различные форматы изображений в PDF файлы. Наша библиотека демонстрирует фрагменты кода для конвертации самых популярных форматов изображений, таких как BMP, DICOM, EMF, JPG, PNG, SVG и TIFF.

## Преобразование BMP в PDF

Преобразование файлов BMP в PDF документ с использованием библиотеки **Aspose.PDF for C++**.

<abbr title="Bitmap Image File">BMP</abbr> изображения это файлы с расширением. BMP представляют файлы изображений, используемые для хранения растровых цифровых изображений. Эти изображения независимы от графического адаптера и также называются форматом независимого от устройства растрового изображения (DIB).
Вы можете конвертировать BMP в PDF файлы с помощью API Aspose.PDF for C++. Таким образом, вы можете следовать следующим шагам для преобразования изображений BMP:

1. Создайте [Класс String](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создается экземпляр нового объекта Document.
1. Добавьте новую [Страницу](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) в этот [Документ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Создается новый Aspose.Pdf BMP.
1. Объект Aspose.PDF BMP инициализируется с использованием входного файла.
1. Aspose.PDF BMP добавляется на страницу как абзац.
1. Наконец, сохраните выходной PDF-файл.

Таким образом, следующий фрагмент кода следует этим шагам и показывает, как преобразовать BMP в PDF с использованием C++:

```cpp
void ConvertBMPtoPDF() 
{
    std::clog << "BMP to PDF convert: Start" << std::endl;

    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.bmp");

    // String for input file name
    String outfilename("ImageToPDF-BMP.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);

    std::clog << "BMP to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Попробуйте преобразовать BMP в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["BMP в PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация BMP в PDF с использованием бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Конвертировать DICOM в PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> формат является стандартом медицинской индустрии для создания, хранения, передачи и визуализации цифровых медицинских изображений и документов обследованных пациентов.

**Aspose.PDF for C++** позволяет конвертировать изображения DICOM и SVG, но по техническим причинам для добавления изображений необходимо указать тип файла, который будет добавлен в PDF:

1. Создайте [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Добавьте [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) в коллекцию страниц документа.
1. Aspose.PDF TDicom добавлен на страницу как абзац.
1. Загрузите и [сохраните](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) входной файл изображения.

Следующий фрагмент кода показывает, как конвертировать файлы DICOM в формат PDF с помощью Aspose.PDF. Вам следует загрузить изображение DICOM, разместить изображение на странице в PDF-файле и сохранить результат как PDF.

```cpp
void ConvertDICOMtoPDF()
{
    std::clog << "DICOM to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("CR_Anno.dcm");
    String outfilename("PDFWithDicomImage_out.pdf");

    // Instantiate Document Object
    auto document = MakeObject<Document>();

    // Add a page to pages collection of document
    auto page = document->get_Pages()->Add();

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);
    image->set_FileType(Aspose::Pdf::ImageFileType::Dicom);

    page->get_Paragraphs()->Add(image);

    // Save output as PDF format
    document->Save(_dataDir + outfilename);
    std::clog << "DICOM to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Попробуйте конвертировать DICOM в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация DICOM в PDF с использованием бесплатного приложения](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Конвертация EMF в PDF

<abbr title="Формат расширенного метафайла">EMF</abbr>EMF хранит графические изображения независимо от устройства. Метафайлы EMF состоят из записей переменной длины в хронологическом порядке, которые могут воспроизводить хранимое изображение после анализа на любом выходном устройстве. Более того, вы можете конвертировать EMF в PDF изображение, используя следующие шаги:

1. Создайте [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создается экземпляр нового объекта Document.
1. Добавьте новую страницу в этот [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. 
Новый Aspose.Pdf TIFF создан.
1. Объект Aspose.PDF TIFF инициализируется с использованием входного файла.
1. Aspose.PDF TIFF добавляется на страницу как параграф.
1. Загрузите и [сохраните](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) входной файл изображения.

Кроме того, следующий фрагмент кода показывает, как конвертировать EMF в PDF с помощью C++ в вашем фрагменте кода:

```cpp
void ConvertEMFtoPDF() 
{
    std::clog << "EMF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.emf");
    String outfilename("ImageToPDF_emf.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "EMF to PDF convert: Finish" << std::endl;
}
```
```
{{% alert color="success" %}}
**Попробуйте преобразовать EMF в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование EMF в PDF с использованием бесплатного приложения](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Преобразование JPG в PDF

Нет необходимости задаваться вопросом, как преобразовать JPG в PDF, потому что библиотека **Aspose.PDF для C++** предлагает лучшее решение.

Вы можете очень легко преобразовать изображения JPG в PDF с помощью Aspose.PDF для C++, следуя этим шагам:

1. Создайте [класс String](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создается экземпляр нового объекта Document.
1. Добавьте новую страницу в этот [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Создается новый объект Aspose::Pdf::Image.
1. Объект изображения Aspose.PDF инициализируется с использованием входного файла.
1. Aspose.PDF Image добавляется на страницу как абзац.
1. Загрузите и сохраните входной файл изображения.

Пример кода ниже показывает, как преобразовать JPG изображение в PDF с использованием C++:

```cpp
void ConvertJPEGtoPDF() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.jpg");

    // Строка для имени выходного файла
    String outfilename("ImageToPDF-JPEG.pdf");

    // Открыть документ
    auto document = MakeObject<Document>();

    // Добавить пустую страницу в пустой документ
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Добавить изображение на страницу
    page->get_Paragraphs()->Add(image);

    // Сохранить выходной документ
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

Затем вы можете увидеть, как преобразовать изображение в PDF с **той же высотой и шириной страницы**. Мы будем получать размеры изображения и соответственно задавать размеры страницы PDF-документа с помощью следующих шагов:

1. Загрузить входной файл изображения
1. Получить высоту и ширину изображения
1. Установить высоту, ширину и поля страницы
1. Сохранить выходной PDF-файл

Следующий фрагмент кода показывает, как преобразовать изображение в PDF с одинаковой высотой и шириной страницы, используя C++:

```cpp
void ConvertJPGtoPDF_fitsize() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.jpg");

    // Строка для имени выходного файла
    String outfilename("ImageToPDF-JPG.pdf");

    // Открыть документ
    auto document = MakeObject<Document>();

    // Добавить пустую страницу в пустой документ
    auto page = document->get_Pages()->Add();
    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Добавить изображение на страницу
    page->get_Paragraphs()->Add(image);

    // Установить размеры и поля страницы
    page->get_PageInfo()->set_Height(bitMap->get_Height());
    page->get_PageInfo()->set_Width(bitMap->get_Width());
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_Paragraphs()->Add(image);

    // Сохранить выходной документ
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Попробуйте конвертировать JPG в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация JPG в PDF с помощью бесплатного приложения](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Конвертировать PNG в PDF

**Aspose.PDF для C++** поддерживает функцию конвертации изображений PNG в формат PDF. Ознакомьтесь со следующим примером кода для выполнения вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу растрового формата файлов изображений, который использует без потерь сжатие, что делает его популярным среди пользователей.

Вы можете конвертировать PNG в изображение PDF, используя следующие шаги:

1. Создайте [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создается экземпляр нового объекта Document.
1. Добавьте новую страницу в этот [документ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Создается новый Aspose.Pdf PNG.
1. Объект Aspose.PDF PNG инициализируется с использованием входного файла.
1. Aspose.PDF PNG добавляется на страницу как параграф.
1. Загрузите и сохраните входной файл изображения.

Кроме того, приведенный ниже фрагмент кода показывает, как конвертировать PNG в PDF в ваших C++ приложениях:

```cpp
void ConvertPNGtoPDF() 
{
    std::clog << "PNG to PDF convert: Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.png");

    // Строка для имени выходного файла
    String outfilename("ImageToPDF-PNG.pdf");

    // Открыть документ
    auto document = MakeObject<Document>();

    // Добавить пустую страницу в пустой документ
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Добавить изображение на страницу
    page->get_Paragraphs()->Add(image);

    // Сохранить выходной документ
    document->Save(_dataDir + outfilename);
    std::clog << "PNG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Попробуйте конвертировать PNG в PDF онлайн**

Aspose предлагает вам бесплатное онлайн-приложение ["PNG в PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PNG в PDF с помощью бесплатного приложения](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Конвертировать SVG в PDF

**Aspose.PDF для C++** объясняет, как конвертировать SVG-изображения в формат PDF и как получить размеры исходного файла <abbr title="Scalable Vector Graphics">SVG</abbr>.

Scalable Vector Graphics (SVG) — это семейство спецификаций формата файлов на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

SVG-изображения и их поведение определяются в текстовых файлах XML. Это означает, что они могут быть найдены, индексированы, скриптованы и, при необходимости, сжаты. Как файлы XML, SVG-изображения можно создавать и редактировать с помощью любого текстового редактора, но часто удобнее создавать их с помощью графических программ, таких как Inkscape.

1. Создайте [класс String](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создайте экземпляр класса [`SvgLoadOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options).
1. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) с указанием исходного имени файла и опций.
1. Сохраните документ с нужным именем файла.

Следующий фрагмент кода показывает процесс преобразования файла SVG в формат PDF с использованием Aspose.PDF для C++.

```cpp
void ConvertSVGtoPDF() 
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```
Сonsider an example with advanced features:

```cpp
void ConvertSVGtoPDF_Advanced()
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("Sweden-Royal-flag-grand-coa.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    options->set_AdjustPageSize(true);
    options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }

    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Попробуйте преобразовать формат SVG в PDF онлайн**

Aspose.PDF for C++ предлагает вам бесплатное онлайн-приложение ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Конвертация TIFF в PDF

Формат файла **Aspose.PDF** поддерживается, будь то однофреймное или многофреймное изображение <abbr title="Tag Image File Format">TIFF</abbr>. Это означает, что вы можете конвертировать изображение TIFF в PDF в своих приложениях на C++.

TIFF или TIF, Tagged Image File Format, представляет собой растровые изображения, предназначенные для использования на различных устройствах, соответствующих этому стандарту файлового формата. Изображение TIFF может содержать несколько кадров с различными изображениями. Формат файла Aspose.PDF также поддерживается, будь то однофреймное или многофреймное изображение TIFF. Таким образом, вы можете конвертировать изображение TIFF в PDF в своих приложениях на C++. Поэтому мы рассмотрим пример конвертации многостраничного изображения TIFF в многостраничный документ PDF с помощью следующих шагов:

1. Создайте [Строковый Класс](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создается экземпляр нового объекта Document.
1. Добавьте новую страницу в этот [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Создается новый Aspose.Pdf TIFF.
1. Объект Aspose.PDF TIFF инициализируется с использованием входного файла.
1. Aspose.PDF TIFF добавляется на страницу в качестве абзаца.
1. Загрузите и сохраните входной файл изображения.

Кроме того, следующий фрагмент кода показывает, как преобразовать многостраничное или многокадровое изображение TIFF в PDF с использованием C++:

```cpp
void ConvertTIFFtoPDF() 
{
    std::clog << "TIFF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.tiff");
    String outfilename("ImageToPDF-TIFF.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "TIFF to PDF convert: Finish" << std::endl;
}
```