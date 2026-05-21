---
title: Trabalhar com metadados de arquivo PDF em Python
linktitle: Metadados de Arquivo PDF
type: docs
weight: 200
url: /pt/python-net/pdf-file-metadata/
description: Saiba como extrair, atualizar e gerenciar metadados de arquivo PDF e propriedades XMP em Python usando Aspose.PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtenha e defina informações do documento PDF e metadados XMP em Python
Abstract: Este artigo explica como trabalhar com metadados PDF no Aspose.PDF for Python via .NET. Aprenda como ler informações do documento, como autor, título e palavras‑chave, atualizar propriedades do arquivo, definir campos de metadados XMP e registrar prefixos de metadados personalizados para arquivos PDF em Python.
---

Use este guia quando precisar inspecionar as propriedades do documento, atualizar as informações do arquivo PDF para busca ou catalogação, ou gerenciar metadados XMP programaticamente em Python.

## Obter informações do arquivo PDF

Este trecho de código demonstra como extrair metadados de um documento PDF usando Aspose.PDF for Python via .NET. Ao acessar a propriedade info do objeto Document, ele recupera informações essenciais como autor, data de criação, palavras‑chave, data de modificação, assunto e título. Essa funcionalidade é essencial para aplicações que exigem catalogação de documentos, otimização de busca ou validação das propriedades do documento.

1. Abra o arquivo PDF usando a classe Document
1. Recupere os metadados do documento através da propriedade info
1. Exiba as informações de metadados. Imprima os campos de metadados desejados

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## Definir informações do arquivo PDF

Aspose.PDF for Python via .NET permite definir informações específicas de arquivo para um PDF, informações como autor, data de criação, assunto e título. Para definir essas informações:

1. Abra o arquivo PDF usando a classe Document.
1. Criar um [DocumentInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) objeto e definir as propriedades de metadados desejadas.
1. Salvar as alterações em um novo arquivo PDF usando o método save.

O trecho de código a seguir mostra como definir informações de arquivo PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## Definir metadados XMP em um arquivo PDF

Este trecho de código demonstra como definir ou atualizar programaticamente metadados XMP em um documento PDF usando Aspose.PDF for Python via .NET. Ao modificar propriedades como xmp:CreateDate, xmp:Nickname e campos definidos pelo usuário, você pode incorporar metadados padronizados em seus arquivos PDF. Essa abordagem é particularmente útil para melhorar a organização de documentos, facilitar a pesquisa e incorporar informações essenciais diretamente no arquivo.

Aspose.PDF permite que você defina metadados em um arquivo PDF. Para definir metadados:

1. Abra o arquivo PDF usando o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.
1. Modifique os metadados XMP atribuindo valores a chaves específicas.
1. Salve o Documento PDF Atualizado.

O trecho de código a seguir mostra como definir metadados em um arquivo PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## Inserir Metadados com Prefixo

Alguns desenvolvedores precisam criar um novo espaço de nomes de metadados com um prefixo. O trecho de código a seguir mostra como inserir metadados com prefixo.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## Tópicos Relacionados

- [Operações avançadas de PDF em Python](/pdf/pt/python-net/advanced-operations/)
- [Trabalhe com documentos PDF em Python](/pdf/pt/python-net/working-with-documents/)
- [Trabalhe com anexos PDF em Python](/pdf/pt/python-net/attachments/)
- [Compare documentos PDF em Python](/pdf/pt/python-net/compare-pdf-documents/)
