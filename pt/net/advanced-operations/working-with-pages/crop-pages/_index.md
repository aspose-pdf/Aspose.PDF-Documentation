---
title: Crop PDF Pages programmatically C#
linktitle: Crop Pages
type: docs
weight: 80
url: /pt/net/crop-pages/
description: Você pode obter propriedades de páginas, como a largura, altura, bleed-, crop- e trimbox usando o Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Crop PDF Pages programmatically C#",
    "alternativeHeadline": "How to crop PDF Pages in .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, crop pdf pages",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Você pode obter propriedades de páginas, como a largura, altura, bleed-, crop- e trimbox usando o Aspose.PDF para .NET."
}
</script>
## Obter Propriedades da Página

Cada página em um arquivo PDF tem uma série de propriedades, como largura, altura, boxes de sangria, corte e refilo. O Aspose.PDF permite que você acesse essas propriedades.

- **Caixa de mídia**: A caixa de mídia é a maior caixa da página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, Carta dos EUA, etc.) selecionado quando o documento foi impresso para PostScript ou PDF. Em outras palavras, a caixa de mídia determina o tamanho físico da mídia na qual o documento PDF é exibido ou impresso.
- **Caixa de sangria**: Se o documento possui sangria, o PDF também terá uma caixa de sangria. Sangria é a quantidade de cor (ou arte) que se estende além da borda da página. É usada para garantir que, quando o documento é impresso e cortado no tamanho ("refilado"), a tinta vá até a borda da página. Mesmo que a página seja cortada de forma imprecisa - cortada ligeiramente fora das marcas de corte - nenhuma borda branca aparecerá na página.
- **Caixa de corte**: A caixa de corte indica o tamanho final de um documento após impressão e corte.
- **Caixa de arte**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos.
- **Caixa de Arte**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos.
- **Caixa de Corte**: A caixa de corte é o "tamanho da página" no qual seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da caixa de corte é exibido no Adobe Acrobat. Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, especialmente 10.10.1 Limites da Página.
- **Page.Rect**: a interseção (retângulo comumente visível) do MediaBox e DropBox. A imagem abaixo ilustra essas propriedades.
Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O trecho abaixo mostra como cortar a página:

```csharp
public static void CropPagesPDF()
{
    var pdfDocument1 = new Aspose.Pdf.Document("crop_page.pdf");
    Console.WriteLine(pdfDocument1.Pages[1].CropBox);
    Console.WriteLine(pdfDocument1.Pages[1].TrimBox);
    Console.WriteLine(pdfDocument1.Pages[1].ArtBox);
    Console.WriteLine(pdfDocument1.Pages[1].BleedBox);
    Console.WriteLine(pdfDocument1.Pages[1].MediaBox);

    // Criar novo Retângulo de Caixa
    var newBox = new Rectangle(200, 220, 2170, 1520);
    pdfDocument1.Pages[1].CropBox = newBox;
    pdfDocument1.Pages[1].TrimBox = newBox;
    pdfDocument1.Pages[1].ArtBox = newBox;
    pdfDocument1.Pages[1].BleedBox = newBox;
   
    pdfDocument1.Save("crop_page_modified.pdf");           
}
```
Neste exemplo, usamos um arquivo de exemplo [aqui](crop_page.pdf). Inicialmente, nossa página parece como mostrado na Figura 1.
![Figura 1. Página Cortada](crop_page.png)

Após a mudança, a página ficará como na Figura 2.
![Figura 2. Página Cortada](crop_page2.png)

