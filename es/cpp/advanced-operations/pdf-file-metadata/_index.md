---
title: Metadata de Archivo PDF
type: docs
weight: 20
url: es/cpp/pdf-file-metadata/
---

## Obtener/Establecer Información del Archivo PDF

Para obtener información específica de un archivo PDF, primero necesitas llamar al **get_Info()** de la clase Document. Una vez que se recupera el objeto DocumentInfo, puedes obtener los valores de las propiedades individuales. Además, también puedes establecer las propiedades utilizando los métodos respectivos de la clase DocumentInfo. El siguiente fragmento de código demuestra cómo obtener/establecer la información del archivo PDF usando Aspose.PDF para C++:

{{% alert color="primary" %}}

Por favor, ten en cuenta que no puedes establecer valores en los campos **Application** y **Producer**, porque Aspose Ltd. y Aspose.PDF for C++ x.x.x se mostrarán en estos campos.

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // Obtener información del documento
    auto docInfo = pdfDocument->get_Info();
    // Mostrar información del documento
    Console::WriteLine(u"Autor: {0}", docInfo->get_Author());
    Console::WriteLine(u"Fecha de Creación: {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Palabras Clave: {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Fecha de Modificación: {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Asunto: {0}", docInfo->get_Subject());
    Console::WriteLine(u"Título: {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // Especificar información del documento
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"Información del PDF");
    docInfo->set_Title (u"Estableciendo Información del Documento PDF");

    // Guardar documento de salida
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```

## Obtener/Establecer Metadatos XMP de un Archivo PDF

Aspose.PDF para C++ te permite acceder y establecer los metadatos XMP de un archivo PDF. Para obtener/establecer los metadatos de un archivo PDF:

1. Crea un objeto Document y abre el archivo PDF de entrada.
1. Obtén/Establece los metadatos del archivo utilizando los métodos respectivos.

El siguiente fragmento de código te muestra cómo obtener/establecer metadatos del archivo PDF.

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // Obtener propiedades
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // Establecer propiedades
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // Guardar documento
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // el prefijo xmlns ha sido eliminado
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // Guardar documento
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```