---
title: Anotações Extras usando Python
linktitle: Anotações Extras
type: docs
weight: 60
url: /pt/python-net/extra-annotations/
description: Esta seção descreve como adicionar, obter e deletar tipos extras de anotações do seu documento PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Anotações Extras usando Python",
    "alternativeHeadline": "Como adicionar Anotações Extras em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, anotação de link, anotação de acento",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe Aspose.PDF Doc",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/extra-annotations/"
    },
    "dateModified": "2023-02-04",
    "description": "Esta seção descreve como adicionar, obter e deletar tipos extras de anotações do seu documento PDF com Python."
}
</script>


## Como adicionar Anotação de Plica em um arquivo PDF existente via Python

A Anotação de Plica é um símbolo que indica a edição de texto. A Anotação de Plica também é uma anotação de marcação, então a classe Caret deriva da classe Markup e também fornece funções para obter ou definir propriedades da Anotação de Plica e redefinir o fluxo da aparência da Anotação de Plica. As anotações de plica são frequentemente usadas para sugerir alterações, adições ou modificações no texto.

Passos com os quais criamos anotação de plica:

1. Carregar o arquivo PDF - novo [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Criar nova [CaretAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/caretannotation/) e definir parâmetros de Plica (novo Retângulo, título, assunto, bandeiras, cor). Esta anotação é usada para indicar a inserção de texto.
3. Uma vez que somos capazes de anexar anotações à página.

O trecho de código a seguir mostra como adicionar Anotação de Plica a um arquivo PDF:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_file)

    caretAnnotation1 = ap.annotations.CaretAnnotation(
        document.pages[1], ap.Rectangle(200, 700.664, 308.708, 740.769, True)
    )
    caretAnnotation1.title = "Usuário Aspose"
    caretAnnotation1.subject = "Texto inserido 1"
    caretAnnotation1.flags = ap.annotations.AnnotationFlags.PRINT
    caretAnnotation1.color = ap.Color.blue

    document.pages[1].annotations.append(caretAnnotation1)
    document.save(output_file)
```


### Obter Anotação de Posição

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Posição em um documento PDF

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

### Excluir Anotação de Posição

O trecho de código a seguir mostra como Excluir Anotação de Posição de um arquivo PDF usando Python.

```python

    import aspose.pdf as ap

    # Carregar o arquivo PDF
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

## Adicionar Anotação de Link

[Links](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) são anotações que abrem URLs ou se movem para certas posições dentro do mesmo ou de um documento externo quando você clica.

Uma Anotação de Link é uma área retangular que pode ser colocada em qualquer lugar da página. Cada link tem uma ação PDF correspondente associada a ele. Esta ação é executada quando o usuário clica na área deste link.

O trecho de código a seguir mostra como adicionar uma Anotação de Link a um arquivo PDF usando um exemplo de número de telefone:

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Criar objeto TextFragmentAbsorber para encontrar um número de telefone
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Aceitar o absorvedor apenas para a 1ª página
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Criar Anotação de Link e definir a ação para chamar um número de telefone
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Adicionar anotação à página
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```


### Obter Anotação de Link

Por favor, tente usar o seguinte trecho de código para Obter [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) do documento PDF.

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

O seguinte trecho de código mostra como Excluir Anotação de Link do arquivo PDF. Para isso, precisamos encontrar e remover todas as anotações de link na 1ª página. Após isso, salvaremos o documento com a anotação removida.

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


## Redigir certa região da página com Anotação de Redação usando Aspose.PDF para Python

Aspose.PDF para Python via .NET suporta o recurso de adicionar e manipular Anotações em um arquivo PDF existente. Anotações de Redação em documentos PDF servem para o propósito de remover ou ocultar permanentemente informações confidenciais do documento. O processo de edição das informações envolve cobrir ou sombrear conteúdo específico, como texto, imagens ou gráficos, de maneira que restrinja sua visibilidade e acessibilidade para outras pessoas. Isso garante que as informações sensíveis permaneçam ocultas e protegidas dentro do documento. Para atender a este requisito, é fornecida uma classe chamada [RedactionAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/redactionannotation/), que pode ser usada para redigir certas regiões da página ou pode ser usada para manipular RedactionAnnotations existentes e redigi-las (ou seja, achatar a anotação e remover o texto sob ela).

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

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>