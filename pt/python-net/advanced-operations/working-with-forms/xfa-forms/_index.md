---
title: Trabalhando com Formulários XFA
linktitle: Formulários XFA
type: docs
weight: 20
url: /pt/python-net/xfa-forms/
description: Aspose.PDF para Python via API .NET permite que você trabalhe com campos XFA e XFA Acroform em um documento PDF.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Converter XFA para Acroform

{{% alert color="primary" %}}

Experimentar online
Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

O próximo trecho de código demonstra como converter um formulário XFA dinâmico (XML Forms Architecture) para um AcroForm padrão.

**Etapas principais incluem:**

1. Carregando o documento PDF de entrada.
1. Alterando o tipo de formulário para PADRÃO.
1. Salvando o PDF convertido em um novo arquivo.

Essa conversão permite melhor compatibilidade e manuseio consistente de formulários em diferentes leitores e aplicativos de PDF.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save PDF document
        document.save(path_outfile)
```

## Uso de IgnoreNeedsRendering

Este exemplo demonstra como converter um formulário XFA dinâmico para um AcroForm padrão usando Aspose.PDF para Python. O código verifica se o PDF de entrada contém um formulário XFA e substitui a renderização se necessário. Em seguida, define o tipo de formulário como PADRÃO e salva o PDF atualizado.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```

