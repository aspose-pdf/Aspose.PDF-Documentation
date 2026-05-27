---
title: Gerenciar cabeçalhos e rodapés de PDF usando Python
linktitle: Gerenciar cabeçalhos e rodapés de PDF
type: docs
weight: 70
url: /pt/python-net/artifacts-header-footer/
description: Aprenda como gerenciar cabeçalhos e rodapés em documentos PDF com Python e Aspose.PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar, personalizar e remover cabeçalhos e rodapés de PDF usando Python
Abstract: Gerenciar cabeçalhos e rodapés é uma necessidade comum ao trabalhar com documentos PDF em negócios, publicação e fluxos de trabalho de automação. Este artigo demonstra como usar Aspose.PDF for Python para adicionar cabeçalhos e rodapés com aparência profissional, com estilo personalizado como fonte, tamanho, cor e alinhamento. Também mostra como detectar e remover artefatos de paginação existentes, como cabeçalhos e rodapés, de uma página PDF. Com funções reutilizáveis e exemplos claros, os desenvolvedores podem integrar rapidamente esses recursos em sistemas de processamento de documentos para branding, relatórios ou limpeza de arquivos.
---

## Criar Artefatos de Texto Estilizado

Esta função utilitária explica como criar um artefato de texto reutilizável para páginas PDF usando Aspose.PDF for Python. Ela foi projetada para gerar cabeçalhos ou rodapés estilizados com formatação consistente, incluindo configurações de Font, cor, tamanho e alinhamento. A função abstrai a criação do artefato para que possa ser reutilizada em diferentes decorações de texto a nível de página.

1. Instanciar o objeto artefato.
1. Definir o conteúdo de texto do artefato.
1. Aplicar estilo de texto.
1. Definir alinhamento.
1. Retornar artefato configurado.

```python
from os import path
import aspose.pdf as ap
import sys

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact

```

## Adicionar cabeçalho ao PDF

1. Abra o PDF de entrada.
1. Crie um HeaderArtifact com o texto "Sample Header".
1. Anexe‑o à primeira página.
1. Salve o PDF atualizado.

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Adicionar Rodapé ao PDF

1. Abra o PDF de entrada.
1. Crie um FooterArtifact com texto "Sample Footer".
1. Anexe‑o à primeira página.
1. Salve o arquivo de saída.

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Excluir Artefatos de Cabeçalho ou Rodapé

1. Abrir o PDF.
1. Encontre artefatos marcados como cabeçalhos ou rodapés de paginação.
1. Remova-os da primeira página.
1. Salve o documento limpo.

```python
from os import path
import aspose.pdf as ap
import sys

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## Tópicos de Artefatos Relacionados

- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)
- [Adicionar fundos PDF em Python](/pdf/pt/python-net/add-backgrounds/)
- [Adicionar numeração Bates ao PDF em Python](/pdf/pt/python-net/add-bates-numbering/)
- [Contar tipos de artefato em arquivos PDF](/pdf/pt/python-net/counting-artifacts/)