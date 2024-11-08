---
title: Ajouter une chaîne HTML en utilisant DOM dans PHP
type: docs
weight: 10
url: /fr/java/add-html-string-using-dom-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ajouter HTML

Pour ajouter une chaîne HTML dans un document Pdf en utilisant **Aspose.PDF Java for PHP**, il suffit d'invoquer le module **AddHtml**.

Code PHP

```php
# Instancier l'objet Document
$doc = new Document();

# Ajouter une page à la collection de pages du fichier PDF
$page = $doc->getPages()->add();

# Instancier HtmlFragment avec le contenu HTML
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# définir MarginInfo pour les détails des marges
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Définir les informations de marge
$title->setMargin($margin);

# Ajouter le Fragment HTML à la collection de paragraphes de la page
$page->getParagraphs()->add($title);

# Sauvegarder le fichier PDF
$doc->save($dataDir . "html.output.pdf");

print "HTML ajouté avec succès" . PHP_EOL;

```

**Télécharger le code en cours d'exécution**

Téléchargez **Ajouter HTML (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)