---
title: Anotações adesivas PDF usando Python
linktitle: Anotação adesiva
type: docs
weight: 50
url: /pt/python-net/sticky-annotations/
description: Descubra como adicionar anotações adesivas em documentos PDF usando Aspose.PDF em Python via .NET para comentários e feedback.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guia sobre como manipular anotações adesivas em PDF
Abstract: Este artigo fornece um guia detalhado sobre como gerenciar anotações de marca d'água em documentos PDF usando a biblioteca Aspose.PDF para Python. Ele explica o processo de adicionar, recuperar e excluir anotações de marca d'água para garantir a autenticidade e a marca do documento. A anotação de marca d'água pode ser usada para incorporar gráficos, como logotipos, em um tamanho e posição fixos em uma página. O guia inclui trechos de código que demonstram como adicionar uma anotação de marca d'água em uma posição específica com opacidade ajustável, bem como como recuperar e excluir anotações de marca d'água existentes. Os exemplos de código ilustram o uso da biblioteca Aspose.PDF para manipular documentos PDF programaticamente, oferecendo uma abordagem prática para desenvolvedores integrarem funcionalidades de marca d'água em suas aplicações.
---

## Adicionar Anotação de Marca d'Água

A anotação de marca d'água é a mais visível e fácil de visualizar e transmitir. Esta é a melhor forma de colocar em seu documento PDF um logotipo ou qualquer outro sinal que confirme sua originalidade.

Uma anotação de marca d'água deve ser usada para representar gráficos que serão impressos em um tamanho e posição fixos em uma página, independentemente das dimensões da página impressa.

Você pode adicionar Texto de Marca d'água usando [WatermarkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/) em uma posição específica da página PDF. A opacidade da Marca d'água também pode ser controlada usando a propriedade [opacity](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/watermarkannotation/#properties).

Por favor, confira o trecho de código a seguir para adicionar WatermarkAnnotation.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create Annotation
    # Load Page object to add Annotation
    page = document.pages[1]

    # Create Annotation
    wa = ap.annotations.WatermarkAnnotation(page, ap.Rectangle(100, 0, 400, 100, True))

    # Add annotaiton into Annotation collection of Page
    page.annotations.append(wa)

    # Create TextState for Font settings
    ts = ap.text.TextState()
    ts.foreground_color = ap.Color.blue
    ts.font_size = 25
    ts.font = ap.text.FontRepository.find_font("Arial");

    # Set opacity level of Annotaiton Text
    wa.opacity = 0.5

    # Add Text in Annotation
    wa.set_text_and_state([ "HELLO", "Line 1", "Line 2" ], ts)

    document.save(output_file)
```

## Obter Anotação de Marca d'Água

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        print(ta.rect)
```

## Excluir Anotação de Marca d'Água

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    watermarkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.WATERMARK)
    ]

    for ta in watermarkAnnotations:
        document.pages[1].annotations.delete(ta)

    document.save(output_file)
```


