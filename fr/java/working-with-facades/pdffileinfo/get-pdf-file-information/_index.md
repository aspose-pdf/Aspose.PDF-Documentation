---
title: Obtenir des informations sur le fichier PDF - façades
type: docs
weight: 10
url: fr/java/get-pdf-information/
description: Cette section explique comment obtenir des informations sur un fichier PDF avec Aspose.PDF Facades en utilisant la classe PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Pour obtenir des informations spécifiques à un fichier PDF, vous devez créer un objet de la classe [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). Après cela, vous pouvez obtenir les valeurs des propriétés individuelles telles que Sujet, Titre, Mots-clés et Créateur, etc.

Le fragment de code suivant vous montre comment obtenir des informations sur un fichier PDF.

```java
public static void GetPdfInfo()
    {
        // Ouvrir le document
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Obtenir des informations sur le PDF
        System.out.println("Sujet: " + fileInfo.getSubject());
        System.out.println("Titre: " + fileInfo.getTitle());
        System.out.println("Mots-clés: " + fileInfo.getKeywords());
        System.out.println("Créateur: " + fileInfo.getCreator());
        System.out.println("Date de création: " + fileInfo.getCreationDate());
        System.out.println("Date de modification: " + fileInfo.getModDate());
        // Vérifier si c'est un PDF valide et s'il est également crypté
        System.out.println("Est-ce un PDF valide: " + fileInfo.isPdfFile());
        System.out.println("Est crypté: " + fileInfo.isEncrypted());

        System.out.println("Largeur de la page:" +fileInfo.getPageWidth(1));
    }
```


## Obtenir des informations méta

Afin d'obtenir des informations, nous utilisons la méthode [getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--). Avec 'Hashtable' nous obtenons toutes les valeurs possibles.

```java
public static void GetMetaInfo()
    {        
        // Créer une instance de l'objet PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // Récupérer tous les attributs personnalisés existants
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // obtenir la clé
            String key = enumerator.nextElement();  
            // imprimer la clé et la valeur correspondant à cette clé
            System.out.println(key + ": " + hTable.get(key));
        }

        // Récupérer un attribut personnalisé
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```