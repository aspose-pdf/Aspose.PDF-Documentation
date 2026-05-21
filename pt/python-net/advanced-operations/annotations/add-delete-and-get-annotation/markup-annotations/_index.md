---
title: Anotações de marcação usando Python
linktitle: Anotações de marcação
type: docs
weight: 30
url: /pt/python-net/markup-annotations/
description: Aprenda como adicionar, ler e excluir anotações de texto, cursor e substituição em documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabalhe com anotações de marcação em arquivos PDF usando Python.
Abstract: Este artigo explica como criar, inspecionar e remover anotações de marcação em documentos PDF usando Aspose.PDF for Python via .NET. Ele cobre anotações de texto, anotações de cursor e anotações de substituição, com cada fluxo de trabalho dividido em pequenas etapas e exemplos de código.
---

Este artigo mostra como trabalhar com anotações de marcação em documentos PDF usando Aspose.PDF for Python via .NET.

O script de exemplo demonstra três fluxos de trabalho comuns de anotação:

- anotações de texto para comentários em estilo de nota
- anotações de caret para marcadores de inserção
- substituir anotações por marcação de substituição de texto

## Anotações de texto

### Adicionar Anotações de Texto

Este exemplo cria uma anotação de texto na primeira página e a vincula a uma janela pop-up. Anotações de texto são úteis para comentários estilo post-it em fluxos de revisão.

#### Abra o PDF de origem

```python
document = ap.Document(infile)
```

#### Criar e configurar a anotação de texto

Defina o retângulo da anotação e defina seu título, assunto, conteúdo, sinalizadores de exibição, cor e ícone.

```python
text_annotation = ap.annotations.TextAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
)
text_annotation.title = "Aspose User"
text_annotation.subject = "Sticky Note"
text_annotation.contents = (
    "This is a text annotation added by Aspose.PDF for Python via .NET"
)
text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
text_annotation.color = ap.Color.blue
text_annotation.icon = ap.annotations.TextIcon.HELP
```

#### Criar a anotação pop-up

Crie uma janela pop-up e conecte-a à anotação de texto.

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
)
popup.open = True

text_annotation.popup = popup
```

#### Adicione a anotação e salve o PDF

```python
document.pages[1].annotations.add(text_annotation, consider_rotation=False)
document.save(outfile)
```

#### Exemplo completo

```python
def text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = (
        "This is a text annotation added by Aspose.PDF for Python via .NET"
    )
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
    )
    popup.open = True

    text_annotation.popup = popup

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)
```

### Obter Anotações de Texto

Para inspecionar anotações de texto existentes, filtre a coleção de anotações na primeira página e mantenha apenas os itens cujo tipo é `TEXT`.

#### Carregue o documento e colete anotações de texto

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Imprima os retângulos de anotação

```python
for annotation in text_annotations:
    print(annotation.rect)
```

#### Exemplo completo

```python
def text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)
```

### Excluir anotações de texto

Este fluxo de trabalho remove todas as anotações de texto da primeira página e salva o PDF modificado.

#### Encontrar anotações de texto para remover

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Exclua as anotações e salve o arquivo

```python
for annotation in text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Exemplo completo

```python
def text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Anotações de cursor

### Adicionar Anotações de Cursor

Anotações de cursor são usadas para marcar pontos de inserção em cenários de revisão. Este exemplo adiciona uma anotação de cursor com uma nota popup anexada.

#### Abra o Document e obtenha a página de destino

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Criar e configurar a anotação caret

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
)
caret_annotation.title = "Aspose User"
caret_annotation.subject = "Inserted text 1"
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.color = ap.Color.blue
```

#### Anexe o popup e salve o documento

```python
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
page.annotations.append(caret_annotation)

document.save(outfile)
```

#### Exemplo completo

```python
def caret_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)
```

### Obter Anotações de Cursor

Para inspecionar anotações caret, itere pelas anotações da página e filtre por `CARET` tipo de anotação.

#### Carregue o documento e a página

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Imprimir retângulos de anotação de cursor

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.CARET:
        print(annot.rect)
```

#### Exemplo completo

```python
def caret_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            print(annot.rect)
```

### Excluir anotações de caret

Este fluxo de trabalho coleta anotações de cursor primeiro, exclui‑as uma por uma e, em seguida, salva o arquivo atualizado.

#### Carregue o documento e colete anotações de cursor

```python
document = ap.Document(infile)
page = document.pages[1]

caret_annotations = [
    annot
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.CARET
]
```

#### Exclua as anotações e salve o documento

```python
for annot in caret_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Exemplo completo

```python
def caret_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotations = [
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    for annot in caret_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

## Substituir Anotações

### Adicionar Substituir Anotações

Anotações de substituição combinam uma anotação de caret e uma anotação de tachado agrupada. Esse padrão marca o texto que deve ser substituído e vincula a nota de substituição ao conteúdo riscado.

#### Abra o documento e obtenha a página

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Criar a anotação caret para texto de substituição

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
)
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.subject = "Inserted text 2"
caret_annotation.title = "Aspose User"
caret_annotation.color = ap.Color.blue
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
```

#### Criar a anotação de tachado agrupada

Defina a área de tachado, atribua pontos quad e vincule-a à anotação de cursor através de `in_reply_to` e `reply_type`.

```python
strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
)
strikeout_annotation.color = ap.Color.blue
strikeout_annotation.quad_points = [
    ap.Point(321.66, 739.416),
    ap.Point(365.664, 739.416),
    ap.Point(321.66, 728.508),
    ap.Point(365.664, 728.508),
]
strikeout_annotation.subject = "Cross-out"
strikeout_annotation.in_reply_to = caret_annotation
strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP
``` 

#### Adicione ambas as anotações e salve o PDF

```python
page.annotations.append(caret_annotation)
page.annotations.append(strikeout_annotation)

document.save(outfile)
```

#### Exemplo completo

```python
def replace_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508),
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    document.save(outfile)
```

### Obter Substituir Anotações

Para identificar anotações de substituição, encontre anotações de tachado que estejam agrupadas como respostas a outra anotação. O exemplo converte cada anotação de tachado antes de verificar seus campos de relacionamento.

#### Carregue o documento e itere pelas anotações

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Filtrar anotações de tachado agrupadas

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
        sa = cast(ap.annotations.StrikeOutAnnotation, annot)
        if (
            sa.in_reply_to is not None
            and sa.reply_type == ap.annotations.ReplyType.GROUP
        ):
            print(f"Replace annotation rect: {sa.rect}")
```

#### Exemplo completo

```python
def replace_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (
                sa.in_reply_to is not None
                and sa.reply_type == ap.annotations.ReplyType.GROUP
            ):
                print(f"Replace annotation rect: {sa.rect}")
```

### Excluir Substituir Anotações

Este fluxo de trabalho coleta anotações de tachado usadas para substituir marcações, remove-as da página e salva o PDF de saída.

#### Carregue o documento e colete anotações de substituição

```python
document = ap.Document(infile)
page = document.pages[1]

replace_annotations = [
    cast(ap.annotations.StrikeOutAnnotation, annot)
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]
```

#### Exclua as anotações e salve o documento

```python
for annot in replace_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Exemplo completo

```python
def replace_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annot in replace_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```
