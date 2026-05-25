---
title: Criar links PDF em Python
linktitle: Criar links
type: docs
weight: 10
url: /pt/python-net/create-links/
description: Aprenda como criar links PDF internos, externos e remotos em Python.
lastmod: "2026-05-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como criar links em PDF
Abstract: O guia Aspose.PDF for Python via .NET sobre criação de links fornece aos desenvolvedores instruções práticas para adicionar hiperlinks interativos a documentos PDF usando Python. Ele cobre como criar vários tipos de links, incluindo aqueles que iniciam aplicativos externos, navegam para páginas específicas dentro do mesmo documento ou abrem outros arquivos PDF. A documentação explica como usar objetos LinkAnnotation, definir áreas clicáveis com Rectangle e atribuir ações como LaunchAction ou GoToRemoteAction. Com exemplos de código claros e orientações passo a passo, este recurso ajuda os desenvolvedores a melhorar a navegação e a interatividade de PDFs em suas aplicações Python.
---

## Links em Documentos PDF

De acordo com a especificação PDF 1.7 (ISO 32000-1:2008), uma **Link annotation** pode acionar vários tipos de ações que definem o que acontece quando a anotação é ativada. Aqui estão as principais ações suportadas:

1. **GoTo** – Navega para um destino dentro do mesmo documento.
1. **GoToR** – Salta para um destino em outro arquivo PDF (go-to remoto).
1. **URI** – Abre um identificador uniforme de recurso, normalmente um link da web.
1. **Launch** – Lança um aplicativo ou abre um arquivo (dependente da plataforma e frequentemente restrito por questões de segurança).
1. **Named** – Executa uma ação predefinida, como ir para a próxima página ou imprimir o documento.
1. **JavaScript** – Executa código JavaScript incorporado (usado com cautela devido a preocupações de segurança).
1. **SubmitForm** – Envia os dados do formulário para um URL especificado.
1. **ResetForm** – Reseta os campos do formulário para seus valores padrão.
1. **ImportData** – Importa dados para o documento a partir de um arquivo externo.

Ao adicionar um link para um aplicativo em um documento, é possível vincular aplicativos a partir de um documento. Isso é útil quando você deseja que os leitores realizem uma certa ação em um ponto específico de um tutorial, por exemplo, ou para criar um documento rico em recursos.

Para criar um link de aplicativo com ‘LaunchAction’:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## Criar link de Document PDF em um arquivo PDF

### Usando GoToRemoteAction

Este trecho de código demonstra como adicionar uma anotação de link a uma página específica de um documento PDF usando uma biblioteca PDF para Python.

1. Abrir o documento PDF
1. Selecione a segunda página do documento (índice 1)
1. Criar uma anotação de link:
1. Posicionado nas coordenadas (10, 580, 120, 600)
1. Colorido em verde
1. Links para 'sample.pdf' na sua primeira página
1. Adicionar a anotação de link à página
1. Salvar o documento modificado no caminho do arquivo de saída

Para criar um link de documento PDF usando 'GoToRemoteAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### Usando GoToAction

Este código demonstra como adicionar uma anotação de link a uma página específica de um documento PDF usando Aspose.PDF for Python. O link aparece como um retângulo verde com borda tracejada e permite ao usuário navegar para outra página dentro do mesmo PDF. Para criar um link de documento PDF usando 'GoToAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### Aplicando GoToURIAction

O próximo exemplo demonstra como adicionar uma anotação de link a um documento PDF usando Aspose.PDF for Python. O link aparece como uma área verde clicável na primeira página e, quando clicado, abre a documentação do Aspose.PDF for Python em um navegador da web via uma GoToURIAction.

Essa funcionalidade é útil para incorporar referências externas úteis, documentação ou links de suporte diretamente em seus PDFs.

1. Carregue o Documento PDF. Abra o arquivo PDF existente usando ap.Document.
1. Acesse a Primeira Página. Use document.pages[1] para acessar a primeira página (Aspose usa indexação baseada em 1).
1. Crie uma Anotação de Link. Crie um objeto LinkAnnotation e especifique a área retangular clicável usando ap.Rectangle.
1. Defina a aparência da anotação. Defina a cor da anotação para verde usando link.color = ap.Color.green.
1. Atribua uma ação URI. Use GoToURIAction para vincular a anotação a um URL externo.
1. Adicione a anotação à página. Anexe a anotação de link configurada à coleção de anotações da primeira página.
1. Salve o documento modificado. Salve o documento PDF atualizado no caminho de saída especificado.

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## Tópicos de Links Relacionados

- [Trabalhar com links PDF em Python](/pdf/pt/python-net/links/)
- [Extrair links de PDF em Python](/pdf/pt/python-net/extract-links/)
- [Atualizar links em PDF usando Python](/pdf/pt/python-net/update-links/)