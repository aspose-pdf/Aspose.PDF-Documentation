---
title: Adicionar dicas de ferramenta ao texto PDF em Python
linktitle: Dica de ferramenta PDF
type: docs
weight: 20
url: /pt/python-net/pdf-tooltip/
description: Aprenda como adicionar dicas de ferramenta a fragmentos de texto em documentos PDF em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar dicas de ferramenta interativas a fragmentos de texto PDF usando Python
Abstract: Este artigo fornece dois exemplos em Python para adicionar ajuda interativa ao texto de PDF usando Aspose.PDF for Python via .NET. O primeiro exemplo adiciona tooltips aos fragmentos de texto correspondentes, colocando elementos `ButtonField` invisíveis e definindo `alternate_name`. O segundo exemplo cria um `TextBoxField` oculto que aparece ao passar o mouse, conectando eventos `HideAction` a um `ButtonField` invisível.
---

## Adicionar Tooltip ao Texto Pesquisado em um PDF

Este trecho de código mostra como sobrepor invisível [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) elementos em específico [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) objetos em um PDF para exibir dicas de ferramenta quando o usuário passa o mouse sobre eles. Ele suporta mensagens de dica curtas e longas usando o `alternative_name` propriedade de `ButtonField`.

Use esta página quando precisar tornar o texto do PDF mais interativo, adicionando ajuda ao passar o mouse, explicações inline ou notas contextuais.

1. Criar um novo [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Salvar o documento inicial.
1. Reabrir o documento PDF.
1. Pesquisar texto de destino usando [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Adicionar um invisível [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) com uma tooltip curta.
1. Pesquisar o segundo texto-alvo.
1. Adicionar um invisível [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) com uma dica de ferramenta longa sobre o fragmento correspondente.
1. Salvar o documento final.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

# region PDF Tooltip
def add_tool_tip_to_searched_text(outfile):
    # Create PDF document
    with ap.Document() as document:
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display a tooltip")
        )
        document.pages[1].paragraphs.add(
            ap.text.TextFragment(
                "Move the mouse cursor here to display a very long tooltip"
            )
        )
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a tooltip"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the extracted text fragments
        text_fragments = absorber.text_fragments

        # Loop through the fragments
        for fragment in text_fragments:
            # Create invisible button on text fragment position
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # alternate_name value will be displayed as tooltip by a viewer application
            field.alternate_name = "Tooltip for text."
            # Add button field to the document
            document.form.add(field)

        # Next will be sample of very long tooltip
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a very long tooltip"
        )
        document.pages.accept(absorber)
        text_fragments = absorber.text_fragments

        for fragment in text_fragments:
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # Set very long text
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

        # Save document
        document.save(outfile)
```

## Criar um Bloco de Texto Oculto Que Aparece ao Passar o Mouse em um PDF

Adicione texto flutuante interativo a um documento PDF. Ele sobrepõe um invisível [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) em uma frase-alvo e revela um oculto [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) quando o usuário passa o mouse sobre ele. Esta técnica é ideal para ajuda contextual, anotações ou apresentação de conteúdo dinâmico.

1. Crie um novo documento PDF.
1. Salve o PDF para que ele possa ser reaberto para configuração de interatividade.
1. Reabrir o documento PDF.
1. Localize o texto alvo usando [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. Crie um oculto [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. Adicione o campo oculto ao documento [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) coleção.
1. Crie um invisível [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. Atribuir ações do mouse (`on_enter`, `on_exit`) usando [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) para mostrar/ocultar o campo oculto.
1. Salvar o documento final.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

def create_hidden_text_block(outfile):
    # Create PDF document
    with ap.Document() as document:
        #  Add paragraph with text
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display floating text")
        )
        # Save PDF document
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the first extracted text fragment
        text_fragments = absorber.text_fragments
        fragment = text_fragments[1]

        # Create hidden text field for floating text in the specified rectangle of the page
        floating_field = ap.forms.TextBoxField(
            fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
        )
        # Set text to be displayed as field value
        floating_field.value = 'This is the "floating text field".'
        # We recommend to make field 'readonly' for this scenario
        floating_field.read_only = True
        # Set 'hidden' flag to make field invisible on document opening
        floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

        # Setting a unique field name isn't necessary but allowed
        floating_field.partial_name = "FloatingField_1"

        # Setting characteristics of field appearance isn't necessary but makes it better
        floating_field.default_appearance = ap.annotations.DefaultAppearance(
            "Helv", 10, drawing.Color.blue
        )
        floating_field.characteristics.background = drawing.Color.light_blue
        floating_field.characteristics.border = drawing.Color.dark_blue
        floating_field.border = ap.annotations.Border(floating_field)
        floating_field.border.width = 1
        floating_field.multiline = True

        # Add text field to the document
        document.form.add(floating_field)
        # Create invisible button on text fragment position
        button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Create new hide action for specified field (annotation) and invisibility flag.
        # (You also may refer floating field by the name if you specified it above.)
        # Add actions on mouse enter/exit at the invisible button field

        button_field.actions.on_enter = ap.annotations.HideAction(floating_field, False)
        button_field.actions.on_exit = ap.annotations.HideAction(floating_field)

        # Add button field to the document
        document.form.add(button_field)

        # Save document
        document.save(outfile)
```

## Tópicos de Texto Relacionados

- [Trabalhe com texto em PDF usando Python](/pdf/pt/python-net/working-with-text/)
- [Use FloatingBox para layout de texto PDF em Python](/pdf/pt/python-net/floating-box/)
- [Pesquisar e extrair texto de PDF em Python](/pdf/pt/python-net/search-and-get-text-from-pdf/)
- [Adicionando texto ao PDF](/pdf/pt/python-net/add-text-to-pdf-file/)