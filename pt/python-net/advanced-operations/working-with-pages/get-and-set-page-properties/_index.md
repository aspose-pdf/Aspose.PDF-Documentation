---
title: Obter e Definir Propriedades de Página PDF em Python
linktitle: Obtendo e Definindo Propriedades de Página
type: docs
weight: 90
url: /pt/python-net/get-and-set-page-properties/
description: Aprenda como inspecionar e atualizar as propriedades de página PDF, como tamanho, contagem e informações de cor, em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Obter e Definir propriedades de página usando Python
Abstract: Este artigo discute as capacidades do Aspose.PDF for Python via .NET, focando na leitura e definição de propriedades de página em arquivos PDF usando Python. O artigo cobre várias funcionalidades, incluindo a determinação do número de páginas em um PDF, o acesso e modificação de propriedades de página e o tratamento de informações de cores. Para obter o número de páginas, a classe `Document` e a coleção `PageCollection` são usadas, com trechos de código demonstrando como recuperar a contagem de páginas, mesmo sem salvar o documento. O artigo explica diferentes propriedades de página, como MediaBox, BleedBox, TrimBox, ArtBox e CropBox, e fornece exemplos de código para acessar essas propriedades. Além disso, cobre a recuperação de uma página específica de um PDF e sua gravação como um documento separado, bem como a determinação do tipo de cor de cada página. Os exemplos ao longo do texto são implementados em Python, ilustrando aplicações práticas desses recursos.
---

Aspose.PDF for Python via .NET permite que você leia e defina propriedades de páginas em um arquivo PDF em suas aplicações Python. Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre propriedades de página do PDF, como cor, e definir propriedades de página. Os exemplos utilizam o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) e [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) APIs e são escritas em Python.

Use este guia quando precisar inspecionar metadados de página, determinar a contagem de páginas ou atualizar características ao nível da página como parte de tarefas de análise ou normalização de documentos.

## Obter número de páginas em um arquivo PDF

Ao trabalhar com documentos, você costuma querer saber quantas páginas eles contêm. Com Aspose.PDF isso leva no máximo duas linhas de código.

Para obter o número de páginas em um arquivo PDF:

1. Abra o arquivo PDF usando o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Em seguida, use o [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) propriedade Count da collection (do objeto Document) para obter o número total de páginas no documento.

O trecho de código a seguir mostra como obter o número de páginas de um arquivo PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Obter contagem de páginas sem salvar o documento

Às vezes, geramos os arquivos PDF dinamicamente e, durante a criação do arquivo PDF, podemos nos deparar com a necessidade (criar Sumário, etc.) de obter a contagem de páginas do arquivo PDF sem salvar o arquivo no sistema ou em um stream. Portanto, para atender a essa necessidade, um método [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) foi introduzido na classe Document. Por favor, dê uma olhada no trecho de código a seguir que mostra as etapas para obter a contagem de páginas sem salvar o documento.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## Obter propriedades da página

Cada página em um arquivo PDF possui várias propriedades, como largura, altura, bleed-, crop- e trimbox. Aspose.PDF permite que você acesse essas propriedades.

### Entendendo as Propriedades da Página: a Diferença entre Artbox, BleedBox, CropBox, MediaBox, TrimBox e a propriedade Rect

- **Media box**: A caixa de mídia é a maior caixa de página. Ela corresponde ao tamanho da página (por exemplo A4, A5, US Letter, etc.) selecionado quando o documento foi impresso para PostScript ou PDF. Em outras palavras, a caixa de mídia determina o tamanho físico do suporte no qual o documento PDF é exibido ou impresso.
- **Bleed box**: Se o documento tem sangria, o PDF também terá uma caixa de sangria. Sangria é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usada para garantir que, quando o documento for impresso e cortado ao tamanho (“recortado”), a tinta chegue até a borda da página. Mesmo se a página for cortada incorretamente - cortada ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.
- **Trim box**: A caixa de corte indica o tamanho final de um documento após a impressão e o corte.
- **Art box**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Essa caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Crop box**: A crop box é o tamanho de “página” no qual seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da crop box é exibido no Adobe Acrobat.
  Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente 10.10.1 Page Boundaries.
-- **Page.Rect**: a interseção (retângulo comumente visível) da MediaBox e DropBox (`Page.rect`). Veja o [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) tipo para propriedades de retângulo. A imagem abaixo ilustra essas propriedades.

Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Acessando Propriedades da Página

O [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) classe fornece todas as propriedades relacionadas a uma página PDF específica. Todas as páginas dos arquivos PDF estão contidas no do [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) do objeto [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) coleção.

A partir daí, é possível acessar cada indivíduo `Page` objetos usando seu índice, ou percorrer a coleção para obter todas as páginas. Uma vez que uma página individual é acessada, podemos obter suas propriedades. O trecho de código a seguir mostra como obter as propriedades da página (a `Page` API).

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Determinar cor da página

O [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) A classe fornece as propriedades relacionadas a uma página específica em um documento PDF, incluindo o tipo de cor - RGB, preto e branco, escala de cinza ou indefinido - que a página utiliza.

Todas as páginas dos arquivos PDF são contidas por [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) coleção. O [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) a propriedade especifica a cor dos elementos na página. Para obter ou determinar as informações de cor para uma página PDF específica, use o [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) do objeto [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) propriedade.

O trecho de código a seguir mostra como iterar através de cada página individual de um arquivo PDF para obter informações de cor.

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## Tópicos de Página Relacionados

- [Trabalhe com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Alterar tamanho da página PDF em Python](/pdf/pt/python-net/change-page-size/)
- [Cortar páginas PDF em Python](/pdf/pt/python-net/crop-pages/)
- [Rotacionar páginas PDF em Python](/pdf/pt/python-net/rotate-pages/)