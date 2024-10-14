---
title: Obter e Definir Propriedades da Página
type: docs
url: /net/get-and-set-page-properties/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obter e Definir Propriedades da Página",
    "alternativeHeadline": "Obtendo e Definindo Propriedades de Páginas PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, obter propriedades da página, definir propriedades da página",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
Aspose.PDF para .NET permite ler e configurar propriedades de páginas em um arquivo PDF em suas aplicações .NET. Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre propriedades de páginas de PDF como cor e configurar propriedades da página. Os exemplos dados são em C#, mas você pode usar qualquer linguagem .NET como VB.NET para alcançar o mesmo.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obter Número de Páginas em um Arquivo PDF

Ao trabalhar com documentos, você frequentemente quer saber quantas páginas eles contêm. Com Aspose.PDF isso leva não mais do que duas linhas de código.

Para obter o número de páginas em um arquivo PDF:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
2. Em seguida, use a propriedade Count da coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (do objeto Document) para obter o número total de páginas no documento.

O seguinte trecho de código mostra como obter o número de páginas de um arquivo PDF.
O seguinte trecho de código mostra como obter o número de páginas de um arquivo PDF.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetNumberofPages-GetNumberofPages.cs" >}}

### Obter a contagem de páginas sem salvar o documento

Às vezes, geramos os arquivos PDF em tempo real e, durante a criação do arquivo PDF, podemos nos deparar com a necessidade (criação de Sumário, etc.) de obter a contagem de páginas do arquivo PDF sem salvar o arquivo no sistema ou stream. Assim, para atender a essa necessidade, um método [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) foi introduzido na classe Document. Por favor, veja o seguinte trecho de código que mostra os passos para obter a contagem de páginas sem salvar o documento.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetPageCount-GetPageCount.cs" >}}

## Obter Propriedades da Página

Cada página em um arquivo PDF possui uma série de propriedades, tais como largura, altura, sangramento, caixa de corte e caixa de margem.
Cada página em um arquivo PDF possui uma série de propriedades, como a largura, altura, sangria, caixa de corte e caixa de acabamento.

### **Entendendo as Propriedades das Páginas: a Diferença entre Artbox, BleedBox, CropBox, MediaBox, TrimBox e a Propriedade Rect**

- **Caixa de mídia**: A caixa de mídia é a maior caixa de página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, Carta dos EUA, etc.) selecionado quando o documento foi impresso em PostScript ou PDF. Em outras palavras, a caixa de mídia determina o tamanho físico da mídia na qual o documento PDF é exibido ou impresso.
- **Caixa de sangria**: Se o documento possui sangria, o PDF também terá uma caixa de sangria. Sangria é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usada para garantir que, quando o documento é impresso e cortado no tamanho (“acabado”), a tinta irá até a borda da página. Mesmo que a página seja cortada imprecisamente - cortada ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.
- **Caixa de acabamento**: A caixa de acabamento indica o tamanho final de um documento após a impressão e o corte.
- **Trim box**: A caixa de corte indica o tamanho final de um documento após a impressão e corte.
- **Art box**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Crop box**: A caixa de corte é o tamanho de “página” no qual seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da caixa de corte é exibido no Adobe Acrobat.
  Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Limites de Página.
- **Page.Rect**: a interseção (retângulo comumente visível) da MediaBox e DropBox. A imagem abaixo ilustra essas propriedades.

Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Acessando Propriedades da Página**

A classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fornece todas as propriedades relacionadas a uma página PDF específica.
A classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fornece todas as propriedades relacionadas a uma página PDF específica.

A partir daí, é possível acessar objetos Page individuais usando seu índice, ou percorrer a coleção, usando um loop foreach, para obter todas as páginas. Uma vez que uma página individual é acessada, podemos obter suas propriedades. O seguinte trecho de código mostra como obter as propriedades da página.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetProperties-GetProperties.cs" >}}

## Obter uma Página Específica do Arquivo PDF

Aspose.PDF permite que você [divida um PDF em páginas individuais](/pdf/net/split-pdf-document/) e as salve como arquivos PDF. Obter uma página especificada em um arquivo PDF e salvá-la como um novo PDF é uma operação muito semelhante: abrir o documento fonte, acessar a página, criar um novo documento e adicionar a página a este.

O objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) possui um [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) que contém as páginas no arquivo PDF.
O objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) possui uma [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) que contém as páginas do arquivo PDF.

1. Especifique o índice da página usando a propriedade Pages.
1. Crie um novo objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Adicione o objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ao novo objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Salve a saída usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

O seguinte trecho de código mostra como obter uma página específica de um arquivo PDF e salvá-la como um novo arquivo.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetParticularPage-GetParticularPage.cs" >}}

## Determinar Cor da Página

A classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fornece as propriedades relacionadas a uma página específica em um documento PDF, incluindo o tipo de cor - RGB, preto e branco, escala de cinza ou indefinido - que a página utiliza.
A classe [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) fornece as propriedades relacionadas a uma página específica em um documento PDF, incluindo que tipo de cor - RGB, preto e branco, escala de cinza ou indefinido - a página utiliza.

Todas as páginas dos arquivos PDF estão contidas na coleção [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). A propriedade ColorType especifica a cor dos elementos na página. Para obter ou determinar a informação de cor para uma página PDF específica, use a propriedade [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) do objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

O seguinte trecho de código mostra como iterar através de cada página de um arquivo PDF para obter informações sobre a cor.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-DeterminePageColor-DeterminePageColor.cs" >}}

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


