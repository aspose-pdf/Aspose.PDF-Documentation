---
title: Usando Anotação de Texto para PDF
linktitle: Anotação de Texto
type: docs
weight: 10
url: /pt/net/text-annotation/
description: Aspose.PDF para .NET permite que você Adicione, Obtenha e Delete Anotações de Texto do seu documento PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Usando Anotação de Texto para PDF",
    "alternativeHeadline": "Como adicionar Anotação de Texto em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, anotação de texto",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET permite que você Adicione, Obtenha e Delete Anotações de Texto do seu documento PDF."
}
</script>

## Como adicionar Anotação de Texto em um arquivo PDF existente

O trecho de código a seguir também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Uma Anotação de Texto é uma anotação vinculada a uma localização específica no documento PDF. Quando fechada, a anotação é exibida como um ícone; quando aberta, deve exibir uma janela pop-up contendo o texto da nota na fonte e tamanho escolhidos pelo leitor.

As anotações estão contidas na coleção [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) de uma determinada Página. Esta coleção contém as anotações apenas para aquela página individual; cada página possui sua própria coleção de Annotations.

Para adicionar uma anotação a uma página específica, adicione-a à coleção Annotations dessa página com o método [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add).

1. Primeiro, crie uma anotação que você deseja adicionar ao PDF.
1. Em seguida, abra o PDF de entrada.
1.
O seguinte trecho de código mostra como adicionar uma anotação em uma página de PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// Criar anotação
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "Título da Anotação de Exemplo";
textAnnotation.Subject = "Assunto de Exemplo";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "Conteúdos de exemplo para a anotação";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// Adicionar anotação na coleção de anotações da página
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// Salvar arquivo de saída
pdfDocument.Save(dataDir);
```
## Como adicionar Anotação Pop-up

Uma Anotação Pop-up exibe texto em uma janela pop-up para entrada e edição. Ela não deve aparecer sozinha, mas está associada a uma anotação de marcação, sua anotação pai, e deve ser usada para editar o texto do pai.

Ela não deve ter fluxo de aparência ou ações associadas próprias e deve ser identificada pela entrada Popup no dicionário de anotação do pai.

O seguinte trecho de código mostra como adicionar [Anotação Pop-up](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) em uma página PDF usando um exemplo de adição de uma [Anotação de Linha](/pdf/pt/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file) do pai.

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // O caminho para o diretório de documentos.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // Carregar o arquivo PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // Criar Anotação de Linha
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // Adicionar anotação à página
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
## Como adicionar (ou criar) nova Anotação de Texto Livre

Uma anotação de texto livre exibe texto diretamente na página. O método [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) permite criar esse tipo de anotação. No trecho a seguir, adicionamos uma anotação de texto livre acima da primeira ocorrência da string.

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);

    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Demonstração de Texto Livre", 1); // último parâmetro é o número da página
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

### Definir Propriedade de Chamada para Anotação de Texto Livre
### Definir Propriedade de Chamada para FreeTextAnnotation

Para uma configuração mais flexível da anotação no documento PDF, Aspose.PDF para .NET fornece a propriedade [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) da classe [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) que permite especificar um Array de pontos da linha de chamada. O seguinte trecho de código mostra como usar essa funcionalidade:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### Defina a Propriedade de Chamada para Arquivo XFDF

Se você usa importação de arquivo XFDF, por favor use o nome callout-line em vez de apenas Callout. O seguinte trecho de código mostra como usar essa funcionalidade:

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document( dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

O seguinte método está sendo usado para CreateXfdf:

```csharp
/// <summary>
/// Criar XFDF
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">Este é um exemplo</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```
### Tornar a Anotação de Texto Livre Invisível

