---
title: Obter privilégios do Document
type: docs
weight: 10
url: /pt/python-net/get-document-privileges/
description: Saiba como verificar programaticamente os privilégios de um documento PDF usando Aspose.PDF for Python. Este tutorial demonstra como usar a classe PdfFileInfo para ler as configurações de segurança do documento, como impressão, cópia ou permissões de modificação.
lastmod: "2026-05-18"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar privilégios do PDF Document usando Aspose.PDF for Python
Abstract: Documentos PDF podem ter restrições de segurança que limitam ações como impressão, cópia, modificação ou preenchimento de formulários. Ao acessar esses privilégios programaticamente, os desenvolvedores podem determinar quais operações são permitidas em um PDF. Este guia mostra como usar a classe PdfFileInfo para recuperar os privilégios do documento PDF e exibí‑los em Python.
---

Os privilégios do PDF controlam o que os usuários podem e não podem fazer com um documento. As permissões comuns incluem:

- Impressão do documento
- Copiando conteúdo
- Modificando anotações ou conteúdos
- Preenchendo campos de formulário
- Usando leitores de tela
- Montando ou mesclando documentos

Com Aspose.PDF for Python, você pode inspecionar essas configurações programaticamente usando o [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) class. Esta é especialmente útil ao trabalhar com vários PDFs em fluxos de trabalho automatizados, verificando conformidade ou controlando o manuseio de documentos em aplicativos.

1. Carregue um arquivo PDF.
1. Recupere os privilégios do documento.
1. Exiba quais ações são permitidas para o documento.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
