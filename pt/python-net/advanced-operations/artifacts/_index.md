---
title: Trabalhar com Artefatos PDF em Python
linktitle: Trabalhando com Artefatos
type: docs
weight: 170
url: /pt/python-net/artifacts/
description: Aprenda como trabalhar com artefatos PDF em Python para adicionar fundos, marcas d'água e numeração Bates e contar tipos de artefatos com Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar artefatos de fundos, marcas d'água e numeração Bates em Python
Abstract: Este artigo explica como trabalhar com artefatos PDF no Aspose.PDF for Python via .NET. Aprenda o que são os artefatos, por que são importantes para acessibilidade e layout de documentos, e como adicionar imagens de fundo, aplicar marcas d'água, adicionar numeração Bates e inspecionar tipos de artefatos em arquivos PDF com Python.
---

Os artefatos em PDF são objetos gráficos ou outros elementos que não fazem parte do conteúdo real do documento. Eles geralmente são usados para decoração, layout ou fins de fundo. Exemplos de artefatos incluem cabeçalhos de página, rodapés, separadores ou imagens que não transmitem nenhum significado.

O objetivo dos artefatos em PDF é permitir a distinção entre elementos de conteúdo e não‑conteúdo. Isso é importante para acessibilidade, pois leitores de tela e outras tecnologias assistivas podem ignorar os artefatos e focar no conteúdo relevante. Os artefatos também podem melhorar o desempenho e a qualidade dos documentos PDF, pois podem ser omitidos da impressão, pesquisa ou cópia.

Use esta seção quando precisar criar ou inspecionar elementos PDF não‑conteúdo em Python, como fundos de documento, marcas d'água de página e marcas de numeração Bates. Os guias a seguir mostram os principais fluxos de trabalho de artefatos suportados pelo Aspose.PDF for Python via .NET.

Para criar um elemento como artefato em PDF, você precisa usar o [Artefato](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) classe.
Ele contém as seguintes propriedades úteis:

- **custom_type** - Obtém o nome do tipo de artefato. Pode ser usado se o tipo de artefato for não padrão.
- **custom_subtype** - Obtém o nome do subtipo do artefato. Pode ser usado se o subtipo do artefato não for um subtipo padrão.
- **type** - Obtém o tipo do artefato.
- **subtype** - Obtém o subtipo do artefato. Se o artefato tem um subtipo não padrão, o nome do subtipo pode ser lido via CustomSubtype.
- **contents** - Obtém a coleção de operadores internos do artefato.
- **form** - Obtém o XForm do artefato (se XForm for usado).
- **rectangle** - Obtém o retângulo do artefato.
- **position** - Obtém ou define a posição do artefato. Se esta propriedade for especificada, as margens e alinhamentos são ignorados.
- **right_margin** - Margem direita do artefato.Se a posição for especificada explicitamente (na propriedade Position) este valor é ignorado.
- **left_margin** - Margem esquerda do artefato.Se a posição for especificada explicitamente (na propriedade Position) este valor é ignorado.
- **top_margin** - Margem superior do artefato. Se a posição for especificada explicitamente (na propriedade Position) este valor é ignorado.
- **bottom_margin** - Margem inferior do artefato.Se a posição for especificada explicitamente (na propriedade Position) este valor é ignorado.
- **artifact_horizontal_alignment** - Alinhamento horizontal do artefato. Se a posição for especificada explicitamente (na propriedade Position) este valor é ignorado.
- **artifact_vertical_alignment** - Alinhamento vertical do artefato. Se a posição for especificada explicitamente (na propriedade Position) este valor será ignorado.
- **rotation** - Obtém ou define o ângulo de rotação do artefato.
- **text** - Obtém o texto do artefato.
- **image** - Obtém a imagem do artefato (se presente).
- **opacity** - Obtém ou define a opacidade do artefato. Valores possíveis estão no intervalo 0..1.
- **lines** - Linhas do artefato de texto multilinha.
- **text_state** - Estado de texto para texto de artefato.
- **is_background** - Se verdadeiro, o Artefato é colocado atrás do conteúdo da página.

As seguintes classes também podem ser úteis para trabalhar com artefatos:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [BatesNArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)

## Fluxos de Trabalho de Artefato Cobertos Nesta Seção

Por favor, revise as seguintes seções do artigo:

- [Adicionando fundos](/pdf/pt/python-net/add-backgrounds/) - adicione uma imagem de fundo ao seu arquivo PDF com Python.
- [Adicionando numeração Bates](/pdf/pt/python-net/add-bates-numbering/) - adicione numeração Bates ao PDF.
- [Adicionando marca d'água](/pdf/pt/python-net/add-watermarks/) - como adicionar marca d'água a um PDF com Python.
- [Contando Artefatos](/pdf/pt/python-net/counting-artifacts/) - contando Artefatos em PDF usando Python.
- [Gerenciar cabeçalhos e rodapés de PDF](/pdf/pt/python-net/artifacts-header-footer/) - gerenciar cabeçalhos e rodapés em documentos PDF.

Esses tutoriais são úteis quando você precisa gerenciar elementos decorativos ou estruturais de PDF sem alterar o fluxo de conteúdo principal do documento.
