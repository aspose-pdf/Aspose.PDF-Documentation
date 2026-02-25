---
title: Formatação de Documento PDF usando Python
linktitle: Formatação de Documento PDF
type: docs
weight: 11
url: /pt/python-net/formatting-pdf-document/
description: Crie e formate o documento PDF com Aspose.PDF para Python via .NET. Use o próximo trecho de código para resolver suas tarefas.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formatação de documentos PDF usando Python
Abstract: O artigo fornece um guia abrangente sobre manipulação e formatação de documentos PDF usando a biblioteca Aspose.PDF em Python. Ele aborda vários aspectos da personalização de PDF, incluindo a configuração das propriedades da janela do documento e da exibição de páginas, como centralizar a janela, direção de leitura e ocultar elementos da UI. O artigo explica como recuperar e definir essas propriedades programaticamente usando a classe `Document`. Além disso, trata do gerenciamento de fontes, detalhando como incorporar fontes Standard Type 1 e outras fontes em PDFs, garantindo portabilidade do documento e consistência visual entre sistemas. Também destaca técnicas para definir um nome de fonte padrão, recuperar todas as fontes de um PDF e aprimorar a incorporação de fontes usando `FontSubsetStrategy`. Além disso, o artigo elabora sobre o ajuste do fator de zoom de documentos PDF usando a classe `GoToAction` e a configuração das propriedades predefinidas da caixa de diálogo de impressão, incluindo opções de impressão duplex. Trechos de código acompanham cada seção, fornecendo exemplos práticos para implementar esses recursos.
---

## Formatação de Documento PDF

### Obter Propriedades da Janela do Documento e Exibição de Página

Este tópico ajuda você a entender como obter propriedades da janela do documento, do visualizador e como as páginas são exibidas. Para definir essas propriedades:

Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Agora, você pode definir as propriedades do objeto Document, como

- CenterWindow – Centraliza a janela do documento na tela. Padrão: false.
- Direction – Ordem de leitura. Determina como as páginas são dispostas quando exibidas lado a lado. Padrão: da esquerda para a direita.
- DisplayDocTitle – Exibir o título do documento na barra de título da janela do documento. Padrão: false (o título é exibido).
- HideMenuBar – Ocultar ou exibir a barra de menus da janela do documento. Padrão: false (a barra de menus é exibida).
- HideToolBar – Ocultar ou exibir a barra de ferramentas da janela do documento. Padrão: false (a barra de ferramentas é exibida).
- HideWindowUI – Ocultar ou exibir elementos da janela do documento, como barras de rolagem. Padrão: false (os elementos da UI são exibidos).
- NonFullScreenPageMode – Como o documento se comporta quando não está em modo de página cheia.
- PageLayout – O layout da página.
- PageMode – Como o documento é exibido ao ser aberto pela primeira vez. As opções são mostrar miniaturas, tela cheia, mostrar painel de anexos.

O trecho de código a seguir mostra como obter as propriedades usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get different document properties
    # Position of document's window - Default: false
    print("CenterWindow :", document.center_window)

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    print("Direction :", document.direction)

    # Whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    print("FitWindow :", document.fit_window)

    # Whether to hide menu bar of the viewer application - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Whether to hide tool bar of the viewer application - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Document's page mode. How to display document on exiting full-screen mode.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # The page layout i.e. single page, one column
    print("PageLayout :", document.page_layout)

    # How the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    print("pageMode :", document.page_mode)

```

### Definir Propriedades da Janela do Documento e Exibição de Página

Este tópico explica como definir as propriedades da janela do documento, do aplicativo visualizador e da exibição de página. Para definir estas diferentes propriedades:

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

Cada uma é usada e descrita no código abaixo. O trecho de código a seguir mostra como definir as propriedades usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set different document properties
    # Sepcify to position document's window - Default: false
    document.center_window = True

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    document.direction = ap.Direction.R2L

    # Specify whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    document.display_doc_title = True

    # Specify whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    document.fit_window = True

    # Specify whether to hide menu bar of the viewer application - Default: false
    document.hide_menubar = True

    # Specify whether to hide tool bar of the viewer application - Default: false
    document.hide_tool_bar = True

    # Specify whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    document.hide_window_ui = True

    # Document's page mode. specify how to display document on exiting full-screen mode.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Specify the page layout i.e. single page, one column
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Specify how the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_THUMBS

    # Save updated PDF file
    document.save(output_pdf)
```

