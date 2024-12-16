---
title: Trabalhando com Ações em PDF
linktitle: Ações
type: docs
weight: 20
url: /pt/net/actions/
description: Esta seção explica como adicionar ações ao documento e campos de formulário programaticamente com C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Ações em PDF",
    "alternativeHeadline": "Como adicionar Ações em PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "geração de documentos em PDF",
    "keywords": "pdf, c#, ações em pdf",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção explica como adicionar ações ao documento e campos de formulário programaticamente com C#."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Adicionar Hiperlink em um Arquivo PDF

É possível adicionar hiperlinks a arquivos PDF, seja para permitir que os leitores naveguem para outra parte do PDF, ou para conteúdo externo.

Para adicionar hiperlinks da web a documentos PDF:

1. Crie um objeto da Classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Obtenha a Classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) na qual você deseja adicionar o link.
3. Crie um objeto [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) usando os objetos Page e [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle). O objeto retângulo é usado para especificar a localização na página onde o link deve ser adicionado.
4. Defina a propriedade Action para o objeto [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) que especifica a localização do URI remoto.
5.
1. Para adicionar um texto livre:

- Instancie um objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation). Ele também aceita objetos Page e Rectangle como argumento, então é possível fornecer os mesmos valores especificados contra o construtor LinkAnnotation.
- Usando a propriedade Contents do objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), especifique a string que deve ser exibida no PDF de saída.
- Opcionalmente, defina a largura da borda de ambos os objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) e FreeTextAnnotation para 0, para que eles não apareçam no documento PDF.
- Uma vez que os objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) e [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) tenham sido definidos, adicione esses links à coleção de Anotações do objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- Uma vez que os objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) e [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) tenham sido definidos, adicione esses links à coleção de Anotações do objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- Finalmente, salve o PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

O seguinte trecho de código mostra como adicionar um hiperlink a um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Abrir documento
Document document = new Document(dataDir + "AddHyperlink.pdf");
// Criar link
Page page = document.Pages[1];
// Criar objeto de anotação de link
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// Criar objeto de borda para LinkAnnotation
Border border = new Border(link);
// Definir o valor da largura da borda como 0
border.Width = 0;
// Definir a borda para LinkAnnotation
link.Border = border;
// Especificar o tipo de link como URI remoto
link.Action = new GoToURIAction("www.aspose.com");
// Adicionar anotação de link à coleção de anotações da primeira página do arquivo PDF
page.Annotations.Add(link);

// Criar anotação de texto livre
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// String a ser adicionada como texto livre
textAnnotation.Contents = "Link para o site da Aspose";
// Definir a borda para anotação de texto livre
textAnnotation.Border = border;
// Adicionar anotação de texto livre à coleção de anotações da primeira página do Documento
document.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddHyperlink_out.pdf";
// Salvar documento atualizado
document.Save(dataDir);
```
## Criar Hiperlink para páginas no mesmo PDF

Aspose.PDF para .NET oferece uma ótima funcionalidade para criação de PDFs, bem como sua manipulação. Ele também oferece a funcionalidade de adicionar links às páginas do PDF e um link pode direcionar para páginas em outro arquivo PDF, uma URL da web, link para iniciar um aplicativo ou até mesmo link para páginas no mesmo arquivo PDF. Para adicionar hiperlinks locais (links para páginas no mesmo arquivo PDF), uma classe chamada [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) é adicionada ao namespace Aspose.PDF e esta classe possui uma propriedade chamada TargetPageNumber, que é usada para especificar a página de destino para o hiperlink.

Para adicionar o hiperlink local, precisamos criar um TextFragment para que o link possa ser associado ao TextFragment. A classe [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) tem uma propriedade chamada Hyperlink que é usada para associar uma instância LocalHyperlink. O seguinte trecho de código mostra os passos para realizar essa exigência.

```csharp
```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Criar instância de Documento
Document doc = new Document();
// Adicionar página à coleção de páginas do arquivo PDF
Page page = doc.Pages.Add();
// Criar instância de Fragmento de Texto
Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("teste de número de página de link para a página 7");
// Criar instância de hyperlink local
Aspose.Pdf.LocalHyperlink link = new Aspose.Pdf.LocalHyperlink();
// Definir página alvo para a instância de link
link.TargetPageNumber = 7;
// Definir hyperlink para Fragmento de Texto
text.Hyperlink = link;
// Adicionar texto à coleção de parágrafos da Página
page.Paragraphs.Add(text);
// Criar nova instância de Fragmento de Texto
text = new TextFragment("teste de número de página de link para a página 1");
// Fragmento de Texto deve ser adicionado em nova página
text.IsInNewPage = true;
// Criar outra instância de hyperlink local
link = new LocalHyperlink();
// Definir página alvo para o segundo hyperlink
link.TargetPageNumber = 1;
// Definir link para o segundo Fragmento de Texto
text.Hyperlink = link;
// Adicionar texto à coleção de parágrafos do objeto de página
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateLocalHyperlink_out.pdf";
// Salvar documento atualizado
doc.Save(dataDir);
```
## Obter Destino de Hiperlink (URL) em PDF

