---
title: Convert PDF to Images formats 
linktitle: Convert PDF to Images
type: docs
weight: 70
url: /ru/cpp/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать PDF в различные форматы изображений. Конвертируйте страницы PDF в изображения PNG, JPEG, BMP с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** использует несколько подходов для преобразования PDF в изображение. Вообще говоря, мы используем два подхода: преобразование с использованием подхода Device и преобразование с использованием SaveOption. Этот раздел покажет вам, как конвертировать PDF-документы в форматы изображений, такие как BMP, JPEG, PNG, TIFF и SVG, используя один из этих подходов.

В библиотеке есть несколько классов, которые позволяют использовать виртуальное устройство для преобразования изображений. DocumentDevice ориентирован на преобразование всего документа, а ImageDevice - для конкретной страницы.

## Преобразование PDF с использованием класса DocumentDevice

**Aspose.PDF for C++** позволяет конвертировать страницы PDF в изображения TIFF.

The [TiffDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) (основанный на DocumentDevice) класс позволяет вам конвертировать страницы PDF в изображения TIFF. Этот класс предоставляет метод с именем [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device#a0790daa96125c5638a645647e9678f0c), который позволяет вам конвертировать все страницы в PDF файле в одно изображение TIFF.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF для C++ представляет вам бесплатное онлайн-приложение ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попробовать исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF PDF в TIFF с бесплатным приложением](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Конвертация страниц PDF в одно изображение TIFF

Aspose.PDF для C++ объясняет, как конвертировать все страницы в PDF файле в одно изображение TIFF:

1. Откройте [Документ](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) с помощью MakeObject.
1. Создайте объект Resolution.
1. Создайте объект [TIffSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_settings/).
1. Создайте [TIff устройство](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) с указанными атрибутами.
1. Преобразуйте конкретную страницу и сохраните изображение в поток.

Следующий фрагмент кода показывает, как преобразовать все страницы PDF в одно изображение TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTIFF()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("PageToTiff.pdf");
    String outfilename("PagesToTIFF_out.tif");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Создайте объект Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Создайте объект TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
    tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
    tiffSettings->set_SkipBlankPages(false);

    // Создайте устройство TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

    // Преобразуйте страницы и сохраните изображение в поток
    tiffDevice->Process(document, 1, 2, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
### Преобразование одной страницы в изображение TIFF

Aspose.PDF for C++ позволяет преобразовать определенную страницу в PDF файле в изображение TIFF, используя перегруженную версию метода Process(..), который принимает номер страницы в качестве аргумента для преобразования. Следующий фрагмент кода показывает, как преобразовать первую страницу PDF в формат TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("PageToTiff.pdf");
    String outfilename("PageToTiff_out.tif");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Создать объект разрешения
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Создать устройство TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

    // Преобразовать определенную страницу и сохранить изображение в поток
    tiffDevice->Process(document, 1, 1, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Используйте алгоритм Бредли при конверсии

Aspose.PDF для C++ поддерживает функцию преобразования PDF в TIF с использованием LZW-сжатия, а затем с использованием AForge можно применить бинаризацию. Однако один из клиентов запросил, чтобы для некоторых изображений им нужно было получить пороговое значение, используя метод Оцу, поэтому они также хотели бы использовать метод Бредли.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffBradleyBinarization()
{
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Открыть документ
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PageToTIFF.pdf");

    String outputImageFile = _dataDir + u"resultant_out.tif";
    String outputBinImageFile = _dataDir + u"37116-bin_out.tif";

    // Создать объект разрешения
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Создать объект TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::LZW);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format1bpp);

    // Создать устройство TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);
    auto imageStream = System::IO::File::OpenWrite(_dataDir + outputImageFile);

    // Преобразовать определенную страницу и сохранить изображение в поток
    tiffDevice->Process(pdfDocument, 1, 2, imageStream);

    imageStream->Close();

    auto inStream = System::IO::File::OpenRead(outputImageFile);
    auto outStream = System::IO::File::OpenWrite(outputBinImageFile);

    tiffDevice->BinarizeBradley(inStream, outStream, 0.1);
}
```

## Convert PDF using ImageDevice class

`ImageDevice` является предком для `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` и `EmfDevice`.

- Класс [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device/) позволяет преобразовывать страницы PDF в изображения <abbr title="Bitmap Image File">BMP</abbr>.
- Класс [EmfDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.emf_device/) позволяет преобразовывать страницы PDF в изображения <abbr title="Enhanced Meta File">EMF</abbr>.
- Класс [JpegDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.jpeg_device/) позволяет преобразовывать страницы PDF в изображения JPEG.
- Класс [PngDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.png_device/) позволяет преобразовывать страницы PDF в изображения <abbr title="Portable Network Graphics">PNG</abbr>.

- Класс [GifDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.gif_device/) позволяет преобразовывать страницы PDF в изображения <abbr title="Graphics Interchange Format">GIF</abbr>.

Давайте посмотрим, как преобразовать страницу PDF в изображение.

Класс [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device) предоставляет метод с именем [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device#a22cefdb47b7c762320fa7973aa4f1f93), который позволяет конвертировать определенную страницу PDF файла в формат изображения BMP. Другие классы имеют тот же метод. Таким образом, если нам нужно преобразовать страницу PDF в изображение, мы просто создаем экземпляр необходимого класса.

Следующий фрагмент кода демонстрирует эту возможность:

```cpp
void Convert_PDF_To_Images::ConvertPDFusingImageDevice()
{
    std::clog << __func__ << ": Start" << std::endl;

    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Создать объект разрешения            
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300); //300 dpi

    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    bmpDevice = MakeObject<Aspose::Pdf::Devices::BmpDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    jpegDevice = MakeObject<Aspose::Pdf::Devices::JpegDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    gifDevice = MakeObject<Aspose::Pdf::Devices::GifDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    emfDevice = MakeObject<Aspose::Pdf::Devices::EmfDevice>(resolution);

    auto document = MakeObject<Document>(_dataDir + u"ConvertAllPagesToBmp.pdf");

    ConvertPDFtoImage(bmpDevice, u"bmp", document);
    ConvertPDFtoImage(jpegDevice, u"jpeg", document);
    ConvertPDFtoImage(gifDevice, u"gif", document);
    ConvertPDFtoImage(pngDevice, u"png", document);
    ConvertPDFtoImage(emfDevice, u"emf", document);

    std::clog << __func__ << ": Finish" << std::endl;

}

