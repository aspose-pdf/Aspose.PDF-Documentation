---
title: Adicionando Artefato de Numeração Bates em Python via .NET
linktitle: Adicionando Numeração Bates
type: docs
weight: 10
url: /pt/python-net/add-bates-numbering/
description: Aspose.PDF para Python via .NET permite que você adicione Numeração Bates a PDFs.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Numeração Bates via Python
Abstract: A numeração Bates é um recurso crítico em fluxos de trabalho de documentos jurídicos, médicos e empresariais, garantindo que cada página de um conjunto receba um identificador único e sequencial para referência confiável. Este artigo demonstra como o Aspose.PDF para Python via .NET simplifica a automação da numeração Bates por meio de sua API flexível. Usando a classe BatesNArtifact, os desenvolvedores podem configurar o comportamento da numeração — incluindo quantidade de dígitos, prefixos, sufixos, alinhamento e margens — e aplicá‑la programaticamente em documentos inteiros. São apresentadas várias abordagens, desde a aplicação direta do artefato até a configuração baseada em delegados, oferecendo controle estático e dinâmico. Além disso, a API suporta a remoção completa dos números Bates com uma única chamada de método, permitindo o gerenciamento de ciclo de vida completo dos artefatos de paginação. Exemplos de código claros e passo a passo ilustram como adicionar, personalizar e excluir a numeração Bates, tornando este guia um recurso prático para desenvolvedores que buscam otimizar fluxos de trabalho de processamento de documentos.
---

A numeração Bates é amplamente usada em fluxos de trabalho jurídicos, médicos e empresariais para atribuir identificadores únicos e sequenciais às páginas dentro de um conjunto de documentos. O Aspose.PDF para Python via .NET oferece uma API simples e flexível para automatizar este processo, permitindo que você aplique números Bates padronizados programaticamente em qualquer PDF.

Usando a classe [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) os desenvolvedores podem personalizar totalmente o comportamento da numeração — incluindo o número inicial, quantidade de dígitos, prefixos e sufixos, alinhamento e margens. Uma vez configurado, o artefato pode ser aplicado ao [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) através do método `add_bates_numbering` na [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) ou adicionado como parte de uma lista de objetos [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/). O Aspose.PDF também suporta um estilo de configuração baseado em delegados, permitindo controle dinâmico das configurações do artefato em tempo de execução.

Além de criar números Bates, a API fornece uma maneira fácil de removê‑los usando `delete_bates_numbering`, oferecendo flexibilidade total nos fluxos de trabalho de processamento de documentos.

Este artigo mostra múltiplos métodos para adicionar e remover numeração Bates em um PDF usando o Aspose.PDF para Python via .NET, com exemplos claros de configuração, aplicação e remoção de artefatos.

## Adicionando Artefato de Numeração Bates

Este exemplo mostra como adicionar programaticamente a numeração Bates a um documento PDF usando o Aspose.PDF para Python via .NET. Ao configurar um [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) com as definições desejadas e aplicá‑lo às páginas do documento, você pode automatizar o processo de adicionar identificadores padronizados a cada página.

Para adicionar um artefato de numeração Bates a um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), chame o método de extensão `AddBatesNumbering(BatesNArtifact)` na [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), passando uma instância de [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) como parâmetro:

```python

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

Ou, você pode passar uma coleção de objetos [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/):

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

Adicione um artefato de numeração Bates usando um delegate de ação:

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## Excluir Numeração Bates

Para remover a numeração Bates de um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), use o método `delete_bates_numbering()` na [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```
