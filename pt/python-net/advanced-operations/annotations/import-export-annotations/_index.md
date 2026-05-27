---
title: Importar e Exportar Anotações usando Python
linktitle: Importar e Exportar Anotações
type: docs
weight: 80
url: /pt/python-net/import-export-annotations/
description: Aprenda como importar anotações de um PDF e exportá-las para um novo documento PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Transferir anotações PDF entre documentos em Python.
Abstract: Este artigo explica como copiar anotações de um PDF de origem e exportá‑las para um novo documento PDF usando Aspose.PDF for Python via .NET. A demonstração divide o processo em etapas pequenas, incluindo o carregamento do arquivo de origem, a criação do documento de destino, a adição de uma página, a cópia de anotações da primeira página e a gravação do resultado.
---

Este artigo mostra como importar anotações de um PDF existente e exportá‑las para um novo documento PDF usando Aspose.PDF for Python via .NET.

O exemplo lê anotações da primeira página de um arquivo de origem, cria um novo PDF, adiciona uma página em branco e copia cada anotação para essa nova página. Essa abordagem é útil quando você precisa mover comentários, marcações ou notas de revisão para um documento de saída separado.

## Carregue o PDF de origem

Criar um `Document` objeto para o arquivo de entrada que já contém anotações. Este objeto fornece acesso à coleção de páginas e às anotações armazenadas em cada página.

```python
source_document = ap.Document(infile)
```

## Criar o PDF de destino

Em seguida, crie um documento PDF vazio que receberá as anotações importadas. Nesta fase, o documento de destino não contém nenhuma página.

```python
destination_document = ap.Document()
```

## Adicionar uma página para anotações exportadas

Como as anotações devem pertencer a uma página, adicione uma nova página ao documento de destino antes de copiar qualquer coisa.

```python
page = destination_document.pages.add()
```

## Copiar anotações da página de origem

Itere através da coleção de anotações na primeira página do PDF de origem e adicione cada anotação à nova página no documento de destino.

O segundo argumento em `page.annotations.add(annot, True)` diz ao Aspose.PDF para copiar a anotação na página de destino em vez de apenas reutilizar a referência ao objeto existente.

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## Salvar o documento de saída

Depois que todas as anotações foram copiadas, salve o documento de destino para criar o arquivo PDF final.

```python
destination_document.save(outfile)
```

## Exemplo completo

O código a seguir combina todas as etapas em uma função reutilizável:

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## Tópicos Relacionados

- [Anotações Interativas](/python-net/interactive-annotations/)
- [Anotações de marcação](/python-net/markup-annotations/)
- [Anotações de Mídia](/python-net/media-annotations/)
- [Anotações de Segurança](/python-net/security-annotations/)
- [Anotações de Forma](/python-net/shape-annotations/)
- [Anotações Baseadas em Texto](/python-net/text-based-annotations/)
- [Anotações de Marca d'Água](/python-net/watermark-annotations/)
