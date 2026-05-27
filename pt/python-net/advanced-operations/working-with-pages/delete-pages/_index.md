---
title: Excluir páginas PDF em Python
linktitle: Excluindo páginas PDF
type: docs
weight: 80
url: /pt/python-net/delete-pages/
description: Aprenda como excluir páginas de arquivos PDF em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Excluir uma ou mais páginas PDF em Python
Abstract: Este artigo explica como remover páginas de arquivos PDF usando Aspose.PDF for Python via .NET. Aprenda como excluir uma única página ou várias páginas de um documento usando a PageCollection API e, em seguida, salvar o PDF atualizado.
---

Você pode excluir páginas de um arquivo PDF usando Aspose.PDF for Python via .NET. Para excluir uma página específica, use o [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) de um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Use este fluxo de trabalho quando precisar remover páginas indesejadas de um PDF antes de compartilhar, arquivar ou combinar documentos.

## Excluir página do arquivo PDF

Aspose.PDF for Python via .NET exclui a página 2 do PDF de entrada e salva o Document atualizado em um novo arquivo. Esse recurso é útil para remover páginas indesejadas ou confidenciais sem alterar o restante do documento.

1. Carregue o PDF de entrada como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Exclua a página usando o [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Chame o [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método para salvar o arquivo PDF atualizado.

O trecho de código a seguir mostra como excluir uma página específica do arquivo PDF usando Python.

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## Excluir várias páginas de um documento PDF

Excluir várias páginas permite remover um conjunto de páginas especificadas em uma única operação, o que é mais eficiente do que excluir páginas uma a uma. O PDF resultante é salvo em um novo arquivo, preservando o documento original.

1. Carregue o PDF de entrada como um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Excluir as páginas listadas no array pages usando o [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salvar o atualizado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para um novo arquivo.

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## Tópicos Relacionados à Página

- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Adicionar páginas PDF em Python](/pdf/pt/python-net/add-pages/)
- [Mover páginas PDF em Python](/pdf/pt/python-net/move-pages/)
- [Extrair páginas PDF em Python](/pdf/pt/python-net/extract-pages/)
