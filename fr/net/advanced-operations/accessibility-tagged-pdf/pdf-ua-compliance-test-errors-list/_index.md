---
title: Test de conformité PDF-UA - Liste des erreurs
linktitle: Test de conformité PDF-UA - Liste des erreurs
type: docs
weight: 50
url: fr/net/pdf-ua-compliance-test-errors-list/
description: Cet article présente une liste des erreurs qui peuvent survenir lors des tests de conformité PDF/UA en utilisant l'API Aspose.PDF et C# ou VB.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Test de conformité PDF-UA - Liste des erreurs",
    "alternativeHeadline": "Tests de conformité PDF/UA en utilisant l'API",
    "author": {
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, génération de documents",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/pdf-ua-compliance-test-errors-list/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-ua-compliance-test-errors-list/"
    },
    "dateModified": "2022-02-04",
    "description": "Cet article présente une liste des erreurs qui peuvent survenir lors des tests de conformité PDF/UA en utilisant l'API Aspose.PDF et C# ou VB."
}
</script>

En effectuant des tests de conformité PDF/UA en utilisant l'API Aspose.PDF, vous pourriez être intéressé par les messages d'erreur que vous pouvez obtenir. Ces erreurs sont de différents types tels que Général, Texte, Polices, Titres, et plusieurs autres. Les informations sur ces erreurs peuvent être utiles pour connaître la cause exacte des erreurs et leur gestion.

Dans cet article, nous listons les erreurs qui peuvent survenir lors des tests de conformité PDF/UA en utilisant l'API.

## **Général**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|5:1|Erreur|Identifiant PDF/UA manquant|
|6.2:1.1|Erreur|Arbre parent structurel : Entrée incohérente trouvée|
|7.1:1.1(14.8.1)|Erreur|Le document n'est pas marqué comme étiqueté|
|7.1:1.1(14.8)|Erreur|L'objet [OBJECT_NAME] n'est pas étiqueté|
|7.1:1.2(14.8.2.2)|Erreur|Artéfact présent à l'intérieur du contenu étiqueté|
|7.1:1.3(14.8.2.2)|Erreur|Contenu étiqueté présent à l'intérieur d'un artéfact|
|7.1:2.1|Avertissement|Arbre de structure manquant|
|7.1:2.2|Avertissement|Élément de structure ‘Document’ trouvé qui n'est pas un élément racine|
|7.1:2.3|Avertissement|Élément de structure ‘[ELEMENT_NAME]’ utilisé comme élément racine|
|7.1:2.3|Warning|L'élément de structure ‘[ELEMENT_NAME]’ utilisé comme élément racine|
|7.1:2.4.1|Warning|Utilisation potentiellement inappropriée d’un élément de structure ‘[ELEMENT_NAME]’|
|7.1:2.4.2|Error|Utilisation invalide d’un élément de structure ‘[ELEMENT_NAME]’|
|7.1:2.5|Warning|Imbrication potentiellement incorrecte de l’élément structuré ‘[ELEMENT_NAME]’ dans StructTreeRoot|
|7.1:3(14.8.4)|Error|Le type de structure non standard ‘[TYPE_NAME]’ n’est mappé ni à un type de structure standard ni à un autre type de structure non standard|
|7.1:4(14.8.4)|Warning|Le type de structure standard ‘[TYPE_NAME]’ est remappé à ‘[TYPE_NAME]’|
|7.1:5|Need check manual|Contraste de couleur|
|7.1:6.1|Error|Métadonnées XMP manquantes dans le document|
|7.1:6.2|Error|Titre manquant dans les métadonnées XMP du document|
|7.1:6.3|Warning|Le titre est vide dans les métadonnées XMP du document|
|7.1:7.1(12.2)|Warning|Le dictionnaire ‘ViewerPreferences’ manquant|
|7.1:7.2(12.2)|Error|L’entrée ‘DisplayDocTitle’ n’est pas définie|
|7.1:8(14.7.1)|Error|L’entrée ‘Suspects’ est définie|
|7.1:9.1(14.7)|Error|La clé ‘StructParents’ manquante dans la page|
|7.1:9.2(14.7)|Error|L’entrée ‘StructParent’ manquante dans l’annotation|
|7.1:9.2(14.7)|Erreur|L'entrée 'StructParent' est manquante dans l'annotation|
|7.1:9.3(14.7)|Erreur|Entrée pour 'StructParents' donné introuvable|

