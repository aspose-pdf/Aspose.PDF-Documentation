---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
weight: 45
url: /pt/python-net/modifying-form/
description: Modificando formulário no seu arquivo PDF com a biblioteca Aspose.PDF for Python via .NET. Você pode adicionar ou remover campos em um formulário existente, obter e definir o limite de campo, etc.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerenciamento e Personalização de Campos de Formulário PDF
Abstract: Esta coleção de exemplos apresenta várias técnicas para gerenciar e personalizar campos de formulário PDF usando Aspose.PDF for Python via .NET. Inclui métodos para limpar texto de campos de formulário no estilo Máquina de Escrever usando TextFragmentAbsorber, definir e recuperar limites de caracteres com FormEditor, aplicar fontes e estilos personalizados a campos de caixa de texto, e remover campos de formulário específicos por nome. Essas operações permitem que desenvolvedores sanitizem, formatem e adaptem formulários PDF para redistribuição, branding ou validação de dados, suportando tanto refinamento estético quanto funcional em fluxos de trabalho de documentos automatizados.
---

## Limpar Texto no Formulário

Este exemplo demonstra como limpar texto de campos de formulário Tipo Máquina de Escrever em um PDF usando Aspose.PDF for Python via .NET. Ele analisa a primeira página do PDF, identifica formulários Tipo Máquina de Escrever, remove seu conteúdo e salva o documento atualizado. Essa abordagem é útil para redefinir ou sanitizar campos de formulário antes de redistribuir um PDF.

1. Carregue o documento PDF de entrada.
1. Acesse os formulários na primeira página.
1. Itere sobre cada formulário e verifique se é um formulário `Typewriter`.
1. Use TextFragmentAbsorber para encontrar fragmentos de texto no formulário.
1. Limpe o texto de cada fragmento.
1. Salve o PDF modificado no arquivo de saída.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    dataDir = "path/to/your/data/dir/"
    path_infile = dataDir + infile
    path_outfile = dataDir + outfile
    document = ap.Document(path_infile)

    # Get the forms from the first page
    forms = document.pages[1].resources.forms

    for form in forms:
        # Check if the form is of type "Typewriter" and subtype "Form"
        if (form.it == "Typewriter" and form.subtype == "Form"):
            # Create a TextFragmentAbsorber to find text fragments
            absorber = ap.Text.TextFragmentAbsorber()
            absorber.visit(form)

            # Clear the text in each fragment
            for fragment in absorber.text_fragments:
                fragment.Text = ""

    # Save PDF document
    document.save(path_outfile)
```

## Obter ou Definir Limite de Campo

O método set_field_limit(field, limit) da classe FormEditor permite definir um limite de campo, o número máximo de caracteres que podem ser inseridos em um campo.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Create FormEditor instance
    form = ap.facades.FormEditor()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Set field limit for "First Name"
    form.set_field_limit("First Name", 15)

    # Save PDF document
    form.save(path_outfile)
```

Da mesma forma, o Aspose.PDF possui um método que obtém o limite de campo.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {textBoxField.max_len}")
```

## Definir Fonte Personalizada para o Campo de Formulário

Os campos de formulário em arquivos PDF da Adobe podem ser configurados para usar fontes padrão específicas. Nas versões iniciais do Aspose.PDF, apenas as 14 fontes padrão eram suportadas. Lançamentos posteriores permitiram que desenvolvedores aplicassem qualquer fonte.

Este código atualiza a aparência de um campo de caixa de texto em um formulário PDF definindo uma fonte personalizada, tamanho e cor, e então salva o documento modificado usando Aspose.PDF for Python via .NET.

O trecho de código a seguir mostra como definir a fonte padrão para campos de formulário PDF.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        textBoxField.default_appearance = ap.annotations.DefaultAppearance(font, 10, ap.Color.black.to_rgb())

    document.save(path_outfile)
```

## Remover campos em formulário existente

Este código remove um campo de formulário específico (pelo seu nome) de um documento PDF e salva o arquivo atualizado usando Aspose.PDF for Python via .NET.

1. Carregue o documento PDF.
1. Exclua um campo de formulário pelo nome.
1. Salve o PDF atualizado.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    # Delete a particular field by name
    document.form.delete("First Name")
    # Save PDF document
    document.save(path_outfile)
```

