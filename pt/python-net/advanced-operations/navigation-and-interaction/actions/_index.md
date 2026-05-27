---
title: Trabalhar com Ações de PDF em Python
linktitle: Ações
type: docs
weight: 20
url: /pt/python-net/actions/
description: Aprenda a adicionar, atualizar e remover ações de documento, página e formulário em arquivos PDF usando Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Adicione ações de documento, página e formulário a arquivos PDF em Python
Abstract: Este artigo explora como trabalhar com ações em documentos PDF usando a biblioteca Aspose.PDF, abordando interações em nível de documento, nível de página e nível de formulário. As ações PDF são gatilhos predefinidos ou personalizáveis que respondem a eventos do usuário, permitindo navegação, execução de JavaScript, reprodução de multimídia, envio de formulários e muito mais. O guia demonstra como adicionar, personalizar e remover ações, como abrir URLs em eventos do documento, criar navegação ou efeitos de zoom específicos de página, adicionar botões interativos para impressão e navegação, ocultar elementos de formulário dinamicamente e enviar dados de formulário para endpoints web. Por meio de exemplos detalhados de código Python, os leitores aprendem a aprimorar a interatividade do PDF, simplificar fluxos de trabalho e integrar PDFs a sistemas externos, compreendendo as considerações de compatibilidade dos visualizadores.
---

Ações em um PDF são tarefas predefinidas que são acionadas por interação do usuário ou eventos do documento. Elas podem ser usadas para:

- Navegue até uma página específica ou um arquivo externo
- Abrir um link da web
- Reproduzir conteúdo multimídia
- Executar JavaScript
- Enviar ou redefinir um formulário
- Mostrar/ocultar campos
- Alterar nível de zoom ou modo de visualização

Quase todas as ações utilizam parâmetros integrados, mas há algumas que podem ser personalizadas. Por exemplo – Ações JavaScript.

## Adicionar Ações de Lançamento de PDF

Adicione ações de lançamento baseadas em JavaScript a um documento PDF usando Python e Aspose.PDF. Ele atribui ações a eventos chave do documento, como abertura, salvamento e impressão, permitindo que URLs sejam abertas automaticamente quando esses eventos ocorrerem em visualizadores de PDF compatíveis.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_launch_actions(infile, outfile):
    """Add JavaScript launch actions for document events.

    Adds JavaScript actions that launch URLs when specific document events occur:
    - On document open: launches http://localhost:3000/open
    - Before saving: launches http://localhost:3000/save
    - Before printing: launches http://localhost:3000/print

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with document actions.

    Returns:
        None

    Example:
        >>> add_launch_actions("sample_data/input/add_launch_actions_in.pdf", "sample_data/output/add_launch_actions_out.pdf")

    Notes:
        - Uses `ap.annotations.JavascriptAction` with `app.launchURL()`.
        - URLs are opened in the default browser depending on viewer support.
    """

    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)
```

## Removendo Ações do PDF Document

Para limpar (ou remover) ações, basta definir o manipulador para `None`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def remove_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)
```

## Adicionando Ações à página no Documento PDF

Os gatilhos semelhantes são fornecidos para páginas: `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(outfile)
```

## Ações em AcroForms

### Usando ações de navegação

O padrão PDF prevê um determinado conjunto de ações nomeadas. O significado dessas ações é determinado pelo seu nome.
No código a seguir, usaremos ações para navegações.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_navigation_buttons(infile, outfile):
    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

Este código adiciona botões de navegação a cada página de um documento PDF, facilitando para os usuários moverem‑se entre as páginas. Ele começa determinando os caminhos completos dos arquivos de entrada e saída usando um método auxiliar. A lista button_config define quatro tipos de botões de navegação —Primeira Página, Página Anterior, Próxima Página e Última Página— juntamente com suas posições horizontais, as ações de navegação predefinidas que eles acionam e uma função lambda que determina se cada botão deve ser somente leitura em uma determinada página (por exemplo, os botões "Primeira Página" e "Página Anterior" são somente leitura na primeira página).

O código então carrega o PDF e itera por cada página. Para cada página, ele percorre as configurações de botões, criando uma área retangular para cada botão e instanciando um ButtonField naquele local. Cada botão recebe um nome, seu status somente‑leitura é definido com base na página atual, e sua ação de clique é atribuída à ação de navegação correspondente. O botão é então adicionado aos campos de formulário do PDF.

Depois que todos os botões são adicionados a todas as páginas, o documento modificado é salvo. Se ocorrerem erros durante esse processo, eles são capturados e impressos. Essa abordagem garante que cada página tenha um conjunto consistente de controles de navegação, melhorando a usabilidade de PDFs de várias páginas. Uma sutileza é o uso da lambda is_readonly_fn para desativar os botões de navegação quando não fizer sentido (por exemplo, "Next Page" na última página), o que ajuda a prevenir a confusão do usuário.

