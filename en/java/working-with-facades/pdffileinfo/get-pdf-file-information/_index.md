---
title: Get PDF file information - facades
type: docs
weight: 10
url: /java/get-pdf-information/
description: This section explains how to get PDF file information with Aspose.PDF Facades using PdfFileInfo Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

In order to get information specific to PDF file, you need to create an object of [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) class. After that, you can get values of the individual properties like Subject, Title, Keywords and Creator etc.

The following code snippet shows you how to get PDF file information.

```java
public static void GetPdfInfo()
    {
        // Open document
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Get PDF information
        System.out.println("Subject: " + fileInfo.getSubject());
        System.out.println("Title: " + fileInfo.getTitle());
        System.out.println("Keywords: " + fileInfo.getKeywords());
        System.out.println("Creator: " + fileInfo.getCreator());
        System.out.println("Creation Date: " + fileInfo.getCreationDate());
        System.out.println("Modification Date: " + fileInfo.getModDate());
        // Find whether is it valid PDF and it is encrypted as well
        System.out.println("Is Valid PDF: " + fileInfo.isPdfFile());
        System.out.println("Is Encrypted: " + fileInfo.isEncrypted());

        System.out.println("Page width:" +fileInfo.getPageWidth(1));
    }
```

## Get Meta Info

In order to get information, we use the [getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--) method. With 'Hashtable'  we get all the possible values.

```java
public static void GetMetaInfo()
    {        
        // Create instance of PdffileInfo object
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // Retrieve all existing custom attributes
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // get key
            String key = enumerator.nextElement();  
            // print key and value corresponding to that key
            System.out.println(key + ": " + hTable.get(key));
        }

        // Retrieve one custom attributes
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```