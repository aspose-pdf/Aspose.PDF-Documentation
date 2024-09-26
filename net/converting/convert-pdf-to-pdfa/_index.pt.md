---
title: Converter PDF para formatos PDF/A
linktitle: Converter PDF para formatos PDF/A
type: docs
weight: 100
url: /net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Este tópico mostra como o Aspose.PDF permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para .NET** permite converter um arquivo PDF para um arquivo PDF compatível com <abbr title="Portable Document Format / A">PDF/A</abbr>. Antes de fazer isso, o arquivo deve ser validado. Este tópico explica como.

{{% alert color="primary" %}}

Observe que seguimos o Adobe Preflight para validar a conformidade com PDF/A. Todas as ferramentas do mercado têm sua própria "representação" de conformidade com PDF/A. Por favor, verifique este artigo sobre ferramentas de validação de PDF/A para referência. Escolhemos os produtos Adobe para verificar como o Aspose.PDF produz arquivos PDF porque a Adobe está no centro de tudo que está conectado ao PDF.

{{% /alert %}}

Converta o arquivo usando o método Convert da classe Document.
{{% alert color="success" %}}
**Tente converter PDF para PDF/A online**

Aspose.PDF para .NET apresenta a você a aplicação gratuita online ["PDF para PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para PDF/A com Aplicativo Gratuito](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Converter arquivo PDF para PDF/A-1b

O seguinte trecho de código mostra como converter arquivos PDF para PDFs compatíveis com PDF/A-1b.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Abrir documento
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// Converter para documento compatível com PDF/A
// Durante o processo de conversão, a validação também é realizada
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// Salvar documento de saída
pdfDocument.Save(dataDir);
```
Para realizar apenas a validação, use a seguinte linha de código:

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validar PDF para PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## Converter arquivo PDF para PDF/A-3b

Aspose.PDF para .NET também suporta a funcionalidade de converter um arquivo PDF para o formato PDF/A-3b.

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Abrir documento
Document pdfDocument = new Document(dataDir + "input.pdf");           

pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// Salvar documento de saída
pdfDocument.Save(dataDir);
```
## Converter arquivo PDF para formato PDF/A-2u

Aspose.PDF para .NET também suporta a funcionalidade de converter um arquivo PDF para o formato PDF/A-2u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Converter arquivo PDF para formato PDF/A-3u

Aspose.PDF para .NET também suporta a funcionalidade de converter um arquivo PDF para o formato PDF/A-3u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Adicionar Anexo ao arquivo PDF/A

Caso você tenha a necessidade de anexar arquivos ao formato de conformidade PDF/A, então recomendamos usar o valor PDF_A_3A da enumeração Aspose.PDF.PdfFormat.
PDF/A_3a é o formato que proporciona a funcionalidade de anexar qualquer formato de arquivo como um anexo ao arquivo compatível com PDF/A.

```csharp
```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instanciar a classe Document para carregar um arquivo existente
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// Configurar novo arquivo para ser adicionado como anexo
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "Arquivo de imagem grande");
// Adicionar anexo à coleção de arquivos anexados do documento
doc.EmbeddedFiles.Add(fileSpecification);
// Realizar a conversão para PDF/A_3a para que o anexo seja incluído no arquivo resultante
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// Salvar o arquivo resultante
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```

## Substituir fontes ausentes por fontes alternativas

Conforme os padrões PDFA, as fontes devem ser incorporadas no documento PDFA.
De acordo com os padrões PDFA, as fontes devem ser incorporadas no documento PDFA.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // A fonte está faltando na máquina de destino
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert( dataDir +  "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```
