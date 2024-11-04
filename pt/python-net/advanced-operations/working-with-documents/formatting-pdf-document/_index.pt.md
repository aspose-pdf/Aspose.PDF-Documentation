---
title: Formatando Documento PDF usando Python
linktitle: Formatando Documento PDF
type: docs
weight: 11
url: /python-net/formatting-pdf-document/
description: Crie e formate o Documento PDF com Aspose.PDF para Python via .NET. Use o próximo trecho de código para resolver suas tarefas.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Formatando Documento PDF usando Python",
    "alternativeHeadline": "Como formatar Documento PDF em Python via .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos pdf",
    "keywords": "pdf, dotnet, python, formatar documento pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/formatting-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Crie e formate o Documento PDF com Aspose.PDF para Python via .NET. Use o próximo trecho de código para resolver suas tarefas."
}
</script>


## Formatação do Documento PDF

### Obter Propriedades da Janela do Documento e Exibição de Página

Este tópico ajuda você a entender como obter propriedades da janela do documento, aplicativo visualizador e como as páginas são exibidas. Para definir essas propriedades:

Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Agora, você pode definir as propriedades do objeto Document, tais como:

- CenterWindow – Centralizar a janela do documento na tela. Padrão: false.
- Direction – Ordem de leitura. Isso determina como as páginas são dispostas quando exibidas lado a lado. Padrão: da esquerda para a direita.
- DisplayDocTitle – Exibir o título do documento na barra de título da janela do documento. Padrão: false (o título é exibido).
- HideMenuBar – Ocultar ou exibir a barra de menu da janela do documento. Padrão: false (a barra de menu é exibida).
- HideToolBar – Ocultar ou exibir a barra de ferramentas da janela do documento. Padrão: false (a barra de ferramentas é exibida).
- HideWindowUI – Ocultar ou exibir elementos da janela do documento, como barras de rolagem.
 Padrão: false (elementos da UI são exibidos).
- NonFullScreenPageMode – Como o documento quando não está exibido em modo de página inteira.
- PageLayout – O layout da página.
- PageMode – Como o documento é exibido quando aberto pela primeira vez. As opções são mostrar miniaturas, tela cheia, mostrar painel de anexos.

O seguinte trecho de código mostra como obter as propriedades usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Obter diferentes propriedades do documento
    # Posição da janela do documento - Padrão: false
    print("CenterWindow :", document.center_window)

    # Ordem de leitura predominante; determina a posição da página
    # Quando exibido lado a lado - Padrão: L2R
    print("Direction :", document.direction)

    # Se a barra de título da janela deve exibir o título do documento
    # Se false, a barra de título exibe o nome do arquivo PDF - Padrão: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Se redimensionar a janela do documento para ajustar ao tamanho da
    # Primeira página exibida - Padrão: false
    print("FitWindow :", document.fit_window)

    # Se esconder a barra de menu do aplicativo visualizador - Padrão: false
    print("HideMenuBar :", document.hide_menubar)

    # Se esconder a barra de ferramentas do aplicativo visualizador - Padrão: false
    print("HideToolBar :", document.hide_tool_bar)

    # Se esconder elementos de UI como barras de rolagem
    # E deixar apenas o conteúdo da página exibido - Padrão: false
    print("HideWindowUI :", document.hide_window_ui)

    # Modo de página do documento. Como exibir o documento ao sair do modo de tela cheia.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # O layout da página, ou seja, página única, uma coluna
    print("PageLayout :", document.page_layout)

    # Como o documento deve ser exibido ao ser aberto
    # Ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos
    print("pageMode :", document.page_mode)

```

### Definir Propriedades da Janela do Documento e Exibição de Página

Este tópico explica como definir as propriedades da janela do documento, aplicativo de visualização e exibição de página. Para definir essas diferentes propriedades:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Defina as propriedades do objeto Document.
1. Salve o arquivo PDF atualizado usando o método save.

As propriedades disponíveis são:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Cada uma é usada e descrita no código abaixo. O seguinte trecho de código mostra como definir as propriedades usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Definir diferentes propriedades do documento
    # Especificar para posicionar a janela do documento - Padrão: false
    document.center_window = True

    # Ordem de leitura predominante; determina a posição da página
    # Quando exibido lado a lado - Padrão: L2R
    document.direction = ap.Direction.R2L

    # Especificar se a barra de título da janela deve exibir o título do documento
    # Se false, a barra de título exibe o nome do arquivo PDF - Padrão: false
    document.display_doc_title = True

    # Especificar se deve redimensionar a janela do documento para ajustar ao tamanho da
    # Primeira página exibida - Padrão: false
    document.fit_window = True

    # Especificar se deve ocultar a barra de menu do aplicativo de visualização - Padrão: false
    document.hide_menubar = True

    # Especificar se deve ocultar a barra de ferramentas do aplicativo de visualização - Padrão: false
    document.hide_tool_bar = True

    # Especificar se deve ocultar elementos da interface do usuário como barras de rolagem
    # E deixar apenas o conteúdo da página exibido - Padrão: false
    document.hide_window_ui = True

    # Modo de página do documento. especificar como exibir o documento ao sair do modo de tela cheia.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Especificar o layout da página, ou seja, página única, uma coluna
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Especificar como o documento deve ser exibido quando aberto
    # Ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos
    document.page_mode = ap.PageMode.USE_THUMBS

    # Salvar arquivo PDF atualizado
    document.save(output_pdf)
```


