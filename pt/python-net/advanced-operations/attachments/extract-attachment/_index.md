---
title: Extrair anexos de PDF
linktitle: Extrair anexos
type: docs
weight: 50
url: /pt/python-net/extract-attachment/
description: Aprenda como trabalhar com anexos de PDF usando Python e Aspose.PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Guia completo para gerenciar anexos de PDF em Python: adicionar, extrair e processar arquivos incorporados"
Abstract: Os anexos de PDF são amplamente usados para armazenar documentos de apoio, relatórios, imagens e outros recursos diretamente dentro de um arquivo PDF. Este artigo fornece uma visão completa sobre o manuseio de anexos de PDF com Python usando Aspose.PDF. Ele explica como incorporar arquivos externos em PDFs existentes, extrair anexos específicos ou todos, inspecionar metadados como tamanho de arquivo e marcadores de tempo, e recuperar arquivos armazenados como anotações FileAttachment. Cada exemplo demonstra técnicas práticas para automatizar fluxos de trabalho de anexos, melhorar a portabilidade de documentos e simplificar o gerenciamento de arquivos. Seja construindo sistemas de documentos corporativos ou scripts de automação personalizados, os desenvolvedores podem usar esses métodos para gerenciar eficientemente arquivos incorporados dentro de documentos PDF.
---

## Extrair Anexo Específico de PDF

Extrair um único arquivo incorporado de um documento PDF usando Python e Aspose.PDF. Ele procura um anexo pelo nome, recupera seu conteúdo e o salva como um arquivo separado. Isso é útil para acessar documentos incorporados, como relatórios, logs ou arquivos de suporte armazenados dentro do PDF.

1. Definir Função 'extract_single_attachment()'.
1. Abrir documento PDF.
1. Pesquisar anexo.
1. Extrair conteúdo do anexo.

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## Exibir Metadados do Anexo de Arquivo

Esta função auxiliar imprime informações de metadados de um objeto de especificação de arquivo. Ela é tipicamente usada ao trabalhar com anexos de arquivos incorporados em PDFs usando Aspose.PDF, permitindo que os desenvolvedores inspecionem detalhes como checksum, data de criação, data de modificação e tamanho do arquivo.

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## Extrair e Inspecionar Todos os Anexos PDF

Este trecho de código demonstra como extrair todos os arquivos incorporados de um documento PDF usando Python e Aspose.PDF. Ele não apenas salva cada anexo em uma pasta especificada, mas também imprime metadados detalhados, como nome do arquivo, descrição, tipo MIME, soma de verificação e carimbos de data/hora. Isso é útil para auditoria, exportação ou processamento de conteúdo incorporado em arquivos PDF.

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## Extrair arquivos de anotações de anexos PDF

Extrair um arquivo incorporado de uma anotação FileAttachment em um PDF usando Python e Aspose.PDF. Ele procura na primeira página a primeira anotação de anexo, recupera o arquivo incorporado e o salva em um diretório de saída selecionado. Isso é útil quando os PDFs contêm ícones de anexos de arquivo clicáveis em vez de coleções padrão de arquivos incorporados.

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```