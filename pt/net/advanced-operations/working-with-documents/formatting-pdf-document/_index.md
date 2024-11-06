---
title: Formatação de Documento PDF usando C#
linktitle: Formatação de Documento PDF
type: docs
weight: 11
url: pt/net/formatting-pdf-document/
description: Crie e formate o Documento PDF com Aspose.PDF para .NET. Use o próximo trecho de código para resolver suas tarefas.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatação de Documento PDF usando C#",
    "alternativeHeadline": "Como formatar Documento PDF em .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, dotnet, formatar documento pdf",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Crie e formate o Documento PDF com Aspose.PDF para .NET. Use o próximo trecho de código para resolver suas tarefas."
}
</script>

## Formatação de Documento PDF

### Obter Propriedades da Janela do Documento e da Exibição de Páginas

Este tópico ajuda você a entender como obter propriedades da janela do documento, aplicativo visualizador e como as páginas são exibidas. Para definir essas propriedades:

Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Agora, você pode definir as propriedades do objeto Document, como:

- CenterWindow – Centraliza a janela do documento na tela. Padrão: false.
- Direction – Ordem de leitura. Isso determina como as páginas são organizadas quando exibidas lado a lado. Padrão: da esquerda para a direita.
- DisplayDocTitle – Exibe o título do documento na barra de título da janela do documento. Padrão: false (o título é exibido).
- HideMenuBar – Oculta ou exibe a barra de menu da janela do documento. Padrão: false (a barra de menu é exibida).
- HideToolBar – Oculta ou exibe a barra de ferramentas da janela do documento. Padrão: false (a barra de ferramentas é exibida).
- HideWindowUI – Oculta ou exibe elementos da janela do documento como barras de rolagem. Padrão: false (elementos da janela são exibidos).
- HideWindowUI – Ocultar ou exibir elementos da janela do documento como barras de rolagem.
- NonFullScreenPageMode – Como o documento é exibido quando não está em modo de página inteira.
- PageLayout – O layout da página.
- PageMode – Como o documento é exibido quando aberto pela primeira vez. As opções são mostrar miniaturas, tela cheia, mostrar painel de anexos.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

O seguinte trecho de código mostra como obter as propriedades usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// Obter diferentes propriedades do documento
// Posição da janela do documento - Padrão: false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);

// Ordem de leitura predominante; determina a posição da página
// Quando exibidas lado a lado - Padrão: L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);

// Se a barra de título da janela deve exibir o título do documento
// Se falso, a barra de título exibe o nome do arquivo PDF - Padrão: false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);

// Se redimensionar a janela do documento para ajustar o tamanho da
// Primeira página exibida - Padrão: false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);

// Se ocultar a barra de menu da aplicação visualizadora - Padrão: false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);

// Se ocultar a barra de ferramentas da aplicação visualizadora - Padrão: false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);

// Se ocultar elementos da interface do usuário como barras de rolagem
// E deixando apenas o conteúdo da página exibido - Padrão: false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);

// Modo de página do documento. Como exibir o documento ao sair do modo tela cheia.
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);

// O layout da página, por exemplo, página única, uma coluna
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);

// Como o documento deve ser exibido quando aberto
// Por exemplo, mostrar miniaturas, tela cheia, mostrar painel de anexos
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### Definir Propriedades da Janela do Documento e Exibição de Página

Este tópico explica como configurar as propriedades da janela do documento, aplicativo de visualização e exibição de página. Para configurar essas diferentes propriedades:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Defina as propriedades do objeto Document.
1. Salve o arquivo PDF atualizado usando o método Save.

Propriedades disponíveis são:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Cada uma é usada e descrita no código abaixo. O seguinte trecho de código mostra como configurar as propriedades usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Abrir documento
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// Definir diferentes propriedades do documento
// Especificar para posicionar a janela do documento - Padrão: false
pdfDocument.CenterWindow = true;

// Ordem de leitura predominante; determina a posição da página
// Quando exibido lado a lado - Padrão: L2R
pdfDocument.Direction = Direction.R2L;

// Especificar se a barra de título da janela deve exibir o título do documento
// Se falso, a barra de título exibe o nome do arquivo PDF - Padrão: false
pdfDocument.DisplayDocTitle = true;

