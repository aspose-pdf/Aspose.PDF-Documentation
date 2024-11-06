---
title: Créer un Document PDF
linktitle: Créer
type: docs
weight: 10
url: fr/java/create-document/
description: Apprenez à créer un fichier PDF avec Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF pour Java** API permet aux développeurs d'applications Java d'intégrer des fonctionnalités de traitement de documents PDF dans leurs applications. Il peut être utilisé pour créer et lire des fichiers PDF sans avoir besoin d'aucun autre logiciel installé sur la machine sous-jacente. Aspose.PDF pour Java peut être utilisé dans une variété de types d'applications Java telles que les applications Desktop, JSP et JSF.

## Comment créer un fichier PDF en utilisant Java

Pour créer un fichier PDF en utilisant Java, les étapes suivantes peuvent être utilisées.

1. Instancier un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)
1. Ajouter une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à l'objet document
1. Créer un objet [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)

1. Ajouter [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) à la collection de [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) de la page
1. Enregistrer le document PDF résultant

```java
// Initialiser l'objet document
Document document = new Document();
 
// Ajouter une page
Page page = document.getPages().add();
 
// Ajouter du texte à la nouvelle page
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// Enregistrer le PDF mis à jour
document.save("HelloWorld_out.pdf");
```