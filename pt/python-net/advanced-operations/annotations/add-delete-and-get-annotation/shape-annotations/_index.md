---
title: Anotações de Forma via Python
linktitle: Anotações de Forma
type: docs
weight: 20
url: /pt/python-net/shape-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de linha, quadrado, círculo, polígono e polilinha em documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Trabalhe com anotações geométricas de PDF em Python.
Abstract: Este artigo explica como criar, ler e remover anotações de forma em documentos PDF usando Aspose.PDF for Python via .NET. Ele cobre anotações de linha, quadrado, círculo, polígono e polilinha, com cada fluxo de trabalho dividido em pequenas etapas e exemplos de código completos.
---

Este artigo mostra como trabalhar com anotações de forma em documentos PDF usando Aspose.PDF for Python via .NET.

O script de exemplo demonstra vários fluxos de trabalho de anotação baseados em geometria:

- anotações de linha
- anotações quadradas
- anotações de círculo
- anotações de polígono
- anotações de polilinha

## Anotação de Linha 

### Adicionar Anotação de Linha 

Este exemplo adiciona uma anotação de linha à primeira página e configura estilos de seta, largura da linha e uma janela popup.

#### Abra o PDF de origem

```python
document = ap.Document(infile)
```

#### Criar e configurar a anotação de linha

```python
line_annotation = ap.annotations.LineAnnotation(
    document.pages[1],
    ap.Rectangle(550, 93, 562, 439, True),
    ap.Point(556, 99),
    ap.Point(556, 443),
)

line_annotation.title = "John Smith"
line_annotation.color = ap.Color.red
line_annotation.width = 3
line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW
```

#### Anexe o popup e salve o PDF

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 124, 1021, 266, True),
)
line_annotation.popup = popup

document.pages[1].annotations.append(line_annotation)
document.save(outfile)
```

#### Exemplo completo

```python
def line_annotation_add(infile, outfile):
    document = ap.Document(infile)

    line_annotation = ap.annotations.LineAnnotation(
        document.pages[1],
        ap.Rectangle(550, 93, 562, 439, True),
        ap.Point(556, 99),
        ap.Point(556, 443),
    )

    line_annotation.title = "John Smith"
    line_annotation.color = ap.Color.red
    line_annotation.width = 3
    line_annotation.starting_style = ap.annotations.LineEnding.OPEN_ARROW
    line_annotation.ending_style = ap.annotations.LineEnding.OPEN_ARROW

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 124, 1021, 266, True),
    )
    line_annotation.popup = popup

    document.pages[1].annotations.append(line_annotation)
    document.save(outfile)
```

### Obter Anotação de Linha 

Para inspecionar anotações de linha, filtre a coleção de anotações na primeira página e converta cada resultado para `LineAnnotation` para que você possa ler seus pontos de início e fim.

#### Carregue o PDF e colete anotações de linha

```python
document = ap.Document(infile)

line_annotation = [
    cast(ap.annotations.LineAnnotation, annotation)
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Imprima as coordenadas da linha

```python
for annotation in line_annotation:
    print(
        f"[{annotation.starting.x},{annotation.starting.y}]"
        f"-[{annotation.ending.x},{annotation.ending.y}]"
    )
```

#### Exemplo completo

```python
def line_annotations_get(infile, outfile):
    document = ap.Document(infile)

    line_annotation = [
        cast(ap.annotations.LineAnnotation, annotation)
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotation:
        print(
            f"[{annotation.starting.x},{annotation.starting.y}]"
            f"-[{annotation.ending.x},{annotation.ending.y}]"
        )
```

### Excluir anotação de linha 

Este fluxo de trabalho remove todas as anotações de linha da primeira página e salva o PDF atualizado.

#### Encontrar anotações de linha para remover

```python
document = ap.Document(infile)
page = document.pages[1]

line_annotations = [
    annotation
    for annotation in page.annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.LINE
]
```

#### Exclua as anotações e salve o PDF

```python
for annotation in line_annotations:
    page.annotations.delete(annotation)

document.save(outfile)
```

#### Exemplo completo

```python
def line_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    line_annotations = [
        annotation
        for annotation in page.annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.LINE
    ]

    for annotation in line_annotations:
        page.annotations.delete(annotation)

    document.save(outfile)
```


## Anotações de Quadrado e Círculo

### Adicionar Anotação Quadrada 

Anotações de quadrado são úteis para marcar áreas retangulares em um documento. Este exemplo cria uma anotação de quadrado com configurações de borda, preenchimento e transparência.

#### Abra o PDF e crie a anotação quadrada

```python
document = ap.Document(infile)

square_annotation = ap.annotations.SquareAnnotation(
    document.pages[1],
    ap.Rectangle(60, 600, 250, 450, True),
)
square_annotation.title = "John Smith"
square_annotation.color = ap.Color.blue
square_annotation.interior_color = ap.Color.blue_violet
square_annotation.opacity = 0.25
```

#### Adicione a anotação e salve o PDF

```python
document.pages[1].annotations.append(square_annotation)
document.save(outfile)
```

#### Exemplo completo

```python
def square_annotation_add(infile, outfile):
    document = ap.Document(infile)

    square_annotation = ap.annotations.SquareAnnotation(
        document.pages[1],
        ap.Rectangle(60, 600, 250, 450, True),
    )
    square_annotation.title = "John Smith"
    square_annotation.color = ap.Color.blue
    square_annotation.interior_color = ap.Color.blue_violet
    square_annotation.opacity = 0.25

    document.pages[1].annotations.append(square_annotation)
    document.save(outfile)
```

### Obter Anotação Quadrada 

Para inspecionar anotações quadradas, filtre as anotações da primeira página pelo `SQUARE` digite e imprima cada retângulo.

#### Carregue o documento e colete anotações quadradas

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]
```

#### Imprima os retângulos de anotação

```python
for annotation in square_annotations:
    print(annotation.rect)
