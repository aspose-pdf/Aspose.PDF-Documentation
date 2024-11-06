---
title: Configurando Propriedades de Elementos de Estrutura em PDF Marcado
linktitle: Configurando Propriedades de Elementos de Estrutura
type: docs
weight: 30
url: pt/java/set-tagged-pdfs-element-properties/
description: Com o Aspose.PDF para Java, você pode configurar diferentes Propriedades de Elementos de Estrutura. Existem configurações de Elementos de Estrutura de Bloco de Texto, configuração de Elementos de Estrutura Inline, adicionando Elemento de Estrutura em Elementos e etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Configurando Propriedades de Elementos de Estrutura

Para configurar propriedades de elementos de estrutura em um Documento PDF Marcado, Aspose.PDF oferece os métodos **createSectElement()** e **createHeaderElement()** da Interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). O trecho de código a seguir mostra como configurar propriedades de elementos de estrutura de um Documento PDF Marcado:

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

// Criar Elementos de Estrutura
StructureElement rootElement = taggedContent.getRootElement();

SectElement sect = taggedContent.createSectElement();
rootElement.appendChild(sect);

HeaderElement h1 = taggedContent.createHeaderElement(1);
sect.appendChild(h1);
h1.setText("O Cabeçalho");

h1.setTitle("Título");
h1.setLanguage("en-US");
h1.setAlternativeText("Texto Alternativo");
h1.setExpansionText("Texto de Expansão");
h1.setActualText("Texto Atual");

// Salvar Documento Pdf Marcado
document.save(path + "StructureElementsProperties.pdf");
```


## Configurando Elementos de Estrutura de Texto

Para configurar elementos de estrutura de texto de um Documento PDF Marcado, a Aspose.PDF oferece a Classe [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). O trecho de código a seguir mostra como configurar elementos de estrutura de texto de um Documento PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor, acesse https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String path = "pathTodir";

// Crie um Documento Pdf
Document document = new Document();

// Obtenha o Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Defina o Título e o Idioma para o Documento
taggedContent.setTitle("Documento Pdf Marcado");
taggedContent.setLanguage("en-US");

// Obtenha Elementos de Estrutura Raiz
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// Defina o Texto para o Elemento de Estrutura de Texto
p.setText("Parágrafo.");
rootElement.appendChild(p);


// Salve o Documento Pdf Marcado
document.save(path + "TextStructureElement.pdf");
```


## Configurando Elementos de Estrutura de Bloco de Texto