### Incorporação de Fontes Standard Type 1

Alguns documentos PDF possuem fontes de um conjunto especial da Adobe. As fontes desse conjunto são chamadas “Standard Type 1 Fonts”. Esse conjunto inclui 14 fontes e incorporar esse tipo de fontes requer o uso de flags especiais, por exemplo [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). A seguir está o trecho de código que pode ser usado para obter um documento com todas as fontes incorporadas, incluindo as Standard Type 1 Fonts:

```python

    import aspose.pdf as ap

    # Load an existing PDF Document
    document = ap.Document(input_pdf)
    # Set EmbedStandardFonts property of document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Check if font is already embedded
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Incorporando Fontes ao criar PDF

Se precisar usar alguma fonte diferente das 14 fontes principais suportadas pelo Adobe Reader, você deve incorporar a descrição da fonte ao gerar o arquivo PDF. Se as informações da fonte não forem incorporadas, o Adobe Reader as obterá do Sistema Operacional, caso estejam instaladas, ou criará uma fonte substituta de acordo com o descritor de fonte no PDF.

>Observe que a fonte incorporada deve estar instalada na máquina host, por exemplo, no código a seguir a fonte ‘Univers Condensed’ está instalada no sistema.

Usamos a propriedade 'is_embedded' para incorporar as informações da fonte no arquivo PDF. Definir o valor dessa propriedade como 'True' incorporará o arquivo de fonte completo ao PDF, sabendo que isso aumentará o tamanho do arquivo PDF. A seguir está o trecho de código que pode ser usado para incorporar as informações da fonte ao PDF.

```python

    import aspose.pdf as ap

    # Instantiate Pdf object by calling its empty constructor
    doc = ap.Document()

    # Create a section in the Pdf object
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Save PDF Document
    doc.save(output_pdf)
```

### Definir Nome da Fonte Padrão ao Salvar PDF

Quando um documento PDF contém fontes que não estão disponíveis no próprio documento nem no dispositivo, a API substitui essas fontes pela fonte padrão. Se a fonte estiver disponível (instalada no dispositivo ou incorporada ao documento), o PDF de saída deve manter a mesma fonte (não deve ser substituída pela fonte padrão). O valor da fonte padrão deve conter o nome da fonte (não o caminho para os arquivos de fonte). Implementamos um recurso para definir o nome da fonte padrão ao salvar um documento como PDF. O trecho de código a seguir pode ser usado para definir a fonte padrão:

```python

    import aspose.pdf as ap

    # Load an existing PDF document with missing font
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Specify Default Font Name
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Obter Todas as Fontes de um Documento PDF

Caso você queira obter todas as fontes de um documento PDF, pode usar o método [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) fornecido na classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Por favor, verifique o trecho de código a seguir para obter todas as fontes de um documento PDF existente:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Melhorar a Incorporação de Fontes usando FontSubsetStrategy

O trecho de código a seguir mostra como definir a [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) usada na propriedade [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties):

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # All fonts will be embedded as subset into document in case of SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Obter e Definir o Fator de Zoom de um Arquivo PDF

Às vezes, você deseja determinar qual é o fator de zoom atual de um documento PDF. Com Aspose.Pdf, você pode descobrir o valor atual e também definir um.

A propriedade Destination da classe [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) permite obter o valor de zoom associado a um arquivo PDF. Da mesma forma, pode ser usada para definir o fator de zoom de um arquivo.

#### Definir Fator de Zoom

O trecho de código a seguir mostra como definir o fator de zoom de um arquivo PDF.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Save the document
    doc.save(output_pdf)
```

#### Obter Fator de Zoom

O trecho de código a seguir mostra como obter o fator de zoom de um arquivo PDF.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    # Create GoToAction object
    action = doc.open_action

    # Get the Zoom factor of PDF file
    print(action.destination.zoom)
```

### Definir Propriedades Predefinidas do Diálogo de Impressão

Aspoose.PDF permite definir os membros [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) de um documento PDF. Ele permite alterar a propriedade DuplexMode de um documento PDF, que por padrão está definida como simplex. Isso pode ser alcançado usando duas metodologias diferentes, conforme mostrado abaixo.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Definir Propriedades Predefinidas do Diálogo de Impressão usando o PDF Content Editor

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("The file has duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```


