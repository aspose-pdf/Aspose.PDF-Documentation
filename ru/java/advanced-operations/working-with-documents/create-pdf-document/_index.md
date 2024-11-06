---
title: Создать документ
type: docs
weight: 10
url: ru/java/create-pdf-document/
description: Aspose.PDF для Java помогает создавать PDF-документ и файл поискового PDF всего за несколько простых шагов.
lastmod: "2021-06-05"
---

В этой статье мы покажем, как использовать Aspose.PDF для Java API для легкого создания и чтения PDF-файлов в Java-приложениях.

Aspose.PDF для Java API позволяет разработчикам Java-приложений встроить функциональность обработки PDF-документов в свои приложения. Он может использоваться для создания и чтения PDF-файлов без необходимости установки какого-либо другого программного обеспечения на базовую машину. Aspose.PDF для Java может использоваться в различных типах Java-приложений, таких как настольные приложения, JSP и JSF приложения.

## Как создать PDF файл с использованием Java

Чтобы создать PDF файл с использованием Java, можно использовать следующие шаги.

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)

1. Добавьте объект [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) в коллекцию Pages объекта Document
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) в коллекцию [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) страницы
1. Сохраните полученный PDF документ

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
 
        //Добавить страницу
        Page page = document.getPages().add();
         
        // Добавить текст на новую страницу
        page.getParagraphs().add(new TextFragment("Hello World!"));
         
        // Сохранить обновленный PDF
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```


В этом случае мы создаем PDF-документ на одной странице с размером страницы A4, портретной ориентации. Наша страница будет содержать "Hello, World" в верхней левой части страницы.

Кроме того, Aspose.PDF для Java предоставляет возможность создать поисковый PDF. Давайте изучим следующий кодовый фрагмент:

```java
public static void CreateSearchablePDF() {                
        Document doc = new Document(_dataDir + "sample1.pdf");
        
        // Создать callBack - логика распознавания текста для изображений pdf. Используйте внешние OCR, поддерживающие стандарт HOCR(http://en.wikipedia.org/wiki/HOCR).
        // Мы использовали бесплатный google tesseract OCR(http://en.wikipedia.org/wiki/Tesseract_%28software%29)
        
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
        
                // чтение out.html в строку
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
        
                // удаление временных файлов
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
        // Конец callBack
        
        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");        
    }
}
```