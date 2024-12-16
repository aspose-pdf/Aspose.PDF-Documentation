---
title: Salvar documento PDF programaticamente
linktitle: Salvar PDF
type: docs
weight: 30
url: /pt/net/save-pdf-document/
description: Aprenda como salvar um arquivo PDF em C# usando a biblioteca Aspose.PDF para .NET. Salve o documento PDF no sistema de arquivos, em stream e em aplicações Web.
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

O próximo trecho de código também funciona com a nova interface gráfica [Aspose.Drawing](/pdf/pt/net/drawing/).

## Salvar documento PDF no sistema de arquivos

Você pode salvar o documento PDF criado ou manipulado no sistema de arquivos usando o método `Save` da classe `Document`.
Quando você não fornece o tipo de formato (opções), o documento é salvo no formato Aspose.PDF v.1.7 (*.pdf).

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // faça algumas manipulações, por exemplo, adicionar uma nova página vazia
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```
## Salvar documento PDF em stream

Você também pode salvar o documento PDF criado ou manipulado em um stream usando sobrecargas dos métodos `Save`.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // fazer algumas manipulações, por exemplo, adicionar uma nova página vazia
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## Salvar documento PDF em aplicações Web

Para salvar documentos em aplicações Web, você pode usar os métodos propostos acima. Além disso, a classe `Document` tem o método `Save` sobrecarregado para uso com a classe [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8).

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// fazer algumas manipulações, por exemplo, adicionar uma nova página vazia
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```
Para uma explicação mais detalhada, por favor siga para a seção [Showcase](/pdf/pt/net/showcases/).

## Salvar no formato PDF/A ou PDF/X

PDF/A é uma versão padronizada pela ISO do Formato de Documento Portátil (PDF) usado para arquivamento e preservação de longo prazo de documentos eletrônicos.
O PDF/A difere do PDF porque proíbe recursos não adequados para arquivamento de longo prazo, como vinculação de fontes (em oposição à incorporação de fontes) e criptografia. Os requisitos da ISO para visualizadores de PDF/A incluem diretrizes de gerenciamento de cores, suporte a fontes incorporadas e uma interface de usuário para ler anotações incorporadas.

PDF/X é um subconjunto do padrão ISO PDF. O propósito do PDF/X é facilitar a troca de gráficos, e, portanto, possui uma série de requisitos relacionados à impressão que não se aplicam aos arquivos PDF padrão.

Nos dois casos, o método `Save` é usado para armazenar os documentos, enquanto os documentos devem ser preparados usando o método `Convert`.

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```

