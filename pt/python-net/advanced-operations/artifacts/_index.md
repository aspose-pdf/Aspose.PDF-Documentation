---
title: Trabalhando com Artefatos em Python via .NET
linktitle: Trabalhando com Artefatos
type: docs
weight: 170
url: /pt/python-net/artifacts/
description: Aspose.PDF para Python via .NET permite adicionar uma imagem de fundo às páginas PDF e obter cada marca d'água usando a classe Artifact.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar Artefatos ao PDF usando Python
Abstract: Este artigo explora o conceito e a aplicação de artefatos em documentos PDF, enfocando particularmente seu papel na melhoria da acessibilidade e desempenho. Artefatos são elementos não‑conteúdo, como componentes decorativos ou de layout, que não transmitem significado ao documento. O artigo destaca o uso da classe `Artifact` na biblioteca Aspose.PDF para Python via .NET para gerenciar esses elementos, oferecendo propriedades como `custom_type`, `contents` e `opacity` para personalização detalhada. Também apresenta classes relacionadas para manipular tipos específicos de artefatos. Exemplos práticos demonstram operações como recuperar marcas d'água, adicionar imagens de fundo, contar tipos de artefatos e implementar numeração Bates.
---

Artefatos em PDF são objetos gráficos ou outros elementos que não fazem parte do conteúdo real do documento. Eles geralmente são usados para decoração, layout ou fins de fundo. Exemplos de artefatos incluem cabeçalhos de página, rodapés, separadores ou imagens que não transmitem nenhum significado.

O objetivo dos artefatos em PDF é permitir a distinção entre elementos de conteúdo e não‑conteúdo. Isso é importante para a acessibilidade, pois leitores de tela e outras tecnologias assistivas podem ignorar os artefatos e focar no conteúdo relevante. Os artefatos também podem melhorar o desempenho e a qualidade dos documentos PDF, pois podem ser omitidos na impressão, pesquisa ou cópia.

Para criar um elemento como artefato em PDF, você precisa usar a classe [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/).
Ele contém as seguintes propriedades úteis:

- **custom_type** - Obtém o nome do tipo de artefato. Pode ser usado se o tipo de artefato for não padrão.
- **custom_subtype** - Obtém o nome do subtipo de artefato. Pode ser usado se o subtipo de artefato não for um subtipo padrão.
- **type** - Obtém o tipo de artefato.
- **subtype** - Obtém o subtipo de artefato. Se o artefato tiver subtipo não padrão, o nome do subtipo pode ser lido via CustomSubtype.
- **contents** - Obtém a coleção de operadores internos do artefato.
- **form** - Obtém o XForm do artefato (se XForm for usado).
- **rectangle** - Obtém o retângulo do artefato.
- **position** - Obtém ou define a posição do artefato. Se esta propriedade for especificada, as margens e alinhamentos são ignorados.
- **right_margin** - Margem direita do artefato. Se a posição for especificada explicitamente (na propriedade Position), este valor é ignorado.
- **left_margin** - Margem esquerda do artefato. Se a posição for especificada explicitamente (na propriedade Position), este valor é ignorado.
- **top_margin** - Margem superior do artefato. Se a posição for especificada explicitamente (na propriedade Position), este valor é ignorado.
- **bottom_margin** - Margem inferior do artefato. Se a posição for especificada explicitamente (na propriedade Position), este valor é ignorado.
- **artifact_horizontal_alignment** - Alinhamento horizontal do artefato. Se a posição for especificada explicitamente (na propriedade Position), este valor é ignorado.
- **artifact_vertical_alignment** - Alinhamento vertical do artefato. Se a posição for especificada explicitamente (na propriedade Position), este valor é ignorado.
- **rotation** - Obtém ou define o ângulo de rotação do artefato.
- **text** - Obtém o texto do artefato.
- **image** - Obtém a imagem do artefato (se presente).
- **opacity** - Obtém ou define a opacidade do artefato. Valores possíveis estão no intervalo 0..1.
- **lines** - Linhas de texto multilinha do artefato.
- **text_state** - Estado de texto para o texto do artefato.
- **is_background** - Se verdadeiro, o Artefato é colocado atrás do conteúdo da página.

As classes a seguir também podem ser úteis para trabalhar com artefatos:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [Bates Numbering](https://reference.aspose.com/pdf/python-net/aspose.pdf/)

Por favor, reveja as seguintes seções do artigo:

- [Adicionando fundos](/pdf/python-net/add-backgrounds/) - adicione imagem de fundo ao seu arquivo PDF com Python.
- [Adicionando numeração Bates](/pdf/python-net/add-bates-numbering/) - adicione numeração Bates ao PDF.
- [Adicionando marca d'água](/pdf/python-net/add-watermarks/) - como adicionar marca d'água ao PDF com Python.
- [Contando artefatos](/pdf/python-net/counting-artifacts/) - contando artefatos em PDF usando Python.

