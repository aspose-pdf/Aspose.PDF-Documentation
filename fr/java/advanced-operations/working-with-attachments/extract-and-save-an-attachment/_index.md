---
title: Extraire et Enregistrer une Pièce Jointe
linktitle: Extraire et Enregistrer une Pièce Jointe
type: docs
weight: 20
url: /fr/java/extract-and-save-an-attachment/
description: Aspose.PDF pour Java vous permet d'obtenir toutes les pièces jointes d'un document PDF. De plus, vous pouvez obtenir une pièce jointe individuelle de votre document.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir les Pièces Jointes d'un Document PDF

Avec Aspose.PDF, il est possible d'obtenir toutes les pièces jointes d'un document PDF. Ceci est utile soit lorsque vous souhaitez enregistrer les documents séparément du PDF, soit si vous avez besoin de retirer les pièces jointes d'un PDF.

Les extraits de code suivants montrent comment obtenir toutes les pièces jointes d'un document PDF.

```java
   public static void GetAttachmentsFromPDFDocument() {
// Ouvrir le document
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Obtenir un fichier intégré particulier
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Obtenir les propriétés du fichier
  System.out.printf("Nom : - " + fileSpecification.getName());
  System.out.printf("\nDescription : - " + fileSpecification.getDescription());
  System.out.printf("\nType MIME : - " + fileSpecification.getMIMEType());
  // Obtenir la pièce jointe du fichier PDF
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // Créer le chemin pour le fichier depuis le pdf
   file.getParentFile().mkdirs();
   // Créer et extraire le fichier depuis le pdf
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // Fermer l'objet InputStream
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // Fermer l'objet Document
  pdfDocument.dispose();
        
    }

```


## Obtenir des informations sur la pièce jointe

Comme mentionné dans [Obtenir des pièces jointes à partir d'un document PDF](/pdf/fr/java/get-attachments-from-a-pdf-document/), les informations sur la pièce jointe sont contenues dans l'objet [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification), rassemblées avec d'autres pièces jointes dans la collection EmbeddedFiles de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

L'objet [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) fournit des méthodes qui obtiennent des informations sur la pièce jointe, par exemple :

- getName() – obtient le nom du fichier.
- [getDescription()](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – obtient la description du fichier.
- getMIMEType() – obtient le type MIME du fichier.
- getParams() – informations sur les paramètres du fichier, par exemple CheckSum, CreationDate, ModDate et Size.

Pour obtenir ces paramètres, assurez-vous d'abord que la méthode getParams() ne renvoie pas null.

Soit en parcourant toutes les pièces jointes dans la collection EmbeddedFiles en utilisant une boucle for, soit en obtenant une pièce jointe individuelle en spécifiant sa valeur d'index.
 The following code snippet shows how to get information about a specific attachment.

```java
    public static void GetAttachmentInformation() {
  // Ouvrir le document
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Obtenir un fichier intégré particulier
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // Obtenir les propriétés du fichier
  System.out.println("Nom:-" + fileSpecification.getName());
  System.out.println("Description:- " + fileSpecification.getDescription());
  System.out.println("Type MIME:-" + fileSpecification.getMIMEType());
  // Vérifier si l'objet paramètre contient les paramètres
  if (fileSpecification.getParams() != null) {
   System.out.println("Somme de contrôle:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Date de création:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Date de modification:- " + fileSpecification.getParams().getModDate());
   System.out.println("Taille:- " + fileSpecification.getParams().getSize());
  } 
```