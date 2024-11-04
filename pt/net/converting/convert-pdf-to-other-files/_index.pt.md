---
title: Converter PDF para EPUB, LaTeX, Texto, XPS em C#
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /net/convert-pdf-to-other-files/
lastmod: "2021-11-01"
keywords: converter, PDF, EPUB, LaTeX, Texto, XPS, C#
description: Este tópico mostra como converter arquivos PDF para outros formatos de arquivo como EPUB, LaTeX, Texto, XPS etc usando C# ou .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter PDF para EPUB

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF para .NET apresenta a você a aplicação gratuita online ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para EPUB com App Gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publicação Eletrônica">EPUB</abbr>** é um padrão de e-book livre e aberto do International Digital Publishing Forum (IDPF).
**<abbr title="Publicação Eletrônica">EPUB</abbr>** é um padrão de e-book livre e aberto do Fórum Internacional de Publicação Digital (IDPF).
EPUB é projetado para conteúdo refluível, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico. EPUB também suporta conteúdo de layout fixo. O formato é destinado como um formato único que editoras e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Aspose.PDF para .NET também suporta a funcionalidade de converter documentos PDF para o formato EPUB. Aspose.PDF para .NET possui uma classe chamada EpubSaveOptions que pode ser usada como segundo argumento no método [`Document.Save(..)`](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index), para gerar um arquivo EPUB.
Por favor, tente usar o seguinte trecho de código para realizar essa tarefa com C#.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// Carregar o documento PDF
Document pdfDocument = new Document(dataDir + "PDFToEPUB.pdf");
// Instanciar opções de salvar em Epub
EpubSaveOptions options = new EpubSaveOptions();
// Especificar o layout para os conteúdos
options.ContentRecognitionMode = EpubSaveOptions.RecognitionMode.Flow;
// Salvar o documento ePUB
pdfDocument.Save(dataDir + "PDFToEPUB_out.epub", options);
```
## Converter PDF para LaTeX/TeX

**Aspose.PDF for .NET** suporta a conversão de PDF para LaTeX/TeX.
O formato de arquivo LaTeX é um formato de arquivo de texto com marcação especial e usado no sistema de preparação de documentos baseado em TeX para tipografia de alta qualidade.

{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF for .NET apresenta a você a aplicação gratuita online ["PDF para LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para LaTeX/TeX com Aplicativo Gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Para converter arquivos PDF para TeX, o Aspose.PDF tem a classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/latexsaveoptions) que fornece a propriedade OutDirectoryPath para salvar imagens temporárias durante o processo de conversão.

O seguinte trecho de código mostra o processo de conversão de arquivos PDF para o formato TEX com C#.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Criar objeto Document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "PDFToTeX.pdf");

// Instanciar opção de salvar LaTeX          
LaTeXSaveOptions saveOptions = new LaTeXSaveOptions();

// Especificar o diretório de saída
string pathToOutputDirectory = dataDir;

// Definir o caminho do diretório de saída para o objeto de opção de salvar
saveOptions.OutDirectoryPath = pathToOutputDirectory;

// Salvar arquivo PDF no formato LaTeX           
doc.Save(dataDir + "PDFToTeX_out.tex", saveOptions);
```
## Converter PDF para Texto

**Aspose.PDF para .NET** suporta a conversão de todo o documento PDF e de página única para um arquivo de Texto.

### Converter todo o documento PDF para arquivo de Texto

Você pode converter um documento PDF para um arquivo TXT usando o método [Visit](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber/methods/visit/index) da classe [TextAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textabsorber).

O seguinte trecho de código explica como extrair os textos de todas as páginas.

```csharp
public static void ConvertPDFDocToTXT()
{
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "demo.pdf");
    TextAbsorber ta = new TextAbsorber();
    ta.Visit(pdfDocument);
    // Salvar o texto extraído em arquivo de texto
    File.WriteAllText(_dataDir + "input_Text_Extracted_out.txt",ta.Text);
}
```

{{% alert color="success" %}}
**Tente converter PDF para Texto online**

Aspose.PDF para .NET apresenta a você uma aplicação gratuita online ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode experimentar investigar a funcionalidade e qualidade com que funciona.
Aspose.PDF for .NET apresenta-lhe a aplicação gratuita online ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Conversão de PDF para Texto com Aplicativo Gratuito Aspose.PDF](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Converter página PDF para arquivo de texto

Você pode converter um documento PDF para um arquivo TXT com Aspose.PDF para .NET. Você deve usar o método `Visit` da classe `TextAbsorber` para resolver essa tarefa.

O seguinte trecho de código explica como extrair os textos das páginas específicas.

```csharp
public static void ConvertPDFPagestoTXT()
{
    Document pdfDocument = new Document(System.IO.Path.Combine(_dataDir, "demo.pdf"));
    TextAbsorber ta = new TextAbsorber();
    var pages = new [] {1, 3, 4};
    foreach (var page in pages)
    {
        ta.Visit(pdfDocument.Pages[page]);
    }
   
    // Salva o texto extraído em arquivo de texto
    File.WriteAllText(System.IO.Path.Combine(_dataDir, "input_Text_Extracted_out.txt"), ta.Text);
}
```
## Converter PDF para XPS

**Aspose.PDF for .NET** oferece a possibilidade de converter arquivos PDF para o formato <abbr title="XML Paper Specification">XPS</abbr>. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com C#.

{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF for .NET apresenta a você a aplicação gratuita online ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode experimentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para XPS com Aplicativo Gratuito](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

O tipo de arquivo XPS está principalmente associado à Especificação de Papel XML pela Microsoft Corporation. A Especificação de Papel XML (XPS), anteriormente conhecida como codinome Metro e englobando o conceito de marketing Next Generation Print Path (NGPP), é uma iniciativa da Microsoft para integrar a criação e visualização de documentos ao sistema operacional Windows.

Para converter arquivos PDF para XPS, Aspose.PDF possui a classe [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) que é usada como segundo argumento no método [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) para gerar o arquivo XPS.
Para converter arquivos PDF em XPS, o Aspose.PDF possui a classe [XpsSaveOptions](https://reference.aspose.com/net/pdf/aspose.pdf/xpssaveoptions) que é usada como segundo argumento no método [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) para gerar o arquivo XPS.

O seguinte trecho de código mostra o processo de conversão de um arquivo PDF em formato XPS.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá até https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Carregar o documento PDF
Document pdfDocument = new Document(dataDir + "input.pdf");

// Instanciar as opções de salvamento XPS
Aspose.Pdf.XpsSaveOptions saveOptions = new Aspose.Pdf.XpsSaveOptions();
// Salvar o documento XPS
pdfDocument.Save("PDFToXPS_out.xps", saveOptions)
```
