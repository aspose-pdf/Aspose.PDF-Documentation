---
title: Trabalhando com Metadados de Arquivo PDF em Python
linktitle: Metadados de Arquivo PDF
type: docs
weight: 200
url: /pt/python-net/pdf-file-metadata/
description: Explore como extrair e gerenciar metadados de PDF, como autor e título, em Python usando Aspose.PDF.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obter e Definir Metadados em PDF usando Python
Abstract: O artigo fornece um guia abrangente sobre manipulação de metadados de PDF usando Aspose.PDF para Python via .NET. Ele descreve métodos para extrair e definir propriedades de metadados, incluindo autor, data de criação, palavras‑chave e mais, que são cruciais para catalogação de documentos, otimização de busca ou validação. Os trechos de código demonstram como recuperar metadados de um PDF usando a classe `Document` e a propriedade `info`, definir novos metadados usando o objeto `DocumentInfo` e salvar as alterações. Além disso, mostra como atualizar programaticamente os metadados XMP, o que aprimora a organização e a pesquisabilidade do documento. O artigo também explica como inserir metadados com um prefixo personalizado registrando um URI de namespace. Essas funcionalidades são essenciais para desenvolvedores que desejam gerenciar informações de documentos PDF de forma eficaz dentro de aplicativos.
---

## Obter Informações do Arquivo PDF

Este trecho de código demonstra como extrair metadados de um documento PDF usando Aspose.PDF para Python via .NET. Ao acessar a propriedade info do objeto Document, ele recupera informações chave como autor, data de criação, palavras‑chave, data de modificação, assunto e título. Essa funcionalidade é essencial para aplicações que requerem catalogação de documentos, otimização de busca ou validação das propriedades do documento.

1. Abra o arquivo PDF usando a classe Document
1. Recupere os metadados do documento através da propriedade info
1. Exiba as informações de metadados. Imprima os campos de metadados desejados

```python

    import aspose.pdf as ap

    def get_pdf_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "GetFileInfo.pdf")

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

## Definir Informações do Arquivo PDF

Aspose.PDF para Python via .NET permite definir informações específicas de arquivo para um PDF, informações como autor, data de criação, assunto e título. Para definir estas informações:

1. Abra o arquivo PDF usando a classe Document.
1. Crie um objeto [DocumentInfo]() e defina as propriedades de metadados desejadas.
1. Salve as alterações em um novo arquivo PDF usando o método save.

O trecho de código a seguir mostra como definir informações de arquivo PDF.

```python

    import aspose.pdf as ap
    import datetime

    def set_file_information():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_workingdocuments()

        # Open PDF document
        document = ap.Document(data_dir + "SetFileInfo.pdf")

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
        document.save(data_dir + "SetFileInfo_out.pdf")
```

## Definir Metadados XMP em um Arquivo PDF

Este trecho de código demonstra como definir ou atualizar programaticamente metadados XMP em um documento PDF usando Aspose.PDF para Python via .NET. Ao modificar propriedades como xmp:CreateDate, xmp:Nickname e campos personalizados, você pode incorporar metadados padronizados em seus arquivos PDF. Esta abordagem é particularmente útil para melhorar a organização do documento, facilitar a pesquisabilidade e incorporar informações essenciais diretamente no arquivo.

Aspose.PDF permite definir metadados em um arquivo PDF. Para definir metadados:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Modifique os metadados XMP atribuindo valores a chaves específicas.
1. Salve o Documento PDF Atualizado.

O trecho de código a seguir mostra como definir metadados em um arquivo PDF.

```python

    import aspose.pdf as ap
    import datetime

    def set_xmp_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Set XMP metadata properties
        document.metadata["xmp:CreateDate"] = datetime.datetime.now().isoformat()
        document.metadata["xmp:Nickname"] = "Nickname"
        document.metadata["xmp:CustomProperty"] = "Custom Value"

        # Save the updated PDF document
        document.save(data_dir + "SetXMPMetadata_out.pdf")
```

## Inserir Metadados com Prefixo

Alguns desenvolvedores precisam criar um novo namespace de metadados com um prefixo. O trecho de código a seguir mostra como inserir metadados com prefixo.

```python

    import aspose.pdf as ap
    import datetime

    def set_prefix_metadata():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf()

        # Open PDF document
        document = ap.Document(data_dir + "SetXMPMetadata.pdf")

        # Register a namespace URI for the 'xmp' prefix
        document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

        # Set the metadata property using the registered prefix
        document.metadata["xmp:ModifyDate"] = datetime.datetime.now().isoformat()  # ISO 8601 format

        # Save the updated PDF document
        document.save(data_dir + "SetPrefixMetadata_out.pdf")
```
