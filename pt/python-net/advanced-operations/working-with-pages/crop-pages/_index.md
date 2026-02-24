---
title: Recortando páginas PDF usando Python
linktitle: Recortando páginas PDF
type: docs
weight: 70
url: /pt/python-net/crop-pages/
description: Você pode mudar as propriedades da página, como largura, altura, Bleed-, Crop- e Trimbox usando Aspose.PDF para Python via .NET.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como acessar e modificar propriedades de página em PDF usando Python
Abstract: O artigo fornece uma visão geral de como acessar e modificar propriedades de página em um documento PDF usando Aspose.PDF para Python. Ele descreve várias propriedades de página, incluindo a media box, bleed box, trim box, art box e crop box, explicando seus papéis na definição das dimensões e limites de uma página PDF para impressão e exibição. A media box representa o maior tamanho de página, enquanto a bleed box garante a cobertura de tinta além da borda da página para o corte. A trim box indica o tamanho final do documento após o corte, e a art box envolve o conteúdo real da página. A crop box define a área visível no Adobe Acrobat. O artigo inclui um trecho de código Python demonstrando como definir uma nova crop box, junto com outras boxes, para uma página específica em um documento PDF. Exemplos visuais ilustram a aparência da página antes e depois de aplicar o recorte, demonstrando a aplicação prática da modificação dessas propriedades.
---

## Obter propriedades da página

Cada página em um arquivo PDF possui várias propriedades, como largura, altura, bleed-, crop- e trimbox. Aspose.PDF para Python permite que você acesse essas propriedades.

- **media_box**: A media box é a maior caixa da página. Ela corresponde ao tamanho da página (por exemplo A4, A5, US Letter, etc.) selecionado quando o documento foi impresso para PostScript ou PDF. Em outras palavras, a media box determina o tamanho físico do meio no qual o documento PDF é exibido ou impresso.
- **bleed_box**: Se o documento tem bleed, o PDF também terá uma bleed box. Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usada para garantir que, quando o documento for impresso e cortado ao tamanho ("trimmed"), a tinta chegará até a borda da página. Mesmo que a página seja cortada incorretamente - cortada ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.
- **trim_box**: A trim box indica o tamanho final de um documento após impressão e corte.
- **art_box**: A art box é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **crop_box**: A crop box é o tamanho de "página" no qual seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da crop box é exibido no Adobe Acrobat. Para descrições detalhadas dessas propriedades, consulte a especificação Adobe.Pdf, particularmente 10.10.1 Page Boundaries.

Recorte a primeira [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) de um PDF para uma área retangular específica usando Aspose.PDF para Python. A função ajusta múltiplas caixas de página—`crop_box`, `trim_box`, `art_box` e `bleed_box`—para garantir resultados visuais consistentes. O recorte pode ser útil para remover margens indesejadas ou focar em uma região específica da página.

1. Carregue o PDF como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (use `ap.Document()`).
1. Defina o retângulo de recorte usando [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) com as coordenadas desejadas (em pontos).
1. Defina o `crop_box`, `trim_box`, `art_box` e `bleed_box` da [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para o retângulo definido.
1. Salve o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado em um novo arquivo de saída.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

Neste exemplo usamos um arquivo de exemplo [aqui](crop_page.pdf). Inicialmente nossa página parece como mostrada na Figura 1.
![Figura 1. Página recortada](crop_page.png)

Após a alteração, a página ficará como na Figura 2.
![Figura 2. Página recortada](crop_page2.png)

## Recortar página PDF com base no conteúdo da primeira imagem

Recorte a primeira [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dinamicamente com base nos limites da primeira imagem encontrada na página. Usando [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), o script identifica a primeira imagem e ajusta o `crop_box` da página para corresponder às dimensões da imagem. Essa abordagem é útil quando você deseja focar em conteúdo visual específico em vez de coordenadas predefinidas.

1. Carregue o PDF como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Localize imagens na primeira página usando [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Verifique se existem imagens:
- Se encontrado, defina o `crop_box` da [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para corresponder ao [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) da primeira imagem.
- Caso contrário, mantenha a página inalterada e notifique o usuário.
1. Salve o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) modificado no arquivo de saída especificado.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```
