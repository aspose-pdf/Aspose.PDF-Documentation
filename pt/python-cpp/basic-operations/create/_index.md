---
title: Criar documento PDF
linktitle: Criar PDF
type: docs
weight: 10
url: pt/python-cpp/create-document/
description: Esta página descreve como criar um documento PDF do zero com Aspose.PDF para Python via biblioteca C++.
---

Para os desenvolvedores, existem muitos cenários onde se torna necessário gerar arquivos PDF programaticamente. Você pode precisar gerar relatórios PDF e outros arquivos PDF programaticamente em seu software. É bastante longo e ineficiente escrever seu próprio código e funções do zero. Para criar um arquivo PDF com Python, há uma solução melhor - **Aspose.PDF para Python via C++**.

## Criar Arquivo PDF usando Python

Para criar um arquivo PDF usando Python, os seguintes passos podem ser usados.

* importe todas as classes e métodos da biblioteca Aspose.PDF para Python via C++.
* Crie um novo objeto Document que representa um documento PDF vazio usando [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/)

* Obtenha o objeto [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/) que contém todas as páginas no documento.
 * Adiciona uma nova página ao final da coleção de páginas [page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/) e retorna o objeto Page que representa a página adicionada.
* Salva o documento em um arquivo com o nome especificado no diretório de trabalho atual.
* Fecha o handle do documento e libera quaisquer recursos associados a ele.

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```


## Criar Arquivo PDF baseado em DOM

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```