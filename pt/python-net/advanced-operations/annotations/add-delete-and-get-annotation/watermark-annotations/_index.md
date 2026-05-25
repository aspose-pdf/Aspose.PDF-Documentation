---
title: Anotações de Marca d'água usando Python
linktitle: Anotações de Marca d'Água
type: docs
weight: 70
url: /pt/python-net/watermark-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações de marca d'água em documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabalhe com anotações de marca d'água em arquivos PDF usando Python.
Abstract: Este artigo explica como criar, ler e remover anotações de marca d'água em documentos PDF usando Aspose.PDF for Python via .NET. Ele abrange a adição de uma anotação de marca d'água de texto com estado de texto personalizado e opacidade, a inspeção de anotações de marca d'água existentes e a exclusão de anotações de marca d'água de uma página PDF.
---

Este artigo mostra como trabalhar com anotações de marca d'água em documentos PDF usando Aspose.PDF for Python via .NET.

O script de exemplo demonstra três fluxos de trabalho comuns:

- adicionar uma anotação de marca d'água
- obter retângulos de anotação de marca d'água
- excluir anotações de marca d'água

## Adicionar Anotação de Marca d'água

Este exemplo adiciona uma anotação de marca d'água à primeira página de um documento PDF. A marca d'água usa um estado de texto para controlar as configurações de fonte e aplica opacidade personalizada para uma aparência semitransparente.

### Abra o PDF e obtenha a página de destino

```python
document = ap.Document(infile)
page = document.pages[1]
```

### Criar a anotação de marca d'água

Defina o retângulo da anotação e adicione-o à coleção de anotações da página.

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### Configure a aparência do texto

Criar um `TextState` objeto para controlar a cor do texto, o tamanho da fonte e a família da fonte.

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### Definir opacidade e texto da marca d'água

O exemplo usa opacidade de 50% e escreve três linhas de texto na anotação de marca d'água.

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### Salvar o PDF

```python
document.save(outfile)
```

### Exemplo completo

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## Obter Anotação de Marca d'água

Para inspecionar anotações de marca d'água existentes, filtre as anotações da primeira página pelo `WATERMARK` digite e imprima seus retângulos.

### Carregue o documento e colete as anotações de marca d'água

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Imprima os retângulos de anotação

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### Exemplo completo

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## Excluir anotação de marca d'água

Este fluxo de trabalho remove todas as anotações de marca d'água da primeira página e salva o PDF atualizado.

### Encontrar anotações de marca d'água para remover

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Exclua as anotações e salve o PDF

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### Exemplo completo

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## Tópicos Relacionados

- [Importar e Exportar Anotações](/python-net/import-export-annotations/)
- [Anotações Interativas](/python-net/interactive-annotations/)
- [Anotações de marcação](/python-net/markup-annotations/)
- [Anotações de Mídia](/python-net/media-annotations/)
- [Anotações de Segurança](/python-net/security-annotations/)
- [Anotações de Forma](/python-net/shape-annotations/)
- [Anotações Baseadas em Texto](/python-net/text-based-annotations/)
