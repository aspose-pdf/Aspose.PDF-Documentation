---
title: Obtenir des informations sur un fichier PDF en PHP
type: docs
weight: 40
url: /java/get-pdf-file-information-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obtenir des informations sur un fichier PDF

Pour obtenir des informations sur un document Pdf en utilisant **Aspose.PDF Java for PHP**, il suffit d'invoquer la classe **GetPdfFileInfo**.

Code PHP

```php

# Ouvrir un document pdf.
$doc = new Document($dataDir . "input1.pdf");

# Obtenir les informations du document
$doc_info = $doc->getInfo();

# Afficher les informations du document
print "Auteur:-" . $doc_info->getAuthor();
print "Date de création:-" . $doc_info->getCreationDate();
print "Mots clés:-" . $doc_info->getKeywords();
print "Date de modification:-" . $doc_info->getModDate();
print "Sujet:-" . $doc_info->getSubject();
print "Titre:-" . $doc_info->getTitle();

```

**Télécharger le code en cours d'exécution**

Téléchargez **Get PDF File Information (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/GetPdfFileInfo.php)