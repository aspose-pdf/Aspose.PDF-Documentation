---
title: Trabalhar com Camadas PDF usando Python
linktitle: Trabalhar com camadas PDF
type: docs
weight: 50
url: /pt/python-net/working-with-pdf-layers/
description: Aprenda a adicionar, bloquear, extrair, achatar e mesclar camadas de PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerencie camadas de PDF com Python
Abstract: Este artigo explica como trabalhar com camadas PDF (Grupos de Conteúdo Opcional) usando Aspose.PDF for Python via .NET. Aprenda como adicionar camadas, bloquear a visibilidade das camadas, extrair o conteúdo da camada, achatar o conteúdo em camadas e mesclar camadas em uma única.
---

As camadas de PDF, também chamadas de Grupos de Conteúdo Opcional (OCGs), permitem organizar o conteúdo em grupos visuais separados que podem ser exibidos ou ocultados em visualizadores de PDF compatíveis. No Aspose.PDF, as operações de camada são construídas em torno do [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API.

Com Aspose.PDF for Python via .NET, você pode:

- Adicionar várias camadas a uma página.
- Bloqueie e desbloqueie camadas para controlar o comportamento de visibilidade.
- Extrair camadas em arquivos ou fluxos separados.
- Achatar conteúdo em camadas na página.
- Mesclar várias camadas em uma camada.

## Adicionar Camadas a um PDF

Este exemplo cria um PDF com três camadas. Ele usa um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), adiciona um [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), e adiciona [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) objetos para essa página.

1. Criar um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) e adicione um [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Crie e adicione a camada vermelha.
1. Crie e adicione a camada verde.
1. Crie e adicione a camada azul.
1. Salve o documento PDF.

O PDF resultante conterá três camadas separadas: uma linha vermelha, uma linha verde e uma linha azul. Cada uma pode ser ativada ou desativada em leitores de PDF que suportam conteúdo em camadas.

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## Bloquear uma camada PDF

Este exemplo abre um PDF, bloqueia uma camada específica na primeira página e salva o arquivo atualizado.

Bloquear uma camada impede que os usuários alterem o estado de visibilidade dessa camada em visualizadores de PDF compatíveis. As camadas são acessadas a partir de uma página e gerenciadas através da coleção de camadas da página.

Métodos e propriedades disponíveis:

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) bloqueia a camada.
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) desbloqueia a camada.
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) retorna o estado atual de bloqueio.

1. Abra o documento PDF.
1. Acesse a primeira página do PDF.
1. Verifique se a página tem camadas.
1. Obtenha a primeira camada e bloqueie-a.
1. Salve o PDF atualizado.

Se o PDF contiver camadas, a primeira camada será travada, garantindo que seu estado de visibilidade não possa ser alterado pelo usuário. Se nenhuma camada for encontrada, uma mensagem será impressa em vez disso.

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## Extrair elementos de camada PDF

Este exemplo usa a biblioteca Aspose.PDF for Python via .NET para extrair camadas individuais da primeira página de um documento PDF e salvar cada camada como um arquivo PDF separado usando [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

Para criar um novo PDF a partir de uma camada, o seguinte trecho de código pode ser usado:

1. Carregue o PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Acesse as camadas na página 1 até [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Verifique se as camadas existem.
1. Iterar pelas camadas e salvar cada uma.

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

É possível extrair elementos de camada PDF e salvá-los em um novo fluxo de arquivo PDF:

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## Aplanar um PDF em camadas

Este script usa Aspose.PDF for Python via .NET para achatar todas as camadas na primeira página de um PDF Document. O aplanamento mescla o conteúdo visual de cada camada em uma camada unificada, facilitando a impressão, o compartilhamento ou o arquivamento sem perder a fidelidade visual ou os dados específicos de camada. A operação é executada com [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. Carregue o documento PDF.
1. Acessar camadas na página 1.
1. Verifique se as camadas existem.
1. Achatar cada camada com `layer.flatten(True)`.
1. Salve o documento modificado.

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## Mesclar Todas as Camadas de um PDF em Uma

Este trecho de código usa Aspose.PDF para mesclar todas as camadas na primeira página de um PDF em uma única camada unificada com um nome personalizado usando [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. Carregue o documento PDF.
1. Acesse a página 1 e recupere suas camadas.
1. Verifique se as camadas existem.
1. Defina um novo nome de camada.
1. Mescle as camadas em uma.
1. Salvar o documento.

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## Tópicos de Camada Relacionados

- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Trabalhar com tabelas em PDF usando Python](/pdf/pt/python-net/working-with-tables/)
- [Adicionar páginas PDF em Python](/pdf/pt/python-net/add-pages/)
