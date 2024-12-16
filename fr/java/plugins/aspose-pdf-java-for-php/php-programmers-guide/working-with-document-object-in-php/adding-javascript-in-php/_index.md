---
title: Ajouter JavaScript dans PHP
type: docs
weight: 10
url: /fr/java/adding-javascript-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ajouter JavaScript

Pour ajouter JavaScript dans un document Pdf en utilisant **Aspose.PDF Java pour PHP**, il suffit d'invoquer la classe **AddJavaScript**.

Code PHP

```php
# Ouvrir un document pdf.
$doc = new Document($dataDir . "input1.pdf");

# Ajouter JavaScript au niveau du document
# Instancier JavascriptAction avec l'instruction JavaScript souhaitée
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assigner l'objet JavascriptAction à l'action souhaitée du Document
$doc->setOpenAction($javaScript);

# Ajouter JavaScript au niveau de la page
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('la page 2 est ouverte')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('la page 2 est fermée')"));

# Enregistrer le document PDF
$doc->save($dataDir . "JavaScript-Added.pdf");

print "JavaScript ajouté avec succès, veuillez vérifier le fichier de sortie.";
```


**Télécharger le code en cours d'exécution**

Téléchargez **Ajouter JavaScript (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)