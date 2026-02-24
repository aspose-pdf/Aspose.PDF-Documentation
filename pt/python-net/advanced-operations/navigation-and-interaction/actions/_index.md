---
title: Trabalhando com Ações em documento PDF
linktitle: Ações
type: docs
weight: 20
url: /pt/python-net/actions/
description: Explore como extrair e gerenciar metadados de PDF, como autor e título, em Python usando Aspose.PDF.
lastmod: "2025-07-10"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Lidando com Ações em documento PDF usando Python
Abstract: Este artigo explora como trabalhar com ações em documentos PDF usando a biblioteca Aspose.PDF, cobrindo interações ao nível do documento, da página e do formulário. As ações de PDF são gatilhos pré-definidos ou personalizáveis que respondem a eventos do usuário, permitindo navegação, execução de JavaScript, reprodução de multimídia, envio de formulários e muito mais. O guia demonstra como adicionar, personalizar e remover ações, como abrir URLs em eventos do documento, criar navegação ou efeitos de zoom específicos da página, adicionar botões interativos para impressão e navegação, ocultar elementos de formulário dinamicamente e enviar dados de formulário para endpoints web. Por meio de exemplos detalhados de código Python, os leitores aprendem a melhorar a interatividade dos PDFs, otimizar fluxos de trabalho e integrar PDFs com sistemas externos, compreendendo as considerações de compatibilidade dos visualizadores.
---

Ações em um PDF são tarefas pré-definidas que são disparadas por interação do usuário ou eventos do documento. Elas podem ser usadas para:

- Navegar para uma página específica ou arquivo externo
- Abrir um link web
- Reproduzir conteúdo multimídia
- Executar JavaScript
- Enviar ou redefinir um formulário
- Mostrar/ocultar campos
- Alterar o nível de zoom ou modo de visualização

Quase todas as ações utilizam parâmetros incorporados, mas há algumas que podem ser personalizadas. Por exemplo - Ações JavaScript.

## Ações ao nível do documento

### Adicionando Ações ao Documento PDF

Documentos PDF suportam várias ações ao nível do documento, incluindo código que é executado ao abrir o documento ou em resposta a eventos específicos. Use a propriedade `open_action` para ações ao abrir; outras ações são gerenciadas na coleção `actions`.

Vamos considerar como usar `open_action`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/open');"
)
document.save(path_outfile)
```

Neste exemplo chamamos o método `launchURL` do objeto `app` e abrimos um site (para fins de demonstração).

Outras ações podem ser adicionadas da mesma forma, mas com pequenas alterações:

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.actions.before_saving = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/save');"
)
document.actions.before_printing = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/print');"
)
```

Você pode adicionar ações para os seguintes eventos: `before_saving`, `before_printing`, `before_closing`, `after_saving`, `after_printing`.

Este trecho de código demonstra como anexar ações JavaScript a vários eventos ao nível do documento em um PDF. Primeiro, ele carrega um documento PDF existente a partir do caminho de arquivo de entrada especificado. A propriedade `document.open_action` é definida como uma ação JavaScript que abre uma URL quando o documento é aberto, solicitando ao visualizador de PDF que abra `http://localhost:3000/open` no navegador do usuário.

Em seguida, duas ações JavaScript adicionais são atribuídas aos eventos `before_saving` e `before_printing` do documento. Essas ações são disparadas quando o usuário tenta salvar ou imprimir o documento, respectivamente, cada vez abrindo uma URL diferente (`/save` ou `/print`) no navegador. Isso pode ser útil para rastrear interações do usuário ou integrar com fluxos de trabalho baseados na web.

### Removendo Ações do Documento PDF

Para limpar (ou remover) ações, basta definir o manipulador como `None`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = None
document.actions.before_saving = None
document.actions.before_printing = None
document.save(path_outfile)
```

## Ações ao nível da página

### Adicionando Ações à página no Documento PDF

Os gatilhos semelhantes são fornecidos para páginas: `on_open`, `on_close`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_page_actions(self, infile, outfile):
    """
    Add actions to the third page of the PDF.

    Adds two actions to page 3:
    - On page open: Navigate to the top of the page with specific zoom
    - On page close: Launch a URL with page-specific information

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Raises:
        ValueError: If document has fewer than 3 pages

    Example:
        >>> actions.add_page_actions("multipage.pdf", "page_actions.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)

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

    document.save(path_outfile)

```

Adicionamos duas ações a esta página. Primeiro, cria uma ação "GoTo" que é disparada quando a página é aberta. Esta ação usa um destino explícito para pular para o canto superior esquerdo da página em um nível de zoom específico. Segundo, anexa uma ação JavaScript que é executada quando a página é fechada, instruindo o visualizador de PDF a abrir uma URL específica no navegador. Por fim, o documento modificado é salvo no caminho de saída especificado.

