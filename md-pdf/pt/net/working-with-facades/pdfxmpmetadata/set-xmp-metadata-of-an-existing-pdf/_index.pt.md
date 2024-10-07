---
title: Definir Metadados XMP de um PDF existente
type: docs
weight: 20
url: /net/set-xmp-metadata-of-an-existing-pdf/
description: Esta seção explica como definir Metadados XMP de um PDF existente com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Para definir metadados XMP em um arquivo PDF, você precisa criar um objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) e vincular o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Você pode usar o método [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) da classe [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para adicionar diferentes propriedades. Finalmente, chame o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) da classe [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata). O trecho de código a seguir mostra como adicionar metadados XMP em um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Criar objeto PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Vincular arquivo pdf ao objeto
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// Adicionar data de criação
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// Alterar data de metadados
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// Adicionar ferramenta de criação
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Nome da ferramenta de criação");

// Remover data de modificação
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// Adicionar propriedade definida pelo usuário
// Passo #1: registrar prefixo de namespace e URI
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// Passo #2: adicionar propriedade do usuário com o prefixo
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// Alterar propriedade definida pelo usuário
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// Salvar metadados xmp no arquivo pdf
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// Fechar o objeto
xmpMetaData.Close();
```