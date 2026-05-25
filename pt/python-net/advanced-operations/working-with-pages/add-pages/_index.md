---
title: Adicionar páginas PDF em Python
linktitle: Adicionando páginas
type: docs
weight: 10
url: /pt/python-net/add-pages/
description: Aprenda como adicionar ou inserir páginas em documentos PDF em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar ou inserir páginas PDF com Python
Abstract: Este artigo explica como adicionar páginas a arquivos PDF usando Aspose.PDF for Python via .NET. Aprenda como inserir páginas em branco em posições específicas, anexar páginas ao final de um documento e importar uma página de outro PDF usando as APIs Document e PageCollection.
---

Aspose.PDF for Python via .NET oferece operações flexíveis em nível de página para documentos PDF. Você pode gerenciar páginas através de [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) e adicionar páginas a um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) em posições específicas ou ao final do arquivo.

Use esta página quando precisar inserir novas páginas em branco em um PDF existente ou acrescentar páginas ao final de um documento durante fluxos de trabalho de geração.

## Adicionar ou Inserir Páginas em um Arquivo PDF

Aspose.PDF for Python via .NET suporta tanto a inserção de página em um índice específico quanto a anexação de páginas ao final de um PDF.

### Inserir uma Página Vazia em um Arquivo PDF

Para inserir uma página vazia em um arquivo PDF:

1. Abrir um existente [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando métodos apropriados.
1. Insira uma nova página vazia em um índice específico usando o [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` método.
1. Salvar o modificado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) para o caminho de saída desejado.

Inserir uma página vazia em um arquivo PDF existente em uma posição especificada:

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Adicionar uma Página em Branco ao Final de um Arquivo PDF

Às vezes, você deseja garantir que um documento termine em uma página em branco. Este tópico explica como inserir uma página em branco ao final do documento PDF.

Para inserir uma página em branco ao final de um arquivo PDF:

1. Abrir um existente [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) usando métodos apropriados.
1. Adicione uma nova página em branco ao final do documento usando o [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` método.
1. Salvar o atualizado [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

O trecho de código a seguir mostra como inserir uma página vazia no final de um arquivo PDF.

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### Adicionar uma página de outro documento PDF

Com Aspose.PDF for Python via .NET, você pode criar um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), adicione uma página inicial e, em seguida, importe uma página de outro PDF para ela.

1. Criar um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Adicionar um novo em branco [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) e escreva algum texto nele usando [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Abra outro existente [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Copiar um [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) do documento.
1. Cole a página copiada no seu documento principal usando [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o arquivo combinado.

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## Tópicos Relacionados da Página

- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Mover páginas PDF em Python](/pdf/pt/python-net/move-pages/)
- [Excluir páginas de PDF em Python](/pdf/pt/python-net/delete-pages/)
- [Extrair páginas de PDF em Python](/pdf/pt/python-net/extract-pages/)
