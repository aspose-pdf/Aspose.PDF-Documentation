---
title: Extrair Imagens do PDF C#
linktitle: Extrair Imagens do PDF
type: docs
weight: 20
url: /pt/net/extract-images-from-the-pdf-file/
description: Como extrair uma parte da imagem de um PDF usando Aspose.PDF para .NET em C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

As imagens estão contidas na coleção [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) da coleção [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) de cada página. Para extrair uma página específica, obtenha a imagem da coleção Images usando o índice específico da imagem.

O índice da imagem retorna um objeto [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage). Este objeto fornece um método Save que pode ser usado para salvar a imagem extraída. O seguinte trecho de código mostra como extrair imagens de um arquivo PDF.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

 ```csharp
 // Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET

// Para exemplos completos e arquivos de dados, por favor vá até https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ExtractImages.pdf");

// Extrair uma imagem específica
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// Salvar a imagem de saída
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// Salvar o arquivo PDF atualizado
pdfDocument.Save(dataDir);
```
