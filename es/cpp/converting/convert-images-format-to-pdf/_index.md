---
title: Convertir varios formatos de imágenes a PDF 
linktitle: Convertir Imágenes a PDF
type: docs
weight: 60
url: /es/cpp/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: Este tema muestra cómo la biblioteca Aspose.PDF para C++ permite convertir varios formatos de imágenes a PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF para C++** te permite convertir diferentes formatos de imágenes a archivos PDF. Nuestra biblioteca demuestra fragmentos de código para convertir los formatos de imagen más populares, tales como - formatos BMP, DICOM, EMF, JPG, PNG, SVG y TIFF.

## Convertir BMP a PDF

Convierte archivos BMP a documentos PDF usando la biblioteca **Aspose.PDF para C++**.

Las imágenes <abbr title="Archivo de Imagen Bitmap">BMP</abbr> son archivos que tienen la extensión. BMP representa archivos de imagen de mapa de bits que se utilizan para almacenar imágenes digitales de mapa de bits. Estas imágenes son independientes del adaptador gráfico y también se llaman formato de archivo de mapa de bits independiente del dispositivo (DIB).
Puedes convertir archivos BMP a PDF con la API de Aspose.PDF para C++. Por lo tanto, puede seguir los siguientes pasos para convertir imágenes BMP:

