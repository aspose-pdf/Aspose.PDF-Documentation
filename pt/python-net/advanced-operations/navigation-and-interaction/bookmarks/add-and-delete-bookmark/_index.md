---
title: Adicionar e Excluir Marcadores de PDF em Python
linktitle: Adicionar e Excluir um Marcador
type: docs
weight: 10
url: /pt/python-net/add-and-delete-bookmark/
description: Aprenda como adicionar e excluir marcadores em documentos PDF usando Python.
lastmod: "2026-05-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar e remover Marcadores usando Python
Abstract: Este artigo fornece instruções abrangentes sobre como gerenciar marcadores em documentos PDF usando a biblioteca Aspose.PDF para Python. Ele descreve os processos de adição, modificação e exclusão de marcadores dentro de um PDF. O artigo começa com um guia sobre como adicionar um marcador criando um objeto `OutlineItemCollection` e anexando‑o à `OutlineCollection` do documento. Inclui exemplos de código que demonstram a criação e a adição de marcadores pai e filho, destacando uma relação hierárquica. Além disso, o artigo aborda métodos para excluir todos os marcadores ou um marcador específico por título. Cada seção inclui trechos de código Python para ilustrar as operações, garantindo que os leitores possam implementar facilmente as funcionalidades descritas em suas tarefas de manipulação de PDF.
---

## Adicionar um marcador a um documento PDF

Os marcadores são mantidos no objeto Document\u0027s [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) coleção, ela mesma no [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) coleção.

Para adicionar um marcador a um PDF:

1. Abra um documento PDF usando [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto.
1. Crie um marcador e defina suas propriedades.
1. Adicionar o [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) coleção para a coleção Outlines.

O trecho de código a seguir mostra como adicionar um marcador em um documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Test Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Set the destination page number
    pdf_outline.action = ap.annotations.GoToAction(document.pages[1])

    # Add bookmark to the document's outline collection
    outlines = document.outlines
    outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Adicionar um marcador filho ao documento PDF

Os marcadores podem ser aninhados, indicando uma relação hierárquica entre marcadores pai e filho. Este artigo explica como adicionar um marcador filho, ou seja, um marcador de segundo nível, a um PDF.

Para adicionar um marcador filho a um arquivo PDF, primeiro adicione um marcador pai:

1. Abrir um documento.
1. Adicionar um marcador ao [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), definindo suas propriedades.
1. Adicionar o OutlineItemCollection ao objeto Document [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) coleção.

O marcador filho é criado exatamente como o marcador pai, explicado acima, mas é adicionado à coleção Outlines do marcador pai

Os trechos de código a seguir mostram como adicionar um marcador filho a um documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_child_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Create a parent bookmark object
    pdf_outline = ap.OutlineItemCollection(document.outlines)
    pdf_outline.title = "Parent Outline"
    pdf_outline.italic = True
    pdf_outline.bold = True

    # Create a child bookmark object
    pdf_child_outline = ap.OutlineItemCollection(document.outlines)
    pdf_child_outline.title = "Child Outline"
    pdf_child_outline.italic = True
    pdf_child_outline.bold = True

    # Add child bookmark to parent bookmark's collection
    pdf_outline.append(pdf_child_outline)

    # Add parent bookmark to the document's outline collection
    document.outlines.append(pdf_outline)

    # Save PDF document
    document.save(outfile)
```

## Excluir todos os marcadores de um documento PDF

Todos os marcadores em um PDF são armazenados em [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) coleção. Este artigo explica como excluir todos os marcadores de um arquivo PDF.

Para excluir todos os marcadores de um arquivo PDF:

1. Chame o [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) método Delete da coleção.
1. Salve o arquivo modificado usando o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

Os trechos de código a seguir mostram como excluir todos os marcadores de um documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmarks(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete all bookmarks in the PDF document
    document.outlines.delete()

    # Save PDF document
    document.save(outfile)
```

## Excluir um Marcador Particular de um Documento PDF

Para excluir um marcador específico de um arquivo PDF:

1. Passe o título do marcador como parâmetro para o [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) método Delete da coleção.
1. Em seguida, salve o arquivo atualizado usando o método Save do objeto Document.

O [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe’ fornece o [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) coleção. O [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) método remove qualquer marcador com o título passado ao método.

Os trechos de código a seguir mostram como excluir um marcador específico do documento PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def delete_bookmark(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Delete a specific bookmark by title.
    # Note: If multiple bookmarks have the same title, only the first matching bookmark will be deleted.
    document.outlines.delete("Child Outline")

    # Save PDF document
    document.save(outfile)
```

## Tópicos Relacionados ao Marcador

- [Trabalhar com marcadores de PDF em Python](/pdf/pt/python-net/bookmarks/)
- [Obtenha, atualize e expanda marcadores de PDF em Python](/pdf/pt/python-net/get-update-and-expand-bookmark/)
- [Navegação e interação em PDF usando Python](/pdf/pt/python-net/navigation-and-interaction/)

