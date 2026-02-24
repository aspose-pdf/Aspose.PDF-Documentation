---
title: Criar Links em arquivo PDF com Python
linktitle: Criar Links
type: docs
weight: 10
url: /pt/python-net/create-links/
description: Esta seção explica como criar links em seu documento PDF com Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como criar Links em PDF
Abstract: O guia Aspose.PDF for Python via .NET sobre criação de links fornece aos desenvolvedores instruções práticas para adicionar hiperlinks interativos a documentos PDF usando Python. Ele abrange como criar vários tipos de links, incluindo aqueles que iniciam aplicativos externos, navegam para páginas específicas dentro do mesmo documento ou abrem outros arquivos PDF. A documentação explica como usar objetos LinkAnnotation, definir áreas clicáveis com Rectangle e atribuir ações como LaunchAction ou GoToRemoteAction. Com exemplos de código claros e orientação passo a passo, este recurso ajuda os desenvolvedores a aprimorar a navegação e interatividade de PDFs em suas aplicações Python.
---

## Links em Documentos PDF

De acordo com a especificação PDF 1.7 (ISO 32000-1:2008), uma **anotação de Link** pode acionar vários tipos de ações que definem o que acontece quando a anotação é ativada. Aqui estão as principais ações suportadas:

1. **GoTo** – Navega para um destino dentro do mesmo documento.
1. **GoToR** – Salta para um destino em outro arquivo PDF (go-to remoto).
1. **URI** – Abre um identificador de recurso uniforme, tipicamente um link web.
1. **Launch** – Inicia um aplicativo ou abre um arquivo (dependente da plataforma e frequentemente restrito por segurança).
1. **Named** – Executa uma ação pré-definida, como ir para a próxima página ou imprimir o documento.
1. **JavaScript** – Executa código JavaScript incorporado (usado com cautela devido a preocupações de segurança).
1. **SubmitForm** – Envia dados do formulário para uma URL especificada.
1. **ResetForm** – Redefine os campos do formulário para seus valores padrão.
1. **ImportData** – Importa dados para o documento a partir de um arquivo externo.

Adicionando um link para um aplicativo em um documento, é possível vincular a aplicativos a partir de um documento. Isso é útil quando você deseja que os leitores realizem uma ação específica em um ponto determinado de um tutorial, por exemplo, ou para criar um documento rico em recursos.

Para criar um link de aplicativo com 'LaunchAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## Criar Link de Documento PDF em um Arquivo PDF

### Usando GoToRemoteAction

Este trecho de código demonstra como adicionar uma anotação de link a uma página específica de um documento PDF usando uma biblioteca PDF para Python.

1. Abra o documento PDF
1. Selecione a segunda página do documento (índice 1)
1. Crie uma anotação de link:
1. Posicionada nas coordenadas (10, 580, 120, 600)
1. Colorida de verde
1. Vincula ao 'sample.pdf' em sua primeira página
1. Adicione a anotação de link à página
1. Salve o documento modificado no caminho de arquivo de saída

Para criar um link de documento PDF usando 'GoToRemoteAction':

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### Usando GoToAction

Este código demonstra como adicionar uma anotação de link a uma página específica de um documento PDF usando Aspose.PDF for Python. O link aparece como um retângulo verde com borda tracejada e permite que o usuário navegue para outra página dentro do mesmo PDF. Para criar um link de documento PDF usando 'GoToAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### Aplicando GoToURIAction

O próximo exemplo demonstra como adicionar uma anotação de link a um documento PDF usando Aspose.PDF for Python. O link aparece como uma área clicável verde na primeira página e, ao ser clicado, abre a documentação do Aspose.PDF for Python em um navegador web via GoToURIAction.

Esta funcionalidade é útil para incorporar referências externas úteis, documentação ou links de suporte diretamente em seus PDFs.

1. Carregue o Documento PDF. Abra o arquivo PDF existente usando ap.Document.
1. Acesse a Primeira Página. Use document.pages[1] para acessar a primeira página (Aspose usa indexação baseada em 1).
1. Crie uma Anotação de Link. Crie um objeto LinkAnnotation e especifique a área retangular clicável usando ap.Rectangle.
1. Defina a Aparência da Anotação. Defina a cor da anotação para verde usando link.color = ap.Color.green.
1. Atribua uma Ação URI. Use GoToURIAction para vincular a anotação a uma URL externa.
1. Adicione a Anotação à Página. Anexe a anotação de link configurada à coleção de anotações da primeira página.
1. Salve o Documento Modificado. Salve o documento PDF atualizado no caminho de saída especificado.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```