### Incorporando Fontes Tipo 1 Padrão

Alguns documentos PDF possuem fontes de um conjunto especial de fontes da Adobe. Fontes deste conjunto são chamadas de "Fontes Tipo 1 Padrão". Este conjunto inclui 14 fontes e incorporar este tipo de fontes requer o uso de flags especiais, ou seja, [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). A seguir está o trecho de código que pode ser usado para obter um documento com todas as fontes incorporadas, incluindo Fontes Tipo 1 Padrão:

```python

    import aspose.pdf as ap

    # Carregar um Documento PDF existente
    document = ap.Document(input_pdf)
    # Definir a propriedade EmbedStandardFonts do documento
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Verificar se a fonte já está incorporada
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Incorporando Fontes ao criar PDF

Se você precisar usar qualquer fonte além das 14 fontes principais suportadas pelo Adobe Reader, você deve incorporar a descrição da fonte ao gerar o arquivo PDF. Se a informação da fonte não estiver incorporada, o Adobe Reader a obterá do Sistema Operacional se estiver instalada no sistema, ou construirá uma fonte substituta de acordo com o descritor de fonte no PDF.

>Por favor, note que a fonte incorporada deve estar instalada na máquina host, ou seja, no caso do seguinte código a fonte 'Univers Condensed' está instalada no sistema.

Usamos a propriedade 'is_embedded' para incorporar a informação da fonte no arquivo PDF. Definir o valor desta propriedade como 'True' irá incorporar o arquivo completo da fonte no PDF, sabendo que isso aumentará o tamanho do arquivo PDF. A seguir está o trecho de código que pode ser usado para incorporar a informação da fonte no PDF.

```python

    import aspose.pdf as ap

    # Instanciar objeto Pdf chamando seu construtor vazio
    doc = ap.Document()

    # Criar uma seção no objeto Pdf
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" Este é um texto de exemplo usando fonte personalizada.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Salvar Documento PDF
    doc.save(output_pdf)
```


### Definir Nome de Fonte Padrão ao Salvar PDF

Quando um documento PDF contém fontes que não estão disponíveis no próprio documento e no dispositivo, a API substitui essas fontes pela fonte padrão. Se a fonte estiver disponível (instalada no dispositivo ou incorporada no documento), o PDF de saída deve ter a mesma fonte (não deve ser substituída pela fonte padrão). O valor da fonte padrão deve conter o nome da fonte (não o caminho para os arquivos de fonte). Implementamos um recurso para definir o nome da fonte padrão ao salvar um documento como PDF. O seguinte trecho de código pode ser usado para definir a fonte padrão:

```python

    import aspose.pdf as ap

    # Carregar um documento PDF existente com fonte ausente
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Especificar Nome da Fonte Padrão
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Obter Todas as Fontes de um Documento PDF

Caso você queira obter todas as fontes de um documento PDF, você pode usar o método [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) fornecido na classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
 Verifique o seguinte trecho de código para obter todas as fontes de um documento PDF existente:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Melhorar a Incorporação de Fontes usando FontSubsetStrategy

O trecho de código a seguir mostra como definir [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) usando a propriedade [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties):

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # Todas as fontes serão incorporadas como subconjunto no documento no caso de SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # O subconjunto de fontes será incorporado para fontes totalmente incorporadas, mas fontes que não estão incorporadas no documento não serão afetadas.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Obter-Definir Fator de Zoom de Arquivo PDF

Às vezes, você quer determinar qual é o fator de zoom atual de um documento PDF. Com Aspose.Pdf, você pode descobrir o valor atual e também definir um.

A propriedade Destination da classe [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) permite que você obtenha o valor de zoom associado a um arquivo PDF. Da mesma forma, ela pode ser usada para definir o fator de zoom de um arquivo.

#### Definir fator de Zoom

O trecho de código a seguir mostra como definir o fator de zoom de um arquivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar novo objeto Document
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Salvar o documento
    doc.save(output_pdf)
```

#### Obter Fator de Zoom

O trecho de código a seguir mostra como obter o fator de zoom de um arquivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar novo objeto Document
    doc = ap.Document(input_pdf)

    # Criar objeto GoToAction
    action = doc.open_action

    # Obter o fator de Zoom do arquivo PDF
    print(action.destination.zoom)
```


### Configurando Propriedades Predefinidas de Diálogo de Impressão

Aspose.PDF permite configurar os membros [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) de um documento PDF. Isso permite alterar a propriedade DuplexMode de um documento PDF, que é configurada como simplex por padrão. Isso pode ser realizado usando duas metodologias diferentes, como mostrado abaixo.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Configurando Propriedades Predefinidas de Diálogo de Impressão usando Editor de Conteúdo PDF

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("O arquivo tem duplex flip borda curta")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```