Às vezes, é necessário criar uma marca d'água que não seja visível no documento ao visualizá-lo, mas que deve ser visível quando o documento é impresso. Use as flags de anotação para esse propósito. O seguinte trecho de código mostra como.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// Salvar arquivo de saída
doc.Save(dataDir);
```
### Definir Formatação de FreeTextAnnotation

Esta parte analisa como formatar o texto em uma anotação de texto livre.

As anotações estão contidas na coleção [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) de um objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Ao adicionar uma [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) a um documento PDF, você pode especificar as informações de formatação, como fonte, tamanho, cor e assim por diante, usando a classe [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index). Também é possível especificar as informações de formatação usando a propriedade TextStyle. Além disso, você pode atualizar a formatação de qualquer FreeTextAnnotation já no documento PDF.

A classe [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) suporta trabalhar com a entrada de estilo padrão.

A classe [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) suporta o trabalho com a entrada de estilo padrão.

- A propriedade FontName obtém ou define o nome da fonte (string).
- A propriedade FontSize obtém e define o tamanho padrão do texto (double).
- A propriedade System.Drawing.Color obtém e define a cor do texto (color).
- A propriedade TextAlignment obtém e define o alinhamento do texto da anotação (alignment).

O seguinte trecho de código mostra como adicionar uma FreeTextAnnotation com formatação de texto específica.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

Quando você altera o conteúdo ou o estilo de texto de uma anotação de texto livre, a aparência da anotação é regenerada para refletir as alterações.

{{% /alert %}}

### Riscar Palavras usando StrikeOutAnnotation

Aspose.PDF para .NET permite adicionar, deletar e atualizar anotações em documentos PDF.
Aspose.PDF para .NET permite adicionar, excluir e atualizar anotações em documentos PDF.

Para riscar um certo TextFragment:

1. Procure por um TextFragment no arquivo PDF.
1. Obtenha as coordenadas do objeto TextFragment.
1. Use as coordenadas para instanciar um objeto StrikeOutAnnotation.

O seguinte trecho de código mostra como procurar por um TextFragment específico e adicionar um StrikeOutAnnotation a esse objeto.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

Este recurso é suportado pela versão 19.6 ou superior.

{{% /alert %}}

## Excluir Todas as Anotações de uma Página do Arquivo PDF

A coleção [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) de um objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) contém todas as anotações para aquela página específica.
Um objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) possui uma coleção [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) que contém todas as anotações para aquela página específica.

O seguinte trecho de código mostra como deletar todas as anotações de uma página específica.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// Deletar anotação específica
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```

## Deletar Anotação Específica de um Arquivo PDF

{{% alert color="primary" %}}

Você pode verificar a qualidade do Aspose.PDF e obter os resultados online neste link:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF permite que você remova uma Anotação específica de um arquivo PDF. Este tópico explica como fazer isso.

Para deletar uma anotação específica de um PDF, chame o método Delete da [coleção AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). Esta coleção pertence ao objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). O método Delete requer o índice da anotação que você deseja deletar. Então, salve o arquivo PDF atualizado. O seguinte trecho de código mostra como deletar uma anotação específica.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// Deletar anotação específica
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```
## Obter Todas as Anotações de uma Página do Documento PDF

Aspose.PDF permite que você obtenha anotações de um documento inteiro ou de uma página específica. Para obter todas as anotações de uma página em um documento PDF, percorra a coleção [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) dos recursos da página desejada. O seguinte trecho de código mostra como obter todas as anotações de uma página.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// Percorrer todas as anotações
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // Obter propriedades da anotação
    Console.WriteLine("Título : {0} ", annotation.Title);
    Console.WriteLine("Assunto : {0} ", annotation.Subject);
    Console.WriteLine("Conteúdo : {0} ", annotation.Contents);
}
```
Por favor, note que para obter todas as anotações de todo o PDF, você deve percorrer a coleção da classe PageCollection do documento antes de navegar pela coleção da classe AnnotationCollection. Você pode obter cada anotação da coleção em um tipo de anotação base chamado classe MarkupAnnotation e, em seguida, mostrar suas propriedades.

## Obter Anotação Particular de um Arquivo PDF

As anotações estão associadas a páginas individuais e armazenadas na coleção [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) do objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
As anotações estão associadas a páginas individuais e armazenadas na coleção [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) de um objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// Obter uma anotação específica
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// Obter propriedades da anotação
Console.WriteLine("Título : {0} ", textAnnotation.Title);
Console.WriteLine("Assunto : {0} ", textAnnotation.Subject);
Console.WriteLine("Conteúdos : {0} ", textAnnotation.Contents);
```

## Obter Recurso de Anotação

Aspose.PDF permite que você obtenha um recurso de anotação de um documento inteiro, ou de uma página específica.
Aspose.PDF permite que você obtenha um recurso de anotação de um documento inteiro ou de uma página específica.

```csharp
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document doc = new Document(dataDir + "AddAnnotation.pdf");
// Criar anotação
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// Salvar Documento
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// Abrir documento
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

// Obter ação da anotação
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

// Obter rendição da ação de rendição
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

// Clipe de Mídia
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
// Os dados da mídia estão acessíveis em FileSpecification.Contents
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Biblioteca .NET",
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

