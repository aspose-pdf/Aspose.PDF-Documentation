---
title: Trabajando con Portafolio en PDF
linktitle: Portafolio
type: docs
weight: 40
url: es/cpp/portfolio/
description: Cree un Portafolio PDF con Aspose.PDF para C++. Debe usar un archivo de Microsoft Excel, un documento de Word y un archivo de imagen para crear un Portafolio PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cómo Crear un Portafolio PDF

Aspose.PDF permite crear documentos de Portafolio PDF usando la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Agregue un archivo en un objeto Document.Collection después de obtenerlo con la clase [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Cuando los archivos han sido agregados, use el método Save de la clase Document para guardar el documento del portafolio.

El siguiente ejemplo utiliza un archivo de Microsoft Excel, un documento de Word y un archivo de imagen para crear un Portafolio PDF.

El código a continuación da como resultado el siguiente portafolio.

### Un Portafolio PDF creado con Aspose.PDF

![Un Portafolio PDF creado con Aspose.PDF para C++](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Document
    auto pdfDocument = MakeObject<Document>();

    // Instanciar objeto de colección de documentos
    pdfDocument->set_Collection(MakeObject<Collection>());

    // Obtener archivos para agregar al portafolio
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // Proporcionar descripción de los archivos
    excel->set_Description(u"Archivo de Excel");
    word->set_Description(u"Archivo de Word");
    image->set_Description(u"Archivo de Imagen");

    // Agregar archivos a la colección de documentos
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // Guardar documento del portafolio
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```

## Extraer archivos del portafolio PDF

PDF Portfolios le permiten reunir contenido de una variedad de fuentes (por ejemplo, archivos PDF, Word, Excel, JPEG) en un contenedor unificado. Los archivos originales conservan sus identidades individuales pero se ensamblan en un archivo de Portafolio PDF. Los usuarios pueden abrir, leer, editar y formatear cada archivo componente independientemente de los otros archivos componentes.

Aspose.PDF permite la creación de documentos de Portafolio PDF usando la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). También ofrece la capacidad de extraer archivos de un portafolio PDF.

El siguiente fragmento de código le muestra los pasos para extraer archivos de un portafolio PDF.

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Abrir un documento
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // Obtener colección de archivos incrustados
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // Iterar a través de cada archivo del Portafolio
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // Guardar el archivo extraído en alguna ubicación
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // Cerrar el objeto stream
    fileStream->Close();
    }
}
```

![Extract files from PDF Portfolio](working-with-pdf-portfolio_2.jpg)

## Eliminar archivos del portafolio PDF

Para eliminar/quitar archivos del portafolio PDF, intente usar las siguientes líneas de código.

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Cargar portafolio PDF de origen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```