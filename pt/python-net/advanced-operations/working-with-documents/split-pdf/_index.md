---
title: Dividir arquivos PDF em Python
linktitle: Dividir arquivos PDF
type: docs
weight: 60
url: /pt/python-net/split-pdf-document/
description: Aprenda como dividir páginas de PDF em arquivos PDF separados em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dividindo páginas de PDF usando Python
Abstract: O artigo discute o processo de dividir páginas de PDF em arquivos individuais usando Python, destacando a utilidade desse recurso para gerenciar documentos PDF grandes. Ele faz referência ao Aspose.PDF Splitter, uma ferramenta online projetada para demonstrar a funcionalidade de divisão de PDFs. O artigo fornece um método detalhado para alcançar isso em aplicações Python, envolvendo a iteração pelas páginas de um documento PDF através da `PageCollection` do objeto `Document`. Para cada página, um novo objeto `Document` é criado, a página é adicionada a ele e o novo arquivo PDF é salvo usando o método `save()`. Um trecho de código Python acompanhante ilustra esse processo, mostrando as etapas necessárias para dividir um documento PDF em arquivos separados ao iterar pelas suas páginas e salvar cada uma como um PDF individual.
---

Dividir páginas de PDF pode ser um recurso útil para quem deseja dividir um arquivo grande em páginas individuais ou grupos de páginas.

Use este fluxo de trabalho quando precisar dividir PDFs grandes em arquivos de uma única página ou em conjuntos de documentos menores para distribuição, revisão ou processamento subsequente.

## Exemplo ao vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) é um aplicativo web gratuito online que permite investigar como a funcionalidade de divisão de apresentação funciona.

[![Aspose.PDF Splitter](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tópico mostra como dividir páginas PDF em arquivos PDF individuais em seus aplicativos Python. Para dividir páginas PDF em arquivos PDF de página única usando Python, os seguintes passos podem ser seguidos:

1. Percorra as páginas do documento PDF através do [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) do objeto [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) coleção
1. Para cada iteração, crie um novo objeto Document e adicione o individual [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objeto no documento vazio
1. Salvar o novo PDF usando [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método

## Divida PDF em vários arquivos ou PDFs separados em Python

O trecho de código Python a seguir mostra como dividir páginas de PDF em arquivos PDF individuais.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## Divida um PDF em duas partes iguais

1. Carregue o documento PDF.
1. Determine o número total de páginas.
1. Calcule o ponto médio.
1. Crie o primeiro documento de saída.
1. Remover as páginas da segunda metade do primeiro documento.
1. Salve a primeira parte.
1. Crie o segundo documento de saída.
1. Remover as páginas da primeira metade do segundo documento.
1. Salvar a segunda parte.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## Dividir um PDF em vários arquivos a cada N páginas

Divida um documento PDF em vários arquivos menores com base em um número fixo de páginas usando Aspose.PDF for Python.

1. Carregue o documento PDF.
1. Determine o número total de páginas.
1. Definir páginas por parte.
1. Iterar pelo documento em blocos.
1. Calcule o intervalo de páginas para cada parte.
1. Crie um novo documento para cada parte.
1. Copie páginas para o novo documento.
1. Salvar o documento dividido.
1. Repita até que todas as páginas sejam processadas.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## Dividir um PDF por intervalos de páginas personalizados

Divida um documento PDF em vários arquivos com base em intervalos de páginas definidos de forma personalizada usando Aspose.PDF for Python.

1. Carregue o documento PDF.
1. Determine o número total de páginas.
1. Crie uma lista de tuplas representando intervalos (start_page, end_page).
1. Iterar pelos intervalos definidos.
1. Validar a página inicial.
1. Ajuste a página final.
1. Valide o intervalo efetivo.
1. Crie um novo documento para cada intervalo.
1. Copie páginas para o novo documento.
1. Salve cada documento dividido.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## Divida um PDF em Primeira Página e Páginas Restantes

Separe a primeira página de um documento PDF do restante das páginas usando Aspose.PDF for Python.

1. Carregue o documento PDF.
1. Determine o número total de páginas.
1. Verifique se o documento está vazio.
1. Crie um documento para a primeira página.
1. Adicionar a primeira página.
1. Salvar o documento da primeira página.
1. Verifique se há páginas adicionais.
1. Crie um documento para as páginas restantes.
1. Copiar páginas restantes.
1. Salvar o documento das páginas restantes.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## Divida um PDF em Última Página e Páginas Anteriores

Extraia a última página de um documento PDF e separe-a das páginas restantes usando Aspose.PDF for Python.

1. Carregue o documento PDF.
1. Determine o número total de páginas.
1. Verifique se o documento está vazio.
1. Crie um documento para a última página.
1. Adicionar a última página.
1. Salvar o documento da última página.
1. Verificar documentos de página única.
1. Remova a última página do documento original.
1. Salvar as páginas restantes.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## Dividir um PDF em três partes

Divida um documento PDF em três partes separadas usando o Aspose.PDF for Python.

1. Carregue o documento PDF.
1. Determine o número total de páginas.
1. Verifique se o documento está vazio.
1. Calcule o tamanho da parte.
1. Iterar através de três partes.
1. Determine o intervalo de páginas para cada parte.
1. Validar o intervalo de páginas.
1. Crie um novo documento para cada parte.
1. Copiar páginas para o documento da parte.
1. Salvar cada parte.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## Divisor de Página PDF Personalizado

Divida um documento PDF em vários arquivos com base em grupos de páginas definidos customizados usando Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## Dividir PDF em Páginas Individuais com Nomes de Arquivo Estáveis

Divida um documento PDF em páginas individuais e salve-as com nomes de arquivo estáveis usando o Aspose.PDF para Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## Dividir PDF em Páginas Ímpares e Pares

Divida um documento PDF em dois arquivos separados contendo, respectivamente, páginas ímpares e pares, usando Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## Tópicos Relacionados ao Documento

- [Trabalhe com documentos PDF em Python](/pdf/pt/python-net/working-with-documents/)
- [Mesclar arquivos PDF em Python](/pdf/pt/python-net/merge-pdf-documents/)
- [Otimizar arquivos PDF em Python](/pdf/pt/python-net/optimize-pdf/)
- [Manipular documentos PDF em Python](/pdf/pt/python-net/manipulate-pdf-document/)

