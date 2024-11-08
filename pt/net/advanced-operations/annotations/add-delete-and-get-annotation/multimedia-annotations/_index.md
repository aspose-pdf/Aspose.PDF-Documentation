---
title: Anotação Multimídia em PDF usando C#
linktitle: Anotação Multimídia
type: docs
weight: 40
url: /pt/net/multimedia-annotation/
description: Aspose.PDF para .NET permite que você adicione, obtenha e exclua a anotação multimídia do seu documento PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotação Multimídia em PDF usando C#",
    "alternativeHeadline": "Como adicionar Anotação Multimídia em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, anotação multimídia, anotação de tela, anotação de som, anotação de widget, anotação 3D",
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
    "url": "/net/multimedia-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/multimedia-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF para .NET permite que você adicione, obtenha e exclua a anotação multimídia do seu documento PDF."
}
</script>

As anotações em um documento PDF estão contidas na coleção de Anotações de um objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Esta coleção contém todas as anotações apenas para aquela página específica: cada página tem sua própria coleção de Anotações. Para adicionar uma anotação a uma página específica, adicione-a à coleção de Anotações dessa página usando o método Add.

Use a classe [ScreenAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/screenannotation) no namespace Aspose.PDF.InteractiveFeatures.Annotations para incluir arquivos SWF como anotações em um documento PDF. Uma anotação de tela especifica uma região de uma página na qual clipes de mídia podem ser reproduzidos.

Quando você precisar adicionar um link de vídeo externo em um documento PDF, você pode usar [MovieAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/movieannotation). Uma Anotação de Filme contém gráficos animados e som para serem apresentados na tela do computador e através dos alto-falantes.

Uma [Sound Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) deve ser análoga a uma anotação de texto, exceto que, em vez de uma nota de texto, contém som gravado do microfone do computador ou importado de um arquivo.
Uma [Anotação de Som](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/soundannotation) deve ser análoga a uma anotação de texto, exceto que, em vez de uma nota de texto, contém som gravado do microfone do computador ou importado de um arquivo.

No entanto, quando há uma necessidade de embutir mídia dentro de um documento PDF, você precisa usar [RichMediaAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/richmediaannotation).

Os seguintes métodos/propriedades da classe RichMediaAnnotation podem ser usados.

- Stream CustomPlayer { set; }: Permite definir o player usado para reproduzir vídeo.
- string CustomFlashVariables { set; }: Permite definir variáveis que são passadas para a aplicação flash. Esta linha é um conjunto de pares "chave=valor" que são separados com '&'.
- void AddCustomData(strig name, Stream data): Adiciona dados adicionais para o player. Por exemplo source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: Evento ativa player; valores possíveis são Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Define os dados de vídeo/áudio a serem reproduzidos.
- void SetContent(Stream stream, string name): Define dados de vídeo/áudio a serem reproduzidos.
- void Update(): Crie uma estrutura de dados da anotação. Este método deve ser chamado por último.
- void SetPoster(Stream): Define o pôster do vídeo, ou seja, imagem exibida quando o player não está ativo.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Adicionar Anotação de Tela

