---
title: Trabalhar com camadas PDF usando Python
linktitle: Trabalhar com camadas PDF
type: docs
weight: 50
url: /pt/python-net/working-with-pdf-layers/
description: A próxima tarefa explica como bloquear uma camada PDF, extrair elementos de camada PDF, achatar um PDF em camadas e mesclar todas as camadas dentro do PDF em uma única.
lastmod: "2025-11-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manipular as camadas PDF
Abstract: Este guia oferece uma visão abrangente de como gerenciar e manipular camadas PDF usando a biblioteca Aspose.PDF para Python via .NET. Camadas PDF — também conhecidas como Grupos de Conteúdo Opcional (OCGs) — permitem a organização do conteúdo em componentes visuais separados que podem ser ativados ou desativados.
---

Camadas PDF são uma forma poderosa de organizar e apresentar conteúdo de maneira flexível dentro de um único arquivo PDF, permitindo que os usuários exibam ou ocultem diferentes partes conforme suas necessidades.

Com **Aspose.PDF para Python via .NET**, você pode:

- Bloquear/Desbloquear camadas para controlar a visibilidade.
- Extrair camadas em arquivos ou fluxos separados.
- Achatar camadas para torná-las permanentes.
- Mesclar camadas em uma única camada unificada.

## Adicionar camadas ao PDF

Este exemplo mostra como criar e adicionar múltiplas camadas a um documento PDF usando Aspose.PDF para Python via .NET. Cada camada contém conteúdo gráfico separado, como linhas coloridas, que podem ser ativadas ou desativadas em visualizadores de PDF que suportam camadas.

1. Crie um novo documento PDF e adicione uma página.
1. Crie e adicione a camada vermelha.
1. Crie e adicione a camada verde.
1. Crie e adicione a camada azul.
1. Salve o documento PDF.

O PDF resultante conterá três camadas distintas: uma linha vermelha, uma linha verde e uma linha azul. Cada uma pode ser ativada ou desativada em leitores de PDF que suportam conteúdo em camadas.

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## Bloquear uma camada PDF

Com Aspose.PDF para Python via .NET você pode abrir um PDF, bloquear uma camada específica na primeira página e salvar o documento com as alterações.

Este exemplo mostra como bloquear uma camada (Grupo de Conteúdo Opcional, OCG) em um documento PDF usando Aspose.PDF para Python via .NET. Bloquear impede que os usuários alterem a visibilidade da camada em um visualizador de PDF, garantindo que o conteúdo permaneça sempre visível (ou oculto) conforme definido pelo documento.

Métodos e propriedades disponíveis:

- layer.lock() – Bloqueia a camada.
- layer.unlock() – Desbloqueia a camada.
- layer.locked – Retorna o estado atual de bloqueio.

1. Abra o documento PDF.
1. Acesse a primeira página do PDF.
1. Verifique se a página possui camadas.
1. Obtenha a primeira camada e bloqueie-a.
1. Salve o PDF atualizado.

Se o PDF contiver camadas, a primeira camada será bloqueada, garantindo que seu estado de visibilidade não possa ser alterado pelo usuário. Caso nenhuma camada seja encontrada, uma mensagem será exibida.

```python

import aspose.pdf as ap
from os import path

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

Este exemplo usa a biblioteca Aspose.PDF para Python via .NET para extrair camadas individuais da primeira página de um documento PDF e salvar cada camada como um arquivo PDF separado.

Para criar um novo PDF a partir de uma camada, o trecho de código a seguir pode ser usado:

1. Carregue o documento PDF. O PDF de entrada é carregado em um objeto Aspose.PDF.Document.
1. Acesse as Camadas na Página 1. O script recupera todas as camadas da primeira página usando document.pages[1].layers.
1. Verifique a presença de Camadas. Se nenhuma camada for encontrada, uma mensagem é exibida e a função termina.
1. Itere e Salve Cada Camada.

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

É possível extrair elementos de camada PDF e salvá-los em um novo fluxo de arquivo PDF:

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## Achatar um PDF em camadas

Este script usa Aspose.PDF para Python via .NET para achatar todas as camadas na primeira página de um documento PDF. O achatamento mescla o conteúdo visual de cada camada em uma única camada unificada, facilitando a impressão, o compartilhamento ou o arquivamento sem perder a fidelidade visual ou os dados específicos das camadas.

1. Carregue o documento PDF. O PDF de entrada é carregado em um objeto Aspose.PDF.Document.
1. Acesse as camadas na página 1. O script recupera todas as camadas da primeira página usando document.pages[1].layers.
1. Verifique a presença de camadas. Se nenhuma camada for encontrada, uma mensagem é exibida e a função termina.
1. Achate cada camada. Cada camada é achatada usando layer.flatten(True), que mescla seu conteúdo na página.
1. Salve o documento modificado.

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if not page.layers:
            print("No layers found in the document.")
            return
        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## Mesclar todas as camadas dentro do PDF em uma única

Este trecho de código usa Aspose.PDF para mesclar todas as camadas na primeira página de um PDF em uma única camada unificada com um nome personalizado.

1. Carregue o documento PDF. O PDF é carregado em um objeto Aspose.PDF.Document.
1. Acesse a página e suas camadas. A primeira página é selecionada e suas camadas são recuperadas.
1. Verifique a existência de camadas. Se não houver camadas, uma mensagem é exibida e o processo termina.
1. Defina o novo nome da camada. Um novo nome de camada ("LayerNew") é especificado para o resultado mesclado.
1. Mescle as camadas. Se um ID de grupo de conteúdo opcional for fornecido, ele é usado na mesclagem. Caso contrário, as camadas são mescladas usando apenas o novo nome.
1. Salve o documento

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
