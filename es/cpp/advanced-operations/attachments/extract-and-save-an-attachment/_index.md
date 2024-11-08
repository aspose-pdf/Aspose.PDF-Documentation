---
title: Extraer y Guardar un Adjunto
linktitle: Extraer y Guardar un Adjunto
type: docs
weight: 20
url: /es/cpp/extract-and-save-an-attachment/
description: Aspose.PDF para C++ le permite obtener todos los adjuntos de un documento PDF. Además, puede obtener un adjunto individual de su documento.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Todos los Adjuntos

Con Aspose.PDF, es posible obtener todos los adjuntos de un documento PDF. Esto es útil ya sea cuando desea guardar los documentos por separado del PDF, o si necesita eliminar los adjuntos de un PDF.

Para obtener todos los adjuntos de un archivo PDF:

1. Recorrer la colección [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). La colección [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) contiene todos los archivos adjuntos. Cada elemento de esta colección representa un objeto [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Cada iteración del bucle foreach a través de la colección [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) devuelve un objeto [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification).
1. Una vez que el objeto está disponible, recupere las propiedades del archivo adjunto o el archivo en sí.

Los siguientes fragmentos de código muestran cómo obtener todos los archivos adjuntos de un documento PDF.

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // Abrir documento
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // Obtener colección de archivos incrustados
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // Obtener el conteo de los archivos incrustados
 Console::WriteLine(u"Total de archivos : {0}", embeddedFiles->get_Count());

 int count = 1;

 // Recorrer la colección para obtener todos los archivos adjuntos
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Nombre: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Descripción: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Tipo MIME: {0}", fileSpecification->get_MIMEType());

  // Verificar si el objeto parámetro contiene los parámetros
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"CheckSum: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Fecha de creación: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Fecha de modificación: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Tamaño: {0}", fileSpecification->get_Params()->get_Size());
  }

  // Obtener el adjunto y escribir en archivo o flujo
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```
## Obtener un Adjunto Individual

Para obtener un adjunto individual, podemos especificar el índice del adjunto en el objeto `EmbeddedFiles` de la instancia de Documento. Por favor, intente usar el siguiente fragmento de código.

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // Obtener archivo incrustado en particular
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // Obtener las propiedades del archivo
    Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

    // Verificar si el objeto parámetro contiene los parámetros
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"CheckSum: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"Creation Date: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"Modification Date: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"Size: {0}",
        fileSpecification->get_Params()->get_Size());
    }

    // Obtener el adjunto y escribirlo en un archivo o flujo
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```