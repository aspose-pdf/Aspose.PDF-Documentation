---
title: Atualizar links PDF em Python
linktitle: Atualizar links
type: docs
weight: 20
url: /pt/python-net/update-links/
description: Aprenda como atualizar a aparência e os destinos dos links PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como atualizar links em PDF
Abstract: O guia Aspose.PDF for Python via .NET sobre atualização de links orienta os desenvolvedores no processo de modificar o comportamento de hyperlinks em documentos PDF usando Python. Ele explica como alterar os destinos dos links para apontar para páginas específicas, sites externos ou até mesmo outros arquivos PDF. A documentação também aborda como ajustar a aparência das anotações de link, incluindo a cor do texto, e fornece exemplos de código práticos para cada cenário. Seja corrigindo URLs desatualizadas ou aprimorando a navegação, este recurso oferece uma abordagem clara e eficiente para gerenciar links programaticamente.
---

## Atualizar a Cor do Texto da LinkAnnotation

Este exemplo mostra como detectar todas as anotações de link na primeira página de um PDF usando Aspose.PDF for Python, então destacar o texto próximo a cada link alterando a cor da fonte para vermelho. Ele usa TextFragmentAbsorber com uma área ligeiramente expandida ao redor de cada retângulo de link para encontrar e modificar o texto próximo.

Isso pode ser usado para:

- Marcar visualmente links em um documento
- Aprimorar a acessibilidade enfatizando o conteúdo vinculado
- Pré-processamento de arquivos PDF antes da revisão ou exportação

Para cada uma dessas anotações de link, o script recupera seu limite retangular e expande ligeiramente essa região para incluir texto próximo, permitindo uma identificação visual mais ampla. Em seguida, aplica um TextFragmentAbsorber sobre essa área expandida para extrair quaisquer fragmentos de texto localizados nela. Esses fragmentos capturados são modificados alterando a cor da fonte para vermelho, marcando efetivamente o texto ao redor para ênfase e revisão. Após aplicar todas essas atualizações, o documento modificado é salvo no caminho de saída, preservando as anotações destacadas e seu texto associado.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## Atualizar borda

O script concentra-se na primeira página do documento e filtra todas as anotações, selecionando apenas aquelas do tipo LINK—geralmente representam elementos interativos, como hyperlinks ou gatilhos de navegação. Para cada uma dessas anotações de link, o código as converte para o tipo LinkAnnotation e atualiza sua propriedade de cor para vermelho, destacando-as visualmente para se sobressair ao restante do conteúdo. Após todas as anotações de link terem sido modificadas, o documento atualizado é salvo no local de saída definido, preservando o novo estilo.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## Atualizar Destino da Web

Uma vez que os caminhos estejam configurados, o documento original é carregado usando a biblioteca Aspose.PDF, tornando seu conteúdo acessível para modificação. O script então foca na primeira página do documento, filtrando todas as anotações e selecionando apenas aquelas do tipo link, que tipicamente representam áreas clicáveis ou hiperlinks. Para evitar erros de tipo e garantir um manuseio seguro, cada anotação é verificada com is_assignable e então convertida para o tipo adequado LinkAnnotation. Se o link estiver associado a uma GoToURIAction, significando que aponta para um endereço web, o script atualiza esse URI para redirecionar os usuários para "https://www.aspose.com". Finalmente, depois que todas as alterações desejadas foram aplicadas, o documento modificado é salvo no caminho de saída especificado.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## Tópicos de Links Relacionados

- [Trabalhar com links de PDF em Python](/pdf/pt/python-net/links/)
- [Criar links de PDF em Python](/pdf/pt/python-net/create-links/)
- [Extrair links de PDF em Python](/pdf/pt/python-net/extract-links/)