## **Texte**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.2:1|Vérification manuelle nécessaire|Ordre de lecture logique|
|7.2:2(14.8.2.4.2)|Erreur|Les caractères dans un objet texte ne peuvent pas être mappés à Unicode|
|7.2:3.1(14.9.2.2)|Erreur|La langue naturelle pour l'objet texte ne peut pas être déterminée|
|7.2:3.2(14.9.2.2)|Erreur|La langue naturelle du texte alternatif ne peut pas être déterminée|
|7.2:3.3(14.9.2.2)|Erreur|La langue naturelle du texte réel ne peut pas être déterminée|
|7.2:3.4(14.9.2.2)|Erreur|La langue naturelle du texte d'expansion ne peut pas être déterminée|
|7.2:4(14.9.4)|Erreur|Caractère extensible non tagué utilisant ActualText|

## **Polices**

|**Clause**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.21.3.1|Erreur|La collection de caractères dans CIDFont n'est pas compatible avec la collection de caractères du CMap interne|
|7.21.3.2|Erreur|CIDToGIDMap n'est pas intégré ou est incomplet dans la police ‘[FONT_NAME]’|
|7.21.3.2|Erreur|CMap n'est pas intégré pour la police ‘[FONT_NAME]’|
|7.21.3.2|Erreur|CMap n'est pas intégré pour la police ‘[FONT_NAME]’|
|7.21.4.2|Erreur|CIDSet manquant ou incomplet pour la police ‘[FONT_NAME]’|
|7.21.4.2|Erreur|Glyphes manquants dans la police intégrée ‘[FONT_NAME]’|
|7.21.6|Erreur|La police TrueType non symbolique ‘[FONT_NAME]’ n'a pas d'entrées cmap|
|7.21.6|Erreur|Entrée d'encodage interdite pour la police TrueType symbolique ‘[FONT_NAME]’|
|7.21.6|Erreur|Encodage incorrect utilisé pour la police TrueType ‘[FONT_NAME]’|
|7.21.6|Erreur|Tableau “Differences” incorrect pour la police TrueType non symbolique ‘[FONT_NAME]’|

## **Graphiques**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.3:1(14.8.4.5)|Erreur|Élément ‘[ELEMENT_NAME]’ sur une seule page sans boîte englobante|
|7.3:2|Erreur|Texte alternatif manquant pour l'élément de structure ‘[ELEMENT_NAME]’|
|7.3:3|Erreur|Légende accompagnant la figure manquante|
|7.3:4(14.8.4.5)|Erreur|Objet graphique apparaît entre les opérateurs BT et ET|

## **Titres**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.4.2:1|Erreur|Le premier titre n'est pas au premier niveau|
|7.4.2:2|Erreur|Titre numéroté saute un ou plusieurs niveaux de titres|
|7.4.2:2|Erreur|Les titres numérotés sautent un ou plusieurs niveaux de titres|
|7.4.4:1|Erreur|Éléments de structure ‘H’ et ‘Hn’ trouvés|
|7.4.4:2|Erreur|Plus d'un élément de structure ‘H’ à l'intérieur de l'élément de structure parent|

## **Tables**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.5:1|Avertissement|Ligne de tableau irrégulière|
|7.5:2|Erreur|La cellule d'en-tête du tableau n'a pas de sous-cellules associées|
|7.5:3.1|Avertissement|En-têtes de tableau manquants|
|7.5:3.2|Avertissement|Résumé du tableau manquant|

## **Listes**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.6:1|Erreur|L'élément de structure ‘LI’ doit être un enfant de l'élément ‘L’|
|7.6:2|Erreur|Les éléments de structure ‘Lbl’ et ‘LBody’ doivent être des enfants de l'élément ‘LI’|

