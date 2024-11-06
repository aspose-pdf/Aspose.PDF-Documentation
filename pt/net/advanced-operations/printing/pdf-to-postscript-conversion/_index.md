---
title: Conversão de PDF para PostScript
linktitle: Conversão de PDF para PostScript
type: docs
weight: 30
url: pt/net/pdf-to-postscript-conversion/
keywords: "pdf to postscript c#"
description: Temos uma solução para conversão de PDF para PostScript. Use para essa tarefa a impressão e a classe PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Conversão de PDF para PostScript",
    "alternativeHeadline": "Converter PDF para PostScript",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, pdf to postscript",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/pdf-to-postscript-conversion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-to-postscript-conversion/"
    },
    "dateModified": "2022-02-04",
    "description": "Temos uma solução para conversão de PDF para PostScript. Use para essa tarefa a impressão e a classe PdfViewer."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **PDF Para Postscript em C#**

A classe PdfViewer fornece a capacidade de imprimir documentos PDF e com a ajuda desta classe, também podemos converter arquivos PDF para o formato PostScript. Para converter um arquivo PDF em PostScript, primeiro instale qualquer impressora PS e apenas imprima para o arquivo com a ajuda do PdfViewer. Você pode seguir as instruções especificadas pela Universidade do Havaí sobre como instalar a impressora PS. O seguinte trecho de código mostra como imprimir e converter um PDF para o formato PostScript.

```csharp
public static void PrintToPostscriptFile()
{
    // O caminho para o diretório de documentos.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // Configurar PrinterSettings e PageSettings
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // Configurar a impressora PS, pode-se encontrar este driver na lista de drivers de impressora pré-instalados no Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // Configurar o nome do arquivo de saída e o atributo PrintToFile
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // Desativar o diálogo de página de impressão
    viewer.PrintPageDialog = false;
    // Passar o objeto de configurações de impressora para o método
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```
## Verificando o Status do Trabalho de Impressão

Um arquivo PDF pode ser impresso em uma impressora física, bem como no Microsoft XPS Document Writer, sem mostrar um diálogo de impressão, usando a classe PdfViewer. Ao imprimir arquivos PDF grandes, o processo pode demorar muito tempo, então o usuário pode não ter certeza se o processo de impressão foi concluído ou encontrou algum problema. Para determinar o status de um trabalho de impressão, use a propriedade PrintStatus. O seguinte trecho de código mostra como imprimir o arquivo PDF em um arquivo XPS e obter o status da impressão.

```csharp
public static void CheckingPrintJobStatus()
{
    // Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
    // O caminho para o diretório de documentos.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Instanciar objeto PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Vincular arquivo PDF de origem
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // Ocultar diálogo de impressão
    viewer.PrintPageDialog = false;

    // Criar objeto de configurações de impressora
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Especificar o nome da impressora
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Nome resultante da impressão
    ps.PrintFileName = "ResultantPrintout.xps";

    // Imprimir a saída para arquivo
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // Especificar o tamanho da página da impressão
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Imprimir o documento com as configurações especificadas acima
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Verificar o status da impressão
    if (viewer.PrintStatus != null)
    {
        // Uma exceção foi lançada
        if (viewer.PrintStatus is Exception ex)
        {
            // Obter mensagem de exceção
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // Não foram encontrados erros. O trabalho de impressão foi concluído com sucesso
        Console.WriteLine("printing completed without any issue..");
    }
}
```
## Obter/Definir o nome do proprietário da impressão

