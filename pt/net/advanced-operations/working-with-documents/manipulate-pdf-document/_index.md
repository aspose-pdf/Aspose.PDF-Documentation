---
title: Manipular Documento PDF em C#
linktitle: Manipular Documento PDF
type: docs
weight: 20
url: /pt/net/manipulate-pdf-document/
description: Este artigo contém informações sobre como validar um Documento PDF para o Padrão PDF A, como trabalhar com TOC, como definir a data de expiração do PDF, entre outros.
keywords: "manipulate pdf c#"
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipular Documento PDF",
    "alternativeHeadline": "Como manipular arquivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, dotnet, manipulate pdf file",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo contém informações sobre como validar um Documento PDF para o Padrão PDF A, como trabalhar com TOC, como definir a data de expiração do PDF, entre outros."
}
</script>
## **Manipular Documento PDF em C#**

## Validar Documento PDF para o Padrão PDF A (A 1A e A 1B)

Para validar um documento PDF para compatibilidade com PDF/A-1a ou PDF/A-1b, use o método Validate da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Este método permite especificar o nome do arquivo no qual o resultado deve ser salvo e o tipo de validação necessário [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat) enumeração: PDF_A_1A ou PDF_A_1B.

{{% alert color="primary" %}}

O formato XML de saída é um formato personalizado da Aspose. O XML contém uma coleção de tags com o nome Problem; cada tag contém os detalhes de um problema específico. O atributo ObjectID da tag Problem representa o ID do objeto específico a que este problema está relacionado. O atributo Clause representa uma regra correspondente na especificação PDF.

{{% /alert %}}

O trecho de código a seguir também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O seguinte trecho de código mostra como validar um documento PDF para PDF/A-1A.
O seguinte trecho de código mostra como validar um documento PDF para PDF/A-1A.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validar PDF para PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

O seguinte trecho de código mostra como validar um documento PDF para PDF/A-1B.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validar PDF para PDF/A-1b
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```
{{% alert color="primary" %}}

Aspose.PDF para .NET pode ser usado para determinar se o documento carregado é um PDF válido e também [se está criptografado ou não](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). Para estender ainda mais as capacidades da classe Document, a propriedade *IsPdfaCompliant* foi adicionada para determinar se o arquivo de entrada é compatível com PDF/A e uma propriedade chamada *PdfaFormat* para identificar o formato PDF/A foram introduzidas.

{{% /alert %}}

## Trabalhando com TOC

### Adicionar TOC a um PDF Existente

A API Aspose.PDF permite que você adicione um índice de conteúdos tanto na criação de um PDF, quanto em um arquivo existente. A classe ListSection no namespace Aspose.Pdf.Generator permite que você crie um índice de conteúdos ao criar um PDF do zero. Para adicionar títulos, que são elementos do TOC, use a classe Aspose.Pdf.Generator.Heading.

Para adicionar um TOC a um arquivo PDF existente, use a classe Heading no namespace Aspose.Pdf.
Para adicionar um Sumário a um arquivo PDF existente, use a classe Heading no namespace Aspose.Pdf.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Carregar um arquivo PDF existente
Document doc = new Document(dataDir + "AddTOC.pdf");

// Obter acesso à primeira página do arquivo PDF
Page tocPage = doc.Pages.Insert(1);

// Criar objeto para representar as informações do Sumário
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Índice");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// Definir o título para o Sumário
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// Criar objetos string que serão usados como elementos do Sumário
string[] titles = new string[4];
titles[0] = "Primeira página";
titles[1] = "Segunda página";
titles[2] = "Terceira página";
titles[3] = "Quarta página";
for (int i = 0; i < 2; i++)
{
    // Criar objeto Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // Especificar a página de destino para o objeto de título
    heading2.DestinationPage = doc.Pages[i + 2];

    // Página de destino
    heading2.Top = doc.Pages[i + 2].Rect.Height;

    // Coordenada de destino
    segment2.Text = titles[i];

    // Adicionar título à página que contém o Sumário
    tocPage.Paragraphs.Add(heading2);
}
dataDir = dataDir + "TOC_out.pdf";
// Salvar o documento atualizado
doc.Save(dataDir);
```
### Definir diferentes Tipos de Líderes de Tabulação para Diferentes Níveis do TOC

Aspose.PDF também permite definir diferentes tipos de líderes de tabulação para diferentes níveis do TOC. Você precisa configurar a propriedade LineDash de FormatArray com o valor apropriado do enum TabLeaderType da seguinte forma.

```csharp
 string outFile = "TOC.pdf";

Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();

//definir LeaderType
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("Índice");
title.TextState.FontSize = 30;
tocInfo.Title = title;

//Adicionar a seção da lista à coleção de seções do documento Pdf
tocPage.TocInfo = tocInfo;
//Definir o formato dos quatro níveis da lista configurando as margens esquerdas
//e
//configurações de formato de texto de cada nível

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

//Criar uma seção no documento Pdf
Page page = doc.Pages.Add();

//Adicionar quatro títulos na seção
for (int Level = 1; Level <= 4; Level++)
{

    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "Título de Exemplo" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    //Adicionar o título no Índice.
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// salvar o Pdf

doc.Save(outFile);
```
### Ocultar Números de Página no Índice

