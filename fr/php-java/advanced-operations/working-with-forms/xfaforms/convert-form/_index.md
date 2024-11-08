---
title: Convertir un formulaire XFA en AcroForm
linktitle: Convertir un formulaire XFA
type: docs
weight: 10
url: /fr/php-java/convert-form/
description: Cette section explique comment convertir un formulaire XFA en AcroForm avec Aspose.PDF pour PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convertir un formulaire XFA dynamique en AcroForm standard

Les formulaires dynamiques sont basés sur une spécification XML connue sous le nom de XFA, l'« Architecture des formulaires XML ». Il est également possible de convertir un formulaire XFA dynamique en Acroform standard. Les informations concernant le formulaire (en ce qui concerne le PDF) sont très vagues – elles spécifient que des champs existent, avec des propriétés et des événements JavaScript, mais ne spécifient aucun rendu. Les objets du formulaire XFA sont dessinés lors du chargement du document.

Actuellement, le PDF prend en charge deux méthodes différentes pour intégrer des données et des formulaires PDF :

- AcroForms (également connus sous le nom de formulaires Acrobat), introduits et inclus dans la spécification du format PDF 1.2.

- Adobe XML Forms Architecture (XFA) forms, introduites dans la spécification de format PDF 1.5 en tant que fonctionnalité optionnelle. (La spécification XFA n'est pas incluse dans la spécification PDF, elle est seulement référencée.)

Il n'est pas possible d'extraire ou de manipuler des pages de formulaires XFA, car le contenu du formulaire est généré à l'exécution (lors de l'affichage du formulaire XFA) au sein de l'application essayant d'afficher ou de rendre le formulaire XFA. Aspose.PDF a une fonctionnalité qui permet aux développeurs de convertir des formulaires XFA en AcroForms standard.

```php

        // Charger le formulaire XFA
        $document = new Document($inputFile);
        
        // Définir le type de champs de formulaire comme AcroForm standard
        $formType = new FormType();
        $document->getForm()->setType($formType->getStandard());
            
        // Enregistrer le document mis à jour
        $document->save($outputFile);
        
        // Enregistrer le PDF modifié    
        $document->close();
```