---
title: Tooltip em PDF usando Python
linktitle: Tooltip em PDF
type: docs
weight: 20
url: /python-net/pdf-tooltip/
description: Aprenda como adicionar tooltip ao fragmento de texto em PDF usando Python e Aspose.PDF
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tooltip em PDF usando Python",
    "alternativeHeadline": "Adicionar Tooltip em PDF ao Texto",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, adicionar tooltip em pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação do Aspose.PDF",
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
    "url": "/python-net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/pdf-tooltip/"
    },
    "dateModified": "2024-02-04",
    "description": "Aprenda como adicionar tooltip ao fragmento de texto em PDF usando Python e Aspose.PDF"
}
</script>


## Adicionar Tooltip ao Texto Pesquisado adicionando Botão Invisível

Este código demonstra como adicionar tooltips a fragmentos de texto específicos em um documento PDF usando Aspose.PDF. Os tooltips são exibidos quando o cursor do mouse passa sobre o texto correspondente.

O trecho de código a seguir mostrará como alcançar essa funcionalidade:

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Mova o cursor do mouse aqui para exibir um tooltip")
    )
    document.pages[1].paragraphs.add(
        ap.text.TextFragment(
            "Mova o cursor do mouse aqui para exibir um tooltip muito longo"
        )
    )
    document.save(output_pdf)

    # Abrir documento com texto
    document = ap.Document(output_pdf)
    # Criar objeto TextAbsorber para encontrar todas as frases que correspondem à expressão regular
    absorber = ap.text.TextFragmentAbsorber(
        "Mova o cursor do mouse aqui para exibir um tooltip"
    )
    # Aceitar o absorvedor para as páginas do documento
    document.pages.accept(absorber)
    # Obter os fragmentos de texto extraídos
    text_fragments = absorber.text_fragments

    # Percorrer os fragmentos
    for fragment in text_fragments:
        # Criar botão invisível na posição do fragmento de texto
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # O valor alternate_name será exibido como tooltip por um aplicativo visualizador
        field.alternate_name = "Tooltip para texto."
        # Adicionar campo de botão ao documento
        document.form.add(field)

    # Próximo será um exemplo de tooltip muito longo
    absorber = ap.text.TextFragmentAbsorber(
        "Mova o cursor do mouse aqui para exibir um tooltip muito longo"
    )
    document.pages.accept(absorber)
    text_fragments = absorber.text_fragments

    for fragment in text_fragments:
        field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Definir texto muito longo
        field.alternate_name = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
            " sed do eiusmod tempor incididunt ut labore et dolore magna"
            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
            " ullamco laboris nisi ut aliquip ex ea commodo consequat."
            " Duis aute irure dolor in reprehenderit in voluptate velit"
            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
            " occaecat cupidatat non proident, sunt in culpa qui officia"
            " deserunt mollit anim id est laborum."
        )
        document.form.add(field)

    # Salvar documento
    document.save(output_pdf)
```


## Criar um Bloco de Texto Oculto e Mostrá-lo ao Passar o Mouse

Este trecho de código Python mostra como adicionar texto flutuante a um documento PDF, que aparece quando o cursor do mouse passa sobre uma área específica.

Primeiro, um novo documento PDF é criado, e um parágrafo contendo o texto "Mova o cursor do mouse aqui para exibir o texto flutuante" é adicionado a ele. O documento é então salvo.

Em seguida, o documento salvo é reaberto, e um objeto TextAbsorber é criado para encontrar o fragmento de texto adicionado anteriormente. Este fragmento de texto é então usado para definir a posição e as características do campo de texto flutuante.

Um objeto TextBoxField é criado para representar o campo de texto flutuante, e suas propriedades como posição, valor, status de somente leitura e visibilidade são configuradas adequadamente. Além disso, um nome único e características de aparência são atribuídos ao campo.

O campo de texto flutuante é adicionado ao formulário do documento, e um campo de botão invisível é criado na posição do fragmento de texto original.
 Os eventos HideAction são atribuídos ao campo do botão, especificando que o campo de texto flutuante deve aparecer quando o cursor do mouse entrar em sua proximidade e desaparecer quando o cursor sair.

Finalmente, o campo do botão é adicionado ao formulário do documento, e o documento modificado é salvo.

Este trecho de código fornece um método para criar elementos de texto flutuantes interativos em um documento PDF usando Aspose.PDF para Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    document.pages.add().paragraphs.add(
        ap.text.TextFragment("Mova o cursor do mouse aqui para exibir o texto flutuante")
    )
    document.save(output_pdf)

    # Abrir documento com texto
    document = ap.Document(output_pdf)
    # Criar objeto TextAbsorber para encontrar todas as frases que correspondem à expressão regular
    absorber = ap.text.TextFragmentAbsorber(
        "Mova o cursor do mouse aqui para exibir o texto flutuante"
    )
    # Aceitar o absorvedor para as páginas do documento
    document.pages.accept(absorber)
    # Obter o primeiro fragmento de texto extraído
    text_fragments = absorber.text_fragments
    fragment = text_fragments[1]

    # Criar campo de texto oculto para texto flutuante no retângulo especificado da página
    floating_field = ap.forms.TextBoxField(
        fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
    )
    # Definir texto a ser exibido como valor do campo
    floating_field.value = 'Este é o "campo de texto flutuante".'
    # Recomendamos tornar o campo 'somente leitura' para este cenário
    floating_field.read_only = True
    # Definir flag 'oculto' para tornar o campo invisível na abertura do documento
    floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

    # Definir um nome de campo único não é necessário, mas permitido
    floating_field.partial_name = "FloatingField_1"

    # Definir características de aparência do campo não é necessário, mas melhora
    floating_field.default_appearance = ap.annotations.DefaultAppearance(
        "Helv", 10, ap.Color.blue.to_rgb()
    )
    floating_field.characteristics.background = ap.Color.light_blue.to_rgb()
    floating_field.characteristics.border = ap.Color.dark_blue.to_rgb()
    floating_field.border = ap.annotations.Border(floating_field)
    floating_field.border.width = 1
    floating_field.multiline = True

    # Adicionar campo de texto ao documento
    document.form.add(floating_field)
    # Criar botão invisível na posição do fragmento de texto
    button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
    # Criar nova ação de ocultação para o campo especificado (anotação) e flag de invisibilidade.
    # (Você também pode referir-se ao campo flutuante pelo nome se especificado anteriormente.)
    # Adicionar ações de entrada/saída do mouse no campo do botão invisível

    button_field.actions.on_enter = ap.annotations.HideAction(
        floating_field.partial_name, False
    )
    button_field.actions.on_exit = ap.annotations.HideAction(
        floating_field.partial_name
    )

    # Adicionar campo do botão ao documento
    document.form.add(button_field)

    # Salvar documento
    document.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Python via .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>