### Usando ações de impressão

Ao usar formulários PDF, frequentemente há a necessidade de imprimir esses documentos PDF. Essa ação pode ser realizada usando um leitor de PDF, mas às vezes é mais conveniente fazê‑la diretamente a partir do documento usando um botão especial.

Na verdade, este é mais um exemplo de como usar ações nomeadas. Nós usaremos `PredefinedAction.FILE_PRINT` (simulando o uso do item de menu File‑>Print), mas você também pode usar `PredefinedAction.PRINT` ou `PredefinedAction.PRINT_DIALOG`, dependendo dos seus próprios propósitos.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_print(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(outfile)
```

Este trecho de código demonstra como adicionar um botão "Print" à primeira página de um documento PDF. Ele começa carregando o PDF a partir do caminho de arquivo de entrada especificado e selecionando a primeira página (document.pages[1]).

Uma área retangular é definida para a posição e tamanho do botão na página. Um ButtonField é então criado nessa localização, recebe o nome “printButton,” e seu valor de exibição é definido como “Print.” O botão é configurado para que, quando for clicado (especificamente, quando o botão do mouse for liberado), ele acione a ação predefinida “Print File,” solicitando ao visualizador de PDF que abra a caixa de diálogo de impressão.

Para melhorar a aparência do botão, cria-se uma borda e atribui‑se ao botão, definindo sua largura como 1 unidade. O botão é então adicionado aos campos de formulário do PDF na primeira página. Finalmente, o documento modificado é salvo no caminho do arquivo de saída. Essa abordagem oferece aos usuários uma maneira conveniente de imprimir o documento diretamente a partir do PDF. Observe que a eficácia desse recurso depende do suporte do visualizador de PDF a campos de formulário interativos e ações predefinidas.

### Usando a ação Ocultar

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_hide(infile, outfile):
    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)
```

Este trecho de código adiciona um botão à primeira página de um PDF que, ao ser clicado, oculta todos os campos de caixa de seleção no documento. Ele começa resolvendo os caminhos completos dos arquivos de entrada e saída usando um método auxiliar. O PDF é carregado, e todos os campos de caixa de seleção são coletados filtrando os campos de formulário por instâncias de `ap.CheckboxField`.

Uma área retangular é definida para a posição do novo botão próximo ao topo da página. Um ButtonField é criado neste local, chamado “HideButton”, e rotulado “Hide Checkboxes”. O botão está configurado de modo que, quando clicado (ao liberar o botão do mouse), ele aciona uma HideAction que oculta todas as caixas de seleção coletadas.

O botão é então adicionado aos campos de formulário na primeira página, e o PDF modificado é salvo no arquivo de saída. Se ocorrerem erros durante este processo, eles são capturados e exibidos. Esse recurso oferece aos usuários uma maneira de ocultar rapidamente todas as caixas de seleção no PDF, o que pode ser útil para personalizar a aparência ou o fluxo de trabalho do documento.

### Aplicando Ação de Envio

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_submit_action(infile, outfile):
    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)
```

Esta função adiciona um botão “Submit” à primeira página de um formulário PDF, permitindo que os usuários enviem os dados do formulário para um endpoint web especificado. Ela começa construindo os caminhos completos para os arquivos PDF de entrada e saída, depois carrega o PDF de entrada usando a biblioteca Aspose.PDF.

A `SubmitFormAction` é criado para definir o comportamento quando o botão é clicado. O URL da ação é definido usando um `FileSpecification` apontando para http://localhost:3000/submit, o que significa que os dados do formulário serão enviados para esta URL. A propriedade flags combina `EXPORT_FORMAT` e `SUBMIT_COORDINATES`, garantindo que os dados do formulário sejam exportados em um formato padrão e que as coordenadas do clique do botão sejam incluídas na submissão.

Uma área retangular é definida para a posição e o tamanho do botão na página. Um ButtonField é criado neste local na primeira página, com o nome “SubmitButton,” e seu valor de exibição é definido como “Submit.” A ação de envio é atribuída ao evento de liberação do mouse do botão, de modo que a ação é acionada quando o usuário clica no botão.

Por fim, o botão é adicionado aos campos de formulário na primeira página, e o PDF modificado é salvo no arquivo de saída. Se ocorrerem erros durante este processo, eles são capturados e impressos. Essa abordagem fornece uma maneira amigável ao usuário para que os usuários de PDF enviem os dados do formulário diretamente para um endpoint de servidor.

## Tópicos de Navegação Relacionados

- [Navegação e interação em PDF usando Python](/pdf/pt/python-net/navigation-and-interaction/)
- [Trabalhar com marcadores em PDF usando Python](/pdf/pt/python-net/bookmarks/)
- [Trabalhe com links em PDF usando Python](/pdf/pt/python-net/links/)