## **Notes et références**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.9:2.1|Erreur|ID manquant dans l'élément de structure ‘Note’|
|7.9:2.2|Erreur|L'entrée ID dans l'élément de structure ‘Note’ n'est pas unique|

## **Contenu optionnel**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.10:1|Erreur|‘Nom’ manquant dans le dictionnaire de configuration du contenu optionnel|
|7.10:1|Error|Le nom est manquant dans le dictionnaire de configuration de contenu optionnel|
|7.10:2|Error|Le dictionnaire de configuration de contenu optionnel contient la clé ‘AS’|

## **Fichiers intégrés**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.11:1|Error|Clé ‘F’ ou ‘UF’ manquante dans la spécification du fichier|
|7.11:2|Warning|Clé ‘Desc’ manquante dans la spécification du fichier|

## **Signatures numériques**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.13:1|Error|Le champ de signature ‘[FIELD_NAME]’ ne conforme pas à la spécification|
|7.13:2.1|Error|La langue naturelle d'un nom alternatif d'un champ de formulaire ‘[FIELD_NAME]’ ne peut pas être déterminée|
|7.13:2.2|Error|Entrée de nom de champ alternatif manquante dans le champ de formulaire ‘[FIELD_NAME]’|

## **Formulaires non interactifs**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.14:1|Error|Attribut ‘PrintField’ manquant dans l'élément de formulaire non interactif|

## **XFA**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.15:1|Error|Le PDF contient un formulaire XFA dynamique|

## **Sécurité**

|**Code**|**Severity**|**Message**|
|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.16:1(7.6.3.2)|Error|Les paramètres de sécurité empêchent les technologies d'assistance d'accéder au contenu du document|
|7.16:2(7.6.3.2)|Error|La conversion n'est pas autorisée en raison des restrictions de permission|

## **Navigation**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.17:1|Error|Erreur des contours du document|
|7.17:2|Error|La langue naturelle des contours ne peut pas être déterminée|
|7.17:3|Need manual check|Étiquettes de pages sémantiquement appropriées|

## **Annotations**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.18.1:1|Error|La langue naturelle de l'entrée du contenu ne peut pas être déterminée|
|7.18.1:2|Error|Description alternative manquante pour une annotation|
|7.18.1:3|Error|L'annotation n'est pas imbriquée dans un élément de structure ‘Annot’|
|7.18.2:1|Error|Une annotation avec un sous-type non défini dans l'ISO 32000 ne respecte pas 7.18.1|
|7.18.2:2|Error|Une annotation de sous-type TrapNet existe|
|7.18.3:1|Error|L'entrée d'ordre des onglets dans une page avec des annotations n'est pas réglée sur 'S' (Structure)|
|7.18.4:1|Error|L'annotation ‘Widget’ n'est pas imbriquée dans un élément de structure ‘Form’|
|7.18.4:1|Error|L'annotation « Widget » n'est pas imbriquée dans un élément de structure « Form »|
|7.18.5:1|Error|L'annotation « Link » n'est pas imbriquée dans un élément de structure « Link »|
|7.18.6.2:1|Error|La clé CT est absente du dictionnaire de données du clip média|
|7.18.6.2:2|Error|La clé Alt est absente du dictionnaire de données du clip média|
|7.18.7:1|Error|Annotation de pièce jointe de fichier. Clé « F » ou « UF » manquante dans la spécification du fichier|
|7.18.7:2|Warning|Annotation de pièce jointe de fichier. Clé « Desc » manquante dans la spécification du fichier|
|7.18.8:1|Error|Une annotation PrinterMark est incluse dans la structure logique|
|7.18.8:2|Error|Le flux d'apparence d'une annotation PrinterMark n'est pas marqué comme Artifact|

## **Actions**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.19:1|Need check manual|Des actions ont été trouvées. Besoin de vérifier les actions selon la spécification PDF/UA manuellement|

## **XObjects**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.20:1|Error|L'objet X de référence ne doit pas être utilisé dans un fichier PDF/UA conforme|
|7.20:2|Error|Le contenu de l'objet X de formulaire n'est pas incorporé dans les éléments de structure|
|7.20:2|Erreur|Le contenu du Form XObject n'est pas incorporé dans les éléments de structure|

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

