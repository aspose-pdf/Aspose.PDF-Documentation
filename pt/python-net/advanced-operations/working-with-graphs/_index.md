---
title: Trabalhando com Gráficos em PDF usando Python
linktitle: Trabalhando com Gráficos
type: docs
weight: 70
url: /pt/python-net/working-with-graphs/
description: Este artigo explica o que é um Gráfico, como criar um objeto de retângulo preenchido e outras funções
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionando Gráficos ao PDF usando Python
Abstract: O artigo discute a integração de gráficos em documentos PDF, uma necessidade comum para desenvolvedores que utilizam o Adobe Acrobat Writer ou ferramentas de processamento de PDF semelhantes. Ele apresenta a classe Graph em Aspose.PDF for Python via .NET, que facilita essa tarefa ao permitir a adição de vários tipos de formas a documentos PDF. A classe Graph é um elemento de nível de parágrafo que pode ser inserido na coleção Paragraphs de uma instância Page e suporta uma coleção de formas, incluindo Arc, Circle, Curve, Line, Rectangle e Ellipse. Cada forma tem um propósito único, como Arcs representando adjacência, Circles ilustrando porções de dados, Curves representando linhas conectadas, Lines exibindo tendências contínuas de dados, Rectangles resolvendo problemas espaciais e Ellipses formando formas ovais. O artigo também fornece representações visuais dessas formas para auxiliar a compreensão.
---

## O que é um Gráfico

Adicionar gráficos a documentos PDF é uma tarefa muito comum para desenvolvedores que trabalham com Adobe Acrobat Writer ou outros aplicativos de processamento de PDF. Existem muitos tipos de gráficos que podem ser usados em aplicações PDF.
[Aspose.PDF for Python via .NET](/pdf/python-net/) também suporta a adição de gráficos a documentos PDF. Para esse fim, a classe Graph é fornecida. Graph é um elemento de nível de parágrafo e pode ser adicionada à coleção Paragraphs em uma instância Page. Uma instância Graph contém uma coleção de Shapes.

Os seguintes tipos de formas são suportados pela classe [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/):

- [Arc](/pdf/python-net/add-arc/) - às vezes também chamado de bandeira é um par ordenado de vértices adjacentes, mas às vezes também chamado de linha dirigida.
- [Circle](/pdf/python-net/add-circle/) - exibe dados usando um círculo dividido em setores. Usamos um gráfico de círculo (também chamado de gráfico de pizza) para mostrar como os dados representam porções de um todo ou de um grupo.
- [Curve](/pdf/python-net/add-curve/) - é uma união conectada de linhas projetivas, cada linha encontrando outras três em pontos duplos comuns.
- [Line](/pdf/python-net/add-line) - gráficos de linha são usados para exibir dados contínuos e podem ser úteis na previsão de eventos futuros quando mostram tendências ao longo do tempo.
- [Rectangle](/pdf/python-net/add-rectangle/) - é uma das muitas formas fundamentais que você encontrará em gráficos, e pode ser muito útil para ajudar a resolver um problema.
- [Ellipse](/pdf/python-net/add-ellipse/) - é um conjunto de pontos em um plano, criando uma forma oval e curva.

Os detalhes acima também são mostrados nas figuras abaixo:

![Figuras em Gráficos](graphs.png)


