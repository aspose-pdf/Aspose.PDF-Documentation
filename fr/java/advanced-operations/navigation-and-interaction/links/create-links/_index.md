---
title: Créer des liens dans un fichier PDF
linktitle: Créer des liens
type: docs
weight: 10
url: fr/java/create-links/
description: Cette section explique comment créer des liens dans votre document PDF avec Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Créer des liens

Aspose.PDF pour Java vous permet d'ajouter un lien vers un fichier PDF externe afin que vous puissiez lier plusieurs documents ensemble. En ajoutant un lien vers une application dans un document, il est possible de lier à des applications depuis un document. Ceci est utile lorsque vous souhaitez que les lecteurs effectuent une certaine action à un moment précis dans un tutoriel, par exemple, ou pour créer un document riche en fonctionnalités. Pour créer un lien d'application :

1. [Créer un document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) objet.
1. Obtenez la [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à laquelle vous souhaitez ajouter un lien.

1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) en utilisant les objets [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) et [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Définissez les attributs du lien en utilisant l'objet [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Définissez également l'objet [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) et appelez la méthode setAction(..).
1. Lors de la création de l'objet [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction), spécifiez l'application que vous souhaitez lancer.
1. Ajoutez le lien à la collection [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) de l'objet Page.
1. Enfin, enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Le fragment de code suivant montre comment créer un lien vers une application dans un fichier PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;


public class ExampleLinks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // Ouvrir le document
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // Créer un lien
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // Enregistrer le document mis à jour
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### Créer un lien de document PDF dans un fichier PDF

Aspose.PDF pour Java vous permet d'ajouter un lien vers un fichier PDF externe afin que vous puissiez lier plusieurs documents ensemble.
 Pour créer un lien de document PDF :

1. Tout d'abord, créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Ensuite, obtenez la [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) particulière à laquelle vous souhaitez ajouter le lien.
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) en utilisant les objets [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) et [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Définissez les attributs du lien en utilisant l'objet [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Appelez la méthode setAction(..) et passez l'objet [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction).
1. Lors de la création de l'objet [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction), spécifiez le fichier PDF qui doit être lancé, ainsi que le numéro de page sur lequel il doit s'ouvrir.
1. Ajoutez le lien à la collection [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) de l'objet Page.
1. Enfin, enregistrez le PDF mis à jour en utilisant la méthode Save de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Le snippet de code suivant montre comment créer un lien de document PDF dans un fichier PDF.

```java
    public static void CreatePDFDocumentLink() {

        // Ouvrir le document
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // Créer un lien
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // Enregistrer le document mis à jour
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```