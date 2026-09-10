---
title: Définir l'indicateur de soumission
linktitle: Définir l'indicateur de soumission
type: docs
weight: 40
url: /java/set-submit-flag/
description: Passez en revue la couverture Java actuelle pour définir un indicateur de soumission sur un bouton de formulaire PDF avec la façade FormEditor dans Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Soumettre la configuration de l'indicateur dans les exemples Java FormEditor
Abstract: L’ensemble d’exemples Java actuel n’expose pas la configuration submit-flag en tant qu’exemple de méthode autonome distinct. Au lieu de cela, cela est démontré avec la configuration de l'URL de soumission dans `setSubmitUrl(...)`.
---
La méthode Java `FormEditorExamples.setSubmitUrl(...)` comprend :


## 
Configurer un indicateur de soumission


1. 
Liez le PDF source à la façade `FormEditor`.

2. 
Définissez l'URL de soumission pour le champ du bouton.

3. 
Définissez l'indicateur de soumission pour le format requis.
4. Enregistrez le document mis à jour.


```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```


Utilisez cet exemple combiné comme workflow Java basé sur la source pour configurer un indicateur de soumission dans ce référentiel.
