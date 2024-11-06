---
title: Obter e Definir Propriedades de Página usando Python
linktitle: Obter e Definir Propriedades de Página
type: docs
weight: 90
url: pt/python-net/get-and-set-page-properties/
description: Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre propriedades de página de PDF, como cor, e definir propriedades de página.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obter e Definir Propriedades de Página usando Python",
    "alternativeHeadline": "Obtendo e Definindo Propriedades de Página de PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, python, obter propriedades de página, definir propriedades de página",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe Aspose.PDF Doc",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/get-and-set-page-properties/"
    },
    "dateModified": "2023-04-04",
    "description": ""
}
</script>


Aspose.PDF para Python via .NET permite que você leia e defina propriedades de páginas em um arquivo PDF em suas aplicações Python. Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre propriedades de páginas PDF, como cor, e definir propriedades de páginas. Os exemplos dados estão em Python.

## Obter Número de Páginas em um Arquivo PDF

Ao trabalhar com documentos, você frequentemente quer saber quantas páginas eles contêm. Com o Aspose.PDF isso não leva mais do que duas linhas de código.

Para obter o número de páginas em um arquivo PDF:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Em seguida, use a propriedade Count da coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (do objeto Document) para obter o número total de páginas no documento.

O trecho de código a seguir mostra como obter o número de páginas de um arquivo PDF.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obter contagem de páginas
    print("Contagem de Páginas:", str(len(document.pages)))
```


### Obter contagem de páginas sem salvar o documento

Às vezes, geramos arquivos PDF em tempo real e, durante a criação do arquivo PDF, podemos nos deparar com a necessidade (criação de Índice etc.) de obter a contagem de páginas do arquivo PDF sem salvar o arquivo no sistema ou fluxo. Portanto, para atender a essa necessidade, um método [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) foi introduzido na classe Document. Por favor, veja o trecho de código a seguir que mostra as etapas para obter a contagem de páginas sem salvar o documento.

```python

    import aspose.pdf as ap

    # Instanciar instância do Documento
    document = ap.Document()
    # Adicionar página à coleção de páginas do arquivo PDF
    page = document.pages.add()
    # Criar instância de loop
    for i in range(0, 300):
        # Adicionar TextFragment à coleção de parágrafos do objeto página
        page.paragraphs.add(ap.text.TextFragment("Teste de contagem de páginas"))
    # Processar os parágrafos no arquivo PDF para obter contagem de páginas precisa
    document.process_paragraphs()
    # Imprimir número de páginas no documento
    print("Número de páginas no documento =", str(len(document.pages)))
