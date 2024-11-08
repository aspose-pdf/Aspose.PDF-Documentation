---
title: Converter arquivo PDF para outros formatos 
linktitle: Converter PDF para outros formatos 
type: docs
weight: 90
url: /pt/java/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Este tópico mostra como o Aspose.PDF permite converter arquivos PDF para outros formatos de arquivo.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter PDF para EPUB

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode experimentar a funcionalidade e a qualidade do trabalho.

[![Conversão Aspose.PDF PDF para EPUB com App Gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Publicação Eletrônica">EPUB</abbr>** (abreviação de publicação eletrônica) é um padrão de livro eletrônico gratuito e aberto do International Digital Publishing Forum (IDPF).
 Arquivos têm a extensão .epub. EPUB é projetado para conteúdo refluível, o que significa que um leitor EPUB pode otimizar o texto para um dispositivo de exibição específico. EPUB também suporta conteúdo de layout fixo. O formato é destinado como um único formato que editores e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

Aspose.PDF para Java suporta o recurso de converter documentos PDF para o formato EPUB. Aspose.PDF para Java tem uma classe chamada [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) que pode ser usada como o segundo argumento para o método [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..), para gerar um arquivo EPUB. Por favor, tente usar o seguinte trecho de código para realizar este requisito.

```java
// Carregar documento PDF
Document document = new Document(DATA_DIR + "PDFToEPUB.pdf");
// Instanciar opções de salvamento Epub
EpubSaveOptions options = new EpubSaveOptions();
// Especificar o layout para conteúdos
options.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
// Salvar o documento ePUB
document.save(DATA_DIR + "PDFToEPUB_out.epub", options);
document.close();
```

## Converter PDF para LaTeX/TeX

**Aspose.PDF para Java** suporta a conversão de PDF para LaTeX/TeX. O formato de arquivo LaTeX é um formato de arquivo de texto com marcação especial e é usado no sistema de preparação de documentos baseado em TeX para composição tipográfica de alta qualidade.

Para converter arquivos PDF para TeX, o Aspose.PDF possui a classe [TeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions) que fornece o método `setOutDirectoryPath` para salvar imagens temporárias durante o processo de conversão.

O trecho de código a seguir mostra o processo de conversão de arquivos PDF para o formato TEX com Java.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX.pdf").toString();
String texDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX_out.tex").toString();

// Criar objeto Documento
Document document = new Document(documentFileName);

// Instanciar opção de salvamento LaTex
TeXSaveOptions saveOptions = new TeXSaveOptions();

// Especificar o diretório de saída
String pathToOutputDirectory = DATA_DIR.toString();

// Definir o caminho do diretório de saída para o objeto de opção de salvamento
saveOptions.setOutDirectoryPath(pathToOutputDirectory);

// Salvar arquivo PDF no formato LaTex
document.save(texDocumentFileName, saveOptions);
document.close();
```


{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["PDF para LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF PDF para LaTeX/TeX com Aplicativo Gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Converter PDF para Texto

**Aspose.PDF para Java** suporta a conversão de todo o documento PDF e de uma única página para um arquivo de Texto. 

### Converter todo o documento PDF para arquivo de Texto

Você pode converter um documento PDF para um arquivo TXT usando o método Visit da classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

O trecho de código a seguir explica como extrair os textos de todas as páginas.

```java
// Abrir documento
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Carregar documento PDF
Document document = new Document(pdfFileName);
TextAbsorber ta = new TextAbsorber();
ta.visit(document);
// Salvar o texto extraído no arquivo de texto
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
```


{{% alert color="success" %}}
**Tente converter PDF para Texto online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode experimentar a funcionalidade e qualidade do serviço.

[![Aspose.PDF Conversão de PDF para Texto com App Gratuito](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Converter página de PDF para arquivo de texto

Você pode converter um documento PDF em um arquivo TXT com Aspose.PDF para Java. Você deve usar o método Visit da classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) para resolver esta tarefa.

O trecho de código a seguir explica como extrair os textos das páginas específicas.

```java
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Carregar documento PDF
Document document = new Document(pdfFileName);

TextAbsorber ta = new TextAbsorber();
int[] pages = new int[] { 1, 3, 4 };

for (int page : pages) {
    ta.visit(document.getPages().get_Item(page));
}

// Salvar o texto extraído em arquivo de texto
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
document.close();
```


## Converter PDF para XPS

**Aspose.PDF para Java** oferece a possibilidade de converter arquivos PDF para o formato <abbr title="XML Paper Specification">XPS</abbr>. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com Java.

{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF para Java apresenta a você o aplicativo online gratuito ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão de PDF para XPS com Aplicativo Gratuito](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

O tipo de arquivo XPS está principalmente associado à Especificação de Papel XML pela Microsoft Corporation. A Especificação de Papel XML (XPS), anteriormente com o codinome Metro e englobando o conceito de marketing Caminho de Impressão de Próxima Geração (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos no sistema operacional Windows.

Para converter arquivos PDF para XPS, o Aspose.PDF possui a classe [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) que é usada como o segundo argumento no construtor Document.save(..) para gerar o arquivo XPS.
 O trecho de código a seguir mostra o processo de conversão de arquivos PDF para o formato XPS.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(DATA_DIR.toString(), "sample-res-xps.xps").toString();

// Criar objeto Document
Document document = new Document(documentFileName);

// Instanciar opções de salvamento XPS
XpsSaveOptions saveOptions = new XpsSaveOptions();

// Salvar saída em formato XML
document.save(xpsDocumentFileName, saveOptions);
document.close();
```