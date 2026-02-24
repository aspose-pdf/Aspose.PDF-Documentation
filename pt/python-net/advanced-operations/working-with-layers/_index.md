---
title: Trabalhando com camadas PDF usando Python
linktitle: Trabalhando com camadas PDF
type: docs
weight: 50
url: /pt/python-net/work-with-pdf-layers/
description: Este artigo explica como bloquear uma camada PDF, extrair elementos de camada PDF, achatar um PDF com camadas e mesclar todas as camadas dentro de um PDF em uma única.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como gerenciar, bloquear, extrair, achatar e mesclar camadas PDF em Python
Abstract: Este artigo explica como trabalhar com camadas PDF em Python usando Aspose.PDF para .NET, incluindo bloqueio de camadas, extração de elementos de camada, achatamento de PDFs com camadas e mesclagem de camadas.
---

Camadas PDF permitem que um documento contenha múltiplos conjuntos de conteúdo que podem ser exibidos ou ocultados seletivamente. Cada camada pode incluir texto, imagens ou gráficos, e os usuários podem alterná‑las ligando ou desligando conforme necessário. Camadas são especialmente úteis em documentos complexos onde o conteúdo deve ser organizado ou separado. Os exemplos abaixo usam as APIs [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) e [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) e manipulam objetos [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) via a coleção `layers` da página.

## Bloquear uma camada PDF

Com Aspose.PDF para Python via .NET você pode abrir um PDF (veja [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)), bloquear uma [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) específica na primeira [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/), e salvar o documento com as alterações.

Métodos e propriedades disponíveis no objeto [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/):

- `layer.lock()` – Bloqueia a camada. (veja [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.unlock()` – Desbloqueia a camada. (veja [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods))
- `layer.locked` – Retorna o estado atual de bloqueio. (veja [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties))

1. Abra o documento PDF (veja [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Recupere a primeira página usando a coleção [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) do documento (veja [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).
1. Selecione a [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) a ser bloqueada a partir de `page.layers`.
1. Chame `layer.lock()` para impedir que os usuários alternem a visibilidade da camada.
1. Salve o documento atualizado usando [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Extrair elementos de camada PDF

Aspose.PDF permite extrair cada [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) de uma [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) e salvá‑la como um arquivo PDF separado.

Para criar um novo PDF a partir de uma camada, o seguinte trecho de código pode ser usado (a coleção `layers` é acessada via `Page.layers`):

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

Você também pode salvar camadas em um stream:

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## Achatar um PDF com camadas

O achatamento torna uma [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) permanente na página, removendo sua funcionalidade de alternância.

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

O parâmetro `cleanup_content_stream` controla se os marcadores de grupo de conteúdo opcional (marcadores OCG) são removidos. Definir como `False` acelera o achatamento. Veja o método [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) para detalhes.

## Mesclar todas as camadas dentro do PDF em uma única

Você pode mesclar todas as camadas (ou específicas) em uma nova única [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) (a API de mesclagem está no objeto [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)).

Métodos no objeto [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/):

- `page.merge_layers(new_layer_name)` — mescla todas as camadas em um novo nome de camada (veja [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).
- `page.merge_layers(new_layer_name, new_optional_content_group_id)` — mescla usando um ID de grupo de conteúdo opcional personalizado (veja [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)).

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
