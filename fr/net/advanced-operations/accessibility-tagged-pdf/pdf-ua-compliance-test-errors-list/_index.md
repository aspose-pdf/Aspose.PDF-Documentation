---
title: Test de conformité PDF-UA - Liste des erreurs
linktitle: Test de conformité PDF-UA - Liste des erreurs
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /fr/net/pdf-ua-compliance-test-errors-list/
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
    "headline": "PDF-UA Compliance Test - Errors List",
    "alternativeHeadline": "Comprehensive Error List for PDF-UA Compliance Testing",
    "abstract": "Découvrez la nouvelle fonctionnalité de test de conformité PDF-UA qui simplifie l'identification des erreurs lors des tests de conformité PDF/UA avec l'API Aspose.PDF. Cette fonctionnalité fournit une liste complète des messages d'erreur classés par type, permettant aux développeurs de résoudre efficacement les problèmes et d'assurer la conformité en matière d'accessibilité dans leurs documents PDF. Améliorez votre processus de développement avec des informations claires sur les erreurs de conformité courantes, des problèmes généraux aux validations spécifiques des graphiques et du texte.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF-UA compliance, Aspose.PDF API, compliance testing errors, document generation, C# PDF handling, PDF/UA errors list, PDF validation messages, accessibility compliance, PDF error codes, structured document compliance",
    "wordcount": "1372",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "dateModified": "2024-11-25",
    "description": "Cet article présente une liste des erreurs qui peuvent survenir lors des tests de conformité PDF/UA en utilisant l'API Aspose.PDF et C# ou VB."
}
</script>

Lors des tests de conformité PDF/UA utilisant l'API Aspose.PDF, vous pourriez être intéressé par les messages d'erreur que vous pouvez obtenir. Ces erreurs sont de différents types tels que Général, Texte, Polices, Titres, et plusieurs autres. Les informations sur ces erreurs peuvent être utiles pour connaître la cause exacte des erreurs et leur gestion.

Dans cet article, nous listons les erreurs qui peuvent survenir lors des tests de conformité PDF/UA en utilisant l'API.

## **Général**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|5:1|Erreur|Identifiant PDF/UA manquant|
|6.2:1.1|Erreur|Arbre parent structurel : entrée incohérente trouvée|
|7.1:1.1(14.8.1)|Erreur|Le document n'est pas marqué comme étiqueté|
|7.1:1.1(14.8)|Erreur|L'objet [OBJECT_NAME] n'est pas étiqueté|
|7.1:1.2(14.8.2.2)|Erreur|Artefact présent à l'intérieur du contenu étiqueté|
|7.1:1.3(14.8.2.2)|Erreur|Contenu étiqueté présent à l'intérieur d'un artefact|
|7.1:2.1|Avertissement|Arbre de structure manquant|
|7.1:2.2|Avertissement|Élément de structure ‘Document’ trouvé qui n'est pas un élément racine|
|7.1:2.3|Avertissement|L'élément de structure ‘[ELEMENT_NAME]’ utilisé comme élément racine|
|7.1:2.4.1|Avertissement|Utilisation possiblement inappropriée d'un élément de structure ‘[ELEMENT_NAME]’|
|7.1:2.4.2|Erreur|Utilisation invalide d'un élément de structure ‘[ELEMENT_NAME]’|
|7.1:2.5|Avertissement|Possiblement mauvaise imbrication de l'élément struct ‘[ELEMENT_NAME]’ dans StructTreeRoot|
|7.1:3(14.8.4)|Erreur|Type de structure non standard ‘[TYPE_NAME]’ n'est mappé ni à un type de structure standard ni à un autre type de structure non standard|
|7.1:4(14.8.4)|Avertissement|Type de structure standard ‘[TYPE_NAME]’ est remappé à ‘[TYPE_NAME]’|
|7.1:5|Vérification manuelle nécessaire|Contraste des couleurs|
|7.1:6.1|Erreur|Métadonnées XMP manquantes dans le document|
|7.1:6.2|Erreur|Titre manquant dans les métadonnées XMP du document|
|7.1:6.3|Avertissement|Titre vide dans les métadonnées XMP du document|
|7.1:7.1(12.2)|Avertissement|Dictionnaire ‘ViewerPreferences’ manquant|
|7.1:7.2(12.2)|Erreur|L'entrée ‘DisplayDocTitle’ n'est pas définie|
|7.1:8(14.7.1)|Erreur|L'entrée ‘Suspects’ est définie|
|7.1:9.1(14.7)|Erreur|Clé ‘StructParents’ manquante dans la page|
|7.1:9.2(14.7)|Erreur|Entrée ‘StructParent’ manquante dans l'annotation|
|7.1:9.3(14.7)|Erreur|Entrée pour les ‘StructParents’ donnés non trouvée|

