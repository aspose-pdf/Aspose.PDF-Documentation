---
title: Preencher AcroForm - Preencher Formulário PDF usando Python
linktitle: Preencher AcroForm
type: docs
weight: 20
url: /pt/python-net/fill-form/
description: Você pode preencher formulários no seu documento PDF com a biblioteca Aspose.PDF para Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como preencher campo de formulário em PDF usando Python
Abstract: O artigo fornece um guia sobre como preencher um campo de formulário em um documento PDF usando a biblioteca Aspose.PDF para Python. Ele explica o processo de acesso a um campo de formulário a partir da coleção de formulários do documento e a definição de seu valor através da propriedade value do campo. O código de exemplo demonstra como abrir um documento PDF, iterar pelos seus campos de formulário para encontrar um campo específico pelo nome parcial (neste caso, "Field 1"), e modificar o valor de um TextBoxField para "777". Finalmente, o documento atualizado é salvo em um arquivo de saída. Links para a documentação relevante da Aspose são fornecidos para referência adicional.
---

## Preencher Campo de Formulário em um Documento PDF

O próximo exemplo preenche campos de formulário PDF com novos valores usando Aspose.PDF para Python via .NET e salva o documento atualizado. Suporta a atualização de vários campos especificando um dicionário de nomes de campos e valores.

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Define the new field values
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New"
    }

    # Create a Form object from the input PDF file
    form = ap.facades.Form(path_infile)

    # Fill out the form fields with the new values
    for formField in form.field_names:
        if formField in new_field_values:
            form.fill_field(formField, new_field_values[formField])

    # Save the modified form to the output PDF file
    form.save(path_outfile)
```



