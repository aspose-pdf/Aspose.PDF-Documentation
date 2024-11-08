---
title: Trabalhando com Portfólio em documentos PDF
linktitle: Portfólio
type: docs
weight: 40
url: /pt/java/portfolio/
description: Como Criar um Portfólio em PDF com Java. Você deve usar um arquivo do Microsoft Excel, um documento do Word e uma imagem para criar um Portfólio em PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Primeiro, vamos entender **O que é um formato de arquivo de Portfólio em PDF?**

Por exemplo, considere um arquivo de Portfólio em PDF que contém um documento do Word, Excel, apresentações do PowerPoint etc., como anexos. Aqui, cada um dos arquivos anexados mantém seu formato de documento original, mas é incorporado ou montado em um único arquivo de Portfólio em PDF. Você pode, é claro, abrir, ler ou editar cada um dos arquivos individuais do Portfólio em PDF como se estivesse em um drive ou pasta. Além disso, assim como um documento PDF normal, você também pode aplicar marcas d'água, definir senhas e permissões de segurança, como a capacidade de visualizar, imprimir ou fazer alterações nos anexos do Portfólio em PDF.

Podemos colocar ou montar arquivos nativos, em seus tipos ou formatos originais como anexos, em um arquivo de Portfólio em PDF.

## Como Criar um Portfólio PDF

Aspose.PDF permite criar documentos de Portfólio PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Adicione um arquivo em um objeto Document.Collection após obtê-lo com a classe [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). Quando os arquivos forem adicionados, use o método Save da classe Document para salvar o documento do portfólio.

O exemplo a seguir usa um arquivo Microsoft Excel, um documento Word e um arquivo de imagem para criar um Portfólio PDF.

O código abaixo resulta no seguinte portfólio.

### Um Portfólio PDF criado com Aspose.PDF

![Um Portfólio PDF criado com Aspose.PDF para Java](working-with-pdf-portfolio_1.jpg)

```java
    public static void CreatePortfolio() throws IOException {
        // Instanciar Objeto Document
        Document pdfDocument = new Document();

        // Instanciar objeto Collection do documento
        pdfDocument.setCollection(new Collection());

        // Obter Arquivos para adicionar ao Portfólio
        FileSpecification excel = new FileSpecification(_dataDir + "HelloWorld.xlsx");
        FileSpecification word = new FileSpecification(_dataDir + "HelloWorld.docx");
        FileSpecification image = new FileSpecification(_dataDir + "aspose-logo.jpg");

        // Fornecer descrição dos arquivos
        excel.setDescription ("Arquivo Excel");
        word.setDescription ("Arquivo Word");
        image.setDescription ("Arquivo de Imagem");

        // Adicionar arquivos à coleção de documentos
        pdfDocument.getCollection().add(excel);
        pdfDocument.getCollection().add(word);
        pdfDocument.getCollection().add(image);

        // Salvar documento do Portfólio
        pdfDocument.save(_dataDir + "CreatePDFPortfolio_out.pdf");
    }
```


## Extrair arquivos de um Portfólio PDF

Os Portfólios PDF permitem que você reúna conteúdo de uma variedade de fontes (por exemplo, arquivos PDF, Word, Excel, JPEG) em um único contêiner unificado. Os arquivos originais mantêm suas identidades individuais, mas são montados em um arquivo de Portfólio PDF. Os usuários podem abrir, ler, editar e formatar cada arquivo componente independentemente dos outros arquivos componentes.

Aspose.PDF permite a criação de documentos de Portfólio PDF usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Ele também oferece a capacidade de extrair arquivos de um portfólio PDF.

O trecho de código a seguir mostra as etapas para extrair arquivos de um portfólio PDF.

![Extrair arquivos de um Portfólio PDF](working-with-pdf-portfolio_2.jpg)

```java
    public static void ExtractPortfolio() throws IOException {
        // Abrir um documento
        Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
        // Obter coleção de arquivos incorporados
        EmbeddedFileCollection embeddedFiles = pdfDocument.getEmbeddedFiles();

        // Iterar através de arquivos individuais do Portfólio
        for (FileSpecification fileSpecification : embeddedFiles) {
            InputStream initialStream = fileSpecification.getContents();
            byte[] buffer = new byte[fileSpecification.getContents().available()];
            initialStream.read(buffer);

            File targetFile = new File(_dataDir + fileSpecification.getName());
            OutputStream outStream = new FileOutputStream(targetFile);
            outStream.write(buffer);
            outStream.close();
        }
    }
```


## Remover Arquivos de um Portfólio PDF

Para deletar/remover arquivos de um portfólio PDF, tente usar as seguintes linhas de código.

```java
public static void RemoveFilesFromPDFPortfolio() {
    // Carregar o Portfólio PDF de origem
    Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
    pdfDocument.getCollection().delete();
    pdfDocument.save(_dataDir + "No_PortFolio_out.pdf");
}
```