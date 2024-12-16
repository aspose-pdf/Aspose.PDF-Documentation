---
title: Obtener información de archivo PDF - fachadas
type: docs
weight: 10
url: /es/java/get-pdf-information/
description: Esta sección explica cómo obtener información del archivo PDF con Aspose.PDF Facades usando la clase PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para obtener información específica de un archivo PDF, necesitas crear un objeto de la clase [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). Después de eso, puedes obtener valores de las propiedades individuales como Asunto, Título, Palabras clave y Creador, etc.

El siguiente fragmento de código te muestra cómo obtener información del archivo PDF.

```java
public static void GetPdfInfo()
    {
        // Abrir documento
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Obtener información del PDF
        System.out.println("Asunto: " + fileInfo.getSubject());
        System.out.println("Título: " + fileInfo.getTitle());
        System.out.println("Palabras clave: " + fileInfo.getKeywords());
        System.out.println("Creador: " + fileInfo.getCreator());
        System.out.println("Fecha de creación: " + fileInfo.getCreationDate());
        System.out.println("Fecha de modificación: " + fileInfo.getModDate());
        // Determinar si es un PDF válido y si está encriptado también
        System.out.println("Es un PDF válido: " + fileInfo.isPdfFile());
        System.out.println("Está encriptado: " + fileInfo.isEncrypted());

        System.out.println("Ancho de página:" +fileInfo.getPageWidth(1));
    }
```


## Obtener Información Meta

Para obtener información, utilizamos el método [getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--). Con 'Hashtable' obtenemos todos los valores posibles.

```java
public static void GetMetaInfo()
    {        
        // Crear instancia del objeto PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // Recuperar todos los atributos personalizados existentes
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // obtener clave
            String key = enumerator.nextElement();  
            // imprimir clave y valor correspondiente a esa clave
            System.out.println(key + ": " + hTable.get(key));
        }

        // Recuperar un atributo personalizado
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```