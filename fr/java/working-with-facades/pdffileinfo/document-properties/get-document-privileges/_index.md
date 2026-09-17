---
title: Obtenez des privilèges sur les documents
linktitle: Obtenez des privilèges sur les documents
type: docs
weight: 10
url: /java/get-document-privileges/
description: Découvrez comment inspecter les privilèges des documents PDF en Java avec la façade PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Récupérer les privilèges des documents PDF à l'aide d'Aspose.PDF pour Java
Abstract: Découvrez comment récupérer les privilèges de document avec Aspose.PDF pour Java. L'exemple Java crée un objet PdfFileInfo, lit ses paramètres DocumentPrivilege et imprime les indicateurs d'autorisation pour l'impression, la copie, la modification, les annotations, le remplissage de formulaires, les lecteurs d'écran et l'assemblage.
---
## Obtenez des privilèges sur les documents



Utilisez `PdfFileInfo.getDocumentPrivilege()` pour inspecter les opérations autorisées par le PDF actuel.


### 
Étapes


1. 
Créez un objet `PdfFileInfo` pour le PDF d'entrée.

2. 
Appelez `getDocumentPrivilege()` pour récupérer l'ensemble de privilèges.
3. Lisez les indicateurs booléens pertinents de l'objet `DocumentPrivilege` renvoyé.

4. 
Fermez l'instance `PdfFileInfo` lorsque vous avez terminé.


### 
Exemple Java

```java
public static void getDocumentPrivileges(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    DocumentPrivilege privileges = pdfInfo.getDocumentPrivilege();

    System.out.println("Document Privileges:");
    System.out.println("  Can Print: " + privileges.isAllowPrint());
    System.out.println("  Can Degraded Print: " + privileges.isAllowDegradedPrinting());
    System.out.println("  Can Copy: " + privileges.isAllowCopy());
    System.out.println("  Can Modify Contents: " + privileges.isAllowModifyContents());
    System.out.println("  Can Modify Annotations: " + privileges.isAllowModifyAnnotations());
    System.out.println("  Can Fill In: " + privileges.isAllowFillIn());
    System.out.println("  Can Screen Readers: " + privileges.isAllowScreenReaders());
    System.out.println("  Can Assembly: " + privileges.isAllowAssembly());
    pdfInfo.close();
}
```
