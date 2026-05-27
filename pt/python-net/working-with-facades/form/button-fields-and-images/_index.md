---
title: Campos de Botão e Imagens
type: docs
weight: 40
url: /pt/python-net/button-fields-and-images/
description: Este exemplo demonstra como gerenciar campos de botão em um formulário PDF usando a API Aspose.PDF Facades.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Adicionando Aparência de Imagem a Campos de Botão & Lendo Sinais de Submissão
Abstract: Formulários PDF frequentemente incluem botões interativos que acionam ações JavaScript ou enviam os dados do formulário. Você pode melhorar visualmente os campos de botão adicionando imagens como sua aparência e inspecionar programaticamente seu comportamento de envio.
---

## Adicionar Aparência de Imagem a Campos de Botão

Este trecho de código explica como adicionar uma aparência de imagem a um campo de botão existente em um formulário PDF. A operação melhora a apresentação visual de um botão PDF substituindo sua aparência padrão por uma imagem personalizada.

1. Crie um objeto Form.
1. Vincule o arquivo PDF ao objeto Form.
1. Adicione imagem ao campo Button.

    - Determine o caminho para o arquivo de imagem associado ao PDF
    - Abra a imagem em modo binário como image_stream.
    - Chame fill_image_field() com o nome totalmente qualificado do campo de botão.

1. Salvar o PDF atualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Add image appearance to button fields
def add_image_appearance_to_button_fields(infile, outfile):
    """Add image appearance to button fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Add image appearance to button fields by providing the field name and image stream
    image_path = infile.replace(".pdf", ".jpg")
    with open(image_path, "rb") as image_stream:
        pdf_form.fill_image_field("Image1_af_image", image_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```

## Obter Flags de Envio

A biblioteca Python ajuda você a recuperar os flags de envio de um botão de envio em um formulário PDF usando a API Aspose.PDF Facades. Os flags de envio definem o comportamento de um botão de envio, como se ele envia todo o formulário, inclui anotações ou envia em formato FDF, XFDF, PDF ou HTML.

1. Crie um objeto Form.
1. Chame get_submit_flags() no objeto form usando o nome totalmente qualificado do botão submit.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_submit_flags(infile, outfile):
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)
    flags = pdf_form.get_submit_flags("Submit1_af_submit")

    print(f"Submit flags: {flags}")
```
