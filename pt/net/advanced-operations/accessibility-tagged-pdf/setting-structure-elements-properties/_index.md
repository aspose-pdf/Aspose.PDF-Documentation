---
title: Definindo Propriedades de Elementos Estruturais
linktitle: Definindo Propriedades de Elementos Estruturais
type: docs
weight: 30
url: /pt/net/setting-structure-elements-properties/
description: Você pode definir diferentes propriedades dos elementos estruturais em um documento PDF com Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Definindo Propriedades de Elementos Estruturais",
    "alternativeHeadline": "Como definir as propriedades dos elementos estruturais",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento PDF",
    "keywords": "pdf, c#, configurar estrutura de texto, configurar idioma, configurar título, configurar elemento de estrutura de Nota",
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
    "url": "/net/setting-structure-elements-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/setting-structure-elements-properties/"
    },
    "dateModified": "2022-02-04",
    "description": "Você pode definir diferentes propriedades dos elementos estruturais em um documento PDF com Aspose.PDF para .NET."
}
</script>
Para definir as propriedades dos elementos de estrutura em um Documento PDF Marcado, o Aspose.PDF oferece os métodos [CreateSectElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createsectelement) e [CreateHeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createheaderelement/index) da interface [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent).

O seguinte trecho de código mostra como definir as propriedades dos elementos de estrutura de um Documento PDF Marcado:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Definir Título e Idioma para o Documento
taggedContent.SetTitle("Documento PDF Marcado");
taggedContent.SetLanguage("en-US");

// Criar Elementos de Estrutura
StructureElement rootElement = taggedContent.RootElement;

SectElement sect = taggedContent.CreateSectElement();
rootElement.AppendChild(sect);

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
sect.AppendChild(h1);
h1.SetText("O Cabeçalho");

h1.Title = "Título";
h1.Language = "en-US";
h1.AlternativeText = "Texto Alternativo";
h1.ExpansionText = "Texto de Expansão";
h1.ActualText = "Texto Real";

// Salvar Documento PDF Marcado
document.Save(dataDir + "StructureElementsProperties.pdf");
```
changefreq: "monthly"
type: docs
## Definindo Elementos de Estrutura de Texto

Para definir elementos de estrutura de texto de um Documento PDF Marcado, Aspose.PDF oferece a classe [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). O seguinte trecho de código mostra como definir elementos de estrutura de texto de um Documento PDF Marcado:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Definir Título e Língua para o Documento
taggedContent.SetTitle("Documento PDF Marcado");
taggedContent.SetLanguage("en-US");

// Obter Elementos de Estrutura Raiz
StructureElement rootElement = taggedContent.RootElement;

ParagraphElement p = taggedContent.CreateParagraphElement();
// Definir Texto para Elemento de Estrutura de Texto
p.SetText("Parágrafo.");
rootElement.AppendChild(p);


// Salvar Documento PDF Marcado
document.Save(dataDir + "TextStructureElement.pdf");
```
## Definindo Elementos de Estrutura de Bloco de Texto

