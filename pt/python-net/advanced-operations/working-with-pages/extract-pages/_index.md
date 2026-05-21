---
title: Extrair Páginas PDF em Python
linktitle: Extraindo Páginas PDF
type: docs
weight: 80
url: /pt/python-net/extract-pages/
description: Aprenda como extrair páginas PDF individuais ou múltiplas para novos arquivos em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair páginas PDF usando Python
Abstract: Este artigo explica como extrair páginas de arquivos PDF usando Aspose.PDF for Python via .NET. Aprenda como copiar uma única página ou várias páginas para um novo documento usando indexação de páginas baseada em 1 e a API PageCollection.
---

## Extrair Página Única de um PDF

Extrair uma página específica de um documento PDF e salvá‑la como um novo arquivo. Usando a biblioteca Aspose.PDF, o script copia a página desejada para um novo PDF, deixando o documento original inalterado. Isso é útil para dividir PDFs ou isolar páginas importantes para distribuição.

1. Carregue o PDF de origem usando o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Crie um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para armazenar a página extraída.
1. Adicionar o desejado [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) do documento fonte para o novo PDF usando o documento de destino [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - Neste exemplo, a página 2 é extraída (indexação baseada em 1).
1. Salvar o novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com a página extraída para o arquivo de saída especificado.

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## Extrair Múltiplas Páginas de um PDF

Extrair várias páginas específicas de um documento PDF e salvá‑las em um novo arquivo. Usando a biblioteca Aspose.PDF, as páginas selecionadas são copiadas para um novo PDF enquanto o documento original permanece intacto. Isso é útil para criar PDFs menores contendo apenas as seções relevantes de um documento maior.

1. Carregue o PDF de origem usando o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Crie um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para armazenar as páginas extraídas.
1. Selecione as páginas a extrair (neste exemplo, páginas 2 e 3 usando indexação baseada em 1).
1. Adicione cada selecionado [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) do documento fonte para o novo PDF usando seu [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salvar o novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) com as páginas extraídas para o arquivo de saída especificado.

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## Tópicos de Página Relacionados

- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Excluir páginas PDF em Python](/pdf/pt/python-net/delete-pages/)
- [Mover páginas PDF em Python](/pdf/pt/python-net/move-pages/)
- [Dividir arquivos PDF em Python](/pdf/pt/python-net/split-document/)
