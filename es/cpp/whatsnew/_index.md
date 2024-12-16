---
title: Novedades de C++
linktitle: Novedades
type: docs
weight: 10
url: /es/cpp/whatsnew/
description: En esta página se presentan las características nuevas más populares en Aspose.PDF para C++ que se han introducido en lanzamientos recientes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## Novedades en Aspose.PDF 24.8

Capacidad para agregar imágenes SVG a una página.

## Novedades en Aspose.PDF 24.4

Se solucionó un problema al cargar imágenes SVG.

## Novedades en Aspose.PDF 24.3

Se corrigieron fugas de memoria al convertir documentos PDF a otros formatos.

## Novedades en Aspose.PDF 24.2

Desde 24.2 se implementó:

- Se ha mejorado el rendimiento del JPXDecoder.

- Se corrigió la lectura de documentos con estructura rota.

## Novedades en Aspose.PDF 23.7

- Se ha introducido la posibilidad de guardar documentos PDF en formato EPUB:

```cpp

    void ConvertPDFtoEPUB()
    {
        std::clog << __func__ << ": Inicio" << std::endl;
        // Cadena para el nombre de la ruta
        String _dataDir("C:\\Samples\\Conversion\\");

        // Cadena para el nombre del archivo de entrada
        String infilename("sample.pdf");
        // Cadena para el nombre del archivo de salida
        String outfilename("PDFToEPUB_out.epub");

        // Abrir documento
        auto document = MakeObject<Document>(_dataDir + infilename);

        // Guardar archivo PDF en formato EPUB
        document->Save(_dataDir + outfilename, SaveFormat::Epub);
        std::clog << __func__ << ": Fin" << std::endl;
    }
```

- La carga de archivos en formato PCL ha sido implementada:

```cpp

    int main(int argc, char** argv)
    {
        try
        {
            auto options = System::MakeObject<PclLoadOptions>();
            options->ConversionEngine = Aspose::Pdf::PclLoadOptions::ConversionEngines::NewEngine;
            options->SupressErrors = false;

            auto doc = System::MakeObject<Document>(u"c:/aspose.pcl", options);
            doc->Save(u"e:/37432.pdf");
        }
        catch (const System::Exception& error)
        {
            Console::WriteLine(u"Error: {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "Error: " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```

## Qué hay de nuevo en Aspose.PDF 23.1

Desde la versión 23.1 se añadió el soporte para imágenes en formato Dicom:

```cpp

    int main()
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Dicom);
        image->set_ImageStream(MakeObject<FileStream>(u"c:/aspose.pdf/Aspose.dcm", FileMode::Open, FileAccess::Read));
        page->get_Paragraphs()->Add(image);
        document->Save(u"e:/document.pdf");
    }
```

## Qué hay de nuevo en Aspose.PDF 22.11

Desde 22.11 se anunció el primer lanzamiento público de **Aspose.PDF para C++ macOS**.

Nos complace anunciar el primer lanzamiento público de Aspose.PDF para C++ macOS. Aspose.PDF para C++ macOS es una biblioteca propietaria de C++ que permite a los desarrolladores crear y manipular documentos PDF sin usar Adobe Acrobat. Aspose.PDF para C++ macOS permite a los desarrolladores crear formularios, agregar/editar texto, manipular páginas PDF, agregar anotaciones, procesar fuentes personalizadas y más.

## Qué hay de nuevo en Aspose.PDF 22.5

Se implementó el soporte de formularios XFA en documentos PDF.

## Qué hay de nuevo en Aspose.PDF 22.4

La nueva versión de Aspose.PDF para C++ tiene una base de código de Aspose.PDF para .Net 22.4 y Aspose.Imaging 22.4.

- se implementó el método System::Drawing::GetThumbnailImage();
- se optimizó el constructor RegionDataNodeRect;
- se corrigió la carga de imágenes en blanco y negro de 1 bit por píxel.

## Qué hay de nuevo en Aspose.PDF 22.3

Se agregaron sobrecargas de métodos a numerosas clases. Estos parámetros tipificados con ArrayView son compatibles donde anteriormente solo se admitía ArrayPtr.

## Qué hay de nuevo en Aspose.PDF 22.1

La nueva versión de Aspose.PDF para C++ tiene una base de código de Aspose.PDF para .Net 22.1:

- se proporcionó la nueva implementación para System::Xml. Anteriormente, teníamos una implementación personalizada basada en las bibliotecas libxml2 y libxslt. La nueva versión se basa en el código portado de CoreFX

- la biblioteca de conversión doble se actualizó a la versión 3.1.7

- los archivos Dll están firmados con el certificado de Aspose

## Qué hay de nuevo en Aspose.PDF 21.10

### Aspose.PDF para C++ admite la característica de convertir SVG a formato PDF

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
Сonsiderar un ejemplo con características avanzadas:

```cpp

    void ConvertSVGtoPDF_Advanced()
    {
        std::clog << "Conversión de SVG a PDF: Inicio" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("Aspose.svg");
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

## Qué hay de nuevo en Aspose.PDF 21.4

### Se ha implementado el guardado de documentos PDF en formato HTML

Aspose.PDF para C++ soporta las características para convertir un archivo PDF en HTML.

```cpp

    int main()
    {
        auto doc = MakeObject<Document>(u"e:\\sample.pdf");
        doc->Save(u"e:\\sample.html", SaveFormat::Html);
    }
```