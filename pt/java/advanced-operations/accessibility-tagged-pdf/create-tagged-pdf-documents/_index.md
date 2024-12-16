---
title: Criar PDF Marcado
linktitle: Criar PDF Marcado
type: docs
weight: 10
lastmod: "2021-06-05"
url: /pt/java/create-tagged-pdf-documents/
description: Este artigo explica como criar elementos de estrutura para documentos PDF marcados programaticamente usando Aspose.PDF para Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Criando Elementos de Estrutura

Para criar elementos de estrutura em um Documento PDF Marcado, Aspose.PDF oferece métodos para criar elementos de estrutura usando a Interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). O trecho de código a seguir mostra como criar elementos de estrutura de um PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String path = "pathTodir";

// Criar Documento Pdf
Document document = new Document();

// Obter conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Definir título e idioma para o documento
taggedContent.setTitle("Documento Pdf Marcado");
taggedContent.setLanguage("en-US");

// Criar Elementos de Agrupamento
PartElement partElement = taggedContent.createPartElement();
ArtElement artElement = taggedContent.createArtElement();
SectElement sectElement = taggedContent.createSectElement();
DivElement divElement = taggedContent.createDivElement();
BlockQuoteElement blockQuoteElement = taggedContent.createBlockQuoteElement();
CaptionElement captionElement = taggedContent.createCaptionElement();
TOCElement tocElement = taggedContent.createTOCElement();
TOCIElement tociElement = taggedContent.createTOCIElement();
IndexElement indexElement = taggedContent.createIndexElement();
NonStructElement nonStructElement = taggedContent.createNonStructElement();
PrivateElement privateElement = taggedContent.createPrivateElement();

// Criar Elementos de Estrutura de Texto em Nível de Bloco
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// Criar Elementos de Estrutura de Texto em Nível Inline
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// Criar Elementos de Estrutura de Ilustração
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// Métodos estão em desenvolvimento
ListElement listElement = taggedContent.createListElement();
TableElement tableElement = taggedContent.createTableElement();
ReferenceElement referenceElement = taggedContent.createReferenceElement();
BibEntryElement bibEntryElement = taggedContent.createBibEntryElement();
CodeElement codeElement = taggedContent.createCodeElement();
LinkElement linkElement = taggedContent.createLinkElement();
AnnotElement annotElement = taggedContent.createAnnotElement();
RubyElement rubyElement = taggedContent.createRubyElement();
WarichuElement warichuElement = taggedContent.createWarichuElement();
FormElement formElement = taggedContent.createFormElement();

// Salvar Documento Pdf Marcado
document.save(path + "StructureElements.pdf");
```


## Criando Árvore de Elementos de Estrutura

Para criar uma árvore de elementos de estrutura em um Documento PDF Marcado, Aspose.PDF oferece métodos para criar uma árvore de elementos de estrutura usando a Interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). O trecho de código a seguir mostra como criar a árvore de elementos de estrutura de um Documento PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String path = "pathTodir";
// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Definir Título e Idioma para o Documento
taggedContent.setTitle("Documento Pdf Marcado");
taggedContent.setLanguage("en-US");

// Obter elemento de estrutura raiz (Documento)
StructureElement rootElement = taggedContent.getRootElement();

// Criar Estrutura Lógica
SectElement sect1 = taggedContent.createSectElement();
rootElement.appendChild(sect1);

SectElement sect2 = taggedContent.createSectElement();
rootElement.appendChild(sect2);

DivElement div11 = taggedContent.createDivElement();
sect1.appendChild(div11);

DivElement div12 = taggedContent.createDivElement();
sect1.appendChild(div12);

ArtElement art21 = taggedContent.createArtElement();
sect2.appendChild(art21);

ArtElement art22 = taggedContent.createArtElement();
sect2.appendChild(art22);

DivElement div211 = taggedContent.createDivElement();
art21.appendChild(div211);

DivElement div212 = taggedContent.createDivElement();
art21.appendChild(div212);

DivElement div221 = taggedContent.createDivElement();
art22.appendChild(div221);

DivElement div222 = taggedContent.createDivElement();
art22.appendChild(div222);

SectElement sect3 = taggedContent.createSectElement();
rootElement.appendChild(sect3);

DivElement div31 = taggedContent.createDivElement();
sect3.appendChild(div31);

// Salvar Documento Pdf Marcado
document.save(path + "StructureElementsTree.pdf");
```


