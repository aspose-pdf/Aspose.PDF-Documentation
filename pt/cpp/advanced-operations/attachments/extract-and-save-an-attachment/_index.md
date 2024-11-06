---
title: Extrair e Salvar um Anexo
linktitle: Extrair e Salvar um Anexo
type: docs
weight: 20
url: pt/cpp/extract-and-save-an-attachment/
description: Aspose.PDF para C++ permite que você obtenha todos os anexos de um documento PDF. Além disso, você pode obter um anexo individual do seu documento.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Todos os Anexos

Com Aspose.PDF, é possível obter todos os anexos de um documento PDF. Isso é útil quando você deseja salvar os documentos separadamente do PDF ou se precisar remover anexos de um PDF.

Para obter todos os anexos de um arquivo PDF:

1. Loop através da coleção [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). A coleção [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) contém todos os anexos. Cada elemento desta coleção representa um objeto [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Cada iteração do loop foreach através da coleção [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) retorna um objeto [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). 
1. Uma vez que o objeto está disponível, recupere todas as propriedades do arquivo anexado ou o próprio arquivo.

Os trechos de código a seguir mostram como obter todos os anexos de um documento PDF.

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // Abrir documento
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // Obter coleção de arquivos incorporados
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // Obter contagem dos arquivos incorporados
 Console::WriteLine(u"Total de arquivos : {0}", embeddedFiles->get_Count());

 int count = 1;

 // Loop através da coleção para obter todos os anexos
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Nome: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Descrição: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Tipo Mime: {0}", fileSpecification->get_MIMEType());

  // Verificar se o objeto de parâmetro contém os parâmetros
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"Checksum: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Data de Criação: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Data de Modificação: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Tamanho: {0}", fileSpecification->get_Params()->get_Size());
  }

  // Obter o anexo e escrever para arquivo ou stream
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```
## Obter Anexo Individual

Para obter um anexo individual, podemos especificar o índice do anexo no objeto `EmbeddedFiles` da instância do Documento. Por favor, tente usar o seguinte trecho de código.

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // Obter arquivo incorporado específico
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // Obter as propriedades do arquivo
    Console::WriteLine(u"Nome: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"Descrição: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"Tipo MIME: {0}", fileSpecification->get_MIMEType());

    // Verificar se o objeto de parâmetro contém os parâmetros
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"Checksum: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"Data de Criação: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"Data de Modificação: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"Tamanho: {0}",
        fileSpecification->get_Params()->get_Size());
    }

    // Obter o anexo e escrever para o arquivo ou fluxo
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```