void Convert_PDF_To_Images::ConvertPDFtoImage(
 System::SmartPtr<Aspose::Pdf::Devices::ImageDevice> imageDevice,
 String ext, System::SmartPtr<Document> document)
{
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    for (int pageCount = 1; pageCount <= document->get_Pages()->get_Count(); pageCount++)
    {
    String outfilename = String::Format(u"{0}PageToBmp{1}_out.{2}",
    _dataDir, pageCount, ext);

    auto imageStream = System::IO::File::OpenWrite(outfilename);

    // Создать объект разрешения
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Конвертировать определенную страницу и сохранить изображение в поток
    imageDevice->Process(document->get_Pages()->idx_get(pageCount), imageStream);

    // Закрыть поток
    imageStream->Close();
    }
}
```

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в PNG онлайн**

Как пример того, как работают наши бесплатные приложения, пожалуйста, ознакомьтесь со следующей функцией.

Aspose.PDF для C++ представляет вам бесплатное онлайн-приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попробовать изучить функциональность и качество работы.

[![Как преобразовать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Преобразование PDF с использованием класса SaveOptions

Эта часть статьи показывает, как преобразовать PDF в <abbr title="Scalable Vector Graphics">SVG</abbr> с использованием C++ и класса SaveOptions.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в SVG онлайн**

Aspose.PDF для C++ представляет вам бесплатное онлайн-приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попробовать изучить функциональность и качество работы.

[![Преобразование PDF в SVG с помощью бесплатного приложения Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)

{{% /alert %}}

Для того чтобы преобразовать PDF в SVG, Aspose.PDF для CPP предлагает метод [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Вам необходимо передать путь к выходному файлу и перечисление SaveFormat:: svg в метод Save для преобразования PDF в SVG. Следующий фрагмент кода показывает, как преобразовать PDF в SVG:

Эта статья учит вас, как преобразовать PDF в <abbr title="Scalable Vector Graphics">SVG</abbr> с использованием C++.

**Scalable Vector Graphics (SVG)** — это семейство спецификаций формата файлов на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который находится в разработке Всемирным консорциумом веб-стандартов (W3C) с 1999 года.

Изображения SVG и их поведение определяются в XML текстовых файлах. Это означает, что их можно искать, индексировать, скриптовать и, при необходимости, сжимать. Как и XML файлы, SVG изображения могут быть созданы и отредактированы с помощью любого текстового редактора, но часто удобнее создавать их с помощью программ для рисования, таких как Inkscape.

Aspose.PDF for C++ поддерживает функцию преобразования SVG изображения в формат PDF, а также предлагает возможность преобразования PDF файлов в формат SVG. Для выполнения этого требования в пространство имен Aspose.PDF был введен класс `SvgSaveOptions`. Создайте экземпляр объекта SvgSaveOptions и передайте его в качестве второго аргумента методу [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

Следующий фрагмент кода показывает шаги для преобразования PDF файла в формат SVG с использованием C++.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoSvgSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени файла
    String infilename("PageToSvg.pdf");
    String outfilename("PageToSvg_out.svg");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать экземпляр объекта SvgSaveOptions
    auto saveOptions = MakeObject<SvgSaveOptions>();
    // Не сжимать изображение SVG в архив Zip
    saveOptions->CompressOutputToZipArchive = false;

    try {
    // Сохранить выходные данные в файлы SVG
    document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```