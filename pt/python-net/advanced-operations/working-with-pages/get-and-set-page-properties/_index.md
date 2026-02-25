---
title: Obter e Definir Propriedades de Página usando Python
linktitle: Obter e Definir Propriedades de Página
type: docs
weight: 90
url: /pt/python-net/get-and-set-page-properties/
description: Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre as propriedades de página do PDF, como cor, e definir propriedades de página.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Obter e Definir propriedades de página usando Python
Abstract: Este artigo discute as capacidades do Aspose.PDF para Python via .NET, focando na leitura e definição de propriedades de página em arquivos PDF usando Python. O artigo cobre várias funcionalidades, incluindo determinar o número de páginas em um PDF, acessar e modificar propriedades de página e lidar com informações de cor. Para obter o número de páginas, são usadas a classe `Document` e a coleção `PageCollection`, com trechos de código que demonstram como recuperar a contagem de páginas, mesmo sem salvar o documento. O artigo explica diferentes propriedades de página, como MediaBox, BleedBox, TrimBox, ArtBox e CropBox, e fornece exemplos de código para acessar essas propriedades. Além disso, aborda a recuperação de uma página específica de um PDF e sua gravação como um documento separado, bem como a determinação do tipo de cor de cada página. Os exemplos ao longo do texto são implementados em Python, ilustrando aplicações práticas desses recursos.
---

Aspose.PDF for Python via .NET permite ler e definir propriedades de páginas em um arquivo PDF em suas aplicações Python. Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre as propriedades de página do PDF, como cor, e definir propriedades de página. Os exemplos usam as APIs [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) e [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) e são escritos em Python.

## Obter Número de Páginas em um Arquivo PDF

Ao trabalhar com documentos, você costuma querer saber quantas páginas eles contêm. Com Aspose.PDF isso leva no máximo duas linhas de código.

Para obter o número de páginas em um arquivo PDF:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Em seguida, use a propriedade Count da coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (do objeto Document) para obter o número total de páginas no documento.

O trecho de código a seguir mostra como obter o número de páginas de um arquivo PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count(input_file_name):
    """
    Get the total number of pages in a PDF document.
    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        None: Prints the page count to console.
    Example:
        get_page_count("example.pdf")
        # Output: Page Count: 10
    """
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### Obter contagem de páginas sem salvar o documento

Às vezes geramos arquivos PDF dinamicamente e, durante a criação do PDF, podemos nos deparar com a necessidade (criar índice etc.) de obter a contagem de páginas do PDF sem salvar o arquivo no sistema ou em stream. Para atender a essa necessidade, um método [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) foi introduzido na classe Document. Por favor, veja o trecho de código a seguir que mostra as etapas para obter a contagem de páginas sem salvar o documento.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count_without_saving(input_file_name):
    """
    Get the page count of a PDF document after adding content without saving the file.

    This function opens an existing PDF document, adds a new page with 300 text fragments,
    processes the paragraphs to ensure accurate page counting, and prints the total number
    of pages in the document. The document is not saved to disk.

    Args:
        input_file_name (str): Path to the input PDF file to be processed.

    Returns:
        None: This function prints the page count but does not return a value.

    Example:
        >>> get_page_count_without_saving("sample.pdf")
        Number of pages in document = 2
    """
    # Instantiate Document instance
    document = ap.Document(input_file_name)
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

## Obter Propriedades de Página

Cada página em um arquivo PDF possui várias propriedades, como largura, altura, bleed-, crop- e trimbox. Aspose.PDF permite acessar essas propriedades.

### Entendendo as Propriedades de Página: a Diferença entre Artbox, BleedBox, CropBox, MediaBox, TrimBox e a propriedade Rect

- **Media box**: A media box é a maior caixa da página. Ela corresponde ao tamanho da página (por exemplo A4, A5, US Letter, etc.) selecionado quando o documento foi impresso para PostScript ou PDF. Em outras palavras, a media box determina o tamanho físico do meio no qual o documento PDF é exibido ou impresso.
- **Bleed box**: Se o documento tem sangramento, o PDF também terá uma bleed box. O sangramento (bleed) é a quantidade de cor (ou arte) que se estende além da borda da página. É usado para garantir que, quando o documento for impresso e cortado ao tamanho (“recortado”), a tinta chegue até a borda da página. Mesmo que a página seja recortada incorretamente - cortada levemente fora das marcas de corte - não aparecerão bordas brancas na página.
- **Trim box**: A trim box indica o tamanho final de um documento após a impressão e o recorte.
- **Art box**: A art box é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **Crop box**: A crop box é o tamanho “da página” em que seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, somente o conteúdo da crop box é exibido no Adobe Acrobat.
Para descrições detalhadas dessas propriedades, leia a especificação Adobe.Pdf, particularmente a seção 10.10.1 Limites de Página.
-- **Page.Rect**: a interseção (retângulo geralmente visível) da MediaBox e DropBox (`Page.rect`). Veja o tipo [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) para propriedades do retângulo. A imagem abaixo ilustra essas propriedades.

Para mais detalhes, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Acessando Propriedades de Página

A classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) fornece todas as propriedades relacionadas a uma página PDF específica. Todas as páginas dos arquivos PDF estão contidas na coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Da lá, é possível acessar objetos `Page` individuais usando seu índice, ou percorrer a coleção para obter todas as páginas. Uma vez que uma página individual é acessada, podemos obter suas propriedades. O trecho de código a seguir mostra como obter propriedades de página (a API `Page`).

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_properties(input_file_name):
    """
    Retrieves and displays various page properties for the first page of a PDF document.

    Args:
        input_file_name (str): Path to the PDF file to analyze.
    """
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
        "Rect": page.rect
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}")

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## Determinar Cor da Página

A classe [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) fornece as propriedades relacionadas a uma página específica em um documento PDF, incluindo o tipo de cor - RGB, preto e branco, escala de cinza ou indefinido - que a página utiliza.

Todas as páginas dos arquivos PDF são contidas na coleção [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/). A propriedade [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) especifica a cor dos elementos na página. Para obter ou determinar as informações de cor de uma página PDF específica, use a propriedade [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) do objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

O trecho de código a seguir mostra como percorrer individualmente as páginas de um arquivo PDF para obter informações de cor.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_color_type(input_file_name):
    """
    Analyzes and prints the color type information for each page in a PDF document.

    This function opens a PDF file and iterates through all pages to determine
    the color type of each page (black and white, grayscale, RGB, or undefined).
    The results are printed to the console with human-readable descriptions.

    Args:
        input_file_name (str): Path to the PDF file to analyze.

    Returns:
        None: This function prints results directly to console and doesn't return a value.

    Example:
        >>> get_page_color_type("sample.pdf")
        Page # 1 is RGB.
        Page # 2 is Gray Scale.
        Page # 3 is Black and white.

    Note:
        Requires the aspose.pdf library (imported as ap) to be installed and available.
        The PDF file must be accessible at the specified path.
    """
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
            ap.ColorType.UNDEFINED: "undefined"
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```


