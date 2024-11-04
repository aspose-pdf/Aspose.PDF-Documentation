---
title: Trabalhando com Gráficos em PDF
linktitle: Trabalhando com Gráficos
type: docs
weight: 70
url: /cpp/graphs/
description: Este artigo explica o que é um Gráfico, como criar um objeto retângulo preenchido, como adicionar texto dentro de um objeto gráfico, como adicionar um objeto de linha ao PDF e etc.
lastmod: "2021-12-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## O que é um Gráfico

Adicionar gráficos a documentos PDF é uma tarefa muito comum para desenvolvedores ao trabalhar com o Adobe Acrobat Writer ou outras aplicações de processamento de PDF. Existem muitos tipos de gráficos que podem ser usados em aplicações PDF.
[Aspose.PDF for C++](/pdf/cpp/) também suporta a adição de gráficos a documentos PDF. Para este propósito, a classe Graph é fornecida. Graph é um elemento de nível de parágrafo e pode ser adicionado à coleção Paragraphs em uma instância Page. Uma instância Graph contém uma coleção de Shapes.

Os seguintes tipos de formas são suportados pela classe [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph):

- [Arc](/pdf/cpp/add-arc/) - às vezes também chamado de bandeira é um par ordenado de vértices adjacentes, mas às vezes também chamado de linha dirigida.
- [Circle](/pdf/cpp/add-circle/) - exibe dados usando um círculo dividido em setores. Usamos um gráfico de círculo (também chamado de gráfico de pizza) para mostrar como os dados representam partes de um todo ou de um grupo.
- [Curve](/pdf/cpp/add-curve/) - é uma união conectada de linhas projetivas, cada linha encontrando outras três em pontos duplos comuns.
- [Line](/pdf/cpp/add-line) - gráficos de linha são usados para exibir dados contínuos e podem ser úteis na previsão de eventos futuros quando mostram tendências ao longo do tempo.
- [Rectangle](/pdf/cpp/add-rectangle/) - é uma das muitas formas fundamentais que você verá em gráficos, pode ser muito útil para ajudá-lo a resolver um problema.
- [Ellipse](/pdf/cpp/add-ellipse/) - é um conjunto de pontos em um plano, criando uma forma oval e curva.

Os detalhes acima também são representados nas figuras abaixo:

![Figures in Graphs](graph.png)