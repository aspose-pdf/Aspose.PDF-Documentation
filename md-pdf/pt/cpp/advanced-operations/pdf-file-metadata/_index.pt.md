---
title: Metadados do Arquivo PDF
type: docs
weight: 20
url: /cpp/pdf-file-metadata/
---

## Obter/Definir Informações do Arquivo PDF

Para obter informações específicas de um arquivo PDF, você primeiro precisa chamar o **get_Info()** da classe Document. Uma vez que o objeto DocumentInfo é recuperado, você pode obter os valores das propriedades individuais. Além disso, você também pode definir as propriedades usando os métodos respectivos da classe DocumentInfo. O trecho de código a seguir demonstra como obter/definir informações do arquivo PDF usando Aspose.PDF para C++:

{{% alert color="primary" %}}

Por favor, note que você não pode definir valores contra os campos **Application** e **Producer**, porque Aspose Ltd. e Aspose.PDF para C++ x.x.x serão exibidos contra esses campos.

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // Obter informações do documento
    auto docInfo = pdfDocument->get_Info();
    // Mostrar informações do documento
    Console::WriteLine(u"Autor: {0}", docInfo->get_Author());
    Console::WriteLine(u"Data de Criação: {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Palavras-chave: {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Data de Modificação: {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Assunto: {0}", docInfo->get_Subject());
    Console::WriteLine(u"Título: {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // Especificar informações do documento
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"Informações do PDF");
    docInfo->set_Title (u"Definindo Informações do Documento PDF");

    // Salvar documento de saída
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```

## Obter/Definir Metadados XMP de um Arquivo PDF

Aspose.PDF para C++ permite acessar os metadados XMP de um arquivo PDF, bem como defini-los. Para obter/definir os metadados de um arquivo PDF:

1. Crie um objeto Document e abra o arquivo PDF de entrada.
1. Obtenha/Defina os metadados do arquivo usando os métodos respectivos.

O snippet de código a seguir mostra como obter/definir metadados do arquivo PDF.

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // Obter propriedades
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // Definir propriedades
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // Salvar documento
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // o prefixo xmlns foi removido
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // Salvar documento
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```