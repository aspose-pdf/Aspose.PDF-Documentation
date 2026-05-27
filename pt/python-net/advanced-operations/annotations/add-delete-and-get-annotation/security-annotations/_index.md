---
title: Anotações de Segurança usando Python
linktitle: Anotações de Segurança
type: docs
weight: 75
url: /pt/python-net/security-annotations/
description: Aprenda como marcar texto para remoção, aplicar anotações de remoção e remover áreas de imagens em arquivos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redigir conteúdo sensível de PDF em Python com anotações de segurança.
Abstract: Este artigo explica como trabalhar com anotações de segurança em documentos PDF usando Aspose.PDF for Python via .NET. Ele abrange a marcação de texto correspondente com anotações de redação, a aplicação permanente das redações e a redação de áreas de imagem selecionadas com base nos retângulos de posicionamento de imagem detectados.
---

Este artigo mostra como usar anotações de segurança em documentos PDF com Aspose.PDF for Python via .NET.

O script de exemplo demonstra três fluxos de trabalho comuns de redação:

- marcar fragmentos de texto com anotações de redação
- aplicar permanentemente anotações de redação existentes
- censurar uma área de imagem detectada em uma página

## Marcar Redação de Texto

Este fluxo de trabalho procura por texto correspondente no documento e coloca anotações de redação sobre cada correspondência. Ele ainda não remove o conteúdo; apenas marca o texto para posterior redação.

### Abra o PDF e procure o texto alvo

Criar um `TextFragmentAbsorber` para o termo de pesquisa e habilite as opções de pesquisa de texto padrão antes de analisar todas as páginas.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### Criar anotações de redação para cada correspondência

Para cada fragmento de texto correspondido, crie um `RedactionAnnotation` usando o retângulo de fragmento e configure sua aparência visual.

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### Salvar o PDF marcado

```python
document.save(outfile)
```

### Exemplo completo

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```

## Aplicar Redação

Depois que as anotações de redação foram adicionadas, este fluxo de trabalho as aplica permanentemente na primeira página. Uma vez aplicadas, o conteúdo original é removido da saída do documento.

### Carregue o PDF e colete anotações de redação

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### Aplique cada anotação de redação

O exemplo verifica que cada anotação pode ser tratada como um `RedactionAnnotation` antes de chamar `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### Salvar o PDF redigido

```python
document.save(outfile)
```

### Exemplo completo

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```

## Área de Redação

Este exemplo censura uma área de imagem detectada em vez de texto. Ele varre a página em busca de posicionamentos de imagens, seleciona um retângulo de posicionamento e adiciona uma anotação de censura sobre essa área.

### Abra o PDF e detecte a colocação de imagens

Usar `ImagePlacementAbsorber` para encontrar as posições das imagens na primeira página.

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### Criar uma anotação de redação para a área de imagem selecionada

O exemplo usa a terceira colocação de imagem detectada e aplica a mesma estilização de redação usada no exemplo de marcação de texto.

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### Adicione a anotação e salve o PDF

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### Exemplo completo

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## Tópicos Relacionados

- [Importar e Exportar Anotações](/python-net/import-export-annotations/)
- [Anotações Interativas](/python-net/interactive-annotations/)
- [Anotações de marcação](/python-net/markup-annotations/)
- [Anotações de Mídia](/python-net/media-annotations/)
- [Anotações de Forma](/python-net/shape-annotations/)
- [Anotações Baseadas em Texto](/python-net/text-based-annotations/)
- [Anotações de Marca d'Água](/python-net/watermark-annotations/)
