---
title: Extrair AcroForm - Extrair Dados de Formulário de PDF em Python
linktitle: Extrair AcroForm
type: docs
weight: 30
url: /pt/python-net/extract-form/
description: Extraia o formulário do seu documento PDF com a biblioteca Aspose.PDF for Python. Obtenha o valor de um campo individual do arquivo PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como obter Dados de Formulário de PDF usando Python
Abstract: Este artigo fornece um guia sobre como extrair dados de campos de formulário dentro de um documento PDF usando Python. Ele descreve como navegar por todos os campos usando a biblioteca Aspose.PDF, especificamente acessando a coleção `Form` e utilizando o tipo `Field` e sua propriedade `value`. Um trecho de código Python de exemplo está incluído, demonstrando como abrir um documento PDF, iterar pelos seus campos de formulário e imprimir o nome e o valor de cada campo. Este método é útil para recuperar programaticamente os dados de formulário de arquivos PDF.
---

## Extrair dados do formulário

### Obter valores de todos os campos do documento PDF

Para obter valores de todos os campos em um documento PDF, você precisa navegar por todos os campos de formulário e então obter o valor usando a propriedade Value. Obtenha cada campo da coleção Form, no tipo de campo base chamado [Campo](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) e acesse sua propriedade [valor](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties).

Os seguintes trechos de código Python mostram como obter os valores de todos os campos de um documento PDF.

```python

    import aspose.pdf as ap

    # Construct the full path to the input PDF file
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    # Create a Form object from the PDF file
    form = ap.facades.Form(path_infile)

    # Initialize an empty dictionary to store form values
    form_values = {}

    # Iterate through all form fields in the PDF
    for formField in form.field_names:
        # Retrieve the value for each form field and store in the dictionary
        form_values[formField] = form.get_field(formField)

    # Print and return the extracted form values
    print(form_values)
```

