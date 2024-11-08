---
title: Migration depuis la version Pre 4.x.x d'Aspose.PDF pour Java
type: docs
weight: 20
url: /fr/java/migration-from-pre-4-x-x-version-of-aspose-pdf-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Une nouvelle version auto-portée d'Aspose.PDF pour Java a été publiée et maintenant ce produit unique supporte la capacité de générer des documents PDF à partir de zéro ainsi que la capacité de manipuler des documents PDF existants.

{{% /alert %}}

## Binaires du produit

{{% alert color="primary" %}}

Dans la première version (v4.0.0), nous livrons deux fichiers jar, à savoir **aspose.pdf-3.3.0.jdk15.jar** et **aspose.pdf-new-4.0.0.jar**.
{{% /alert %}}
- **aspose.pdf-3.3.0.jdk14.jar**

Ce fichier jar est la même version du produit que celle actuellement disponible dans le module de téléchargement avec le titre [Aspose.PDF for java 3.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry417659.aspx). Par la suite, nous allons appeler cette version de publication comme legacy Aspose.PDF for Java. Dans cette première version, les utilisateurs existants d'Aspose.PDF pour Java pourraient ne pas être impactés car ils obtiennent la même version de publication. Cependant, bientôt, nous retirerons ce fichier jar séparé et toutes les classes et énumérations de l'ancien Aspose.PDF pour Java (avant 4.x.x) seront disponibles sous le package com.aspose.pdf.generator du fichier unique aspose.pdf-new-4.x.x.jar.
- **aspose.pdf-new-4.0.0.jar**
  Ce fichier jar est une nouvelle version auto-portée d'Aspose.PDF pour .NET vers la plateforme Java.
 Ce fichier jar contient le nouveau modèle d'objet de document (DOM) pour créer ainsi que manipuler les fichiers PDF existants et aussi l'actuel Aspose.PDF.Kit pour Java. Toutes les classes et énumérations d'Aspose.PDF.Kit pour Java sont regroupées sous le package com.aspose.pdf.facades et au troisième trimestre de 2013, Aspose.PDF.Kit pour Java sera abandonné. Par conséquent, nous encourageons nos clients actuels d'Aspose.PDF.Kit pour Java à essayer de migrer leur code vers la nouvelle version auto-portée.

Veuillez consulter le billet de blog suivant pour obtenir plus d'informations sur la structure de l'Aspose.PDF pour Java auto-porté.