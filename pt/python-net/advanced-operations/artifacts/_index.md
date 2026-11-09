---
title: Trabalhe com artefatos PDF em Python
linktitle: Trabalhando com Artefatos
type: docs
weight: 170
url: /pt/python-net/artifacts/
description: Adicione, inspecione e remova artefatos PDF em Python, incluindo fundos, marcas d'água, cabeçalhos, rodapés e numeração Bates.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerencie artefatos de página PDF em Python
Abstract: Encontre guias para adicionar e remover artefatos PDF, inspecionar detalhes de marcas d'água e contar artefatos de paginação por subtipo com Aspose.PDF for Python via .NET.
---

Artefatos PDF marcam elementos de página como fundos decorativos, cabeçalhos e rodapés correntes e marcas d'água. Em um Tagged PDF, tecnologias assistivas podem pular artefatos e focar no conteúdo significativo do documento.

## Escolher um guia

### Adicionar artefatos

- [Adicionar fundos](/pdf/pt/python-net/add-backgrounds/)
- [Adicionar marcas d'água](/pdf/pt/python-net/add-watermarks/)
- [Adicionar numeração Bates](/pdf/pt/python-net/add-bates-numbering/)
- [Adicionar cabeçalhos e rodapés](/pdf/pt/python-net/artifacts-header-footer/)

### Inspecionar artefatos

- [Contar artefatos de paginação por subtipo](/pdf/pt/python-net/counting-artifacts/)
- [Extrair detalhes da marca d'água](/pdf/pt/python-net/extract-watermarks/)

### Remover artefatos

- [Remover fundos](/pdf/pt/python-net/remove-backgrounds/)
- [Remover marcas d'água](/pdf/pt/python-net/remove-watermarks/)
- [Remover numeração Bates](/pdf/pt/python-net/remove-bates-numbering/)
- [Remover cabeçalhos e rodapés](/pdf/pt/python-net/remove-headers-footers/)

## API de artefatos

A propriedade `artifacts` retorna a coleção [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/) da página. A classe [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) fornece as propriedades comuns às classes especializadas [`BackgroundArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/), [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/), [`HeaderArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/), [`FooterArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/) e [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/).

| Tarefa | Propriedades |
| --- | --- |
| Identificar o artefato | Usar `type` e `subtype` para classificações padrão e `custom_type` e `custom_subtype` para nomes personalizados. |
| Inspecione seu conteúdo | Usar `text`, `image`, e `lines` para texto e imagens, ou `contents` e `form` para operadores PDF e o XForm associado. |
| Posicione-o na página | Usar `rectangle` para inspecionar seus limites. Definir `position` para posicionamento explícito ou uso `left_margin`, `right_margin`, `top_margin`, `bottom_margin`, `artifact_horizontal_alignment`, e `artifact_vertical_alignment`. Uma posição explícita substitui margens e alinhamento. |
| Controle sua aparência | Usar `rotation`, `opacity` (de 0 a 1), e `text_state`. Definir `is_background` para colocar o artefato atrás do conteúdo da página. |
