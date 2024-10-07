---
title: Obter Metadados XMP de Arquivo PDF
type: docs
weight: 30
url: /net/get-xmp-metadata-of-an-existing-pdf-file/
description: Esta seção explica como obter Metadados XMP de um PDF existente com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Para obter metadados XMP de um arquivo PDF, você precisa criar um objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) e vincular o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Você pode passar propriedades específicas de metadados XMP para o objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para obter seus valores. O trecho de código a seguir mostra como obter metadados XMP de um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Criar objeto PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Vincular arquivo pdf ao objeto
xmpMetaData.BindPdf(dataDir + "input.pdf");

// Obter propriedades de Metadados XMP
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreateDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.MetadataDate].ToString());
Console.WriteLine(": {0}", xmpMetaData[DefaultMetadataProperties.CreatorTool].ToString());
Console.WriteLine(": {0}", xmpMetaData["customNamespace:UserPropertyName"].ToString());

Console.ReadLine();
```