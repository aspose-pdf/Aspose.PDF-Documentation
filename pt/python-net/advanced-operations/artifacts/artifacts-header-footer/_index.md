---
title: Adicionar cabeçalhos e rodapés de PDF em Python
linktitle: Adicionar cabeçalhos e rodapés
type: docs
weight: 70
url: /pt/python-net/artifacts-header-footer/
description: Adicionar artefatos de cabeçalho e rodapé estilizados às páginas de PDF em Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar cabeçalhos e rodapés em um PDF com Python
Abstract: Adicionar artefatos de cabeçalho e rodapé estilizados às páginas de PDF em Python.
---

Usar `HeaderArtifact` e `FooterArtifact` para adicionar texto em execução às páginas PDF. Estes exemplos adicionam artefatos à primeira página.

## Criar artefatos de texto formatado

Defina a função auxiliar antes de executar qualquer um dos exemplos de adição. Ela aplica a mesma fonte, tamanho, cor e alinhamento aos cabeçalhos e rodapés.

```python
import aspose.pdf as ap

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

Passe `HeaderArtifact` para a função auxiliar e adicione o artefato resultante à página.

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Adicionar rodapé ao PDF

Passe `FooterArtifact` para a função auxiliar e adicione o artefato resultante à página.

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Tópicos relacionados

- [Remover Cabeçalhos e Rodapés](/pdf/pt/python-net/remove-headers-footers/)
- [Trabalhar com artefatos PDF em Python](/pdf/pt/python-net/artifacts/)
