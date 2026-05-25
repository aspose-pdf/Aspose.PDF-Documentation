---
title: Formatar documentos PDF em Python
linktitle: Formatando documento PDF
type: docs
weight: 11
url: /pt/python-net/formatting-pdf-document/
description: Aprenda a formatar documentos PDF, incorporar Font, controlar configurações do visualizador e ajustar opções de exibição no Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Formatando documentos PDF usando Python.
Abstract: O artigo fornece um guia abrangente sobre manipulação e formatação de documentos PDF usando a biblioteca Aspose.PDF em Python. Ele aborda vários aspectos da personalização de PDFs, incluindo a definição de propriedades da janela do documento e da exibição de página, como centralizar a janela, direção de leitura e ocultar elementos da interface do usuário. O artigo explica como recuperar e definir essas propriedades programaticamente usando a classe `Document`. Além disso, trata da gestão de fontes, detalhando como incorporar fontes Standard Type 1 e outras fontes em PDFs, garantindo a portabilidade do documento e consistência visual entre sistemas. Também destaca técnicas para definir um nome de fonte padrão, recuperar todas as fontes de um PDF e melhorar a incorporação de fontes usando `FontSubsetStrategy`. Ademais, o artigo aprofunda o ajuste do fator de zoom de documentos PDF usando a classe `GoToAction` e a configuração de propriedades predefinidas da caixa de diálogo de impressão, incluindo opções de impressão duplex. Trechos de código acompanham cada seção, fornecendo exemplos práticos para implementar esses recursos.
---

Este guia é útil quando você precisa controlar o comportamento do visualizador PDF, a incorporação de Font, as configurações padrão de exibição ou as preferências de impressão em documentos gerados em Python.

## Formatando documento PDF

### Obter Propriedades de Exibição da Janela e da Página do Documento

Este tópico ajuda você a entender como obter propriedades da janela do documento, do aplicativo visualizador e como as páginas são exibidas. Para definir essas propriedades:

Abra o arquivo PDF usando o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe. Agora, você pode definir as propriedades do objeto Document, como

- CenterWindow – Centralizar a janela do documento na tela. Padrão: false.
- Direção – Ordem de leitura. Isso determina como as páginas são dispostas quando exibidas lado a lado. Padrão: da esquerda para a direita.
- DisplayDocTitle – Exibe o título do documento na barra de título da janela do documento. Padrão: false (o título é exibido).
- HideMenuBar – Ocultar ou exibir a barra de menus da janela do documento. Padrão: false (a barra de menus é exibida).
- HideToolBar – Ocultar ou exibir a barra de ferramentas da janela do documento. Padrão: false (a barra de ferramentas é exibida).
- HideWindowUI – Ocultar ou exibir elementos da janela do documento, como barras de rolagem. Padrão: false (os elementos da IU são exibidos).
- NonFullScreenPageMode – Como o documento quando não é exibido no modo de página inteira.
- PageLayout – O layout da página.
- PageMode – Como o documento é exibido quando aberto pela primeira vez. As opções são mostrar miniaturas, tela cheia, mostrar painel de anexos.

O trecho de código a seguir mostra como obter as propriedades usando [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### Definir propriedades de exibição da janela do documento e da página

Este tópico explica como definir as propriedades da janela do documento, do aplicativo visualizador e da exibição da página. Para definir essas diferentes propriedades:

1. Abra o arquivo PDF usando o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Defina as propriedades do objeto Document.
1. Salve o arquivo PDF atualizado usando o método save.

Propriedades disponíveis são:

- CentralizarJanela
- Direção
- Exibir título do documento
- Ajustar à janela
- OcultarBarraDeMenu
- OcultarBarraDeFerramentas
- OcultarInterfaceDaJanela
- ModoNãoTelaCheia
- Layout da Página
- Modo de página

Cada um é usado e descrito no código abaixo. O trecho de código a seguir mostra como definir as propriedades usando o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### Incorporação de Fontes Tipo 1 Padrão

Alguns documentos PDF têm fontes de um conjunto especial de fontes da Adobe. As fontes desse conjunto são chamadas “Standard Type 1 Fonts”. Esse conjunto inclui 14 fontes e a incorporação desse tipo de fontes requer o uso de flags especiais, ou seja [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). O trecho de código a seguir pode ser usado para obter um documento com todas as fontes incorporadas, incluindo fontes Standard Type 1:

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Incorporando fontes ao criar PDF

Se precisar usar qualquer fonte que não seja as 14 fontes principais suportadas pelo Adobe Reader, você deve incorporar a descrição da fonte ao gerar o arquivo PDF. Se as informações da fonte não forem incorporadas, o Adobe Reader as obterá do Sistema Operacional se estiverem instaladas nele, ou construirá uma fonte substituta de acordo com o descritor de fonte no PDF.

>Por favor, note que a fonte incorporada deve estar instalada na máquina host, ou seja, no caso do código a seguir, a fonte ‘Univers Condensed’ está instalada no sistema.

Usamos a propriedade 'is_embedded' para incorporar as informações da fonte no arquivo PDF. Definir o valor desta propriedade como 'True' incorporará o arquivo de fonte completo no PDF, sabendo que isso aumentará o tamanho do arquivo PDF. A seguir, está o trecho de código que pode ser usado para incorporar as informações da fonte no PDF.

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### Definir o Nome da Fonte Padrão ao Salvar o PDF

Quando um documento PDF contém fontes que não estão disponíveis no próprio documento e no dispositivo, a API substitui essas fontes pela fonte padrão. Se a fonte estiver disponível (instalada no dispositivo ou incorporada ao documento), o PDF de saída deve ter a mesma fonte (não deve ser substituída pela fonte padrão). O valor da fonte padrão deve conter o nome da fonte (não o caminho para os arquivos de fonte). Implementamos um recurso para definir o nome da fonte padrão ao salvar um documento como PDF. O trecho de código a seguir pode ser usado para definir a fonte padrão:

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### Obter Todas as Fonts do PDF Document

Caso você queira obter todas as fontes de um documento PDF, você pode usar [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) método fornecido em [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe. Por favor, verifique o trecho de código a seguir para obter todas as fontes de um documento PDF existente:

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### Melhorar a incorporação de fontes usando FontSubsetStrategy

O trecho de código a seguir mostra como definir [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) usado [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) propriedade:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### Obter-Definir Fator de Zoom de Arquivo PDF

Às vezes, você deseja determinar qual é o fator de zoom atual de um documento PDF. Com o Aspose.Pdf, você pode descobrir o valor atual e também definir um.

O [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) A propriedade Destination da classe permite que você obtenha o valor de zoom associado a um arquivo PDF. Da mesma forma, ela pode ser usada para definir o fator de zoom de um arquivo.

#### Definir fator de zoom

O trecho de código a seguir mostra como definir o fator de zoom de um arquivo PDF.

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### Obter Fator de Zoom

O trecho de código a seguir mostra como obter o fator de zoom de um arquivo PDF.

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## Tópicos Relacionados ao Documento

- [Trabalhe com documentos PDF em Python](/pdf/pt/python-net/working-with-documents/)
- [Criar arquivos PDF em Python](/pdf/pt/python-net/create-pdf-document/)
- [Manipular documentos PDF em Python](/pdf/pt/python-net/manipulate-pdf-document/)
- [Otimizar arquivos PDF em Python](/pdf/pt/python-net/optimize-pdf/)