O seguinte trecho de código mostra como adicionar uma Anotação de Tela em um arquivo PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.IO;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleMultimediaAnnotation
    {
        // O caminho para o diretório de documentos.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddScreenAnnotation()
        {
            // Carrega o arquivo PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "input.swf");
            // Cria Anotação de Tela
            var screenAnnotation = new ScreenAnnotation(
                document.Pages[1],
                new Rectangle(170, 190, 470, 380),
                mediaFile);
            document.Pages[1].Annotations.Add(screenAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_swf.pdf"));
        }
    }
}
```
## Adicionar Anotação de Som

O seguinte trecho de código mostra como adicionar uma Anotação de Som a um arquivo PDF:

```csharp
        public static void AddSoundAnnotation()
        {
            // Carregar o arquivo PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));

            var mediaFile = System.IO.Path.Combine(_dataDir, "file_example_WAV_1MG.wav");
            // Criar Anotação de Som
            var soundAnnotation = new SoundAnnotation(
                document.Pages[1],
                new Rectangle(20, 700, 60, 740),
                mediaFile)
            {
                Color = Color.Blue,
                Title = "John Smith",
                Subject = "Demonstração de Anotação de Som",
                Popup = new PopupAnnotation(document)
            };

            document.Pages[1].Annotations.Add(soundAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_wav.pdf"));
        }
```

## Adicionar RichMediaAnnotation

O seguinte trecho de código mostra como adicionar uma RichMediaAnnotation a um arquivo PDF:
O seguinte trecho de código mostra como adicionar RichMediaAnnotation a um arquivo PDF:

```csharp
        public static void AddRichMediaAnnotation()
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
            var pathToAdobeApp = @"C:\Program Files (x86)\Adobe\Acrobat 2017\Acrobat\Multimedia Skins";
            Page page = doc.Pages.Add();
            //dê um nome aos dados do vídeo. Esses dados serão incorporados ao documento com esse nome e referenciados a partir das variáveis flash por esse nome.
            //videoName não deve conter o caminho para o arquivo; isso é mais um "chave" para acessar dados dentro do documento PDF
            const string videoName = "file_example_MP4_480_1_5MG.mp4";
            const string posterName = "file_example_MP4_480_1_5MG_poster.jpg";
            //também usamos skin para o player de vídeo
            string skinName = "SkinOverAllNoFullNoCaption.swf";
            RichMediaAnnotation rma = new RichMediaAnnotation(page, new Aspose.Pdf.Rectangle(100, 500, 300, 600))
            {
                //aqui devemos especificar o fluxo contendo o código do player de vídeo
                CustomPlayer = new FileStream(Path.Combine(pathToAdobeApp,"Players","Videoplayer.swf"), FileMode.Open, FileAccess.Read),
                //compõe a linha de variáveis flash para o player. observe que diferentes players podem ter diferentes formatos da linha de variáveis flash. Consulte a documentação do seu player.
                CustomFlashVariables = $"source={videoName}&skin={skinName}"
            };
            //adicionar o código da skin.
            rma.AddCustomData(skinName,
                new FileStream(Path.Combine(pathToAdobeApp,"SkinOverAllNoFullNoCaption.swf"), FileMode.Open, FileAccess.Read));
            //definir o poster para o vídeo
            rma.SetPoster(new FileStream(Path.Combine(_dataDir, posterName), FileMode.Open, FileAccess.Read));

            Stream fs = new FileStream(Path.Combine(_dataDir,videoName), FileMode.Open, FileAccess.Read);

            //definir o conteúdo do vídeo
            rma.SetContent(videoName, fs);

            //definir o tipo do conteúdo (vídeo)
            rma.Type = RichMediaAnnotation.ContentType.Video;

            //ativar o player por clique
            rma.ActivateOn = RichMediaAnnotation.ActivationEvent.Click;

            //atualizar dados da anotação. Esse método deve ser chamado após todas as atribuições/configurações. Este método inicializa a estrutura de dados da anotação e incorpora os dados necessários.
            rma.Update();

            //adicionar anotação na página.
            page.Annotations.Add(rma);

            doc.Save(Path.Combine(_dataDir,"RichMediaAnnotation.pdf"));
        }
```
### Obter MultimediaAnnotation

Por favor, tente usar o seguinte trecho de código para obter MultimediaAnnotation de um documento PDF.

```csharp
        public static void GetMultimediaAnnotation()
        {
            // Carregar o arquivo PDF
            Document document = new Document(
                Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var mediaAnnotations = document.Pages[1].Annotations
                .Where(a => (a.AnnotationType == AnnotationType.Screen)
                || (a.AnnotationType == AnnotationType.Sound)
                || (a.AnnotationType == AnnotationType.RichMedia))
                .Cast<Annotation>();
            foreach (var ma in mediaAnnotations)
            {
                Console.WriteLine($"{ma.AnnotationType} [{ma.Rect}]");
            }
        }
```

### Excluir MultimediaAnnotation

O seguinte trecho de código mostra como excluir MultimediaAnnotation de um arquivo PDF.

```csharp
        public static void DeletePolyAnnotation()
        {
            // Carregar o arquivo PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation.pdf"));
            var richMediaAnnotations = document.Pages[1].Annotations
                            .Where(a => a.AnnotationType == AnnotationType.RichMedia)
                            .Cast<RichMediaAnnotation>();

            foreach (var rma in richMediaAnnotations)
            {
                document.Pages[1].Annotations.Delete(rma);
            }
            document.Save(System.IO.Path.Combine(_dataDir, "RichMediaAnnotation_del.pdf"));
        }
```
## Adicionar Anotações de Widget

Formulários interativos usam [Anotações de Widget](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) para representar a aparência dos campos e gerenciar interações do usuário.
Usamos esses elementos de formulário que adicionamos a um PDF para facilitar a entrada, envio de informações ou realizar algumas outras interações do usuário.

Anotações de Widget são uma representação gráfica de um campo de formulário em páginas específicas, por isso não podemos criá-las diretamente como uma anotação.

Cada Anotação de Widget terá gráficos apropriados (aparência) dependendo do seu tipo. Após a criação, certos aspectos visuais podem ser alterados, como estilo de borda e cor de fundo.
Outras propriedades, como cor do texto e fonte, podem ser alteradas através do campo, uma vez anexado a um.

Em alguns casos, você pode querer que um campo apareça em mais de uma página, repetindo o mesmo valor.
Em alguns casos, você pode querer que um campo apareça em mais de uma página, repetindo o mesmo valor.
Alguém preenchendo o formulário pode usar qualquer um desses widgets para atualizar o valor do campo, e isso é refletido em todos os outros widgets também.

Cada campo de formulário para cada local no documento representa uma Anotação de Widget. Os dados específicos do local da Anotação de Widget são adicionados à página específica. Cada campo de formulário possui várias variações. Um botão pode ser um botão de rádio, uma caixa de seleção ou um botão de pressão. Um widget de escolha pode ser uma caixa de listagem ou uma caixa combinada.

Neste exemplo, aprenderemos como adicionar os botões de navegação no documento.

### Adicionar Botão ao Documento

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "Imprimir documento atual",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "Imprimir Documento"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```
Este botão tem borda e define um fundo. Também configuramos um nome para o botão (Nome), uma dica de ferramenta (NomeAlternativo), um rótulo (LegendaNormal) e a cor do texto do rótulo (Cor).

### Usando ações de navegação de documentos

Existe um exemplo mais complexo do uso de Anotações de Widget - navegação de documentos em um documento PDF. Isso pode ser necessário para preparar uma apresentação de documento PDF.

Este exemplo mostra como criar 4 botões:

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "Ir para a primeira página", "Ir para a página anterior", "Ir para a próxima página", "Ir para a última página" };
var normalCaptions = new[] { "Primeira", "Anterior", "Próxima", "Última" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

Devemos criar os botões sem anexá-los à página.
Devemos criar os botões sem anexá-los à página.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

Devemos duplicar esse array de botões em cada página do documento.

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i],
          $"btn{pageIndex}_{i + 1}", pageIndex);

