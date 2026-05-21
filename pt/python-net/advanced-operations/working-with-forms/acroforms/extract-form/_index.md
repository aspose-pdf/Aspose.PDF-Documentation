---
title: Extrair AcroForm - Extrair Dados de Form de PDF em Python
linktitle: Extrair AcroForm
type: docs
weight: 30
url: /pt/python-net/extract-form/
description: Extrair valores dos campos AcroForm em documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como obter Dados de Form de PDF usando Python
Abstract: Este artigo mostra como extrair dados dos campos AcroForm em documentos PDF usando Aspose.PDF for Python via .NET. O exemplo itera pelos nomes dos campos Form, lê os valores usando a fachada Form, e retorna um dicionário para processamento posterior. Este fluxo de trabalho é útil para relatórios, validação e integração com sistemas externos.
---

## Extrair Dados de Form

### Obter valores de todos os campos em um documento PDF

Para ler valores de todos os campos em um documento PDF, itere pelos nomes dos campos de formulário e recupere cada valor do [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) facade.

Use os passos a seguir:

1. Vincular o PDF de entrada a um `Form` objeto.
1. Iterar através de `field_names`.
1. Leia cada valor com `get_field()`.
1. Armazene valores em um dicionário.
1. Retornar ou processar os valores extraídos.

O trecho de código Python a seguir demonstra essa abordagem.

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## Tópicos Relacionados

- [Criar AcroForm](/pdf/pt/python-net/create-form/)
- [Preencher AcroForm](/pdf/pt/python-net/fill-form/)
- [Importar e Exportar Dados do Form](/pdf/pt/python-net/import-export-form-data/)
- [Modificando AcroForm](/pdf/pt/python-net/modifying-form/)