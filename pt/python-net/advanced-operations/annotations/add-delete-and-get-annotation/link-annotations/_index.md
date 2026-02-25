---
title: Usando Anotações de Link em PDF
linktitle: Anotações de Link
type: docs
weight: 70
url: /pt/python-net/link-annotations/
description: Aspose.PDF para Python via .NET permite que você Adicione, Recupere e Exclua Anotações de Link do seu documento PDF.
lastmod: "2025-07-28"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
---

## Adicionar Anotação de Link em um arquivo PDF existente

[Links](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) são anotações que abrem URLs ou movem para determinadas posições dentro do mesmo documento ou de um documento externo quando você clica.

Uma Anotação de Link é uma área retangular que pode ser colocada em qualquer lugar da página. Cada link tem uma ação PDF correspondente associada a ele. Essa ação é executada quando o usuário clica na área desse link.

O trecho de código a seguir mostra como adicionar Anotação de Link a um arquivo PDF usando um exemplo de número de telefone:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```

### Obter Anotação de Link

Por favor, experimente usar o trecho de código a seguir para Obter [Anotação de Link](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) do documento PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### Excluir Anotação de Link

O trecho de código a seguir mostra como Excluir Anotação de Link de um arquivo PDF. Para isso, precisamos encontrar e remover todas as anotações de link na primeira página. Depois disso, salvaremos o documento com a anotação removida.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```
