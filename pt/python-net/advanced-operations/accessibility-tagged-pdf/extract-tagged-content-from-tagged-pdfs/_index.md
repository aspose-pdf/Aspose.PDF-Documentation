---
title: Extrair Conteúdo Marcado de PDFs em Python
linktitle: Extrair Conteúdo Marcado
type: docs
weight: 20
url: /pt/python-net/extract-tagged-content-from-tagged-pdfs/
description: Saiba como extrair conteúdo marcado de PDF em Python com Aspose.PDF for Python via .NET, incluindo acesso ao conteúdo marcado, à estrutura raiz e aos elementos de estrutura filho.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Neste artigo, você aprenderá como extrair conteúdo marcado de documentos PDF usando Python.

Use esses exemplos quando precisar inspecionar um Tagged PDF, ler a árvore de estrutura lógica ou validar se os Structure Elements foram criados corretamente para fluxos de trabalho de acessibilidade.

## Obtendo Conteúdo de Tagged PDF

Para obter o conteúdo de um PDF Document com Tagged Text, Aspose.PDF oferece [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) propriedade de [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe.

Crie um PDF avançado, totalmente marcado, com um índice estruturado e hierárquico Table of Contents (TOC):

1. Crie um novo objeto Document.
1. Acesse a propriedade tagged_content.
1. Defina o título do documento usando 'set_title()'.
1. Defina o idioma do documento usando 'set_language()'.
1. Salve o documento.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

# region Extract Tagged Content from PDF
def get_tagged_content(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Obtendo a Estrutura Raiz

Os PDFs Tagged contêm uma árvore de estrutura lógica que define a estrutura semântica do documento. O StructTreeRoot representa a raiz dessa árvore lógica, enquanto o RootElement fornece uma interface para interagir com o elemento de estrutura de nível superior do documento.

O trecho de código a seguir mostra como obter a estrutura raiz de um Tagged PDF Document:

1. Crie um novo documento PDF marcado.
1. Acesse o conteúdo marcado e defina os metadados.
1. Acesse StructTreeRoot e RootElement.
1. Salve o PDF marcado.

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def get_root_structure(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Properties StructTreeRootElement and RootElement are used for access to
        # StructTreeRoot object of pdf document and to root structure element (Document structure element).
        struct_tree_root_element = tagged_content.struct_tree_root_element
        root_element = tagged_content.root_element

        print(f"StructTreeRootElement: {struct_tree_root_element}")
        print(f"RootElement: {root_element}")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Acessando Elementos Filhos

Os PDFs Marcados contêm uma árvore de estrutura lógica que define a hierarquia semântica do documento (títulos, parágrafos, formulários, listas, etc.). Acessar e modificar esses elementos de estrutura permite que você:

- Inspecionar metadados como título, idioma, actual_text e propriedades relacionadas à acessibilidade
- Atualizar propriedades para melhorar a acessibilidade ou a localização
- Ajustar programaticamente a estrutura lógica do documento para conformidade PDF/UA

 O trecho de código a seguir mostra como acessar os elementos filhos de um Documento Tagged PDF:

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def access_child_elements(infile, outfile):

    # Open PDF Document
    with ap.Document(infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logicalstructure.StructureElement, element)
                # Get properties
                print(
                    "StructureElement properties - "
                    f"title: {structure_element.title}, "
                    f"language: {structure_element.language}, "
                    f"actual_text: {structure_element.actual_text}, "
                    f"expansion_text: {structure_element.expansion_text}, "
                    f"alternative_text: {structure_element.alternative_text}"
                )

        # Access to child elements of first element in root element
        element_list = tagged_content.root_element.child_elements[1].child_elements
        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = element

                # Set properties
                structure_element.title = "title"
                structure_element.language = "fr-FR"
                structure_element.actual_text = "actual text"
                structure_element.expansion_text = "exp"
                structure_element.alternative_text = "alt"

        # Save Tagged PDF Document
        document.save(outfile)
```

## Tópicos Relacionados ao PDF Marcado

- [Criar Tagged PDF](/pdf/pt/python-net/create-tagged-pdf/) para construir documentos marcados acessíveis antes de inspecionar sua estrutura.
- [Definindo Propriedades dos Structure Elements](/pdf/pt/python-net/setting-structure-elements-properties/) para atualizar propriedades semânticas após extrair elementos de estrutura.
- [Trabalhando com Tabela em PDFs Marcados](/pdf/pt/python-net/working-with-table-in-tagged-pdfs/) para fluxos de trabalho de acessibilidade de tabelas marcadas.