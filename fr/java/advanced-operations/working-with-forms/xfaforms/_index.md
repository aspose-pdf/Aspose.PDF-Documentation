---
title: Travailler avec des formulaires XFA dans les PDF
linktitle: Formulaires XFA
type: docs
weight: 20
url: fr/java/xfa-forms/
description: Avec Aspose.PDF pour Java, vous pouvez créer un formulaire à partir de zéro, remplir le champ de formulaire dans un document PDF, extraire des données du formulaire, ajouter ou supprimer des champs dans le formulaire existant.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA signifie Architecture de Formulaires XML (XML Forms Architecture). C'est un ensemble de spécifications XML propriétaires initialement conçu pour être utilisé avec des formulaires web en 1999, et qui est devenu disponible pour les PDF depuis.

## Convertir un formulaire XFA dynamique en AcroForm standard

Les formulaires dynamiques sont basés sur une spécification XML connue sous le nom de XFA, l'“Architecture de Formulaires XML”. Il peut également convertir un formulaire XFA dynamique en Acroform standard. Les informations sur le formulaire (en ce qui concerne le PDF) sont très vagues – elles spécifient que des champs existent, avec des propriétés et des événements JavaScript, mais ne spécifient aucun rendu. Les objets du formulaire XFA sont dessinés lors du chargement du document.

Actuellement, le PDF prend en charge deux méthodes différentes pour intégrer des données et des formulaires PDF :

- AcroForms (également connus sous le nom de formulaires Acrobat), introduits et inclus dans la spécification du format PDF 1.2.

- Formulaires Adobe XML Forms Architecture (XFA), introduits dans la spécification du format PDF 1.5 en tant que fonctionnalité optionnelle. (La spécification XFA n'est pas incluse dans la spécification PDF, elle est seulement référencée.)

Il n'est pas possible d'extraire ou de manipuler des pages de formulaires XFA, car le contenu du formulaire est généré à l'exécution (pendant la visualisation du formulaire XFA) au sein de l'application essayant d'afficher ou de rendre le formulaire XFA. Aspose.PDF a une fonctionnalité qui permet aux développeurs de convertir les formulaires XFA en AcroForms standard.

```java
// Charger le formulaire XFA dynamique
Document document = new Document("XFAform.pdf");
// Définir le type des champs de formulaire comme AcroForm standard
document.getForm().setType(FormType.Standard);
// Enregistrer le PDF résultant
document.save("Standard_AcroForm.pdf");
```