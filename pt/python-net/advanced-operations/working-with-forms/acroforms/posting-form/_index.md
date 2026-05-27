---
title: Publicando Formulários em PDF via Python
linktitle: Publicando Formulários
type: docs
weight: 75
url: /pt/python-net/posting-form/
description: Adicione botões de envio e ações de submissão ao PDF AcroForms usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Adicionar Botões de Envio e Ações de Submissão de Formulário a um PDF Usando Python
Abstract: Este artigo mostra duas abordagens para adicionar funcionalidade de envio a formulários PDF usando Aspose.PDF for Python via .NET. Você pode adicionar um botão de envio pronto por meio do FormEditor ou criar um campo de botão personalizado com SubmitFormAction para controle avançado. Esses padrões ajudam a integrar formulários PDF com endpoints de processamento de formulários no lado do servidor.
---

## Adicionar Botão de Envio com FormEditor

O trecho de código a seguir demonstra como adicionar um botão de envio a um formulário PDF usando a classe FormEditor no Aspose.PDF for Python via .NET. O botão está configurado para enviar os dados do formulário para um URL especificado ao ser clicado.

1. Criar um `FormEditor` objeto.
1. Adicionar um botão de envio à página de destino.
1. Definir o URL de envio e as coordenadas do botão.
1. Salvar o PDF atualizado.

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## Adicionar Ação de Envio Personalizada

O trecho de código a seguir explica como criar um botão de envio personalizado em um formulário PDF usando Aspose.PDF for Python via .NET. O botão está configurado para enviar os dados do formulário para uma URL especificada ao ser clicado.

1. Abra o PDF com ap.Document().
1. Crie uma ação de envio.
1. Defina a URL de destino e as flags de envio.
1. Crie um campo de botão e vincule sua ação de clique.
1. Adicione o botão ao formulário.
1. Salvar o PDF atualizado.

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## Tópicos Relacionados

- [Criar AcroForm](/pdf/pt/python-net/create-form/)
- [Preencher AcroForm](/pdf/pt/python-net/fill-form/)
- [Modificando AcroForm](/pdf/pt/python-net/modifying-form/)
- [Importar e Exportar Dados de Formulário](/pdf/pt/python-net/import-export-form-data/)