Recentemente, recebemos uma solicitação para obter/definir o nome do proprietário da impressão (o usuário atual que pressionou o botão de imprimir na página da web). Essas informações são necessárias ao imprimir o arquivo PDF. Para cumprir essa solicitação, você pode usar a propriedade chamada PrinterJobName:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// Vincular arquivo PDF fonte
viewer.BindPdf(dataDir + "input.pdf");
// Especificar o nome do trabalho de impressão
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static string GetCurrentUserCredentials()
{
    // A implementação depende do tipo de aplicação em execução (ASP.NET, Windows forms, etc.)
    string userCredentials = string.Empty;
    return userCredentials;
}
```
## Usando Impersonação

Outra abordagem para obter o nome do proprietário do trabalho de impressão é usar a impersonação (executando rotinas de impressão em outro contexto de usuário) ou o usuário pode alterar o nome do proprietário diretamente usando a rotina SetJob.

Por favor, note que não há possibilidade de definir o valor do proprietário usando a API de impressão Aspose.PDF por considerações de segurança. A propriedade PrinterJobName pode ser usada para definir o valor da coluna nome do documento na aplicação de spool de impressão. O trecho de código compartilhado acima apenas mostra como o usuário pode incluir o nome do usuário na coluna nome do documento (por exemplo, usando a sintaxe UserName\documentName). Mas a configuração das colunas de Proprietário pode ser implementada diretamente pelo usuário das seguintes maneiras:

1) Impersonação. Como o valor da coluna proprietário contém o valor do usuário que executa o código de impressão, há uma maneira de invocar a API de impressão Aspose.PDF dentro de outro contexto de usuário. Por exemplo, por favor, dê uma olhada na solução descrita aqui. Usando esta classe, o usuário pode alcançar um objetivo:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf(dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// Não produzir o diálogo de número de página ao imprimir
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName é um valor da coluna Proprietário na aplicação de spooler
    viewer.Close();
}
```
2) Usando a API Spooler e a rotina SetJob

O seguinte trecho de código mostra como imprimir algumas páginas de um arquivo PDF em modo Simplex e algumas páginas em modo Duplex.

```csharp
struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public System.Drawing.Printing.Duplex Mode { get; set; }
}
```

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

int printingJobIndex = 0;
string inPdf = dataDir + "input.pdf";
string output = dataDir;
IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

PrintingJobSettings printingJob1 = new PrintingJobSettings();
printingJob1.FromPage = 1;
printingJob1.ToPage = 3;
printingJob1.OutputFile = output + "35925_1_3.xps";
printingJob1.Mode = Duplex.Default;

printingJobs.Add(printingJob1);

PrintingJobSettings printingJob2 = new PrintingJobSettings();
printingJob2.FromPage = 4;
printingJob2.ToPage = 6;
printingJob2.OutputFile = output + "35925_4_6.xps";
printingJob2.Mode = Duplex.Simplex;

printingJobs.Add(printingJob2);

PrintingJobSettings printingJob3 = new PrintingJobSettings();
printingJob3.FromPage = 7;
printingJob3.ToPage = 7;
printingJob3.OutputFile = output + "35925_7.xps";
printingJob3.Mode = Duplex.Default;

printingJobs.Add(printingJob3);

PdfViewer viewer = new PdfViewer();

viewer.BindPdf(inPdf);
viewer.AutoResize = true;
viewer.AutoRotate = true;
viewer.PrintPageDialog = false;

PrinterSettings ps = new PrinterSettings();
PageSettings pgs = new PageSettings();

ps.PrinterName = "Microsoft XPS Document Writer";
ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
ps.PrintToFile = true;
ps.FromPage = printingJobs[printingJobIndex].FromPage;
ps.ToPage = printingJobs[printingJobIndex].ToPage;
ps.Duplex = printingJobs[printingJobIndex].Mode;
ps.PrintRange = PrintRange.SomePages;

pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);
viewer.EndPrint += (sender, args) =>
{
    if (++printingJobIndex < printingJobs.Count)
    {
        ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
        ps.FromPage = printingJobs[printingJobIndex].FromPage;
        ps.ToPage = printingJobs[printingJobIndex].ToPage;
        ps.Duplex = printingJobs[printingJobIndex].Mode;
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
};

viewer.PrintDocumentWithSettings(pgs, ps);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