```

#### Exemplo completo

```python
def square_annotation_get(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        print(annotation.rect)
```

### Excluir Anotação Quadrada 

Este fluxo de trabalho remove todas as anotações quadradas da primeira página e salva o documento.

#### Encontrar e excluir anotações quadradas

```python
document = ap.Document(infile)
square_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
]

for annotation in square_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemplo completo

```python
def square_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    square_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.SQUARE
    ]

    for annotation in square_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Adicionar Anotação de Círculo 

Anotações de círculo marcam áreas arredondadas em um PDF. Este exemplo adiciona uma anotação de círculo com cor de preenchimento, opacidade e uma anotação pop‑up.

#### Abra o PDF e crie a anotação de círculo

```python
document = ap.Document(infile)

circle_annotation = ap.annotations.CircleAnnotation(
    document.pages[1],
    ap.Rectangle(270, 160, 483, 383, True),
)
circle_annotation.title = "John Smith"
circle_annotation.color = ap.Color.red
circle_annotation.interior_color = ap.Color.misty_rose
circle_annotation.opacity = 0.5
```

#### Anexe o popup e salve o PDF

```python
circle_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 316, 1021, 459, True),
)

document.pages[1].annotations.append(circle_annotation)
document.save(outfile)
```

#### Exemplo completo

```python
def circle_annotation_add(infile, outfile):
    document = ap.Document(infile)

    circle_annotation = ap.annotations.CircleAnnotation(
        document.pages[1],
        ap.Rectangle(270, 160, 483, 383, True),
    )
    circle_annotation.title = "John Smith"
    circle_annotation.color = ap.Color.red
    circle_annotation.interior_color = ap.Color.misty_rose
    circle_annotation.opacity = 0.5
    circle_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 316, 1021, 459, True),
    )

    document.pages[1].annotations.append(circle_annotation)
    document.save(outfile)
```

### Obter Anotação de Círculo 

Para inspecionar anotações de círculo, filtre as anotações da página por `CIRCLE` digite e imprima seus retângulos.

#### Carregue o documento e colete anotações de círculo

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]
```

#### Imprima os retângulos de anotação

```python
for annotation in circle_annotations:
    print(annotation.rect)
```

#### Exemplo completo

```python
def circle_annotation_get(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        print(annotation.rect)
```

### Excluir anotação de círculo 

Este fluxo de trabalho remove todas as anotações de círculo da primeira página e salva o PDF de saída.

#### Localizar e excluir anotações de círculo

```python
document = ap.Document(infile)
circle_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
]

for annotation in circle_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemplo completo

```python
def circle_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    circle_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.CIRCLE
    ]

    for annotation in circle_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```


## Anotações de Polígono e Polilinha

### Adicionar anotação de polígono 

Anotações de polígono definem uma forma fechada de múltiplos pontos. Este exemplo cria uma anotação de polígono a partir de um retângulo e de uma lista de pontos.

#### Abra o PDF e crie a anotação de polígono

```python
document = ap.Document(infile)

