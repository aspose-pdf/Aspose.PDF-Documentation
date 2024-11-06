---
title: Extrair fontes de PDF C#
linktitle: Extrair fontes de PDF
type: docs
weight: 30
url: pt/net/extract-fonts-from-pdf/
description: Utilize a biblioteca Aspose.PDF para .NET para extrair todas as fontes incorporadas do seu documento PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Caso você queira obter todas as fontes de um documento PDF, você pode usar o método FontUtilities.GetAllFonts() fornecido na classe Document. Por favor, verifique o seguinte trecho de código para obter todas as fontes de um documento PDF existente:

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