Caso você não queira exibir números de página, juntamente com os títulos no índice, você pode usar a propriedade [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) da Classe [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) como false. Por favor, verifique o seguinte trecho de código para ocultar números de página no índice de conteúdos:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document doc = new Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Índice de Conteúdos");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
//Adicione a seção de lista à coleção de seções do documento Pdf
tocPage.TocInfo = tocInfo;
//Defina o formato dos quatro níveis de lista ajustando as margens esquerdas e
//configurações de formato de texto de cada nível

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = doc.Pages.Add();
//Adicione quatro títulos na seção
for (int Level = 1; Level != 5; Level++)

{ Heading heading2 = new Heading(Level); TextSegment segment2 = new TextSegment(); heading2.TocPage = tocPage; heading2.Segments.Add(segment2); heading2.IsAutoSequence = true; segment2.Text = "este é o título do nível " + Level; heading2.IsInList = true; page.Paragraphs.Add(heading2); }
doc.Save(outFile);
```
### Personalizar Números de Página ao adicionar TOC

É comum personalizar a numeração das páginas no TOC ao adicionar um TOC em um documento PDF. Por exemplo, pode ser necessário adicionar algum prefixo antes do número da página como P1, P2, P3, e assim por diante. Nesse caso, o Aspose.PDF para .NET oferece a propriedade PageNumbersPrefix da classe TocInfo que pode ser usada para personalizar os números das páginas conforme mostrado no seguinte exemplo de código.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824_out.pdf";
// Carregar um arquivo PDF existente
Document doc = new Document(inFile);
// Acessar a primeira página do arquivo PDF
Aspose.Pdf.Page tocPage = doc.Pages.Insert(1);
// Criar objeto para representar informações de TOC
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Índice");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// Definir o título para TOC
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i<doc.Pages.Count; i++)
{
    // Criar objeto Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // Especificar a página de destino para o objeto de cabeçalho
    heading2.DestinationPage = doc.Pages[i + 1];
    // Página de destino
    heading2.Top = doc.Pages[i + 1].Rect.Height;
    // Coordenada de destino
    segment2.Text = "Página " + i.ToString();
    // Adicionar cabeçalho à página contendo TOC
    tocPage.Paragraphs.Add(heading2);
}

// Salvar o documento atualizado
doc.Save(outFile);
```
## Como definir a data de expiração de um PDF

Aplicamos privilégios de acesso em arquivos PDF para que um determinado grupo de usuários possa acessar recursos/objetos específicos dos documentos PDF. Para restringir o acesso ao arquivo PDF, geralmente aplicamos criptografia e podemos ter a necessidade de definir a expiração do arquivo PDF, para que o usuário que acessa/visualiza o documento receba um aviso válido sobre a expiração do arquivo PDF.

Para realizar o requisito acima mencionado, podemos usar o objeto *JavascriptAction*. Por favor, dê uma olhada no seguinte trecho de código.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instanciar objeto Document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
// Adicionar página à coleção de páginas do arquivo PDF
doc.Pages.Add();
// Adicionar fragmento de texto à coleção de parágrafos do objeto de página
doc.Pages[1].Paragraphs.Add(new TextFragment("Olá Mundo..."));
// Criar objeto JavaScript para definir a data de expiração do PDF
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('O arquivo expirou. Você precisa de um novo.');");
// Definir JavaScript como ação de abertura do PDF
doc.OpenAction = javaScript;

dataDir = dataDir + "SetExpiryDate_out.pdf";
// Salvar Documento PDF
doc.Save(dataDir);
```
## Determinar o Progresso da Geração de Arquivo PDF

Um cliente solicitou que adicionássemos um recurso que permite aos desenvolvedores determinar o progresso da geração de arquivos PDF. Aqui está a resposta a essa solicitação.

O campo [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) da classe [DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) permite determinar como está indo a geração do PDF. O manipulador possui os seguintes tipos:

- DocSaveOptions.ConversionProgessEventHandler
- DocSaveOptions.ProgressEventHandlerInfo
- DocSaveOptions.ProgressEventType

Os trechos de código abaixo mostram como usar CustomerProgressHandler.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

dataDir = dataDir + "DetermineProgress_out.pdf";
pdfDocument.Save(dataDir, saveOptions);
Console.ReadLine();
```
```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Progresso da conversão : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalized:
            Console.WriteLine(String.Format("{0}  - Página fonte {1} de {2} analisada.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Layout da página de resultado {1} de {2} criado.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Página de resultado {1} de {2} exportada.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }

}
```
## Achatar PDF Preenchível em C#

Documentos PDF frequentemente incluem formulários com widgets preenchíveis interativos, como botões de rádio, caixas de seleção, caixas de texto, listas, etc. Para torná-los não editáveis para diversos fins de aplicação, precisamos achatar o arquivo PDF.
Aspose.PDF oferece a função para achatar seu PDF em C# com apenas algumas linhas de código:

```csharp
// Carregar o formulário PDF de origem
Document doc = new Document(dataDir + "input.pdf");

// Achatar PDF Preenchível 
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Salvar o documento atualizado
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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