polygon_annotation = ap.annotations.PolygonAnnotation(
    document.pages[1],
    ap.Rectangle(200, 300, 400, 400, True),
    [
        ap.Point(200, 300),
        ap.Point(220, 300),
        ap.Point(250, 330),
        ap.Point(300, 304),
        ap.Point(300, 400),
    ],
)
polygon_annotation.title = "John Smith"
polygon_annotation.color = ap.Color.blue
polygon_annotation.interior_color = ap.Color.blue_violet
polygon_annotation.opacity = 0.25
```

#### Adicione a anotação e salve o PDF

```python
document.pages[1].annotations.append(polygon_annotation)
document.save(outfile)
```

#### Exemplo completo

```python
def polygon_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polygon_annotation = ap.annotations.PolygonAnnotation(
        document.pages[1],
        ap.Rectangle(200, 300, 400, 400, True),
        [
            ap.Point(200, 300),
            ap.Point(220, 300),
            ap.Point(250, 330),
            ap.Point(300, 304),
            ap.Point(300, 400),
        ],
    )
    polygon_annotation.title = "John Smith"
    polygon_annotation.color = ap.Color.blue
    polygon_annotation.interior_color = ap.Color.blue_violet
    polygon_annotation.opacity = 0.25

    document.pages[1].annotations.append(polygon_annotation)
    document.save(outfile)
```

### Obter Anotação de Polígono 

Para inspecionar anotações de polígono, filtre as anotações da primeira página pelo `POLYGON` digite e imprima cada retângulo de anotação.

#### Carregue o documento e colete anotações de polígonos

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]
```

#### Imprima os retângulos de anotação

```python
for annotation in polygon_annotations:
    print(annotation.rect)
```

#### Exemplo completo

```python
def polygon_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        print(annotation.rect)
```

### Excluir Anotação de Polígono 

Este fluxo de trabalho remove todas as anotações de polígonos da primeira página e salva o PDF atualizado.

#### Encontrar e excluir anotações de polígono

```python
document = ap.Document(infile)
polygon_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
]

for annotation in polygon_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemplo completo

```python
def polygon_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polygon_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLYGON
    ]

    for annotation in polygon_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

### Adicionar Anotação de Polilinha 

Anotações de polilinha definem um caminho aberto através de múltiplos pontos. Este exemplo cria uma anotação de polilinha com uma nota pop-up.

#### Abra o PDF e crie a anotação de polilinha

```python
document = ap.Document(infile)

polyline_annotation = ap.annotations.PolylineAnnotation(
    document.pages[1],
    ap.Rectangle(270, 193, 571, 383, True),
    [
        ap.Point(545, 150),
        ap.Point(545, 190),
        ap.Point(667, 190),
        ap.Point(667, 110),
        ap.Point(626, 111),
    ],
)
polyline_annotation.title = "John Smith"
polyline_annotation.color = ap.Color.red
```

#### Anexe o popup e salve o PDF

```python
polyline_annotation.popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(842, 196, 1021, 338, True),
)

document.pages[1].annotations.append(polyline_annotation)
document.save(outfile)
```

#### Exemplo completo

```python
def polyline_annotation_add(infile, outfile):
    document = ap.Document(infile)

    polyline_annotation = ap.annotations.PolylineAnnotation(
        document.pages[1],
        ap.Rectangle(270, 193, 571, 383, True),
        [
            ap.Point(545, 150),
            ap.Point(545, 190),
            ap.Point(667, 190),
            ap.Point(667, 110),
            ap.Point(626, 111),
        ],
    )
    polyline_annotation.title = "John Smith"
    polyline_annotation.color = ap.Color.red
    polyline_annotation.popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(842, 196, 1021, 338, True),
    )

    document.pages[1].annotations.append(polyline_annotation)
    document.save(outfile)
```

### Obter Anotação de Polilinha 

Para inspecionar anotações de polilinha, filtre as anotações da página por `POLY_LINE` digite e imprima seus retângulos.

#### Carregue o documento e colete anotações de polilinha

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]
```

#### Imprima os retângulos de anotação

```python
for annotation in polyline_annotations:
    print(annotation.rect)
```

#### Exemplo completo

```python
def polyline_annotation_get(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        print(annotation.rect)
```

### Excluir Anotação PolyLine 

Este fluxo de trabalho remove todas as anotações de polilinha da primeira página e salva o PDF de saída.

#### Encontrar e excluir anotações de polilinha

```python
document = ap.Document(infile)
polyline_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
]

for annotation in polyline_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemplo completo

```python
def polyline_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    polyline_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.POLY_LINE
    ]

    for annotation in polyline_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Tópicos Relacionados

- [Importar e Exportar Anotações](/python-net/import-export-annotations/)
- [Anotações Interativas](/python-net/interactive-annotations/)
- [Anotações de marcação](/python-net/markup-annotations/)
- [Anotações de Mídia](/python-net/media-annotations/)
- [Anotações de Segurança](/python-net/security-annotations/)
- [Anotações Baseadas em Texto](/python-net/text-based-annotations/)
- [Anotações de Marca d'Água](/python-net/watermark-annotations/)