Para configurar elementos de estrutura de bloco de texto de um Documento PDF Marcado, Aspose.PDF oferece as Classes [HeaderElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement) e [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Você pode adicionar objetos dessas classes como um filho do objeto **StructureElement**. O trecho de código a seguir mostra como definir elementos de estrutura de bloco de texto de um Documento PDF Marcado:

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

// Obter Elemento de Estrutura Raiz
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. Cabeçalho de Nível 1");
h2.setText("H2. Cabeçalho de Nível 2");
h3.setText("H3. Cabeçalho de Nível 3");
h4.setText("H4. Cabeçalho de Nível 4");
h5.setText("H5. Cabeçalho de Nível 5");
h6.setText("H6. Cabeçalho de Nível 6");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.appendChild(p);

// Salvar Documento Pdf Marcado
document.save(path + "TextBlockStructureElements.pdf");
```


## Configurando Elementos de Estrutura Inline

Para definir elementos de estrutura inline de um Documento PDF Marcado, o Aspose.PDF oferece as Classes [SpanElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement) e [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Você pode anexar objetos dessas classes como um filho do objeto **StructureElement**. O trecho de código a seguir mostra como definir elementos de estrutura inline de um Documento PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório dos documentos.
String path = "pathTodir";
// Criar Documento Pdf
Document document = new Document();

// Obter Conteúdo para trabalhar com TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Definir Título e Idioma para o Documento
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Obter Elemento de Estrutura Raiz
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

SpanElement spanH11 = taggedContent.createSpanElement();
spanH11.setText("H1. ");
h1.appendChild(spanH11);
SpanElement spanH12 = taggedContent.createSpanElement();
spanH12.setText("Cabeçalho Nível 1");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("Cabeçalho Nível 2");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("Cabeçalho Nível 3");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("Cabeçalho Nível 4");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("Cabeçalho Nível 5");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("Cabeçalho Nível 6");
h6.appendChild(spanH62);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. ");
rootElement.appendChild(p);
SpanElement span1 = taggedContent.createSpanElement();
span1.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.appendChild(span1);
SpanElement span2 = taggedContent.createSpanElement();
span2.setText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.appendChild(span2);
SpanElement span3 = taggedContent.createSpanElement();
span3.setText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.appendChild(span3);
SpanElement span4 = taggedContent.createSpanElement();
span4.setText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.appendChild(span4);
SpanElement span5 = taggedContent.createSpanElement();
span5.setText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.appendChild(span5);
SpanElement span6 = taggedContent.createSpanElement();
span6.setText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.appendChild(span6);
SpanElement span7 = taggedContent.createSpanElement();
span7.setText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.appendChild(span7);
SpanElement span8 = taggedContent.createSpanElement();
span8.setText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.appendChild(span8);
SpanElement span9 = taggedContent.createSpanElement();
span9.setText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.appendChild(span9);
SpanElement span10 = taggedContent.createSpanElement();
span10.setText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.appendChild(span10);

// Salvar Documento Pdf Marcado
document.save(path + "InlineStructureElements.pdf");
```


## Definindo Nome de Tag Personalizado

Para definir um nome de tag personalizado dos elementos de um Documento PDF Marcado, o Aspose.PDF oferece o método **setTag()** para elementos. O trecho de código a seguir mostra como definir um nome de tag personalizado:

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

// Criar Elementos de Estrutura Lógica
SectElement sect = taggedContent.createSectElement();
taggedContent.getRootElement().appendChild(sect);

ParagraphElement p1 = taggedContent.createParagraphElement();
ParagraphElement p2 = taggedContent.createParagraphElement();
ParagraphElement p3 = taggedContent.createParagraphElement();
ParagraphElement p4 = taggedContent.createParagraphElement();

p1.setText("P1. ");
p2.setText("P2. ");
p3.setText("P3. ");
p4.setText("P4. ");

p1.setTag("P1");
p2.setTag("Para");
p3.setTag("Para");
p4.setTag("Paragraph");

sect.appendChild(p1);
sect.appendChild(p2);
sect.appendChild(p3);
sect.appendChild(p4);

SpanElement span1 = taggedContent.createSpanElement();
SpanElement span2 = taggedContent.createSpanElement();
SpanElement span3 = taggedContent.createSpanElement();
SpanElement span4 = taggedContent.createSpanElement();

span1.setText("Span 1.");
span2.setText("Span 2.");
span3.setText("Span 3.");
span4.setText("Span 4.");

span1.setTag("SPAN");
span2.setTag("Sp");
span3.setTag("Sp");
span4.setTag("TheSpan");

p1.appendChild(span1);
p2.appendChild(span2);
p3.appendChild(span3);
p4.appendChild(span4);

// Salvar Documento PDF Marcado
document.save(path + "CustomTag.pdf");
```


## Adicionando Elemento de Estrutura em Elementos

Para definir elementos de estrutura de link em um Documento PDF Marcado, Aspose.PDF oferece o método **createLinkElement()** da Interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). O trecho de código a seguir mostra como definir elementos de estrutura em um parágrafo com texto de um Documento PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// Criação de documento e obtendo Conteúdo PDF Marcado
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

// Definindo Título e Idioma Natural para o documento
taggedContent.setTitle("Exemplo de Elementos de Texto");
taggedContent.setLanguage("en-US");

// Obtendo elemento de estrutura raiz (elemento de estrutura do Documento)
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p1 = taggedContent.createParagraphElement();
rootElement.appendChild(p1);
SpanElement span11 = taggedContent.createSpanElement();
span11.setText("Span_11");
SpanElement span12 = taggedContent.createSpanElement();
span12.setText(" e Span_12.");
p1.setText("Parágrafo com ");
p1.appendChild(span11);
p1.appendChild(span12);

ParagraphElement p2 = taggedContent.createParagraphElement();
rootElement.appendChild(p2);
SpanElement span21 = taggedContent.createSpanElement();
span21.setText("Span_21");
SpanElement span22 = taggedContent.createSpanElement();
span22.setText("Span_22.");
p2.appendChild(span21);
p2.setText(" e ");
p2.appendChild(span22);

ParagraphElement p3 = taggedContent.createParagraphElement();
rootElement.appendChild(p3);
SpanElement span31 = taggedContent.createSpanElement();
span31.setText("Span_31");
SpanElement span32 = taggedContent.createSpanElement();
span32.setText(" e Span_32");
p3.appendChild(span31);
p3.appendChild(span32);
p3.setText(".");

ParagraphElement p4 = taggedContent.createParagraphElement();
rootElement.appendChild(p4);
SpanElement span41 = taggedContent.createSpanElement();
SpanElement span411 = taggedContent.createSpanElement();
span411.setText("Span_411, ");
span41.setText("Span_41, ");
span41.appendChild(span411);
SpanElement span42 = taggedContent.createSpanElement();
SpanElement span421 = taggedContent.createSpanElement();
span421.setText("Span 421 e ");
span42.appendChild(span421);
span42.setText("Span_42");
p4.appendChild(span41);
p4.appendChild(span42);
p4.setText(".");

// Salvar Documento PDF Marcado
document.save(outFile);
```


## Definindo Elemento de Estrutura de Nota

Aspose.PDF para Java API também permite que você adicione um **NoteElement** em um documento PDF marcado. O snippet de código a seguir mostra como adicionar um elemento de nota em um Documento PDF Marcado:

```java
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-Java
// O caminho para o diretório de documentos.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// Cria Documento Pdf
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Exemplo de Elementos de Nota");
taggedContent.setLanguage("en-US");

// Adiciona Elemento de Parágrafo
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// Adiciona NoteElement
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("Nota com ID gerado automaticamente. ");

// Adiciona NoteElement
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("Nota com ID = 'note_002'. ");
note2.setId("note_002");

// Adiciona NoteElement
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("Nota com ID = 'note_003'. ");
note3.setId("note_003");
// Salva Documento Pdf Marcado
document.save(outFile);
```