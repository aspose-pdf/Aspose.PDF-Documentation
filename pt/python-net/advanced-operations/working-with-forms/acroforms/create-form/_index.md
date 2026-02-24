---
title: Criar AcroForm - Criar PDF preenchível em Python
linktitle: Criar AcroForm
type: docs
weight: 10
url: /pt/python-net/create-form/
description: Com o Aspose.PDF para Python você pode criar um formulário do zero no seu arquivo PDF
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como criar AcroForm em PDF usando Python
Abstract: O artigo fornece um guia sobre como criar um campo de formulário em um documento PDF usando a biblioteca Aspose.PDF para Python. Ele apresenta a classe `Document`, que contém uma coleção `Form` para gerenciar campos de formulário. O processo de adicionar um campo de formulário envolve criar o campo desejado e utilizar o método `add` da coleção `Form`. Um exemplo específico é fornecido para ilustrar a adição de um `TextBoxField` a um documento PDF. O exemplo inclui código detalhado demonstrando a criação de um `TextBoxField`, configurando suas propriedades como posição, nome, valor, borda e cor, e, subsequentemente, adicionando-o ao documento. O PDF modificado é então salvo com o campo de formulário recém adicionados.
---

## Criar formulário do zero

### Adicionar campo de formulário em um documento PDF

A classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) fornece uma coleção chamada [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) que ajuda a gerenciar campos de formulário em um documento PDF.

Para adicionar um campo de formulário:

1. Crie o campo de formulário que deseja adicionar.
1. Chame o método [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) da coleção Form.

### Adicionando TextBoxField

O exemplo abaixo mostra como adicionar um [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Open document
    pdfDocument = ap.Document(path_infile)

    # Create a field
    textBoxField = ap.forms.TextBoxField(pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True))
    textBoxField.partial_name = "textbox1"
    textBoxField.value = "Text Box"

    border = ap.annotations.Border(textBoxField)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    textBoxField.border = border

    textBoxField.color = ap.Color.green

    # Add field to the document
    pdfDocument.form.add(textBoxField, 1)

    # Save modified PDF
    pdfDocument.save(path_outfile)
```


