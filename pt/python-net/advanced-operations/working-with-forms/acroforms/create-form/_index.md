---
title: Criar AcroForm - Criar PDF preenchível em Python
linktitle: Criar AcroForm
type: docs
weight: 10
url: /pt/python-net/create-form/
description: Crie campos AcroForm do zero em documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como criar AcroForm em PDF usando Python
Abstract: Este artigo explica como criar campos AcroForm em documentos PDF usando o Aspose.PDF for Python via .NET. Ele abrange a criação básica de campos com TextBoxField, a personalização da aparência de caixas de texto com múltiplos widgets e tipos de campo adicionais, como botões de opção, caixas de combinação, caixas de seleção, caixas de lista, campos de assinatura e campos de código de barras. Esses exemplos ajudam a criar formulários PDF interativos para coleta de dados e fluxos de trabalho de automação de documentos.
---

## Criar Form a partir do zero

### Adicionar Campo de Formulário em um Documento PDF

O [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) a classe fornece uma coleção chamada [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) que ajuda a gerenciar campos de formulário em um documento PDF.

Para adicionar um campo de formulário:

1. Crie o campo de formulário que você deseja adicionar.
1. Chame a coleção Form [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) método.

### Adicionando TextBoxField

O exemplo a seguir mostra como adicionar um [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rectangle = ap.Rectangle(10, 600, 110, 620, True)
    text_box_field = ap.forms.TextBoxField(page, rectangle)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Text Box"

    text_box_field.default_appearance = ap.annotations.DefaultAppearance(
        "Arial", 10, drawing.Color.dark_blue
    )

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field, 1)
    document.save(output_file_name)
```

### Campo de Caixa de Texto Multi-Widget em PDF

Crie um campo de formulário de caixa de texto com várias aparências de widget em um PDF usando Python e Aspose.PDF. Ele coloca várias áreas de entrada de texto em uma página, aplica diferentes fontes e cores a cada widget, personaliza bordas e define o estilo de fundo para um formulário PDF interativo.

1. Criar Novo Documento PDF.
1. Definir posições dos campos de texto.
1. Criar Aparências Padrão Diferentes.
1. Criar Campo de Caixa de Texto.
1. Aplicar Aparência a Cada Widget.
1. Personalizar o estilo da borda.
1. Adicionar campo ao Form.
1. Salvar arquivo PDF.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field_nt(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rects = [
        ap.Rectangle(10, 600, 110, 620, normalize_coordinates=True),
        ap.Rectangle(10, 630, 110, 650, normalize_coordinates=True),
        ap.Rectangle(10, 660, 110, 680, normalize_coordinates=True),
    ]

    default_appearances = [
        ap.annotations.DefaultAppearance("Arial", 10, drawing.Color.dark_blue),
        ap.annotations.DefaultAppearance("Helvetica", 12, drawing.Color.dark_green),
        ap.annotations.DefaultAppearance(
            ap.text.FontRepository.find_font("Calibri"), 14, drawing.Color.dark_magenta
        ),
    ]

    text_box_field = ap.forms.TextBoxField(page, rects)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Some text"

    for i, widget in enumerate(text_box_field):
        widget.default_appearance = default_appearances[i]

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field)
    document.save(output_file_name)
```

## Adicionando Outros Campos de Formulário

Os trechos de código a seguir demonstram como adicionar vários tipos de campos, como botões de opção, caixas de combinação, caixas de seleção, caixas de lista, campos de assinatura e campos de código de barras. Cada função cria um novo documento PDF, adiciona um campo de destino com as opções selecionadas e salva o arquivo atualizado.

1. Adicionar campo de Botão de Opção
1. Adicionar Campo de Caixa de Combinação
1. Adicionar campo de caixa de seleção
1. Adicionar Campo de Lista
1. Adicionar Campo de Assinatura
1. Adicionar Campo de Código de Barras

### Adicionar campo de Botão de Opção

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_radio_button(output_file_name):
    document = ap.Document()
    document.pages.add()

    radio = ap.forms.RadioButtonField(document.pages[1])
    radio.add_option(
        "Option 1", ap.Rectangle(100, 640, 120, 680, normalize_coordinates=True)
    )
    radio.add_option(
        "Option 2", ap.Rectangle(140, 640, 160, 680, normalize_coordinates=True)
    )

    document.form.add(radio)
    document.save(output_file_name)
```

### Adicionar Campo de Caixa de Combinação

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_combo_box(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    combo = ap.forms.ComboBoxField(
        page, ap.Rectangle(100, 640, 150, 656, normalize_coordinates=True)
    )
    combo.add_option("Red")
    combo.add_option("Yellow")
    combo.add_option("Green")
    combo.add_option("Blue")
    combo.selected = 3

    document.form.add(combo)
    document.save(output_file_name)
```

### Adicionar campo de caixa de seleção

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_checkbox_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    checkbox = ap.forms.CheckboxField(
        page, ap.Rectangle(50, 620, 100, 650, normalize_coordinates=True)
    )
    checkbox.characteristics.background = ap.Color.aqua.to_rgb()
    checkbox.style = ap.forms.BoxStyle.CIRCLE

    document.form.add(checkbox)
    document.save(output_file_name)
```

### Adicionar Campo de Lista

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_list_box_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    list_box = ap.forms.ListBoxField(
        page, ap.Rectangle(50, 650, 100, 700, normalize_coordinates=True)
    )
    list_box.partial_name = "list"
    list_box.add_option("Red")
    list_box.add_option("Green")
    list_box.add_option("Blue")

    document.form.add(list_box)
    document.save(output_file_name)
```

### Adicionar Campo de Assinatura

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_signature_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    signature_field = ap.forms.SignatureField(
        page, ap.Rectangle(100, 700, 200, 800, True)
    )
    signature_field.partial_name = "Signature1"
    document.form.add(signature_field)
    document.save(output_file_name)
```

### Adicionar Campo de Código de Barras

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_barcode_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    barcode = ap.forms.BarcodeField(page, ap.Rectangle(100, 700, 200, 740, True))
    barcode.partial_name = "Barcode1"
    barcode.add_barcode("1234567890")
    document.form.add(barcode)
    document.save(output_file_name)
```

## Tópicos Relacionados

- [Preencher AcroForm](/pdf/pt/python-net/fill-form/)
- [Extrair AcroForm](/pdf/pt/python-net/extract-form/)
- [Modificando AcroForm](/pdf/pt/python-net/modifying-form/)
- [Importar e Exportar Dados de Formulário](/pdf/pt/python-net/import-export-form-data/)
