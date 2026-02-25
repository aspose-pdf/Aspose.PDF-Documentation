---
title: Extrair Links do Arquivo PDF usando Python
linktitle: Extrair Links
type: docs
weight: 30
url: /pt/python-net/extract-links/
description: Descubra como extrair hiperligações de documentos PDF em Python usando Aspose.PDF para gerenciamento de conteúdo e análise de links.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair Links de PDF
Abstract: O guia Aspose.PDF para Python via .NET sobre extração de links explica como recuperar programaticamente anotações de hiperligações de documentos PDF usando Python. A documentação inclui exemplos de código práticos e destaca como essa funcionalidade pode ser usada para tarefas como auditoria de links, análise de navegação ou criação de recursos interativos em documentos. Seja trabalhando com PDFs de página única ou processando grandes lotes, este guia oferece uma abordagem clara e eficiente para a extração de hiperligações.
---

## Extrair Links do Arquivo PDF

Este exemplo demonstra como iterar por todas as anotações de link na primeira página de um PDF usando Aspose.PDF para Python. Ele filtra as anotações para identificar aquelas do tipo LinkAnnotation, faz a conversão segura e, em seguida, imprime o índice da página e a posição retangular na página.

Isso pode ser usado para depuração, análise ou atualizações automatizadas de anotações de link existentes em um PDF.

1. Carregue o documento PDF. Use ap.Document(path_infile) para abrir o arquivo.
1. Acesse as anotações da primeira página. Use document.pages[1].annotations para recuperar todas as anotações.
1. Filtre apenas tipos LinkAnnotation. Verifique o annotation_type de cada anotação.
1. Converta e processe LinkAnnotations. Use is_assignable() e cast() para garantir acesso seguro às propriedades do LinkAnnotation.
1. Imprima os detalhes da anotação. Saída do índice da página e do retângulo (localização) de cada link.

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## Extrair Hiperlinks do Arquivo PDF

Este código demonstra como extrair todos os objetos LinkAnnotation da primeira página de um documento PDF usando Aspose.PDF para Python, e então identificar aqueles que contêm um GoToURIAction. Para cada link, ele imprime o índice da página e o URI de destino.

Isso é útil para tarefas como:

- Auditar links externos em um PDF
- Extrair URLs de documentação ou suporte
- Detectar hiperlinks quebrados ou desatualizados

1. Carregue o documento PDF. Abra o arquivo usando ap.Document.
1. Obtenha todas as anotações de link da primeira página. Filtre as anotações para incluir apenas aquelas com o tipo AnnotationType.LINK.
1. Verifique o tipo e converta para LinkAnnotation. Certifique-se de que cada anotação seja realmente um LinkAnnotation antes de acessar suas propriedades.
1. Verifique o tipo de ação do link. Filtre links que utilizam um GoToURIAction (ou seja, links para uma URL web).
1. Extraia e imprima o URI e o índice da página. Use .uri para obter o link externo e .page_index para o contexto.

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```
