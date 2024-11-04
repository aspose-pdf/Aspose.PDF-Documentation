---
title: Désactiver la Compression des Fichiers lors de l'Ajout comme Ressources Incorporées
linktitle: Désactiver la Compression des Fichiers
type: docs
weight: 40
url: /java/disable-files-compression-when-adding-as-embedded-resources/
description: Cet article explique comment désactiver la compression des fichiers lors de l'ajout comme ressources incorporées
lastmod: "2021-06-05"
---

La classe [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) permet aux développeurs d'ajouter des pièces jointes aux documents PDF. Par défaut, les pièces jointes sont compressées. Nous avons mis à jour l'API pour permettre aux développeurs de désactiver la compression lors de l'ajout de fichiers en tant que ressources incorporées. Cela donne aux développeurs plus de contrôle sur la façon dont les fichiers sont traités.

Pour permettre aux développeurs de contrôler la compression des fichiers, la méthode [setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-) a été ajoutée à la classe [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification).
 Cette propriété détermine quel encodage sera utilisé pour la compression de fichiers. La méthode accepte une valeur de l'énumérateur [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding). Les valeurs possibles sont [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None et [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

Si l'encodage est défini sur [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None, alors la pièce jointe n'est pas compressée. L'encodage par défaut est [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip.

Le fragment de code suivant montre comment ajouter une pièce jointe à un document PDF.

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // obtenir la référence du fichier source/entrée
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // lire tout le contenu du fichier source dans un tableau ByteArray
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // créer une instance de l'objet Stream à partir du contenu ByteArray
  InputStream is = new ByteArrayInputStream(data);
  // Instancier un objet Document à partir de l'instance de stream
  Document pdfDocument = new Document(is);
  // configurer un nouveau fichier à ajouter en tant que pièce jointe
  FileSpecification fileSpecification = new FileSpecification("test.txt", "Fichier texte exemple");
  // Spécifier le paramètre de la propriété Encoding en le définissant sur FileEncoding.None
  fileSpecification.setEncoding(FileEncoding.None);
  // ajouter la pièce jointe à la collection de pièces jointes du document
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // enregistrer la nouvelle sortie
  pdfDocument.save("output.pdf");
    }
```