---
title: Anotações Interativas usando Python
linktitle: Anotações Interativas
type: docs
weight: 60
url: /pt/python-net/interactive-annotations/
description: Aprenda a adicionar, ler e excluir anotações de link, e como criar botões de navegação e impressão em documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabalhe com anotações e botões interativos de PDF em Python.
Abstract: Este artigo explica como trabalhar com anotações interativas em arquivos PDF usando Aspose.PDF for Python via .NET. Ele aborda a adição de anotações de link, a leitura de áreas de link existentes, a exclusão de anotações de link, a criação de botões de navegação de página e a adição de um botão de impressão a um documento PDF.
---

Este artigo mostra como trabalhar com anotações interativas em documentos PDF usando Aspose.PDF for Python via .NET.

O script de exemplo demonstra vários fluxos de trabalho comuns:

- adicionar uma anotação de link ao texto existente
- obter retângulos de anotação de link de uma página
- excluir anotações de link
- criar botões de navegação
- criar um botão de impressão

## Anotação de link

### Adicionar Anotação de Link

Este exemplo procura o fragmento de texto na primeira página `"file"` e coloca uma anotação de link clicável sobre a área de texto correspondente. Quando o usuário clica na anotação, o PDF abre o endereço web especificado.

#### Carregue o documento e encontre o texto-alvo

Criar um `Document` objeto e usar `TextFragmentAbsorber` para procurar o texto que se tornará interativo.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

document.pages[1].accept(text_fragment_absorber)
phone_number_fragment = text_fragment_absorber.text_fragments[1]
```

#### Criar a anotação de link

Construir um `LinkAnnotation` usando o retângulo do fragmento de texto correspondido e atribuindo uma ação URI a ele.

```python
link_annotation = ap.annotations.LinkAnnotation(
    document.pages[1], phone_number_fragment.rectangle
)
link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")
```

#### Adicione a anotação e salve o PDF

Anexe a anotação à página e salve o arquivo atualizado.

```python
document.pages[1].annotations.append(link_annotation)
document.save(outfile)
```

#### Exemplo completo

```python
def link_add(infile, outfile):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber("file")

    document.pages[1].accept(text_fragment_absorber)
    phone_number_fragment = text_fragment_absorber.text_fragments[1]

    link_annotation = ap.annotations.LinkAnnotation(
        document.pages[1], phone_number_fragment.rectangle
    )
    link_annotation.action = ap.annotations.GoToURIAction("https://www.aspose.com")

    document.pages[1].annotations.append(link_annotation)
    document.save(outfile)
```

### Obter Anotação de Link

Para inspecionar os links interativos existentes, filtre a coleção de anotações na primeira página e mantenha apenas os itens cujo tipo é `LINK`. O exemplo então imprime o retângulo para cada anotação correspondente.

#### Carregue o PDF e colete anotações de link

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Ler os retângulos de anotação

Percorra as anotações filtradas e imprima as coordenadas de cada área de link.

```python
for link_annotation in link_annotations:
    print(link_annotation.rect)