// Especificar se redimensionar a janela do documento para caber no tamanho da
// Primeira página exibida - Padrão: false
pdfDocument.FitWindow = true;

// Especificar se ocultar a barra de menus do aplicativo visualizador - Padrão: false
pdfDocument.HideMenubar = true;

// Especificar se ocultar a barra de ferramentas do aplicativo visualizador - Padrão: false
pdfDocument.HideToolBar = true;

// Especificar se ocultar elementos da interface do usuário como barras de rolagem
// E deixar apenas o conteúdo da página exibido - Padrão: false
pdfDocument.HideWindowUI = true;

// Modo de página do documento. especificar como exibir o documento ao sair do modo tela cheia.
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;

// Especificar o layout da página, ou seja, página única, uma coluna
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;

// Especificar como o documento deve ser exibido quando aberto
// Ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// Salvar arquivo PDF atualizado
pdfDocument.Save(dataDir);
```
### Incorporando Fontes em um arquivo PDF existente

Leitores de PDF suportam [um núcleo de 14 fontes](https://en.wikipedia.org/wiki/PDF#Text) para que os documentos possam ser exibidos da mesma maneira, independentemente da plataforma em que o documento está sendo visualizado. Quando um PDF contém uma fonte que não é uma das 14 fontes principais, incorpore a fonte ao arquivo PDF para evitar a substituição da fonte.

Aspose.PDF para .NET suporta a incorporação de fontes em arquivos PDF existentes. Você pode incorporar uma fonte completa ou um subconjunto da fonte. Para incorporar a fonte, abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Em seguida, use a classe [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text) para incorporar a fonte no arquivo PDF. Para incorporar a fonte completa, use a propriedade IsEmbeded da classe Font; para usar um subconjunto da fonte, use a propriedade IsSubset.

{{% alert color="primary" %}}

Um subconjunto de fonte incorpora apenas os caracteres que são usados e é útil onde as fontes são usadas para frases curtas ou slogans, por exemplo, onde uma fonte corporativa é usada para um logotipo, mas não para o texto principal.
Um subconjunto de fontes incorpora apenas os caracteres que são utilizados e é útil onde as fontes são usadas para frases curtas ou slogans, por exemplo, onde uma fonte corporativa é usada para um logotipo, mas não para o texto principal.

{{% /alert %}}

O seguinte trecho de código mostra como incorporar uma fonte em um arquivo PDF.

### Incorporando Fontes Padrão Tipo 1

Alguns documentos PDF possuem fontes de um conjunto especial da Adobe. Fontes deste conjunto são chamadas de “Fontes Padrão Tipo 1”. Este conjunto inclui 14 fontes e a incorporação deste tipo de fontes requer o uso de sinalizadores especiais, ou seja [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). A seguir está o trecho de código que pode ser usado para obter um documento com todas as fontes incorporadas, incluindo Fontes Padrão Tipo 1:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Carregar um Documento PDF existente
Document pdfDocument = new Document(dataDir + "input.pdf");
// Definir a propriedade EmbedStandardFonts do documento
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
// Verificar se a fonte já está incorporada
if (!pageFont.IsEmbedded)
{
    pageFont.IsEmbedded = true;
}
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### Incorporando Fontes ao criar PDF

Se você precisar usar qualquer fonte além das 14 fontes principais suportadas pelo Adobe Reader, você deve incorporar a descrição da fonte ao gerar o arquivo PDF. Se as informações da fonte não forem incorporadas, o Adobe Reader as obterá do Sistema Operacional, se estiver instalado no sistema, ou construirá uma fonte substituta de acordo com o descritor de fonte no PDF.

>Observe que a fonte incorporada deve estar instalada na máquina hospedeira, ou seja, no caso do seguinte código, a fonte ‘Univers Condensed’ está instalada no sistema.

Usamos a propriedade IsEmbedded da classe Font para incorporar as informações da fonte no arquivo PDF. Definir o valor desta propriedade como ‘True’ incorporará o arquivo de fonte completo no PDF, sabendo que isso aumentará o tamanho do arquivo PDF. A seguir está o trecho de código que pode ser usado para incorporar as informações da fonte no PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instancia um objeto Pdf chamando seu construtor vazio
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// Cria uma seção no objeto Pdf
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" Este é um texto de exemplo usando fonte personalizada.");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// Salva o Documento PDF
doc.Save(dataDir);
```
### Definir Nome da Fonte Padrão ao Salvar PDF