1. Cree una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de ruta y el nombre de archivo.
1. Se crea una instancia de un nuevo objeto Document.
1. Añada una nueva [Página](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) a este [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Se crea un nuevo Aspose.Pdf BMP.
1. El objeto Aspose.PDF BMP se inicializa utilizando el archivo de entrada.
1. Aspose.PDF BMP se añade a la Página como un Párrafo.
1. Finalmente, guarde el archivo PDF de salida

Por lo tanto, el siguiente fragmento de código sigue estos pasos y muestra cómo convertir BMP a PDF usando C++:

```cpp
void ConvertBMPtoPDF() 
{
    std::clog << "BMP to PDF convert: Start" << std::endl;

    // String para el nombre de ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para el nombre del archivo de entrada
    String infilename("sample.bmp");

    // String para el nombre del archivo de salida
    String outfilename("ImageToPDF-BMP.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    // Añadir página vacía en documento vacío
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Añadir imagen en una página
    page->get_Paragraphs()->Add(image);

    // Guardar documento de salida
    document->Save(_dataDir + outfilename);

    std::clog << "BMP to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Intenta convertir BMP a PDF en línea**

Aspose te presenta una aplicación gratuita en línea ["BMP a PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF BMP a PDF usando la aplicación gratuita](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Convertir DICOM a PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> es el formato estándar de la industria médica para la creación, almacenamiento, transmisión y visualización de imágenes médicas digitales y documentos de pacientes examinados.

**Aspsoe.PDF para C++** te permite convertir imágenes DICOM y SVG, pero por razones técnicas para añadir imágenes necesitas especificar el tipo de archivo que se añadirá al PDF:

1. Crea una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de ruta y el nombre del archivo.
1. Instanciar el objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Añadir una [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) a la colección de páginas del documento.
1. Aspose.PDF TDicom se añade a la Página como un Párrafo.
1. Cargar y [Guardar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) el archivo de imagen de entrada.

El siguiente fragmento de código muestra cómo convertir archivos DICOM a formato PDF con Aspose.PDF. Debes cargar la imagen DICOM, colocar la imagen en una página en un archivo PDF y guardar el resultado como PDF.

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
**Intenta convertir DICOM a PDF en línea**

Aspose te presenta la aplicación gratuita en línea ["DICOM a PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), donde puedes probar a investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de DICOM a PDF usando la aplicación gratuita](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Convertir EMF a PDF

<abbr title="Formato de metarchivo mejorado">EMF</abbr>EMF almacena imágenes gráficas independientemente del dispositivo. Los metarchivos de EMF constan de registros de longitud variable en orden cronológico que pueden renderizar la imagen almacenada después de analizarse en cualquier dispositivo de salida. Además, puedes convertir EMF a imagen PDF usando los siguientes pasos:

1. Crea una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de ruta y el nombre del archivo.
1. Se crea una instancia de un nuevo objeto Document.
1. Añade una nueva Página a este [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Un nuevo Aspose.Pdf TIFF es creado.
1. El objeto Aspose.PDF TIFF se inicializa usando el archivo de entrada.
1. Aspose.PDF TIFF se añade a la Página como un Párrafo.
1. Cargue y [Guarde](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) el archivo de imagen de entrada.

Además, el siguiente fragmento de código muestra cómo convertir un EMF a PDF con C++ en su fragmento de código:

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
{{% alert color="success" %}}
**Intente convertir EMF a PDF en línea**

Aspose le presenta una aplicación gratuita en línea ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Convertion EMF to PDF using Free App](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Convertir JPG a PDF

No hay necesidad de preguntarse cómo convertir JPG a PDF, porque la biblioteca **Aspose.PDF for C++** tiene la mejor solución.

Puede convertir muy fácilmente imágenes JPG a PDF con Aspose.PDF for C++ siguiendo estos pasos:

1. Cree una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de ruta y el nombre de archivo.
1. Se crea una instancia de un nuevo objeto Documento.
1. Agregue una nueva Página a este [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Se crea una nueva Aspose::Pdf::Image.
1. El objeto Imagen de Aspose.PDF se inicializa usando el archivo de entrada.
1. Aspose.PDF Image se agrega a la página como un párrafo.  
1. Cargue y guarde el archivo de imagen de entrada.

El fragmento de código a continuación muestra cómo convertir una imagen JPG a PDF usando C++:

```cpp
void ConvertJPEGtoPDF() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.jpg");

    // Cadena para el nombre del archivo de salida
    String outfilename("ImageToPDF-JPEG.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    // Agregar página vacía en documento vacío
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Agregar imagen en una página
    page->get_Paragraphs()->Add(image);

    // Guardar documento de salida
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

Luego puede ver cómo convertir una imagen a PDF con **la misma altura y ancho de la página**. Obtendremos las dimensiones de la imagen y, en consecuencia, estableceremos las dimensiones de la página del documento PDF con los siguientes pasos:

1. Cargar el archivo de imagen de entrada
1. Obtener la altura y el ancho de la imagen
1. Establecer la altura, el ancho y los márgenes de una página
1. Guardar el archivo PDF de salida

El siguiente fragmento de código muestra cómo convertir una imagen a PDF con la misma altura y ancho de página usando C++:

```cpp
void ConvertJPGtoPDF_fitsize() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.jpg");

    // String for input file name
    String outfilename("ImageToPDF-JPG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);


    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Set page dimensions and margins
    page->get_PageInfo()->set_Height(bitMap->get_Height());
    page->get_PageInfo()->set_Width(bitMap->get_Width());
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Intenta convertir JPG a PDF en línea**

Aspose te presenta una aplicación gratuita en línea ["JPG a PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de JPG a PDF usando la Aplicación Gratuita](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Convertir PNG a PDF

**Aspose.PDF para C++** soporta la característica de convertir imágenes PNG a formato PDF. Revisa el siguiente fragmento de código para realizar tu tarea.

<abbr title="Portable Network Graphics">PNG</abbr> se refiere a un tipo de formato de archivo de imagen rasterizada que utiliza compresión sin pérdida, lo que lo hace popular entre sus usuarios.

Puedes convertir PNG a imagen PDF usando los siguientes pasos:

1. Crea una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de la ruta y el nombre del archivo.
1. Se crea una instancia de un nuevo objeto Document.
1. Agrega una nueva Página a este [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Se crea un nuevo Aspose.Pdf PNG.
1. El objeto Aspose.PDF PNG se inicializa usando el archivo de entrada.
1. Aspose.PDF PNG se añade a la Página como un Párrafo.
1. Cargar y guardar el archivo de imagen de entrada.

Además, el siguiente fragmento de código muestra cómo convertir PNG a PDF en tus aplicaciones C++:

```cpp
void ConvertPNGtoPDF() 
{
    std::clog << "PNG a PDF convertir: Inicio" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.png");

    // Cadena para el nombre del archivo de salida
    String outfilename("ImageToPDF-PNG.pdf");

    // Abrir documento
    auto document = MakeObject<Document>();

    // Agregar página vacía en documento vacío
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Agregar imagen en una página
    page->get_Paragraphs()->Add(image);

    // Guardar documento de salida
    document->Save(_dataDir + outfilename);
    std::clog << "PNG a PDF convertir: Fin" << std::endl;
}
```
{{% alert color="success" %}}
**Intenta convertir PNG a PDF en línea**

Aspose te presenta la aplicación gratuita en línea ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Conversión PNG a PDF usando la aplicación gratuita](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Convertir SVG a PDF

**Aspose.PDF para C++** explica cómo convertir imágenes SVG al formato PDF y cómo obtener las dimensiones del archivo <abbr title="Scalable Vector Graphics">SVG</abbr> de origen.

Scalable Vector Graphics (SVG) es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el World Wide Web Consortium (W3C) desde 1999.

Las imágenes SVG y sus comportamientos se definen en archivos de texto XML. Esto significa que pueden ser buscados, indexados, programados y, si es necesario, comprimidos. Como archivos XML, las imágenes SVG pueden ser creadas y editadas con cualquier editor de texto, pero a menudo es más conveniente crearlas con programas de dibujo como Inkscape.

1. Crear una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de ruta y el nombre del archivo.
1. Crear una instancia de la clase [`SvgLoadOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options).
1. Crear una instancia de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el nombre de archivo de origen mencionado y opciones.
1. Guardar el documento con el nombre de archivo deseado.

El siguiente fragmento de código muestra el proceso de conversión de un archivo SVG a formato PDF con Aspose.PDF para C++.

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
    std::clog << "Conversión de SVG a PDF: Inicio" << std::endl;

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

    std::clog << "Conversión de SVG a PDF: Fin" << std::endl;
}
```

{{% alert color="success" %}}
**Intenta convertir el formato SVG a PDF en línea**


Aspose.PDF para C++ te presenta la aplicación en línea gratuita ["SVG a PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), donde puedes probar e investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión SVG a PDF con Aplicación Gratuita](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## Convertir TIFF a PDF

El formato de archivo **Aspose.PDF** es compatible, ya sea una imagen <abbr title="Formato de Archivo de Imagen Etiquetado">TIFF</abbr> de un solo fotograma o de múltiples fotogramas. Esto significa que puedes convertir la imagen TIFF a PDF en tus aplicaciones C++.

TIFF o TIF, Formato de Archivo de Imagen Etiquetado, representa imágenes rasterizadas que están destinadas a su uso en una variedad de dispositivos que cumplen con este estándar de formato de archivo. Una imagen TIFF puede contener varios fotogramas con diferentes imágenes. El formato de archivo Aspose.PDF también es compatible, ya sea una imagen TIFF de un solo fotograma o de múltiples fotogramas. Así que puedes convertir la imagen TIFF a PDF en tus aplicaciones C++. Por lo tanto, consideraremos un ejemplo de conversión de una imagen TIFF de varias páginas a un documento PDF de varias páginas con los siguientes pasos:

1. Crear una [Clase String](https://reference.aspose.com/pdf/cpp/class/system.string) para el nombre de la ruta y el nombre del archivo.
1. Un instancia de un nuevo objeto Documento es creado.
1. Agregar una nueva Página a este [Documento](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Se crea un nuevo Aspose.Pdf TIFF.
1. El objeto Aspose.PDF TIFF se inicializa usando el archivo de entrada.
1. Aspose.PDF TIFF se agrega a la Página como un Párrafo.
1. Cargar y guardar el archivo de imagen de entrada.

Además, el siguiente fragmento de código muestra cómo convertir una imagen TIFF de múltiples páginas o múltiples cuadros a PDF con C++:

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