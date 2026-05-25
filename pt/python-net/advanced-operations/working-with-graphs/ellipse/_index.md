---
title: Adicionar formas de elipse ao PDF em Python
linktitle: Adicionar elipse
type: docs
weight: 60
url: /pt/python-net/add-ellipse/
description: Aprenda como desenhar, preencher e rotular formas de elipse em arquivos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhar formas de elipse em arquivos PDF usando Python
Abstract: Este artigo mostra como adicionar formas elípticas a documentos PDF com Aspose.PDF for Python via .NET. Ele cobre elipses contornadas, elipses preenchidas e a inserção de texto dentro de objetos elipse.
---

## Adicionar objeto Elipse

Aspose.PDF for Python via .NET permite que você adicione [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) formas para páginas PDF com o [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) classe. Você pode desenhar contornos de elipse, aplicar cores de preenchimento e colocar texto dentro de objetos elipse.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(150, 100, 120, 60)
    ellipse1.graph_info.color = ap.Color.green_yellow
    ellipse1.text = ap.text.TextFragment("Ellipse")
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(50, 50, 18, 300)
    ellipse2.graph_info.color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Adicionar elipse](ellipse.png)

## Criar Objeto Elipse Preenchida

O trecho de código a seguir mostra como adicionar um [Ellipse](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/ellipse/) objeto que está preenchido com cor.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def create_ellipse_filled(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    ellipse1 = drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    graph.shapes.add(ellipse1)

    ellipse2 = drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Elipse Preenchida](fill_ellipse.png)

## Adicionar texto dentro da elipse

O Aspose.PDF for Python via .NET também permite colocar texto dentro de objetos de forma. O exemplo a seguir adiciona texto a formas de elipse.

```python
import aspose.pdf as ap
import aspose.pdf.drawing as drawing

def add_text_inside_ellipse(outfile: str):
    document = ap.Document()
    page = document.pages.add()
    graph = drawing.Graph(400, 400)
    graph.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.green)

    text_fragment = ap.text.TextFragment("Ellipse")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Helvetica")
    text_fragment.text_state.font_size = 24

    ellipse1 = ap.drawing.Ellipse(100, 100, 120, 180)
    ellipse1.graph_info.fill_color = ap.Color.green_yellow
    ellipse1.text = text_fragment
    graph.shapes.add(ellipse1)

    ellipse2 = ap.drawing.Ellipse(200, 150, 180, 120)
    ellipse2.graph_info.fill_color = ap.Color.dark_red
    ellipse2.text = text_fragment
    graph.shapes.add(ellipse2)

    page.paragraphs.add(graph)
    document.save(outfile)
```

![Texto dentro da Ellipse](text_ellipse.png)

## Tópicos Relacionados ao Gráfico

- [Trabalhar com gráficos PDF em Python](/pdf/pt/python-net/working-with-graphs/)
- [Adicionar formas de círculo ao PDF em Python](/pdf/pt/python-net/add-circle/)
- [Adicionar formas de curva ao PDF em Python](/pdf/pt/python-net/add-curve/)
- [Adicionar formas de retângulo ao PDF em Python](/pdf/pt/python-net/add-rectangle/)
