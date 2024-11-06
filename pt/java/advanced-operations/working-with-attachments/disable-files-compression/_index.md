---
title: Desativar Compressão de Arquivos ao Adicionar como Recursos Incorporados
linktitle: Desativar Compressão de Arquivos
type: docs
weight: 40
url: pt/java/disable-files-compression-when-adding-as-embedded-resources/
description: Este artigo explica como desativar a compressão de arquivos ao adicionar como recursos incorporados
lastmod: "2021-06-05"
---

A classe [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) permite que os desenvolvedores adicionem anexos a documentos PDF. Por padrão, os anexos são comprimidos. Atualizamos a API para permitir que os desenvolvedores desativem a compressão ao adicionar arquivos como recurso incorporado. Isso dá aos desenvolvedores mais controle sobre como os arquivos são processados.

Para permitir que os desenvolvedores controlem a compressão de arquivos, o método [setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-) foi adicionado à classe [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification).
 Esta propriedade determina qual codificação será usada para a compressão de arquivos. O método aceita um valor do enumerador [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding). Os valores possíveis são [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None e [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

Se a Codificação estiver definida como [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None, o anexo não será comprimido. A codificação padrão é [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

O trecho de código a seguir mostra como adicionar um anexo a um documento PDF.

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // obter referência do arquivo de origem/entrada
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // ler todo o conteúdo do arquivo de origem em ByteArray
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // criar uma instância do objeto Stream a partir do conteúdo do ByteArray
  InputStream is = new ByteArrayInputStream(data);
  // Instanciar objeto Document a partir da instância do stream
  Document pdfDocument = new Document(is);
  // configurar novo arquivo a ser adicionado como anexo
  FileSpecification fileSpecification = new FileSpecification("test.txt", "Arquivo de texto de exemplo");
  // Especificar a propriedade Encoding definindo-a como FileEncoding.None
  fileSpecification.setEncoding(FileEncoding.None);
  // adicionar anexo à coleção de anexos do documento
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // salvar nova saída
  pdfDocument.save("output.pdf");
    }
```