Para definir elementos de estrutura de bloco de texto de um Documento PDF Marcado, o Aspose.PDF oferece as classes [HeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/headerelement) e [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Você pode anexar objetos dessas classes como um filho do objeto [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement).
O seguinte trecho de código mostra como definir elementos de estrutura de bloco de texto de um Documento PDF Marcado:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Criar Documento PDF
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Definir Título e Idioma para o Documento
taggedContent.SetTitle("Documento PDF Marcado");
taggedContent.SetLanguage("en-US");

// Obter Elemento de Estrutura Raiz
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
h1.SetText("H1. Cabeçalho de Nível 1");
h2.SetText("H2. Cabeçalho de Nível 2");
h3.SetText("H3. Cabeçalho de Nível 3");
h4.SetText("H4. Cabeçalho de Nível 4");
h5.SetText("H5. Cabeçalho de Nível 5");
h6.SetText("H6. Cabeçalho de Nível 6");
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.AppendChild(p);

// Salvar Documento PDF Marcado
document.Save(dataDir + "TextBlockStructureElements.pdf");
```
## Definindo Elementos de Estrutura Inline

Para definir elementos de estrutura inline de um Documento PDF Marcado, Aspose.PDF oferece as classes [SpanElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/spanelement) e [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Você pode anexar objetos dessas classes como um filho de um objeto [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). O trecho de código a seguir mostra como definir elementos de estrutura inline de um Documento PDF Marcado:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Definir Título e Idioma para o Documento
taggedContent.SetTitle("Documento PDF Marcado");
taggedContent.SetLanguage("en-US");

// Obter Elemento de Estrutura Raiz
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

SpanElement spanH11 = taggedContent.CreateSpanElement();
spanH11.SetText("H1. ");
h1.AppendChild(spanH11);
SpanElement spanH12 = taggedContent.CreateSpanElement();
spanH12.SetText("Cabeçalho Nível 1");
h1.AppendChild(spanH12);

SpanElement spanH21 = taggedContent.CreateSpanElement();
spanH21.SetText("H2. ");
h2.AppendChild(spanH21);
SpanElement spanH22 = taggedContent.CreateSpanElement();
spanH22.SetText("Cabeçalho Nível 2");
h2.AppendChild(spanH22);

SpanElement spanH31 = taggedContent.CreateSpanElement();
spanH31.SetText("H3. ");
h3.AppendChild(spanH31);
SpanElement spanH32 = taggedContent.CreateSpanElement();
spanH32.SetText("Cabeçalho Nível 3");
h3.AppendChild(spanH32);

SpanElement spanH41 = taggedContent.CreateSpanElement();
spanH41.SetText("H4. ");
h4.AppendChild(spanH41);
SpanElement spanH42 = taggedContent.CreateSpanElement();
spanH42.SetText("Cabeçalho Nível 4");
h4.AppendChild(spanH42);

SpanElement spanH51 = taggedContent.CreateSpanElement();
spanH51.SetText("H5. ");
h5.AppendChild(spanH51);
SpanElement spanH52 = taggedContent.CreateSpanElement();
spanH52.SetText("Cabeçalho Nível 5");
h5.AppendChild(spanH52);

SpanElement spanH61 = taggedContent.CreateSpanElement();
spanH61.SetText("H6. ");
h6.AppendChild(spanH61);
SpanElement spanH62 = taggedContent.CreateSpanElement();
spanH62.SetText("Cabeçalho Nível 6");
h6.AppendChild(spanH62);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. ");
rootElement.AppendChild(p);
SpanElement span1 = taggedContent.CreateSpanElement();
span1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.AppendChild(span1);
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.AppendChild(span2);
SpanElement span3 = taggedContent.CreateSpanElement();
span3.SetText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.AppendChild(span3);
SpanElement span4 = taggedContent.CreateSpanElement();
span4.SetText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.AppendChild(span4);
SpanElement span5 = taggedContent.CreateSpanElement();
span5.SetText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.AppendChild(span5);
SpanElement span6 = taggedContent.CreateSpanElement();
span6.SetText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.AppendChild(span6);
SpanElement span7 = taggedContent.CreateSpanElement();
span7.SetText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.AppendChild(span7);
SpanElement span8 = taggedContent.CreateSpanElement();
span8.SetText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.AppendChild(span8);
SpanElement span9 = taggedContent.CreateSpanElement();
span9.SetText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.AppendChild(span9);
SpanElement span10 = taggedContent.CreateSpanElement();
span10.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.AppendChild(span10);

// Salvar Documento PDF Marcado
document.Save(dataDir + "InlineStructureElements.pdf");
```

## Configurando Nome de Tag Personalizado

Para configurar o nome de tag personalizado dos elementos de um Documento PDF Marcado, Aspose.PDF oferece o método [SetTag](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/methods/settag) da classe StructureElement para elementos. O seguinte trecho de código mostra como definir um nome de tag personalizado:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Definir Título e Idioma para o Documento
taggedContent.SetTitle("Documento Pdf Marcado");
taggedContent.SetLanguage("en-US");

// Criar Elementos de Estrutura Lógica
SectElement sect = taggedContent.CreateSectElement();
taggedContent.RootElement.AppendChild(sect);

ParagraphElement p1 = taggedContent.CreateParagraphElement();
ParagraphElement p2 = taggedContent.CreateParagraphElement();
ParagraphElement p3 = taggedContent.CreateParagraphElement();
ParagraphElement p4 = taggedContent.CreateParagraphElement();

p1.SetText("P1. ");
p2.SetText("P2. ");
p3.SetText("P3. ");
p4.SetText("P4. ");

p1.SetTag("P1");
p2.SetTag("Para");
p3.SetTag("Para");
p4.SetTag("Paragraph");

sect.AppendChild(p1);
sect.AppendChild(p2);
sect.AppendChild(p3);
sect.AppendChild(p4);

SpanElement span1 = taggedContent.CreateSpanElement();
SpanElement span2 = taggedContent.CreateSpanElement();
SpanElement span3 = taggedContent.CreateSpanElement();
SpanElement span4 = taggedContent.CreateSpanElement();

span1.SetText("Span 1.");
span2.SetText("Span 2.");
span3.SetText("Span 3.");
span4.SetText("Span 4.");

span1.SetTag("SPAN");
span2.SetTag("Sp");
span3.SetTag("Sp");
span4.SetTag("TheSpan");

p1.AppendChild(span1);
p2.AppendChild(span2);
p3.AppendChild(span3);
p4.AppendChild(span4);

// Salvar Documento Pdf Marcado
document.Save(dataDir + "CustomTag.pdf");
```
## Adicionando Elemento de Estrutura nos Elementos

**Este recurso é suportado pela versão 19.4 ou superior.**

Para configurar elementos de estrutura de link em um Documento PDF Marcado, Aspose.PDF oferece o método [CreateLinkElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createlinkelement) da interface [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). O seguinte trecho de código mostra como configurar elementos de estrutura em parágrafo com texto de Documento PDF Marcado:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "LinkStructureElements_Output.pdf";
string logFile = dataDir + "46035_log.xml";
string imgFile = dataDir + "google-icon-512.png";

// Criação de documento e obtenção de Conteúdo PDF Marcado
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// Configurando Título e Linguagem Natural para o documento
taggedContent.SetTitle("Exemplo de Elementos de Link");
taggedContent.SetLanguage("en-US");

// Obtendo o elemento de estrutura Raiz (elemento de estrutura do Documento)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
LinkElement link1 = taggedContent.CreateLinkElement();
p1.AppendChild(link1);
link1.Hyperlink = new WebHyperlink("http://google.com");
link1.SetText("Google");
link1.AlternateDescriptions = "Link para o Google";


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
LinkElement link2 = taggedContent.CreateLinkElement();
p2.AppendChild(link2);
link2.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Google");
link2.AppendChild(span2);
link2.AlternateDescriptions = "Link para o Google";


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
LinkElement link3 = taggedContent.CreateLinkElement();
p3.AppendChild(link3);
link3.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("G");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText("oogle");
link3.AppendChild(span31);
link3.SetText("-");
link3.AppendChild(span32);
link3.AlternateDescriptions = "Link para o Google";


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
LinkElement link4 = taggedContent.CreateLinkElement();
p4.AppendChild(link4);
link4.Hyperlink = new WebHyperlink("http://google.com");
link4.SetText("O link de várias linhas: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google");
link4.AlternateDescriptions = "Link para o Google (múltiplas linhas)";


ParagraphElement p5 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p5);
LinkElement link5 = taggedContent.CreateLinkElement();
p5.AppendChild(link5);
link5.Hyperlink = new WebHyperlink("http://google.com");
FigureElement figure5 = taggedContent.CreateFigureElement();
figure5.SetImage(imgFile, 1200);
figure5.AlternativeText = "Ícone do Google";
StructureAttributes linkLayoutAttributes = link5.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
placementAttribute.SetNameValue(AttributeName.Placement_Block);
linkLayoutAttributes.SetAttribute(placementAttribute);
link5.AppendChild(figure5);
link5.AlternateDescriptions = "Link para o Google";


// Salvar Documento PDF Marcado
document.Save(outFile);

// Verificando conformidade com PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Conformidade com PDF/UA: {0}", isPdfUaCompliance));
```
## Definindo Elemento de Estrutura de Link

**Este recurso é suportado pela versão 19.4 ou superior.**

A API Aspose.PDF para .NET também permite que você adicione elementos de estrutura de link. O trecho de código a seguir mostra como adicionar um elemento de estrutura de link em um Documento PDF com Tags:

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
string logFile = dataDir + "46144_log.xml";

// Criação do documento e obtenção de Conteúdo PDF com Tags
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// Definindo Título e Linguagem Natural para o documento
taggedContent.SetTitle("Exemplo de Elementos de Texto");
taggedContent.SetLanguage("en-US");

// Obtendo o elemento de estrutura raiz (elemento de estrutura do documento)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
SpanElement span11 = taggedContent.CreateSpanElement();
span11.SetText("Span_11");
SpanElement span12 = taggedContent.CreateSpanElement();
span12.SetText(" e Span_12.");
p1.SetText("Parágrafo com ");
p1.AppendChild(span11);
p1.AppendChild(span12);


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
SpanElement span21 = taggedContent.CreateSpanElement();
span21.SetText("Span_21");
SpanElement span22 = taggedContent.CreateSpanElement();
span22.SetText("Span_22.");
p2.AppendChild(span21);
p2.SetText(" e ");
p2.AppendChild(span22);


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("Span_31");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText(" e Span_32");
p3.AppendChild(span31);
p3.AppendChild(span32);
p3.SetText(".");


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
SpanElement span41 = taggedContent.CreateSpanElement();
SpanElement span411 = taggedContent.CreateSpanElement();
span411.SetText("Span_411, ");
span41.SetText("Span_41, ");
span41.AppendChild(span411);
SpanElement span42 = taggedContent.CreateSpanElement();
SpanElement span421 = taggedContent.CreateSpanElement();
span421.SetText("Span 421 e ");
span42.AppendChild(span421);
span42.SetText("Span_42");
p4.AppendChild(span41);
p4.AppendChild(span42);
p4.SetText(".");


// Salvar Documento PDF com Tags
document.Save(outFile);

// Verificando conformidade com PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Conformidade com PDF/UA: {0}", isPdfUaCompliance));
```
## Estrutura do Elemento de Nota de Configuração

Aspose.PDF para API .NET também permite que você adicione [NoteElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/noteelement) em um documento PDF etiquetado. O trecho de código a seguir mostra como adicionar elemento de nota em Documento PDF Etiquetado:

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "45929_doc.pdf";
string logFile = dataDir + "45929_log.xml";

// Criar Documento Pdf
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("Exemplo de Elementos de Nota");
taggedContent.SetLanguage("en-US");

// Adicionar Elemento de Parágrafo
ParagraphElement paragraph = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(paragraph);

// Adicionar NoteElement
NoteElement note1 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note1);
note1.SetText("Nota com ID gerado automaticamente. ");

// Adicionar NoteElement
NoteElement note2 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note2);
note2.SetText("Nota com ID = 'note_002'. ");
note2.SetId("note_002");

// Adicionar NoteElement
NoteElement note3 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note3);
note3.SetText("Nota com ID = 'note_003'. ");
note3.SetId("note_003");

// Deve lançar exceção - Aspose.Pdf.Tagged.TaggedException : Elemento de estrutura com ID='note_002' já existe
//note3.SetId("note_002");

// O documento resultante não está em conformidade com PDF/UA se ClearId() for usado para Elemento de Estrutura de Nota
//note3.ClearId();


// Salvar Documento PDF Etiquetado
document.Save(outFile);

// Verificação de conformidade com PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Conformidade com PDF/UA: {0}", isPdfUaCompliance));
```
## Configurando Idioma e Título

**Este recurso é suportado pela versão 19.6 ou superior.**

Aspose.PDF para API .NET também permite que você defina o idioma e o título para um documento de acordo com a especificação PDF/UA. O idioma pode ser configurado tanto para o documento inteiro quanto para seus elementos estruturais separados. O seguinte trecho de código mostra como definir idioma e título em Documento PDF Marcado:

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Document document = new Document();
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Obter TaggedContent
Tagged.ITaggedContent taggedContent = document.TaggedContent;

// Definir Título e Idioma
taggedContent.SetTitle("Documento Marcado de Exemplo");
taggedContent.SetLanguage("en-US");

// Cabeçalho (en-US, herdado do documento)
LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
h1.SetText("Frase em diferentes idiomas");
taggedContent.RootElement.AppendChild(h1);

// Parágrafo (Inglês)
LogicalStructure.ParagraphElement pEN = taggedContent.CreateParagraphElement();
pEN.SetText("Olá, Mundo!");
pEN.Language = "en-US";
taggedContent.RootElement.AppendChild(pEN);

// Parágrafo (Alemão)
LogicalStructure.ParagraphElement pDE = taggedContent.CreateParagraphElement();
pDE.SetText("Hallo Welt!");
pDE.Language = "de-DE";
taggedContent.RootElement.AppendChild(pDE);

// Parágrafo (Francês)
LogicalStructure.ParagraphElement pFR = taggedContent.CreateParagraphElement();
pFR.SetText("Bonjour le monde!");
pFR.Language = "fr-FR";
taggedContent.RootElement.AppendChild(pFR);

// Parágrafo (Espanhol)
LogicalStructure.ParagraphElement pSP = taggedContent.CreateParagraphElement();
pSP.SetText("¡Hola Mundo!");
pSP.Language = "es-ES";
taggedContent.RootElement.AppendChild(pSP);

// Salvar Documento PDF Marcado
document.Save(dataDir + "SetupLanguageAndTitle.pdf");
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