## **Texte**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.2:1|Vérification manuelle nécessaire|Ordre de lecture logique|
|7.2:2(14.8.2.4.2)|Erreur|Les caractères dans un objet texte ne peuvent pas être mappés à Unicode|
|7.2:3.1(14.9.2.2)|Erreur|La langue naturelle pour l'objet texte ne peut pas être déterminée|
|7.2:3.2(14.9.2.2)|Erreur|La langue naturelle du texte alternatif ne peut pas être déterminée|
|7.2:3.3(14.9.2.2)|Erreur|La langue naturelle du texte réel ne peut pas être déterminée|
|7.2:3.4(14.9.2.2)|Erreur|La langue naturelle du texte d'expansion ne peut pas être déterminée|
|7.2:4(14.9.4)|Erreur|Caractère extensible non étiqueté utilisant ActualText|

## **Polices**

|**Clause**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.21.3.1|Erreur|La collection de caractères dans CIDFont n'est pas compatible avec la collection de caractères de CMap interne|
|7.21.3.2|Erreur|CIDToGIDMap n'est pas intégré ou incomplet dans la police ‘[FONT_NAME]’|
|7.21.3.2|Erreur|CMap n'est pas intégré pour la police ‘[FONT_NAME]’|
|7.21.4.2|Erreur|CIDSet est manquant ou incomplet pour la police ‘[FONT_NAME]’|
|7.21.4.2|Erreur|Glyphes manquants dans la police intégrée ‘[FONT_NAME]’|
|7.21.6|Erreur|La police TrueType non symbolique ‘[FONT_NAME]’ n'a pas d'entrées cmap|
|7.21.6|Erreur|L'entrée d'encodage est interdite pour la police TrueType symbolique ‘[FONT_NAME]’|
|7.21.6|Erreur|Un encodage incorrect est utilisé pour la police TrueType ‘[FONT_NAME]’|
|7.21.6|Erreur|Tableau “Differences” incorrect pour la police TrueType non symbolique ‘[FONT_NAME]’|

## **Graphiques**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.3:1(14.8.4.5)|Erreur|L'élément ‘[ELEMENT_NAME]’ sur une seule page sans boîte englobante|
|7.3:2|Erreur|Texte alternatif manquant pour l'élément de structure ‘[ELEMENT_NAME]’|
|7.3:3|Erreur|Légende accompagnant la figure manquante|
|7.3:4(14.8.4.5)|Erreur|L'objet graphique apparaît entre les opérateurs BT et ET|

## **Titres**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.4.2:1|Erreur|Le premier titre n'est pas au premier niveau|
|7.4.2:2|Erreur|Le titre numéroté saute un ou plusieurs niveaux de titre|
|7.4.4:1|Erreur|Éléments de structure ‘H’ et ‘Hn’ trouvés|
|7.4.4:2|Erreur|Plus d'un élément de structure ‘H’ à l'intérieur de l'élément de structure parent|

## **Tables**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.5:1|Avertissement|Ligne de table irrégulière|
|7.5:2|Erreur|La cellule d'en-tête de table n'a pas de sous-cellules associées|
|7.5:3.1|Avertissement|En-têtes de table manquants|
|7.5:3.2|Avertissement|Résumé de table manquant|

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
|7.10:1|Erreur|‘Name’ manquant dans le dictionnaire de configuration du contenu optionnel|
|7.10:2|Erreur|Le dictionnaire de configuration du contenu optionnel contient la clé ‘AS’|

