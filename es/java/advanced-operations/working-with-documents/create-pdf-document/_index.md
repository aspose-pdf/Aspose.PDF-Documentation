---
title: Crear Documento
type: docs
weight: 10
url: es/java/create-pdf-document/
description: Aspose.PDF para Java te ayuda a crear documentos PDF y archivos PDF buscables en pocos pasos fáciles.
lastmod: "2021-06-05"
---

En este artículo, vamos a mostrar cómo usar Aspose.PDF para Java API para generar y leer fácilmente archivos PDF en aplicaciones Java.

Aspose.PDF para Java API permite a los desarrolladores de aplicaciones Java integrar la funcionalidad de procesamiento de documentos PDF en sus aplicaciones. Se puede usar para crear y leer archivos PDF sin la necesidad de ningún otro software instalado en la máquina subyacente. Aspose.PDF para Java se puede usar en una variedad de tipos de aplicaciones Java como aplicaciones de escritorio, JSP y JSF.

## Cómo Crear un Archivo PDF usando Java

Para crear un archivo PDF usando Java, se pueden seguir los siguientes pasos.

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)

1. Agregar un objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) a la colección Pages del objeto Document
1. Agregar [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) a la colección [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) de la página
1. Guardar el documento PDF resultante

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
 
        //Agregar página
        Page page = document.getPages().add();
         
        // Agregar texto a la nueva página
        page.getParagraphs().add(new TextFragment("¡Hola Mundo!"));
         
        // Guardar el PDF actualizado
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```


En este caso, creamos un documento PDF de una página con tamaño de página A4, orientación vertical. Nuestra página contendrá un "Hola, Mundo" en la parte superior izquierda de la página.

Además, Aspose.PDF para Java proporciona la capacidad de crear cómo crear un PDF con capacidad de búsqueda. Aprendamos el siguiente fragmento de código:

```java
public static void CreateSearchablePDF() {                
        Document doc = new Document(_dataDir + "sample1.pdf");
        
        // Crear callBack - lógica para reconocer texto para imágenes en pdf. Usar OCR externo que soporte el estándar HOCR(http://en.wikipedia.org/wiki/HOCR).
        // Hemos utilizado el OCR gratuito de google tesseract(http://en.wikipedia.org/wiki/Tesseract_%28software%29)
        
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
        
                // leyendo out.html a cadena
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
        
                // eliminando archivos temporales
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
        // Fin callBack
        
        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");        
    }
}
```