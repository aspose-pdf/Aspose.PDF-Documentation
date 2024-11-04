---
title: Create Document
type: docs
weight: 10
url: /java/create-pdf-document/
description: Aspose.PDF para Java ajuda você a criar documentos PDF e arquivos PDF pesquisáveis em poucos passos fáceis.
lastmod: "2021-06-05"
---

Neste artigo, vamos mostrar como usar a API Aspose.PDF para Java para gerar e ler facilmente arquivos PDF em aplicativos Java.

A API Aspose.PDF para Java permite que os desenvolvedores de aplicativos Java integrem funcionalidades de processamento de documentos PDF em suas aplicações. Pode ser usada para criar e ler arquivos PDF sem a necessidade de qualquer outro software instalado na máquina subjacente. Aspose.PDF para Java pode ser usado em uma variedade de tipos de aplicativos Java, como aplicativos Desktop, JSP e JSF.

## Como Criar Arquivo PDF usando Java

Para criar um arquivo PDF usando Java, os seguintes passos podem ser usados.

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)

1. Adicione um objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) à coleção Pages do objeto Document
1. Adicione [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) à coleção [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) da página
1. Salve o documento PDF resultante

```java
package com.aspose.pdf.examples;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.Document.CallBackGetHocr;

public class ExampleCreate {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    
    public static void Create() {        
        Document document = new Document();
 
        //Adicionar página
        Page page = document.getPages().add();
         
        // Adicionar texto à nova página
        page.getParagraphs().add(new TextFragment("Hello World!"));
         
        // Salvar PDF atualizado
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```


No caso, criamos um documento PDF de uma página com tamanho A4, orientação retrato. Nossa página conterá um "Hello, World" na parte superior esquerda da página.

Além disso, o Aspose.PDF para Java fornece a capacidade de criar um PDF pesquisável. Vamos aprender o próximo trecho de código:

```java
public static void CreateSearchablePDF() {                
        Document doc = new Document(_dataDir + "sample1.pdf");
        
        // Criar callBack - lógica para reconhecer texto em imagens de pdf. Use suporte OCR externo que suporte o padrão HOCR(http://en.wikipedia.org/wiki/HOCR).
        // Usamos o OCR gratuito google tesseract(http://en.wikipedia.org/wiki/Tesseract_%28software%29)
        
        CallBackGetHocr cbgh = new CallBackGetHocr() {
            @Override
            public String invoke(java.awt.image.BufferedImage img) {
                File outputfile = new File(_dataDir + "test.jpg");
                try {
                    ImageIO.write(img, "jpg", outputfile);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
        
                try {
                    java.lang.Process process = Runtime.getRuntime().exec("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    System.out.println("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    process.waitFor();
        
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
        
                // lendo out.html para string
                File file = new File(_dataDir + "out.hocr");
                StringBuilder fileContents = new StringBuilder((int) file.length());
                Scanner scanner = null;
                try {
                    scanner = new Scanner(file);
                    String lineSeparator = System.getProperty("line.separator");
        
                    while (scanner.hasNextLine()) {
                        fileContents.append(scanner.nextLine() + lineSeparator);
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } finally {
                    if (scanner != null)
                        scanner.close();
                }
        
                // deletando arquivos temporários
                File fileOut = new File(_dataDir + "out.hocr");
                if (fileOut.exists()) {
                    fileOut.delete();
                }
                File fileTest = new File(_dataDir + "test.jpg");
                if (fileTest.exists()) {
                    fileTest.delete();
                }
        
                return fileContents.toString();
            }
        };
        // Fim do callBack
        
        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");        
    }
}
```