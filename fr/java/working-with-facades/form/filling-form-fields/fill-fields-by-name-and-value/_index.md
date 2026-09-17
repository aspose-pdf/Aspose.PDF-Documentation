---
title: Remplissez les champs par nom et valeur
linktitle: Remplissez les champs par nom et valeur
type: docs
weight: 60
url: /java/fill-fields-by-name-and-value/
description: Découvrez comment adapter l'API de remplissage de champs Form Façade en Java pour les mises à jour dynamiques des formulaires nom-valeur.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remplissez plusieurs champs de formulaire PDF à partir de paires nom-valeur en Java
Abstract: L'ensemble d'échantillons Java actuel remplit les champs individuellement avec des appels `fillField(...)` répétés. Cet article montre comment appliquer le même modèle d'API à votre propre collection nom-valeur sans inventer une fonctionnalité de façade distincte qui n'est pas présente dans les exemples de référentiel.
---
La classe Java `FormExamples` remplit directement les champs individuels :


```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```


Si votre application dispose déjà d'un ensemble dynamique de noms et de valeurs de champs, appliquez le même appel `fillField(...)` dans votre propre boucle :


```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```


Il s'agit d'un modèle au niveau de l'application dérivé de la même API Java utilisée dans `FormExamples.fillTextFields(...)` ; le référentiel actuel n'inclut pas de méthode d'assistance dédiée distincte pour le remplissage basé sur une carte.