```

Chamamos o [método Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) com os seguintes parâmetros: campo, nome e o índice das páginas onde esse campo será adicionado.
Chamamos o [método Form.Add](https://reference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) com os seguintes parâmetros: campo, nome e o índice das páginas em que esse campo será adicionado.

E para obter o resultado completo, precisamos desativar os botões “Primeiro” e “Anterior” na primeira página e os botões “Próximo” e “Último” na última página.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

Para mais informações detalhadas e possibilidades dessas funcionalidades, veja também [Trabalhando com Formulários](/pdf/pt/net/acroforms/).

Em documentos PDF, você pode visualizar e gerenciar conteúdo 3D de alta qualidade criado com software CAD 3D ou de modelagem 3D e incorporado no documento PDF. Pode girar elementos 3D em todas as direções como se os estivesse segurando nas mãos.

Por que você precisa de uma exibição 3D de imagens afinal?

Nos últimos anos, a tecnologia fez enormes avanços em todas as áreas graças à impressão 3D.
Nos últimos anos, a tecnologia alcançou grandes avanços em todas as áreas graças à impressão 3D
e professores.

A principal tarefa da modelagem 3D é a ideia de um futuro objeto ou objeto porque, para liberar um objeto, você precisa de um entendimento de suas características de design em todos os detalhes para a regeneração sucessiva em design industrial ou arquitetura.

## Adicionar Anotação 3D

A anotação 3D é adicionada usando um modelo criado no formato U3D.

1. Crie um novo [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Carregue os dados do modelo 3D desejado (no nosso caso "Ring.u3d") para criar [PDF3DContent](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dcontent)
1. Crie o objeto [3dArtWork](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dartwork) e vincule-o ao documento e ao 3DContent
1. Ajuste o objeto pdf3dArtWork:

    - 3DLightingScheme - (definiremos `CAD` no exemplo)
    - 3DRenderMode - (definiremos `Solid` no exemplo)
    - Preencha `ViewArray`, crie pelo menos uma [Visualização 3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) e adicione-a ao array.
- Preencha `ViewArray`, crie pelo menos uma [Visualização 3D](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/pdf3dview) e adicione-a ao array.

1. Defina 3 parâmetros básicos na anotação:
    - a `página` na qual a anotação será colocada,
    - o `retângulo`, dentro do qual a anotação,
    - e o objeto `3dArtWork`.
1. Para uma melhor apresentação do objeto 3D, defina a moldura da borda
1. Defina a visualização padrão (por exemplo - TOP)
1. Adicione alguns parâmetros adicionais: nome, poster de pré-visualização etc.
1. Adicione a Anotação à [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page)
1. Salve o resultado

### Exemplo

Por favor, verifique o seguinte trecho de código para adicionar uma Anotação 3D.

```csharp
    public static void Add3dAnnotation()
    {
    // Carregar o arquivo PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(System.IO.Path.Combine(_dataDir,"Ring.u3d"));
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent)
    {
        LightingScheme = new PDF3DLightingScheme(LightingSchemeType.CAD),
        RenderMode = new PDF3DRenderMode(RenderModeType.Solid),
    };
    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.ViewArray.Add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.Pages.Add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.Border = new Border(pdf3dAnnotation);
    pdf3dAnnotation.SetDefaultViewIndex(1);
    pdf3dAnnotation.Flags = AnnotationFlags.NoZoom;
    pdf3dAnnotation.Name = "Ring.u3d";
    //definir imagem de pré-visualização se necessário
    //pdf3dAnnotation.SetImagePreview(System.IO.Path.Combine(_dataDir, "sample_3d.png"));
    document.Pages[1].Annotations.Add(pdf3dAnnotation);

    document.Save(System.IO.Path.Combine(_dataDir, "sample_3d.pdf"));
    }
```
Este exemplo de código mostrou-nos um modelo como este:

![Demonstração de Anotação 3D](3d_demo.png)

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