## Estrutura de Estilização de Texto

Para estilizar a estrutura de texto em um Documento PDF Marcado, o Aspose.PDF oferece as propriedades **setFont()**, **setFontSize()**, **setFontStyle()** e **setForegroundColor()** da Classe [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState). O trecho de código a seguir mostra como estilizar a estrutura de texto em um Documento PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String path = "pathTodir";
// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Definir Título e Idioma para o Documento
taggedContent.setTitle("Documento Pdf Marcado");
taggedContent.setLanguage("en-US");

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// Em Desenvolvimento
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("Texto em itálico vermelho.");

// Salvar Documento Pdf Marcado
document.save(path + "StyleTextStructure.pdf");
```


## Ilustrando Elementos de Estrutura

Para ilustrar elementos de estrutura em um Documento PDF Marcado, Aspose.PDF oferece a Classe [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement). O trecho de código a seguir mostra como ilustrar elementos de estrutura em um Documento PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String path = "pathTodir";
// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Definir Título e Idioma para o Documento
taggedContent.setTitle("Documento Pdf Marcado");
taggedContent.setLanguage("en-US");

// Em Desenvolvimento
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("Figura Um");
figure1.setTitle("Imagem 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// Salvar Documento Pdf Marcado
document.save(path + "IllustrationStructureElements.pdf");
```


## **Criar PDF com Imagem Marcada**

Para criar um PDF com Imagem Marcada, o Aspose.PDF oferece o método [createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) da Interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). O trecho de código a seguir mostra a funcionalidade.

```java
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-Java
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("Aspose Logo");
figure1.setTitle("Imagem 1");
figure1.setTag("Fig");
// Adicionar imagem com resolução de 300 DPI (por padrão)
figure1.setImage("aspose-logo.jpg");
// Salvar Documento PDF
document.save("PDFwithTaggedImage.pdf");
```


## Criar PDF com Texto Marcado

Para criar um PDF com Texto Marcado, o Aspose.PDF oferece a Interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). O trecho de código a seguir mostra a funcionalidade.

```java
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Definir Título e Idioma para o Documento
taggedContent.setTitle("Documento Pdf Marcado");
taggedContent.setLanguage("en-US");

// Criar Elementos de Estrutura de Texto em Nível de Bloco
HeaderElement headerElement = taggedContent.createHeaderElement();
headerElement.setActualText("Cabeçalho 1");
ParagraphElement paragraphElement1 = taggedContent.createParagraphElement();
paragraphElement1.setActualText("teste 1");
ParagraphElement paragraphElement2 = taggedContent.createParagraphElement();
paragraphElement2.setActualText("teste 2");
ParagraphElement paragraphElement3 = taggedContent.createParagraphElement();
paragraphElement3.setActualText("teste 3");
ParagraphElement paragraphElement4 = taggedContent.createParagraphElement();
paragraphElement4.setActualText("teste 4");
ParagraphElement paragraphElement5 = taggedContent.createParagraphElement();
paragraphElement5.setActualText("teste 5");
ParagraphElement paragraphElement6 = taggedContent.createParagraphElement();
paragraphElement6.setActualText("teste 6");
ParagraphElement paragraphElement7 = taggedContent.createParagraphElement();
paragraphElement7.setActualText("teste 7");

// Salvar Documento PDF
document.save(dataDir + "PDFcomTextoMarcado.pdf");
```