---
title: Adicionar numeração Bates ao PDF em Python
linktitle: Adicionando numeração Bates
type: docs
weight: 10
url: /pt/python-net/add-bates-numbering/
description: Aprenda como adicionar e remover numeração Bates em documentos PDF usando Python com Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar numeração Bates via Python
Abstract: Bates numbering é um recurso crítico em fluxos de trabalho de documentos jurídicos, médicos e empresariais, garantindo que cada página de um conjunto receba um identificador único e sequencial para referência confiável. Este artigo demonstra como o Aspose.PDF for Python via .NET simplifica a automação da numeração Bates por meio de sua API flexível. Usando a classe BatesNArtifact, os desenvolvedores podem configurar o comportamento da numeração — incluindo contagem de dígitos, prefixos, sufixos, alinhamento e margens — e aplicá‑la programaticamente em documentos inteiros. São apresentadas várias abordagens, desde a aplicação direta do artefato até a configuração baseada em delegados, oferecendo controle estático e dinâmico. Além disso, a API suporta a remoção completa dos números Bates com uma única chamada de método, permitindo o gerenciamento total do ciclo de vida dos artefatos de paginação. Exemplos de código claros e passo a passo ilustram como adicionar, personalizar e excluir a numeração Bates, tornando este guia um recurso prático para desenvolvedores que buscam otimizar fluxos de trabalho de processamento de documentos.
---

A numeração Bates é amplamente utilizada em fluxos de trabalho jurídicos, médicos e empresariais para atribuir identificadores únicos e sequenciais às páginas de um conjunto de documentos. Aspose.PDF for Python via .NET oferece uma API simples e flexível para automatizar esse processo, permitindo que você aplique números Bates padronizados programaticamente em qualquer PDF.

Usando o [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) classe, os desenvolvedores podem personalizar totalmente o comportamento da numeração — incluindo o número inicial, a contagem de dígitos, prefixos e sufixos, alinhamento e margens. Uma vez configurado, o artefato pode ser aplicado ao [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) através do `add_bates_numbering` método no [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) ou adicionado como parte de uma lista de [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) objects. Aspose.PDF também suporta um estilo de configuração baseado em delegate, permitindo o controle dinâmico das configurações de artefatos em tempo de execução.

Além de criar números Bates, a API fornece uma maneira fácil de removê-los usando `delete_bates_numbering`, oferecendo total flexibilidade nos fluxos de trabalho de processamento de documentos.

Este artigo mostra vários métodos para adicionar e remover numeração Bates em um PDF usando Aspose.PDF for Python via .NET, com exemplos claros de configuração, aplicação e remoção de artefatos.

## Adicionando Artefato de Numeração Bates

Este exemplo mostra como adicionar programaticamente a numeração Bates a um documento PDF usando Aspose.PDF for Python via .NET. Configurando um [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) com as configurações desejadas e aplicando‑as às páginas do documento, você pode automatizar o processo de adicionar identificadores padronizados a cada página.

Para adicionar um artefato de numeração Bates a um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), chame o `AddBatesNumbering(BatesNArtifact)` método de extensão em [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), passando um [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) instância como parâmetro:

```python
import sys
from os import path
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Adicionar numeração Bates usando artefatos de paginação

Adicionar numeração Bates a um PDF usando a coleção de artefatos de paginação no Aspose.PDF for Python:

1. Carregue o documento PDF.
1. Insira páginas extras se necessário antes de aplicar a numeração.
1. Crie um artefato Bates.
1. Configure as propriedades do artefato.
1. Adicione o artefato à coleção de paginação.
1. Aplicar paginação nas páginas.
1. Salve o documento atualizado.

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Excluir numeração Bates

Para remover a numeração Bates de um [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), use o `delete_bates_numbering()` método no [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Tópicos de Artefatos Relacionados

- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)
- [Adicionar marcas d'água ao PDF em Python](/pdf/pt/python-net/add-watermarks/)
- [Adicionar fundos PDF em Python](/pdf/pt/python-net/add-backgrounds/)
- [Contar tipos de artefato em arquivos PDF](/pdf/pt/python-net/counting-artifacts/)