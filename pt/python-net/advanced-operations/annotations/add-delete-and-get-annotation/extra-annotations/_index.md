---
title: Anotações Extras usando Python
linktitle: Anotações Extras
type: docs
weight: 60
url: /pt/python-net/extra-annotations/
description: Aprenda como adicionar anotações extras, como destaques ou notas, a PDFs em Python com Aspose.PDF para aprimorar o conteúdo PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guia sobre como manipular anotações extras em PDF
Abstract: O artigo fornece um guia abrangente sobre como adicionar, recuperar e excluir diferentes tipos de anotações em um arquivo PDF usando Python, especificamente com a biblioteca Aspose.PDF. Ele cobre três tipos de anotações – Caret, Link e Redaction. O artigo explica que as anotações Caret são usadas para sugestões de edição de texto. Descreve o processo de carregar um arquivo PDF, criar uma anotação Caret com parâmetros específicos (como retângulo, título, assunto, flags e cor), anexá‑la ao documento e salvar as alterações. Trechos de código são fornecidos para adicionar, recuperar e excluir anotações Caret. As anotações Link são usadas para criar áreas clicáveis que redirecionam para URLs ou posições específicas do documento. O guia inclui instruções e código para adicionar uma anotação Link identificando um fragmento de texto (ex., um número de telefone), definindo uma ação e gerenciando essas anotações.
---

## Como adicionar Anotação Caret a um arquivo PDF existente via Python

Anotação Caret é um símbolo que indica edição de texto. Anotação Caret também é uma anotação de marcação, portanto a classe Caret herda da classe Markup e também fornece funções para obter ou definir propriedades da Anotação Caret e redefinir o fluxo da aparência da Anotação Caret.
Anotações Caret são frequentemente usadas para sugerir alterações, adições ou modificações no texto.

Etapas para criar a anotação Caret:

1. Carregue o arquivo PDF - novo [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crie uma nova [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) e defina os parâmetros Caret (novo Rectangle, título, assunto, flags, cor). Esta anotação é usada para indicar a inserção de texto.
1. Depois que pudermos anexar anotações à página.

O trecho de código a seguir mostra como adicionar Anotação Caret a um arquivo PDF:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Aspose User"
    caretAnnotation1.subject = "Inserted text 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```

### Obter Anotação Caret

Por favor, experimente usar o trecho de código a seguir para obter a Anotação Caret em um documento PDF

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        print(ca.rect)
```

### Excluir Anotação Caret

O trecho de código a seguir mostra como excluir a Anotação Caret de um arquivo PDF usando Python.

```python

    import aspose.pdf as ap

    # Load the PDF file
    document = ap.Document(input_file)
    caretAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.CARET)
    ]

    for ca in caretAnnotations:
        document.pages[1].annotations.delete(ca)

    document.save(output_file)
```

## Redigir determinada região da página com Anotação de Redação usando Aspose.PDF para Python

O Aspose.PDF para Python via .NET oferece o recurso de adicionar e manipular Anotações em um arquivo PDF existente. As Anotações de Redação em documentos PDF têm a finalidade de remover ou ocultar permanentemente informações confidenciais do documento. O processo de edição dessas informações envolve cobrir ou sombrear conteúdo específico, como texto, imagens ou gráficos, de forma a restringir sua visibilidade e acessibilidade a terceiros. Isso garante que as informações sensíveis permanecam escondidas e protegidas dentro do documento. Para atender a essa necessidade, uma classe chamada [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/) é fornecida, que pode ser usada para redigir determinadas regiões da página ou para manipular RedactionAnnotations existentes e redigi‑las (ou seja, achatar a anotação e remover o texto subjacente).

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    page = document.pages[1]
    redactionAnnotation = ap.annotations.RedactionAnnotation(page, ap.Rectangle(270, 190, 371, 250, True))
    redactionAnnotation.title = "John Smith"
    redactionAnnotation.fill_color = ap.Color.light_gray
    redactionAnnotation.color = ap.Color.red
    redactionAnnotation.redact()

    page.annotations.append(redactionAnnotation)
    document.save(output_file)
```

### Obter Anotação de Redação

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        print(pa.rect)
```

### Excluir Anotação de Redação

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    redactionAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.REDACTION)
    ]

    for pa in redactionAnnotations:
        document.pages[1].annotations.delete(pa)

    document.save(output_file)
```



