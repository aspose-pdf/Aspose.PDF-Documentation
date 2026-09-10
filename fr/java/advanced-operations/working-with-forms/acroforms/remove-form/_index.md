---
title: Supprimer des formulaires d'un PDF en Java
linktitle: Supprimer des formulaires
type: docs
weight: 70
url: /java/remove-form/
description: Supprimez les objets de formulaire des pages PDF à l'aide d'Aspose.PDF pour Java, y compris un nettoyage complet et une suppression ciblée.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Supprimer les ressources de formulaire des pages PDF avec Java
Abstract: Cet article explique comment supprimer les ressources de formulaire des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la suppression de tous les formulaires d’une page et la suppression uniquement des ressources de formulaire Typewriter sélectionnées après avoir filtré la collection de formulaires de page.
---
Ces exemples suppriment les ressources de formulaire d'une page plutôt que de simplement modifier les valeurs des champs.


## 
Supprimer toutes les ressources de formulaire d'une page



Utilisez cet exemple lorsque chaque ressource de formulaire sur une page sélectionnée doit être supprimée en une seule opération.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez au [XFormCollection] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) pour la page cible.
1. Effacez la collection et enregistrez le document mis à jour.


```java
public static void removeAllForms(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        forms.clear();
        document.save(outputFile.toString());
    }
}
```

## 
Supprimer des ressources de formulaire spécifiques



Utilisez cet exemple lorsque seules les ressources de formulaire sélectionnées, telles que les formulaires Typewriter, doivent être supprimées.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Accédez au [XFormCollection] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xformcollection/) pour la page cible.
1. Filtrez les ressources [XForm] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) que vous souhaitez supprimer et supprimez-les de la collection.

1. 
Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void removeSpecifiedForm(Path inputFile, int pageNum, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XFormCollection forms = document.getPages().get_Item(pageNum).getResources().getForms();
        List<String> formNames = new ArrayList<>();
        for (XForm form : forms) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                formNames.add(forms.getFormName(form));
            }
        }
        for (String formName : formNames) {
            forms.delete(formName);
        }
        document.save(outputFile.toString());
    }
}
```
