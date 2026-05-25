---
title: Obter valores de campo
type: docs
weight: 50
url: /pt/python-net/get-field-values/
description: Recuperando valores de campo de um formulário PDF com Aspose.PDF Facades usando a classe Form.
lastmod: "2026-05-18"
---

Este trecho de código mostra como recuperar os valores atuais dos campos de formulário de um documento PDF usando a API Aspose.PDF Facades. O [get_field()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/#methods) método permite que você acesse programaticamente os dados inseridos em campos de texto, caixas de seleção, botões de opção e outros elementos AcroForm.

1. Vincule o PDF a um objeto Form.
1. Especifique os nomes dos campos que você deseja ler.
1. Recupere o valor de cada campo usando get_field().

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir


    # Get field values
    def get_field_values(infile):
        """Get field values from a PDF document."""
        # Create Form object
        pdf_form = pdf_facades.Form()

        # Bind PDF document
        pdf_form.bind_pdf(infile)

        # Get field values by their names
        field_names = ["First Name", "Last Name"]
        for field_name in field_names:
            value = pdf_form.get_field(field_name)
            print(f"Value of '{field_name}': {value}")
```