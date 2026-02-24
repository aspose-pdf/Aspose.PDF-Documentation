---
title: Trabalhando com Gráficos Vetoriais usando Python
linktitle: Trabalhando com Gráficos Vetoriais
type: docs
weight: 100
url: /pt/python-net/working-with-vector-graphics/
description: Este artigo descreve os recursos de trabalho com a ferramenta GraphicsAbsorber usando Python.
lastmod: "2025-05-17"
TechArticle: true
AlternativeHeadline: Use a ferramenta GraphicsAbsorber em PDF com Python
Abstract: A documentação do Aspose.PDF for Python via .NET sobre o artigo Trabalhando com Gráficos Vetoriais fornece um guia abrangente para desenvolvedores que desejam manipular gráficos vetoriais em documentos PDF usando a classe GraphicsAbsorber. Esta classe facilita a extração, movimentação, remoção e duplicação de elementos gráficos vetoriais em páginas PDF.
---

Neste capítulo, exploraremos como usar a poderosa classe `GraphicsAbsorber` para interagir com gráficos vetoriais em documentos PDF. Seja para mover, remover ou adicionar gráficos, este guia mostrará como executar essas tarefas de forma eficaz.

## Introdução

Gráficos vetoriais são um componente crucial de muitos documentos PDF, usados para representar imagens, formas e outros elementos gráficos. O Aspose.PDF fornece a classe `GraphicsAbsorber`, que permite que desenvolvedores acessem e manipulem esses gráficos programaticamente. Ao usar o método `Visit` do `GraphicsAbsorber`, você pode extrair gráficos vetoriais de uma página especificada e executar várias operações, como mover, remover ou copiar para outras páginas.

## Extraindo Gráficos

O primeiro passo ao trabalhar com gráficos vetoriais é extraí‑los de um documento PDF. Veja como fazer isso usando a classe `GraphicsAbsorber`:

1. Abra o documento PDF.
1. Inicialize o GraphicsAbsorber.
1. Selecione a página alvo.
1. Extraia os gráficos da página.
1. Itere e exiba os elementos extraídos.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

A classe GraphicsAbsorber faz parte do namespace aspose.pdf.vector e foi projetada especificamente para interagir com gráficos vetoriais dentro de documentos PDF.

## Movendo Gráficos

Depois de extrair os gráficos, você pode movê‑los para uma posição diferente na mesma página. Veja como fazer isso:

1. Abra o documento PDF.
1. Inicialize o GraphicsAbsorber.
1. Selecione a página alvo.
1. Extraindo elementos gráficos.
1. Suspender atualizações para desempenho.
1. Modificar as posições dos elementos gráficos.
1. Retomar atualizações e aplicar as alterações.
1. Salvar o documento atualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Removendo Gráficos

Existem cenários em que você pode querer remover gráficos específicos de uma página. O Aspose.PDF for Python oferece dois métodos para fazer isso:

### Método 1: Usando Limite Retangular

O exemplo a seguir demonstra como remover elementos gráficos vetoriais localizados dentro de uma área retangular específica na primeira página de um documento PDF usando a biblioteca Aspose.PDF for Python via .NET. Esse processo envolve identificar os elementos gráficos dentro do retângulo definido e removê‑los para limpar ou modificar o conteúdo do PDF.

1. Abra o documento PDF.
1. Inicialize o GraphicsAbsorber.
1. Selecione a página alvo.
1. Extraindo elementos gráficos.
1. Definir o retângulo alvo.
1. Suspender atualizações para desempenho.
1. Remover elementos gráficos dentro do retângulo.
1. Retomar atualizações e aplicar as alterações.
1. Salvar o documento atualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Método 2: Usando uma Coleção de Elementos Removidos

O exemplo a seguir demonstra como remover elementos gráficos vetoriais localizados dentro de uma área retangular específica na primeira página de um documento PDF usando a biblioteca Aspose.PDF for Python via .NET. Esse processo envolve identificar os elementos gráficos dentro do retângulo definido e removê‑los para limpar ou modificar o conteúdo do PDF.

1. Abra o documento PDF.
1. Inicialize o GraphicsAbsorber.
1. Selecione a página alvo.
1. Definir o retângulo alvo.
1. Extraindo elementos gráficos.
1. Criando uma coleção para remoção.
1. Identificando elementos dentro do retângulo.
1. Suspendendo atualizações para desempenho.
1. Removendo elementos gráficos.
1. Retomando atualizações e aplicando alterações.
1. Salvando o documento atualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## Adicionando Gráficos a Outra Página

Gráficos absorvidos de uma página podem ser adicionados a outra página dentro do mesmo documento.
Aqui estão dois métodos para alcançar isso:

### Método 1: Adicionando Gráficos Individualmente

O próximo exemplo copia elementos gráficos vetoriais da primeira página de um documento PDF e os cola na segunda página. Esta operação é facilitada pela classe GraphicsAbsorber, que permite a extração e manipulação de gráficos vetoriais em documentos PDF.

1. Abra o documento PDF.
1. Inicialize o GraphicsAbsorber.
1. Selecione a página de destino.
1. Extraindo elementos gráficos da primeira página.
1. Suspendendo atualizações na segunda página para desempenho.
1. Adicionando os elementos gráficos extraídos à segunda página.
1. Retomando atualizações e aplicando alterações.
1. Salvando o documento atualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### Método 2: Adicionando Gráficos como uma Coleção

O próximo exemplo duplica elementos gráficos vetoriais da primeira página de um documento PDF e os coloca na segunda página. Isso é conseguido usando a classe GraphicsAbsorber, que facilita a extração e manipulação de gráficos vetoriais em documentos PDF.

1. Abra o documento PDF.
1. Inicialize o GraphicsAbsorber.
1. Selecione a página de destino.
1. Extraindo elementos gráficos da primeira página.
1. Suspendendo atualizações na segunda página para desempenho.
1. Adicionando os elementos gráficos extraídos à segunda página.
1. Retomando atualizações e aplicando alterações.
1. Salvando o documento atualizado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