```

#### Exemplo completo

```python
def link_get(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        print(link_annotation.rect)
```

### Excluir Anotação de Link

Este fluxo de trabalho remove todas as anotações de link da primeira página e salva o PDF limpo como um novo arquivo.

#### Encontre as anotações de link para remover

```python
document = ap.Document(infile)
link_annotations = [
    a
    for a in document.pages[1].annotations
    if (a.annotation_type == ap.annotations.AnnotationType.LINK)
]
```

#### Exclua cada anotação de link

```python
for link_annotation in link_annotations:
    document.pages[1].annotations.delete(link_annotation)
```

#### Salvar o documento atualizado

```python
document.save(outfile)
```

#### Exemplo completo

```python
def link_delete(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for link_annotation in link_annotations:
        document.pages[1].annotations.delete(link_annotation)

    document.save(outfile)
```

## Anotação de Widget

### Adicionar Botão de Navegação

Botões de navegação são úteis em PDFs de várias páginas quando você quer que os leitores se movimentem entre as páginas sem usar a interface do visualizador. Este exemplo adiciona `Previous Page` e `Next Page` botões para cada página.

#### Definir configurações do botão

Armazene as legendas dos botões, posições e ações predefinidas em uma lista de configuração simples.

```python
button_config = [
    ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
    ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
]
```

#### Carregue o PDF e verifique se há várias páginas

O exemplo abre o documento de origem e adiciona mais uma página, de modo que as ações de navegação tenham pelo menos duas páginas para trabalhar.

```python
document = ap.Document(infile)
document.pages.add()
```

#### Crie os botões em cada página

Para cada página, crie um `ButtonField`, defina seu texto e cores, atribua uma ação de navegação predefinida e adicione-o ao formulário.

```python
for page in document.pages:
    for name, x_pos, action in button_config:
        rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
        button = ap.forms.ButtonField(page, rect)
        button.partial_name = name
        button.value = name
        button.characteristics.border = ap.Color.red.to_rgb()
        button.characteristics.background = ap.Color.orange.to_rgb()
        button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
        document.form.add(button)
```

#### Salvar o resultado

```python
document.save(outfile)
```

#### Exemplo completo

```python
def navigation_buttons_add(infile, outfile):
    button_config = [
        ("Previous Page", 120.0, ap.annotations.PredefinedAction.PREV_PAGE),
        ("Next Page", 230.0, ap.annotations.PredefinedAction.NEXT_PAGE),
    ]

    document = ap.Document(infile)
    document.pages.add()

    for page in document.pages:
        for name, x_pos, action in button_config:
            rect = ap.Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ap.forms.ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            button.actions.on_release_mouse_btn = ap.annotations.NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

### Adicionar Botão de Impressão

Este exemplo cria um novo PDF de uma página e coloca um botão de impressão próximo ao topo da página. Clicar no botão aciona a ação de impressão predefinida em um visualizador de PDF compatível.

#### Crie um novo PDF e adicione uma página

```python
document = ap.Document()
page = document.pages.add()
```

#### Criar e configurar o botão

Defina o retângulo do botão, crie o `ButtonField`, defina sua legenda e anexe a ação de impressão.

```python
rect = ap.Rectangle(72, 748, 164, 768, True)

print_button = ap.forms.ButtonField(page, rect)
print_button.alternate_name = "Print current document"
print_button.color = ap.Color.black
print_button.partial_name = "printBtn1"
print_button.value = "Print Document"
print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
    ap.annotations.PredefinedAction.FILE_PRINT
)
```

#### Definir estilos de borda e plano de fundo

O exemplo define uma borda sólida e aplica cores personalizadas para tornar o botão visível no documento.

```python
border = ap.annotations.Border(print_button)
border.style = ap.annotations.BorderStyle.SOLID
border.width = 2
print_button.border = border

print_button.characteristics.border = ap.Color.blue.to_rgb()
print_button.characteristics.background = ap.Color.light_blue.to_rgb()
```

#### Adicione o botão e salve o PDF

```python
document.form.add(print_button)
document.save(outfile)
```

#### Exemplo completo

```python
def print_button_add(infile, outfile):
    document = ap.Document()
    page = document.pages.add()

    rect = ap.Rectangle(72, 748, 164, 768, True)

    print_button = ap.forms.ButtonField(page, rect)
    print_button.alternate_name = "Print current document"
    print_button.color = ap.Color.black
    print_button.partial_name = "printBtn1"
    print_button.value = "Print Document"
    print_button.actions.on_release_mouse_btn = ap.annotations.NamedAction(
        ap.annotations.PredefinedAction.FILE_PRINT
    )

    border = ap.annotations.Border(print_button)
    border.style = ap.annotations.BorderStyle.SOLID
    border.width = 2
    print_button.border = border

    print_button.characteristics.border = ap.Color.blue.to_rgb()
    print_button.characteristics.background = ap.Color.light_blue.to_rgb()

    document.form.add(print_button)
    document.save(outfile)
```

## Tópicos Relacionados

- [Importar e Exportar Anotações](/python-net/import-export-annotations/)
- [Anotações de marcação](/python-net/markup-annotations/)
- [Anotações de Mídia](/python-net/media-annotations/)
- [Anotações de Segurança](/python-net/security-annotations/)
- [Anotações de Forma](/python-net/shape-annotations/)
- [Anotações Baseadas em Texto](/python-net/text-based-annotations/)
- [Anotações de Marca d'Água](/python-net/watermark-annotations/)
