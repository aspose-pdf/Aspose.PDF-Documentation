---
title: Convertir PDF a formatos de Imágenes
linktitle: Convertir PDF a Imágenes
type: docs
weight: 70
url: /cpp/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir PDF a varios formatos de imágenes. Convierte páginas PDF a imágenes PNG, JPEG, BMP con unas pocas líneas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** utiliza pocos enfoques para convertir PDF a imagen. Generalmente hablando, usamos dos enfoques: conversión usando el enfoque Device y conversión usando SaveOption. Esta sección te mostrará cómo convertir documentos PDF a formatos de imagen como BMP, JPEG, PNG, TIFF, y SVG usando uno de esos enfoques.

Hay varias clases en la biblioteca que permiten usar un dispositivo virtual para transformar imágenes. DocumentDevice está orientado a la conversión de todo el documento, pero ImageDevice - para una página en particular.

## Convertir PDF usando la clase DocumentDevice

**Aspose.PDF for C++** hace posible convertir Páginas PDF a imágenes TIFF.

El [TiffDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) (basado en DocumentDevice) permite convertir páginas de PDF a imágenes TIFF. Esta clase proporciona un método llamado [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device#a0790daa96125c5638a645647e9678f0c) que te permite convertir todas las páginas en un archivo PDF a una sola imagen TIFF.

{{% alert color="success" %}}
**Intenta convertir PDF a TIFF en línea**

Aspose.PDF para C++ te presenta la aplicación en línea gratuita ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puedes intentar investigar la funcionalidad y calidad de cómo funciona.

[![Conversión de Aspose.PDF de PDF a TIFF con la aplicación gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir Páginas de PDF a Una Imagen TIFF

Aspose.PDF para C++ explica cómo convertir todas las páginas de un archivo PDF a una sola imagen TIFF:

1.  Abrir [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) con MakeObject.
1. Crear objeto Resolution.
1. Crear objeto [TIffSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_settings/).
1. Crear [dispositivo Tiff](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) con atributos especificados.
1. Convertir una página en particular y guardar la imagen en el flujo.

El siguiente fragmento de código muestra cómo convertir todas las páginas de un PDF en una sola imagen TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTIFF()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("PageToTiff.pdf");
    String outfilename("PagesToTIFF_out.tif");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Crear objeto Resolution
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Crear objeto TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
    tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
    tiffSettings->set_SkipBlankPages(false);

    // Crear dispositivo TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

    // Convertir páginas y guardar la imagen en el flujo
    tiffDevice->Process(document, 1, 2, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
### Convertir Una Página a Imagen TIFF

Aspose.PDF para C++ le permite convertir una página particular en un archivo PDF a una imagen TIFF, use una versión sobrecargada del método Process(..) que toma un número de página como argumento para la conversión. El siguiente fragmento de código muestra cómo convertir la primera página de un PDF al formato TIFF.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para nombre de ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para nombre de archivo
    String infilename("PageToTiff.pdf");
    String outfilename("PageToTiff_out.tif");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Crear objeto de resolución
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Crear dispositivo TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

    // Convertir una página particular y guardar la imagen en el stream
    tiffDevice->Process(document, 1, 1, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Usar el algoritmo de Bradley durante la conversión

Aspose.PDF para C++ ha estado apoyando la función para convertir PDF a TIF usando compresión LZW y luego con el uso de AForge, se puede aplicar Binarización. Sin embargo, uno de los clientes solicitó que para algunas imágenes, necesitan obtener el Umbral usando Otsu, por lo que también les gustaría usar Bradley.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffBradleyBinarization()
{
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PageToTIFF.pdf");

    String outputImageFile = _dataDir + u"resultant_out.tif";
    String outputBinImageFile = _dataDir + u"37116-bin_out.tif";

    // Crear objeto Resolution 
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Crear objeto TiffSettings
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::LZW);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format1bpp);

    // Crear dispositivo TIFF
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);
    auto imageStream = System::IO::File::OpenWrite(_dataDir + outputImageFile);

    // Convertir una página en particular y guardar la imagen en el flujo
    tiffDevice->Process(pdfDocument, 1, 2, imageStream);

    imageStream->Close();

    auto inStream = System::IO::File::OpenRead(outputImageFile);
    auto outStream = System::IO::File::OpenWrite(outputBinImageFile);

    tiffDevice->BinarizeBradley(inStream, outStream, 0.1);
}
```

## Convertir PDF usando la clase ImageDevice

`ImageDevice` es el ancestro de `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` y `EmfDevice`.

- La clase [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device/) te permite convertir páginas de PDF a imágenes <abbr title="Archivo de Imagen de Mapa de Bits">BMP</abbr>.
- La clase [EmfDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.emf_device/) te permite convertir páginas de PDF a imágenes <abbr title="Archivo de Metarchivo Mejorado">EMF</abbr>.
- La clase [JpegDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.jpeg_device/) te permite convertir páginas de PDF a imágenes JPEG.
- La clase [PngDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.png_device/) te permite convertir páginas de PDF a imágenes <abbr title="Gráficos de Red Portátiles">PNG</abbr>.

- La clase [GifDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.gif_device/) te permite convertir páginas de PDF a imágenes <abbr title="Formato de Intercambio de Gráficos">GIF</abbr>.

Echemos un vistazo a cómo convertir una página PDF en una imagen.

La clase [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device) proporciona un método llamado [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device#a22cefdb47b7c762320fa7973aa4f1f93) que te permite convertir una página particular del archivo PDF al formato de imagen BMP. Las otras clases tienen el mismo método. Entonces, si necesitamos convertir una página PDF en una imagen, simplemente instanciamos la clase requerida.

El siguiente fragmento de código muestra esta posibilidad:

```cpp
void Convert_PDF_To_Images::ConvertPDFusingImageDevice()
{
    std::clog << __func__ << ": Start" << std::endl;

    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Crear objeto de resolución            
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
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    for (int pageCount = 1; pageCount <= document->get_Pages()->get_Count(); pageCount++)
    {
    String outfilename = String::Format(u"{0}PageToBmp{1}_out.{2}",
    _dataDir, pageCount, ext);

    auto imageStream = System::IO::File::OpenWrite(outfilename);

    // Crear objeto de resolución
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // Convertir una página particular y guardar la imagen en el flujo
    imageDevice->Process(document->get_Pages()->idx_get(pageCount), imageStream);

    // Cerrar flujo
    imageStream->Close();
    }
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como un ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revisa la siguiente característica.

Aspose.PDF para C++ te presenta la aplicación gratuita en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes intentar investigar la funcionalidad y calidad con la que funciona.

[![Cómo convertir PDF a PNG usando la aplicación gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF usando la clase SaveOptions

Esta parte del artículo te muestra cómo convertir PDF a <abbr title="Gráficos Vectoriales Escalables">SVG</abbr> usando C++ y la clase SaveOptions.

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF para C++ te presenta la aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes intentar investigar la funcionalidad y calidad con la que funciona.

[![Conversión de PDF a SVG con la aplicación gratuita de Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

Para convertir PDF a SVG, Aspose.PDF para CPP ofrece el método [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Necesita pasar la ruta de salida y el enum SaveFormat:: svg al método Save para convertir PDF a SVG. El siguiente fragmento de código muestra cómo convertir PDF a SVG:

Este artículo te enseña cómo convertir PDF a <abbr title="Scalable Vector Graphics">SVG</abbr> usando C++.

**Gráficos Vectoriales Escalables (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el World Wide Web Consortium (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscados, indexados, programados y, si es necesario, comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

Aspose.PDF para C++ admite la función de convertir imágenes SVG a formato PDF y también ofrece la capacidad de convertir archivos PDF a formato SVG. Para cumplir con este requisito, la clase `SvgSaveOptions` ha sido introducida en el espacio de nombres Aspose.PDF. Instanciar un objeto de SvgSaveOptions y pasarlo como un segundo argumento al método [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

El siguiente fragmento de código muestra los pasos para convertir un archivo PDF a formato SVG con C++.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoSvgSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre del camino
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("PageToSvg.pdf");
    String outfilename("PageToSvg_out.svg");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar un objeto de SvgSaveOptions
    auto saveOptions = MakeObject<SvgSaveOptions>();
    // No comprimir la imagen SVG en un archivo Zip
    saveOptions->CompressOutputToZipArchive = false;

    try {
    // Guardar la salida en archivos SVG
    document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```