Links são representados como anotações em um arquivo PDF e podem ser adicionados, atualizados ou excluídos. O Aspose.PDF para .NET também suporta a obtenção do destino (URL) do hiperlink em um arquivo PDF.

Para obter a URL de um link:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Obtenha a [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) da qual você deseja extrair os links.
3. Use a classe [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) para extrair todos os objetos [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) da página especificada.
4. Passe o objeto [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) para o método Accept do objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1.
1. Finalmente, extraia a ação LinkAnnotation como GoToURIAction.

O seguinte trecho de código mostra como obter destinos de hiperlink (URL) de um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Carregar o arquivo PDF
Document document = new Document(dataDir + "input.pdf");

// Percorrer todas as páginas do PDF
foreach (Aspose.Pdf.Page page in document.Pages)
{
    // Obter as anotações de link da página específica
    AnnotationSelector selector = new AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // Criar lista contendo todos os links
    IList<Annotation> list = selector.Selected;
    // Iterar sobre cada item na lista
    foreach (LinkAnnotation a in list)
    {
        // Imprimir a URL de destino
        Console.WriteLine("\nDestino: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
    }
}
```
## Obter Texto do Hiperlink

Um hiperlink possui duas partes: o texto que aparece no documento e o URL de destino. Em alguns casos, é o texto, e não o URL, que precisamos.

Texto e anotações/ações em um arquivo PDF são representados por entidades diferentes. O texto em uma página é apenas um conjunto de palavras e caracteres, enquanto as anotações trazem alguma interatividade, como aquela inerente a um hiperlink.

Para encontrar o conteúdo do URL, você precisa trabalhar tanto com a anotação quanto com o texto. O objeto [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) por si só não possui texto, mas fica sob o texto na página. Assim, para obter o texto, a Annotation fornece os limites do URL, enquanto o objeto Text fornece os conteúdos do URL. Veja o seguinte trecho de código.

```csharp
  {
        public static void Run()
        {
            try
            {
                // ExStart:GetHyperlinkText
                // O caminho para o diretório dos documentos.
                string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
                // Carregar o arquivo PDF
                Document document = new Document(dataDir + "input.pdf");
                // Iterar por cada página do PDF
                foreach (Page page in document.Pages)
                {
                    // Mostrar anotação de link
                    ShowLinkAnnotations(page);
                }
                // ExEnd:GetHyperlinkText
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // ExStart:ShowLinkAnnotations
        public static void ShowLinkAnnotations(Page page)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annot in page.Annotations)
            {
                if (annot is LinkAnnotation)
                {
                    // Imprimir o URL de cada Anotação de Link
                    Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
                    TextAbsorber absorber = new TextAbsorber();
                    absorber.TextSearchOptions.LimitToPageBounds = true;
                    absorber.TextSearchOptions.Rectangle = annot.Rect;
                    page.Accept(absorber);
                    string extractedText = absorber.Text;
                    // Imprimir o texto associado ao hiperlink
                    Console.WriteLine(extractedText);
                }

            }
        }
        // ExEnd:ShowLinkAnnotations
    }
}
```
## Remover Ação de Abertura de Documento de um Arquivo PDF

[Como Especificar a Página do PDF ao Visualizar o Documento](#how-to-specify-pdf-page-when-viewing-document) explicou como instruir um documento a abrir em uma página diferente da primeira. Ao concatenar vários documentos, e um ou mais têm uma ação GoTo definida, provavelmente você vai querer removê-las. Por exemplo, se combinar dois documentos e o segundo tem uma ação GoTo que leva você para a segunda página, o documento resultante abrirá na segunda página do segundo documento em vez da primeira página do documento combinado. Para evitar esse comportamento, remova o comando de ação de abertura.

Para remover uma ação de abertura:

1. Defina a propriedade [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) do objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) como nula.
1. Salve o PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) do objeto Document.

O seguinte trecho de código mostra como remover uma ação de abertura de documento do arquivo PDF.
O seguinte trecho de código mostra como remover uma ação de abertura de documento de um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Abrir documento
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// Remover ação de abertura do documento
document.OpenAction = null;
dataDir = dataDir + "RemoveOpenAction_out.pdf";
// Salvar documento atualizado
document.Save(dataDir);
```

## Como Especificar a Página do PDF ao Visualizar o Documento {#how-to-specify-pdf-page-when-viewing-document}

Ao visualizar arquivos PDF em um visualizador de PDFs, como o Adobe Reader, os arquivos geralmente são abertos na primeira página. No entanto, é possível definir o arquivo para abrir em uma página diferente.

A classe [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) permite que você especifique uma página em um arquivo PDF que você deseja abrir.
A classe [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) permite que você especifique uma página em um arquivo PDF que deseja abrir.

```csharp
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Carregar o arquivo PDF
Document doc = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// Obter a instância da segunda página do documento
Page page2 = doc.Pages[2];
// Criar a variável para definir o fator de zoom da página de destino
double zoom = 1;
// Criar instância de GoToAction
GoToAction action = new GoToAction(doc.Pages[2]);
// Ir para a 2ª página
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// Definir a ação de abertura do documento
doc.OpenAction = action;
// Salvar o documento atualizado
doc.Save(dataDir + "goto2page_out.pdf");
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

