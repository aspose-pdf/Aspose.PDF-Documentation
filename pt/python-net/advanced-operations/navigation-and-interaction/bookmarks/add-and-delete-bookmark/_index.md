---
title: Adicionar e Excluir um Marcador usando Python
linktitle: Adicionar e Excluir um Marcador
type: docs
weight: 10
url: /pt/python-net/add-and-delete-bookmark/
description: Você pode adicionar um marcador a um documento PDF com Python. É possível excluir todos ou marcadores específicos de um documento PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar e remover Marcadores usando Python
Abstract: Este artigo fornece instruções abrangentes sobre como gerenciar marcadores em documentos PDF usando a biblioteca Aspose.PDF para Python. Ele descreve os processos de adição, modificação e exclusão de marcadores dentro de um PDF. O artigo começa com um guia sobre como adicionar um marcador criando um objeto `OutlineItemCollection` e anexando‑o à `OutlineCollection` do documento. Inclui exemplos de código que demonstram a criação e adição de marcadores pai e filho, destacando uma relação hierárquica. Além disso, o artigo aborda métodos para excluir todos os marcadores ou um marcador específico por título. Cada seção inclui trechos de código Python para ilustrar as operações, garantindo que os leitores possam implementar facilmente as funcionalidades descritas em suas tarefas de manipulação de PDF.
---

## Adicionar um Marcador a um Documento PDF

Os marcadores são armazenados na coleção [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) do objeto Document, que por sua vez está na coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Para adicionar um marcador a um PDF:

1. Abra um documento PDF usando o objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie um marcador e defina suas propriedades.
1. Adicione a coleção [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) à coleção Outlines.

O trecho de código a seguir mostra como adicionar um marcador em um documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Bookmark"
    outline.italic = True
    outline.bold = True
    # Set the destination page number
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Add bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Adicionar um Marcador Filho ao Documento PDF

Os marcadores podem ser aninhados, indicando uma relação hierárquica entre marcadores pai e filho. Este artigo explica como adicionar um marcador filho, ou seja, um marcador de segundo nível, a um PDF.

Para adicionar um marcador filho a um arquivo PDF, primeiro adicione um marcador pai:

1. Abra um documento.
1. Adicione um marcador à [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), definindo suas propriedades.
1. Adicione o OutlineItemCollection à coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) do objeto Document.

O marcador filho é criado da mesma forma que o marcador pai, explicado acima, mas é adicionado à coleção Outlines do marcador pai

Os trechos de código a seguir mostram como adicionar um marcador filho a um documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create a parent bookmark object
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Create a child bookmark object
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Add child bookmark in parent bookmark's collection
    outline.append(childOutline)
    # Add parent bookmark in the document's outline collection.
    document.outlines.append(outline)

    # Save output
    document.save(output_pdf)
```

## Excluir Todos os Marcadores de um Documento PDF

Todos os marcadores em um PDF são armazenados na coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Este artigo explica como excluir todos os marcadores de um arquivo PDF.

Para excluir todos os marcadores de um arquivo PDF:

1. Chame o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Salve o arquivo modificado usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Os trechos de código a seguir mostram como excluir todos os marcadores de um documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all bookmarks
    document.outlines.delete()

    # Save updated file
    document.save(output_pdf)

```

## Excluir um Marcador Específico de um Documento PDF

Para excluir um marcador específico de um arquivo PDF:

1. Passe o título do marcador como parâmetro para o método Delete da coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Em seguida, salve o arquivo atualizado com o método Save do objeto Document.

A classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) fornece a coleção [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). O método [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) remove qualquer marcador com o título passado ao método.

Os trechos de código a seguir mostram como excluir um marcador específico do documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete particular outline by Title
    document.outlines.delete("Child Outline")

    # Save updated file
    document.save(output_pdf)
```


