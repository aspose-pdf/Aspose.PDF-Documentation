---
title: Obter Fachadas de Campo
type: docs
weight: 10
url: /pt/python-net/get-field-facades/
description: Este exemplo demonstra como ler os valores de campos de formulário específicos de um documento PDF usando a API Aspose.PDF Facades.
lastmod: "2026-05-18"
---

Os formulários PDF contêm campos onde os usuários podem inserir dados, como caixas de texto, caixas de seleção ou botões de opção. Para processar esses formulários programaticamente, muitas vezes é necessário recuperar os valores atuais desses campos.

1. Crie um objeto Form.
1. Vincule o documento PDF ao objeto de formulário.
1. Recuperar Valores dos Campos.

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