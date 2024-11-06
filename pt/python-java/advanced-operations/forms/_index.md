---
title: Trabalhando com Formulários usando Python
linktitle: Formulários em Documento PDF
type: docs
weight: 60
url: pt/python-java/forms/
lastmod: "2023-05-19"
description: Esta seção contém artigos referentes ao trabalho com formulários em documentos PDF usando API Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Formulários são arquivos com áreas para os usuários selecionarem ou preencherem informações com o propósito de coletar e armazenar informações.

AcroForms são arquivos PDF que contêm campos de formulário. Dados podem ser inseridos nesses campos (manualmente ou através de um processo automatizado) pelos usuários finais ou pelo autor do formulário. Internamente, AcroForms são anotações ou campos aplicados a um documento PDF.

Nesta seção, é descrita uma abordagem rápida e simples para completar programaticamente um documento PDF através do uso do Aspose.PDF. A seção também discute como se pode usar o Aspose.PDF para Java para descobrir e mapear os campos disponíveis dentro de um PDF existente com AcroForms.

**Nossa biblioteca Aspose.PDF para Python via Java** permite que você trabalhe com sucesso, rapidez e facilidade com formulários em documentos PDF.

- **AcroForms** - criar formulário, preencher campo de formulário, extrair dados de formulário, modificar campos em seu PDF com a biblioteca Java.
- **Formulários XFA** - preencher campos XFA, converter XFA, obter propriedades de campos XFA.

## As seguintes funções estão disponíveis:

- exportar/importar fdf
- exportar/importar xfdf
- exportar/importar xml
- exportar/definir XfaData
- preencher campos
- achatar campos
- determinar valores válidos de botão de rádio
- obter nomes de campo, bandeiras, tipos, valores
- renomear campos

```python

from asposepdf import Api, Forms


# iniciar licença
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# exemplo de preenchimento de campo

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```