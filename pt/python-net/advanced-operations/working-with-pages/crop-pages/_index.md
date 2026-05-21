---
title: Recortar páginas PDF em Python
linktitle: Recorte de páginas PDF
type: docs
weight: 70
url: /pt/python-net/crop-pages/
description: Aprenda como recortar páginas PDF e ajustar as caixas de recorte, corte, sangria e mídia em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como acessar e modificar propriedades de página em PDF usando Python
Abstract: O artigo fornece uma visão geral de como acessar e modificar propriedades de página em um documento PDF usando Aspose.PDF for Python. Ele descreve várias propriedades de página, incluindo a media box, bleed box, trim box, art box e crop box, explicando seus papéis na definição das dimensões e limites de uma página PDF para impressão e exibição. A media box representa o maior tamanho de página, enquanto a bleed box garante a cobertura da tinta além da borda da página para o corte. A trim box indica o tamanho final do documento após o corte, e a art box envolve o conteúdo real da página. A crop box define a área visível no Adobe Acrobat. O artigo inclui um trecho de código Python demonstrando como definir uma nova crop box, juntamente com as demais caixas, para uma página específica em um documento PDF. Exemplos visuais ilustram a aparência da página antes e depois da aplicação do recorte, mostrando a aplicação prática da modificação dessas propriedades.
---

## Obter propriedades da página

Cada página em um arquivo PDF possui várias propriedades, como largura, altura, bleed-, crop- e trimbox. Aspose.PDF for Python permite que você acesse essas propriedades.

Use esta página quando precisar reduzir a área visível da página, preparar arquivos para fluxos de trabalho de impressão ou inspecionar a geometria das caixas da página em documentos PDF.

- **media_box**: A media box é a maior caixa da página. Ela corresponde ao tamanho da página (por exemplo A4, A5, US Letter, etc.) selecionado quando o documento foi impresso para PostScript ou PDF. Em outras palavras, a media box determina o tamanho físico da mídia na qual o documento PDF é exibido ou impresso.
- **bleed_box**: Se o documento tem bleed, o PDF também terá uma bleed box. Bleed é a quantidade de cor (ou arte) que se estende além da borda de uma página. É usado para garantir que, quando o documento é impresso e cortado ao tamanho (\"trimmed\"), a tinta chegue até a borda da página. Mesmo que a página seja cortada incorretamente - ligeiramente fora das marcas de corte - não aparecerão bordas brancas na página.
- **trim_box**: A trim box indica o tamanho final de um documento após a impressão e o corte.
- **art_box**: A caixa de arte é a caixa desenhada ao redor do conteúdo real das páginas em seus documentos. Esta caixa de página é usada ao importar documentos PDF em outras aplicações.
- **crop_box**: A crop box é o tamanho "página" no qual seu documento PDF é exibido no Adobe Acrobat. Na visualização normal, apenas o conteúdo da crop box é exibido no Adobe Acrobat. Para descrições detalhadas dessas propriedades, lea a especificação Adobe.Pdf, particularmente 10.10.1 Limites de Página.

Cortar o primeiro [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) de um PDF para uma área retangular específica usando Aspose.PDF for Python. A função ajusta várias caixas de página—`crop_box`, `trim_box`, `art_box`, e `bleed_box`—para garantir resultados visuais consistentes. O recorte pode ser útil para remover margens indesejadas ou focar em uma região específica de uma página.

1. Carregue o PDF como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) (usar `ap.Document()`).
1. Defina o retângulo de corte usando [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) com as coordenadas desejadas (em pontos).
1. Defina o [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)'s `crop_box`, `trim_box`, `art_box`, e `bleed_box` para o retângulo definido.
1. Salvar o modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para um novo arquivo de saída.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

Neste exemplo, usamos um arquivo de amostra [aqui](crop_page.pdf). Inicialmente, nossa página parece como mostrada na Figura 1.
![Figura 1. Página recortada](crop_page.png)

Depois da alteração, a página ficará como a Figura 2.
![Figura 2. Página recortada](crop_page2.png)

## Recortar página PDF com base no conteúdo da primeira imagem

Cortar o primeiro [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) dinamicamente com base nos limites da primeira imagem encontrada na página. Usando [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/), o script identifica a primeira imagem e ajusta a página `crop_box` para corresponder às dimensões da imagem. Essa abordagem é útil quando você deseja focar em conteúdo visual específico em vez de coordenadas predefinidas.

1. Carregue o PDF como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Localizar imagens na primeira página usando [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. Verificar se as imagens existem:
    - Se encontrado, definir o [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` para corresponder ao da primeira imagem [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - Se não, mantenha a página inalterada e notifique o usuário.
1. Salvar o modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para o arquivo de saída especificado.

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
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

## Tópicos Relacionados da Página

- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Alterar tamanho da página PDF em Python](/pdf/pt/python-net/change-page-size/)
- [Obter e definir propriedades da página PDF em Python](/pdf/pt/python-net/get-and-set-page-properties/)
- [Girar páginas PDF em Python](/pdf/pt/python-net/rotate-pages/)