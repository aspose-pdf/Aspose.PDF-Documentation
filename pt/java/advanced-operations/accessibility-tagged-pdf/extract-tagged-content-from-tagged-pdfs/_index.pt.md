---
title: Extrair Conteúdo Marcado de PDF 
linktitle: Extrair Conteúdo Marcado
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Este artigo explica como extrair conteúdo marcado de um documento PDF usando Aspose.PDF para Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtendo Conteúdo de PDF Marcado

Para obter o conteúdo de um Documento PDF com Texto Marcado, Aspose.PDF oferece o método [getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--) da Classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). O trecho de código a seguir mostra como obter o conteúdo de um documento PDF com Texto Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String path = "pathTodir";

// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

//
// Trabalhar com conteúdo de Pdf Marcado
//

// Definir Título e Idioma para o Documento
taggedContent.setTitle("Documento Pdf Marcado Simples");
taggedContent.setLanguage("en-US");

// Salvar Documento Pdf Marcado
document.save(path + "TaggedPDFContent.pdf");
```


## Obtendo Estrutura Raiz

Para obter a estrutura raiz de um Documento PDF Marcado, o Aspose.PDF oferece os métodos [getStructTreeRootElement]()(https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) e **getStructureElement()** da Interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). O trecho de código a seguir mostra como obter a estrutura raiz de um Documento PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String path = "pathTodir";
// Criar Documento PDF
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Definir Título e Idioma para o Documento
taggedContent.setTitle("Documento PDF Marcado");
taggedContent.setLanguage("en-US");

// As propriedades StructTreeRootElement e RootElement são usadas para acessar o
// objeto StructTreeRoot do documento pdf e o elemento de estrutura raiz (elemento de estrutura do Documento).
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```


## Acessando Elementos Filhos

Para acessar elementos filhos de um Documento PDF Marcado, Aspose.PDF oferece a Classe **ElementList**. O trecho de código a seguir mostra como acessar elementos filhos de um Documento PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-Java
String path = "pathTodir";
// Abrir Documento Pdf
Document document = new Document( path +"StructureElements.pdf");

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Acessar o(s) elemento(s) raiz
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // Obter propriedades
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// Acessar elementos filhos do primeiro elemento no elemento raiz
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // Definir propriedades
        structureElement.setTitle("title");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("actual text");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// Salvar Documento Pdf Marcado
document.save( path +"AccessChildrenElements.pdf");
```