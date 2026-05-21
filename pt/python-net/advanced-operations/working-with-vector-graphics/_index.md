---
title: Trabalhar com Gráficos Vetoriais em Python
linktitle: Trabalhando com Gráficos Vetoriais
type: docs
weight: 100
url: /pt/python-net/working-with-vector-graphics/
description: Aprenda como extrair, mover, remover e copiar gráficos vetoriais entre páginas PDF usando GraphicsAbsorber em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Use GraphicsAbsorber para inspecionar e manipular gráficos vetoriais PDF em Python.
Abstract: Este artigo explica como trabalhar com gráficos vetoriais no Aspose.PDF for Python via .NET usando a classe GraphicsAbsorber. Aprenda como extrair elementos vetoriais de páginas PDF, mover ou removê-los e copiar gráficos entre páginas com controle de baixo nível em fluxos de trabalho Python.
---

[Aspose.PDF para Python via .NET](/pdf/pt/python-net/) fornece o [Absorvedor de Gráficos](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) classe para acessar e manipular gráficos vetoriais já presentes em uma página PDF. Chame-a `visit` método em qualquer página para extrair caminhos, formas e outros operadores gráficos, então mover, remover ou copiar esses elementos conforme necessário.

Use esta página quando precisar inspecionar ou modificar elementos de desenho vetorial incorporados em um PDF existente, em vez de desenhar novas formas do zero.

## Extraindo Gráficos

A extração é o ponto de partida para todas as tarefas de gráficos vetoriais. `GraphicsAbsorber` lê o fluxo de conteúdo de uma página e expõe cada elemento gráfico com sua referência de página, posição e operadores brutos.

1. Abra o documento PDF.
1. Criar um [Absorvedor de Gráficos](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) instância.
1. Chamar `visit` na página de destino para preencher `elements`.
1. Iterar sobre `elements` para inspecionar a posição e as contagens de operadores.

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` é parte do `aspose.pdf.vector` namespace e é projetado especificamente para interagir com gráficos vetoriais em fluxos de conteúdo PDF.

## Gráficos em movimento

Após a extração, defina um novo `position` em cada elemento para realocá-lo na mesma página. Envolva as atualizações em `suppress_update` / `resume_update` chamadas para agrupar gravações de fluxos de conteúdo em uma única operação e evitar repinturas redundantes.

1. Abra o documento PDF.
1. Criar um `GraphicsAbsorber` e chamar `visit` na página de destino.
1. Chamar `suppress_update` para pausar gravações de fluxo de conteúdo.
1. Atualizar o `position` de cada elemento.
1. Chamar `resume_update` para confirmar todas as alterações de uma só vez.
1. Salve o documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## Removendo Gráficos

Para excluir elementos vetoriais específicos de uma página, filtre por posição ou retângulo delimitador e, em seguida, remova-os. Aspose.PDF for Python fornece duas abordagens, dependendo de você querer remover os elementos inline ou coletá-los primeiro.

### Método 1: Remover Inline Usando Limite do Retângulo

Esta abordagem verifica a posição de cada elemento em relação a um retângulo e chama `element.remove()` diretamente dentro do loop. Use-o quando quiser código conciso e não precisar inspecionar o conjunto removido posteriormente.

1. Abra o documento PDF.
1. Criar um `GraphicsAbsorber` e chamar `visit` na página de destino.
1. Defina o alvo [Retângulo](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. Chamar `suppress_update` para pausar gravações de fluxo de conteúdo.
1. Iterar `elements`, chamando `remove()` em cada elemento cuja posição esteja dentro do retângulo.
1. Chamar `resume_update` para confirmar as exclusões.
1. Salve o documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### Método 2: Coletar Elementos Primeiro, Depois Excluir

Esta abordagem reúne elementos correspondentes em um [GraphicElementCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) e passa a coleção para `page.delete_graphics`. Use-o quando precisar revisar ou registrar o que será removido antes de confirmar a exclusão.

1. Abra o documento PDF.
1. Criar um `GraphicsAbsorber` e chamar `visit` na página de destino.
1. Defina o retângulo de destino.
1. Iterar `elements` e adicione elementos correspondentes a um `GraphicElementCollection`.
1. Chamar `page.contents.suppress_update` para pausar gravações de fluxo de conteúdo.
1. Chamar `page.delete_graphics` com a coleção.
1. Chamar `page.contents.resume_update` para confirmar as exclusões.
1. Salve o documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## Adicionando Gráficos a Outra Página

Elementos vetoriais extraídos de uma página podem ser colocados em qualquer outra página no mesmo documento. Dois métodos estão disponíveis: adicionar os elementos um a um ou passar toda a coleção em uma única chamada.

### Método 1: Adicionar Elementos Individualmente

Use este método quando precisar de controle por elemento, como filtrar ou transformar elementos individuais antes de colocá‑los na página de destino.

1. Abra o documento PDF.
1. Criar um `GraphicsAbsorber` e chamar `visit` na página de origem.
1. Adicionar uma nova página de destino ao documento.
1. Chamar `page_2.contents.suppress_update` para pausar gravações de fluxo de conteúdo.
1. Chamar `element.add_on_page(page_2)` para cada elemento.
1. Chamar `page_2.contents.resume_update` para confirmar todas as adições.
1. Salve o documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### Método 2: Adicionar toda a coleção de uma vez

Use este método quando quiser copiar todos os elementos extraídos para uma página em uma única operação sem iterar manualmente.

1. Abra o documento PDF.
1. Criar um `GraphicsAbsorber` e chamar `visit` na página de origem.
1. Adicionar uma nova página de destino ao documento.
1. Chamar `page_2.contents.suppress_update` para pausar gravações de fluxo de conteúdo.
1. Chamar `page_2.add_graphics` com o completo `elements` coleção.
1. Chamar `page_2.contents.resume_update` para confirmar todas as adições.
1. Salve o documento modificado.

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## Tópicos Relacionados

- [Operações avançadas de PDF em Python](/pdf/pt/python-net/advanced-operations/)
- [Trabalhe com gráficos PDF em Python](/pdf/pt/python-net/working-with-graphs/)
- [Trabalhar com operadores PDF em Python](/pdf/pt/python-net/working-with-operators/)
- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