## **Fichiers intégrés**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.11:1|Erreur|Clé ‘F’ ou ‘UF’ manquante dans la spécification du fichier|
|7.11:2|Avertissement|Clé ‘Desc’ manquante dans la spécification du fichier|

## **Signatures numériques**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.13:1|Erreur|Le champ de formulaire de signature ‘[FIELD_NAME]’ ne respecte pas la spécification|
|7.13:2.1|Erreur|La langue naturelle d'un nom alternatif d'un champ de formulaire ‘[FIELD_NAME]’ ne peut pas être déterminée|
|7.13:2.2|Erreur|L'entrée de nom alternatif manquante dans le champ de formulaire ‘[FIELD_NAME]’|

## **Formulaires non interactifs**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.14:1|Erreur|Attribut ‘PrintField’ manquant dans l'élément de formulaire non interactif|

## **XFA**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.15:1|Erreur|Le PDF contient un formulaire XFA dynamique|

## **Sécurité**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.16:1(7.6.3.2)|Erreur|Les paramètres de sécurité bloquent les technologies d'assistance d'accéder au contenu du document|
|7.16:2(7.6.3.2)|Erreur|La conversion n'est pas autorisée par les restrictions de permission|

## **Navigation**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.17:1|Erreur|Erreur des contours du document|
|7.17:2|Erreur|La langue naturelle des contours peut être déterminée|
|7.17:3|Vérification manuelle nécessaire|Étiquettes de page sémantiquement appropriées|

## **Annotations**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.18.1:1|Erreur|La langue naturelle de l'entrée de contenu ne peut pas être déterminée|
|7.18.1:2|Erreur|Description alternative manquante pour une annotation|
|7.18.1:3|Erreur|L'annotation n'est pas imbriquée à l'intérieur d'un élément de structure ‘Annot’|
|7.18.2:1|Erreur|Une annotation avec un sous-type non défini dans l'ISO 32000 ne respecte pas 7.18.1|
|7.18.2:2|Erreur|Une annotation de sous-type TrapNet existe|
|7.18.3:1|Erreur|L'entrée d'ordre d'onglet dans la page avec des annotations n'est pas définie sur 'S' (Structure)|
|7.18.4:1|Erreur|L'annotation ‘Widget’ n'est pas imbriquée à l'intérieur d'un élément de structure ‘Form’|
|7.18.5:1|Erreur|L'annotation ‘Link’ n'est pas imbriquée à l'intérieur d'un élément de structure ‘Link’|
|7.18.6.2:1|Erreur|La clé CT est manquante dans le dictionnaire de données du clip média|
|7.18.6.2:2|Erreur|La clé Alt est manquante dans le dictionnaire de données du clip média|
|7.18.7:1|Erreur|Annotation de pièce jointe de fichier. Clé ‘F’ ou ‘UF’ manquante dans la spécification du fichier|
|7.18.7:2|Avertissement|Annotation de pièce jointe de fichier. Clé ‘Desc’ manquante dans la spécification du fichier|
|7.18.8:1|Erreur|Une annotation PrinterMark est incluse dans la structure logique|
|7.18.8:2|Erreur|Le flux d'apparence d'une annotation PrinterMark n'est pas marqué comme Artefact|

## **Actions**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.19:1|Vérification manuelle nécessaire|Des actions ont été trouvées. Besoin de vérifier les actions selon la spécification PDF/UA manuellement|

## **XObjects**

|**Code**|**Sévérité**|**Message**|
| :- | :- | :- |
|7.20:1|Erreur|L'objet XObject de référence ne doit pas être utilisé dans un fichier PDF/UA conforme|
|7.20:2|Erreur|Le contenu de l'objet XObject de formulaire n'est pas incorporé dans les éléments de structure|

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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
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
    "applicationCategory": "PDF Manipulation Library for .NET",
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