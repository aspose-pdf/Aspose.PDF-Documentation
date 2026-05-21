---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
weight: 45
url: /pt/python-net/modifying-form/
description: Modifique os campos AcroForm em documentos PDF usando Aspose.PDF for Python via .NET, incluindo limpar texto, definir limites, estilizar campos e remover campos.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerenciando e Personalizando Campos de Formulário PDF
Abstract: Este artigo apresenta exemplos práticos para modificar campos AcroForm usando Aspose.PDF for Python via .NET. Ele aborda a limpeza de texto de conteúdo de formulário Typewriter, a definição e leitura de limites de caracteres de campos de texto, a aplicação de aparência de fonte personalizada e a remoção de campos por nome. Esses fluxos de trabalho dão suporte a tarefas comuns de manutenção de formulários em pipelines automatizados de processamento de PDF.
---

## Limpar Texto no Form

Este exemplo demonstra como limpar texto de campos de formulário Typewriter em um PDF usando Aspose.PDF for Python via .NET. Ele varre a primeira página do PDF, identifica os formulários Typewriter, remove seu conteúdo e salva o documento atualizado. Essa abordagem é útil para redefinir ou sanitizar campos de formulário antes de redistribuir um PDF.

1. Carregue o documento PDF de entrada.
1. Acesse os formulários na primeira página.
1. Itere sobre cada formulário e verifique se ele é um `Typewriter` formulário.
1. Use TextFragmentAbsorber para encontrar fragmentos de texto no formulário.
1. Limpe o texto de cada fragmento.
1. Salve o PDF modificado no arquivo de saída.

```python
import aspose.pdf as ap


def clear_text_in_form(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)
```

## Definir Limite de Campo

Usar `set_field_limit(field, limit)` de `FormEditor` para definir o número máximo de caracteres permitidos em um campo de texto.

1. Criar um `FormEditor` objeto.
1. Vincule o PDF de entrada.
1. Defina o limite de campo para um campo alvo.
1. Salvar o PDF atualizado.

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## Obter limite do campo

Você também pode ler o limite de caracteres de um campo de texto.

1. Carregue o documento PDF.
1. Acesse o campo de formulário de destino.
1. Certifique-se de que o campo seja um `TextBoxField`.
1. Ler e imprimir `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## Definir Fonte Personalizada para o Campo de Formulário

Este exemplo define uma aparência padrão personalizada para um campo de caixa de texto, incluindo fonte, tamanho e cor.

1. Carregue o documento PDF.
1. Acesse o campo de destino e verifique seu tipo.
1. Encontre a fonte em `FontRepository`.
1. Aplicar um novo `DefaultAppearance`.
1. Salvar o PDF atualizado.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        text_box_field.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## Remover Campos em um Formulário Existente

Este código remove um campo de formulário específico (pelo nome) de um documento PDF e salva o arquivo atualizado usando Aspose.PDF for Python via .NET.

1. Carregue o documento PDF.
1. Excluir um campo de formulário pelo nome.
1. Salvar o PDF atualizado.

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## Tópicos Relacionados

- [Criar AcroForm](/pdf/pt/python-net/create-form/)
- [Preencher AcroForm](/pdf/pt/python-net/fill-form/)
- [Extrair AcroForm](/pdf/pt/python-net/extract-form/)
- [Importar e Exportar Dados de Formulário](/pdf/pt/python-net/import-export-form-data/)