Um ponto sutil a observar é a indexação das páginas, pois usar o índice errado pode levar a comportamentos inesperados ou erros. Além disso, o uso de ações JavaScript em PDFs pode não ser suportado por todos os visualizadores de PDF, portanto, esse recurso pode não funcionar em todos os lugares.

### Removendo Ações da página PDF

Use `remove_actions` para remover a ação na página.

```python

import aspose.pdf as ap
from os import path

document = ap.Document(path_infile)

if len(document.pages) < 3:
    print("Error: The document does not have at least 3 pages.")
    return

page = document.pages[3]
page.actions.remove_actions()

document.save(path_outfile)

```

## Ações em AcroForms

### Usando ações de navegação

O padrão PDF fornece um certo conjunto de ações nomeadas. O significado dessas ações é determinado pelo seu nome.
No código a seguir usaremos ações para navegações.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_navigation_buttons(self, infile, outfile):
    """
    Add navigation buttons to each page of the PDF.

    Creates four navigation buttons on each page:
    - First Page: Navigate to the first page
    - Previous Page: Navigate to the previous page
    - Next Page: Navigate to the next page
    - Last Page: Navigate to the last page

    Buttons are automatically disabled when not applicable (e.g.,
    "Previous" is disabled on the first page).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_navigation_buttons("multipage.pdf", "nav_buttons.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    try:
        document = ap.Document(path_infile)
        total_pages = len(document.pages)

        # Add navigation buttons to each page
        for page in document.pages:
            page_number = page.number

            for name, x_pos, action, is_readonly_fn in button_config:
                # Create button rectangle
                rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
                button = ButtonField(page, rect)
                button.partial_name = name

                # Disable button when not applicable
                button.read_only = is_readonly_fn(page_number, total_pages)
                button.actions.on_release_mouse_btn = NamedAction(action)

                document.form.add(button)

        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding navigation buttons: {e}")

```

Este código adiciona botões de navegação a cada página de um documento PDF, facilitando a movimentação dos usuários entre as páginas. Ele começa determinando os caminhos completos dos arquivos de entrada e saída usando um método auxiliar. A lista button_config define quatro tipos de botões de navegação — Primeira Página, Página Anterior, Próxima Página e Última Página — juntamente com suas posições horizontais, as ações de navegação pré-definidas que eles acionam e uma função lambda que determina se cada botão deve ser somente leitura em uma dada página (por exemplo, os botões "Primeira Página" e "Página Anterior" são somente leitura na primeira página).

O código então carrega o PDF e itera por cada página. Para cada página, ele percorre as configurações dos botões, criando uma área retangular para cada botão e instanciando um ButtonField naquele local. Cada botão recebe um nome, seu status de somente leitura é definido com base na página atual, e sua ação de clique é atribuída à ação de navegação correspondente. O botão então é adicionado aos campos de formulário do PDF.

Depois que todos os botões são adicionados a todas as páginas, o documento modificado é salvo. Se ocorrerem erros durante esse processo, eles são capturados e impressos. Essa abordagem garante que cada página tenha um conjunto consistente de controles de navegação, melhorando a usabilidade de PDFs multipágina. Uma sutileza é o uso da lambda is_readonly_fn para desativar botões de navegação quando eles não fariam sentido (por exemplo, "Próxima Página" na última página), o que ajuda a prevenir confusão do usuário.

### Usando ações de impressão

Ao usar formulários PDF, muitas vezes há necessidade de imprimir esses documentos PDF. Essa ação pode ser realizada usando um leitor de PDF, mas às vezes é mais conveniente fazê-lo diretamente do documento usando um botão especial.

Na verdade, este é mais um exemplo de como usar ações nomeadas. Usaremos `PredefinedAction.FILE_PRINT` (simulando o uso do item de menu Arquivo->Imprimir), mas você também pode usar `PredefinedAction.PRINT` ou `PredefinedAction.PRINT_DIALOG`, dependendo dos seus próprios propósitos.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_print(self, infile, outfile):
    """
    Add a print button to the first page of the PDF.

    Creates a button labeled "Print" that triggers the system print dialog
    when clicked. The button is positioned at the bottom-left corner of
    the first page with a 1-pixel border.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_print("input.pdf", "output.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)
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
    document.save(path_outfile)

```

Este trecho de código demonstra como adicionar um botão "Print" à primeira página de um documento PDF. Ele começa carregando o PDF a partir do caminho de arquivo de entrada especificado e selecionando a primeira página (document.pages[1]).

Uma área retangular é definida para a posição e tamanho do botão na página. Um ButtonField é então criado neste local, com o nome "printButton," e seu valor exibido é definido como "Print". O botão é configurado para que, quando for clicado (especificamente, quando o botão do mouse for liberado), ele acione a ação predefinida "Print File", solicitando ao visualizador de PDF que abra a caixa de diálogo de impressão.

Para melhorar a aparência do botão, uma borda é criada e atribuída ao botão, com sua largura definida em 1 unidade. O botão é então adicionado aos campos de formulário PDF na primeira página. Finalmente, o documento modificado é salvo no caminho de arquivo de saída. Essa abordagem oferece aos usuários uma maneira conveniente de imprimir o documento diretamente a partir do PDF. Observe que a eficácia desse recurso depende do suporte do visualizador de PDF a campos de formulário interativos e ações predefinidas.

### Usando ação Hide

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_hide(self, infile, outfile):
    """
    Add a hide button that toggles visibility of all checkbox fields.

    Creates a button labeled "Hide Checkboxes" that can hide or show
    all checkbox fields in the document. Useful for forms with many
    checkboxes that might clutter the interface.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_hide("form.pdf", "form_with_hide.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    try:
        document = ap.Document(path_infile)
        # Collect all checkbox fields in the document
        checkboxes = [field for field in document.form if isinstance(field, ap.CheckboxField)]

        # Create the hide button
        rect = Rectangle(10, 510, 100, 540)
        hide_button = ButtonField(document.pages[1], rect)
        hide_button.partial_name = "HideButton"
        hide_button.value = "Hide Checkboxes"

        # Add HideAction to button - will hide all checkboxes when clicked
        hide_button.actions.on_release_mouse_btn = ap.HideAction(checkboxes, True)

        # Add button to the form on page 1
        document.form.add(hide_button, 1)

        # Save the modified PDF
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding hide button: {e}")

```

Este trecho de código adiciona um botão à primeira página de um PDF que, quando clicado, oculta todos os campos de caixa de seleção no documento. Ele começa resolvendo os caminhos completos de entrada e saída usando um método auxiliar. O PDF é carregado, e todos os campos de caixa de seleção são coletados filtrando os campos de formulário por instâncias de `ap.CheckboxField`.

Uma área retangular é definida para a posição do novo botão próximo ao topo da página. Um ButtonField é criado neste local, nomeado "HideButton," e rotulado "Hide Checkboxes". O botão é configurado para que, quando for clicado (ao liberar o botão do mouse), ele acione um HideAction que oculta todas as caixas de seleção coletadas.

O botão é então adicionado aos campos de formulário na primeira página, e o PDF modificado é salvo no arquivo de saída. Se ocorrerem erros durante este processo, eles são capturados e impressos. Esse recurso oferece aos usuários uma maneira rápida de ocultar todas as caixas de seleção no PDF, o que pode ser útil para personalizar a aparência ou o fluxo de trabalho do documento.

### Aplicando ação Submit

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_submit_action(self, infile, outfile):
    """
    Submit form.

    Parameters:
    - infile (str): The name of the input PDF file.
    - outfile (str): The name of the output PDF file.
    """
    path_infile = self.dataDir + infile
    path_outfile = self.dataDir + outfile

    try:
        document = ap.Document(path_infile)

        # Create the submit action
        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        # Create the submit button
        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        # Add the button to the form on page 1
        document.form.add(submit_button, 1)

        # Save the document
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding submit button: {e}")

```

Esta função adiciona um botão "Submit" à primeira página de um formulário PDF, permitindo que os usuários enviem os dados do formulário para um endpoint web especificado. Ela começa construindo os caminhos completos para os arquivos PDF de entrada e saída, então carrega o PDF de entrada usando a biblioteca Aspose.PDF.

Um `SubmitFormAction` é criado para definir o comportamento quando o botão é clicado. A URL da ação é configurada usando um `FileSpecification` apontando para http://localhost:3000/submit, o que significa que os dados do formulário serão enviados para essa URL. A propriedade flags combina `EXPORT_FORMAT` e `SUBMIT_COORDINATES`, garantindo que os dados do formulário sejam exportados em um formato padrão e que as coordenadas do clique do botão sejam incluídas na submissão.

Uma área retangular é definida para a posição e tamanho do botão na página. Um ButtonField é criado neste local na primeira página, com o nome "SubmitButton," e seu valor exibido é definido como "Submit". A ação de envio é atribuída ao evento de liberação do mouse do botão, de modo que a ação seja acionada quando o usuário clicar no botão.

Finalmente, o botão é adicionado aos campos de formulário na primeira página, e o PDF modificado é salvo no arquivo de saída. Se ocorrerem erros durante este processo, eles são capturados e impressos. Essa abordagem oferece uma maneira amigável para os usuários de PDF enviarem os dados do formulário diretamente para um endpoint de servidor.

