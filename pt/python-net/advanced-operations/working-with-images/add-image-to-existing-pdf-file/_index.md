---
title: Adicionar Imagem ao PDF usando Python
linktitle: Adicionar Imagem
type: docs
weight: 10
url: /pt/python-net/add-image-to-existing-pdf-file/
description: Este artigo fornece orientações sobre como adicionar imagens a arquivos PDF existentes usando Python com a biblioteca Aspose.PDF. Dois métodos são descritos para alcançar isso. O primeiro método envolve o uso da classe `Document` da Aspose.PDF, onde o usuário carrega o PDF, especifica o número da página e utiliza o método `add_image` da classe `Page` para posicionar a imagem. O documento é então salvo usando o método `save()`. O segundo método utiliza a classe `PdfFileMend` do namespace Aspose.PDF.Facades, que oferece uma interface mais simples. Aqui, o método `add_image()` é invocado para adicionar a imagem à página e coordenadas especificadas, seguido de salvar o PDF atualizado e fechar o objeto `PdfFileMend`. Trechos de código são fornecidos para ambos os métodos para demonstrar o processo.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Como adicionar imagens em PDF usando Python
Abstract: Este artigo fornece orientações sobre como adicionar imagens a arquivos PDF existentes usando Python com a biblioteca Aspose.PDF. Dois métodos são descritos para alcançar isso. O primeiro método envolve o uso da classe `Document` da Aspose.PDF, onde o usuário carrega o PDF, especifica o número da página e utiliza o método `add_image` da classe `Page` para posicionar a imagem. O documento é então salvo usando o método `save()`. O segundo método utiliza a classe `PdfFileMend` do namespace Aspose.PDF.Facades, que oferece uma interface mais simples. Aqui, o método `add_image()` é invocado para adicionar a imagem à página e coordenadas especificadas, seguido de salvar o PDF atualizado e fechar o objeto `PdfFileMend`. Trechos de código são fornecidos para ambos os métodos para demonstrar o processo.
---

## Adicionar Imagem em um PDF Existente

Este exemplo demonstra como inserir uma imagem em uma posição específica em uma página PDF usando Aspose.PDF para Python via .NET.

1. Carregue o documento PDF com 'ap.Document'.
1. Selecione a página alvo '(document.pages[1]' - a primeira página).
1. Use 'page.add_image()' para posicionar a imagem:
- Caminho do arquivo da imagem.
- Um objeto 'Rectangle' definindo as coordenadas da imagem (left=20, bottom=730, right=120, top=830).
1. Salve o PDF atualizado.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
```

## Adicionar uma Imagem Usando Operadores

O próximo trecho de código mostra uma abordagem de baixo nível para adicionar uma imagem a uma página PDF trabalhando manualmente com operadores PDF ao invés de métodos auxiliares de alto nível.

Etapas:

1. Crie um novo 'Document' em branco.
1. Adicione uma página e defina seu tamanho (842 × 595 - paisagem A4).
1. Acesse os recursos de imagem da página (page.resources.images).
1. Carregue o arquivo de imagem em um stream e adicione-o aos recursos.
- O método retorna um 'image_id'.
- O objeto de imagem recém-adicionado é recuperado dos recursos.
1. Defina um retângulo que mantenha a proporção da imagem:
1. Construa uma sequência de operadores:
- 'GSave()' - Salva o estado gráfico atual.
- 'ConcatenateMatrix(matrix)' - Aplica a transformação (escala e centraliza a imagem verticalmente na página).
- 'Do(image_id)' - Renderiza a imagem.
- 'GRestore()' - Restaura o estado gráfico.
1. Adicione a sequência de operadores a 'page.contents'.
1. Salve o PDF resultante.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(path_outfile)
```

## Adicionar Imagem com Texto Alternativo

Este exemplo mostra como adicionar uma imagem a uma página PDF e atribuir texto alternativo (alt text) para conformidade de acessibilidade (como PDF/UA).

1. Crie um novo 'Document' e adicione uma página (842 × 595, paisagem A4).
1. Posicione a imagem na página usando 'page.add_image()' com um retângulo que cobre a página inteira.
1. Acesse os recursos de imagem da página ('page.resources.images').
1. Defina uma string de texto alternativo (ex.: 'Alternative text for image').
1. Recupere o primeiro objeto de imagem dos recursos ('x_image = resources_images[1]').
1. Use 'try_set_alternative_text(alt_text, page)' para atribuir texto alternativo à imagem.
1. Salve o PDF resultante.

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```
