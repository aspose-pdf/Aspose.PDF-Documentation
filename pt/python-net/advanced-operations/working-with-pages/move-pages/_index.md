---
title: Mover páginas PDF em Python
linktitle: Movendo páginas PDF
type: docs
weight: 100
url: /pt/python-net/move-pages/
description: Aprenda como mover páginas PDF dentro de um documento ou entre documentos em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mover páginas PDF entre documentos em Python
Abstract: Este artigo explica como mover páginas em PDFs usando Aspose.PDF for Python via .NET. Aprenda como mover uma única página ou várias páginas para outro documento e como reposicionar uma página dentro do mesmo PDF usando as APIs Document e PageCollection.
---

## Mover uma Página de um Documento PDF para Outro

Aspose.PDF for Python permite mover uma página (não apenas copiá‑la) de um PDF para outro. Ele remove a página selecionada do documento original e, em seguida, a adiciona a um novo arquivo PDF.

Pense nisso como recortar uma página de um livro e colá‑la em outro — a página deixa de existir no arquivo original após a movimentação.

1. Abra o documento PDF de origem usando o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Selecione uma página específica para mover (neste caso, página 2) — isso se refere a um [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Crie um novo documento PDF (instancie outro [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Adicione a página selecionada ao novo documento PDF usando o documento de destino [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (por exemplo, `another_document.pages.add(page)`).
1. Exclua a página do documento original por meio de seu [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (por exemplo, `document.pages.delete(index)`).
1. Salve ambos os documentos.

O trecho de código a seguir mostra como mover uma página.

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## Mover várias páginas de um PDF Document para outro

Ao contrário da cópia, esta operação transfere as páginas selecionadas — removendo-as do arquivo de origem e salvando-as em um novo PDF.

1. Crie um novo documento de destino vazio (`Document`).
1. Selecione várias páginas (neste caso, as páginas 1 e 3) do documento de origem [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Percorra as páginas selecionadas e adicione cada uma ao documento de destino [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o documento de destino contendo as páginas movidas.
1. Exclua as páginas movidas do documento de origem usando seu [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o documento fonte modificado com um novo nome de arquivo para preservar ambas as versões.

O trecho de código a seguir mostra como mover várias páginas.

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## Mover uma página para um novo local no mesmo documento PDF

Ele mostra como mover uma página específica para uma posição diferente dentro do mesmo documento — uma necessidade comum ao reorganizar ou editar layouts de PDF.

1. Carregue o documento PDF de entrada usando o [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Selecione a página que você deseja mover (página 2) — isso é um [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Adicione ao final do documento usando o documento [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Exclua a página original de sua localização anterior via o [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Salve o documento modificado como um novo arquivo.

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## Tópicos de Página Relacionados

- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Adicionar páginas PDF em Python](/pdf/pt/python-net/add-pages/)
- [Excluir páginas PDF em Python](/pdf/pt/python-net/delete-pages/)
- [Extrair páginas PDF em Python](/pdf/pt/python-net/extract-pages/)