Quando um documento PDF contém fontes que não estão disponíveis no próprio documento e no dispositivo, a API substitui essas fontes pela fonte padrão. Quando a fonte está disponível (está instalada no dispositivo ou está embutida no documento), o PDF resultante deve manter a mesma fonte (não deve ser substituída pela fonte padrão). O valor da fonte padrão deve conter o nome da fonte (não o caminho para os arquivos de fonte). Implementamos um recurso para definir o nome da fonte padrão ao salvar um documento como PDF. O seguinte trecho de código pode ser usado para definir a fonte padrão:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Carregar um documento PDF existente com fonte faltando
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // Especificar Nome da Fonte Padrão
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```

### Obter Todas as Fontes de um Documento PDF

Caso você queira obter todas as fontes de um documento PDF, você pode usar o método FontUtilities.GetAllFonts() fornecido na classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Por favor, verifique o trecho de código a seguir para obter todas as fontes de um documento PDF existente:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

### Obter Avisos para Substituição de Fonte

Aspose.PDF para .NET oferece métodos para obter notificações sobre substituição de fonte para lidar com casos de substituição de fonte. Os trechos de código abaixo mostram como usar a funcionalidade correspondente.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```
O método **OnFontSubstitution** é listado abaixo.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Console.WriteLine(string.Format("A fonte '{0}' foi substituída por outra fonte '{1}'",
oldFont.FontName, newFont.FontName));
```

### Melhorar a Incorporação de Fontes usando FontSubsetStrategy

A funcionalidade de incorporar as fontes como um subconjunto pode ser realizada usando a propriedade IsSubset, mas às vezes você deseja reduzir um conjunto de fontes totalmente incorporado apenas para os subconjuntos que são usados no documento. Aspose.Pdf.Document possui a propriedade FontUtilities que inclui o método SubsetFonts(FontSubsetStrategy subsetStrategy). No método SubsetFonts(), o parâmetro subsetStrategy ajuda a ajustar a estratégia de subconjunto. FontSubsetStrategy suporta as duas seguintes variantes de subconjunto de fontes.

- SubsetAllFonts - Isso irá criar um subconjunto de todas as fontes, usadas no documento.
- SubsetEmbeddedFontsOnly - Isso irá criar um subconjunto apenas daquelas fontes que estão totalmente incorporadas no documento.

O seguinte trecho de código mostra como definir FontSubsetStrategy:
O seguinte trecho de código mostra como configurar FontSubsetStrategy:

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// Todas as fontes serão incorporadas como subconjunto no documento em caso de SubsetAllFonts.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// O subconjunto de fontes será incorporado para fontes totalmente incorporadas, mas as fontes que não estão incorporadas no documento não serão afetadas.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```

### Obter-Definir Fator de Zoom de Arquivo PDF

Às vezes, você deseja determinar qual é o fator de zoom atual de um documento PDF. Com Aspose.Pdf, você pode descobrir o valor atual e também definir um.

A propriedade Destination da classe [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) permite que você obtenha o valor de zoom associado a um arquivo PDF.
A propriedade Destination da classe [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) permite que você obtenha o valor de zoom associado a um arquivo PDF.

#### Definir fator de zoom

O seguinte trecho de código mostra como definir o fator de zoom de um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instanciar novo objeto Document
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// Salvar o documento
doc.Save(dataDir);
```

#### Obter fator de zoom

O seguinte trecho de código mostra como obter o fator de zoom de um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Instanciar novo objeto Document
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// Criar objeto GoToAction
GoToAction action = doc.OpenAction as GoToAction;

// Obter o fator de zoom do arquivo PDF
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // Valor de zoom do documento;
```
### Configurando Propriedades Predefinidas do Diálogo de Impressão

Aspoose.PDF permite configurar as propriedades Predefinidas do Diálogo de Impressão de um documento PDF. Ele permite que você altere a propriedade DuplexMode de um documento PDF, que é definida como simplex por padrão. Isso pode ser alcançado usando duas metodologias diferentes, conforme mostrado abaixo.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```

### Configurando Propriedades Predefinidas do Diálogo de Impressão usando o Editor de Conteúdo PDF

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("O arquivo tem duplex flip short edge");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
}
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

