---
title: Extrair Links PDF em Python
linktitle: Extrair Links
type: docs
weight: 30
url: /pt/python-net/extract-links/
description: Aprenda como extrair anotações de links e hyperlinks de documentos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair Links de PDF
Abstract: O guia Aspose.PDF for Python via .NET sobre extração de links explica como recuperar programaticamente anotações de hyperlink de documentos PDF usando Python. A documentação inclui exemplos práticos de código e destaca como essa funcionalidade pode ser usada para tarefas como auditoria de links, análise de navegação ou criação de recursos interativos em documentos. Seja trabalhando com PDFs de página única ou processando grandes lotes, este guia oferece uma abordagem clara e eficiente para a extração de hyperlinks.
---

## Extrair Links do Arquivo PDF

Este exemplo demonstra como iterar por todas as anotações de link na primeira página de um PDF usando Aspose.PDF for Python. Ele filtra as anotações para identificar aquelas do tipo LinkAnnotation, faz cast seguro delas e, em seguida, imprime o índice da página e a posição retangular na página.

Isso pode ser usado para depuração, análises ou atualizações automatizadas das anotações de link existentes em um PDF.

1. Carregue o documento PDF. Use ap.Document(path_infile) para abrir o arquivo.
1. Acesse as anotações da primeira página. Use document.pages[1].annotations para recuperar todas as anotações.
1. Filtre apenas os tipos LinkAnnotation. Verifique o annotation_type de cada anotação.
1. Faça cast e processe as LinkAnnotations. Use is_assignable() e cast() para garantir acesso seguro às propriedades de LinkAnnotation.
1. Imprima detalhes da anotação. Exiba o índice da página e o retângulo (localização) de cada link.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## Extrair HyperLinks do Arquivo PDF

Este código demonstra como extrair todos os objetos LinkAnnotation da primeira página de um documento PDF usando Aspose.PDF for Python, e então identificar aqueles que contêm um GoToURIAction. Para cada um desses links, ele imprime o índice da página e o URI de destino.

Isso é útil para tarefas como:

- Auditar links externos em um PDF
- Extrair URLs de documentação ou suporte
- Detectar hiperlinks quebrados ou desatualizados

1. Carregar o documento PDF. Abrir o arquivo usando ap.Document.
1. Obter todas as anotações de link da primeira página. Filtrar anotações para incluir apenas aquelas com o tipo AnnotationType.LINK.
1. Verifique o tipo e faça cast para LinkAnnotation. Certifique‑se de que cada anotação é realmente uma LinkAnnotation antes de acessar suas propriedades.
1. Verifique o tipo de ação do link. Filtre os links que utilizam um GoToURIAction (ou seja, links para um URL da web).
1. Extraia e imprima o URI e o índice da página. Use .uri para obter o link externo e .page_index para obter o contexto.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
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
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## Tópicos de Links Relacionados

- [Trabalhar com links de PDF em Python](/pdf/pt/python-net/links/)
- [Criar links de PDF em Python](/pdf/pt/python-net/create-links/)
- [Atualizar links em PDF usando Python](/pdf/pt/python-net/update-links/)