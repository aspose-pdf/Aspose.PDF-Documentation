---
title: Converter PDF/A para formato PDF
linktitle: Converter PDF/A para formato PDF
type: docs
weight: 110
url: /pt/net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: Este tópico mostra como o Aspose.PDF permite converter um arquivo PDF/A para um documento PDF com a biblioteca .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Converter documento PDF/A para PDF

Converter um documento PDF/A para PDF significa remover a restrição <abbr title="Portable Document Format Archive">PDF/A</abbr> do documento original.
A classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) possui o método [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) para remover as informações de conformidade com PDF do arquivo de entrada/fonte.

```csharp
public static void ConvertPDFAtoPDF()
{
    // Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Remove as informações de conformidade com PDF/A
    pdfDocument.RemovePdfaCompliance();
    // Salva o documento atualizado
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
Esta informação também é removida se você fizer alterações no documento (por exemplo, adicionar páginas). No exemplo a seguir, o documento resultante perde a conformidade com PDF/A após a adição de páginas.

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Adicionar uma nova página (vazia) remove as informações de conformidade com PDF/A.
    pdfDocument.Pages.Add();
    // Salvar o documento atualizado
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