```


## Obter Propriedades da Página

Cada página em um arquivo PDF possui uma série de propriedades, como largura, altura, bleed-, crop- e trimbox. Aspose.PDF permite que você acesse essas propriedades.

### **Entendendo as Propriedades da Página: a Diferença entre a propriedade Artbox, BleedBox, CropBox, MediaBox, TrimBox e Rect**

- **Media box**: A media box é a maior caixa de página. Ela corresponde ao tamanho da página (por exemplo, A4, A5, Carta dos EUA, etc.) selecionado quando o documento foi impresso em PostScript ou PDF. Em outras palavras, a media box determina o tamanho físico do meio no qual o documento PDF é exibido ou impresso.
- **Bleed box**: Se o documento tiver sangramento, o PDF também terá uma bleed box.
 Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usado para garantir que, quando o documento for impresso e cortado no tamanho (“aparado”), a tinta vá até a borda da página. Mesmo que a página seja mal aparada - cortada ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.
- **Caixa de corte**: A caixa de corte indica o tamanho final de um documento após impressão e aparo.
- **Caixa de arte**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Caixa de recorte**: A caixa de recorte é o tamanho da “página” em que seu documento PDF é exibido no Adobe Acrobat. No modo de exibição normal, apenas o conteúdo da caixa de recorte é exibido no Adobe Acrobat.
  Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Limites de Página.
- **Page.Rect**: a interseção (retângulo visível comum) do MediaBox e DropBox. A imagem abaixo ilustra essas propriedades.

Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Acessando Propriedades da Página**

A classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) fornece todas as propriedades relacionadas a uma página específica do PDF. Todas as páginas dos arquivos PDF estão contidas na coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

A partir daí, é possível acessar objetos Page individuais usando seu índice, ou percorrer a coleção, usando um loop foreach, para obter todas as páginas. Uma vez que uma página individual é acessada, podemos obter suas propriedades. O trecho de código a seguir mostra como obter propriedades de página.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Obter página específica
    page = document.pages[1]
    # Obter propriedades da página
    print(
        "ArtBox : Altura={},Largura={},LLX={},LLY={},URX={},URY={}".format(
            page.art_box.height,
            page.art_box.width,
            page.art_box.llx,
            page.art_box.lly,
            page.art_box.urx,
            page.art_box.ury,
        )
    )
    print(
        "BleedBox : Altura={},Largura={},LLX={},LLY={},URX={},URY={}".format(
            page.bleed_box.height,
            page.bleed_box.width,
            page.bleed_box.llx,
            page.bleed_box.lly,
            page.bleed_box.urx,
            page.bleed_box.ury,
        )
    )
    print(
        "CropBox : Altura={},Largura={},LLX={},LLY={},URX={},URY={}".format(
            page.crop_box.height,
            page.crop_box.width,
            page.crop_box.llx,
            page.crop_box.lly,
            page.crop_box.urx,
            page.crop_box.ury,
        )
    )
    print(
        "MediaBox : Altura={},Largura={},LLX={},LLY={},URX={},URY={}".format(
            page.media_box.height,
            page.media_box.width,
            page.media_box.llx,
            page.media_box.lly,
            page.media_box.urx,
            page.media_box.ury,
        )
    )
    print(
        "TrimBox : Altura={},Largura={},LLX={},LLY={},URX={},URY={}".format(
            page.trim_box.height,
            page.trim_box.width,
            page.trim_box.llx,
            page.trim_box.lly,
            page.trim_box.urx,
            page.trim_box.ury,
        )
    )
    print(
        "Rect : Altura={},Largura={},LLX={},LLY={},URX={},URY={}".format(
            page.rect.height,
            page.rect.width,
            page.rect.llx,
            page.rect.lly,
            page.rect.urx,
            page.rect.ury,
        )
    )
    print("Número da Página :", page.number)
    print("Girar :", page.rotate)
```

## Obter uma Página Específica do Arquivo PDF

Aspose.PDF para Python permite [dividir um PDF em páginas individuais](/pdf/python-net/split-pdf-document/) e salvá-las como arquivos PDF. Obter uma página especificada em um arquivo PDF e salvá-la como um novo PDF é uma operação muito semelhante: abrir o documento fonte, acessar a página, criar um novo documento e adicionar a página a este.

A [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection) do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) mantém as páginas no arquivo PDF. Para obter uma página específica desta coleção:

1. Especifique o índice da página usando a propriedade Pages.
1. Crie um novo objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Adicione o objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ao novo objeto Document.
1. Salve a saída usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

O trecho de código a seguir mostra como obter uma página específica de um arquivo PDF e salvá-la como um novo arquivo.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obter página específica
    page = document.pages[2]

    # Salvar a página como arquivo PDF
    new_document = ap.Document()
    new_document.pages.add(page)
    new_document.save(output_pdf)
```

## Determinar Cor da Página

A classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) fornece as propriedades relacionadas a uma página específica em um documento PDF, incluindo qual tipo de cor - RGB, preto e branco, escala de cinza ou indefinido - a página utiliza.

Todas as páginas dos arquivos PDF estão contidas pela coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
 O documento abaixo está em formato markdown com trechos de código. Veja a tradução do texto para o português:

A propriedade [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) especifica a cor dos elementos na página. Para obter ou determinar a informação de cor para uma página específica do PDF, use a propriedade [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) do objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

O trecho de código a seguir mostra como iterar através das páginas individuais de um arquivo PDF para obter informações de cor.

```python

    import aspose.pdf as ap

    # Abrir arquivo PDF de origem
    document = ap.Document(input_pdf)
    # Iterar através de todas as páginas do arquivo PDF
    for page_n in range(0, len(document.pages)):
        page_number = page_n + 1
        # Obter a informação do tipo de cor para uma página específica do PDF
        page_color_type = document.pages[page_number].color_type
        if page_color_type == ap.ColorType.BLACK_AND_WHITE:
            print("Página # " + str(page_number) + " é Preto e branco.")

        if page_color_type == ap.ColorType.GRAYSCALE:
            print("Página # " + str(page_number) + " é Escala de Cinza.")

        if page_color_type == ap.ColorType.RGB:
            print("Página # " + str(page_number) + " é RGB.")

        if page_color_type == ap.ColorType.UNDEFINED:
            print("Cor da Página # " + str(page_number) + " não está definida.")
```

{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}